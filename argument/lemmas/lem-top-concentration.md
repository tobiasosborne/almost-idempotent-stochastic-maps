---
id: lem-top-concentration
kind: lemma
contract: Top concentration: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), hidden top vertex v of height H, and halo width a > 0 with H > a*tau (tau = sqrt(delta)), the positive mass v places outside the genuine set satisfies sum_{j notin G_a} P_vj^+ <= nu_v*(2+4*delta)/(H - a*tau), where G_a = {j : dist_1(p_j, conv{p_w : w in W}) > a*tau} and nu_v is the row-v negative mass.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass; def-height
deps: 
status: proved
af: none
provenance: W25 wave (docs/waves/2026-07-06-W25-step4-decider.md): fresh-codex prover (worker M, the verified core of its PARTIAL) + SEPARATE fresh-codex adversarial verifier (worker O, VALID on all 7 checklist items incl. an exact LP support-functional test on the banked rank-5 instance); first-principles proof (ell1/ell-infty support functional + row reproduction), no imports
owner: A
workspace: proofs/lem-top-concentration
---

**Role (the verified half of step 4; the once-applied maximum principle's actual yield).** In a
tall configuration the hidden top's positive mass CONCENTRATES on the deep set: at width a = 4 with
`H > 13*tau` the bound reads `sum_{j notin G_4} P_vj^+ < tau*(2+4*delta)/9`. Combined with
[[lem-genuine-disintegration]] (slack `R_v <= nu_v*(2+4*delta)/(H - a*tau)` by the same functional,
body consequence) and [[lem-parametric-halo-collapse]] (`g_v > 1/2 - delta` in tall configs), it
gives the LOWER bound `M_v^4 > 1/2 - delta - tau*(2+4*delta)/9` on deep hidden-vertex mass. The
missing OPPOSITE direction is exactly [[conj-min-a-w4]].

**Proof (worker M, T1; verified by worker O).** By ell1/ell-infty duality there is an affine
`phi(x) = u·x + b`, `||u||_inf <= 1`, with `phi <= 0` on C_W and `phi(p_v) = H`; taking infima over
C_W gives `phi(p_i) <= d_i` for every row. Row norms `<= 1+2*delta` give row diameter `<= D = 2+4*delta`,
hence `0 <= H - phi_j <= D` (lower: `phi_j <= d_j <= H`; upper: 1-Lipschitz + diameter). Row
reproduction + row sum 1 distribute the affine `phi`: `0 = sum_j P_vj (H - phi_j)`. Sign-split with
`H - phi_j in [0, D]`: `sum_j P_vj^+ (H - phi_j) = sum_j P_vj^- (H - phi_j) <= nu_v*D`. For
`j notin G_a`: `d_j <= a*tau` so `H - phi_j >= H - a*tau > 0`; restricting the (nonnegative) left
sum: `(H - a*tau) * sum_{j notin G_a} P_vj^+ <= nu_v*D`. QED.

**Body consequences (verified in the same pass, not part of the contract):**
- Disintegration-slack bound: `R_v := sum_{j in G_a} P_vj^+ (H - d_j)/(H - a*tau) <=
  nu_v*D/(H - a*tau)` (since `H - d_j <= H - phi_j` and the restricted sum is bounded by the total
  sign-split sum).
- Deep-mass lower bound (with [[lem-genuine-disintegration]] at i = v and the tall-config forced
  mass from [[lem-parametric-halo-collapse]] + [[lem-mass-split]]): `M_v^4 >= g_v - R_v >
  1/2 - delta - tau*(2+4*delta)/9` when `H > 13*tau`, `delta <= (17-12*sqrt2)/2`.
- Verifier O's wording caveat, kept: the sufficient closing cap is `M_v^4 <= 1/2 - delta -
  nu_v*(2+4*delta)/(H-4*tau)`; the `M+R` form in [[conj-min-a-w4]]'s body is sufficient-not-equivalent.

**Rigour tier.** In-repo paper proof with independent fresh-codex review (L5; Review: line in the
banking commit). NOT af-validated, NOT L0-rigorous; af-elevation candidate (deps: none).
