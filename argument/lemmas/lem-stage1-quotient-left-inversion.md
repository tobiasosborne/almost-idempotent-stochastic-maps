---
id: lem-stage1-quotient-left-inversion
kind: lemma
contract: There is a universal e_H^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_H^r, the scalar-equivariant mu, sigma and the jointly continuous projected straight paths descend to breve-calU; the descended multiplication makes it a connected H-space, and the descended smooth map breve-sigma is a left inversion.
defs: def-approximate-unitary-space; def-h-space-left-inversion; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger; lem-stage1-quotient-manifold-package
status: stated
af: none
provenance: DESIGN-S1-POLAR-v6.md sect-5 downstream row 4, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80).
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §5 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 8/3. Discharges the
"continuous H-space and left inversion; smooth breve-sigma" obligation
(design §6) from rows 5-7 and 11.

**W97 amendment (2026-07-28, deps-only).** Deps replaced per the endorsed
rebuild design (`DESIGN-13E-BINDER-v3.md` §1.11; audit chain v3/v3.2,
final VERDICT LAND): the explicit group operations and paths come from
row 13 (A_5)-(A_6); smoothness and covariance for those same maps from
`lem-stage1-explicit-smooth-unitary-operations` (+ atlas and smooth polar
inverse); coherence-naturality, the retired group-laws parent, the
path-admissibility dep, and the retired smooth-operations parent are
dropped. Contract and defs BYTE-UNCHANGED.
