#!/usr/bin/env python3
"""TDD for check-runs.py. "Runs without errors" is never a pass — each case asserts a verdict."""
import importlib.util
import pathlib
import tempfile

_spec = importlib.util.spec_from_file_location(
    "check_runs", pathlib.Path(__file__).resolve().parent.parent / "check-runs.py")
cr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cr)

FAILS = []


def expect(cond, msg):
    if not cond:
        FAILS.append(msg)


def scenario(bundle_name, readme_text, index_text, has_readme=True):
    """Build a temp repo with one bundle + INDEX.md; return (errors, warnings, n)."""
    tmp = pathlib.Path(tempfile.mkdtemp())
    runs = tmp / "runs"
    runs.mkdir()
    if bundle_name:
        b = runs / bundle_name
        b.mkdir()
        if has_readme:
            (b / "README.md").write_text(readme_text, encoding="utf-8")
    (tmp / "INDEX.md").write_text(index_text, encoding="utf-8")
    return cr.check_runs(runs, tmp / "INDEX.md")


GOOD_README = (
    "# Run: gap floor probe\n"
    "## Hypothesis\nThe degree-6 SoS lower bound on E0 exceeds the variational upper bound minus gamma.\n"
    "## Command\n`julia --project=. scripts/sos_gap.jl --n 8 --seed 1`\n"
    "## Finding\nCertificate verified (exact rational SDP dual); scope: n<=8 only, no thermodynamic limit.\n"
    "## Next\nPush to n=10; check the invariant against exact diagonalization.\n"
    "Invariant: dual feasibility residual < 1e-30 (exact arithmetic).\n")
GOOD_INDEX = "| runs/2026-07-01-gap-floor | SoS gap | sos_gap.jl |\n"

# 1. Empty runs/ is GREEN (day-1).
e, w, n = cr.check_runs(pathlib.Path(tempfile.mkdtemp()) / "runs", pathlib.Path(tempfile.mkdtemp()) / "INDEX.md")
expect(e == [] and n == 0, f"empty runs/ should be green, got errors={e}")

# 2. A fully-formed bundle is GREEN.
e, w, n = scenario("2026-07-01-gap-floor", GOOD_README, GOOD_INDEX)
expect(e == [], f"valid bundle should be green, got errors={e}")

# 3. Missing README -> ERROR.
e, w, n = scenario("2026-07-01-gap-floor", "", GOOD_INDEX, has_readme=False)
expect(any("missing README" in x for x in e), f"missing README should error, got {e}")

# 4. Missing a required field (drop 'Next') -> ERROR.
e, w, n = scenario("2026-07-01-gap-floor", GOOD_README.replace("## Next", "## TODO-later"), GOOD_INDEX)
expect(any("missing required field" in x and "next" in x for x in e), f"missing field should error, got {e}")

# 5. No checkable invariant -> ERROR.
no_inv = ("## Hypothesis\nx\n## Command\n`run`\n## Finding\ngot a number 3.14\n## Next\nmore\n")
e, w, n = scenario("2026-07-01-gap-floor", no_inv, GOOD_INDEX)
expect(any("invariant" in x for x in e), f"no-invariant bundle should error, got {e}")

# 6. Bundle not in INDEX.md -> ERROR.
e, w, n = scenario("2026-07-01-gap-floor", GOOD_README, "nothing here\n")
expect(any("not referenced in INDEX" in x for x in e), f"un-indexed bundle should error, got {e}")

# 7. Bad bundle name -> ERROR.
e, w, n = scenario("gapfloor", GOOD_README, "| runs/gapfloor |\n")
expect(any("bad bundle name" in x for x in e), f"bad name should error, got {e}")

if FAILS:
    print("FAIL:")
    for f in FAILS:
        print("  -", f)
    raise SystemExit(1)
print("test_check_runs: all assertions passed")
raise SystemExit(0)
