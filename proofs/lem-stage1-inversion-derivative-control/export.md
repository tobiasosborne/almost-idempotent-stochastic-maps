# Proof Export

## Node 1

**Statement:** Typed inversion derivative with chart retention: there exist universal C_der, C_ch, C_pol, C_grp >= 1 and kappa_der, kappa_ch, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra, s in {+1, -1}, and 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, the globally defined sigma(U) = u_delta(U^dagger) maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart, where chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)), and F_s(A) = phi_{sJ}^par(sigma(chi_s(A))) satisfies ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for all A in B_r^{icalH}(0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Provider alignment and typed synchronization: fix witnesses (C_g,k_g) from lem-stage1-unitary-graph-control, (P_r,k_r) from lem-stage1-polar-retraction, and (G_c,P_c,k_c) from lem-stage1-explicit-group-closeness. Set C_ch=max{1,C_g}, kappa_ch=min{1/2,k_g}, C_pol=max{1,P_r,P_c}, kappa_pol=min{1/2,k_r,k_c}, and C_grp=max{1,G_c}. The receiving graph, polar, and group guards imply the corresponding guards of all three cited providers. Both polar providers display the identical map Pi_delta(U,H)=U bold-dot H on the identical domain calU x B_delta^{calH}(J), with target its image S_delta, and call its inverse unique; hence ordinary uniqueness of a set-theoretic inverse identifies their displayed (u_delta,h_delta). We choose C_der and kappa_der after the remaining universal estimates are fixed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Scalar graph estimate: put V=sJ, G=g_V and Z_T=T+G(T). Exact unitality, bilinearity and the involution axioms in def-epsilon-cstar-algebra, together with s^2=1, give f_V(Z_T)=G(T)+(1/2) Z_T^dagger bold-dot Z_T. Since zero solves the equation at T=0, uniqueness in lem-stage1-unitary-graph-control gives G(0)=0. With d=C_ch*(epsilon_r+delta)<=kappa_ch<=1/2, its derivative bound gives ||G(T)||<=d||T||. Differentiating the displayed identity gives ||DG(T)||<=(1+epsilon_r)||Z_T||(1+||DG(T)||); for ||T||<=2r, ||Z_T||<=(1+d)||T||<=3r. Thus, once epsilon_r+r is below a universal cutoff, absorption yields ||DG(T)||<=K_g*r for a universal K_g.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Typed adjoint factorization: for A in B_r^{icalH}(0), U=chi_s(A) lies in calU by lem-stage1-unitary-graph-control. Invoke the synchronized inverse from the first step. The C1 inverse in lem-stage1-polar-retraction and the adjoint estimate in lem-stage1-explicit-group-closeness apply to this same u_delta, so W=sigma(U)=u_delta(U^dagger) and Q=h_delta(U^dagger)-J are C1 functions of A, W lies in calU, Q lies in calH with ||Q||<delta, and U^dagger=W bold-dot(J+Q), while ||W-U^dagger||<=C_grp*epsilon_r. Also sJ lies in calU and (sJ)^dagger=sJ, so the retraction identity u_delta(sJ)=sJ gives sigma(sJ)=sJ. No unnamed or separately supplied polar factor is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Polar-normal bound: the typed identity in the preceding step gives U^dagger-W=W bold-dot Q, hence ||W bold-dot Q||<=C_grp*epsilon_r. Since W is unitary, W^dagger bold-dot W=J. Approximate associativity and the product bound imply ||Q||<= (1+epsilon_r)||W|| C_grp*epsilon_r + epsilon_r||W||^2||Q||. The Cstar lower bound applied to W^dagger bold-dot W=J gives ||W||<=(1-epsilon_r)^(-1/2). After making the later C_der guard enforce a universal smallness cutoff on epsilon_r, the last term is absorbed and ||Q||<=K_q*C_grp*epsilon_r for a universal K_q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Same-chart retention: from U=sJ bold-dot(J+A+G(A)), the involution and product estimate give ||U^dagger-sJ||<=(1+epsilon_r)(1+d)||A||. Therefore the explicit closeness estimate gives ||W-sJ||<=(1+epsilon_r)(1+C_ch*(epsilon_r+delta))*r+C_grp*epsilon_r<2delta. Since L_{sJ}=sI exactly, C=phi_{sJ}(W)=s(W-sJ) has norm below 2delta; its Hermitian and anti-Hermitian projections are contractive because dagger is isometric. Write B=C^par. Unitarity of W and W=sJ bold-dot(J+C) imply f_{sJ}(C)=0, so uniqueness in lem-stage1-unitary-graph-control forces C^perp=G(B). Hence W=chi_s(B) in the same sJ graph chart, B=F_s(A), and these coordinate maps are C1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Coordinate identity and radius: substitute U=sJ bold-dot(J+A+G(A)), W=sJ bold-dot(J+B+G(B)), and U^dagger=W bold-dot(J+Q) into the typed factorization and cancel the scalar s. This gives the exact identity J-A+G(A)=(J+B+G(B)) bold-dot(J+Q). Its anti-Hermitian projection is -A=B+P^par((B+G(B)) bold-dot Q). Using ||G(B)||<=d||B|| and the preceding Q bound, choose the C_der smallness cutoff so that (1+epsilon_r)(1+d)||Q||<=1/2. Then ||B||<=r+(1/2)||B||, hence ||B||<=2r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Differentiated identity: for xi in icalH put P=DF_s(A)xi=DB(A)xi and R=DQ(A)xi. Differentiating the exact full coordinate factorization gives -xi+DG(A)xi=P+DG(B)P+R+E, where E=(P+DG(B)P) bold-dot Q+(B+G(B)) bold-dot R. The first two terms P,xi are anti-Hermitian whereas DG(A)xi,DG(B)P,R are Hermitian. Therefore P+xi=-P^par(E) and R=DG(A)xi-DG(B)P-P^perp(E). The scalar graph estimate applies at ||A||<=r and ||B||<=2r, giving ||DG(A)||,||DG(B)||<=K_g*r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Uniform absorption: for ||xi||=1 set p=||P|| and q=||R||. The product bound, ||Q||<=K_q*C_grp*epsilon_r, ||B||<=2r, ||G(B)||<=d||B||, and the two local DG bounds give ||E||<=alpha p+beta q with alpha<=K_1*epsilon_r and beta<=K_2*r for universal K_1,K_2 depending only on the already fixed provider witnesses. Consequently p<=1+alpha p+beta q and q<=K_g*r*(1+p)+alpha p+beta q. A universal cutoff making alpha,beta,K_g*r<=1/8 first yields p<=2; substituting this back and absorbing beta q yields q<=K_3*(epsilon_r+r), and then ||P+xi||<=||E||<=K_4*(epsilon_r+r), for universal K_3,K_4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Final constants and conclusion: take C_der>=max{1,K_4} sufficiently large, and kappa_der in (0,1/2] sufficiently small, so that C_der*(epsilon_r+r)<=kappa_der enforces every universal cutoff and absorption condition used above; these choices depend only on the fixed universal provider witnesses. Homogeneity extends the last estimate to every xi: ||(DF_s(A)+I)xi||<=C_der*(epsilon_r+r)||xi||. Since D(F_s-id)+2I=DF_s+I, this is exactly the derivative inequality in node 1 for every A in B_r^{icalH}(0); the same-chart statement was proved above, and the first step supplies all universal constants and the globally typed u_delta. Thus the existential contract follows.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

