---
id: lem-stage1-explicit-smooth-unitary-operations
kind: lemma
contract: Explicit smooth action/operations bridge: for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0, every family g = (g_V)_{V in calU} of C^1 maps g_V:B_{2delta}^{icalH}(0) -> B_{2delta}^{calH}(0) such that, for every V in calU and every A^par in B_{2delta}^{icalH}(0), g_V(A^par) is the unique A^perp in B_{2delta}^{calH}(0) satisfying f_V(A^par + A^perp) = 0, where f_V(A) = (1/2)*(((J + A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J + A)) - J), and such that the maps chi_V:B_{2delta}^{icalH}(0) -> calU, chi_V(A^par) = V bold-dot (J + A^par + g_V(A^par)), form a C^1 graph atlas calA_delta = {chi_V}_{V in calU} covering calU, and every smooth embedded-manifold structure calM_delta on the underlying set calU for which this displayed calA_delta is a C^infinity atlas and every displayed g_V and chi_V is C^infinity with exactly its displayed point values and C^1 differentials Dg_V and Dchi_V, suppose Pi_delta:calU x B_delta^{calH}(J) -> S_delta := Pi_delta(calU x B_delta^{calH}(J)), Pi_delta(U,H) = U bold-dot H, is a C^1 diffeomorphism onto the open set S_delta with inverse (u_delta,h_delta):S_delta -> calU x B_delta^{calH}(J) characterized by Pi_delta(u_delta(X),h_delta(X)) = X for every X in S_delta and (u_delta(Pi_delta(U,H)),h_delta(Pi_delta(U,H))) = (U,H) for every (U,H) in calU x B_delta^{calH}(J), suppose U bold-dot V and U^dagger lie in S_delta for every U,V in calU, and suppose the displayed Pi_delta and displayed inverse (u_delta,h_delta) are smooth relative to calM_delta with the same displayed point values and with smooth differentials D[(U,H) |-> U bold-dot H] and D[X |-> (u_delta(X),h_delta(X))] equal to their displayed C^1 differentials; writing alpha_C1:U(1) x calU -> calU, alpha_C1(c,U) = cU, mu_C1:calU x calU -> calU, mu_C1(U,V) = u_delta(U bold-dot V), and sigma_C1:calU -> calU, sigma_C1(U) = u_delta(U^dagger), for the resulting C^1 maps, there exist maps alpha:U(1) x calU -> calU, mu:calU x calU -> calU, and sigma:calU -> calU that are smooth relative to calM_delta and satisfy alpha(c,U) = alpha_C1(c,U) = cU, mu(U,V) = mu_C1(U,V) = u_delta(U bold-dot V), sigma(U) = sigma_C1(U) = u_delta(U^dagger), Dalpha = Dalpha_C1, Dmu = Dmu_C1, Dsigma = Dsigma_C1, mu(cU,dV) = c*d*mu(U,V), and sigma(cU) = conj(c)*sigma(U) for every U,V in calU and c,d in U(1).
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-unitary-graph-control; lem-stage1-polar-retraction; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse
status: stated
af: seeded
workspace: proofs/lem-stage1-explicit-smooth-unitary-operations
provenance: DESIGN-13E-BINDER-v3.2.md (binder-closed contract, token-diff-verified transcription of the AUDIT-13E-BINDER-v3.1.md finding-1 prescribed repair), amending DESIGN-13E-BINDER-v3.1.md sect-1 / DESIGN-13E-BINDER-v3.md sect-1.3; AUDIT-13E-BINDER-v3.2.md VERDICT LAND; landing per audit-v3 finding 3.
owner: A
---

**Status.** `stated` candidate landed VERBATIM from
`DESIGN-13E-BINDER-v3.2.md` (the quantifier-closed v3.2 contract, NOT
the v3/v3.1 drafts; elevation queue row 3, target/hard cap 12/18).
Binder-closed replacement for the retired anaphoric parent
`lem-stage1-smooth-unitary-operations`: every former anaphor has a
contract-local typed referent (g_V by its unique zero-equation property,
chi_V by formula, calA_delta the displayed covering atlas, calM_delta the
quantified smooth structure, Pi_delta and (u_delta, h_delta) displayed
with both typed inverse identities, the C^1 maps alpha_C1/mu_C1/sigma_C1
displayed before the smooth alpha/mu/sigma are quantified). Covariance
via bilinearity + ordinary injectivity of the one displayed Pi_delta; no
coherence external and no retired parent is used.

**Build-granularity discipline (BINDING on the af tree; extends the
user-ratified row-1 discipline of 2026-07-28 — run-1 there ABORTED
[BALLOON] from sub-splitting routine norm estimates).** The target is the
design's 12-node skeleton (hard cap 18). Tree discipline: (i) fix the
typed providers EARLY, one node — the graph family from the displayed
unitary-graph-control external, the displayed polar inverse from the
polar-retraction external, its atlas/smooth upgrades from the atlas and
smooth-polar-inverse externals, input membership from the
group-domain-membership external — before any operation map is treated;
(ii) per design v3 sect-1.3: the scalar action is the restriction and
corestriction of ambient scalar multiplication (ONE node), smoothness of
mu and sigma by composition of the displayed smooth maps (ONE node each),
covariance via bilinearity + ordinary injectivity of the ONE displayed
Pi_delta (ONE node per formula) — one node per design-skeleton step, do
NOT sub-split routine composition/restriction arguments. Constants live
in the proof body, never the contract; every smallness inference cites
its guard node explicitly.
