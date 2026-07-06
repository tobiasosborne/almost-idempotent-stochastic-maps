# Wave W20 — g-bootstrap decider 1: the harmonic observable across the certified zoo (2026-07-06)

**Node:** sketch v3 §Route A, mechanism M1 (the g-bootstrap), decider `aism-vmt` — the pre-registered
CHEAP decider that runs FIRST. **Design:** two mutually-blind fresh codex workers (session-9 pattern):
worker A = measurement sweep, worker B = adversarial kill-hunter aimed at the two kill criteria
pre-registered in the sketch. Prompts + raw answers in the session scratchpad (`W20/PROMPT-{A,B}.md`,
`W20/ANSWER-{A,B}.md`); scripts + full reports + orchestrator recompute in
`runs/2026-07-06-w20-g-zoo-measurement/` (L3 bundle). Workers ran no `fr`/`bd` and made no repo edits
outside their designated bundle paths. Orchestrator reran both scripts (exit 0) and independently
recomputed the headline algebra from the printed matrix alone (8/8 checks).

## Verdicts (verbatim first lines)

- Worker A: `LEMMA-A-SUPPORTED (sup g_w/tau = 0 at a=4)`
- Worker B: `NO-KILL-FRONTIER (visible sup g_w/tau = 0 for a in {4,5,6}; band sup g = 0 for a in {4,5,6})`

## Worker A (measurement) — key content

- [T1] Full exact sweep, no subsampling: 527 attempted source entries → 311 qualifying covered
  (all 298 qualifying door-ratio census entries included), 307 unique matrices after dedup, 1842
  exact `(matrix, a)` measurements at `a ∈ {1/4, 1, 2, 4, 5, 6}`; 216 census entries skipped as
  non-qualifying (`δ = 0` or `δ > 1/4`), label-by-label table in the report.
- [T1] 1842 harmonicity checks `P·g = g` and 9564 sandwich checks `σ_g(v) − ν_v ≤ g_v ≤ σ_g(v)`
  passed exactly; the four banked calibrations reproduced (halo-nonrobust; rank-3 partner 229/3200;
  rank-5 self 5991/80000; duplicate splits 5/84).
- [T1] `a = 1/4`: visible max `g_w = 7/80` (`g_w/τ = √(105/569) ≈ 0.4296`) at I007 row 4
  (= the W19 rank-5 genuine-self record instance); hidden-top max `g_v = σ_g(v) = 5991/80000`.
- [T1] **`a ∈ {1, 2, 4, 5, 6}`: `G_a` EMPTY on every covered instance** — all `g ≡ 0`. No row
  anywhere reached `g ≥ 1/2`.
- [T2] K1 and K2 not realized; covered-zoo non-realization only, not an emptiness claim.

## Worker B (adversarial) — key content

- [T1] No kill realized. In every certified worker-B construction (LP-guided anti-absorption designs,
  duplicate families, bounded scans) `G_a` is empty for `a ∈ {4,5,6}`; hence visible `g_w = 0` and
  band `g = 0` — both kills unrealized VACUOUSLY at workable widths.
- [T1] Low-halo stress `a = 1/4`: best visible `g = 7/80` with `(g/τ)² = 105/569` (same anchor as
  worker A, independently); best non-W band value `5991/80000`.
- [T2] Binding constraint: **exposedness absorption, not coefficient capacity** — the exact LP places
  designated positive mass `5/4`, exact geometry then makes the recipients visible (`W = [3,4,5]`,
  `H = 0`, all `G_a` empty). Same wall as W19.
- [T1] Clone consistency: weighted row-cloning transports `G_{1/4}` and preserves old-row `g` exactly
  (the M1 clone-safety claim realized on an example).

## Orchestrator recomputation (banked)

`runs/2026-07-06-w20-g-zoo-measurement/scripts/orchestrator_recompute.py` (exit 0): from the printed
I007 matrix alone — P² = P, row sums 1, δ = 3983/96000, harmonicity for the worker-asserted
`G_{1/4} = {5}`, `g₄ = 7/80`, `σ_g(5) = 5991/80000`, sandwich at row 5, `(g₄/τ)² = 105/569`.
Hand-check of the ratio: `(7/80)²/(3983/96000) = 735/3983 = 105/569` ✓. Geometric side (W, dists, G)
worker-asserted, stated as such.

## Wave outcome (orchestrator, [T2] strategic)

1. **Both pre-registered kills UNREALIZED** — the g-bootstrap survives its cheap decider.
2. **The load-bearing structural fact is the emptiness of the battleground:** nothing in the banked
   zoo (or in worker B's adversarial designs) realizes depth `> 1τ` from `conv W`. The step-4 kill
   zone (band-supported `g ≥ 1/2` webs) is unreachable by every known construction — supporting
   evidence for MIN-A, and simultaneously a hard limit on what further zoo measurement can decide:
   **zoo measurement is exhausted as a step-4 decider.**
3. **The constants fight is now exact and named** (with W21): Lemma A's mechanism needs `a ≥ 4`;
   MIN-A's tall antecedent guarantees depth only `> 29τ/8 = 3.625τ`; the `(29τ/8, 4τ]` band is the
   gap the bootstrap must close (new bd follow-up filed at session close).
4. Honest tier: everything here is L3 evidence / worker-T1 exact certificates; nothing is promoted.
