# Run bundle: arm-E error-bound uniformity PILOT (E1 decision-check, worker B) — 2026-07-05

**Status: L3 numerical evidence — a bounded PILOT (blowup detection), NEVER a uniformity
certificate.** Exact ℚ throughout. Codex-worker-authored (prompt in the session scratchpad,
`PROMPT-e1b-uniformity-pilot.md`); orchestrator reran the script from the banked location
(exit 0, report byte-identical modulo the one mechanical re-home patch of the output/rerun
paths — precedent: the wave-13/W17b bundles) and INDEPENDENTLY recomputed three headline points
from the printed matrices alone (`scripts/orchestrator_recompute.py`: anchor s=1/16, coupled
n=6, block sum — all match). The `min_E` (true-minimum) claims rest on the WORKER's n=3
combinatorial-type enumeration + exact LP, script-asserted, not orchestrator-re-derived.
Companion wave artifact: `docs/waves/2026-07-05-E1-error-bound-decision-check.md`.

## Hypothesis / adversarial question

Arm E wave 1 (bd aism-78w) pilot: does the error-bound ratio
`r(Q,E) = ||Q-E||_{∞→∞} / sqrt(η(Q))`, `η = ||Q²-Q||_{∞→∞}`, visibly grow with n — via clones,
block sums, or one genuinely coupled n-growing family?

## Headline finding

**No visible blowup in this pilot (families tested only).** Largest certified ratio:
`r² = 61937/32768` (`r ≈ 1.375`) at the stochasticized `ex-hume` anchor `s = 1/16`, with the
TRUE n=3 minimum over ALL 3×3 stochastic idempotents (worker enumeration: identity / rank-one /
singleton+pair / two singletons+transient — derived from `E²=E` in the report, worker T1).
Clone lift and block direct sum verified EXACTLY invariance-compatible (any dimension blowup
must be coupled). Coupled level-chain family n=4..12: `r²` drifts `3/23 → 11/69` (bounded,
monotone-ish); constructed-candidate framing — upper-bound evidence only.

## Honest scope

- Pilot, not a theorem and not a sweep: 4 anchor points + 2 exact-min instances + 1 clone +
  1 block sum + 9 coupled sizes. Says nothing about uniformity in n.
- Coupled-family ratios use a CONSTRUCTED candidate `E` (collapse-to-absorbing); a bounded value
  only says this family did not break; a growing value would only have indicted the construction.
- The signed→stochastic conversion of `ex-hume` is rowwise positive-part normalization (order-s²
  change), chosen by the worker; ratios are computed from the resulting exact `Q_s` alone.
- Decision-grade criteria for a wave-2 probe are recorded in the report §Task 5 (kill = coupled
  family with certified LOWER bounds on `min_E ||Q-E||/sqrt(η)` growing with n).

## Command (re-run)

```bash
python3 runs/2026-07-05-e1-uniformity-pilot/scripts/e1_worker_b_pilot.py       # regenerates data/pilot-full-report.md; hard asserts; exit 0
python3 runs/2026-07-05-e1-uniformity-pilot/scripts/orchestrator_recompute.py  # independent 3-point recomputation from printed matrices
```

## Invariant (checkable)

The pilot script exits nonzero unless all 17 assert rows (report §Assert list) are recomputed
from the printed rational matrices; `orchestrator_recompute.py` independently recomputes
`(η, dist, r²)` for the s=1/16 anchor (`241/32896`, `241/2048`, `61937/32768`), coupled n=6
(`115/864`, `5/36`, `10/69`), and the block sum (`9/50`, `42/125`, `392/625`) from hardcoded
copies of the printed matrices, incl. `E` stochastic-idempotency checks.

## Next

Wave-2 decision-grade probe per the report §Task 5 (bd `aism-5an` carries the theory
intermediates): quotient-web rank-growing families with certified two-sided brackets on
`min_E ||Q-E||` for `n ≤ 8` (exact LP/MILP over idempotent support structures) and independent
LOWER bounds from quotient/lumping certificates for `n = 9..12`; skip clones/direct sums
(proved inert here). Kill = certified lower-bound ratios growing with n; support = bounded
brackets collapsing to Hume-like local obstructions.

## Files

- `scripts/e1_worker_b_pilot.py` — the worker pilot (re-homed paths only).
- `scripts/orchestrator_recompute.py` — orchestrator independent recomputation (witness side).
- `data/pilot-full-report.md` — the worker's full report (== wave-doc worker-B section source).
- `data/rerun-stdout.txt` — orchestrator rerun capture (empty on success; asserts are silent).
