#!/usr/bin/env python3
"""
check-runs.py — the NUMERICS gate (CLAUDE.md L3).

THE FAILURE MODE THIS GUARDS AGAINST: a numerical result masquerading as rigorous, or a number with
no re-run command / no checkable invariant / no place in the index. Numerics are evidence, NEVER proof
(the rigour ladder, L0): they are admissible ONLY as a reproducible *run bundle*.

A run bundle is `runs/<YYYY-MM-DD>-<slug>/` and MUST carry:
  1. a `README.md` with the four required fields — a Hypothesis, an exact re-run **Command**, a
     Headline **Finding** (with honest scope limits), and Next steps;
  2. a declared **Invariant / certificate / known-value** check (the thing that makes the number
     checkable rather than decorative);
  3. a row in the top-level `INDEX.md` naming the bundle dir (the reverse lookup).

Day 1: `runs/` is empty by design ⇒ the gate is green.

CLI:
  python3 scripts/check-runs.py --check    # validate; exit 1 on any ERROR (pre-commit)
  python3 scripts/check-runs.py            # audit + print; exit 0
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"
INDEX = ROOT / "INDEX.md"

BUNDLE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*$")
# The README must evidence each of these (case-insensitive substring of a header or line).
REQUIRED_FIELDS = ("hypothesis", "command", "finding", "next")
# At least ONE of these must appear — the checkable-invariant requirement.
INVARIANT_MARKERS = ("invariant", "certificate", "known value", "known-value",
                     "independent", "cross-check", "cross check", "residual", "tolerance")
SKIP = {"README.md"}  # runs/README.md is the schema doc, not a bundle


def check_runs(runs_dir=RUNS, index_path=INDEX):
    errors, warnings = [], []
    runs_dir = pathlib.Path(runs_dir)
    index_text = pathlib.Path(index_path).read_text(encoding="utf-8") if pathlib.Path(index_path).exists() else ""

    bundles = []
    if runs_dir.exists():
        for p in sorted(runs_dir.iterdir()):
            if p.is_dir():
                bundles.append(p)
            elif p.name not in SKIP:
                warnings.append(f"runs/{p.name}: stray file at runs/ top level (bundles are dirs)")

    for b in bundles:
        name = b.name
        if not BUNDLE_RE.match(name):
            errors.append(f"runs/{name}: bad bundle name — must be <YYYY-MM-DD>-<kebab-slug>")
        readme = b / "README.md"
        if not readme.exists():
            errors.append(f"runs/{name}: missing README.md (hypothesis/command/finding/next)")
            continue
        text = readme.read_text(encoding="utf-8").lower()
        missing = [f for f in REQUIRED_FIELDS if f not in text]
        if missing:
            errors.append(f"runs/{name}/README.md: missing required field(s): {', '.join(missing)}")
        if not any(m in text for m in INVARIANT_MARKERS):
            errors.append(f"runs/{name}/README.md: no checkable invariant/certificate/known-value "
                          f"declared (a number without an invariant is not a finding — L3)")
        if name not in index_text:
            errors.append(f"runs/{name}: not referenced in INDEX.md (add a reverse-lookup row)")

    return errors, warnings, len(bundles)


def main(argv):
    check_mode = "--check" in argv
    errors, warnings, n = check_runs()
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"check-runs: {n} run bundle(s), {len(errors)} errors, {len(warnings)} warnings")
    if check_mode and errors:
        print("check-runs: FAILED — a numerical bundle is undocumented or overclaims.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
