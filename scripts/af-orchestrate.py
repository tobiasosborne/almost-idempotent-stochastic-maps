#!/usr/bin/env python3
"""Orchestrate an af (Adversarial Proof Framework) workspace via codex workers.

PROTOCOL (user-mandated, strict — see ~/.claude .../memory/af-verification-protocol.md):
  * This script (the ORCHESTRATOR) only drives the af tree: it dispatches codex prover/
    verifier jobs and reads `af status/jobs/get` for control flow. It NEVER judges a proof's
    correctness and never accepts/challenges itself.
  * PROVERS are codex (gpt-5.6-sol) runs; a prover may build/address multiple nodes.
    Reasoning effort is TIERED per run (user directive 2026-07-09): `--tier creative`
    (the default: prover=ultra, verifier=xhigh) for truly creative/demanding conjectures;
    `--tier routine` (prover=high, verifier=high) for lower-priority mechanical
    elevations (e.g. single-shard corollaries from the parked queue). Fine-grained
    overrides: --prover-effort / --verifier-effort; model override: $CODEX_MODEL.
  * EVERY node is validated ONLY by a FRESH codex verifier — a brand-new `codex exec`
    (independent context) explicitly told that finding a counterexample/gap/error is a BIG
    SUCCESS. Fresh per node; roles never mix; codex used liberally and in parallel.

Flow: one prover build → rounds of {address open challenges (prover) ∥ attack ready nodes
(verifier)} until root node 1 is `validated`, stuck, or max rounds. Bottom-up is enforced:
a node is dispatched to a verifier only once all its children are already `validated`.

Does NOT touch argument/ shards or git — reflecting the final af state into the registry is a
separate (mechanical) orchestrator step. Usage:
  python3 scripts/af-orchestrate.py <id> [--phase all|prove|verify] [--max-rounds N]
                                         [--workers K] [--logdir DIR]
"""
import argparse
import concurrent.futures as cf
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
AF = os.environ.get("AF") or shutil.which("af") or "/home/tobias/Projects/vibefeld/af"
CODEX = "codex"
CODEX_MODEL = os.environ.get("CODEX_MODEL", "gpt-5.6-sol")
# gpt-5.6-sol supported reasoning efforts (codex models cache): low..ultra.
CODEX_EFFORTS = ("low", "medium", "high", "xhigh", "max", "ultra")
# Effort tiers (user directive 2026-07-09): highest thinking for truly creative/demanding
# jobs, lower thinking for lower-priority (mechanical) elevations.
TIERS = {
    "creative": {"prover": "ultra", "verifier": "xhigh"},
    "routine": {"prover": "high", "verifier": "high"},
}
# Deeper reasoning needs more wall-clock before we declare a worker timed out.
_EFFORT_TIMEOUT = {"low": 900, "medium": 1200, "high": 1800, "xhigh": 2400,
                   "max": 3600, "ultra": 3600}


def af(ws, *args, timeout=60):
    r = subprocess.run([AF, *args, "-d", ws], cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    return r.stdout, r.returncode


def af_json(ws, *args):
    out, rc = af(ws, *args, "-f", "json")
    try:
        return json.loads(out)
    except Exception:
        return None


def node_state(ws, nid):
    d = af_json(ws, "get", nid)
    return (d or {}).get("epistemic_state", "?")


def all_node_ids(ws):
    d = af_json(ws, "get", "1", "--subtree")
    if isinstance(d, list):
        return [n["id"] for n in d if "id" in n]
    if isinstance(d, dict) and "id" in d:                      # nested fallback
        ids, stack = [], [d]
        while stack:
            n = stack.pop()
            ids.append(n["id"])
            stack.extend(n.get("children") or [])
        return ids
    return ["1"]


def children_of(ids, nid):
    pref, depth = nid + ".", nid.count(".") + 1
    return [i for i in ids if i.startswith(pref) and i.count(".") == depth]


# Heuristic classification of open-challenge reasons — turns a balloon's challenge dump into an
# actionable signal: a MISSING standard fact (→ provision a byte-matched def) vs a cross-stage DAG
# edge (→ factor at the registry level) vs a possible genuine gap. Order matters: a "sibling/pending"
# mention is the DAG tell even if the reason also says "not in scope".
_CH_BUCKETS = [
    ("DAG / cross-sibling dep  (→ FACTOR the proof into registry sub-lemmas)",
     re.compile(r"sibling|relies (on|entirely)|still pending|pending (sibling|node|child)|cross[- ]?(sibling|dep)", re.I)),
    ("MISSING in-scope fact  (→ PROVISION a byte-matched def / validated dep)",
     re.compile(r"not justified|not established|non[- ]?in[- ]?scope|out of scope|no (declared )?(dependenc|children)|facts not (established|in scope)|requires .*not (established|provided|in scope)|no dependencies or children", re.I)),
]


def classify_open_challenges(ws):
    """Bucket the workspace's open-challenge reasons. Returns (counts:dict, samples:dict)."""
    chs = (af_json(ws, "status") or {}).get("challenges", []) or []
    counts, samples = {}, {}
    for c in chs:
        reason = (c.get("reason") or c.get("summary") or "").strip()
        label = "other / possible genuine gap (read it)"
        for lab, pat in _CH_BUCKETS:
            if pat.search(reason):
                label = lab
                break
        counts[label] = counts.get(label, 0) + 1
        samples.setdefault(label, []).append(f"{c.get('id', '?')}: {reason[:140]}")
    return counts, samples


def _git_porcelain():
    try:
        r = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                           capture_output=True, text=True, timeout=30)
        return r.stdout
    except Exception:
        return ""


def overreach_paths():
    """Working-tree paths under Layers 0/1 (definitions/ + argument/). A codex prover runs with repo-wide
    workspace-write; it must write ONLY inside its proofs/<id>/ af workspace. Any change here means it
    edited ground truth / the registry — that is Claude's job (provision-first), so flag it. Returns the
    set of porcelain lines (status + path) for matching paths."""
    bad = set()
    for ln in _git_porcelain().splitlines():
        if len(ln) < 4:
            continue
        p = ln[3:].strip().strip('"')
        if " -> " in p:                      # rename: take the destination
            p = p.split(" -> ", 1)[1]
        if p.startswith("definitions/") or p.startswith("argument/"):
            bad.add(ln.rstrip())
    return bad


def run_codex(prompt, answer_path, log_path, sandbox="workspace-write", timeout=None,
              effort="xhigh"):
    if timeout is None:
        timeout = _EFFORT_TIMEOUT.get(effort, 1800)
    answer_path = pathlib.Path(answer_path)
    answer_path.parent.mkdir(parents=True, exist_ok=True)
    answer_path.unlink(missing_ok=True)
    with open(log_path, "w") as lf:
        try:
            subprocess.run([CODEX, "exec", "--skip-git-repo-check", "-C", str(ROOT),
                            "-m", CODEX_MODEL,
                            "-c", f'model_reasoning_effort="{effort}"',
                            "-s", sandbox, "-o", str(answer_path), "-"],
                           input=prompt, text=True, stdout=lf, stderr=subprocess.STDOUT,
                           timeout=timeout, cwd=ROOT)
        except subprocess.TimeoutExpired:
            return "TIMEOUT"
    return answer_path.read_text(encoding="utf-8") if answer_path.exists() else ""


# ---------- worker prompts (each codex run is fresh & self-contained) ----------

def _shard_fm(rid):
    p = ROOT / "argument" / "lemmas" / f"{rid}.md"
    fm = {}
    if not p.exists():
        return fm
    lines = p.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].strip() == "---":
        for ln in lines[1:]:
            if ln.strip() == "---":
                break
            if ":" in ln:
                k, v = ln.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm


def deps_groundtruth(rid):
    """Validated upstream results (the shard's `deps:`) the proof MAY cite without re-proving."""
    raw = (_shard_fm(rid).get("deps", "") or "").replace(";", " ").split()
    deps = [d for d in (x.strip() for x in raw) if d]
    if not deps:
        return ""
    rows = "\n".join(f"  - {d}: {_shard_fm(d).get('contract', '')}" for d in deps)
    return ("\nESTABLISHED upstream results (already af-`validated` in their own workspaces — you MAY "
            "cite these as proven lemmas WITHOUT re-proving them; do NOT challenge their truth, only "
            "their correct application here):\n" + rows + "\n")


def ground(rid, ws):
    return (
        f"You are a fresh {CODEX_MODEL} worker with NO prior context. Repo root is your cwd. The af binary is "
        f"`{AF}` (pass `-d {ws}` to EVERY af command). Workspace: {ws}.\n"
        + deps_groundtruth(rid) +
        f"READ THESE FIRST and trust NOTHING you are merely told:\n"
        f"  - argument/lemmas/{rid}.md  — the contract (= af root node 1), the proof sketch, the EXACT "
        f"ALLOWED external inputs, and honesty flags. You may use ONLY what that shard permits.\n"
        f"  - every definitions/<def>.md named in that shard's `defs:` line, and `{AF} defs -d {ws}`.\n"
        f"GROUND TRUTH: the cited definitions (and the registered `af defs`) are byte-matched verbatim to "
        f"local sources under refs/ — they are ALLOWED axioms. Do NOT challenge a definitional fact "
        f"itself (e.g. that the Jordan product ∘ is bilinear and commutative, per def-jordan-product / HOS "
        f"2.3.1); attack only whether the proof's REASONING correctly and validly USES those definitions.\n"
    )


def prover_build_prompt(rid, ws):
    return (
        f"ROLE: PROVER (build). {ground(rid, ws)}"
        f"TASK: construct a rigorous, self-contained, machine-auditable proof TREE for root node 1.\n"
        f"0. Register the allowed vocabulary as af definitions (so verifiers treat it as ground truth): "
        f"for EACH <def-id> on the shard's `defs:` line, run "
        f"`{AF} def-add <def-id> --file definitions/<def-id>.md -d {ws}` (skip any already present in "
        f"`{AF} defs -d {ws}`).\n"
        f"0b. Register EACH established upstream result (the dep(s) listed under 'ESTABLISHED upstream "
        f"results' in your context) as an af EXTERNAL, so verifiers see it in scope: "
        f"`{AF} add-external --name \"<dep-id>\" --source \"imports validated registry lemma "
        f"proofs/<dep-id> — <its contract>\" -d {ws}` (the literal `proofs/<dep-id>` path is REQUIRED so "
        f"the check-refs gate recognises it as a registry import; skip any already in "
        f"`{AF} externals -d {ws}`). In any node that uses a dep, cite it by that exact <dep-id> name. "
        f"Do NOT re-prove deps.\n"
        f"1. `{AF} reap -d {ws}`; `{AF} status -d {ws} -f json` (inspect).\n"
        f"2. If node 1 has no children: `{AF} claim 1 --owner prover-build --role prover -d {ws}`, then "
        f"decompose it with `{AF} refine <parent> \"step A\" \"step B\" ... --owner prover-build -d {ws}` "
        f"(children auto-number 1.1, 1.2, ...; refine deeper for 1.1.1 etc.). Make each node a single "
        f"individually-checkable move that follows from the ALLOWED tools + the definitions + its own "
        f"children. Add depth anywhere a hostile verifier could ask 'why?'. The children of a node must "
        f"logically suffice to establish it.\n"
        f"3. Use ONLY the external inputs the shard explicitly allows; cite each precisely. Invent nothing; "
        f"assume no associativity/positivity/etc. unless the shard permits it.\n"
        f"4. `{AF} release <id> --owner prover-build -d {ws}` for every node you claimed.\n"
        f"You are the prover: do NOT challenge or accept. Final line: a one-paragraph tree summary."
    )


def verifier_prompt(rid, ws, node, owner):
    return (
        f"ROLE: STRICT ADVERSARIAL VERIFIER for node {node} ONLY. {ground(rid, ws)}"
        f"YOUR JOB: try AS HARD AS YOU CAN to BREAK node {node}. FINDING A COUNTEREXAMPLE, A GAP, A HIDDEN "
        f"ASSUMPTION, A MISUSED DEFINITION, OR AN ERROR IS A BIG SUCCESS — that is what you are rewarded "
        f"for. Be hostile; do NOT be charitable; do NOT rubber-stamp.\n"
        f"1. Read it: `{AF} get {node} --full -f json -d {ws}`, its children `{AF} get {node} --subtree -f "
        f"json -d {ws}`, and context `{AF} get {node} --ancestors -d {ws}`.\n"
        f"2. INDEPENDENTLY re-derive / stress-test the claim using the allowed tools + cited definitions "
        f"(byte-matched ground truth — see above) + this node's already-`validated` children. Hunt for: an "
        f"invalid inference; use of a genuinely FORBIDDEN assumption (e.g. associativity or positivity, "
        f"which the shard does NOT allow); a logical gap; a concrete counterexample; children that do not "
        f"actually suffice. Do NOT challenge a byte-matched definitional fact itself (commutativity / "
        f"bilinearity of ∘ are allowed) — only its misuse.\n"
        f"3a. If you find ANY real flaw: `{AF} claim {node} --owner {owner} --role verifier -d {ws}`; "
        f"`{AF} challenge {node} --reason \"<specific concrete objection>\" --target "
        f"<statement|inference|gap|type_error|context|dependencies|scope> --owner {owner} -d {ws}`; "
        f"`{AF} release {node} --owner {owner} -d {ws}`. Then STOP. Final line: `VERDICT challenged {node}`.\n"
        f"3b. ONLY if after a genuine, determined effort you CANNOT break it, AND (node {node} is a leaf OR "
        f"every NON-ARCHIVED child is already epistemic_state=`validated` — archived children are "
        f"removed/superseded sub-steps that do NOT count): `{AF} claim {node} --owner {owner} --role "
        f"verifier -d {ws}`; `{AF} accept {node} --agent {owner} --confirm -d {ws}`; "
        f"`{AF} release {node} --owner {owner} -d {ws}`. Final line: `VERDICT accepted {node}`.\n"
        f"3c. If some child is NOT yet `validated`, do nothing and output `VERDICT blocked {node}`."
    )


def prover_fix_prompt(rid, ws, node, owner):
    return (
        f"ROLE: PROVER (address challenge) for node {node}. {ground(rid, ws)}"
        f"Node {node} has an OPEN verifier challenge. `{AF} get {node} --full -f json -d {ws}` to read the "
        f"challenge(s) and reason(s).\n"
        f"Address it RIGOROUSLY: `{AF} claim {node} --owner {owner} --role prover -d {ws}`, then add bridging "
        f"sub-steps with `{AF} refine {node} \"...\" --owner {owner} -d {ws}` and/or answer with "
        f"`{AF} resolve-challenge {node}:<cid> --owner {owner} -d {ws}` giving a concrete response that "
        f"genuinely closes the objection (no hand-waving). If the verifier is RIGHT and the node is actually "
        f"wrong, FIX the mathematics — do not paper over it. `{AF} release {node} --owner {owner} -d {ws}`.\n"
        f"Final line: what you changed."
    )


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("rid")
    ap.add_argument("--phase", choices=["all", "prove", "verify"], default="all")
    ap.add_argument("--max-rounds", type=int, default=8)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--logdir", default=None)
    # Balloon tripwire: abort early (before spending another round of codex) when the tree is far
    # past any legit size (validated trees this project topped out ~23-26 nodes; balloons hit 75-102),
    # or when the pending set is not shrinking over several rounds with open challenges (thrash, not
    # convergence). Aborting here SAVES the codex quota a doomed run would otherwise burn.
    ap.add_argument("--node-cap", type=int, default=40,
                    help="abort if live (non-archived) node count exceeds this (balloon guard)")
    ap.add_argument("--stuck-rounds", type=int, default=3,
                    help="abort if pending count has not decreased over this many rounds while challenges are open")
    # Prover-overreach guard: a codex prover (repo-wide workspace-write) must write ONLY to its
    # proofs/<id>/ workspace. Twice now provers have edited registry shards / created phantom Layer-1
    # shards / hand-provisioned defs. Abort the moment the prover dirties definitions/ or argument/ so
    # Claude provisions the needed fact properly (byte-matched, correct layer) and re-runs.
    ap.add_argument("--no-overreach-guard", action="store_true",
                    help="disable the guard that aborts when a prover edits definitions/ or argument/")
    # Reasoning-effort tiering (user directive 2026-07-09): highest thinking for truly
    # creative/demanding conjectures, lower thinking for lower-priority mechanical jobs.
    ap.add_argument("--tier", choices=sorted(TIERS), default="creative",
                    help="effort preset: creative = prover ultra / verifier xhigh (default); "
                         "routine = prover high / verifier high (mechanical elevations)")
    ap.add_argument("--prover-effort", choices=CODEX_EFFORTS, default=None,
                    help="override the tier's prover reasoning effort")
    ap.add_argument("--verifier-effort", choices=CODEX_EFFORTS, default=None,
                    help="override the tier's verifier reasoning effort")
    a = ap.parse_args(argv)
    prover_effort = a.prover_effort or TIERS[a.tier]["prover"]
    verifier_effort = a.verifier_effort or TIERS[a.tier]["verifier"]
    rid, ws = a.rid, f"proofs/{a.rid}"
    logdir = pathlib.Path(a.logdir or f"/tmp/af-orch/{rid}")
    logdir.mkdir(parents=True, exist_ok=True)

    def log(m):
        print(f"[af-orch:{rid}] {m}", flush=True)

    if not (ROOT / ws / "ledger").exists():
        log(f"ERROR: no workspace at {ws} (seed it first)")
        return 2

    base_overreach = set() if a.no_overreach_guard else overreach_paths()

    def check_overreach(when):
        if a.no_overreach_guard:
            return None
        new = overreach_paths() - base_overreach
        if not new:
            return None
        log(f"PROVER-OVERREACH ({when}): the prover wrote OUTSIDE its workspace, into Layers 0/1:")
        for x in sorted(new):
            log(f"    {x}")
        return ("PROVER-OVERREACH", f"prover dirtied definitions/ or argument/ during {when}")

    if a.phase in ("all", "prove"):
        log(f"PROVER build dispatch (codex {CODEX_MODEL}, effort={prover_effort}; "
            f"verifiers at {verifier_effort})...")
        out = run_codex(prover_build_prompt(rid, ws), logdir / "prover-build.answer.txt",
                        logdir / "prover-build.log", effort=prover_effort)
        log(f"prover build done: {' '.join(out.split())[-280:]}")
        if check_overreach("prover build"):
            log("ABORTED [PROVER-OVERREACH]: review `git diff`; provision the needed fact YOURSELF "
                "(byte-matched def, correct layer), revert the prover's stray edits, re-seed, re-run.")
            return 3

    if a.phase == "prove":
        log(f"root state: {node_state(ws, '1')}")
        return 0

    pool = cf.ThreadPoolExecutor(max_workers=a.workers)
    pending_hist, abort = [], None
    for rnd in range(a.max_rounds):
        af(ws, "reap")
        s = (af_json(ws, "status") or {}).get("statistics", {})
        es = s.get("epistemic_state", {}) or {}
        root = node_state(ws, "1")
        n_live = (s.get("total_nodes") or 0) - (es.get("archived") or 0)
        n_pend = es.get("pending") or 0
        open_ch = s.get("open_challenges") or 0
        log(f"round {rnd}: root={root}  live={n_live} pending={n_pend} open-ch={open_ch}")
        if root == "validated":
            break
        # --- balloon tripwire: abort BEFORE dispatching this round's codex (saves quota) ---
        pending_hist.append(n_pend)
        if n_live > a.node_cap:
            abort = ("BALLOON", f"{n_live} live nodes > --node-cap {a.node_cap} (DAG forced into one "
                                f"tree, or a missing standard fact being re-derived from scratch)")
            break
        if (len(pending_hist) > a.stuck_rounds and open_ch > 0
                and n_pend >= pending_hist[-1 - a.stuck_rounds]):
            abort = ("STUCK", f"pending not shrinking ({pending_hist[-a.stuck_rounds - 1:]}) over "
                              f"{a.stuck_rounds} rounds with {open_ch} open challenge(s) — thrash, not convergence")
            break
        pj = (af_json(ws, "jobs", "--role", "prover") or {}).get("prover_jobs", [])
        vj = (af_json(ws, "jobs", "--role", "verifier") or {}).get("verifier_jobs", [])
        ids = all_node_ids(ws)
        states = {i: node_state(ws, i) for i in ids}
        # archived children are removed/superseded (e.g. a prover replaced a malformed sub-step);
        # they are NOT live children, so they must not block bottom-up readiness. af's own
        # `jobs --role verifier` already vets the node as reviewable given its live children.
        ready = [j["node_id"] for j in vj
                 if all(states.get(c) in ("validated", "archived")
                        for c in children_of(ids, j["node_id"]))]
        pjids = [j["node_id"] for j in pj]
        log(f"  prover-jobs={pjids}  verifier-ready={ready}  (of {len(vj)} reviewable)")
        if not pjids and not ready:
            log("  no actionable jobs — stuck; stopping.")
            break
        tasks = []
        for n in pjids:
            o = f"pf-{n.replace('.', '_')}-r{rnd}"
            tasks.append(("prover-fix", n, pool.submit(
                run_codex, prover_fix_prompt(rid, ws, n, o),
                logdir / f"fix-{n}-r{rnd}.answer.txt", logdir / f"fix-{n}-r{rnd}.log",
                effort=prover_effort)))
        for n in ready:
            o = f"v-{n.replace('.', '_')}-r{rnd}"
            tasks.append(("verifier", n, pool.submit(
                run_codex, verifier_prompt(rid, ws, n, o),
                logdir / f"verify-{n}-r{rnd}.answer.txt", logdir / f"verify-{n}-r{rnd}.log",
                effort=verifier_effort)))
        for kind, n, fut in tasks:
            tail = " ".join((fut.result() or "").split())[-160:]
            log(f"    {kind} {n}: {tail}")
        ov = check_overreach(f"round {rnd}")
        if ov:
            abort = ov
            break
    pool.shutdown(wait=True)

    final = node_state(ws, "1")
    stats = (af_json(ws, "status") or {}).get("statistics", {})
    log(f"DONE root={final} nodes={stats.get('total_nodes')} epistemic={stats.get('epistemic_state')} "
        f"taint={stats.get('taint_state')}")
    if final != "validated":
        if abort:
            log(f"ABORTED [{abort[0]}]: {abort[1]}")
        counts, samples = classify_open_challenges(ws)
        if counts:
            log("open-challenge classification (what's actually blocking):")
            for lab, c in sorted(counts.items(), key=lambda kv: -kv[1]):
                log(f"  [{c}] {lab}")
                for ex in samples[lab][:3]:
                    log(f"        - {ex}")
        converging = len(pending_hist) >= 2 and pending_hist[-1] < max(pending_hist)
        if abort and abort[0] == "PROVER-OVERREACH":
            log("RECOMMEND: the prover edited Layers 0/1 (`git diff definitions/ argument/`). It hit a "
                "missing fact and tried to provision it itself. Provision that fact YOURSELF as a "
                "byte-matched cited def (correct layer; Rule 6), revert the prover's stray edits, "
                "re-seed the workspace, and re-run. Do NOT reflect this run.")
        elif abort and abort[0] == "BALLOON":
            log("RECOMMEND: do NOT bump rounds — provision any MISSING in-scope fact (a byte-matched "
                "def) and/or FACTOR the proof into registry sub-lemmas, then re-seed + re-orchestrate.")
        elif abort and abort[0] == "STUCK":
            log("RECOMMEND: act on the classification above (provision the missing fact / factor the "
                "DAG edge); re-seed if the fix is structural.")
        elif converging:
            log("RECOMMEND: converging but hit --max-rounds; resume with "
                "`--phase verify --max-rounds <larger>` (no rebuild — continues the existing tree).")
        else:
            log("RECOMMEND: read the open challenge(s) above — likely a genuine gap or a missing input.")
    return 0 if final == "validated" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
