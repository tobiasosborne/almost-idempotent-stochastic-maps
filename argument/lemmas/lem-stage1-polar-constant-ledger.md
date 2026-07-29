---
id: lem-stage1-polar-constant-ledger
kind: lemma
contract: Compatible Stage-1 polar witnesses and range: there exists one universal def-stage1-polar-witness-data tuple W = (C_rect, C_ch, C_pol, C_grp, C_path, C_der, e_rect, kappa_ch, kappa_pol, kappa_der, delta_*, epsilon_*^r, e_S1, r_iso), with C_rect, C_ch, C_pol, C_grp, C_path, C_der >= 1, 0 < e_rect <= 1/C_rect, and 0 < kappa_ch, kappa_pol, kappa_der <= 1/2, such that all of the following hold simultaneously: (A_1) for every finite-dimensional epsilon_X-C*-algebra (calX, I_X, ., dagger) with 0 <= epsilon_X <= e_rect, there are on the same involutive normed space a bilinear product bold-dot and an element J = J^dagger for which (calX, J, bold-dot, dagger) satisfies every exact-unit epsilon_r-C*-algebra axiom of def-epsilon-cstar-algebra, including ||J|| = 1, where epsilon_r = C_rect*epsilon_X, and for every x, y in calX, ||J - I_X|| <= C_rect*epsilon_X and ||x bold-dot y - xy|| <= C_rect*epsilon_X*||x||*||y||; (A_2) for every finite-dimensional exact-unit epsilon_r-C*-algebra (calX, J, bold-dot, dagger), every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, every V in calUbar_delta, and every A^par in B^{icalH}_{2delta}(0), there is a unique g_V(A^par) in B^{calH}_{2delta}(0) such that f_V(A^par + g_V(A^par)) = 0, where f_V(A) = (1/2)*(((J + A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J + A)) - J), the element V bold-dot (J + A^par + g_V(A^par)) lies in calU, ||g_V(A^par) + (1/2)*(V^dagger bold-dot V - J)|| <= C_ch*(epsilon_r*delta + delta^2), ||Dg_V(A^par)|| <= C_ch*(epsilon_r + delta), and ||D_{A^perp} f_V(A^par + g_V(A^par)) - I_{calH}|| <= C_ch*(epsilon_r + delta) < 1, and these C^1 graph charts cover calU; (A_3) for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, and every family g = (g_U)_{U in calU} of C^1 maps g_U: B^{icalH}_{2delta}(0) -> B^{calH}_{2delta}(0) such that, for every U in calU and A^par in B^{icalH}_{2delta}(0), g_U(A^par) is the unique element of B^{calH}_{2delta}(0) satisfying f_U(A^par + g_U(A^par)) = 0, where f_U(A) = (1/2)*(((J + A^dagger) bold-dot U^dagger) bold-dot (U bold-dot (J + A)) - J), every tangent space T_U calU is the image of L_U(I + Dg_U(0)): icalH -> calX, and omega_U(Z) = (L_U^{-1} Z)^par : T_U calU -> icalH is a global C^1 bundle trivialization with distortion at most 1 + C_ch*epsilon_r, satisfying omega_{cU}(cZ) = omega_U(Z) and omega_U(iU) = iJ for every U in calU, Z in T_U calU, and c in U(1); (A_4) for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, the map Pi_delta: calU x B^{calH}_delta(J) -> calX, Pi_delta(U, H) = U bold-dot H, is a C^1 diffeomorphism onto the open set S_delta := Pi_delta(calU x B^{calH}_delta(J)), its inverse (u_delta, h_delta): S_delta -> calU x B^{calH}_delta(J) satisfies X = u_delta(X) bold-dot h_delta(X), u_delta(U) = U, and h_delta(U) = J for every X in S_delta and U in calU, and calU_{delta - C_pol*(epsilon_r*delta + delta^2)} subseteq S_delta subseteq calU_{delta + C_pol*(epsilon_r*delta + delta^2)}; (A_5) for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the formulas mu(U, V) = u_delta(U bold-dot V) and sigma(U) = u_delta(U^dagger) define C^1 maps on all of calU x calU and calU, respectively, and for every U, V, Z in calU, mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), Z) - mu(U, mu(V, Z))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r; (A_6) for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, every U_0, U_1 in calU, and every q in [0, 1] satisfying ||U_1 - U_0|| <= q, C_path*q <= 1/4, and C_path*(q + epsilon_r*q + q^2) < delta - C_pol*(epsilon_r*delta + delta^2), every L_{Z_t} is invertible and every Z_t = (1-t)*U_0 + t*U_1 lies in calUbar_{C_path*(q + epsilon_r*q + q^2)} for t in [0, 1], and, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the map H(t, U_0, U_1) = u_delta(Z_t) is jointly continuous in (t, U_0, U_1), joins U_0 to U_1, and satisfies H(t, cU_0, cU_1) = c*H(t, U_0, U_1) for every c in U(1); (A_7) for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0, every s in {+1, -1}, and every 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, and g_{sJ}: B_{2delta}^{icalH}(0) -> B_{2delta}^{calH}(0) for the unique C^1 map such that, for every A in B_{2delta}^{icalH}(0), f_{sJ}(A + g_{sJ}(A)) = 0, where f_{sJ}(B) = (1/2)*(((J + B^dagger) bold-dot (sJ)^dagger) bold-dot (sJ bold-dot (J + B)) - J), define chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)) and the global C^1 map sigma(U) = u_delta(U^dagger); then sigma maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart and, with F_s(A) = phi_{sJ}^par(sigma(chi_s(A))), one has ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for every A in B_r^{icalH}(0); and (R) delta_* = min{1/4, kappa_ch/(4*C_ch), kappa_pol/(4*C_pol)}, epsilon_*^r = min{1/4, kappa_ch/(4*C_ch), kappa_pol/(4*C_pol), kappa_der/(8*C_der), 1/C_grp, delta_*/(12*C_path*C_grp)}, e_S1 = min{e_rect, epsilon_*^r/C_rect}, r_iso = min{delta_*/4, kappa_der/(8*C_der)}, and for every 0 <= epsilon_X <= e_S1, on setting epsilon_r = C_rect*epsilon_X, q = C_grp*epsilon_r, r_- = delta_* - C_pol*(epsilon_r*delta_* + delta_*^2), and eta = C_path*(q + epsilon_r*q + q^2), one has C_ch*(epsilon_r + delta_*) <= kappa_ch, C_pol*(epsilon_r + delta_*) <= kappa_pol, q < r_-, C_path*q <= 1/4, eta < r_-, C_der*(epsilon_r + r_iso) <= kappa_der, (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta_*))*r_iso + q < 2*delta_*, r_- >= 3*delta_*/4, eta <= delta_*/4, and C_der*(r_iso + epsilon_r) <= kappa_der/4 < 1.
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-rectified-cstar-transport; lem-stage1-unitary-graph-transport; lem-stage1-maurer-cartan-transport; lem-stage1-polar-retraction-transport; lem-stage1-approximate-group-laws-transport; lem-stage1-polar-path-transport; lem-stage1-inversion-derivative-transport; lem-stage1-polar-scalar-arithmetic
status: proved
af: validated
workspace: proofs/lem-stage1-polar-constant-ledger
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional insertions in (A_5)-(A_7), audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 458 plus finite maxima/minima of the seven helper base witnesses; object-level monotonicity discharged in the helper rows; AUDIT-S1-POLAR-v4.md sect-1.3, 1.5-1.7, 2.2, 3, 6.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 13 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 11/3 (root, tuple
selection/range, seven helper applications, one arithmetic application,
final conjunction assembly — below the 12/3 cap; the rejected unfactored
projection is 18/4).

**What the consumer receives (design §2).** The literal assertion
"exists W (AnalyticWitnesses(W) AND Arithmetic(W))" — one tuple
simultaneously witnessing all seven analytic producers and the scalar
arithmetic — NOT the invalid v2 pair of an arithmetic existential plus
unrelated analytic existentials. Both predicates are expanded object-level
in the contract itself.

**Derivation obligation (design §4).** Obtain the seven helper base-witness
packages, take finite maxima of their coefficients and finite minima of
their margins, choose the one receiving tuple W, apply each parameterized
helper and the universal scalar-arithmetic result, then assemble the eight
clauses.

**Build-granularity discipline (BINDING on the af tree; extends the
user-ratified W98 row-1 discipline of 2026-07-28 — that run-1 ABORTED
[BALLOON] from sub-splitting routine norm estimates).** The target is
the design's 11-node skeleton (hard cap 12; the rejected unfactored
projection was 18/4): root; ONE tuple-selection/range node (finite
maxima of the seven helper base coefficients, finite minima of their
margins, the one receiving tuple W, and the (R) scalar definitions);
ONE node per helper application (seven: 13a-13g at W, each a
monotonicity instantiation of the displayed parameterized external);
ONE scalar-arithmetic application node; ONE final conjunction-assembly
node. Do NOT sub-split routine max/min monotonicity steps or the (R)
inequality chain (that chain is exactly the scalar-arithmetic
external's conclusion at the chosen tuple). Constants live in the proof
body, never the contract.

**af-VALIDATED 2026-07-29 (W98 session, first post-queue elevation).**
The keystone single-tuple ledger: consumes all seven transports
13a-13g (four of them banked the same day) + scalar arithmetic.
Consumer re-check performed mechanically before seeding: clauses
(A_5)/(A_6)/(A_7) byte-identical to the 13e/13f/13g contract bodies
(modulo the terminal period). First-pass run under the binding
build-granularity discipline above (tier routine, fresh codex verifier
per node): root validated, 11/11 live nodes (EXACTLY the design
budget; hard cap 12), taint clean, 3 rounds, ZERO challenges. Export
in the workspace; oracle `af-lem-stage1-polar-constant-ledger` +
`fr verify` PASS. This status flip is a mechanical reflection of the
codex ledger.
