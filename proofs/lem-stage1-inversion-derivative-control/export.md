# Proof Export

## Node 1

**Statement:** Typed inversion derivative with chart retention: there exist universal C_der, C_ch, C_pol, C_grp >= 1 and kappa_der, kappa_ch, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra, s in {+1, -1}, and 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, the globally defined sigma(U) = u_delta(U^dagger) maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart, where chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)), and F_s(A) = phi_{sJ}^par(sigma(chi_s(A))) satisfies ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for all A in B_r^{icalH}(0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Constant alignment: take C_ch,kappa_ch from lem-stage1-unitary-graph-control; take C_pol to be the maximum of the polar coefficients in lem-stage1-polar-retraction and lem-stage1-approximate-group-laws and kappa_pol the minimum of their margins; and take C_grp from lem-stage1-approximate-group-laws. Enlarging a coefficient and decreasing a margin only strengthens every hypothesis needed to invoke those lemmas. It remains to choose universal C_der large and kappa_der in (0,1/2] small after the universal constants in the estimates below are fixed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Exact scalar-chart calculation: put V=sJ, G=g_V, and Z_T=T+G(T). Exact unitality, bilinearity, the involution laws in def-epsilon-cstar-algebra, and s^2=1 give f_V(Z_T)=G(T)+(1/2)Z_T^dagger bold-dot Z_T. Hence G(0)=0 by uniqueness in lem-stage1-unitary-graph-control, and, with d=C_ch*(epsilon_r+delta)<=kappa_ch<=1/2, its derivative bound gives ||G(T)||<=d||T||. Differentiating G(T)=-(1/2)Z_T^dagger bold-dot Z_T shows ||DG(T)||<=K_g*r whenever ||T||<=2r and epsilon_r+r is below a universal threshold, for a universal K_g: indeed ||DG(T)||<=(1+epsilon_r)||Z_T||(1+||DG(T)||), while ||Z_T||<=(1+d)||T||<=3r, and the last DG term is absorbed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Global polar factorization: for A in B_r^{icalH}(0), U=chi_s(A) belongs to calU by lem-stage1-unitary-graph-control. The common polar inverse supplied by lem-stage1-polar-retraction, identified across admissible polar data by lem-stage1-polar-coherence-naturality, and the all-calU adjoint domain in lem-stage1-approximate-group-laws give C1 maps W=sigma(U)=u_delta(U^dagger) and Q=h_delta(U^dagger)-J in calH with ||Q||<delta and the exact identity U^dagger=W bold-dot (J+Q). Moreover ||W-U^dagger||<=C_grp*epsilon_r; scalar naturality, or directly u_delta(sJ)=sJ, also gives sigma(sJ)=sJ.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Polar-normal estimate: from U^dagger-W=W bold-dot Q and the preceding closeness, ||W bold-dot Q||<=C_grp*epsilon_r. Since W is unitary, W^dagger bold-dot W=J, and approximate associativity gives ||Q||<=||W^dagger bold-dot(W bold-dot Q)||+epsilon_r||W||^2||Q||<=(1+epsilon_r)||W||C_grp*epsilon_r+epsilon_r||W||^2||Q||. The Cstar lower bound applied to W^dagger bold-dot W=J gives ||W||<=(1-epsilon_r)^(-1/2). Thus, after the C_der guard makes epsilon_r universally small, absorption yields ||Q||<=K_q*C_grp*epsilon_r for a universal K_q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Chart retention and coordinate legitimacy: the involution law and product estimate give ||U^dagger-sJ||<= (1+epsilon_r)(1+d)||A||. Therefore ||W-sJ||<=(1+epsilon_r)(1+C_ch*(epsilon_r+delta))*r+C_grp*epsilon_r<2delta by the stated guard. Since L_{sJ}=sI exactly, C=phi_{sJ}(W) has norm below 2delta; its Hermitian and anti-Hermitian projections are contractive because dagger is isometric. Writing B=C^parallel, unitarity of W implies f_{sJ}(C)=0, so uniqueness in lem-stage1-unitary-graph-control forces C^perp=G(B). Consequently W=chi_s(B) in the same sJ chart and B=F_s(A); all maps involved are C1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Exact coordinate factorization and pointwise radius: substituting U=sJ bold-dot(J+A+G(A)), W=sJ bold-dot(J+B+G(B)), and U^dagger=W bold-dot(J+Q) and cancelling the scalar s gives J-A+G(A)=(J+B+G(B)) bold-dot(J+Q). Taking the anti-Hermitian projection yields the exact identity -A=B+P^parallel((B+G(B)) bold-dot Q). Since ||G(B)||<=d||B|| and ||Q||<=K_q*C_grp*epsilon_r, choosing the C_der smallness guard so that (1+epsilon_r)(1+d)||Q||<=1/2 gives ||B||<=r+(1/2)||B||, hence ||B||<=2r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Differentiated coordinate identity: for xi in icalH set P=DF_s(A)xi and R=DQ(A)xi. Differentiating the exact full factorization gives -xi+DG(A)xi=P+DG(B)P+R+E, where E=(P+DG(B)P) bold-dot Q+(B+G(B)) bold-dot R. Hermitian/anti-Hermitian typing gives P+xi=-P^parallel(E) and R=DG(A)xi-DG(B)P-P^perp(E). By the local graph estimate in the second step at ||A||<=r and ||B||<=2r, ||DG(A)||,||DG(B)||<=K_g*r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Uniform linear absorption: for ||xi||=1 write p=||P|| and q=||R||. The product bound, ||Q||<=K_q*C_grp*epsilon_r, ||B||<=2r, ||G(B)||<=d||B||, and the local DG bounds imply ||E||<=alpha*p+beta*q with alpha<=K_1*epsilon_r and beta<=K_2*r for universal K_1,K_2. Hence p<=1+alpha*p+beta*q and q<=K_g*r*(1+p)+alpha*p+beta*q. If alpha,beta,K_g*r<=1/8, elementary absorption gives p<=2, q<=K_3*(epsilon_r+r), and therefore ||P+xi||<=||E||<=K_4*(epsilon_r+r), with universal K_3,K_4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Final constants and conclusion: choose kappa_der>0 universally small and at most 1/2, and choose C_der>=1 large enough, depending only on C_grp and the universal K constants above, so that C_der*(epsilon_r+r)<=kappa_der enforces every smallness and absorption condition and C_der>=K_4. The preceding estimate then holds uniformly for every unit xi and every A in B_r^{icalH}(0): ||(DF_s(A)+I)xi||<=C_der*(epsilon_r+r)||xi||. Since D(F_s-id)+2I=DF_s+I, this is exactly the asserted derivative inequality, while the fifth step proves the asserted same-chart retention; together with the aligned constants this proves the existential contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

