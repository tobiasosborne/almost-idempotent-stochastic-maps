# Proof Export

## Node 1

**Statement:** Smooth action/operations upgrade: under lem-stage1-approximate-group-laws, lem-stage1-smooth-unitary-atlas, and lem-stage1-smooth-polar-inverse, the scalar action U(1) x calU -> calU, (c, U) |-> cU, and the same maps mu: calU x calU -> calU, mu(U, V) = u_delta(U bold-dot V), and sigma: calU -> calU, sigma(U) = u_delta(U^dagger), are smooth as maps into the embedded manifold calU; they obey mu(cU, dV) = c*d*mu(U, V) and sigma(cU) = conj(c)*sigma(U), and no point or first derivative is changed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix an arbitrary finite-dimensional exact-unit epsilon_r-C*-algebra and delta in the common regime of the four named dependencies. The scalar action A: U(1) x calU -> calU, A(c,U)=cU, is well-defined and smooth for the embedded smooth structure supplied by lem-stage1-smooth-unitary-atlas.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Scalar multiplication preserves calU: if U^dagger bold-dot U=J and U bold-dot R=J, then for c in U(1), conjugate-linearity of dagger and bilinearity give (cU)^dagger bold-dot(cU)=conj(c)cJ=J and (cU) bold-dot(conj(c)R)=J. The ambient map (c,U) |-> cU, restricted from complex scalar multiplication to U(1) x calU, is smooth.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Let Pi_delta and (u_delta,h_delta) be the polar diffeomorphism and inverse from lem-stage1-smooth-polar-inverse. Since J lies in B_delta^{calH}(J) and Pi_delta(U,J)=U bold-dot J=U, both U and cU belong to S_delta. Hence A has image in the open set S_delta, u_delta composed with A is smooth into calU, and lem-stage1-polar-coherence-naturality gives u_delta(cU)=c*u_delta(U)=cU. Thus A itself is smooth as a calU-valued map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** In the same setting, the maps mu(U,V)=u_delta(U bold-dot V) and sigma(U)=u_delta(U^dagger), already globally defined as C^1 maps by lem-stage1-approximate-group-laws, are smooth maps into the embedded manifold calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By lem-stage1-approximate-group-laws, for every U,V in calU the elements U bold-dot V and U^dagger lie in the domain S_delta of u_delta (this membership is implicit in the asserted globally defined formulas), and the displayed formulas define the same global C^1 maps mu and sigma.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The ambient multiplication (U,V) |-> U bold-dot V is bilinear and hence smooth, while U |-> U^dagger is conjugate-linear and hence real-linear and smooth. Because S_delta is open and these restricted maps have image in S_delta by lem-stage1-approximate-group-laws, they are smooth as S_delta-valued maps. Composing with the smooth u_delta: S_delta -> calU from lem-stage1-smooth-polar-inverse proves that mu and sigma are smooth into calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every c,d in U(1) and U,V in calU, the operations satisfy mu(cU,dV)=c*d*mu(U,V) and sigma(cU)=conj(c)*sigma(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For every c,d in U(1) and U,V in calU, mu(cU,dV)=c*d*mu(U,V). Child 1.3.1.1 proves directly from def-approximate-unitary-space and the conjugate-linearity and bilinearity in def-epsilon-cstar-algebra that scalar multiples cU and dV remain in calU. Child 1.3.1.2 then applies lem-stage1-approximate-group-laws to obtain the required S_delta domain memberships, uses bilinearity to identify (cU) bold-dot (dV)=(cd)(U bold-dot V), and applies lem-stage1-polar-coherence-naturality with the scalar cd to obtain the displayed covariance identity.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Local scalar preservation, independent of node 1.1: let a in U(1) and W in calU. By the definition calU=overline{calU}_0, W^dagger bold-dot W=J and there is R with W bold-dot R=J. Conjugate-linearity of dagger and bilinearity of bold-dot give (aW)^dagger bold-dot(aW)=(conj(a)W^dagger) bold-dot(aW)=conj(a)*a*(W^dagger bold-dot W)=J. Also (aW) bold-dot(conj(a)R)=a*conj(a)*(W bold-dot R)=J, so aW has the explicit right inverse conj(a)R. Therefore aW lies in calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Apply the preceding local fact to (a,W)=(c,U) and (d,V), obtaining cU,dV in calU without using node 1.1. Since lem-stage1-approximate-group-laws defines mu(A,B)=u_delta(A bold-dot B) for every A,B in calU, both X=U bold-dot V and Y=(cU) bold-dot(dV) belong to the domain S_delta of u_delta. Bilinearity gives Y=(cd)X. As cd is in U(1), lem-stage1-polar-coherence-naturality applied in this same polar chart gives u_delta(Y)=u_delta((cd)X)=cd*u_delta(X). Hence mu(cU,dV)=cd*mu(U,V)=c*d*mu(U,V).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** For c in U(1), conjugate-linearity gives (cU)^dagger=conj(c)U^dagger, with conj(c) in U(1). By child 1.3.2.1, cU lies in calU directly from the defining zero-defect and right-inverse conditions, without using node 1.1. Hence lem-stage1-approximate-group-laws applies both to U and to cU and puts U^dagger and (cU)^dagger in S_delta, the domain of u_delta. Lem-stage1-polar-coherence-naturality with scalar conj(c) then gives sigma(cU)=u_delta(conj(c)U^dagger)=conj(c)u_delta(U^dagger)=conj(c)*sigma(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** The membership cU in calU follows directly from the permitted definitions, independently of node 1.1: since U is in calU=overline{calU}_0, one has U^dagger bold-dot U=J and a right inverse R with U bold-dot R=J. Conjugate-linearity and complex bilinearity give (cU)^dagger bold-dot(cU)=(conj(c)U^dagger) bold-dot(cU)=conj(c)c(U^dagger bold-dot U)=J for c in U(1), while (cU) bold-dot(conj(c)R)=c conj(c)(U bold-dot R)=J. Thus cU satisfies both the zero-defect condition and the right-inverse condition defining calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** These upgrades use the same scalar action, the same set-theoretic u_delta, the same mu and sigma, and the same embedded charts, so they change neither any point value nor any first derivative.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Lem-stage1-smooth-unitary-atlas explicitly retains the same graph/chart point values and first derivatives, lem-stage1-smooth-polar-inverse explicitly retains the same set-theoretic (u_delta,h_delta) and its first derivative, and lem-stage1-approximate-group-laws supplies the pre-existing C^1 maps with the identical formulas mu=u_delta composed with multiplication and sigma=u_delta composed with dagger. The ambient scalar multiplication, algebra multiplication, and dagger maps are not altered. Therefore the smoothness conclusions in nodes 1.1 and 1.2 merely upgrade regularity of identical functions through identical charts; uniqueness of derivatives (equivalently, the chain rule using the unchanged component derivatives) shows their first derivatives remain the pre-existing ones, while their point values are literally unchanged.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

