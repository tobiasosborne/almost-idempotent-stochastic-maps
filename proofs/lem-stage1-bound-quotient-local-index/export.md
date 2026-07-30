# Proof Export

## Node 1

**Statement:** Parameterized same-map quotient local-index and ambient-chart package: for every universal def-stage1-polar-witness-data tuple W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) with C_rect,C_ch,C_pol,C_grp,C_path,C_der>=1, 0<e_rect<=1/C_rect, 0<kappa_ch,kappa_pol,kappa_der<=1/2, delta_*=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol)}, epsilon_*^r=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol),kappa_der/(8*C_der),1/C_grp,delta_*/(12*C_path*C_grp)}, e_S1=min{e_rect,epsilon_*^r/C_rect}, and r_iso=min{delta_*/4,kappa_der/(8*C_der)}, there exist universal e_quot^r>0 and epsilon_B^r>0 with epsilon_B^r=min{epsilon_*^r,e_quot^r} such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=epsilon_B^r and 1<dim_C calX<infinity, and for displayed data satisfying all of the following: (A_2) for every V in calUbar_delta_* and A^par in B_{2delta_*}^{icalH}(0) there is a unique g_V(A^par) in B_{2delta_*}^{calH}(0) with f_V(A^par+g_V(A^par))=0, where f_V(A)=(1/2)*(((J+A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J+A))-J), chi_V(A^par)=V bold-dot (J+A^par+g_V(A^par)) lies in calU, ||Dg_V(A^par)||<=C_ch*(epsilon_r+delta_*), ||D_{A^perp}f_V(A^par+g_V(A^par))-I_calH||<=C_ch*(epsilon_r+delta_*)<1, and these C^1 charts cover calU; (A_4) set Pi_delta_*:calU x B_{delta_*}^{calH}(J)->calX by Pi_delta_*(U,K):=U bold-dot K and set S_delta_*:=Pi_delta_*(calU x B_{delta_*}^{calH}(J)); Pi_delta_* is a C^1 diffeomorphism onto S_delta_* with unique inverse maps u_delta:S_delta_*->calU and h_delta:S_delta_*->B_{delta_*}^{calH}(J) satisfying X=u_delta(X) bold-dot h_delta(X) for every X in S_delta_* and u_delta(U)=U and h_delta(U)=J for every U in calU; (A_5) the displayed maps mu:calU x calU->calU and sigma:calU->calU are defined by mu(U,V):=u_delta(U bold-dot V) and sigma(U):=u_delta(U^dagger), are global C^1 and, for every U,V,Z in calU, mu(J,U)=mu(U,J)=U, sigma(J)=J, ||mu(U,V)-U bold-dot V||<=C_grp*epsilon_r, ||sigma(U)-U^dagger||<=C_grp*epsilon_r, ||mu(mu(U,V),Z)-mu(U,mu(V,Z))||<=C_grp*epsilon_r, ||mu(sigma(U),U)-J||<=C_grp*epsilon_r, and ||mu(U,sigma(U))-J||<=C_grp*epsilon_r; (A_6) for every U_0,U_1 in calU and q in [0,1] satisfying ||U_1-U_0||<=q, C_path*q<=1/4, and C_path*(q+epsilon_r*q+q^2)<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), the path H(-,U_0,U_1):[0,1]->calU given by H(t,U_0,U_1):=u_delta((1-t)*U_0+t*U_1) is defined, is jointly continuous in its displayed variables, and joins U_0 to U_1, and satisfies H(t,cU_0,cU_1)=c*H(t,U_0,U_1) for every c in U(1) and t in [0,1]; (A_7) for every s in {+1,-1}, set chi_s:B_{r_iso}^{icalH}(0)->calU by chi_s(A):=sJ bold-dot (J+A+g_{sJ}(A)), let phi_{sJ}^par:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0) be its inverse, and set F_s:B_{r_iso}^{icalH}(0)->icalH by F_s(A):=phi_{sJ}^par(sigma(chi_s(A))); then sigma maps chi_s(B_{r_iso}^{icalH}(0)) into itself and ||D(F_s-id)(A)+2I||<=C_der*(epsilon_r+r_iso) for every A in B_{r_iso}^{icalH}(0); and (R) set q_*:=C_grp*epsilon_r, set r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and set eta_*:=C_path*(q_*+epsilon_r*q_*+q_*^2); the guards C_ch*(epsilon_r+delta_*)<=kappa_ch, C_pol*(epsilon_r+delta_*)<=kappa_pol, q_*<r_-, C_path*q_*<=1/4, eta_*<r_-, C_der*(epsilon_r+r_iso)<=kappa_der/4<1, and (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q_*<2delta_* hold; then, for those same u_delta,h_delta,mu,sigma,H,chi_s,F_s, there exist a space breve-calU, maps breve-mu:breve-calU x breve-calU->breve-calU and breve-sigma:breve-calU->breve-calU, and maps psi_s:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0) for s in {+1,-1} such that breve-calU=calU_e/U(1), set breve-e:=[J], breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,breve-e) is a connected H-space, breve-sigma is a smooth left inversion, sigma(cU)=conj(c)*sigma(U), ||sigma(U)-U^dagger||<=C_grp*epsilon_r, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension (dim_C calX)-1, chi_s:B_{r_iso}^{icalH}(0)->calU has chi_s(0)=sJ and inverse psi_s=phi_{sJ}^par on its image, sigma retains that image, F_s=psi_s o sigma o chi_s and ||D(F_s-id)(A)+2I||<1, calU intersect B_{r_iso}(sJ) is contained in chi_s(B_{r_iso}^{icalH}(0)), and ||A-B||<=||chi_s(A)-chi_s(B)|| for A,B in B_{r_iso}^{icalH}(0); for these same maps, breve-e is an isolated fixed point of breve-sigma, i*reals*J is D-sigma_J-invariant, ||D-breve-sigma_{breve-e}+I||<1 in the quotient norm, det(I-D-breve-sigma_{breve-e})>0, and the local index of breve-e is +1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose the universal witnesses e_quot^r and epsilon_B^r furnished by lem-stage1-bound-quotient-left-inversion; under the present stronger hypotheses, establish with the same u_delta,h_delta,mu,sigma,H the connected compact orientable smooth quotient H-space, its smooth left inversion, equivariance, and the stated sigma estimate, while the three smooth-upgrade imports identify all smooth structures and maps with the displayed C^1 ones.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By (A_2), ||D_{A^perp}f_V-I||<1, so the Neumann-series criterion makes every such derivative invertible; lem-stage1-smooth-unitary-atlas therefore makes the same g_V and chi_V smooth with unchanged points and first derivatives. We now supply the ambient-openness step omitted from the earlier wording. Regard calX as a real finite-dimensional space. The conjugate-linear involution gives the real direct sum calX=calH direct-sum icalH: for every X, X=(X+X^dagger)/2+(X-X^dagger)/2 with the first summand Hermitian and the second anti-Hermitian, and their intersection is zero. The graph atlas models calU on open subsets of icalH, so dim_R(calU x B_{delta_*}^{calH}(J))=dim_R(icalH)+dim_R(calH)=dim_R(calX). Because (A_4) says Pi_delta_* is a C^1 diffeomorphism onto its image as a C^1 submanifold of calX, it is a C^1 embedding; consequently its ambient differential is injective at every point, and the dimension equality makes that differential a real-linear isomorphism. Fix a source point p and take a graph-product coordinate representative P of Pi_delta_* with x_0 representing p. Put V=DP(x_0). Continuity of DP permits a ball B_r(x_0) in the coordinate domain on which ||V^(-1)DP(x)-I||<=1/2. Applying lem-stage1-quantitative-inverse-function, P(B_r(x_0)) contains P(x_0)+V(B_{r/2}(0)), an ambient-open neighborhood of P(x_0). Since p was arbitrary and S_delta_* is the image, S_delta_* is open in calX. Now (A_4), including its C^1 inverse, is a bijective C^1 local diffeomorphism onto this ambient-open set, so lem-stage1-smooth-polar-inverse makes this same Pi_delta_* and the same inverse (u_delta,h_delta) smooth. Global definition in (A_5) implies U bold-dot V and U^dagger belong to S_delta_*; hence lem-stage1-explicit-smooth-unitary-operations makes the same scalar action, mu, and sigma smooth, with unchanged values/differentials and sigma(cU)=conj(c)*sigma(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** All assumptions required by lem-stage1-bound-quotient-left-inversion are literally (A_2),(A_4),(A_5),(A_6) and the first five guards in (R), all present here; take its universal e_quot^r>0 and epsilon_B^r=min{epsilon_*^r,e_quot^r}. Its conclusion, for the same u_delta,h_delta,mu,sigma,H, gives breve-calU=calU_e/U(1), breve-e=[J], breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], the connected H-space and smooth-left-inversion assertions, ||sigma(U)-U^dagger||<=C_grp*epsilon_r, and the connected compact orientable boundaryless smooth-manifold assertion with real dimension dim_C(calX)-1; the preceding smooth upgrades ensure these are exactly the displayed maps and unchanged C^1 differentials.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For each s in {+1,-1}, establish the entire asserted ambient-chart package for chi_s, psi_s, and F_s: smoothness, chi_s(0)=sJ, psi_s=phi_{sJ}^par on the image, sigma-invariance and the displayed F_s formula and derivative bound, containment of calU intersect B_{r_iso}(sJ), and the lower Lipschitz estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For V=sJ, exact unitality and bilinearity give f_{sJ}(0)=0; uniqueness in (A_2) gives g_{sJ}(0)=0, hence chi_s(0)=sJ. The graph-coordinate identity phi_{sJ}(chi_s(A))=A+g_{sJ}(A) shows that the inverse is its anti-Hermitian component psi_s=phi_{sJ}^par. Smoothness follows from lem-stage1-smooth-unitary-atlas. The sigma-invariance and F_s=psi_s o sigma o chi_s are exactly (A_7), and D(F_s-id)+2I=DF_s+I has norm at most C_der*(epsilon_r+r_iso)<=kappa_der/4<1 by (A_7) and (R).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** If U is in calU with ||U-sJ||<r_iso, left multiplication by sJ is scalar multiplication by s, so phi:=phi_{sJ}(U)=s(U-sJ). Its anti-Hermitian and Hermitian projections A=(phi-phi^dagger)/2 and B=(phi+phi^dagger)/2 have norms at most ||phi||<r_iso<=delta_*/4<2delta_*. Since U=sJ bold-dot(J+phi) and U^dagger bold-dot U=J, the defining displayed formula gives f_{sJ}(phi)=0. Uniqueness in (A_2) forces B=g_{sJ}(A), so U=chi_s(A) with A in B_{r_iso}^{icalH}(0); therefore calU intersect B_{r_iso}(sJ) is contained in the asserted chart image.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** For A,B in B_{r_iso}^{icalH}(0), exact unitality and bilinearity give chi_s(A)-chi_s(B)=s*((A-B)+(g_{sJ}(A)-g_{sJ}(B))). The anti-Hermitian projection P_parallel(X)=(X-X^dagger)/2 is contractive because dagger is an isometry, and it kills the Hermitian g-difference while fixing A-B. Thus ||A-B||=||P_parallel(chi_s(A)-chi_s(B))||<=||chi_s(A)-chi_s(B)||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** At breve-e=[J], prove that i*reals*J is D-sigma_J-invariant and that the induced quotient differential satisfies ||D-breve-sigma_{breve-e}+I||<1 in the quotient norm.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** From sigma(cU)=conj(c)*sigma(U) and sigma(J)=J, differentiating sigma(exp(it)J)=exp(-it)J at t=0 gives D-sigma_J(iJ)=-iJ, hence i*reals*J is invariant. In the chi_+ coordinate, the vertical tangent of the U(1)-orbit is the same line i*reals*J (the coordinate of exp(it)J has derivative iJ), so DF_+(0) acts as -I on that line.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** The quotient tangent is T_{breve-e}breve-calU identified with icalH/(i*reals*J), equipped with the quotient norm, and D-breve-sigma_{breve-e} is induced by DF_+(0). Put R=DF_+(0)+I. By the preceding vertical calculation R vanishes on i*reals*J, so it induces Rbar=D-breve-sigma_{breve-e}+I. For quotient classes, ||Rbar[x]||_quot=inf_v||R(x+v)||<=||R||*inf_v||x+v||, hence ||Rbar||<=||R||. By (A_7) and (R), ||R||<=C_der*(epsilon_r+r_iso)<=kappa_der/4<1, proving the asserted quotient estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Correct the quotient-norm step as follows. Let V=i*reals*J and let q:icalH->icalH/V be the quotient map. Since R|_V=0, the induced map Rbar is well-defined by Rbar(q(x))=q(Rx). Hence, for every x in icalH and every v in V, Rbar(q(x))=q(R(x+v)), and therefore ||Rbar(q(x))||_quot=||q(R(x+v))||_quot<=||R(x+v)||<=||R||*||x+v||. Taking the infimum over v in V gives ||Rbar(q(x))||_quot<=||R||*||q(x)||_quot, so ||Rbar||<=||R||. Here R=DF_+(0)+I=D(F_+-id)(0)+2I, and (A_7) together with (R) gives ||R||<=C_der*(epsilon_r+r_iso)<=kappa_der/4<1. Thus ||D-breve-sigma_{breve-e}+I||=||Rbar||<1. No equality between the quotient norm of q(Rx) and the ambient norm of Rx is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Replace the final norm chain by the following fully non-strict argument. Let V=i*reals*J and q:icalH->icalH/V be the quotient map. With R=DF_+(0)+I=D(F_+-id)(0)+2I, the preceding vertical calculation gives R|_V=0, so Rbar(q(x)):=q(Rx) is well-defined and equals D-breve-sigma_{breve-e}+I. For every x in icalH and v in V, Rbar(q(x))=q(R(x+v)); hence ||Rbar(q(x))||_quot<=||R(x+v)||<=||R||*||x+v||. Infimizing over v gives ||Rbar(q(x))||_quot<=||R||*||q(x)||_quot and therefore ||Rbar||<=||R||. Assumption (A_7), evaluated at A=0, gives ||R||=||D(F_+-id)(0)+2I||<=C_der*(epsilon_r+r_iso), while (R) gives C_der*(epsilon_r+r_iso)<=kappa_der/4<1. Consequently ||D-breve-sigma_{breve-e}+I||=||Rbar||<=||R||<=C_der*(epsilon_r+r_iso)<=kappa_der/4<1. This uses no unsupported strict inequality and proves the required strict conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Prove that breve-e is an isolated fixed point of breve-sigma by applying lem-stage1-quantitative-inverse-function in a local quotient chart to id-breve-sigma.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Take a smooth local chart theta of breve-calU at breve-e with theta(breve-e)=0, write b=theta o breve-sigma o theta^{-1}, and L=Db(0). The estimate ||L+I||<1 makes T:=I-L=2I-(L+I) invertible by the Neumann series. For q(x):=x-b(x), Dq(0)=T; continuity of Dq permits a ball B_rho(0) on which ||T^{-1}Dq(x)-I||<=c<1. Apply lem-stage1-quantitative-inverse-function with V=T: q is injective on this ball. Since sigma(J)=J gives q(0)=0, zero is the only zero of q there, equivalently breve-e is the only fixed point of breve-sigma in the corresponding neighborhood.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** Let Q=T_{breve-e}breve-calU with its quotient norm and A=D-breve-sigma_{breve-e}. Node 1.3.2 gives ||A+I_Q||<1. Hence T_0:=I_Q-A=2I_Q-(A+I_Q)=2(I_Q-(A+I_Q)/2) is a Banach-space isomorphism by the Neumann series, since ||(A+I_Q)/2||<1/2. Now choose any smooth chart theta at breve-e, after shrinking its domain so that breve-sigma maps it into the chart, with theta(breve-e)=0. Put E for its finite-dimensional coordinate space, S=Dtheta_{breve-e}:Q->E, b=theta o breve-sigma o theta^{-1}, and L=Db(0)=S A S^{-1}. Then T:=I_E-L=S T_0 S^{-1} is an isomorphism; no bound on ||L+I_E|| in the coordinate norm is asserted or needed. For q(x)=x-b(x), one has Dq(0)=T. Choose a norm on E (any norm makes finite-dimensional E Banach) and rho>0 with B_rho(0) in the domain of q. Because x |-> T^{-1}Dq(x) is continuous and equals I_E at 0, after decreasing rho there is c<1 such that ||T^{-1}Dq(x)-I_E||<=c throughout B_rho(0). Lem-stage1-quantitative-inverse-function applied with V=T, x_0=0, and f=q makes q injective on B_rho(0). Since breve-sigma(breve-e)=breve-e, b(0)=0 and q(0)=0, so q has no other zero there. Thus breve-e is an isolated fixed point of breve-sigma.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Work independently of pending node 1.3.2. Let p:calU_e->breve-calU be the scalar quotient and V=i*reals*J. In the chi_+ chart at J, the smooth quotient supplied by lem-stage1-bound-quotient-left-inversion identifies T_{breve-e}breve-calU with Q=icalH/V and its quotient norm; Dp_J is the quotient map p_Q:icalH->Q. Since breve-sigma([U])=[sigma(U)], the identity p o sigma=breve-sigma o p and the chain rule show that A:=D-breve-sigma_{breve-e} is induced on Q by B:=DF_+(0). Indeed F_+=psi_+ o sigma o chi_+ is the local expression of sigma. Scalar equivariance and sigma(J)=J give sigma(exp(it)J)=exp(-it)J; differentiating at zero in the chi_+ coordinate gives B(iJ)=-iJ, hence B=-I on V. Thus R:=B+I vanishes on V and Rbar(p_Q x):=p_Q(Rx) is well-defined, with Rbar=A+I_Q. For every x in icalH and v in V, Rbar(p_Q x)=p_Q(R(x+v)), so ||Rbar(p_Q x)||_quot<=||R(x+v)||<=||R||*||x+v||. Infimizing over v yields ||A+I_Q||=||Rbar||<=||R||. Since R=DF_+(0)+I=D(F_+-id)(0)+2I, (A_7) at zero and (R) give the fully non-strict chain ||R||<=C_der*(epsilon_r+r_iso)<=kappa_der/4<1. Consequently T_0:=I_Q-A=2(I_Q-(A+I_Q)/2) is an isomorphism by the Neumann series. Choose a smooth chart theta at breve-e, restricted to the open intersection of its domain with breve-sigma^{-1} of its domain, and set theta(breve-e)=0, S=Dtheta_{breve-e}, b=theta o breve-sigma o theta^{-1}, and G(x)=x-b(x). Then DG(0)=I-Db(0)=S T_0 S^{-1}=:T is an isomorphism. Equip the finite-dimensional coordinate space with any Banach norm. By continuity of DG, on some ball B_rho(0) one has ||T^{-1}DG(x)-I||<=1/2<1. Lem-stage1-quantitative-inverse-function applied to G with V=T makes G injective there. Finally breve-sigma(breve-e)=breve-e because sigma(J)=J, so G(0)=0; injectivity makes 0 its only zero on that ball. Hence breve-e is an isolated fixed point of breve-sigma, without using node 1.3.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Prove det(I-D-breve-sigma_{breve-e})>0 and apply lem-topology-local-index-sign to obtain local index +1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Let E=D-breve-sigma_{breve-e}+I, so ||E||<1 and I-D-breve-sigma_{breve-e}=2I-E. For 0<=t<=1, 2I-tE is invertible because ||tE/2||<1; its real determinant is continuous and never zero, and at t=0 equals det(2I)>0, hence det(I-D-breve-sigma_{breve-e})>0. The map breve-sigma is smooth on the compact orientable manifold breve-calU, and breve-e is isolated by the preceding node; therefore lem-topology-local-index-sign applies and gives ind(breve-sigma,breve-e)=sgn det(I-D-breve-sigma_{breve-e})=+1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

