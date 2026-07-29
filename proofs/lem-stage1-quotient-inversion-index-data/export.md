# Proof Export

## Node 1

**Statement:** There is a universal e_idx^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_idx^r and 1 < N = dim_C calX < infinity, the scalar class breve-e = [J] is an isolated fixed point of the smooth breve-sigma, the vertical line iR*J is D-sigma_J-invariant, ||D-breve-sigma_{breve-e} + I|| < 1 in the quotient norm, and det(I - D-breve-sigma_{breve-e}) > 0, so its local index is +1; more precisely, there is a quotient neighborhood calN of [J] such that if [U] in calN is fixed, choose a representative U_0 close to J and c in U(1) with sigma(U_0) = c*U_0, choose a in U(1) with a^2 = c, and use sigma(a*U_0) = conj(a)*sigma(U_0) = a*U_0: the two actual fixed lifts +-a*U_0 lie in the J- and -J-isolation balls, hence equal J and -J, so [U] = [J].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso^W) from lem-stage1-polar-constant-ledger, (e_iso^r,rho_iso) from lem-stage1-uniform-inversion-isolation, e_H^r from lem-stage1-quotient-left-inversion, and e_quot^r from lem-stage1-quotient-manifold-package, and set e_idx^r=min{C_rect*e_S1,e_iso^r,e_H^r,e_quot^r}>0. If 0<=epsilon_r<=e_idx^r, put epsilon_X=epsilon_r/C_rect; then epsilon_X<=e_S1, so clause (R) applies at delta=delta_* and r=r_iso^W, all hypotheses of (A_2),(A_4),(A_5),(A_7) hold, and C_der*(epsilon_r+r_iso^W)<1. Clause (A_2), lem-stage1-smooth-unitary-atlas, (A_4), lem-stage1-smooth-polar-inverse, and lem-stage1-explicit-smooth-unitary-operations therefore synchronize a single smooth map sigma(U)=u_{delta_*}(U^dagger), with exactly the point values and first differential of the C^1 map in (A_5)/(A_7), satisfying sigma(J)=J and sigma(cU)=conj(c)*sigma(U); all three smallness-dependent quotient/isolation externals apply.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For 0<=epsilon_r<=e_idx^r and 1<N=dim_C calX<infinity, lem-stage1-quotient-manifold-package and lem-stage1-quotient-left-inversion give M=breve-calU=calU_e/U(1) as a compact orientable smooth manifold of real dimension N-1 and give a smooth descended self-map breve-sigma with breve-sigma([U])=[sigma(U)] and fixed point breve-e=[J]. For the quotient projection pi:calU_e->M, the scalar orbit through J has tangent iR*J, so the differential of pi identifies T_{breve-e}M with T_J calU_e/(iR*J), and the differential of any scalar-equivariant descended map is the operator induced on this quotient whenever its differential preserves iR*J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let e_H^r>0 and e_quot^r>0 be the universal cutoffs supplied respectively by lem-stage1-quotient-left-inversion and lem-stage1-quotient-manifold-package, and let the other positive universal quantities be those supplied by lem-stage1-polar-constant-ledger and lem-stage1-uniform-inversion-isolation. In the root existential construction choose, explicitly and independently of any sibling, e_idx^r=min{C_rect*e_S1,e_iso^r,e_H^r,e_quot^r}. Every entry of this finite minimum is positive, so e_idx^r>0; moreover e_idx^r<=e_H^r and e_idx^r<=e_quot^r. Hence 0<=epsilon_r<=e_idx^r implies simultaneously epsilon_r<=e_H^r and epsilon_r<=e_quot^r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Under 0<=epsilon_r<=e_idx^r and 1<N=dim_C calX<infinity, the inequalities just proved meet the precise cutoff hypotheses of both externals: lem-stage1-quotient-manifold-package yields M=breve-calU=calU_e/U(1) as a compact orientable smooth manifold of real dimension N-1, and lem-stage1-quotient-left-inversion yields the smooth descended map breve-sigma with breve-sigma([U])=[sigma(U)]. Since sigma(J)=J, breve-e=[J] is fixed. For the smooth quotient projection pi, the tangent to the U(1)-orbit t|->exp(it)J at J is iR*J; therefore Dpi_J has kernel iR*J and identifies T_{breve-e}M with T_J calU_e/(iR*J). Differentiating pi o sigma=breve-sigma o pi shows that whenever Dsigma_J preserves iR*J, D-breve-sigma_{breve-e} is exactly the endomorphism induced by Dsigma_J on that quotient.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** The missing quotient-differential facts follow directly from the already supplied smooth graph atlas and smooth scalar action, without assuming them from the quotient-manifold external.  The U(1)-action on calU_e is free: if cU=U, then (c-1)U=0, and U has a right inverse, hence c=1.  Fix any U and use the graph chart chi_U with omega_U o Dchi_U(0)=I_{iH} and omega_U(iU)=iJ.  Choose a real-linear functional ell:iH->R with ell(iJ)=1 and put K=ker ell.  For Theta_U(t,k)=exp(it)chi_U(k), defined near (0,0) in R x K, smoothness of the scalar action and chart gives omega_U DTheta_U(0,0)(s,k)=s*iJ+k, an isomorphism R x K -> iH; thus the finite-dimensional inverse-function theorem makes Theta_U a diffeomorphism onto a neighborhood of U.  Because the action is free and U(1) is compact, after shrinking this neighborhood no phase outside the chosen small arc can return it to itself; therefore its saturation modulo U(1) is homeomorphic to an open subset of K, with quotient map represented in Theta_U-coordinates by (t,k)|->k.  Repeating this construction at all U gives the canonical smooth quotient atlas: on an overlap, after multiplying one representative by the fixed phase matching the two centers, the transition is k|->pr_K(Theta_V^{-1}(Theta_U(0,k))), hence is smooth.  Consequently pi:calU_e->calU_e/U(1) is a smooth submersion and ker Dpi_U is the orbit tangent iR*U.  In particular ker Dpi_J=iR*J and Dpi_J induces T_J calU_e/(iR*J) congruent T_[J](calU_e/U(1)).  This canonical quotient has the same quotient topology as the manifold in lem-stage1-quotient-manifold-package, so the package supplies its compactness, dimension and topological orientability (equivalently smooth orientability); moreover the set map breve-sigma([U])=[sigma(U)] is smooth in this atlas because sigma is smooth and scalar-equivariant.  Finally pi o sigma=breve-sigma o pi; if Dsigma_J preserves iR*J, the chain rule gives Dpi_J Dsigma_J=D-breve-sigma_[J] Dpi_J, and surjectivity of Dpi_J says uniquely that D-breve-sigma_[J] is the endomorphism induced by Dsigma_J on T_J calU_e/(iR*J).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The covariance from lem-stage1-explicit-smooth-unitary-operations and sigma(J)=J imply, by differentiating sigma(exp(it)J)=exp(-it)J at t=0, that Dsigma_J(iJ)=-iJ, hence iR*J is Dsigma_J-invariant. At s=+1, clause (A_7) of lem-stage1-polar-constant-ledger applies with delta=delta_* and r=r_iso^W. Here g_J(0)=0 because f_J(0)=0 and (A_2) gives uniqueness, chi_+(0)=J, and omega_J is the inverse differential of chi_+ at 0; since the smooth upgrades preserve point values and first derivatives, F_+(A)=phi_J^par(sigma(chi_+(A))) is the graph-coordinate expression of sigma and DF_+(0)=omega_J*Dsigma_J*omega_J^{-1}. Thus ||DF_+(0)+I_{iH}||<=C_der*(epsilon_r+r_iso^W)<1, and the invariant vertical line corresponds under omega_J to iR*J because omega_J(iJ)=iJ.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Let A=DF_+(0) on the real normed space iH and L=iR*J. By the preceding invariant-line computation A(L) subseteq L, so A induces bar-A on iH/L; by the definition of the quotient norm, ||bar-A+I||<=||A+I||<1. Under the quotient tangent identification and graph-coordinate identification above, bar-A is D-breve-sigma_{breve-e}; consequently ||D-breve-sigma_{breve-e}+I||<1 in the quotient norm.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For any endomorphism T of a finite-dimensional real normed space with ||T+I||<1, set B=(T+I)/2. Then ||B||<1/2, every I-tB is invertible for 0<=t<=1 by the Neumann series, and continuity of the nonzero real determinant along t gives det(I-B)>0 from det(I)=1. Since I-T=2(I-B), det(I-T)=2^d det(I-B)>0, where d is the real dimension. Applying this to T=D-breve-sigma_{breve-e} yields det(I-D-breve-sigma_{breve-e})>0 (and in particular nonzero).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Shrink a quotient neighborhood calN of [J] so every class in calN has a representative U_0 arbitrarily close to J. If [U_0] is fixed by breve-sigma, then sigma(U_0)=cU_0 for some c in U(1). Continuity of sigma at J and ||J||=1 give |c-1|=||(c-1)J||<=||U_0-J||+||sigma(U_0)-J||, so after shrinking calN, c is arbitrarily close to 1. Label the two square roots of c as a and -a with a close to 1; shrinking once more makes aU_0 lie in B_{rho_iso}(J) and -aU_0 lie in B_{rho_iso}(-J). The covariance and a^2=c give sigma(aU_0)=conj(a)cU_0=aU_0 and sigma(-aU_0)=conj(-a)cU_0=-aU_0, so these are actual fixed lifts in the two prescribed isolation balls.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** For calN from the phase-lift step, any fixed class [U] in calN has actual fixed representatives aU_0 in B_{rho_iso}(J) and -aU_0 in B_{rho_iso}(-J). Since epsilon_r<=e_idx^r<=e_iso^r, lem-stage1-uniform-inversion-isolation forces aU_0=J and -aU_0=-J. Hence [U]=[U_0]=[aU_0]=[J]; thus breve-e=[J] is an isolated fixed point of breve-sigma, with precisely the representative/square-root conclusion stated in the root.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** The smooth breve-sigma acts on the compact orientable manifold M, breve-e is isolated, and det(I-D-breve-sigma_{breve-e})>0. Therefore lem-topology-local-index-sign applies and gives ind(breve-sigma,breve-e)=sgn det(I-D-breve-sigma_{breve-e})=+1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

