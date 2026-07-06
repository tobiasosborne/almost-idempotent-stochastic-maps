# Run bundle: g-zoo measurement — the harmonic observable across the certified zoo (W20) — 2026-07-06

**Status: L3 numerical evidence — a zoo-wide measurement + an adversarial non-realization; NEVER an
emptiness claim (wave-15 lesson stamped).** Exact ℚ throughout. Two mutually-blind codex workers
(prompts in the session scratchpad, `W20/PROMPT-A.md` / `W20/PROMPT-B.md`): worker A measured, worker B
attacked. Orchestrator reran both scripts (exit 0; captured stdout in `data/`) and INDEPENDENTLY
recomputed the algebraic side of the headline matrix from its printed values alone
(`scripts/orchestrator_recompute.py`: idempotence, row sums, δ, the g-arithmetic given the
worker-asserted halo set); geometric certifications (W, distances, G determination) remain
worker-asserted. Companion wave artifact: `docs/waves/2026-07-06-W20-g-zoo-measurement.md`.

## Hypothesis / adversarial question

G-bootstrap decider 1 (bd `aism-vmt`; sketch v3 §Route A M1, kill criteria pre-registered there):
measure `g^{(a)} = P·1_{G_a}` (signed row mass on the genuine set `G_a = {j : dist₁(p_j, C_W) > a·τ}`)
exactly across the banked certified zoo at halo widths `a ∈ {1/4, 1, 2, 4, 5, 6}`, with harmonicity
`Pg = g` as a pipeline assert — and adversarially try to realize the two pre-registered kills
(K1: a visible row with `g ≫ τ` at `a ∈ {4,5,6}`; K2: a band-supported family with `g ≥ 1/2`
coexisting with `g|_W ≤ C·τ`).

## Headline finding

**LEMMA-A-SUPPORTED / NO-KILL-FRONTIER — and the zoo cannot even enter the battleground: `G_a` is
EMPTY zoo-wide for every `a ≥ 1`.** Worker A (full exact sweep, no subsampling: 311 qualifying
entries covered incl. all 298 qualifying door-ratio census entries, 307 unique matrices, 1842 exact
`(matrix, a)` measurements, 216 non-qualifying census entries skipped with a label-by-label table):
- 1842 harmonicity checks `P·g^{(a)} = g^{(a)}` and 9564 sandwich checks
  `σ_g^{(a)}(v) − ν_v ≤ g^{(a)}_v ≤ σ_g^{(a)}(v)` all passed exactly; 4 banked calibrations reproduced.
- At `a = 1/4`: visible-row maximum `g_w = 7/80` (`g_w/τ = √(105/569) ≈ 0.4296`) at row 4 of the
  rank-5 genuine-self instance (I007); hidden-top maximum `g_v = σ_g(v) = 5991/80000` (the W19 record).
- At `a ∈ {1, 2, 4, 5, 6}`: `G_a` is empty on EVERY covered instance, hence all `g ≡ 0` — the deepest
  genuine geometry ever banked sits within 1·τ of `conv W`. No row anywhere reached `g ≥ 1/2`.
Worker B (adversarial: LP-guided anti-absorption designs, duplicate families, clone tests): NO kill;
in every certified construction `G_a` is empty at `a ∈ {4,5,6}`; low-halo frontier matches I007
(`7/80`, band `5991/80000`); the binding constraint is again **exposedness absorption** (its exact LP
places designated mass 5/4; exact geometry then makes the recipients visible, `W = [3,4,5]`, `H = 0`);
weighted row-cloning transports `G_{1/4}` and preserves old-row `g` exactly.

## Honest scope + strategic reading (orchestrator)

A covered-zoo non-realization, NOT an emptiness theorem. Strategic content: (i) the Lemma-A empirical
constant at the only populated width is ≈ 0.43·τ — comfortably inside the proved `4τ` cap (W21);
(ii) the bootstrap's step-4 kill zone (band-supported `g ≥ 1/2` webs) is unreachable by every known
construction — evidence FOR MIN-A, priced as evidence only; (iii) the pre-registered constants fight
is now exact: Lemma A's mechanism needs `a ≥ 4` while MIN-A's tall antecedent guarantees depth only
`> 29τ/8 = 3.625τ`, and NOTHING banked realizes depth beyond `1τ` — the `(29τ/8, 4τ]` band is the
named gap (see the W21 bundle and FINDINGS).

## Command (re-run)

```bash
python3 runs/2026-07-06-w20-g-zoo-measurement/scripts/w20_worker_a.py        # full sweep + asserts (exit 0)
python3 runs/2026-07-06-w20-g-zoo-measurement/scripts/w20_worker_b.py        # adversarial designs (exit 0)
python3 runs/2026-07-06-w20-g-zoo-measurement/scripts/orchestrator_recompute.py  # algebraic recompute (exit 0)
```

`data/worker-a-report.md` / `data/worker-b-report.md` are the workers' complete reports (full exact
matrices for every headline instance); `data/rerun-a-stdout.txt` / `data/rerun-b-stdout.txt` are the
orchestrator's captured reruns.

## Invariant / known-value check

Worker A hard-asserts four banked calibrations before sweeping (halo-nonrobust witness
δ = 252559/1280000 with σ_g = 0; rank-3 partner σ_g(row 3) = 229/3200; rank-5 self
σ_g(row 5) = 5991/80000; duplicate splits δ = 1/16, H = 1/10, σ_g = 5/84), plus 1842 harmonicity and
9564 sandwich identities. The orchestrator's `orchestrator_recompute.py` re-derives the headline
arithmetic (P² = P, row sums, δ = 3983/96000, g₄ = 7/80, σ_g(5) = 5991/80000, (g₄/τ)² = 105/569)
from the printed I007 matrix alone — 8/8 checks pass.

## Next

The zoo cannot populate `G_a` for `a ≥ 1`: further zoo measurement is DEAD as a step-4 decider.
The live follow-ups are analytic: the `(29τ/8, 4τ]` halo-width gap (new bd issue), the step-4
band-web question itself, and `obs-deep-leakage` elevation (aism-tq3). Refuter searches should
target depth `> τ` constructions before re-attacking `g`.
