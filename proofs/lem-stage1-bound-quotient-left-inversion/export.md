# Proof Export

## Node 1

**Statement:** Parameterized bound quotient H-space package: for every universal def-stage1-polar-witness-data tuple W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) with C_rect,C_ch,C_pol,C_grp,C_path,C_der>=1, 0<e_rect<=1/C_rect, 0<kappa_ch,kappa_pol,kappa_der<=1/2, delta_*=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol)}, epsilon_*^r=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol),kappa_der/(8*C_der),1/C_grp,delta_*/(12*C_path*C_grp)}, e_S1=min{e_rect,epsilon_*^r/C_rect}, and r_iso=min{delta_*/4,kappa_der/(8*C_der)}, there exist universal e_quot^r>0 and epsilon_B^r>0 with epsilon_B^r=min{epsilon_*^r,e_quot^r} such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=epsilon_B^r and 1<dim_C calX<infinity, and for displayed data satisfying all of the following: (A_2) for every V in calUbar_delta_* and A^par in B_{2delta_*}^{icalH}(0) there is a unique g_V(A^par) in B_{2delta_*}^{calH}(0) with f_V(A^par+g_V(A^par))=0, where f_V(A)=(1/2)*(((J+A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J+A))-J), chi_V(A^par)=V bold-dot (J+A^par+g_V(A^par)) lies in calU, ||Dg_V(A^par)||<=C_ch*(epsilon_r+delta_*), ||D_{A^perp}f_V(A^par+g_V(A^par))-I_calH||<=C_ch*(epsilon_r+delta_*)<1, and these C^1 charts cover calU; (A_4) set Pi_delta_*:calU x B_{delta_*}^{calH}(J)->calX by Pi_delta_*(U,K):=U bold-dot K and set S_delta_*:=Pi_delta_*(calU x B_{delta_*}^{calH}(J)); Pi_delta_* is a C^1 diffeomorphism onto S_delta_* with unique inverse maps u_delta:S_delta_*->calU and h_delta:S_delta_*->B_{delta_*}^{calH}(J) satisfying X=u_delta(X) bold-dot h_delta(X) for every X in S_delta_* and u_delta(U)=U and h_delta(U)=J for every U in calU; (A_5) the displayed maps mu:calU x calU->calU and sigma:calU->calU are defined by mu(U,V):=u_delta(U bold-dot V) and sigma(U):=u_delta(U^dagger), are global C^1 and, for every U,V,Z in calU, mu(J,U)=mu(U,J)=U, sigma(J)=J, ||mu(U,V)-U bold-dot V||<=C_grp*epsilon_r, ||sigma(U)-U^dagger||<=C_grp*epsilon_r, ||mu(mu(U,V),Z)-mu(U,mu(V,Z))||<=C_grp*epsilon_r, ||mu(sigma(U),U)-J||<=C_grp*epsilon_r, and ||mu(U,sigma(U))-J||<=C_grp*epsilon_r; (A_6) for every U_0,U_1 in calU and q in [0,1] satisfying ||U_1-U_0||<=q, C_path*q<=1/4, and C_path*(q+epsilon_r*q+q^2)<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), the path H(-,U_0,U_1):[0,1]->calU given by H(t,U_0,U_1):=u_delta((1-t)*U_0+t*U_1) is defined, is jointly continuous in its displayed variables, and joins U_0 to U_1, and satisfies H(t,cU_0,cU_1)=c*H(t,U_0,U_1) for every c in U(1) and t in [0,1]; and (R) set q_*:=C_grp*epsilon_r, set r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and set eta_*:=C_path*(q_*+epsilon_r*q_*+q_*^2); the guards C_ch*(epsilon_r+delta_*)<=kappa_ch, C_pol*(epsilon_r+delta_*)<=kappa_pol, q_*<r_-, C_path*q_*<=1/4, and eta_*<r_- hold; then, for those same u_delta,h_delta,mu,sigma,H, there exist a space breve-calU and maps breve-mu:breve-calU x breve-calU->breve-calU and breve-sigma:breve-calU->breve-calU such that breve-calU=calU_e/U(1), set breve-e:=[J], breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,breve-e) is a connected H-space, breve-sigma is a smooth left inversion, sigma(cU)=conj(c)*sigma(U), and ||sigma(U)-U^dagger||<=C_grp*epsilon_r for every c in U(1) and U in calU, and breve-calU is a connected compact orientable smooth manifold without boundary of real dimension (dim_C calX)-1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix an arbitrary witness tuple W and arbitrary displayed algebra/data satisfying the hypotheses. By positivity of every entry in the defining minimum, epsilon_*^r>0. Invoke lem-stage1-quotient-manifold-package and let e_quot^r>0 be its universal constant; set epsilon_B^r:=min{epsilon_*^r,e_quot^r}>0. Since epsilon_r<=epsilon_B^r<=e_quot^r and 1<dim_C calX<infinity, that external gives breve-calU:=calU_e/U(1) as a connected compact orientable smooth manifold without boundary of real dimension dim_C(calX)-1.

**Type:** claim

**Inference:** universal_generalization

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Under (A_2), (A_4), (A_5), and (R), the registered smooth-upgrade externals give a smooth embedded structure on calU, the same smooth polar inverse (u_delta,h_delta), and smooth maps alpha(c,U)=cU, mu(U,V)=u_delta(U bold-dot V), sigma(U)=u_delta(U^dagger), with unchanged point values and derivatives, satisfying mu(cU,dV)=cd mu(U,V), sigma(cU)=conj(c)sigma(U), and the bound ||sigma(U)-U^dagger||<=C_grp*epsilon_r.

**Type:** claim

**Inference:** universal_generalization

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For each graph point in (A_2), (R) gives ||D_{A^perp}f_V-I_calH||<=C_ch*(epsilon_r+delta_*)<=kappa_ch<=1/2<1. The Neumann-series criterion therefore makes D_{A^perp}f_V invertible. All remaining hypotheses of lem-stage1-smooth-unitary-atlas are exactly (A_2), so that external upgrades the same g_V and chi_V, without changing their points or first derivatives, to a C^infinity graph atlas defining a smooth embedded manifold structure on calU.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** With the smooth atlas from the preceding step, (A_4) says that Pi_delta_* is a bijective C^1 diffeomorphism, hence a bijective C^1 local diffeomorphism; its image S_delta_* is open because every local diffeomorphism is locally open. Thus lem-stage1-smooth-polar-inverse applies and upgrades the same ambient-bilinear Pi_delta_* and its same set-theoretic inverse (u_delta,h_delta), without changing points or first derivatives, to smooth maps.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Write N:=dim_C(calX).  The conjugate-linear involution gives the real direct-sum decomposition calX_R=calH direct-sum icalH: for X in calX, X=(X+X^dagger)/2+(X-X^dagger)/2 with the two summands respectively Hermitian and anti-Hermitian, their intersection is zero, and multiplication by i is a real-linear isomorphism calH->icalH.  Hence dim_R(calH)=dim_R(icalH)=N and dim_R(calX)=2N.  The smooth graph charts supplied by node 1.2.1 are modeled on open subsets of icalH, so dim_R(calU)=N; consequently calU x B_{delta_*}^{calH}(J) and the ambient real manifold calX both have dimension 2N.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** By (A_4), Pi_delta_* is a C^1 diffeomorphism of the 2N-dimensional domain onto its image S_delta_*; in particular it is a C^1 immersion, so at every (U,K) its ambient differential D Pi_delta_*(U,K):T_U calU direct-sum calH -> calX_R is injective.  By the equal 2N-dimensional source and target count in the preceding child, this ambient differential is a linear isomorphism.  The finite-dimensional inverse-function theorem therefore supplies, at every (U,K), a domain neighborhood O_{U,K} whose image Pi_delta_*(O_{U,K}) is open in ambient calX and on which Pi_delta_* is a C^1 diffeomorphism.  These images cover S_delta_*, so S_delta_* is ambient-open and Pi_delta_* is a bijective C^1 local diffeomorphism as a map into calX, not merely relative to S_delta_*.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.3

**Statement:** Now all hypotheses of lem-stage1-smooth-polar-inverse hold: node 1.2.1 supplies the smooth embedded atlas, (A_4) supplies the same ambient-bilinear bijection Pi_delta_* and the same set-theoretic inverse (u_delta,h_delta), and the preceding child supplies the required ambient openness and local-diffeomorphism property.  That external therefore upgrades Pi_delta_* and (u_delta,h_delta) to smooth maps without changing their point values or C^1 differentials, which is the conclusion asserted by node 1.2.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** In (A_5), global well-typedness of u_delta(U bold-dot V) and u_delta(U^dagger), whose domain is S_delta_*, entails U bold-dot V,U^dagger in S_delta_* for all U,V in calU. Apply lem-stage1-explicit-smooth-unitary-operations to the graph family and atlas of the first step and the polar maps of the second: the resulting maps have precisely alpha(c,U)=cU, mu(U,V)=u_delta(U bold-dot V), sigma(U)=u_delta(U^dagger), are smooth with unchanged C^1 differentials, and obey mu(cU,dV)=cd mu(U,V) and sigma(cU)=conj(c)sigma(U). The pointwise estimate ||sigma(U)-U^dagger||<=C_grp*epsilon_r is the unchanged (A_5) estimate.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** On the component calU_e, the operations mu and sigma descend to smooth maps breve-mu([U],[V]):=[mu(U,V)] and breve-sigma([U]):=[sigma(U)]; with breve-e=[J], the exact unit identities and the (A_6) path applied at q_*=C_grp*epsilon_r make (breve-calU,breve-mu,breve-e) a connected H-space and breve-sigma a smooth left inversion. Together with the manifold conclusion and the retained equivariance/error estimate, these are all conclusions of node 1.

**Type:** claim

**Inference:** universal_generalization

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Because calU_e is a connected component of the smooth manifold calU, it is open and hence a smooth submanifold. The connected set U(1) x calU_e has connected image under alpha and contains alpha(1,J)=J, so alpha preserves calU_e. The restricted action is free because every U in calU has a right inverse and is nonzero, so cU=U forces c=1. It is proper: for Phi(c,U)=(cU,U) and compact K in calU_e x calU_e, Phi^{-1}(K) is closed and lies in the compact set U(1) x pr_2(K). Lem-topology-quotient-manifold therefore equips breve-calU:=calU_e/U(1), with its quotient topology, with the unique smooth structure making p:calU_e->breve-calU a smooth surjective submersion; choose this structure, without identifying it with the package atlas. The package manifold is the same orbit space with the same quotient topology. Thus connectedness and compactness persist. If n=dim_C calX-1, the package orientation is a coherent choice of generators of H_n(breve-calU,breve-calU minus {x};Z). Local homology and its continuation maps depend only on the topology. In a smooth m-manifold, the local half-space calculation says that nonzero local homology at every point occurs precisely in degree m and precisely at interior points. Hence the chosen quotient structure has m=n, no boundary, and inherits the same coherent generators as an orientation. Continuity of mu and sigma shows that their images of calU_e x calU_e and calU_e are connected, contain J, and stay in calU_e. Equivariance gives p(mu(cU,dV))=p(mu(U,V)) and p(sigma(cU))=p(sigma(U)), so breve-mu([U],[V]):=[mu(U,V)] and breve-sigma([U]):=[sigma(U)] are well-defined. Local smooth sections of p x p and p express them as p o mu o s_12 and p o sigma o s, proving smoothness. Finally (A_5) gives breve-mu(breve-e,[U])=[U]=breve-mu([U],breve-e) and breve-sigma(breve-e)=breve-e.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Because calU_e is a connected component of the smooth manifold calU, it is open and hence a smooth submanifold. The connected set U(1) x calU_e has connected image under alpha and that image contains alpha(1,J)=J, so alpha preserves calU_e. This restricted action is free: U in calU has a right inverse, hence U is nonzero, and cU=U forces c=1. It is proper: for Phi(c,U)=(cU,U), if K is compact in calU_e x calU_e, then Phi^{-1}(K) is closed, since K is closed in the Hausdorff manifold product, and is contained in the compact set U(1) x pr_2(K); hence Phi^{-1}(K) is compact. Lem-topology-quotient-manifold therefore equips the orbit space breve-calU:=calU_e/U(1), with its quotient topology, with a unique smooth structure for which p:calU_e->breve-calU is a smooth surjective submersion. We choose this smooth structure.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.3.1.2

**Statement:** The smooth manifold asserted by lem-stage1-quotient-manifold-package is the same orbit space calU_e/U(1) with the same quotient topology, although we do not identify its atlas with the chosen quotient-theorem atlas. Connectedness and compactness depend only on that topology. Put n=dim_C calX-1. For the package manifold, which is an n-manifold without boundary, every local homology group H_n(breve-calU,breve-calU\{x};Z) is infinite cyclic, and its smooth orientation is a coherent choice of generators of these groups. Local homology and its continuation maps depend only on the underlying topology. Consequently, for the quotient-theorem smooth structure every point has nonzero local homology precisely in degree n; the local half-space calculation for a smooth m-manifold forces m=n and forces every point to be an interior point, so this structure also has no boundary. The same coherent local-homology generators define an orientation for it. Thus the chosen quotient-theorem structure retains all connected, compact, orientable, boundaryless, and dimension-n conclusions of the package without invoking uniqueness of the package atlas.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.3.1.3

**Statement:** Continuity of mu and sigma implies mu(calU_e x calU_e) and sigma(calU_e) are connected; they contain mu(J,J)=J and sigma(J)=J, so they lie in calU_e. The identities mu(cU,dV)=cd mu(U,V) and sigma(cU)=conj(c)sigma(U) give p(mu(cU,dV))=p(mu(U,V)) and p(sigma(cU))=p(sigma(U)), proving that breve-mu and breve-sigma are well-defined. Since p and mu,sigma are smooth, local smooth sections of the surjective submersions p x p and p express the descended maps locally as p o mu o s_{12} and p o sigma o s; representative-independence makes these expressions agree on overlaps, hence both descended maps are smooth. Finally (A_5) gives breve-mu(breve-e,[U])=[U]=breve-mu([U],breve-e) and breve-sigma(breve-e)=breve-e.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.3.2

**Statement:** Since epsilon_r<=epsilon_B^r<=epsilon_*^r<=1/C_grp, q_*:=C_grp*epsilon_r lies in [0,1]. For U in calU_e put U_0:=mu(sigma(U),U), U_1:=J. Then (A_5) gives ||U_0-U_1||<=q_*; (R) gives C_path*q_*<=1/4 and C_path*(q_*+epsilon_r*q_*+q_*^2)=eta_*<r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2). Hence (A_6) supplies H(t,U_0,J). The formula F(t,[U]):=[H(t,mu(sigma(U),U),J)] is independent of the representative because sigma(cU)=conj(c)sigma(U) and mu(conj(c)sigma(U),cU)=mu(sigma(U),U). It stays in calU_e because each path starts there; it is continuous because on every quotient neighborhood a local section s of p gives the continuous representative formula [H(t,mu(sigma(s(-)),s(-)),J)], and representative-independence makes these formulas agree. It begins at breve-mu(breve-sigma([U]),[U]) and ends at breve-e. It is basepoint-preserving because sigma(J)=J, mu(J,J)=J, and H(t,J,J)=u_delta(J)=J by (A_4). Thus breve-sigma is a left inversion in def-h-space-left-inversion; it is smooth by node 1.3.1. The exact unit identities make the two H-space unit homotopies constant, and breve-calU is connected by lem-stage1-quotient-manifold-package. Therefore (breve-calU,breve-mu,breve-e) is a connected H-space, and node 1.1 plus the all-calU equivariance and error estimate of node 1.2 supplies every remaining asserted conclusion.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Assume the declared dependencies 1.1, 1.2, and 1.3.1 have been validated. Node 1.2 supplies the all-calU identities sigma(cU)=conj(c)sigma(U), mu(cU,dV)=cd mu(U,V), and ||sigma(U)-U^dagger||<=C_grp*epsilon_r. Node 1.3.1 supplies the invariant component calU_e, the quotient p:calU_e->breve-calU with local sections, and the well-defined smooth descended maps breve-mu([U],[V])=[mu(U,V)] and breve-sigma([U])=[sigma(U)], including exact unit and basepoint identities. Since epsilon_r<=epsilon_B^r<=epsilon_*^r<=1/C_grp, q_*:=C_grp*epsilon_r belongs to [0,1]. For U in calU_e, U_0:=mu(sigma(U),U) lies in calU_e by node 1.3.1 and (A_5) gives ||U_0-J||<=q_*; the guards in (R) give C_path*q_*<=1/4 and C_path*(q_*+epsilon_r*q_*+q_*^2)=eta_*<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2). Thus (A_6) defines H(t,U_0,J), joining U_0 to J. Its image lies in calU_e because it is a connected path in calU starting at U_0 in the connected component calU_e. Define F(t,[U]):=p(H(t,mu(sigma(U),U),J)). This is representative-independent: replacing U by cU and using the two equivariances from node 1.2 gives mu(sigma(cU),cU)=mu(conj(c)sigma(U),cU)=mu(sigma(U),U). It is continuous because the local sections of p from node 1.3.1 express it locally as p(H(t,mu(sigma(s(x)),s(x)),J)); joint continuity in (A_6) and continuity of mu,sigma,p make this continuous, and representative-independence makes the local formulas agree. At t=0 it equals breve-mu(breve-sigma([U]),[U]); at t=1 it equals breve-e. At [U]=breve-e, (A_5) gives sigma(J)=J and mu(J,J)=J, while (A_6) gives H(t,J,J)=J (its asserted path joins J to J and its displayed formula plus (A_4) gives u_delta(J)=J), so F is basepoint-preserving. Hence breve-sigma is a left inversion by def-h-space-left-inversion, and it is smooth by node 1.3.1. The exact descended unit identities of node 1.3.1 give the two constant basepoint-preserving H-space unit homotopies, and node 1.1 gives connectedness and the compact orientable boundaryless manifold conclusion with dimension dim_C(calX)-1. Therefore the connected H-space, smooth-left-inversion, manifold, equivariance, and error conclusions asserted by node 1.3.2 all follow, with no use of an undeclared or unvalidated sibling.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

