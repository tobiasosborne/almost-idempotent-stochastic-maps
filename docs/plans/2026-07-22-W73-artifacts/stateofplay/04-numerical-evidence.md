# Numerical Evidence Layer (all L3 — evidence, never proof)

## 1. Inherited spine (2026-07-02 rehome)
- 67,000+ exact verified signed-idempotent instances (P²=P, δ = max_i neg(p_i)), zero exact counterexamples to the linear pattern.
- Linear law H ≈ 2δ (δ ≈ H/2); d13 small-δ probe found no hidden-top-vertex floor for δ ≤ 1e-2.
- Finite-δ correction: certified 5×5 obstruction with δ=49/2000, H=1/20, H/δ = 100/49 > 2 ("hull-dip"); H/δ → 2 and H/τ → 0 as scale shrinks (τ := √δ).
- Rank-3 (EX) enumeration: 444 exact rank-3 records, 278 with δ≤1/4; 2947 theta-half charts checked in-cap; 0 empirical (EX) violations, 0 factorization violations.
- Caveat: below the corner scale δ≈0.233 the dangerous joint regime (σ̃ > τ ∧ H > Bτ) has NEVER been entered by any verified record.

## 2. Arm F exact hunts (2026-07-02)
- web-regime-hunt: exact-ℚ, 7 families, n≤9, ~48,000 exact idempotents, ~500 certified hidden vertices; 0 entered the joint regime (σ̃/τ up to ≈4 alone; H/τ up to 0.502 alone — never together). Collapse bound H·(1−σ̃) ≤ ν·(2+4δ): 0/500 violations.
- sigma-cap-refuter: ~25k float-searched hidden top vertices; genuine (halo-robust, dist≥τ/4) invisible mass never exceeded ≈0.37τ (1−σ̃_g≥0.92 everywhere); max H/τ=0.462. NEGATIVE: naive ε=0 cap exactly FALSE — exact certificate with σ̃=5343/5000 > 1 (all self-mass, P_vv>1, at distance 0.02τ); halo-robust σ̃_g=0 there. Halo-robust collapse bound holds exactly on all certified instances.

## 3. σ_g > 1/2 hunt — consistently empty, growing margin
- door-ratio-census (07-05): 514 exact rank-3 instances; 138 hidden top vertices measured; 0 with σ_g>1/2; best σ_g=1/25. ≥12× empirical slack under the D1 constant-cap target (σ_g≤1/2 ⇒ Kernel with B=29/8).
- w19-sigma-frontier (07-06): LP/geometry attack at any height. Record σ_g=5991/80000≈0.075 (rank 5) — ~6.7× below cap. Binding mechanism identified precisely: EXPOSEDNESS ABSORPTION — LP relaxation happily places mass 5/4 on recipients, but exact geometry then makes recipients visible (H=0), destroying the hidden-vertex antecedent. Duplicate-splitting over 2/4/8 near-coincident recipients does NOT raise σ_g (clone-invariance, single quotient class). Untested residual: geometrically distinct multi-class design.
- w20-g-zoo-measurement: 307 unique matrices, 1842 cases, all exact harmonicity + sandwich checks pass. HEADLINE: G_a (genuine, far set) is EMPTY zoo-wide for every a≥1 — deepest genuine geometry ever banked sits within 1·τ of conv W; relevant threshold sits at 4τ. Zoo-measurement approach retired as decider.

## 4. Hiddenness / witness-coupling (07-06/07)
- w26: bounded search (n≤10, 1000 samples) — no second counterexample family beyond the known 3×3 (which is VISIBLE under canonical geometry, t*=100/101).
- w29 witness-coupling NOT-REFUTED. Best certified true-hidden frontier: δ=99/8000, H=1/40, H²/δ=5/99 (H/τ≈0.225). Pincer: (i) true hiddenness folds back before depth 4τ; (ii) tall/high-mass attempts absorbed into W.
- w30: W-nonemptiness proved only for δ=0 and simplex/rank≤2; 297 exact random Λ-C idempotents, W never empty. Convergent obstruction: hiddenness needs visible anchors (an empty W would leave witnesses anchorless) — candidate mechanism for a general production theorem, still open.

## 5. THE TALLNESS-BIND SEQUENCE — seven consecutive exact batches, all blocked identically
w35, w41, w44, w52, w62, w63(+ihorn), w66, w69, w71: each attempted a different exact construction; EACH blocked by the SAME obstruction — tallness (H > 16τ or H > 4τ) never realized.
- W35: sustained received-deep-mass R_4=0 in every certified construction; captured exact absorption transition in a 1-param family.
- W52: 4 exact families + 1296-record exact grid (1270 with 0<δ≤1/4) — zero entries into H²/δ>16, zero nonempty C4; best disjoint frontier H²/δ ≈ 0.228 (~70× short of threshold 16).
- W62/W63/W63-ihorn: 3rd/4th/5th consecutive constructions fail ONLY on tallness while satisfying every other antecedent clause.
- W66: 6th consecutive bind; first exact definition-level C0 cell entrant but still H<16τ.
- W69: growing-rank family (genuine rank 4,8,16,32, no clones): local finance negativity exactly 0 at every rank — rank CAN distribute local cost — but every GLOBAL gate (root ownership, tallness, ultra-omega nonemptiness) fails by a rank-uniform margin (ownership excess exactly 1/8 at every rank). "Rank distributes the LOCAL finance cost for free... the wall a refuter cannot cross is the GLOBAL package."
- W71: 7th bind. Exact trade-off/ownership law max_i ν(P_i) = β·a: root ownership needs β≥1/8, negativity gate needs β≤τ²/a — positive exact gap at every rank/scale; repairing ownership at β=1/8 drives max single-row negativity to 1/8 (order-one, does not shrink with rank). Mechanism (i) "support disjointness" (ρ(1)=0, G_φ=0) survives only OUTSIDE the gate; mechanism (ii) "orientation starvation" NEVER reached by any tested family.

COMMON PATTERN: the obstruction is never algebraic failure — every antecedent clause except tallness/height is simultaneously satisfiable. The height/tallness gate and exposedness absorption are the recurring single point of failure under several names (σ̃-cap, σ_g>1/2, H²/δ>16, H>4τ, tall-heavy-cluster, R0 ownership). Strongly suggests exposedness absorption IS the actual mechanism behind Kernel/(EX) — but every bundle disclaims emptiness/universality (bounded-family search only).

## 6. Completion/financing deciders (07-10)
- w57/w58 starvation-completion LP: INFEASIBLE for minimal rank-3 actor-hull family via exact Farkas certificates (stable over A0∈[4,6], τ≤1/256); extends to first-extra-vertex family (huge exact margin). Rank-3/fixed-K scope only.
- w61-x2-graft: X2 microfreight exclusion NOT refuted — six-row factorized family satisfies every checked clause except tallness (H=O(τ³)).
- w61-leak-financing: exact dyadic family (δ=τ²→0) PAYS the financing-floor demand with slack.

## 7. Untouched territory (no decider evidence at all)
- LDHR-48 (low-deficit huddle ray): no exact orientation-starved family exists — untouched for both sides.
- Orientation starvation (POTI mechanism ii): never reached; positive-overlap-with-starvation regime (t_φ≤D_0·δ) has zero certified instances.
- RDSE (root-dilution selected-support exchange): no decider (W72 unverified).
- σ_g>1/2 in genuinely multi-class (non-duplicate) hidden-recipient designs: never probed.
- The (29τ/8, 4τ] halo-width gap for Lemma A / MIN-A: zero banked geometry inside it.

## 8. Cumulative picture for a strategist
1. Linear law δ≈H/2 dominates realizable census; √η/quadratic form only the worst-case envelope once H is capped near O(√δ) by exposedness.
2. Zero-violation records are consistent evidence, never proof; several searches are adversarially/LP-guided (stronger than enumeration, still bounded-family).
3. Materially strong lead: multiple independent, differently-shaped constructions all die at the SAME wall (exposedness absorption / tallness / ownership order-one cost) — actively searched and failed, not merely never tried.
4. W71 ownership law is the sharpest quantitative artifact; flagged family-specific; its "why" unverified (W72 pending).
5. Failure-mode taxonomy uniform: δ inflation, forced visibility (exposedness absorption), top-reversion-with-hull-intersection — recur verbatim W52→W71.
