# Run bundle: Lemma A refuter frontier (W21 worker D) — 2026-07-06

**Status: L3 numerical evidence — the refuter side of a prove-or-refute wave; NOT-REFUTED here;
NEVER an emptiness claim.** Exact ℚ throughout. One codex refuter (prompt in the session scratchpad,
`W21/PROMPT-D.md`), mutually blind from the prover (worker C) and verifier (worker E) whose proof
side lives in the wave doc. Orchestrator reran the script (exit 0; stdout in `data/`) and
INDEPENDENTLY recomputed the algebraic side of both printed matrices
(`scripts/orchestrator_recompute.py`); geometric certifications (W, distances, t*, G determination,
the absorption W-flip) remain worker-asserted. Companion wave artifact:
`docs/waves/2026-07-06-W21-lemma-a-decider.md`.

## Hypothesis / adversarial question

Refute LEMMA A (g-bootstrap step 2, bd `aism-0b1`; sketch v3 §Route A M1): construct an exact signed
idempotent (0 < δ ≤ 1/4, W ≠ ∅) with a visible row `w ∈ W` and halo width `a ∈ {4,5,6}` such that
`g^{(a)}_w ≥ K·τ` with `K > 4` (breaks the conjectured constant) or `K = Ω(1/τ)` (kills the lemma);
secondarily, chart the small-`a` frontier (`a ∈ {1/4, 1, 2}`) for the endgame constants fight.

## Headline finding

**NOT-REFUTED at `a ∈ {4,5,6}`: every certified construction has `G_a = ∅`, hence `g_w = 0` — the
refuter could not even populate the far set** (consistent with the W20 zoo-wide emptiness). The
valuable output is the **small-halo frontier certificate**: a rank-5 instance
(`scaled-rank5-lambda-7/5`) with `δ = 27881/480000`, `W = [0,1,2,3,4]`, `G_{1/4} = {5}`, and visible
row 4 carrying `g^{(1/4)}_4 = 49/400`, i.e. `K = g/τ = √(147/569) ≈ 0.5083` — the largest certified
visible-row `g/τ` to date (beats the W20 zoo maximum ≈ 0.4296). Binding constraint: **exposedness
absorption** — scaling the same family from `λ = 7/5` to `λ = 29/20` flips the deep row visible
(`W = [0..5]`, `H = 0`, all halo sets empty).

## Honest scope

- A refuter frontier, not a tightness certificate: 0.51τ at `a = 1/4` says nothing against the proved
  `4τ` cap at `a ≥ 4` (which stands proved + independently verified — see the wave doc), and the
  `a ≥ 4` regime was never populated by ANY construction, here or in W20.
- The large-halo obstruction read (worker D, [T2]): for `a ≥ 4`, any `j ∈ G_a` is ρ-far from every
  visible row — the same inclusion the prover uses; the refuter independently converged on the
  mechanism from the opposite mandate.

## Command (re-run)

```bash
python3 runs/2026-07-06-w21-lemma-a-decider/scripts/w21_worker_d.py            # certificates + asserts (exit 0)
python3 runs/2026-07-06-w21-lemma-a-decider/scripts/orchestrator_recompute.py  # algebraic recompute (exit 0)
```

`data/worker-d-report.md` is the refuter's complete report (both full exact matrices);
`data/rerun-d-stdout.txt` is the orchestrator's captured rerun.

## Invariant / known-value check

The worker script hard-asserts idempotence, row sums, 0 < δ ≤ 1/4, visible membership of the
certificate row, exact distances, halo sets, and g values (rerun exit 0). The orchestrator's
`orchestrator_recompute.py` re-derives from the printed matrices alone: P² = P, row sums,
δ = 27881/480000, harmonicity for G = {5}, g₄ = 49/400, K² = 147/569 > 1/4, and the absorption
companion's algebra (δ = 115507/1920000) — 11/11 checks pass.

## Next

Refutation attempts at `a ≥ 4` are blocked behind the same wall as everything else on Route A:
realizing depth `> τ` (let alone `> 4τ`) against exposedness absorption. The named follow-up is the
halo-width gap `(29τ/8, 4τ]` (new bd issue) and depth-realization itself as a refuter target.
