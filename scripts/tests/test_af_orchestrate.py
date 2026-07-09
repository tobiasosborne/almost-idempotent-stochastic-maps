#!/usr/bin/env python3
"""
Red-green tests for scripts/af-orchestrate.py — the codex worker dispatch layer.
Asserts the model/effort tiering policy (user directive 2026-07-09): codex runs
gpt-5.6-sol; highest thinking (ultra) for creative/demanding jobs, lower for routine.
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
check("creative tier: prover at highest effort (ultra)",
      orch.TIERS["creative"]["prover"] == "ultra")
check("creative tier: verifier at xhigh", orch.TIERS["creative"]["verifier"] == "xhigh")
check("routine tier: prover at lower effort (high)",
      orch.TIERS["routine"]["prover"] == "high")
check("routine tier: verifier at high", orch.TIERS["routine"]["verifier"] == "high")
check("every tier effort is a supported gpt-5.6-sol effort",
      all(v in orch.CODEX_EFFORTS for t in orch.TIERS.values() for v in t.values()))

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
    out = orch.run_codex("prompt", f"{td}/ans.txt", f"{td}/log.txt", effort="ultra")
    cmd = captured["cmd"]
    check("run_codex pins the model with -m gpt-5.6-sol",
          "-m" in cmd and cmd[cmd.index("-m") + 1] == "gpt-5.6-sol")
    check("run_codex passes the reasoning effort as a -c config override",
          'model_reasoning_effort="ultra"' in cmd)
    check("ultra effort gets the extended 3600s timeout", captured["timeout"] == 3600)
    check("answer file content is returned", out == "FAKE ANSWER")

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
                        "--prover-effort", "ultra", "--logdir", td])
except SystemExit:
    ap_ok = False
check("main accepts --tier/--prover-effort and stops at the missing workspace",
      ap_ok and rc == 2)
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

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
