# Proof Export

## Node 1

**Statement:** There is a universal e_H^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_H^r, the scalar-equivariant mu, sigma and the jointly continuous projected straight paths descend to breve-calU; the descended multiplication makes it a connected H-space, and the descended smooth map breve-sigma is a left inversion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Universal ledger specialization and admissible operations/paths. Fix the universal witness tuple W from lem-stage1-polar-constant-ledger and put e_pol^r := C_rect*e_S1 and e_H^r := min{e_pol^r,e_quot^r}, where e_quot^r is from lem-stage1-quotient-manifold-package. Then e_H^r>0. Given 0<=epsilon_r<=e_H^r, set epsilon_X:=epsilon_r/C_rect, delta:=delta_*, q:=C_grp*epsilon_r, r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and eta:=C_path*(q+epsilon_r*q+q^2). Since epsilon_X<=e_S1, clause (R) of lem-stage1-polar-constant-ledger gives all (A_2),(A_4),(A_5),(A_6) guards, in particular q<=1, C_path*q<=1/4, q<r_-, and eta<r_-. Hence (A_5) gives global C^1 maps mu(U,V)=u_delta(U bold-dot V), sigma(U)=u_delta(U^dagger), exact identities mu(J,U)=mu(U,J)=U and sigma(J)=J, and ||mu(sigma(U),U)-J||<=q; and (A_6) gives, for every U_0,U_1 with ||U_1-U_0||<=q, the jointly continuous projected straight path H(t,U_0,U_1)=u_delta((1-t)U_0+tU_1), with the stated endpoints and H(t,cU_0,cU_1)=cH(t,U_0,U_1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Smoothness and scalar covariance of the same operations. At delta=delta_*, (A_2) of lem-stage1-polar-constant-ledger supplies the unique C^1 graph family covering calU and ||D_{A^perp}f_V-I||<1, so each normal derivative is invertible; lem-stage1-smooth-unitary-atlas upgrades exactly those graphs/charts to a smooth embedded atlas without changing points or first derivatives. Clause (A_4) supplies the displayed C^1 polar diffeomorphism and inverse, and lem-stage1-smooth-polar-inverse upgrades those same maps to smooth maps. Thus every antecedent of lem-stage1-explicit-smooth-unitary-operations holds for the very u_delta, mu and sigma fixed above; that lemma makes the same mu and sigma smooth and gives mu(cU,dV)=c*d*mu(U,V) and sigma(cU)=conj(c)*sigma(U) for all c,d in U(1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Restriction to the identity component and descent. Let p:calU_e -> breve-calU=calU_e/U(1) be the orbit map and breve-e=[J]. The connected images mu(calU_e x calU_e) and sigma(calU_e) contain J by the exact basepoint identities, hence lie in the connected component calU_e; every admissible H-path whose initial point is in calU_e also lies in calU_e. The covariance identities therefore define continuous maps breve-mu([U],[V]):=[mu(U,V)] and breve-sigma([U]):=[sigma(U)], independent of representatives, and common-phase covariance makes each admissible projected straight path t |-> [H(t,U_0,U_1)] independent of a simultaneous replacement (U_0,U_1) by (cU_0,cU_1). For N>1 use the smooth quotient structure supplied by lem-stage1-quotient-manifold-package; for N=1, exact unitality and complex dimension one give calX=CJ, (cJ)^dagger=conj(c)J, (cJ) bold-dot (dJ)=cdJ, hence calU_e=U(1)J and breve-calU is the one-point smooth quotient. Thus the stated descents exist in every finite dimension.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** H-space law. The descended multiplication breve-mu is continuous, breve-mu(breve-e,breve-e)=breve-e, and the exact identities mu(J,U)=mu(U,J)=U imply breve-mu(breve-e,x)=x=breve-mu(x,breve-e). Hence both unit maps are literally the identity (and therefore basepoint-preserving homotopic to it by the constant homotopy), so (breve-calU,breve-e,breve-mu) is an H-space in the precise sense of def-h-space-left-inversion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Connectedness. The space calU_e is connected by its definition as the connected component of calU containing J, and p is continuous and surjective; therefore breve-calU=p(calU_e) is connected (also consistently with lem-stage1-quotient-manifold-package when N>1 and with the singleton description when N=1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Smoothness of the descended inversion. For N>1, equip breve-calU=calU_e/U(1) with the canonical smooth orbit-quotient structure obtained directly from the smooth free scalar action on the smooth manifold calU_e: the orbit map p is a smooth submersion with smooth local sections. Since sigma is smooth, preserves calU_e, and satisfies sigma(cU)=conj(c)sigma(U), the representative-independent map breve-sigma([U])=[sigma(U)] is smooth. For N=1, breve-calU is a point and breve-sigma is its unique smooth self-map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Canonical quotient charts from the allowed smooth action. By node 1.2, calU_e is an open smooth submanifold of calU and alpha(c,U)=cU is smooth. The action is free: cU=U implies (c-1)U=0, while a unitary U has a right inverse and hence U is nonzero, so c=1. Fix U. The orbit tangent is the nonzero vector iU. Choose a linear complement E_U of R(iU) in T_U calU_e and a smooth chart psi from a neighborhood of 0 in T_U calU_e to calU_e with psi(0)=U and Dpsi_0=id. For F(theta,v)=exp(i theta)psi(v), v in E_U, one has DF_(0,0)(a,w)=a iU+w, an isomorphism; the inverse-function theorem therefore gives a local product chart. Shrink its slice S_U=psi(B cap E_U) so that no phase outside the chosen identity arc carries S_U into itself: otherwise shrinking neighborhoods would give sequences x_n,y_n->U and c_n outside that arc with c_n x_n=y_n; compactness of U(1) gives a subsequence c_n->c outside the arc and then cU=U, contradicting freeness. Combining this separation with uniqueness in the local product chart shows that U(1) x S_U -> U(1)S_U is bijective modulo the evident orbit coordinate and is locally a diffeomorphism. Hence p(S_U) is open, p|S_U is a homeomorphism, and the charts (p|S_U)^(-1) give the orbit set a smooth atlas: on an overlap, the unique phase carrying one slice representative to the other is smooth by either local product chart, so the transition map is smooth. In these charts p has local form (theta,v)|->v; consequently p is a smooth submersion and the inverse slice maps s_U:p(S_U)->S_U are smooth local sections. This constructs the needed quotient smooth structure from allowed inputs, without asserting that the bare manifold-existence conclusion of lem-stage1-quotient-manifold-package already exported it.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** Smooth equivariant descent. By nodes 1.2 and 1.3, sigma:calU_e->calU_e is smooth and sigma(cU)=conj(c)sigma(U), so breve-sigma([U]):=[sigma(U)] is well-defined. Let O=p(S_U) be any quotient chart from the preceding construction and s_U:O->calU_e its smooth section. The identity breve-sigma|_O = p o sigma o s_U holds pointwise. Each factor is smooth (p by the quotient charts, sigma by node 1.2, and s_U by construction), hence breve-sigma is smooth on every O and therefore globally. For N=1, node 1.3 identifies breve-calU with a singleton, whose unique self-map is smooth.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Left-inversion homotopy. For U in calU_e set A(U):=mu(sigma(U),U). The covariance from lem-stage1-explicit-smooth-unitary-operations gives A(cU)=mu(conj(c)sigma(U),cU)=A(U), while (A_5) of lem-stage1-polar-constant-ledger gives ||A(U)-J||<=q. Thus (A_6) applies to (A(U),J), and P(t,[U]):=[H(t,A(U),J)] is a well-defined continuous homotopy from x |-> breve-mu(breve-sigma(x),x) to the constant breve-e. It is basepoint-preserving because A(J)=mu(sigma(J),J)=J and H(t,J,J)=J. Also breve-sigma(breve-e)=breve-e. Therefore breve-sigma is a left inversion map by def-h-space-left-inversion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

