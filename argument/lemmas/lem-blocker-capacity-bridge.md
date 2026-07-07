---
id: lem-blocker-capacity-bridge
kind: lemma
contract: Conditional blocker capacity bridge: assuming conj-downhill-zero-face-lower-mass (constants c_ship, c0), for every exact signed idempotent P with 0 < delta(P) < (c0/4)^2 in the tall heavy near-cluster regime at a hidden top v: either v ships at least c_ship positive mass outside its rho-near top-slab cluster C, or some cluster vertex is (rho,kappa)-exposed, or every mass-carrying cluster vertex u in C with t*(u) > 0 has intersecting always-tight hulls (an alpha-free optimal display exists).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: conj-downhill-zero-face-lower-mass; lem-affine-exposer-row-capacity; lem-separator-zero-face-obstruction; lem-optimal-face-alpha-free-characterization
status: proved
af: none
provenance: W47 wave (docs/waves/2026-07-07-W47-mechanism.md): fresh-codex prover (worker AY) + SEPARATE fresh-codex hostile verifier (VAY, VALID AS CONDITIONAL — the contradiction is exactly c0*kappa <= nu_z <= delta, i.e. c0*tau/4 <= tau^2, impossible for 0 < delta < (c0/4)^2; kappa = tau/4 per CONVENTIONS; the no-shipping and no-exposure hypotheses are consumed ONLY to invoke the conjecture, not in the capacity arithmetic; t*(u) > 0 and the explicit delta-window made part of the statement)
owner: A
---

**Role (the (T2) closer, modulo one conjecture).** Contrapositive assembly: if neither
shipping nor exposure occurs and some u has disjoint hulls, the conjecture supplies a
blocker z carrying c0 positive mass in the kappa-high slab of h*_u; but z is a zero-face
row of h*_u, so [[lem-affine-exposer-row-capacity]] at z (threshold kappa) forces
c0*kappa <= nu_z <= delta — impossible in the stated delta-window. Hence all hulls meet:
exactly [[conj-zero-face-elimination]]'s intersection horn cluster-uniformly, which feeds
the rigorous pincer=>collapse=>height chain (sketch v12).

**Honest status note.** `status: proved` refers to the CONDITIONAL implication (the
conjecture is an explicit dep and hypothesis); nothing unconditional is claimed. The
conjecture is the single open input.

**Rigour tier.** Reviewed conditional (L5); af-elevation deferred until the L5 deps
(separator obstruction, characterization) elevate.
