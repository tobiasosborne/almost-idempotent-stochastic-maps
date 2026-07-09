---
id: lem-zero-face-capacity-kill
kind: lemma
contract: Zero-face capacity kill: for an exact signed idempotent P with delta(P) > 0, a hidden geometrically distinct row vertex u, an optimal exposer h* at u, a row z with h*(p_z) = 0, and c_r > 0 with sum over {j : h*(p_j) >= kappa} of max(P_zj, 0) >= c_r (kappa = tau/4, tau = sqrt(delta)): c_r*kappa <= nu_z <= delta(P), where nu_z is the row-z negative mass; in particular no such configuration exists for 0 < delta < (c_r/4)^2.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-affine-exposer-row-capacity
status: proved
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): codex prover L4 (PROVED) + fresh hostile codex verifier V-L4 (VALID) — leaf L4 of the W54 case tree
owner: A
---

**Role (the tree's Branch-I capacity charge).** Leaf L4 of the W54 decomposition: a
zero-face row of u's optimal exposer shipping >= c_r of its positive mass to the
kappa-high slab pays c_r*kappa <= nu_z out of its own negative-mass budget — impossible
at small delta. V-L4-audited instantiation of [[lem-affine-exposer-row-capacity]] at
(i, h, eta, F) = (z, h*, kappa, {j : h*(p_j) >= kappa}): the shard needs h*(p_z) = 0 AT
the charged row (the zero-face membership supplies it; z = u is NOT required) and the
global box constraints 0 <= h* <= 1 (def-exposed admissibility). Dimension-free;
clone-invariant (z may be any row, clone or not).

**Rigour tier.** L5 (reviewer != author: fresh hostile codex V-L4, VALID). NOT af-validated.
