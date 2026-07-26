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
python3 scripts/gen-current-pointer.py --check || fail "current-pointer"

echo "[check-all] report definitions render (generated projection of definitions/ shards; L2)"
# The report's definitions section is a deterministic projection of definitions/*.md. A shard
# edited without re-rendering would leave the paper stating an older definition — exactly the
# drift L2 forbids — so the committed render must equal a fresh one.
python3 scripts/gen-report-defs.py --check --dag-anchors || fail "gen-report-defs"

echo "[check-all] report argument-DAG atlas freshness (generated .tex == a fresh render of the shards)"
# Same contract as argument.py's INDEX/DAG staleness check: the committed report/generated/dag/*.tex
# and report/sections/39_argument_dag.tex must equal a fresh render of argument/lemmas/*.md. A shard
# whose status/af/deps changed without regenerating the atlas is STALE => the commit is blocked.
python3 scripts/gen-report-dag.py --check || fail "gen-report-dag"

echo "[check-all] report<->registry provenance sync (+ latexmk build & undefined-ref scan via --build)"
# --build folds the report compile into this step: latexmk into report/.build (never mutates the
# tracked main.pdf) AND scans the log for undefined \ref/\Cref (which -halt-on-error does NOT fail on).
# latexmk is incremental over report/.build, so this is the SINGLE report compile — the standalone
# report-build block below is intentionally gone (would have been a duplicate). Skips cleanly (warn)
# if latexmk is absent, exactly like the old block.
python3 scripts/check-provenance.py --check --build || fail "check-provenance"

echo "[check-all] sharded lab-book (master purity, shard headers, README/CATALOG cross-index)"
bash scripts/check-report-shards.sh || fail "check-report-shards"

echo "[check-all] tooling tests (TDD; port-and-verify)"
for t in scripts/tests/test_argument.py scripts/tests/test_check_defs.py scripts/tests/test_check_refs.py scripts/tests/test_check_provenance.py scripts/tests/test_check_runs.py scripts/tests/test_af_orchestrate.py scripts/tests/test_register_oracle.py; do
  [ -f "$t" ] || continue
  out=$(python3 "$t" 2>&1) || { echo "$out"; fail "$t"; }
done

# NOTE: the report build (latexmk -> report/.build) now runs inside the check-provenance --build step
# above (single compile + undefined-reference scan). No separate build block here — see that step.

echo "[check-all] OK"
