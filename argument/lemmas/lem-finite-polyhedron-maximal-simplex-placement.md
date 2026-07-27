---
id: lem-finite-polyhedron-maximal-simplex-placement
kind: lemma
contract: Every point of a finite polyhedron lies in a maximal simplex of its defining finite simplicial complex; therefore every finite fixed set does.
defs:
deps:
status: stated
af: none
provenance: DESIGN-S1-POLAR-v6.md sect-5 (downstream row 6), landed verbatim; AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Algebra-independent finite-poset derivation; consumes none of the analytic rows.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §5 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 2/1. Algebra-independent:
a finite partially-ordered-set argument (every simplex is contained in a
maximal one; finitely many simplices), added by the audits as required
input 10 of the corrected `lem-stage1-extra-fixed-class` dependency list
(design §6).
