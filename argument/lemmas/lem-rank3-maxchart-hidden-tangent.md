---
id: lem-rank3-maxchart-hidden-tangent
kind: lemma
contract: Rank-3 max-chart hidden tangent: for an exact signed idempotent P with rank(P) = 3 and 0 < delta(P) <= 1/4 (tau = sqrt(delta), rho = 4*tau, kappa = tau/4), let U = (u_0, u_1, u_2) be a maximum-area triangle among geometrically distinct row vertices in the two-dimensional affine row hull and write p_j = sum_s a_s(j)*p_{u_s} in barycentric coordinates; if u_s is hidden, then some row j has ||p_j - p_{u_s}||_1 >= rho and a_s(j) > 1 - 2*kappa, and one of its two transverse barycentric coordinates is negative with magnitude q > tau*(3 - 2*delta(P))/(4*(1 + 2*delta(P))) >= 5*tau/12.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: 
status: proved
af: none
provenance: W31 wave (docs/waves/2026-07-07-W31-anchorless-witness.md): fresh-codex prover (worker Y) + SEPARATE fresh-codex hostile verifier (VY, VALID — re-derived the vertex-maximality step |a_s| <= 1 via affinity of a_s over convex combinations of row vertices; rank-3 => affine row hull EXACTLY 2-dim from the row-sum splitting; exact fixtures: banked W19 rank-3 (delta = 74551/1600000, max chart (0,1,2), all chart exposers admissible) + canonical rank-3 projection delta = 1/16)
owner: A
workspace: proofs/lem-rank3-maxchart-hidden-tangent
---

**Role (the anchorless-witness route's first brick, Kernel(i) at rank 3).** In an all-hidden
rank-3 configuration, EVERY max-area chart vertex must have a ρ-far "tangent companion":
a row hugging the a_s ≈ 1 slab (within 2κ) yet escaping ℓ¹-distance ρ by dipping NEGATIVELY
(magnitude > 5τ/12) in a transverse barycentric direction. Mechanism: max-area maximality makes
h_s = (1 − a_s)/2 an admissible exposer (|a_s| ≤ 1 on all rows — affinity pushes the extremes
to row vertices); hiddenness (def-exposed, t* < κ applied to h_s directly) hands the companion;
nonnegative transverse coordinates would keep the row within (τ/2)(2+4δ) ≤ 3τ/2 < ρ.

**Why this does not yet close W-nonemptiness (the honest gap, worker Y + VY).** Swapping two
same-orientation tangent companions into the chart gains area ~ q_r·q_s = Θ(τ²) but pays slab
defects ε_r + ε_s = Θ(τ) — the max-volume contradiction needs slab defects O(τ²) (or a
coefficient-coupling input). This is the SAME missing shape as conj-min-a-w4's
coefficient-coupling gap (FINDINGS 2026-07-07 W31/W32).

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous; af-elevation candidate
(deps: none).
