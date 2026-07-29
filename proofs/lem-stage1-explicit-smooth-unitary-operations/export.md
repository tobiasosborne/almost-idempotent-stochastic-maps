# Proof Export

## Node 1

**Statement:** Explicit smooth action/operations bridge: for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0, every family g = (g_V)_{V in calU} of C^1 maps g_V:B_{2delta}^{icalH}(0) -> B_{2delta}^{calH}(0) such that, for every V in calU and every A^par in B_{2delta}^{icalH}(0), g_V(A^par) is the unique A^perp in B_{2delta}^{calH}(0) satisfying f_V(A^par + A^perp) = 0, where f_V(A) = (1/2)*(((J + A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J + A)) - J), and such that the maps chi_V:B_{2delta}^{icalH}(0) -> calU, chi_V(A^par) = V bold-dot (J + A^par + g_V(A^par)), form a C^1 graph atlas calA_delta = {chi_V}_{V in calU} covering calU, and every smooth embedded-manifold structure calM_delta on the underlying set calU for which this displayed calA_delta is a C^infinity atlas and every displayed g_V and chi_V is C^infinity with exactly its displayed point values and C^1 differentials Dg_V and Dchi_V, suppose Pi_delta:calU x B_delta^{calH}(J) -> S_delta := Pi_delta(calU x B_delta^{calH}(J)), Pi_delta(U,H) = U bold-dot H, is a C^1 diffeomorphism onto the open set S_delta with inverse (u_delta,h_delta):S_delta -> calU x B_delta^{calH}(J) characterized by Pi_delta(u_delta(X),h_delta(X)) = X for every X in S_delta and (u_delta(Pi_delta(U,H)),h_delta(Pi_delta(U,H))) = (U,H) for every (U,H) in calU x B_delta^{calH}(J), suppose U bold-dot V and U^dagger lie in S_delta for every U,V in calU, and suppose the displayed Pi_delta and displayed inverse (u_delta,h_delta) are smooth relative to calM_delta with the same displayed point values and with smooth differentials D[(U,H) |-> U bold-dot H] and D[X |-> (u_delta(X),h_delta(X))] equal to their displayed C^1 differentials; writing alpha_C1:U(1) x calU -> calU, alpha_C1(c,U) = cU, mu_C1:calU x calU -> calU, mu_C1(U,V) = u_delta(U bold-dot V), and sigma_C1:calU -> calU, sigma_C1(U) = u_delta(U^dagger), for the resulting C^1 maps, there exist maps alpha:U(1) x calU -> calU, mu:calU x calU -> calU, and sigma:calU -> calU that are smooth relative to calM_delta and satisfy alpha(c,U) = alpha_C1(c,U) = cU, mu(U,V) = mu_C1(U,V) = u_delta(U bold-dot V), sigma(U) = sigma_C1(U) = u_delta(U^dagger), Dalpha = Dalpha_C1, Dmu = Dmu_C1, Dsigma = Dsigma_C1, mu(cU,dV) = c*d*mu(U,V), and sigma(cU) = conj(c)*sigma(U) for every U,V in calU and c,d in U(1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix an arbitrary finite-dimensional exact-unit epsilon_r-C*-algebra, delta>0, and arbitrary displayed witnesses g=(g_V), chi_V, calA_delta, calM_delta, Pi_delta, and (u_delta,h_delta) satisfying every antecedent of node 1. Thus calM_delta is the stipulated smooth embedded-manifold structure on the same underlying set calU; Pi_delta and its inverse are the one displayed mutually inverse pair; U bold-dot V and U^dagger are in S_delta for all U,V in calU; and alpha_C1, mu_C1, sigma_C1 are the stipulated well-defined C^1 maps. Proving the requested conclusions for these arbitrary data permits universal generalization.

**Type:** local_assume

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The contract-local witnesses are typed independently of any opaque anaphor. When their respective guards hold, lem-stage1-unitary-graph-control supplies the uniquely characterized graph family and covering C^1 charts, lem-stage1-polar-retraction supplies the displayed polar bijection and inverse, lem-stage1-smooth-unitary-atlas and lem-stage1-smooth-polar-inverse supply the same pointwise maps with unchanged first derivatives as smooth maps, and lem-stage1-explicit-group-domain-membership supplies the two S_delta memberships. Node 1 itself explicitly assumes precisely the needed typed properties for the arbitrary witnesses fixed in 1.1, so no smallness guard or existence assertion is inferred here; hence all later occurrences refer only to those fixed displayed witnesses.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The ambient scalar-multiplication map s_tilde:C x calX -> calX, s_tilde(z,X)=zX, the ambient algebra multiplication b:calX x calX -> calX, b(X,Y)=X bold-dot Y, and the involution q:calX -> calX, q(X)=X^dagger, are smooth as real maps: s_tilde is continuous complex-bilinear by the Banach-space structure, b is continuous complex-bilinear by def-epsilon-cstar-algebra, and q is continuous conjugate-linear (indeed isometric) by def-epsilon-cstar-algebra. Since U(1) is a smooth embedded submanifold of C, the restriction s:=s_tilde|_{U(1) x calX}:U(1) x calX -> calX is smooth as a real manifold map; no bilinearity is asserted for this restricted map. Restricting s, b, and q further to products involving the smooth embedded manifold calM_delta gives smooth ambient-valued maps. Moreover the stipulated codomain of alpha_C1 ensures s(c,U)=cU lies in calU, while the membership antecedent ensures b(U,V)=U bold-dot V and q(U)=U^dagger lie in S_delta for all U,V in calU and c in U(1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The scalar action alpha_C1 is smooth relative to calM_delta. Indeed it is exactly the restriction of the smooth ambient scalar multiplication s from 1.3 to U(1) x calM_delta, with image in the embedded submanifold calM_delta by its stipulated codomain. The standard initial property of a smooth embedded submanifold therefore makes the same map, corestricted to calM_delta, smooth.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The multiplication map mu_C1 is smooth relative to calM_delta. The restricted ambient bilinear map b:calM_delta x calM_delta -> calX is smooth by 1.3 and has image in the open set S_delta by the membership antecedent. Hence it is smooth as an S_delta-valued map; composing it with the stipulated smooth first polar-inverse component u_delta:S_delta -> calM_delta gives (U,V) |-> u_delta(U bold-dot V)=mu_C1(U,V).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** The inversion map sigma_C1 is smooth relative to calM_delta. The restricted involution q:calM_delta -> calX is smooth by 1.3 and has image in the open set S_delta by the membership antecedent. Hence it is smooth as an S_delta-valued map; composing with the stipulated smooth u_delta gives U |-> u_delta(U^dagger)=sigma_C1(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Define alpha:=alpha_C1, mu:=mu_C1, and sigma:=sigma_C1 as literal equalities of maps on the same domains and codomains. By 1.4-1.6 these maps are smooth, and by definition alpha(c,U)=alpha_C1(c,U)=cU, mu(U,V)=mu_C1(U,V)=u_delta(U bold-dot V), and sigma(U)=sigma_C1(U)=u_delta(U^dagger). Because equal C^1 maps between the same manifolds have equal differentials, Dalpha=Dalpha_C1, Dmu=Dmu_C1, and Dsigma=Dsigma_C1; the smooth upgrade has changed neither points nor first derivatives.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** For all c,d in U(1), all U,V,W in calU, and every H in calX, complex bilinearity of bold-dot and conjugate-linearity of dagger from def-epsilon-cstar-algebra give (cU) bold-dot (dV)=(c*d)(U bold-dot V), ((c*d)W) bold-dot H=(c*d)(W bold-dot H), and (cU)^dagger=conj(c)U^dagger. Also c*d and conj(c) lie in U(1), and the stipulated scalar-action codomain gives (c*d)W and conj(c)W in calU. No associativity, positivity, or approximate group law is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** The multiplication covariance holds. Fix U,V,c,d and put W=u_delta(U bold-dot V), H=h_delta(U bold-dot V). The inverse identity gives U bold-dot V=Pi_delta(W,H)=W bold-dot H. By 1.8, (cU) bold-dot (dV)=(c*d)(U bold-dot V)=((c*d)W) bold-dot H=Pi_delta((c*d)W,H). Both ((c*d)W,H) and the inverse pair (u_delta((cU) bold-dot (dV)),h_delta((cU) bold-dot (dV))) lie in the displayed domain and have the same Pi_delta image. Injectivity of the one displayed diffeomorphism Pi_delta makes the pairs equal, so mu(cU,dV)=u_delta((cU) bold-dot (dV))=(c*d)W=c*d*mu(U,V).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.10

**Statement:** The inversion covariance holds. Fix U,c and put W=u_delta(U^dagger), H=h_delta(U^dagger). The inverse identity gives U^dagger=Pi_delta(W,H)=W bold-dot H. By 1.8, (cU)^dagger=conj(c)U^dagger=(conj(c)W) bold-dot H=Pi_delta(conj(c)W,H). Both (conj(c)W,H) and the inverse pair of (cU)^dagger lie in the displayed domain and have the same Pi_delta image. Injectivity of Pi_delta makes the pairs equal, whence sigma(cU)=u_delta((cU)^dagger)=conj(c)W=conj(c)*sigma(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.11

**Statement:** For the arbitrary data fixed in 1.1, the literal choices alpha=alpha_C1, mu=mu_C1, sigma=sigma_C1 satisfy smoothness and all value and differential identities by 1.7, multiplication covariance by 1.9, and inversion covariance by 1.10. Existentially generalizing these three maps and then universally generalizing the arbitrary algebra, delta, and contract-local witnesses proves node 1.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

