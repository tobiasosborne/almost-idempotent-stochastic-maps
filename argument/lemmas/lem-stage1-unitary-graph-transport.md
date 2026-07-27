---
id: lem-stage1-unitary-graph-transport
kind: lemma
contract: Parameterized unitary-graph transport: there exist C_ch^0 >= 1 and kappa_ch^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_ch >= C_ch^0 and 0 < kappa_ch <= kappa_ch^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra (calX, J, bold-dot, dagger), every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, every V in calUbar_delta, and every A^par in B^{icalH}_{2delta}(0), there is a unique g_V(A^par) in B^{calH}_{2delta}(0) such that f_V(A^par + g_V(A^par)) = 0, where f_V(A) = (1/2)*(((J + A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J + A)) - J), the element V bold-dot (J + A^par + g_V(A^par)) lies in calU, ||g_V(A^par) + (1/2)*(V^dagger bold-dot V - J)|| <= C_ch*(epsilon_r*delta + delta^2), ||Dg_V(A^par)|| <= C_ch*(epsilon_r + delta), and ||D_{A^perp} f_V(A^par + g_V(A^par)) - I_{calH}|| <= C_ch*(epsilon_r + delta) < 1, and these C^1 graph charts cover calU.
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-unitary-graph-control
status: stated
af: none
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13b, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 692-793; parameterized coefficient/margin monotonicity; AUDIT-S1-POLAR-v4.md sect-3.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 13b (final verdict LAND; audit-v5:
unchanged-VALID incl. the strict normal-derivative conclusion). Not proved
in-repo; af elevation per the design's projected budget 4/2.
