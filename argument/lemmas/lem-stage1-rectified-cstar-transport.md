---
id: lem-stage1-rectified-cstar-transport
kind: lemma
contract: Parameterized rectification transport: there exist C_rect^0 >= 1 and e_rect^0 in (0, 1/C_rect^0] such that, for every def-stage1-polar-witness-data tuple W with C_rect >= C_rect^0 and 0 < e_rect <= min{e_rect^0, 1/C_rect}, for every finite-dimensional epsilon_X-C*-algebra (calX, I_X, ., dagger) with 0 <= epsilon_X <= e_rect, there are on the same involutive normed space a bilinear product bold-dot and an element J = J^dagger for which (calX, J, bold-dot, dagger) satisfies every exact-unit epsilon_r-C*-algebra axiom of def-epsilon-cstar-algebra, including ||J|| = 1, where epsilon_r = C_rect*epsilon_X, and for every x, y in calX, ||J - I_X|| <= C_rect*epsilon_X and ||x bold-dot y - xy|| <= C_rect*epsilon_X*||x||*||y||.
defs: def-stage1-polar-witness-data; def-epsilon-cstar-algebra
deps: lem-stage1-rectified-cstar-control
status: stated
af: seeded
workspace: proofs/lem-stage1-rectified-cstar-transport
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13a, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 407-440, 672-687; parameterized coefficient/radius monotonicity; AUDIT-S1-POLAR-v4.md sect-3.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 13a (final verdict LAND; audit-v5:
unchanged-VALID). Not proved in-repo; af elevation per the design's
projected budget 4/2 (root, producer-witness instantiation, parameterized
monotonicity, assembly).
