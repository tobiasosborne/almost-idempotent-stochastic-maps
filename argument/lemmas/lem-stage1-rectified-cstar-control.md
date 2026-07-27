---
id: lem-stage1-rectified-cstar-control
kind: lemma
contract: Controlled exact-unit C*-rectification: there are universal C_rect >= 1 and e_rect in (0, 1/C_rect] such that every finite-dimensional epsilon_X-C*-algebra with 0 <= epsilon_X <= e_rect admits, on the same involutive normed space, a bilinear product bold-dot and J = J^dagger for which (calX, J, bold-dot, dagger) satisfies EVERY exact-unit epsilon_r-C*-algebra axiom of def-epsilon-cstar-algebra, including ||J|| = 1, where epsilon_r = C_rect*epsilon_X, and ||J - I_X|| <= C_rect*epsilon_X, ||x bold-dot y - xy|| <= C_rect*epsilon_X*||x||*||y||.
defs: def-epsilon-cstar-algebra
deps: lem-stage1-exact-unit-rectification; lem-stage1-quantitative-inverse-function
status: proved
af: validated
workspace: proofs/lem-stage1-rectified-cstar-control
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 1, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Source loci TeX 407-440, 672-687.
owner: A
---

**Status.** af-VALIDATED 2026-07-27 (88th rigorous result): root validated,
17/17 nodes epistemic=validated, taint clean (fresh codex prover, separate
fresh codex verifiers, routine tier; run went to a --max-rounds resume of
the same tree — converging throughout, all in-flight challenges
prover-resolved and re-verified). Export in the workspace; oracle
`af-lem-stage1-rectified-cstar-control` + `fr verify` PASS. Landed as a
`stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 1 (design budget 10/3; actual 17 nodes).

**Derivation obligation (design §4).** Reconstruct TeX 672–687 inside this
row: from its J_0, bold-dot_0 prove bilinearity, product norm, associator
bound, conjugate-linear isometric involution, exact
(x bold-dot_0 y)^dagger = y^dagger bold-dot_0 x^dagger, the lower C*-bound,
both exact unit laws, J_0^dagger = J_0, and unit closeness. For
a = ||J_0|| > 0 set J = J_0/a and x bold-dot y = a*(x bold-dot_0 y);
recheck every axiom and obtain ||J|| = 1. The landed
`lem-stage1-exact-unit-rectification` contract supplies only its advertised
exact-unit/product-closeness interface (no hidden axiom).
