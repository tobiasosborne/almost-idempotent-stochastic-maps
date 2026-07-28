---
id: lem-stage1-uniform-inversion-isolation
kind: lemma
contract: There are universal e_iso^r > 0, r_iso > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_iso^r, J and -J are the only fixed points of the smooth sigma in their respective ambient r_iso-balls.
defs: def-epsilon-cstar-algebra; def-approximate-unitary-space
deps: lem-stage1-quantitative-inverse-function; lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger
status: stated
af: none
provenance: DESIGN-S1-POLAR-v6.md sect-5 downstream row 1, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80).
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §5 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 6/3. Discharges the
"actual inversion isolation near J, -J" obligation of the corrected
`lem-stage1-extra-fixed-class` ledger (design §6).

**W97 amendment (2026-07-28, deps-only).** Deps replaced per the endorsed
rebuild design (`DESIGN-13E-BINDER-v3.md` §1.11; audit chain v3/v3.2,
final VERDICT LAND): derivative information comes from row 13 (A_7) and
smoothness/regularity of the explicit sigma from
`lem-stage1-explicit-smooth-unitary-operations` (+ atlas and smooth polar
inverse, its antecedents); the retracted control lemma and the retired
smooth-operations parent are dropped. Contract and defs BYTE-UNCHANGED.
