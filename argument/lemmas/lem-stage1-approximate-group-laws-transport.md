---
id: lem-stage1-approximate-group-laws-transport
kind: lemma
contract: Parameterized approximate-group transport: there exist C_grp^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_grp >= C_grp^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the formulas mu(U, V) = u_delta(U bold-dot V) and sigma(U) = u_delta(U^dagger) define C^1 maps on all of calU x calU and calU, respectively, and for every U, V, Z in calU, mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), Z) - mu(U, mu(V, Z))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-approximate-group-laws; lem-stage1-polar-retraction
status: stated
af: seeded
workspace: proofs/lem-stage1-approximate-group-laws-transport
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13e, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional domain restriction, audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 845-878; parameterized estimate/guard monotonicity; AUDIT-S1-POLAR-v4.md sect-1.5, sect-3.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 13e (final verdict LAND; the v5-audit
all-domain polar-inverse defect is CLEARED-BY the finite-dimensional
insertion matched to base row 6 and polar row 4). Not proved in-repo;
af elevation per the design's projected budget 4/2.

**STUCK repair (2026-07-27, W93 run 1).** The af run aborted STUCK: three
verifier challenges correctly identified that the contract's binder "the
unique inverse (u_delta, h_delta) of Pi_delta" is not derivable from the
sole original dep (whose contract mentions only u_delta on its own
hypotheses). The missing fact is exactly the af-validated
`lem-stage1-polar-retraction` (existence, uniqueness, and the two-component
inverse of Pi_delta on calU x B^calH_delta(J)); it was added as a second
dep and byte-matched workspace external. Contract BYTE-UNCHANGED.
