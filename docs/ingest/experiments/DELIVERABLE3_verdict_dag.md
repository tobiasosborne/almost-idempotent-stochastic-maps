# Deliverable 3 — Verdict and D4 DAG impact

## Verdict on (ASQ)

**(ASQ) is TRUE** (no counterexample in ~24 000 LP-verified exact idempotents across
structured skinny-pair families and broad random multi-dimension canonical configs; worst
`δ/H² ≈ 3.4–3.85` in max-neg units, matching d3's envelope `a≈2.4–3.5` and `H/τ ≤ 0.54`).

**Proof status is split:**
- **PROVED in the canonical simplex frame** (`R=[I_r|0]`), via the chain
  `lem-bary-dist-neg` (`dist₁(λ,Δ)=2·neg(λ)`, exact identity) → `lem-archetypes-in-W`
  (`conv W ⊇ Δ`) → `lem-asq-frame` (`H ≤ 2·neg(v) ≤ 2δ`), giving even the *stronger* linear
  bound `δ ≥ H/2`, hence `δ ≥ cH²` a fortiori once `H` is capped by the exposedness window.
  This route does **not** use the skinny-quadrilateral, anchoring, or failed exposedness — it
  is a generic frame fact and is fully rigorous.
- **NOT PROVED transferably** (arbitrary module, no simplex frame). The two-shadow composition
  `(*) H1 ≤ (1+μ1)ρ/(1−μ1μ2)` is **vacuous in the skinny regime** because `μ→1` exactly as the
  pair thins (measured: `μ_on_v2 = 0.998` at gap `0.002`). Convex geometry of one configuration
  cannot cap `H`; the cost must be extracted from `P²=P`. **This residual is identical to the
  d4-note's `lem-dual-localization` (the uncontrolled α-mass on the high zero-face).**

**Constant / convention.** `δ := max_i neg(p_i)`; `‖P‖_{∞→∞} = 1 + 2δ`. ASQ delivers
`δ ≥ c₀ H²` with `c₀ ≈ 3.4` (worst case), i.e. `‖P‖_{∞→∞} ≥ 1 + c H²` with `c = 2c₀ ≈ 6.8`.
(The task's "`c ≈ 2a`" is in ‖P‖-units; with `a≈3.4` that is `c≈6.8` — consistent.)

## Impact on the D4 lemma DAG

D4 had three OPEN nodes feeding MCC:
`lem-no-staircase-or-cost`, `lem-dual-localization`, `lem-anchored-cycle-projection-cost` (HCC),
plus the PROVED recursion chain (`lem-isolated-row-exposes`, `lem-far-row-gives-far-hidden-vertex`,
`lem-hidden-vertex-has-rho-shadow`, `lem-recursion-or-staircase`).

What (ASQ) — really, this whole exercise — changes:

1. **`lem-anchored-cycle-projection-cost` (HCC) / `lem-asq` for k=2:** **DISCHARGED in the
   canonical frame**, OPEN transferably. The k=2 anchored skinny quadrilateral cost is proved
   via Route A. New PROVED shards available: `lem-bary-dist-neg`, `lem-archetypes-in-W`,
   `lem-asq-frame`. These give the whole `op-exposed-hull` / HCC envelope `δ ≥ cH²` **in the
   canonical family**, matching the d3 numerics with a real proof rather than a fit.

2. **`lem-dual-localization`: SURVIVES as a separate need — and is now SHARPENED.** It is exactly
   the obstruction that blocks Route B. The minimal deciding configuration is now explicit (the
   skinny pair with `μ→1`); the open content is "reproduce `||Ebar||₁ ≥ H` from `P²=P` without
   the simplex frame." So (ASQ) does **not** discharge dual-localization in general — it
   *localizes* it to one sharp inequality and *proves* it in the frame.

3. **`lem-no-staircase-or-cost`: SURVIVES, untouched.** (ASQ) is the per-level cost; the
   staircase question (whether the recursion descends `ρ` per step forever vs. forms a
   same-height cycle) is orthogonal and still needed for the `H`-far→cycle step. The d2-note's
   τ-rescaling sketch (`height/τ_real → 0`) remains the candidate route there.

4. **MCC:** moves from "conditional on 3 OPEN lemmas" to **"PROVED in the canonical frame
   (modulo no-staircase, which is also frame-amenable via τ-rescaling), conditional on
   dual-localization only for arbitrary modules."** Net: in the canonical / Layer-1-frame
   setting the projection-cost obstruction is essentially closed; the general Layer-1 structure
   theorem still rests on dual-localization (consistent with `op-layer1-gap` staying OPEN, and
   with the project's honest "Frobenius-bounded but order-unit OPEN" status).

## Honesty ledger

- Agent-B's n=4 dichotomy: **VERIFIED** (structure symbolic, margins/collapse numeric, tight
  constants). It is a clean *lower-bound* certificate (clarification G1) and a reusable collapse
  identity (G2); it gives the right mechanism picture but **not** (ASQ) (embedded, two-high,
  exactness-driven) — that is the new content here.
- The H²-vs-H subtlety is the main correction to any naive reading: along the realizable family
  the tight relation is **linear** `δ=H/2`; the H² form is the worst-case envelope, binding only
  because `H` is capped at `O(τ)` by the exposedness window. Reporting "δ ≳ H²" without "δ ≳ H
  and H ≲ τ" would understate what is actually true.
- The transferable proof is **NOT** complete; claiming MCC fully proved would be the
  confident-plausible-WRONG failure mode. Route A is frame-specific; dual-localization is the
  honest remaining gap.
```
PROVED (frame):    lem-bary-dist-neg · lem-archetypes-in-W · lem-asq-frame  (=> ASQ/HCC k=2, frame)
OPEN (general):    lem-dual-localization (sharpened to one inequality) · lem-no-staircase-or-cost
```
