---
id: lem-stage1-unitary-graph-control
kind: lemma
contract: Uniform unitary graph control: there are universal C_ch >= 1, kappa_ch in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, every V in calUbar_delta, and every A^par in B^{icalH}_{2delta}(0), there is a unique g_V(A^par) in B^{calH}_{2delta}(0) with f_V(A^par + g_V(A^par)) = 0, and the corresponding V bold-dot (J + A^par + g_V(A^par)) lies in calU, where f_V(A) = (1/2)*(((J + A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J + A)) - J); moreover ||g_V(A^par) + (1/2)*(V^dagger bold-dot V - J)|| <= C_ch*(epsilon_r*delta + delta^2), ||Dg_V(A^par)|| <= C_ch*(epsilon_r + delta), and ||D_{A^perp} f_V(A^par + g_V(A^par)) - I_{calH}|| <= C_ch*(epsilon_r + delta) < 1; the resulting C^1 graph charts cover calU.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-quantitative-inverse-function; lem-stage1-rectified-cstar-control
status: stated
af: none
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 2, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Source loci TeX 692-793, especially 728-793.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 2 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 8/3.

**Derivation obligation (design §4).** Replace the fixed finite list of
O(epsilon_r + delta) and O(epsilon_r*delta + delta^2) terms at TeX 758–793
by one coefficient/margin pair. The right-inverse and normal-derivative
Neumann steps use TeX 699–725.
