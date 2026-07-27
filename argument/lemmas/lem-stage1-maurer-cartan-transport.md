---
id: lem-stage1-maurer-cartan-transport
kind: lemma
contract: Parameterized Maurer-Cartan transport: there exist C_ch^0 >= 1 and kappa_ch^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_ch >= C_ch^0 and 0 < kappa_ch <= kappa_ch^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, and every family g = (g_U)_{U in calU} of C^1 maps g_U: B^{icalH}_{2delta}(0) -> B^{calH}_{2delta}(0) such that, for every U in calU and A^par in B^{icalH}_{2delta}(0), g_U(A^par) is the unique element of B^{calH}_{2delta}(0) satisfying f_U(A^par + g_U(A^par)) = 0, where f_U(A) = (1/2)*(((J + A^dagger) bold-dot U^dagger) bold-dot (U bold-dot (J + A)) - J), every tangent space T_U calU is the image of L_U(I + Dg_U(0)): icalH -> calX, and omega_U(Z) = (L_U^{-1} Z)^par : T_U calU -> icalH is a global C^1 bundle trivialization with distortion at most 1 + C_ch*epsilon_r, satisfying omega_{cU}(cZ) = omega_U(Z) and omega_U(iU) = iJ for every U in calU, Z in T_U calU, and c in U(1).
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-maurer-cartan-trivialization
status: proved
af: validated
workspace: proofs/lem-stage1-maurer-cartan-transport
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13c, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 795-807; parameterized distortion/guard monotonicity; AUDIT-S1-POLAR-v4.md sect-1.3, sect-3.
owner: A
---

**Status.** af-VALIDATED 2026-07-27 (104th rigorous result): root
validated, 13/13 nodes, taint clean (tier routine; two genuine
challenges — the gbar unique-zero identification was proved only
conditionally on nodes 1.3/1.3.2 — repaired in-run, all nodes accepted
by round 10). Export in the workspace; oracle
`af-lem-stage1-maurer-cartan-transport` + `fr verify` PASS. Landed
VERBATIM from the audited `DESIGN-S1-POLAR-v6.md` §3 row 13c (final
verdict LAND; audit-v5: unchanged-VALID incl. the minimal unique-zero
binder).
