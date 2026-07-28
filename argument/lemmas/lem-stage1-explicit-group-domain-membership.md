---
id: lem-stage1-explicit-group-domain-membership
kind: lemma
contract: Explicit group-input polar-domain membership: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU is defined at U bold-dot V and U^dagger for every U, V in calU; moreover, U bold-dot V and U^dagger each have a right inverse.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
status: stated
af: seeded
workspace: proofs/lem-stage1-explicit-group-domain-membership
provenance: DESIGN-13E-BINDER-v3.md sect-1.1, landed verbatim (W97 explicit-binder rebuild); AUDIT-13E-BINDER-v3.md (math endorsed; REJECT on process grounds repaired by v3.1/v3.2); AUDIT-13E-BINDER-v3.2.md VERDICT LAND; landing per audit-v3 finding 3.
owner: A
---

**Status.** `stated` candidate landed VERBATIM from the hostile-endorsed
W97 rebuild design (`DESIGN-13E-BINDER-v3.md` §1.1; elevation queue
row 1, target/hard cap 10/14). Binder-closed replacement bridge for the
retired anaphoric parent `lem-stage1-approximate-group-laws`: the typed
pair (u_delta, h_delta) is obtained from the displayed polar-retraction
inverse BEFORE either group input is treated; the sound anaphoric child
`lem-stage1-group-domain-membership` is evidence for the calculation,
not an external. Governed by the two BINDING process laws of
`docs/LEARNINGS.md` 2026-07-28 (typed-witness providers; fixed provider
witnesses before receiving tuples).
