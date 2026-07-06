# Run bundle: sigma_g frontier — exact-feasibility attack at ANY height (W19 worker A) — 2026-07-06

**Status: L3 numerical evidence — NOT-REALIZED-HERE for `σ_g > 1/2`; NEVER an emptiness claim
(wave-15 lesson stamped).** Exact ℚ throughout. Codex-worker-authored (prompt in the session
scratchpad, `PROMPT-w19a-sigma-refuter.md`); reuses the banked web-regime pipeline
(`runs/2026-07-02-web-regime-hunt/scripts/`). Orchestrator reran from the banked location
(exit 0; two mechanical re-home patches: `parents[2]→parents[3]` — the W17b precedent — and the
report output path) and INDEPENDENTLY recomputed the algebraic side of three headline matrices
(`scripts/orchestrator_recompute.py`: idempotence, row sums, δ, mass placement for the m=4
split, the rank-5 record point, and banked instance B); the geometric certifications (W, H,
distances, σ_g) remain worker-asserted. Companion wave artifact:
`docs/waves/2026-07-06-W19-route-a-deciders.md`.

## Hypothesis / adversarial question

W18 decider (bd `aism-213`): realize a hidden top vertex with halo-robust `σ_g > 1/2` at ANY
height (the low-height/high-σ_g region was never searched — W18 proved the cap is strictly
stronger than the height bound), or report the binding constraints via exact optimization
rather than family census.

## Headline finding

**NOT REALIZED in these designs; the binding constraint is EXPOSEDNESS ABSORPTION, not mass
capacity.** The exact LP relaxation (row-negativity + nonnegativity constraints only) places
the full `5/4` mass on designated outside recipients — but the exact-geometry optimizer point
has `W = [3,4,5]`, `H = 0`: the recipients became visible. Certified frontier points:
- new record halo-robust mass `σ_g = 5991/80000 ≈ 0.075` (rank 5, genuine SELF recipient,
  `δ = 3983/96000`) — above W17b's census max `1/25` but still ~6.7× below the cap;
- rank-3 distinct-partner point `σ_g = 229/3200 ≈ 0.072` (= banked instance B, recomputed);
- duplicate-split family: splitting `q = 5/84` of hidden-column mass over m = 2, 4, 8
  near-coincident recipients leaves total `σ_g = 5/84` EXACTLY unchanged (one quotient class —
  clone-consistency realized), and pushing `q` to `1/16` flips the recipients into `W`
  (`H = 0`): the hidden/absorbed frontier on this design sits between `5/84` and `1/16`.

## Honest scope

- Four design axes only (duplicate-split, distinct-partner anchor, rank-5 self, LP-vs-geometry
  comparison). NOT an emptiness claim for `σ_g > 1/2`.
- **Named residual:** geometrically DISTINCT multi-class designs (many recipients in different
  quotient classes, each hosting near its per-class ceiling) were NOT probed — the duplicate
  splits are a single quotient class by construction. This is the sharpest untested axis and
  the direct empirical probe of the W19-B per-class question.
- `σ_g`/W/H certifications come from the worker's pipeline asserts (calibrated against two
  banked exact witnesses: the F2 sigma-halo-nonrobust anchor and instance B); the orchestrator
  recomputation covers the algebraic side only.

## Command (re-run)

```bash
python3 runs/2026-07-06-w19-sigma-frontier/scripts/w19_worker_a.py          # regenerates data/worker-report.md; hard asserts; exit 0
python3 runs/2026-07-06-w19-sigma-frontier/scripts/orchestrator_recompute.py # independent algebraic recomputation, 3 headline matrices
```

## Invariant (checkable)

The worker script exits nonzero unless every assert in the report's Assert List (57 items,
incl. the two banked-witness calibrations) is recomputed from the printed rational matrices;
`orchestrator_recompute.py` independently asserts `P² = P`, row sums, `δ`, and mass placement
for the three headline matrices hardcoded from the printed report.

## Next

Wave-2 per the named residual: exact optimization over designs with m geometrically DISTINCT
genuine-outside quotient classes (not duplicates), each pushed toward its per-class ceiling —
the direct test of whether total `σ_g` can accumulate across classes (the W18 `C/τ`-count
opening) or whether absorption binds classwise. Pair with the `conj-external-poke-charge(A)`
codification (W19 worker B's named target, bd follow-up).

## Files

- `scripts/w19_worker_a.py` — the worker attack (re-homed paths only; imports the banked
  web-regime pipeline).
- `scripts/orchestrator_recompute.py` — orchestrator independent algebraic recomputation.
- `data/worker-report.md` — the worker's full report (regenerated on rerun; == wave-doc
  worker-A section source).
- `data/rerun-stdout.txt` — orchestrator rerun capture.
