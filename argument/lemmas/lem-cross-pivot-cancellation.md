---
id: lem-cross-pivot-cancellation
kind: lemma
contract: Cross-pivot cancellation: let P be a rank-3 exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let U = (u_0,u_1,u_2) be an actual-row chart whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, and define coordinates a_q(i) by p_i = sum_q a_q(i)p_{u_q} and beta_r(i) = P_{u_r i}; then for every pair of distinct indices r, s in {0,1,2}, sum_i beta_r(i)*a_s(i) = 0, the sum running over all row indices i of P.
defs: def-signed-idempotent
deps: 
status: proved-mod-audit
af: none
provenance: docs/waves/2026-07-04-G11-capped-charge.md §Task 1 eq. (2) (exact B-L duality: row reproduction p_{u_r} = sum_i P_{u_r i} p_i from P^2 = P, coordinates taken, a_s(u_r) = 0 for r != s); verified numerically on three exact instances by the orchestrator 2026-07-04
owner: A
workspace: proofs/lem-cross-pivot-cancellation
---

**The B-L duality identity** behind G11's import anatomy. Proof shape: `P^2 = P` gives row
reproduction `p_{u_r} = sum_i P_{u_r i} p_i`; expressing both sides in the chart basis gives
`a_s(u_r) = sum_i P_{u_r i} a_s(i)`; and `a_s(u_r) = delta_{sr}` because a chart row's own
coordinate vector is a standard basis vector.

**Positive/negative-part split (body note, not the contract).** Writing
`A_{r,s} = sum_i beta_r(i)^+ a_s(i)^+`, `B_{r,s} = sum_i beta_r(i)^+ a_s(i)^-`,
`C_{r,s} = sum_i beta_r(i)^- a_s(i)^+`, `D_{r,s} = sum_i beta_r(i)^- a_s(i)^-`, the identity
rearranges to `A_{r,s} = B_{r,s} + C_{r,s} - D_{r,s} <= B_{r,s} + C_{r,s}` — the exact financing
split behind the (PRT) cross-pivot residual: positive pivot-coordinate mass seen by a transverse
pivot is paid by `B_{r,s}` (beta-positive rows with negative pivot coordinate) plus `C_{r,s}`
(beta-negative transverse-chart-row entries against positive pivot coordinates).

**Role.** Composes with [[lem-import-reduction]] and the validated [[lem-collateral-import]] to
reduce the dominant collateral import to `B_{r,s} + C_{r,s}` — the exact residual named by wave
G11 for [[conj-sc]]/(PRT).
