#!/usr/bin/env sh
# Local validation suite (the "CI"). Non-zero exit fails the commit (wired into the pre-commit hook).
# Run from anywhere inside the repo. No remote CI — this is the only gate (CLAUDE.md Rule 12).
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -n "$ROOT" ] || ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT" || exit 1
fail() { echo "[check-all] FAILED: $1"; exit 1; }

echo "[check-all] definitions gate (required fields, drift/dedup, cited sha256)"
python3 scripts/check-defs.py --check || fail "check-defs"

echo "[check-all] refs provenance gate (sources catalogued; payloads byte-verified if present)"
python3 scripts/check-refs.py --check || fail "check-refs"

echo "[check-all] argument linker (acyclic, imports, contracts, rigour-ladder status, brittleness, orphans)"
python3 scripts/argument.py --check || fail "argument"

echo "[check-all] numerics gate (every runs/ bundle: README + INDEX row + invariant; nothing masquerades as rigorous)"
python3 scripts/check-runs.py --check || fail "check-runs"

echo "[check-all] report<->registry provenance sync"
python3 scripts/check-provenance.py --check || fail "check-provenance"

echo "[check-all] sharded lab-book (master purity, shard headers, README/CATALOG cross-index)"
bash scripts/check-report-shards.sh || fail "check-report-shards"

echo "[check-all] tooling tests (TDD; port-and-verify)"
for t in scripts/tests/test_argument.py scripts/tests/test_check_defs.py scripts/tests/test_check_refs.py scripts/tests/test_check_runs.py; do
  [ -f "$t" ] || continue
  out=$(python3 "$t" 2>&1) || { echo "$out"; fail "$t"; }
done

# Report build is gated only when latexmk is available and the report has a main file.
if command -v latexmk >/dev/null 2>&1 && [ -f report/main.tex ]; then
  echo "[check-all] report build (latexmk -> report/.build; main.pdf not mutated)"
  ( cd report && latexmk -pdf -interaction=nonstopmode -halt-on-error \
      -outdir=.build main.tex >/dev/null 2>&1 ) || fail "report build (cd report && make to see errors)"
else
  echo "[check-all] report build SKIPPED (latexmk or report/main.tex absent)"
fi

echo "[check-all] OK"
