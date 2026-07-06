# Wave W35 — the absorption theorem: proximity bricks banked; the exposedness step is the residual (2026-07-07, session 11)

**Node:** conj-low-slab-cap via the OPPOSITE-direction mechanism (sketch v8 / the W34
diagnosis), bd `aism-2fi` (P0). **Design:** mutually-blind pair — worker AC (prove an
absorption theorem, formulation freedom) ∥ worker AD (measure the absorption threshold with
exact certificates — IN FLIGHT at this doc's first commit) — + SEPARATE fresh hostile verifier
VAC on AC's claims. Prompts + raw answers in the session-11 scratchpad (`W35/`).

## Verdicts (verbatim first lines)

- Worker AC: `PARTIAL (proved: received-mass => convex proximity, and a `1-O(tau)` singleton
  recipient lies in the `rho`-shadow; gap: no theorem converts that `rho`-shadow / near-top
  cluster into exposedness, so no universal `theta` cap yet)`
- Verifier VAC: `VALID-WITH-CORRECTIONS (Claim P valid; Claim S needs `0 < delta` for the
  strict `< 4*tau` line, and the `H` Lipschitz form only holds when `v` is a top)`
- Worker AD: `NOT-SUSTAINED (frontier: R_4 = 0 in these certified constructions; binding
  constraint: true-hidden rows stay below 4τ, while coefficient pushes are absorbed into W)`

## Results (round 1)

1. **`lem-received-mass-proximity` (codified, proved/af:none).** dist₁(p_i, conv A) ≤
   D(1 + 2ν_i − σ_A) — receiving mass is proximity. Exact fixtures at three (i, A) pairs.
2. **`lem-single-heavy-recipient-rho-shadow` (codified, proved/af:none, VAC-corrected).**
   A (1−τ)-heavy recipient sits INSIDE the exposedness-exempt ball (27τ/8 < 4τ at δ ≤ 1/16):
   no cap counterexample can outsource to one far row — deep mass must SPREAD.
3. **The residual, priced exactly (AC + VAC arithmetic):** at the cap scale the proximity
   bound is ~ D(θ + 4τ) > ρ even at θ = 0 — proximity can NEVER reach the exposedness-exempt
   scale after the CS pincer spends 4τ. The missing absorption step is
   **cluster-to-EXPOSEDNESS**: a tall hidden top keeping > 1 − θ − 4τ mass on
   G_a ∩ {h* < κ} must force some recipient-side vertex to become (ρ, κ)-exposed. That
   statement (not proximity) is conj-low-slab-cap's true content.

## Results (round 2 — AD's harvest)

4. **The absorption transition, captured exactly** (bundle
   `runs/2026-07-07-w35-absorption-threshold/`, orchestrator rerun PASS): R₄ = 0 in every
   certified true-hidden construction; the rank-5 scaled direction is hidden with
   R_{1/4} ≈ 0.105 at s = 1403/1000 and ABSORBED into W at s = 351/250 (t*₅ = 51/569, H = 0)
   — a 1-parameter family crossing the transition. The LP comparison (δ = 1/4, a 5/4
   coefficient, everything visible) shows coefficient capacity is NOT the blocker: exact
   geometry is. W36 = the transition wave: what quantity crosses zero; extract and generalize
   the exposer that appears at absorption.

## Banking (orchestrator)

Registry: the two shards above (VAC as reviewer). Bundle: AD's exact verifier + README +
INDEX row. Honest tiers: reviewed paper proofs (L5) + L3 certificates; NOT af-validated, NOT
L0-rigorous; the cap remains OPEN.
