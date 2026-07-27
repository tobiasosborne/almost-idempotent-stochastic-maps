---
id: lem-stage1-polar-coherence-naturality
kind: lemma
contract: Polar coherence and scalar naturality: for every exact-unit algebra and every two polar data (delta_j, S_j, u_j, h_j), j = 1, 2, for which Pi_{delta_j}: calU x B^{calH}_{delta_j}(J) -> S_j, (U, H) |-> U bold-dot H, is bijective with inverse (u_j, h_j), one has (u_1, h_1) = (u_2, h_2) on S_1 intersect S_2; moreover, for c in U(1) and X, cX in S_j, u_j(cX) = c*u_j(X) and h_j(cX) = h_j(X).
defs: def-approximate-unitary-space
deps: lem-stage1-polar-retraction
status: proved
af: validated
workspace: proofs/lem-stage1-polar-coherence-naturality
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 5, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Source loci TeX 809-845, 945; uniqueness and bilinearity derivation.
owner: A
---

**Status.** af-VALIDATED 2026-07-27 (92nd rigorous result): root validated,
10/10 nodes epistemic=validated, taint clean, single run, routine tier
(design budget 3/2). Export in the workspace; oracle
`af-lem-stage1-polar-coherence-naturality` + `fr verify` PASS. Landed as a
`stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 5. NOTE (audit-v5, carried):
this row is conditional coherence/naturality with no free polar witness —
it is never used as an existence assertion.

**Derivation obligation (design §4).** Use injectivity on common
decompositions; bilinearity gives the scalar identities.
