# Wave W21 — Lemma A prove-or-refute (g-bootstrap step 2) + independent verification (2026-07-06)

**Node:** sketch v3 §Route A, mechanism M1 step 2 — LEMMA A ("visible rows are g-small"), bd
`aism-0b1`, the load-bearing lemma of the g-bootstrap. **Design:** THREE fresh codex workers —
a mutually-blind adversarial prove/refute pair (worker C prove, worker D refute), plus a separate
fresh adversarial VERIFIER (worker E) dispatched on worker C's proof verbatim (reviewer ≠ author,
told that finding a gap is a big success; the orchestrator never judged the proof). Prompts + raw
answers in the session scratchpad (`W21/PROMPT-{C,D,E}.md`, `W21/ANSWER-{C,D,E}.md`); the refuter's
certificates + orchestrator recompute in `runs/2026-07-06-w21-lemma-a-decider/` (L3 bundle). Workers
ran no `fr`/`bd`; the prover and verifier made no repo edits at all.

## The statement (as briefed, and as codified in `lem-visible-g-small`)

P an exact signed idempotent, 0 < δ = δ(P) ≤ 1/4, τ = √δ, ρ = 4τ, κ = τ/4; W = W(P) ≠ ∅ the visible
set; C_W = conv{p_w : w ∈ W}; for halo width a ≥ 4, G_a = {j : dist₁(p_j, C_W) > a·τ} and
g = P·1_{G_a}. CLAIM: universal C with g_w ≤ C·τ for every w ∈ W.

## Verdicts (verbatim first lines)

- Worker C (prover): `PROVED (C = 4, a >= 4)`
- Worker E (verifier): `VALID (no error found; checks: definition fidelity, affine identity,
  sup/epsilon, sign discipline, duplicates, constants, 2x2/3x3 exact-rational sanity)`
- Worker D (refuter): `NOT-REFUTED-FRONTIER (sup g_w/tau = 0 at a = 4,5,6; small-a frontier:
  K = sqrt(147/569) = 0.508279 at a = 1/4)`

## The proof (worker C, [T1], verified by worker E; full text in the scratchpad ANSWER-C.md and in
the registry shard body)

Mechanism: pair row reproduction `p_w = Σ_j P_wj p_j` (from P² = P; row sums 1 make the affine
exposer distribute) against an admissible exposer `h_ε` of margin ≥ κ − ε (extracted from the sup in
t*(w) ≥ κ); the inclusion `G_a ⊆ {j : ‖p_j − p_w‖₁ ≥ ρ}` holds for a ≥ 4 because p_w ∈ C_W and the
halo comparison is strict; the sign-split of `0 = Σ_j P_wj h_ε(p_j)` with 0 ≤ h_ε ≤ 1 gives
`(κ−ε)·Σ_{G_a} P_wj⁺ ≤ ν_w ≤ δ`; ε → 0 yields `Σ_{G_a} P_wj⁺ ≤ δ/κ = 4τ`. Two-sided conclusion:
**−ν_w ≤ g_w ≤ 4τ** for every w ∈ W, every a ≥ 4. Degenerate branch (no ρ-far row ⇒ G_a = ∅ ⇒
g_w = 0) handled; duplicates harmless (h is a function of the row point); a ≥ 4 is used exactly once
(the halo-to-far-set inclusion). What it does NOT give: no upper control off W; lower control only
−ν_w.

## The verification (worker E, fresh codex, hostile brief)

All seven checklist items returned [T1]-clean: definition fidelity against the shards (exposedness
consumed exactly as written), the affine identity, the sup/ε extraction incl. degenerate branches,
every inequality direction, the duplicate convention, the constants (δ/κ = 4τ), plus a scratch-only
exact-rational sanity sweep (bounded 2×2 + 20,000 random 3×3) with no violation — and the observation
that sampled instances with nonempty W had EMPTY G_a, independently foreshadowing the W20 zoo fact.

## The refutation attempt (worker D, exact certificates in the bundle)

- [T1] At `a ∈ {4,5,6}`: NO refutation — every certified construction has `G_a = ∅`, so `g_w = 0`;
  the refuter could not populate the far set at all (the same absorption wall as W19/W20).
- [T1] Small-halo frontier certificate (`scaled-rank5-lambda-7/5`): δ = 27881/480000,
  W = [0,1,2,3,4], G_{1/4} = {5}, visible row 4 with `g^{(1/4)}_4 = 49/400`,
  `K = √(147/569) ≈ 0.5083` — the largest certified visible-row g/τ to date (W20 zoo max ≈ 0.4296).
  NOTE (orchestrator): 0.51τ at a = 1/4 does not contradict anything — Lemma A claims a ≥ 4 only.
- [T1] Absorption companion: scaling the family `λ: 7/5 → 29/20` flips the deep row visible
  (W = [0..5], H = 0, all halo sets empty) — absorption again the binding constraint.
- [T2] The refuter's "large-halo obstruction read" independently derives the SAME ρ-far inclusion the
  prover uses — adversarial convergence from opposite mandates (the E2 pattern, second occurrence).

## Orchestrator recomputation (banked)

`runs/2026-07-06-w21-lemma-a-decider/scripts/orchestrator_recompute.py` (exit 0): from the printed
matrices alone — both instances P² = P + row sums; δ = 27881/480000 and 115507/1920000; harmonicity
for the worker-asserted G = {5}; `g₄ = 49/400`; `K² = 147/569 > 1/4`; binding negativity on the
certificate row. Hand-check: `(49/400)²/(27881/480000) = 7203/27881 = 147/569` ✓ (both scale by 49).
Rerun of the refuter script: exit 0. Geometric side worker-asserted, stated as such.

## Wave outcome (orchestrator, [T2] strategic)

1. **Lemma A is PROVED (C = 4, a ≥ 4) with an independent fresh-verifier sign-off and a converging
   refuter** — codified as `argument/lemmas/lem-visible-g-small.md`, `status: proved`, `af: none`
   (NOT af-validated; candidate for elevation — bd follow-up). The g-bootstrap's step 2 moves from
   OPEN to done at exact constants; steps 1+2 of M1 now stand.
2. **The constants fight is the new named front:** the proof needs `a ≥ 4`; the MIN-A tall antecedent
   delivers depth only `> 29τ/8 = 3.625τ`. Either the bootstrap's step-3/4 machinery must place the
   deep-band mass beyond `4τ` (obs-deep-leakage territory), or Lemma A must be extended into
   `a ∈ (29/8, 4)` by a different mechanism (the ρ-far inclusion genuinely fails there), or the
   collapse constant must improve. Filed as the wave's follow-up decider.
3. Honest tiers: the lemma is a REVIEWED in-repo paper proof (L5 satisfied; L0 "rigorous" NOT claimed
   — af/byte-match/Lean remain the top rungs); the refuter frontier is L3 evidence.
