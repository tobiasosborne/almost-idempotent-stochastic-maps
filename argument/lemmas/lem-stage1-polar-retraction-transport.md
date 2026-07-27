---
id: lem-stage1-polar-retraction-transport
kind: lemma
contract: Parameterized polar-retraction transport: there exist C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_pol >= C_pol^0 and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, the map Pi_delta: calU x B^{calH}_delta(J) -> calX, Pi_delta(U, H) = U bold-dot H, is a C^1 diffeomorphism onto the open set S_delta := Pi_delta(calU x B^{calH}_delta(J)), its inverse (u_delta, h_delta): S_delta -> calU x B^{calH}_delta(J) satisfies X = u_delta(X) bold-dot h_delta(X), u_delta(U) = U, and h_delta(U) = J for every X in S_delta and U in calU, and calU_{delta - C_pol*(epsilon_r*delta + delta^2)} subseteq S_delta subseteq calU_{delta + C_pol*(epsilon_r*delta + delta^2)}.
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
status: proved
af: validated
workspace: proofs/lem-stage1-polar-retraction-transport
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13d, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 809-855; parameterized loss/guard monotonicity; AUDIT-S1-POLAR-v4.md sect-3.
owner: A
---

**Status.** af-VALIDATED 2026-07-27 (105th rigorous result): first-pass —
root validated, 5/5 nodes, taint clean (tier routine, zero challenges).
Export in the workspace; oracle `af-lem-stage1-polar-retraction-transport`
+ `fr verify` PASS. Landed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 13d (final verdict LAND; audit-v5:
unchanged-VALID incl. both sandwich monotonicity directions).
