---
id: lem-absorption-implies-low-slab-cap
kind: lemma
contract: Conditional absorption-to-low-slab bridge: assuming conj-near-cluster-absorption with constants (a_0 >= 4, theta_0 in (0,1), delta_0 > 0) and conj-far-low-slab-cap with the same constants, conj-low-slab-cap holds with a = a_0, theta = theta_0/4, and delta ceiling min(delta_0, (theta_0/24)^2): every exact signed idempotent P with 0 < delta(P) <= min(delta_0, (theta_0/24)^2), nonempty visible set, and H > (4*(5*a_0/4 + 3/2)/theta_0)*tau has a hidden top vertex v whose optimal exposer h_v* satisfies sum over {j in G_{a_0} : h_v*(p_j) < tau/4} of max(P_vj, 0) <= 1 - theta_0/4 - 4*tau.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: conj-near-cluster-absorption; conj-far-low-slab-cap; lem-cs-low-slab-pincer
status: proved
af: none
provenance: W54 wave (E1 sub-wave): codex prover E1 + fresh hostile codex verifier V-E1 (VALID, no corrections) — the sketch-v17 Tier-1.5 gap E1 wired as a registered conditional lemma
owner: A
---

**Role (the E1 edge, wired).** The previously prose-only assembly hop "absorption =>
low-slab cap" (Opus skeleton gap G2; sketch v17 Tier-1.5 E1) is now a DAG edge. Proof
(V-E1-checked, no corrections): partition the deep low slab {j in G_{a_0} :
h_v*(p_j) < tau/4} into the near part N (||p_j - p_v||_1 < 4*tau: <= 1 - theta_0 by the
absorption antecedent at the GAP-supplied v), the far very-low part F_0
(h < tau/8: <= theta_0/4 by [[conj-far-low-slab-cap]]), and the far band F_1
(tau/8 <= h < tau/4: <= nu_v/(tau/8) <= 8*tau by [[lem-cs-low-slab-pincer]] at s = tau/8);
boundary ownership exact, no hole; the total 1 - 3*theta_0/4 + 8*tau <= 1 - theta_0/4 -
4*tau iff tau <= theta_0/24, delivered by the delta ceiling including the boundary.
Dimension-free; clone-invariant (index sums + contract-level inequalities only).

**Consumer note.** Downstream unchanged from [[conj-low-slab-cap]]'s role: pincer at
s = kappa + [[lem-parametric-halo-collapse]] => the Kernel height clause. With this shard,
tall-emptiness (== the absorption conclusion) + the far cap are the ONLY inputs separating
the huddle charge from the height clause.

**Rigour tier.** L5 (reviewer != author: fresh hostile codex V-E1, VALID). NOT af-validated.
