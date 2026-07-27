---
id: lem-stage1-polar-retraction
kind: lemma
contract: Closed C^1 polar retraction: there are universal C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, Pi_delta(U, H) = U bold-dot H is a C^1 diffeomorphism from calU x B^{calH}_delta(J) onto an open S_delta, its inverse (u_delta, h_delta) obeys X = u_delta(X) bold-dot h_delta(X), u_delta(U) = U, h_delta(U) = J, and calU_{delta - C_pol*(epsilon_r*delta + delta^2)} subseteq S_delta subseteq calU_{delta + C_pol*(epsilon_r*delta + delta^2)}.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-unitary-graph-control
status: stated
af: seeded
workspace: proofs/lem-stage1-polar-retraction
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 4, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Source loci TeX 809-855; the two radii are inlined and only the supported shrunken inner domain is used.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 4 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 12/3.

**Derivation obligation (design §4).** TeX 809–843 supplies the C^1
bijection and losses. Use the smaller inner set and never claim the
unsupported larger line-845 source.
