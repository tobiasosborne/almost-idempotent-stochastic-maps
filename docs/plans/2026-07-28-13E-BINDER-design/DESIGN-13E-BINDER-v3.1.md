# DESIGN v3.1 — narrow binder repair

## 1. Replacement for v3 §1.3 and elevation row 3

```text
contract: Explicit smooth action/operations bridge: for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0, every family g = (g_V)_{V in calU} of C^1 maps g_V:B_{2delta}^{icalH}(0) -> B_{2delta}^{calH}(0) such that g_V(A^par) is the unique A^perp in B_{2delta}^{calH}(0) satisfying f_V(A^par + A^perp) = 0, where f_V(A) = (1/2)*(((J + A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J + A)) - J), and such that the maps chi_V:B_{2delta}^{icalH}(0) -> calU, chi_V(A^par) = V bold-dot (J + A^par + g_V(A^par)), form a C^1 graph atlas calA_delta = {chi_V}_{V in calU} covering calU, and every smooth embedded-manifold structure calM_delta on the underlying set calU for which this displayed calA_delta is a C^infinity atlas and every displayed g_V and chi_V is C^infinity with exactly its displayed point values and C^1 differentials Dg_V and Dchi_V, suppose Pi_delta:calU x B_delta^{calH}(J) -> S_delta := Pi_delta(calU x B_delta^{calH}(J)), Pi_delta(U,H) = U bold-dot H, is a C^1 diffeomorphism onto the open set S_delta with inverse (u_delta,h_delta):S_delta -> calU x B_delta^{calH}(J) characterized by Pi_delta(u_delta(X),h_delta(X)) = X and (u_delta(Pi_delta(U,H)),h_delta(Pi_delta(U,H))) = (U,H), suppose U bold-dot V and U^dagger lie in S_delta for every U,V in calU, and suppose the displayed Pi_delta and displayed inverse (u_delta,h_delta) are smooth relative to calM_delta with the same displayed point values and with smooth differentials D[(U,H) |-> U bold-dot H] and D[X |-> (u_delta(X),h_delta(X))] equal to their displayed C^1 differentials; writing alpha_C1:U(1) x calU -> calU, alpha_C1(c,U) = cU, mu_C1:calU x calU -> calU, mu_C1(U,V) = u_delta(U bold-dot V), and sigma_C1:calU -> calU, sigma_C1(U) = u_delta(U^dagger), for the resulting C^1 maps, there exist maps alpha:U(1) x calU -> calU, mu:calU x calU -> calU, and sigma:calU -> calU that are smooth relative to calM_delta and satisfy alpha(c,U) = alpha_C1(c,U) = cU, mu(U,V) = mu_C1(U,V) = u_delta(U bold-dot V), sigma(U) = sigma_C1(U) = u_delta(U^dagger), Dalpha = Dalpha_C1, Dmu = Dmu_C1, Dsigma = Dsigma_C1, mu(cU,dV) = c*d*mu(U,V), and sigma(cU) = conj(c)*sigma(U) for every U,V in calU and c,d in U(1).
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-unitary-graph-control; lem-stage1-polar-retraction; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse
```

Classification: **NEW**. The target / hard live-node cap remains **12 / 18**: the redraft exposes one provider that was previously only implicit, but adds no mathematical branch to the scalar/product/adjoint argument.

Exact external-registration list:

```text
def-approximate-unitary-space; def-epsilon-cstar-algebra; lem-stage1-explicit-group-domain-membership; lem-stage1-unitary-graph-control; lem-stage1-polar-retraction; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse
```

Every former anaphor now has a contract-local typed referent: `g_V` is quantified with its unique zero-equation property, `chi_V` is displayed by formula, `calA_delta` is the displayed covering graph atlas, and `calM_delta` is quantified as the smooth embedded-manifold structure carrying precisely that atlas and its unchanged point values and differentials. Likewise `Pi_delta` is displayed by source, image-defined target, and formula, while `(u_delta,h_delta)` is displayed by both inverse identities; their smooth upgrades are tied to those exact C^1 maps by explicit value and differential equalities. Finally, the C^1 maps `alpha_C1`, `mu_C1`, and `sigma_C1` are displayed before the smooth maps `alpha`, `mu`, and `sigma` are quantified, and the six point/derivative equalities state exactly what is preserved. Accordingly `lem-stage1-unitary-graph-control` is newly registered as the typed provider of the graph family; the other registrations provide, respectively, input membership, the displayed polar inverse, its atlas upgrade, and its smooth upgrade.

## 2. MINOR-5 classification repair

| registry row | classification | dependency/binder re-check |
|---|---|---|
| `lem-finite-polyhedron-maximal-simplex-placement` | **BYTE-UNCHANGED / NO-DEPENDENCY / NO-BINDER** | Its actual `defs:` and `deps:` fields are empty, its finite-poset contract is algebra-independent, and it contains no Stage-1 definite description or binder to synchronize. No registry, workspace, or consumer action is required, and the touched-shard count is unchanged. |

## 3. Delta

This v3.1 note replaces only `DESIGN-13E-BINDER-v3.md` §1.3 and §2 elevation row 3, and adds the explicit MINOR-5 classification row above. Everything else in `DESIGN-13E-BINDER-v3.md` is unchanged.
