# Proof Export

## Node 1

**Statement:** Parameterized inversion-derivative transport: there exist C_der^0, C_ch^0, C_pol^0, C_grp^0 >= 1 and kappa_der^0, kappa_ch^0, kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_der >= C_der^0, C_ch >= C_ch^0, C_pol >= C_pol^0, C_grp >= C_grp^0, 0 < kappa_der <= kappa_der^0, 0 < kappa_ch <= kappa_ch^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0, every s in {+1, -1}, and every 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, and g_{sJ}: B_{2delta}^{icalH}(0) -> B_{2delta}^{calH}(0) for the unique C^1 map such that, for every A in B_{2delta}^{icalH}(0), f_{sJ}(A + g_{sJ}(A)) = 0, where f_{sJ}(B) = (1/2)*(((J + B^dagger) bold-dot (sJ)^dagger) bold-dot (sJ bold-dot (J + B)) - J), define chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)) and the global C^1 map sigma(U) = u_delta(U^dagger); then sigma maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart and, with F_s(A) = phi_{sJ}^par(sigma(chi_s(A))), one has ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for every A in B_r^{icalH}(0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix all four provider witness tuples and define the universal base chart, polar, and group thresholds before introducing any receiving Stage-1 polar witness datum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-stage1-explicit-group-domain-membership choose fixed universal (G_d,P_d,k_d); by lem-stage1-explicit-group-closeness choose fixed (G_c,P_c,k_c); by lem-stage1-polar-retraction choose fixed (P_r,k_r); and by lem-stage1-unitary-graph-control choose fixed (C_g,k_g), with every coefficient at least 1 and every margin in (0,1/2].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Define C_ch^0=max{1,C_g}, C_pol^0=max{1,P_d,P_c,P_r}, C_grp^0=max{1,G_d,G_c}, kappa_ch^0=min{1/2,k_g}, and kappa_pol^0=min{1/2,k_d,k_c,k_r}; these constants have the ranges required by root node 1 and are fixed before the receiving tuple.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For an arbitrary receiving tuple and object satisfying the root guards, monotonicity makes every fixed provider applicable and ordinary inverse or graph uniqueness synchronizes its displayed u_delta, h_delta, and g_{sJ} with the root-bound maps.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let x=epsilon_r*delta+delta^2>=0. From C_g<=C_ch and C_ch*(epsilon_r+delta)<=kappa_ch<=k_g, the graph provider guard holds. For P in {P_d,P_c,P_r}, P<=C_pol and C_pol*(epsilon_r+delta)<=kappa_pol<=the corresponding fixed margin, so every polar guard holds. For (G,P,k) equal to (G_d,P_d,k_d) or (G_c,P_c,k_c), G*epsilon_r<=C_grp*epsilon_r<delta-C_pol*x<=delta-P*x, so both explicit group providers apply. Also the receiving chart-retention inequality implies (1+epsilon_r)*(1+C_g*(epsilon_r+delta))*r+G_c*epsilon_r<2delta. The polar providers and the root display the identical Pi_delta on calU x B_delta^{calH}(J), with target its image, so uniqueness identifies their inverse pair with root-bound (u_delta,h_delta); uniqueness in lem-stage1-unitary-graph-control similarly identifies its V=sJ graph map with root-bound g_{sJ}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** At V=sJ the synchronized graph equation has the exact quadratic normal form; it gives G(0)=0, a coarse Lipschitz bound, and after one universal smallness cutoff the sharper estimate ||DG(T)|| <= K_g*r for every T in B_{2delta}^{icalH}(0) with ||T||<=2r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Write G=g_{sJ} and Z_T=T+G(T). Since sJ is unitary and (sJ)^dagger=sJ, exact unitality and bilinearity reduce the displayed graph equation to 0=f_{sJ}(Z_T)=G(T)+(1/2) Z_T^dagger bold-dot Z_T. At T=0, G=0 is a solution, so uniqueness in lem-stage1-unitary-graph-control gives G(0)=0; its derivative bound d=C_g*(epsilon_r+delta)<=k_g<=1/2 then gives ||G(T)||<=d||T||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** For every T in B_{2delta}^{icalH}(0) with ||T||<=2r, differentiating the exact quadratic equation in an arbitrary icalH-direction gives ||DG(T)||<=(1+epsilon_r)||Z_T||*(1+||DG(T)||). Node 1.3.1 gives ||Z_T||<=(1+d)||T||<=3r because d<=1/2. Thus, if epsilon_r+r<=b_g:=1/7, then a:=3(1+epsilon_r)r<=24/49<1/2; hence ||DG(T)||<=a/(1-a)<=6(1+epsilon_r)r<=7r. Therefore ||DG(T)||<=K_g*r on this domain with the universal choice K_g=7 (and in particular K_g depends only on the fixed provider data).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The root-bound formula sigma(U)=u_delta(U^dagger) is a global C1 map on calU, and for U=chi_s(A) its value W and the same polar inverse give one typed C1 factorization U^dagger=W bold-dot (J+Q) together with fixed-witness closeness.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The root-bound u_delta is the C1 first component supplied by lem-stage1-polar-retraction. By lem-stage1-explicit-group-domain-membership the same u_delta is defined at every U^dagger, and dagger is real-linear by def-epsilon-cstar-algebra; therefore sigma:U |-> u_delta(U^dagger) is globally C1 on calU. Also u_delta(sJ)=sJ, so sigma(sJ)=sJ.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** For A in B_r^{icalH}(0), lem-stage1-unitary-graph-control gives U=chi_s(A) in calU. Put W=sigma(U) and Q=h_delta(U^dagger)-J for the same synchronized polar inverse. Then W is in calU, Q is Hermitian with ||Q||<delta, U^dagger=W bold-dot(J+Q), and all depend C1 on A; lem-stage1-explicit-group-closeness for this same u_delta gives ||W-U^dagger||<=G_c*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The typed factorization and exact unitarity of W give a polar-normal estimate ||Q|| <= K_q*G_c*epsilon_r after a universal absorption cutoff, where only the fixed provider coefficient G_c occurs.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** From U^dagger=W bold-dot(J+Q), exact unitality gives U^dagger-W=W bold-dot Q, so fixed-witness closeness yields ||W bold-dot Q||<=G_c*epsilon_r. Since W is unitary, W^dagger bold-dot W=J; the Cstar lower bound gives ||W||<=(1-epsilon_r)^(-1/2) when epsilon_r<1. Approximate associativity and the product norm give ||Q||<=||W^dagger bold-dot(W bold-dot Q)||+epsilon_r*||W||^2*||Q||<=(1+epsilon_r)*||W||*G_c*epsilon_r+epsilon_r*||W||^2*||Q||. A universal cutoff on epsilon_r absorbs the last term and bounds the remaining fixed factor, giving ||Q||<=K_q*G_c*epsilon_r for a universal K_q; no receiving C_grp enters this estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** The root chart-retention guard puts W within 2delta of sJ, and the synchronized graph uniqueness then identifies W=chi_s(B) in the same chart with B=F_s(A).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** For U=sJ bold-dot(J+A+G(A)), involution and exact unitality give U^dagger=s(J-A+G(A)); hence ||U^dagger-sJ||<=||A||+||G(A)||<=(1+C_g*(epsilon_r+delta))*r. Adding the fixed closeness bound and using the receiving chart-retention guard by monotonicity yields ||W-sJ||<(1+epsilon_r)*(1+C_g*(epsilon_r+delta))*r+G_c*epsilon_r<2delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** Because L_{sJ}=sI, C=phi_{sJ}(W)=s(W-sJ) has norm below 2delta and its Hermitian and anti-Hermitian parts do too. Put B=C^par. Since W=sJ bold-dot(J+C) is unitary, the defining expression gives f_{sJ}(C)=0; uniqueness in lem-stage1-unitary-graph-control forces C^perp=G(B). Thus W=chi_s(B) in the same chart, B=phi_{sJ}^par(W)=F_s(A), and B,F_s are C1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** The typed polar factorization yields an exact coordinate identity for A,B,Q; its anti-Hermitian projection and the polar-normal estimate imply ||B||<=2r under a universal smallness cutoff.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.7.1

**Statement:** Substitute U=s(J+A+G(A)), W=s(J+B+G(B)), and U^dagger=W bold-dot(J+Q) into the typed factorization. Bilinearity and exact unitality give the exact identity J-A+G(A)=(J+B+G(B)) bold-dot(J+Q), equivalently -A+G(A)=B+G(B)+Q+(B+G(B)) bold-dot Q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.7.2

**Statement:** Taking anti-Hermitian parts gives -A=B+P^par((B+G(B)) bold-dot Q). Thus ||B||<=r+(1+epsilon_r)*(1+d)*||B||*||Q||. The fixed polar-normal bound and a universal cutoff make (1+epsilon_r)*(1+d)*||Q||<=1/2, so ||B||<=2r; therefore the sharp graph derivative estimate from node 1.3 applies at both A and B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Differentiating that exact identity and splitting Hermitian and anti-Hermitian parts gives a two-variable norm system; fixed-coefficient absorption yields ||(DF_s(A)+I)xi|| <= D_0*(epsilon_r+r)||xi||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.8.1

**Statement:** For xi in icalH set P=DF_s(A)xi and R=DQ(A)xi. Differentiating the exact identity in node 1.7 gives -xi+DG(A)xi=P+DG(B)P+R+E, where E=(P+DG(B)P) bold-dot Q+(B+G(B)) bold-dot R. Splitting anti-Hermitian and Hermitian parts gives P+xi=-P^par(E) and R=DG(A)xi-DG(B)P-P^perp(E).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.8.2

**Statement:** For ||xi||=1, p=||P|| and q=||R||, the product bound, ||Q||<=K_q*G_c*epsilon_r, ||B||<=2r, ||G(B)||<=d||B||, and ||DG(A)||,||DG(B)||<=K_g*r give ||E||<=alpha*p+beta*q with alpha<=K_1*epsilon_r and beta<=K_2*r for fixed universal K_1,K_2. Hence p<=1+alpha*p+beta*q and q<=K_g*r*(1+p)+alpha*p+beta*q. Universal cutoffs alpha,beta,K_g*r<=1/8 yield p<=2, then q<=K_3*(epsilon_r+r), and finally ||P+xi||<=||E||<=D_0*(epsilon_r+r); homogeneity gives the stated operator bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Let c_1,...,c_n>0 be the finitely many raw smallness cutoffs required in nodes 1.3, 1.5, 1.7, and 1.8, and let D=max{1,D_0,d_1,...,d_m}, where D_0 and the d_j are all fixed estimate coefficients occurring there. Put b_i=c_i/2, C_der^0=D, and kappa_der^0=min{1/2,b_1,...,b_n,1/(2D)}. These constants are universal and have the root's required ranges. For any receiving tuple, writing t=epsilon_r+r, the guards C_der>=C_der^0 and C_der*t<=kappa_der<=kappa_der^0 imply, for every i, t<=c_i/(2*C_der)<=c_i/2<c_i because C_der>=D>=1; hence every strict cutoff t<c_i (and therefore every non-strict cutoff) used upstream holds even at the permitted endpoints kappa_der=kappa_der^0 and C_der*t=kappa_der. They also imply D_0*t<=C_der*t. Thus node 1.8 gives ||DF_s(A)+I||<=C_der*(epsilon_r+r). Since D(F_s-id)+2I=DF_s+I, node 1.6 supplies chart retention and this is exactly the root estimate for every A; together with nodes 1.1 and 1.2 it completes all existential constants in node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.9.1

**Statement:** After fixing G_d,P_d,k_d,G_c,P_c,k_c,P_r,k_r,C_g,k_g, collect the finitely many positive smallness cutoffs used in nodes 1.3,1.5,1.7,1.8 as b_1,...,b_n and all fixed estimate coefficients, including the D_0 of node 1.8, into D=max{1,D_0,d_1,...,d_m}. Set C_der^0=D and kappa_der^0=min{1/2,b_1,...,b_n,1/(2D)}. These are universal and have the required ranges. For a receiving tuple, C_der>=C_der^0 and C_der*(epsilon_r+r)<=kappa_der<=kappa_der^0 enforce every cutoff and give D_0*(epsilon_r+r)<=C_der*(epsilon_r+r). Therefore ||DF_s(A)+I||<=C_der*(epsilon_r+r). Since D(F_s-id)+2I=DF_s+I, node 1.6 supplies chart retention and this is exactly the root estimate for every A; together with nodes 1.1 and 1.2 it proves all existential constants in node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

