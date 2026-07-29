# Proof Export

## Node 1

**Statement:** There are universal e_iso^r > 0, r_iso > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_iso^r, J and -J are the only fixed points of the smooth sigma in their respective ambient r_iso-balls.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix the universal tuple W supplied by lem-stage1-polar-constant-ledger and set e_iso^r := C_rect*e_S1 and rho := r_iso (the tuple field). These are positive universal constants. If 0 <= epsilon_r <= e_iso^r, put epsilon_X := epsilon_r/C_rect; then 0 <= epsilon_X <= e_S1 and epsilon_r = C_rect*epsilon_X. Consequently the scalar conclusions (R) of lem-stage1-polar-constant-ledger, with delta = delta_* and r = rho, give every guard required in (A_7): rho <= delta_*, C_ch*(epsilon_r+delta_*) <= kappa_ch, C_pol*(epsilon_r+delta_*) <= kappa_pol, C_grp*epsilon_r < delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), C_der*(epsilon_r+rho) <= kappa_der, and (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*rho+C_grp*epsilon_r < 2*delta_*; moreover c := C_der*(epsilon_r+rho) <= kappa_der/4 < 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For any algebra and epsilon_r fixed as in 1.1, the objects used below define one smooth map sigma on all of calU. Indeed (A_2) of lem-stage1-polar-constant-ledger supplies the unique C^1 graph family and gives ||D_{A^perp}f_V-I||<1, hence each D_{A^perp}f_V is invertible; lem-stage1-smooth-unitary-atlas upgrades exactly these graphs and charts to a smooth embedded atlas. Item (A_4) supplies the C^1 polar diffeomorphism, and lem-stage1-smooth-polar-inverse upgrades that same map and same inverse to smooth maps. The guards from 1.1 make (A_5) applicable, so its sigma(U)=u_{delta_*}(U^dagger) is global and sigma(J)=J. Applying lem-stage1-explicit-smooth-unitary-operations to these displayed graphs, atlas, polar map and inverse makes this same sigma smooth without changing its points or first derivatives, and its scalar covariance gives sigma(-J)=sigma((-1)J)=(-1)sigma(J)=-J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For each s in {+1,-1}, let F_s be the same-chart map supplied by (A_7) of lem-stage1-polar-constant-ledger at delta=delta_* and r=rho, and put G_s:=F_s-id on B_rho^{i calH}(0). By 1.1, (A_7) applies and gives chart retention and ||DG_s(A)+2I|| <= c < 1 throughout that ball; by 1.2, G_s is C^1. With V:=-2I, a Banach-space isomorphism of i calH, one has ||V^(-1)DG_s(A)-I||=(1/2)||DG_s(A)+2I|| <= c/2 < 1. Therefore lem-stage1-quantitative-inverse-function makes G_s injective on B_rho^{i calH}(0). Also f_{sJ}(0)=0 using only exact unitality, bilinearity and s^2=1, so uniqueness in (A_2) gives g_{sJ}(0)=0 and chi_s(0)=sJ; the fixed-center identities in 1.2 then give F_s(0)=0 and G_s(0)=0. Thus A=0 is the unique zero of G_s in B_rho^{i calH}(0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Let U in calU satisfy sigma(U)=U and ||U-J||<rho. Exact unitality gives phi_J(U)=U-J=:B; its anti-Hermitian and Hermitian parts A=B^parallel and B^perp each have norm at most ||B||, because dagger is isometric, so A lies in B_rho^{i calH}(0) and both parts lie in the domains from (A_2). Since U=J bold-dot (J+B) and U^dagger bold-dot U=J, the defining expression gives f_J(B)=0; uniqueness in (A_2) therefore yields B^perp=g_J(A), hence U=chi_+(A). The fixed-point equality and same-chart retention imply F_+(A)=phi_J^parallel(U)=A, so G_+(A)=0; 1.3 forces A=0, and uniqueness gives g_J(0)=0, whence U=J. Conversely J is fixed by 1.2, so J is the only fixed point in its ambient rho-ball.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Let U in calU satisfy sigma(U)=U and ||U+J||<rho. Since L_{-J}=-I by exact unitality and bilinearity, phi_{-J}(U)=-(U+J)=:B; its anti-Hermitian and Hermitian parts A=B^parallel and B^perp each have norm at most ||B||, so A lies in B_rho^{i calH}(0) and both parts lie in the domains from (A_2). One has U=(-J) bold-dot (J+B); the involution axiom gives (J+B^dagger) bold-dot (-J)^dagger=U^dagger, and unitarity gives f_{-J}(B)=0. Uniqueness in (A_2) therefore yields B^perp=g_{-J}(A), hence U=chi_-(A). The fixed-point equality and same-chart retention imply F_-(A)=phi_{-J}^parallel(U)=A, so G_-(A)=0; 1.3 forces A=0, and uniqueness gives g_{-J}(0)=0, whence U=-J. Conversely -J is fixed by 1.2, so -J is the only fixed point in its ambient rho-ball.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Assume U in calU, sigma(U)=U, and ||U+J||<rho. By validated node 1.2, the global smooth sigma fixes -J and the (A_7) negative chart is the same chart used by sigma; by validated node 1.3, G_-:=F_- - id has 0 as its unique zero on B_rho^{i calH}(0). Put B:=phi_{-J}(U)=-(U+J), using L_{-J}=-I from exact unitality and bilinearity, and A:=B^parallel. Isometry of dagger gives ||A||,||B^perp||<=||B||<rho, hence these variables are in the (A_2) graph domains. From U=(-J) bold-dot (J+B), the involution axiom gives U^dagger=(J+B^dagger) bold-dot (-J)^dagger; since U is unitary, f_{-J}(B)=0. The uniqueness clause of (A_2) gives B^perp=g_{-J}(A), so U=chi_-(A). Since sigma(U)=U and (A_7) retains sigma(chi_-(A)) in this chart, F_-(A)=phi_{-J}^parallel(U)=A; thus G_-(A)=0. Validated node 1.3 yields A=0, and its established g_{-J}(0)=0 gives B=0 and U=-J. Conversely validated node 1.2 gives sigma(-J)=-J. Therefore -J is the unique fixed point of sigma in the ambient rho-ball about -J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

