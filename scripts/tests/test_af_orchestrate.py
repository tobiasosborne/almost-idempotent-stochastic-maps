#!/usr/bin/env python3
"""
Red-green tests for scripts/af-orchestrate.py — the codex worker dispatch layer.
Asserts the model/effort tiering policy (user directive 2026-07-09, amended 2026-07-13):
codex runs gpt-5.6-sol; effort CAPPED at xhigh (ultra is unstable and spawns subagents
indiscriminately) — xhigh for creative/demanding jobs, lower for routine.
subprocess.run is monkeypatched — no real codex is ever invoked.
Run: python3 scripts/tests/test_af_orchestrate.py
"""
import importlib.util
import os
import pathlib
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent


def load_orch():
    _spec = importlib.util.spec_from_file_location(
        "af_orchestrate", ROOT / "scripts" / "af-orchestrate.py")
    mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(mod)
    return mod


orch = load_orch()
_REAL_RUN = orch.subprocess.run   # stash before any monkeypatching (restored for the stub tests)

passed = failed = 0


def check(name, cond):
    global passed, failed
    if cond:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


# --- model + tier policy constants ---
check("default codex model is gpt-5.6-sol", orch.CODEX_MODEL == "gpt-5.6-sol")
check("creative tier: prover at highest ALLOWED effort (xhigh)",
      orch.TIERS["creative"]["prover"] == "xhigh")
check("creative tier: verifier at xhigh", orch.TIERS["creative"]["verifier"] == "xhigh")
check("routine tier: prover at lower effort (high)",
      orch.TIERS["routine"]["prover"] == "high")
check("routine tier: verifier at high", orch.TIERS["routine"]["verifier"] == "high")
check("every tier effort is an allowed effort",
      all(v in orch.CODEX_EFFORTS for t in orch.TIERS.values() for v in t.values()))
check("effort cap: ultra and max are NOT allowed efforts (2026-07-13 directive)",
      "ultra" not in orch.CODEX_EFFORTS and "max" not in orch.CODEX_EFFORTS)
check("the cap constant is xhigh", orch.EFFORT_CAP == "xhigh")

# --- run_codex command construction (subprocess.run monkeypatched) ---
captured = {}


def fake_run(cmd, **kw):
    captured["cmd"] = cmd
    captured["timeout"] = kw.get("timeout")
    # the fake worker writes its answer file, like codex -o does
    i = cmd.index("-o")
    pathlib.Path(cmd[i + 1]).write_text("FAKE ANSWER", encoding="utf-8")


orch.subprocess.run = fake_run
with tempfile.TemporaryDirectory() as td:
    out = orch.run_codex("prompt", f"{td}/ans.txt", f"{td}/log.txt", effort="xhigh")
    cmd = captured["cmd"]
    check("run_codex pins the model with -m gpt-5.6-sol",
          "-m" in cmd and cmd[cmd.index("-m") + 1] == "gpt-5.6-sol")
    check("run_codex passes the reasoning effort as a -c config override",
          'model_reasoning_effort="xhigh"' in cmd)
    check("xhigh effort gets the extended 3600s timeout", captured["timeout"] == 3600)
    check("answer file content is returned", out == "FAKE ANSWER")

    # The hard cap: a programmatic caller passing ultra/max is clamped to xhigh —
    # ultra must NEVER reach a codex command line (2026-07-13 directive).
    orch.run_codex("prompt", f"{td}/ans-u.txt", f"{td}/log-u.txt", effort="ultra")
    check("effort=ultra is clamped to xhigh on the command line",
          'model_reasoning_effort="xhigh"' in captured["cmd"]
          and 'ultra' not in " ".join(captured["cmd"]))
    orch.run_codex("prompt", f"{td}/ans-m.txt", f"{td}/log-m.txt", effort="max")
    check("effort=max is clamped to xhigh on the command line",
          'model_reasoning_effort="xhigh"' in captured["cmd"])

    orch.run_codex("prompt", f"{td}/ans2.txt", f"{td}/log2.txt", effort="high")
    check("high effort keeps the 1800s timeout", captured["timeout"] == 1800)
    check("effort override reaches the command line",
          'model_reasoning_effort="high"' in captured["cmd"])

    orch.run_codex("prompt", f"{td}/ans3.txt", f"{td}/log3.txt", effort="high",
                   timeout=42)
    check("explicit timeout beats the effort-derived one", captured["timeout"] == 42)

# --- $CODEX_MODEL env override (also proves the -m assertion above can fail) ---
os.environ["CODEX_MODEL"] = "test-model-xyz"
try:
    orch2 = load_orch()
    orch2.subprocess.run = fake_run
    with tempfile.TemporaryDirectory() as td:
        orch2.run_codex("prompt", f"{td}/ans.txt", f"{td}/log.txt", effort="low")
    cmd = captured["cmd"]
    check("CODEX_MODEL env var overrides the model",
          cmd[cmd.index("-m") + 1] == "test-model-xyz")
finally:
    del os.environ["CODEX_MODEL"]

# --- CLI: tier/effort flags parse; invalid values rejected ---
ap_ok = True
try:
    with tempfile.TemporaryDirectory() as td:
        rc = orch.main(["no-such-result-id", "--tier", "routine",
                        "--prover-effort", "xhigh", "--logdir", td])
except SystemExit:
    ap_ok = False
check("main accepts --tier/--prover-effort and stops at the missing workspace",
      ap_ok and rc == 2)
bad_rejected = False
try:
    orch.main(["x", "--prover-effort", "ultra"])
except SystemExit:
    bad_rejected = True
check("--prover-effort ultra is rejected by argparse (cap at xhigh)", bad_rejected)
bad_rejected = False
try:
    orch.main(["x", "--tier", "not-a-tier"])
except SystemExit:
    bad_rejected = True
check("invalid --tier is rejected by argparse", bad_rejected)
bad_rejected = False
try:
    orch.main(["x", "--verifier-effort", "supermax"])
except SystemExit:
    bad_rejected = True
check("invalid --verifier-effort is rejected by argparse", bad_rejected)

# ====================================================================================
# aism-s64: the shared node-size constant (scripts/af_constants.py) reaches this script
# ====================================================================================
check("orchestrator imports the shared NODE_SOFT_CAP (26)", orch.NODE_SOFT_CAP == 26)

# ====================================================================================
# aism-d6m: prover-overreach guard widened — ANY dirty repo path outside the run's own
# proofs/<rid>/ workspace is flagged (was: only definitions/ + argument/)
# ====================================================================================
_orig_porcelain = orch._git_porcelain
orch._git_porcelain = lambda: "\n".join([
    " M definitions/def-x.md",                       # Layer 0 (always flagged)
    "?? argument/lemmas/lem-phantom.md",             # Layer 1 (always flagged)
    " M scripts/argument.py",                        # WIDENED: any other repo path
    " M report/sections/03_x.tex",                   # WIDENED
    "?? proofs/lem-a/ledger/000003.json",            # the run's OWN workspace: allowed
    "?? proofs/lem-a/",                              # untracked-dir porcelain form: allowed
    " M proofs/lem-b/ledger/000001.json",            # ANOTHER result's workspace: flagged
    "R  notes.md -> report/notes-moved.md",          # rename: destination is judged
])


def flagged(bad, sub):
    return any(sub in ln for ln in bad)


bad = orch.overreach_paths("proofs/lem-a")
check("own-workspace writes are allowed", not flagged(bad, "proofs/lem-a"))
check("definitions/ still flagged", flagged(bad, "definitions/def-x.md"))
check("argument/ still flagged", flagged(bad, "argument/lemmas/lem-phantom.md"))
check("WIDENED: scripts/ now flagged", flagged(bad, "scripts/argument.py"))
check("WIDENED: report/ now flagged", flagged(bad, "report/sections/03_x.tex"))
check("WIDENED: another result's proofs/ workspace flagged",
      flagged(bad, "proofs/lem-b/ledger/000001.json"))
check("rename judged by its destination", flagged(bad, "report/notes-moved.md"))
check("no workspace arg -> everything dirty is flagged",
      flagged(orch.overreach_paths(), "proofs/lem-a/ledger/000003.json"))
orch._git_porcelain = _orig_porcelain

# ====================================================================================
# aism-cwt: quota/auth fast-fail — run_codex returns the "ERROR" sentinel on the codex
# usage-limit marker or a nonzero exit (real subprocess against stub codex scripts;
# incident 2026-07-10: a quota outage burned all 14 rounds with empty outputs, no abort)
# ====================================================================================
orch.subprocess.run = _REAL_RUN     # the stub tests exercise the REAL subprocess path
_orig_codex = orch.CODEX
with tempfile.TemporaryDirectory() as td:
    td = pathlib.Path(td)

    def make_stub(name, body):
        p = td / name
        p.write_text(body, encoding="utf-8")
        p.chmod(0o755)
        return str(p)

    # 1) codex prints the literal usage-limit error but exits 0 -> marker scan must catch it
    quota = make_stub("codex-quota", "#!/bin/sh\n"
                      "echo \"stream error: You've hit your usage limit. "
                      "Try again in 2 hours.\"\nexit 0\n")
    orch.CODEX = quota
    out = orch.run_codex("p", td / "a1.txt", td / "l1.log", effort="low", timeout=30)
    check("usage-limit marker in log -> ERROR sentinel", out == "ERROR")
    check("the marker really reached the log file",
          "You've hit your usage limit" in (td / "l1.log").read_text(encoding="utf-8"))

    # 2) codex exits nonzero without the marker -> still ERROR
    boom = make_stub("codex-boom", "#!/bin/sh\necho unrelated failure\nexit 3\n")
    orch.CODEX = boom
    out = orch.run_codex("p", td / "a2.txt", td / "l2.log", effort="low", timeout=30)
    check("nonzero codex exit -> ERROR sentinel", out == "ERROR")

    # 3) healthy worker (writes its -o answer, exits 0) -> answer returned, no false positive
    ok = make_stub("codex-ok", "#!/usr/bin/env python3\nimport sys\n"
                   "a = sys.argv[1:]\n"
                   "open(a[a.index('-o') + 1], 'w').write('REAL ANSWER')\n"
                   "print('worker log line')\n")
    orch.CODEX = ok
    out = orch.run_codex("p", td / "a3.txt", td / "l3.log", effort="low", timeout=30)
    check("healthy stub -> answer returned (no false ERROR)", out == "REAL ANSWER")
orch.CODEX = _orig_codex

# ====================================================================================
# aism-cwt: round-loop dead-round abort — 2 consecutive rounds of all-ERROR/empty
# workers abort with the quota message and a nonzero exit (independent of open_ch)
# ====================================================================================
import contextlib
import io

_ABORT_MSG = "ABORT: codex calls failing (quota/auth?) — nothing consumed, rerun after reset"
with tempfile.TemporaryDirectory() as td:
    root = pathlib.Path(td)
    (root / "proofs" / "lem-t" / "ledger").mkdir(parents=True)
    _saved = (orch.ROOT, orch.af, orch.af_json, orch.run_codex, orch._git_porcelain)
    try:
        orch.ROOT = root
        orch.af = lambda ws, *a, **k: ("", 0)

        def fake_af_json(ws, *a):
            if a and a[0] == "status":
                return {"statistics": {"total_nodes": 3, "open_challenges": 0,
                                       "epistemic_state": {"pending": 2, "archived": 0}},
                        "challenges": []}
            if a and a[0] == "jobs":
                role = a[a.index("--role") + 1] if "--role" in a else ""
                return ({"prover_jobs": [{"node_id": "1.1"}]} if role == "prover"
                        else {"verifier_jobs": []})
            if a and a[0] == "get":
                return {"id": "1", "epistemic_state": "pending"}
            return {}

        orch.af_json = fake_af_json
        orch._git_porcelain = lambda: ""
        orch.run_codex = lambda *a, **k: "ERROR"          # every worker: dead codex
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = orch.main(["lem-t", "--phase", "verify", "--max-rounds", "8",
                            "--logdir", str(root / "logs")])
        out = buf.getvalue()
        check("dead codex: nonzero exit", rc != 0)
        check("dead codex: the mandated abort message is printed", _ABORT_MSG in out)
        check("dead codex: abort classified CODEX-DEAD", "CODEX-DEAD" in out)
        check("aborts after 2 dead rounds, not the full --max-rounds budget",
              "round 1:" in out and "round 2:" not in out)

        # build-phase fast-fail: a dead prover build aborts immediately (rc 4)
        buf2 = io.StringIO()
        with contextlib.redirect_stdout(buf2):
            rc2 = orch.main(["lem-t", "--phase", "prove", "--logdir", str(root / "logs2")])
        check("dead prover build: immediate abort rc=4", rc2 == 4)
        check("dead prover build: abort message printed", _ABORT_MSG in buf2.getvalue())

        # control: workers that answer (non-ERROR) never trip the dead-round abort
        orch.run_codex = lambda *a, **k: "VERDICT blocked 1.1"
        buf3 = io.StringIO()
        with contextlib.redirect_stdout(buf3):
            rc3 = orch.main(["lem-t", "--phase", "verify", "--max-rounds", "3",
                             "--logdir", str(root / "logs3")])
        check("control: healthy outputs never print the quota abort",
              _ABORT_MSG not in buf3.getvalue())
    finally:
        orch.ROOT, orch.af, orch.af_json, orch.run_codex, orch._git_porcelain = _saved

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
