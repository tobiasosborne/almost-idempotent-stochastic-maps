#!/usr/bin/env python3
"""
argument.py — the LINKER for the argument registry (Layer 1, the module graph / DAG).

Enforces the contracts between proof modules and generates the index + dependency graph:
  * acyclic dependency DAG
  * imports resolve (deps -> registry ids; defs -> definitions/ ids)
  * contract match (registry contract == af workspace root conjecture)
  * status propagation (af=validated requires deps validated) + ready-frontier / blocked
  * brittleness (oversized af tree => REFACTOR signal)
  * orphans (registry<->proofs/ workspace correspondence)

Pure check functions (unit-tested in scripts/tests/test_argument.py) take a parsed registry
plus injected "workspace facts"; main() builds those facts from `af ... -f json` + the filesystem.

Usage:
  python3 scripts/argument.py --check       # validate (exit 1 on ERROR)
  python3 scripts/argument.py --generate     # (re)write argument/{INDEX,DAG}.md
  python3 scripts/argument.py --show <id>     # local map of one result: contract, defs,
                                              #   direct deps/routes/dependents, full ancestor/descendant closures
  python3 scripts/argument.py --closure-min <id>  # per-route ancestor closures of a routed (OR-ROUTE) shard
  python3 scripts/argument.py --sync-beads    # mirror registry into beads (idempotent; one issue
                                              #   per result, dep edges = DAG edges, available
                                              #   results closed) so `bd ready` == proof frontier

The whole-DAG map is argument/DAG.md (Mermaid, generated) + argument/INDEX.md (table, generated).
"""
import re
import sys
import json
import shutil
import subprocess
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ARG_DIR = ROOT / "argument"
DEFS_DIR = ROOT / "definitions"
PROOFS_DIR = ROOT / "proofs"
KINDS = {"lemma", "proposition", "theorem", "corollary", "open-problem", "obstruction"}
# 'stated' = asserted (with a proof) in the upstream manuscript, transcribed faithfully, NOT yet
# independently verified in-repo. Distinct from 'proved' (a proof we have checked) and 'cited'
# (literature, byte-matched). This repo audits an existing manuscript, so most results start 'stated'.
# MATH status = the rigour rung of a result (CLAUDE.md L0 rigour ladder).
#   RIGOROUS rungs:     proved (af/independently proved) · cited (byte-matched ground truth) · consensus
#   NON-RIGOROUS rungs:  stated (transcribed, unchecked) · proved-mod-audit (a paper-proof from the
#                        ingested classical-portfolio, NOT yet independently reviewed/af-validated here)
#                        · conjecture · heuristic · numerical (never rigorous — quarantined to runs/)
#                        · open · obstruction · disproved
# The linker treats only `af: validated` or `status: cited` deps as "available", so a rigorous
# (af:validated) result can NEVER rest on a non-rigorous dep — that is the ladder, made mechanical.
MATH_STATUS = {"proved", "cited", "consensus", "open", "obstruction", "disproved", "stated",
               "proved-mod-audit", "conjecture", "heuristic", "numerical"}
NONRIGOROUS_STATUS = {"stated", "proved-mod-audit", "conjecture", "heuristic", "numerical"}
AF_STATES = {"none", "seeded", "validated"}
LIST_FIELDS = ("defs", "deps")
# Brittleness threshold = the ONE shared soft cap (scripts/af_constants.py) also read by
# af-orchestrate.py's balloon guard, so the linker and the orchestrator cannot drift (aism-s64).
_SCRIPTS_DIR = str(pathlib.Path(__file__).resolve().parent)
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)
from af_constants import NODE_SOFT_CAP as NODE_THRESHOLD  # noqa: E402


def normalize(s):
    return " ".join((s or "").split())


def parse_routes(s):
    """Parse the OPTIONAL `routes:` field into a list of routes, each route a conjunctive
    dep-list. Grammar (P0 OR-ROUTE, aism-3ne):

        routes: [dep-a; dep-b] | [dep-c]

    Each bracketed group is ONE route (a conjunction of its members — all must be satisfied
    for that route to fire); groups are separated by `|` (the disjunction — ANY one route
    suffices). Whitespace around `|`, brackets, and `;` is ignored; empty groups are dropped.
    Returns [] for a missing/blank field (backward-compatible: a shard with no routes behaves
    byte-identically to today). Returns e.g. [["dep-a","dep-b"], ["dep-c"]]."""
    s = (s or "").strip()
    if not s:
        return []
    routes = []
    for group in s.split("|"):
        group = group.strip()
        if group.startswith("[") and group.endswith("]"):
            group = group[1:-1]
        members = [x.strip() for x in group.split(";") if x.strip()]
        if members:
            routes.append(members)
    return routes


def route_members(l):
    """Flattened list of every id appearing in any of a shard's routes (with multiplicity)."""
    return [m for r in l.get("routes", []) for m in r]


def all_dep_ids(l):
    """The UNION of unconditional deps + all route members. Used for acyclicity and for the
    (conservative, union-over-routes) ancestor/descendant closures — the 'potentially relevant
    ancestors'. A cycle through ANY route is still a cycle; goal-reachability counts every route's
    members as ancestors. (Per-route closures are available via --closure-min.)"""
    return list(l.get("deps", [])) + route_members(l)


def _parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm = {}
    for line in text[3:end].strip("\n").splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    for f in LIST_FIELDS:
        fm[f] = [x.strip() for x in fm.get(f, "").split(";") if x.strip()]
    # OPTIONAL `routes:` — parsed structurally (not a simple `;`-list); absent -> [] (backward-compat).
    fm["routes"] = parse_routes(fm.get("routes", ""))
    return fm


def parse_registry(arg_dir):
    """Read <arg_dir>/lemmas/*.md -> (lemmas, errors)."""
    arg_dir = pathlib.Path(arg_dir)
    lemmas, errors = [], []
    lemdir = arg_dir / "lemmas"
    for path in sorted(lemdir.glob("*.md")) if lemdir.exists() else []:
        if path.name in ("README.md", "INDEX.md"):
            continue
        fm = _parse_frontmatter(path)
        if fm is None:
            errors.append(f"{path.name}: missing/unterminated frontmatter")
            continue
        if fm.get("id") and fm["id"] != path.stem:
            errors.append(f"{path.name}: id '{fm.get('id')}' != filename stem '{path.stem}'")
        if fm.get("kind") and fm["kind"] not in KINDS:
            errors.append(f"{path.name}: kind '{fm['kind']}' not in {sorted(KINDS)}")
        if fm.get("status") and fm["status"] not in MATH_STATUS:
            errors.append(f"{path.name}: status '{fm['status']}' not in {sorted(MATH_STATUS)}")
        if fm.get("af", "none") not in AF_STATES:
            errors.append(f"{path.name}: af '{fm.get('af')}' not in {sorted(AF_STATES)}")
        lemmas.append(fm)
    return lemmas, errors


# ---------- pure checks ----------

def check_acyclic(lemmas):
    ids = {l["id"] for l in lemmas}
    # Acyclicity is computed over the UNION of deps + all route members (conservative: a cycle
    # hidden in any route — not just the first — is still a cycle).
    adj = {l["id"]: [d for d in all_dep_ids(l) if d in ids] for l in lemmas}
    errors, state = [], {}  # 0=unvisited 1=in-stack 2=done

    def dfs(u, stack):
        state[u] = 1
        for v in adj.get(u, []):
            if state.get(v, 0) == 1:
                cyc = stack[stack.index(v):] + [v]
                errors.append("cycle detected: " + " -> ".join(cyc))
                return True
            if state.get(v, 0) == 0 and dfs(v, stack + [v]):
                return True
        state[u] = 2
        return False

    for l in lemmas:
        if state.get(l["id"], 0) == 0:
            if dfs(l["id"], [l["id"]]):
                break
    return errors


def check_imports(lemmas, def_ids):
    ids = {l["id"] for l in lemmas}
    errors = []
    for l in lemmas:
        for d in l.get("deps", []):
            if d not in ids:
                errors.append(f"{l['id']}: unknown dep '{d}' (not a registry id)")
        for ri, r in enumerate(l.get("routes", []), 1):
            for m in r:
                if m not in ids:
                    errors.append(f"{l['id']}: unknown route member '{m}' "
                                  f"(route {ri}, not a registry id)")
        for df in l.get("defs", []):
            if df not in def_ids:
                errors.append(f"{l['id']}: unknown def '{df}' (not in definitions/)")
    return errors


def check_status(lemmas):
    af_of = {l["id"]: l.get("af", "none") for l in lemmas}
    status_of = {l["id"]: l.get("status") for l in lemmas}
    # A dep is AVAILABLE iff its af is validated OR it is a ground-truth leaf (status=cited:
    # cited background like Kadison's inequality is never af-proven yet is available to build on).
    # Only status=='cited' counts as a leaf — NOT consensus/open/obstruction/disproved/proved.
    def available(d):
        return af_of.get(d, "none") == "validated" or status_of.get(d) == "cited"

    def requirements_met(l):
        """A shard's imports are satisfied iff every unconditional dep is available AND
        (it has no routes, OR at least ONE route's members are ALL available). This is the
        disjunctive (OR-ROUTE) generalisation; a deps-only shard (routes == []) reduces to the
        original 'all deps available' rule byte-for-byte."""
        if not all(available(d) for d in l.get("deps", [])):
            return False
        routes = l.get("routes", [])
        if routes and not any(all(available(m) for m in r) for r in routes):
            return False
        return True

    errors, ready, blocked = [], [], []
    for l in lemmas:
        met = requirements_met(l)
        if l.get("af") == "validated" and not met:
            # Status propagation (the af rule): a validated result can never rest on a non-rigorous
            # dep. With routes, it needs all unconditional deps available AND one FULLY-available route.
            bad = [d for d in l.get("deps", []) if not available(d)]
            if l.get("routes"):
                errors.append(f"{l['id']}: af=validated but no route is fully validated/cited "
                              f"(unconditional bad deps: {bad})")
            else:
                errors.append(f"{l['id']}: af=validated but dep(s) not validated: {bad}")
        if l.get("af", "none") != "validated" and not met:
            blocked.append(l["id"])
        if (l.get("af", "none") in ("none", "seeded")
                and l.get("status") in ("proved", "consensus")
                and met):
            ready.append(l["id"])
    return errors, ready, blocked


def check_contracts(lemmas, ws_contracts):
    by_id = {l["id"]: l for l in lemmas}
    errors = []
    for lid, ws_stmt in ws_contracts.items():
        l = by_id.get(lid)
        if l is None:
            continue
        if normalize(ws_stmt) != normalize(l.get("contract", "")):
            errors.append(f"contract drift: {lid} — af root conjecture != registry contract")
    return errors


def check_brittleness(lemmas, nodecounts, threshold=NODE_THRESHOLD):
    warnings = []
    for l in lemmas:
        nc = nodecounts.get(l["id"])
        if nc is not None and nc > threshold:
            ws = l.get("workspace") or f"proofs/{l['id']}"
            warnings.append(f"REFACTOR: {ws} has {nc} nodes (>{threshold}) "
                            f"— factor {l['id']} into sub-lemmas")
    return warnings


def check_orphans(lemmas, ws_dirs):
    errors = []
    declared = {}
    for l in lemmas:
        ws = l.get("workspace")
        declared[ws] = l["id"]
        if l.get("af", "none") != "none" and ws not in ws_dirs:
            errors.append(f"{l['id']}: af={l.get('af')} but workspace dir missing: {ws}")
    for ws in ws_dirs:
        if ws not in declared:
            errors.append(f"orphan workspace (no registry entry): {ws}")
    return errors


# ---------- beads mirror (--sync-beads) ----------

def _available(l):
    """The linker's availability rule (see check_status): rigorous enough to build on."""
    return l.get("af", "none") == "validated" or l.get("status") == "cited"


def beads_title(l):
    """Stable match key: the registry id as title prefix `<id>: <contract>`."""
    c = normalize(l.get("contract", ""))
    return f"{l['id']}: {c[:90]}" + ("…" if len(c) > 90 else "")


def plan_beads_sync(lemmas, existing):
    """Pure planner: diff the registry against a beads snapshot -> (actions, warnings).

    `existing`: {result_id: {"issue": bd-id, "status": "open"|"closed", "deps": set(result_ids)}}.
    Actions (in execution order — creates, then dep edges, then closes):
      ("create", result_id, title, description, priority)
      ("dep",    result_id, dep_result_id)   # bd: issue(result) depends on / blocked by issue(dep)
      ("close",  result_id, reason)          # result already AVAILABLE (af=validated / cited)
    Idempotent: on a fully-synced state the plan is empty. A closed bd issue whose result is NOT
    available yields a WARNING, never an auto-reopen (a human may have deliberately de-scoped it)."""
    ids = {l["id"] for l in lemmas}
    ordered = sorted(lemmas, key=lambda d: d["id"])
    actions, warnings = [], []
    for l in ordered:
        if l["id"] not in existing:
            prio = 1 if l.get("kind") == "open-problem" else 2
            desc = (f"Establish rigorously (L0): {normalize(l.get('contract', ''))} — shard "
                    f"argument/lemmas/{l['id']}.md; kind={l.get('kind', '?')}, "
                    f"status={l.get('status', '?')}, af={l.get('af', 'none')}. Mirrored from the "
                    f"argument DAG by argument.py --sync-beads; blockers = DAG dep edges.")
            actions.append(("create", l["id"], beads_title(l), desc, prio))
    for l in ordered:
        have = existing.get(l["id"], {}).get("deps", set())
        for d in l.get("deps", []):
            if d in ids and d not in have:
                actions.append(("dep", l["id"], d))
    for l in ordered:
        ex = existing.get(l["id"])
        if _available(l):
            if ex is None or ex["status"] != "closed":
                actions.append(("close", l["id"],
                                f"already rigorous: status={l.get('status')}, af={l.get('af', 'none')}"))
        elif ex is not None and ex["status"] == "closed":
            warnings.append(f"{l['id']}: bd issue {ex['issue']} is closed but the result is NOT "
                            f"rigorous (status={l.get('status')}, af={l.get('af', 'none')}) — "
                            f"reopen manually if still in scope")
    return actions, warnings


def _bd(cli_args, timeout=60):
    return subprocess.run(["bd"] + cli_args, capture_output=True, text=True, timeout=timeout)


def beads_snapshot(registry_ids, bd=_bd):
    """Snapshot bd state for the mirror: {result_id: {issue, status, deps:set(result_id)}}.
    Match key = title prefix `<id>: `. bd calls are strictly serialized (exclusive Dolt lock).
    --limit 0 is load-bearing: bd's default limit (50) would silently truncate the snapshot on a
    grown tracker, making mirrored results look missing and re-creating them (duplicates)."""
    p = bd(["list", "--all", "--json", "--limit", "0"])
    issues = json.loads(p.stdout) if p.stdout.strip() else []
    existing, rid_of_issue = {}, {}
    for it in issues:
        rid = it.get("title", "").split(":", 1)[0].strip()
        if rid in registry_ids:
            status = "closed" if it.get("status") == "closed" else "open"
            existing[rid] = {"issue": it["id"], "status": status, "deps": set()}
            rid_of_issue[it["id"]] = rid
    for rid, e in sorted(existing.items()):
        p = bd(["dep", "list", e["issue"], "--json", "--type", "blocks"])
        try:
            deps = json.loads(p.stdout) if p.stdout.strip() else []
        except json.JSONDecodeError:
            deps = []  # unparseable -> plan re-adds; bd tolerates duplicates
        for d in deps if isinstance(deps, list) else []:
            # the mirror manages ONLY blocks edges; a relates-to/tracks edge between two mirror
            # issues must not suppress a needed blocks edge (belt-and-braces with --type above)
            if isinstance(d, dict) and d.get("dependency_type", "blocks") != "blocks":
                continue
            did = d.get("id") if isinstance(d, dict) else d
            if did in rid_of_issue:
                e["deps"].add(rid_of_issue[did])
    return existing


def sync_beads(lemmas):
    """Execute the plan against bd, strictly serialized. Returns 0 on success."""
    if not shutil.which("bd"):
        print("[--sync-beads] bd not found on PATH — skipped")
        return 1
    existing = beads_snapshot({l["id"] for l in lemmas})
    actions, warnings = plan_beads_sync(lemmas, existing)
    issue_of = {rid: e["issue"] for rid, e in existing.items()}
    counts = {"create": 0, "dep": 0, "close": 0}
    for act in actions:
        if act[0] == "create":
            _, rid, title, desc, prio = act
            p = _bd(["create", "--title", title, "--description", desc,
                     f"--priority={prio}", "--type=task", "-l", "dag-mirror"])
            m = re.search(r"Created issue:\s*(\S+)", p.stdout)
            if p.returncode != 0 or not m:
                print(f"[--sync-beads] ERROR creating {rid}: {p.stderr.strip() or p.stdout.strip()}")
                return 1
            issue_of[rid] = m.group(1)
        elif act[0] == "dep":
            _, rid, dep = act
            p = _bd(["dep", "add", issue_of[rid], issue_of[dep]])
            dup = any(t in (p.stdout + p.stderr).lower() for t in ("exist", "duplicate"))
            if p.returncode != 0 and not dup:
                print(f"[--sync-beads] ERROR dep {rid} -> {dep}: {p.stderr.strip()}")
                return 1
        else:
            _, rid, reason = act
            p = _bd(["close", issue_of[rid], "--reason", reason])
            if p.returncode != 0:
                print(f"[--sync-beads] ERROR closing {rid}: {p.stderr.strip()}")
                return 1
        counts[act[0]] += 1
    for w in warnings:
        print(f"[--sync-beads] WARN {w}")
    print(f"[--sync-beads] synced: {counts['create']} created, {counts['dep']} dep edges, "
          f"{counts['close']} closed ({len(lemmas)} results mirrored)")
    return 0


# ---------- node map: ancestor/descendant closures (--show) ----------

def _closure(lemmas, root, reverse):
    """Transitive set reachable from `root` along dependency edges (reverse=False) or reverse
    dependency edges (reverse=True). Edges = the UNION of deps + all route members (so the
    ancestor closure is the 'potentially relevant ancestors' over ALL routes — the conservative
    goal-reachability set; per-route closures are separate, see route_closures / --closure-min).
    Excludes `root`; ignores dangling deps (check_imports reports those). Returns None if `root`
    is not a registry id."""
    by = {l["id"]: l for l in lemmas}
    if root not in by:
        return None
    if reverse:
        adj = {i: [] for i in by}
        for l in lemmas:
            for d in all_dep_ids(l):
                if d in by:
                    adj[d].append(l["id"])
    else:
        adj = {i: [d for d in all_dep_ids(by[i]) if d in by] for i in by}
    seen, stack = set(), list(adj[root])
    while stack:
        n = stack.pop()
        if n in seen:
            continue
        seen.add(n)
        stack.extend(adj.get(n, []))
    seen.discard(root)  # exclude root even if a cycle through it sneaks in (--show runs pre-acyclic-check)
    return seen


def deps_closure(lemmas, root):
    """All transitive prerequisites of `root` (the ancestors it depends on)."""
    return _closure(lemmas, root, reverse=False)


def dependents_closure(lemmas, root):
    """All transitive dependents of `root` (the descendants that rely on it)."""
    return _closure(lemmas, root, reverse=True)


def route_closures(lemmas, root):
    """Per-route ancestor closures of a routed shard. Returns a list of (route_index, members,
    closure_set) — one entry per route — where closure_set is the transitive ancestor set reached
    by treating THAT route's members (plus the shard's unconditional deps) as the only edges out of
    `root`. Empty list if `root` is unknown or has no routes. This makes the disjunction legible:
    each entry is one self-contained way to discharge `root`."""
    by = {l["id"]: l for l in lemmas}
    if root not in by or not by[root].get("routes"):
        return []
    base = list(by[root].get("deps", []))
    out = []
    for i, r in enumerate(by[root]["routes"], 1):
        # transitive closure over full deps edges, but with `root`'s outgoing edges = base + this route
        seen, stack = set(), [d for d in base + list(r) if d in by]
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n)
            stack.extend(d for d in all_dep_ids(by[n]) if d in by)
        seen.discard(root)
        out.append((i, list(r), seen))
    return out


def format_show(lemmas, root):
    """Human-readable local map of one result: its contract, direct defs/deps,
    direct dependents, and the full ancestor/descendant closures."""
    by = {l["id"]: l for l in lemmas}
    if root not in by:
        return (f"unknown id '{root}' — not a registry result. "
                f"List them with: python3 scripts/argument.py (or see argument/INDEX.md).")
    l = by[root]

    def tag(i):
        x = by.get(i)
        return f"{i}[{x.get('status','?')}/{x.get('af','none')}]" if x else f"{i}[MISSING]"

    direct_deps = l.get("deps", [])
    # route members count as consumers/consumed too (union edge set)
    direct_dependents = sorted(i for i in by if root in all_dep_ids(by[i]))
    anc = sorted(deps_closure(lemmas, root))
    desc = sorted(dependents_closure(lemmas, root))
    lines = [
        f"# {root}  [{l.get('status','?')}/{l.get('af','none')}]  "
        f"kind={l.get('kind','?')}  owner={l.get('owner','-')}",
        f"contract: {l.get('contract','')}",
        f"defs:        {'; '.join(l.get('defs', [])) or '(none)'}",
        f"deps (direct prerequisites): {', '.join(tag(d) for d in direct_deps) or '(none)'}",
    ]
    for i, members in enumerate(l.get("routes", []), 1):
        lines.append(f"route {i} (OR; all-of): {', '.join(tag(m) for m in members) or '(none)'}")
    lines += [
        f"dependents (direct):         {', '.join(tag(d) for d in direct_dependents) or '(none)'}",
        f"ancestors   (all {len(anc)} prerequisites): {', '.join(anc) or '(none)'}",
        f"descendants (all {len(desc)} dependents):   {', '.join(desc) or '(none)'}",
    ]
    return "\n".join(lines)


# ---------- integration (filesystem + af) ----------

def load_def_ids():
    ids = set()
    for p in DEFS_DIR.glob("*.md") if DEFS_DIR.exists() else []:
        if p.name in ("README.md", "INDEX.md"):
            continue
        fm = _parse_frontmatter(p)
        if fm and fm.get("id"):
            ids.add(fm["id"])
    return ids


def scan_workspaces():
    if not PROOFS_DIR.exists():
        return set()
    return {f"proofs/{d.name}" for d in PROOFS_DIR.iterdir()
            if d.is_dir() and (d / "ledger").exists()}


def af_introspect(workspace):
    """Return {'contract':str,'nodes':int,'epistemic':str,'clean':bool} or None."""
    ws = ROOT / workspace
    if not shutil.which("af") or not (ws / "ledger").exists():
        return None
    try:
        root = json.loads(subprocess.run(["af", "get", "1", "-d", str(ws), "-f", "json"],
                                          capture_output=True, text=True, timeout=30).stdout)
        st = json.loads(subprocess.run(["af", "status", "-d", str(ws), "-f", "json"],
                                       capture_output=True, text=True, timeout=30).stdout)
    except Exception:
        return None
    stats = st.get("statistics", {})
    epi = stats.get("epistemic_state", {})
    return {"contract": root.get("statement", ""),
            "nodes": stats.get("total_nodes", 0),
            "epistemic": root.get("epistemic_state", ""),
            "clean": stats.get("taint_state", {}).get("clean", 0) == stats.get("total_nodes", -1)}


# proof-status colour classes (most-solid first); each node gets exactly one class.
CLASSDEFS = [
    ("validated", "fill:#b7f7c2,stroke:#1a7f37,color:#0b3d18"),
    ("proved",    "fill:#cfe3ff,stroke:#0969da,color:#0a3069"),
    ("seeded",    "fill:#fff3c4,stroke:#bf8700,color:#5a4500"),
    ("stated",    "fill:#eaecef,stroke:#8b949e,color:#24292f"),
    ("cited",     "fill:#e7d6ff,stroke:#8250df,color:#3b1a73"),
    ("nonrigorous", "fill:#ffe8cc,stroke:#d97706,color:#7a3d00,stroke-dasharray:4 2"),
    ("open",      "fill:#ffd6d6,stroke:#cf222e,color:#6e1119,stroke-dasharray:5 3"),
]
# OR-route junction nodes (id__routeN) are rendered in this distinct pill style.
ROUTE_CLASSDEF = ("routejct", "fill:#fbe7ff,stroke:#8250df,color:#3b1a73,stroke-dasharray:2 2")
GEN_HEADER = "<!-- GENERATED by scripts/argument.py --generate. Do not hand-edit. -->\n"
# OR-ROUTE rendering (aism-3ne): a shard with a `routes:` field draws, per route i, a rhombus
# junction node `<id>__routeI` labelled "route i"; each route MEMBER feeds that junction with a
# solid edge (member --> id__routeI, the conjunction), and the junction feeds the shard with a
# DASHED "OR" edge (id__routeI -. OR .-> id, the disjunction). Unconditional deps draw ordinary
# solid edges straight to the shard. So: solid = required; dashed OR = "any one route suffices".
DAG_ROUTE_NOTE = ("<!-- OR-routes: `<id>__routeN` rhombus = one alternative route; solid edges into "
                  "it are that route's conjunctive members; the dashed `OR` edge into `<id>` means "
                  "any single route suffices. Unconditional deps draw plain solid edges. -->\n")
LEGEND = ("**Proof-status legend:** 🟩 validated · 🟦 proved · 🟨 seeded · "
          "⬜ stated · 🟪 cited · 🟧 proved-mod-audit/conjecture/heuristic/numerical (NON-rigorous) · 🟥 open")


def proof_class(l):
    """The single proof-status colour class for a result (most-solid wins). A non-rigorous STATUS
    (proved-mod-audit/conjecture/heuristic/numerical) is honoured over an open-problem KIND, so an
    unaudited paper-proof or a conjecture reads as ORANGE (non-rigorous-with-content), not RED (genuinely
    open). proved-mod-audit is the workhorse rung for the ingested classical-portfolio results."""
    af, status, kind = l.get("af", "none"), l.get("status"), l.get("kind")
    if af == "validated":                            return "validated"
    if status == "cited":                            return "cited"
    if status == "proved":                           return "proved"
    if status in {"proved-mod-audit", "conjecture", "heuristic", "numerical"}:  return "nonrigorous"
    if kind == "open-problem" or status == "open":   return "open"
    if af == "seeded":                               return "seeded"
    return "stated"


def render_index(lemmas):
    rows = ["| id | kind | status | af | owner | contract |", "|---|---|---|---|---|---|"]
    for l in sorted(lemmas, key=lambda d: d.get("id", "")):
        c = l.get("contract", "")
        c = (c[:80] + "…") if len(c) > 80 else c
        rows.append(f"| `{l.get('id','?')}` | {l.get('kind','?')} | {l.get('status','?')} | "
                    f"{l.get('af','none')} | {l.get('owner','-')} | {c} |")
    return GEN_HEADER + f"# Argument index ({len(lemmas)} results)\n\n" + "\n".join(rows) + "\n"


def render_dag(lemmas):
    """The full deps DAG + proof status as a status-coloured Mermaid graph. Deterministic.
    Multi-route shards render an OR-junction per route (see DAG_ROUTE_NOTE)."""
    ll = sorted(lemmas, key=lambda d: d.get("id", ""))
    nodes = [f'  {l["id"]}["{l["id"]}<br/>{l.get("status","")}/{l.get("af","none")}"]' for l in ll]
    # unconditional deps -> plain solid edges (required by every route)
    edges = [f"  {d} --> {l['id']}" for l in ll for d in l.get("deps", [])]
    route_nodes, route_edges, route_junctions = [], [], []
    for l in ll:
        for i, r in enumerate(l.get("routes", []), 1):
            jn = f'{l["id"]}__route{i}'
            route_junctions.append(jn)
            route_nodes.append(f'  {jn}{{"route {i}"}}')
            for m in sorted(r):                          # solid = this route's conjunctive members
                route_edges.append(f"  {m} --> {jn}")
            route_edges.append(f"  {jn} -. OR .-> {l['id']}")   # dashed = the disjunction
    edges = sorted(edges) + sorted(route_edges)
    total_edges = len(edges)
    classdefs = [f"  classDef {name} {style};" for name, style in CLASSDEFS]
    classdefs.append(f"  classDef {ROUTE_CLASSDEF[0]} {ROUTE_CLASSDEF[1]};")
    by_class = {}
    for l in ll:
        by_class.setdefault(proof_class(l), []).append(l["id"])
    classlines = [f"  class {','.join(sorted(by_class[name]))} {name};"
                  for name, _ in CLASSDEFS if by_class.get(name)]
    if route_junctions:
        classlines.append(f"  class {','.join(sorted(route_junctions))} {ROUTE_CLASSDEF[0]};")
    body = "\n".join(classdefs + nodes + route_nodes + edges + classlines)
    header = (GEN_HEADER + DAG_ROUTE_NOTE
              + f"# Argument DAG ({len(ll)} results, {total_edges} edges)\n\n")
    return (header + LEGEND + "\n\n```mermaid\ngraph LR\n" + body + "\n```\n")


def generate(lemmas, arg_dir=ARG_DIR):
    (arg_dir / "INDEX.md").write_text(render_index(lemmas), encoding="utf-8")
    (arg_dir / "DAG.md").write_text(render_dag(lemmas), encoding="utf-8")


def check_generated(lemmas, arg_dir=ARG_DIR):
    """CI staleness gate: committed INDEX.md/DAG.md must equal a fresh render of the shards,
    so the deps + proof-status graph is current in every commit. Stale ⇒ ERROR (blocks commit)."""
    errors = []
    for name, render in (("INDEX.md", render_index), ("DAG.md", render_dag)):
        path = arg_dir / name
        have = path.read_text(encoding="utf-8") if path.exists() else ""
        if have != render(lemmas):
            errors.append(f"{name} is STALE — run `python3 scripts/argument.py --generate` "
                          f"(deps/proof-status graph out of sync with the shards)")
    return errors


def main(argv):
    argv = list(argv)
    if "--show" in argv:
        i = argv.index("--show")
        target = argv[i + 1] if i + 1 < len(argv) else None
        if not target or target.startswith("--"):   # missing / flag-shaped -> usage, not "unknown id"
            print("usage: python3 scripts/argument.py --show <id>")
            return 2
        lemmas, _ = parse_registry(ARG_DIR)
        print(format_show(lemmas, target))
        return 0 if any(l.get("id") == target for l in lemmas) else 1
    if "--closure-min" in argv:
        i = argv.index("--closure-min")
        target = argv[i + 1] if i + 1 < len(argv) else None
        if not target or target.startswith("--"):
            print("usage: python3 scripts/argument.py --closure-min <id>")
            return 2
        lemmas, _ = parse_registry(ARG_DIR)
        by = {l["id"]: l for l in lemmas}
        if target not in by:
            print(f"unknown id '{target}' — not a registry result.")
            return 1
        rc = route_closures(lemmas, target)
        if not rc:
            print(f"{target}: no routes (deps-only shard). Full ancestor closure via --show.")
            return 0
        print(f"# {target}: per-route ancestor closures ({len(rc)} routes; ANY one discharges it)")
        base = by[target].get("deps", [])
        if base:
            print(f"unconditional deps (in every route): {', '.join(base)}")
        for idx, members, clo in rc:
            print(f"route {idx} (members: {', '.join(members)}): "
                  f"{len(clo)} ancestors -> {', '.join(sorted(clo)) or '(none)'}")
        return 0
    args = set(argv) or {"--check", "--generate"}
    lemmas, errors = parse_registry(ARG_DIR)
    def_ids = load_def_ids()
    ws_dirs = scan_workspaces()

    ws_contracts, nodecounts = {}, {}
    for l in lemmas:
        if l.get("af", "none") != "none":
            facts = af_introspect(l.get("workspace", ""))
            if facts:
                ws_contracts[l["id"]] = facts["contract"]
                nodecounts[l["id"]] = facts["nodes"]

    errors += check_acyclic(lemmas)
    errors += check_imports(lemmas, def_ids)
    serr, ready, blocked = check_status(lemmas)
    errors += serr
    errors += check_contracts(lemmas, ws_contracts)
    errors += check_orphans(lemmas, ws_dirs)
    # CI staleness gate: in pure check mode (the gate) the committed graph must match a fresh
    # render. When --generate is requested we (re)write the files below instead of failing.
    if "--generate" not in args:
        errors += check_generated(lemmas)
    warnings = check_brittleness(lemmas, nodecounts)

    if "--generate" in args and not errors:
        generate(lemmas)
        print(f"wrote argument/INDEX.md + DAG.md ({len(lemmas)} results)")
    if "--sync-beads" in args:
        if errors:
            print("[--sync-beads] refusing to sync: registry has errors (fix them first)")
        elif sync_beads(lemmas) != 0:
            errors.append("--sync-beads failed (see above)")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\nargument: {len(lemmas)} results, {len(ready)} ready, {len(blocked)} blocked, "
          f"{len(errors)} errors, {len(warnings)} warnings")
    if ready:
        print("  ready frontier:", ", ".join(sorted(ready)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
