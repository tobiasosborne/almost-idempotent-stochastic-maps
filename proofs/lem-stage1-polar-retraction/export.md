# Proof Export

## Node 1

**Statement:** Closed C^1 polar retraction: there are universal C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, Pi_delta(U, H) = U bold-dot H is a C^1 diffeomorphism from calU x B^{calH}_delta(J) onto an open S_delta, its inverse (u_delta, h_delta) obeys X = u_delta(X) bold-dot h_delta(X), u_delta(U) = U, h_delta(U) = J, and calU_{delta - C_pol*(epsilon_r*delta + delta^2)} subseteq S_delta subseteq calU_{delta + C_pol*(epsilon_r*delta + delta^2)}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose universal constants C_pol and kappa_pol so that every occurrence below of C_ch*(epsilon_r+c*delta), every Neumann error, and every fixed finite product/associator error is at most 1/8 whenever C_pol*(epsilon_r+delta)<=kappa_pol; under this guard the algebraic coordinate estimates in node 1.1 hold uniformly.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Multiplier control from def-epsilon-cstar-algebra, with the scale hypothesis actually used below: fix absolute constants c,K>=1. If V lies in calUbar_r, r<=c*delta, and the root guard makes epsilon_r+delta sufficiently small, then (1-epsilon_r)||V||^2<=||V^dagger bold-dot V||<=1+2r, so ||V|| is universally bounded, and for every Z one has ||L_{V^dagger}L_V Z-Z||<=[epsilon_r||V||^2+2*(1+epsilon_r)*r]||Z||<=C_c*(epsilon_r+delta)||Z||. Choosing the root guard so that the last coefficient is at most 1/4 makes L_V invertible with universally bounded inverse. More generally, for every W with ||W-V||<=K*delta the same conclusions hold, with error at most C_{c,K}*(epsilon_r+delta), hence also with a uniform inverse bound after the same choice of root guard. Here c and K range only over the fixed absolute constants occurring below (in particular c=4), so all constants are absolute. No conclusion of small Neumann error is asserted from r<=1/4 alone.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** Let T_V=L_{V^dagger}L_V. Since V lies in calUbar_r, ||V^dagger bold-dot V-J||<=2r. Thus ||V^dagger bold-dot V||<=1+2r and the C*-lower bound gives (1-epsilon_r)||V||^2<=1+2r; under the root guard epsilon_r<=1/2 and r<=c*delta<=1/2, so ||V|| is bounded by an absolute constant depending only on the fixed c. For every Z, exact unitality and the associator/product axioms give ||T_V Z-Z||<=||V^dagger bold-dot(V bold-dot Z)-(V^dagger bold-dot V)bold-dot Z||+||(V^dagger bold-dot V-J)bold-dot Z||<=[epsilon_r||V||^2+2(1+epsilon_r)r]||Z||<=C_c(epsilon_r+delta)||Z||, where the final inequality uses r<=c*delta. This corrected scale hypothesis excludes the verifier counterexample, where r=1/4 is unrelated to delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.2

**Statement:** Write theta=C_c(epsilon_r+delta), made at most 1/4 by the root guard. The preceding estimate gives ||T_V Z||>=(1-theta)||Z||. Also ||L_{V^dagger}Y||<= (1+epsilon_r)||V|| ||Y||, hence ||L_V Z||>=(1-theta)/[(1+epsilon_r)||V||]||Z||. Therefore L_V is injective; as an endomorphism of the finite-dimensional space calX it is bijective, and ||L_V^{-1}||<=(1+epsilon_r)||V||/(1-theta), an absolute bound. The right-inverse clause in calUbar_r is not needed for this multiplier conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.3

**Statement:** If ||W-V||<=K*delta, bilinearity and the product bound imply ||W^dagger bold-dot W-V^dagger bold-dot V||<= (1+epsilon_r)||W-V||(||W||+||V||). Since ||W||<=||V||+K*delta and V is uniformly bounded, this is at most C_K*delta. Hence ||W^dagger bold-dot W-J||<=2r+C_K*delta<=C_{c,K}delta and W is uniformly bounded. Repeating the associator calculation from the first child yields ||L_{W^dagger}L_W-I||<=C_{c,K}(epsilon_r+delta). The root guard makes this at most 1/4, and the argument of the second child gives invertibility of L_W and a uniform inverse bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Coordinate estimate using lem-stage1-unitary-graph-control: at any base V in calUbar_r for r<=c*delta, write every unitary in its graph chart as U=V bold-dot (J+A), A=a+g_V(a), a in icalH. For H=J+q with q in calH, exact unitality and bilinearity give exactly p_V(a,q):=L_V^{-1}(U bold-dot H-V)=A+q+L_V^{-1}((V bold-dot A) bold-dot q). With the max norm on icalH x calH, the bound ||Dg_V||<=C_ch*(epsilon_r+c*delta), the multiplier control of node 1.1.1, and ||g_V(0)+(1/2)(V^dagger bold-dot V-J)||<=C_ch*(epsilon_r*c*delta+c^2*delta^2), differentiation gives ||Dp_V-I||<=C_0*(epsilon_r+delta) on ||a||<2c*delta, ||q||<3delta/2, and p_V(0,0)=g_V(0), hence ||p_V(0,0)+(1/2)(V^dagger bold-dot V-J)||<=C_0*(epsilon_r*delta+delta^2). Here lem-stage1-unitary-graph-control is applied at scale c*delta (with fixed c, later c=4), and all uses satisfy its guard by the choice of C_pol,kappa_pol.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Internal multiplier estimate (replacing the unvalidated sibling 1.1.1). Put s=c*delta. Since V is in calUbar_r and r<=s, ||V^dagger bold-dot V-J||<=2s. The C*-lower axiom and the triangle inequality give (1-epsilon_r)||V||^2<=||V^dagger bold-dot V||<=1+2s, so the parent smallness guard gives a universal bound ||V||<=M_V. For every Z, exact unitality and one use each of approximate associativity and the product bound give ||V^dagger bold-dot(V bold-dot Z)-Z||<=epsilon_r||V||^2||Z||+2(1+epsilon_r)s||Z||=:theta||Z||. The constants in node 1.1 are chosen so theta<=1/2. Hence T:=L_{V^dagger}L_V is invertible by its Neumann series and ||T^{-1}||<=2. Thus L_V is injective; as an endomorphism of the finite-dimensional space it is bijective, and L_V^{-1}=T^{-1}L_{V^dagger}, so ||L_V^{-1}||<=2(1+epsilon_r)||V||<=M_L universally. This proves inside node 1.1.2, without using sibling 1.1.1, that p_V is defined and has the needed uniform inverse-multiplier bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** Graph and coordinate bounds. Apply the allowed lem-stage1-unitary-graph-control at scale s=c*delta: V is in calUbar_s, ||a||<2s, and its guard follows from node 1.1. Set A(a)=a+g_V(a). The external estimates give eta_g:=sup||Dg_V||<=C_ch*(epsilon_r+s) and ||g_V(0)+(1/2)(V^dagger bold-dot V-J)||<=C_ch*(epsilon_r*s+s^2). Since half the displayed defect has norm at most r<=s, the fundamental theorem of calculus along t*a gives ||A(a)||<=||a||+||g_V(0)||+eta_g||a||<=C_A*delta for a universal C_A (c is the fixed universal scale factor and the parent guard bounds eta_g). For U=V bold-dot(J+A(a)) and H=J+q, exact unitality and bilinearity, without reassociation, give U bold-dot H-V=L_V(A(a)+q)+(V bold-dot A(a)) bold-dot q. Applying the inverse from the preceding child proves exactly p_V(a,q)=A(a)+q+L_V^{-1}((V bold-dot A(a)) bold-dot q).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.3

**Statement:** Derivative and base-point estimates. For tangent increments h in icalH and k in calH, differentiation of the exact bilinear formula in the preceding child yields Dp_V(a,q)(h,k)-(h+k)=Dg_V(a)h+L_V^{-1}(((V bold-dot(h+Dg_V(a)h)) bold-dot q)+((V bold-dot A(a)) bold-dot k)). With ||(h,k)||_max<=1, ||q||<3delta/2, the product axiom twice, and the bounds eta_g, M_V, M_L, C_A from the preceding children, its norm is at most eta_g+M_L(1+epsilon_r)^2*M_V*((1+eta_g)*(3delta/2)+C_A*delta)<=C_0*(epsilon_r+delta), where C_0 is universal and the last inequality uses s=c*delta with fixed c and the parent smallness guard. At (a,q)=(0,0), the exact formula gives p_V(0,0)=g_V(0), while the external graph estimate at scale s gives ||p_V(0,0)+(1/2)(V^dagger bold-dot V-J)||<=C_ch*(epsilon_r*c*delta+c^2*delta^2)<=C_0*(epsilon_r*delta+delta^2). These are precisely both estimates claimed in node 1.1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For each admissible approximate-unitary base V, the coordinate polar map p_V constructed in node 1.2 is quantitatively one-to-one and locally C^1 invertible, and when the defect of V is below delta by the stated C_pol*(epsilon_r*delta+delta^2) margin it has a unique zero with Hermitian polar displacement of norm <delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For the coordinate map p_V on the convex box B={||a||<2c*delta, ||q||<3delta/2}, children 1.2.1.1--1.2.1.2 establish directly from def-epsilon-cstar-algebra and lem-stage1-unitary-graph-control that p_V is C^1 and theta:=sup_B ||J_0^{-1}(Dp_V-J_0)||<=1/4, where J_0(alpha,beta)=alpha+beta is the canonical real-linear isomorphism icalH direct-sum calH to calX and the domain has the max norm. For z,z' in B, integration along the line segment gives ||J_0^{-1}(p_V(z)-p_V(z'))-(z-z')||_max<=theta||z-z'||_max. This implies injectivity and quantitative bi-Lipschitz control. Also Dp_V=J_0(I+J_0^{-1}(Dp_V-J_0)) is invertible by the convergent Neumann series, with inverse norm at most (1-theta)^{-1}||J_0^{-1}||. The finite-dimensional C^1 inverse function theorem then makes p_V a local C^1 diffeomorphism, and injectivity makes it a C^1 diffeomorphism B onto its open image. No pending sibling is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** For the base V and scale r=c*delta occurring here (with fixed c and the root guard chosen small), the epsilon-C*-axioms give ||L_{V^dagger}L_V-I|| <= C*(epsilon_r+r): indeed L_{V^dagger}L_V Z-Z is the sum of the associator V^dagger bold-dot (V bold-dot Z)-(V^dagger bold-dot V) bold-dot Z and (V^dagger bold-dot V-J) bold-dot Z, bounded respectively by epsilon_r*||V||^2*||Z|| and (1+epsilon_r)*2r*||Z||; while (1-epsilon_r)||V||^2 <= ||V^dagger bold-dot V|| <= 1+2r bounds ||V|| universally. Thus the guard makes the displayed operator norm at most 1/4. Hence L_V is injective, and because it is an endomorphism of the finite-dimensional space it is bijective; moreover if T=L_{V^dagger}L_V and ||T-I||<=1/4, then ||T^{-1}||<=4/3 and L_V^{-1}=T^{-1}L_{V^dagger}, so ||L_V^{-1}|| is universally bounded.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.2

**Statement:** Fix r=c*delta (c fixed). The epsilon-C*-axioms imply ||V||^2<=(1+2r)/(1-epsilon_r), and the direct associator calculation ||L_{V^dagger}L_V-I||<=epsilon_r||V||^2+2(1+epsilon_r)r. The root guard makes this at most 1/4, so the Neumann series for T=L_{V^dagger}L_V gives ||T^{-1}||<=4/3; finite dimensionality gives L_V^{-1}=T^{-1}L_{V^dagger} and hence a universal bound N on ||L_V^{-1}||. Lem-stage1-unitary-graph-control supplies the C^1 map A(a)=a+g_V(a), with d:=sup||Dg_V||<=C_ch(epsilon_r+r). Exact unitality and bilinearity give p_V(a,q)=A(a)+q+L_V^{-1}((V bold-dot A(a)) bold-dot q), hence Dp_V(alpha,beta)=alpha+beta+Dg_V(a)alpha+L_V^{-1}((V bold-dot(alpha+Dg_V(a)alpha)) bold-dot q)+L_V^{-1}((V bold-dot A(a)) bold-dot beta). Moreover the graph lemma and ||V^dagger bold-dot V-J||<=2r give ||g_V(0)||<=r+C_ch*(epsilon_r*r+r^2), and the mean-value estimate gives ||A(a)||<=||a||+||g_V(0)||+d||a||<=K*delta on ||a||<2c*delta, for a universal K after shrinking the guard. With M:=sup||V||, the product axiom therefore bounds, for ||(alpha,beta)||_max<=1, ||Dp_V(alpha,beta)-(alpha+beta)|| <= d+N*(1+epsilon_r)*M*(1+d)*(3delta/2)+N*(1+epsilon_r)*M*K*delta <= C_0*(epsilon_r+delta). Let J_0(alpha,beta)=alpha+beta. Since J_0^{-1}x=((x-x^dagger)/2,(x+x^dagger)/2) and the involution is isometric, ||J_0^{-1}||<=1 from calX to the max norm. Consequently sup||J_0^{-1}(Dp_V-J_0)||<=C_0*(epsilon_r+delta)<=1/4 after choosing the universal root guard. Thus the indispensable C^1 coordinate map and derivative estimate are proved here from allowed inputs, not imported from pending node 1.1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.3

**Statement:** Let B be the open convex coordinate box, with max norm, and J_0(alpha,beta)=alpha+beta. Put E_z=J_0^{-1}(Dp_V(z)-J_0); child 1.2.1.2 gives sup_B||E_z||=theta<=1/4. For z,z' in B, the finite-dimensional fundamental theorem of calculus along gamma(t)=z'+t(z-z') gives p_V(z)-p_V(z')-J_0(z-z')=integral_0^1 (Dp_V(gamma(t))-J_0)(z-z')dt. Applying J_0^{-1} yields ||J_0^{-1}(p_V(z)-p_V(z'))-(z-z')||_max<=theta||z-z'||_max, and hence (1-theta)||z-z'||_max<=||J_0^{-1}(p_V(z)-p_V(z'))||_max<=(1+theta)||z-z'||_max. Thus p_V is injective and bi-Lipschitz (equivalently in the original codomain norm, since J_0 is a fixed isomorphism). At each z, Dp_V(z)=J_0(I+E_z); the norm-convergent series sum_{n>=0}(-E_z)^n inverts I+E_z and has norm at most (1-theta)^{-1}, so Dp_V(z) is invertible. The finite-dimensional C^1 inverse function theorem makes p_V a local C^1 diffeomorphism and therefore an open map. Its injectivity makes the local inverses agree, yielding a C^1 inverse on p_V(B); hence p_V:B to p_V(B) is a C^1 diffeomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Put D:=epsilon_r*delta+delta^2. For V in calU_{delta-C_pol*D}, apply the registered external lem-stage1-unitary-graph-control at scale delta and define, after identifying icalH x calH with icalH+calH, p_V(a,q):=L_V^{-1}(([V bold-dot (J+a+g_V(a))] bold-dot (J+q))-V). The axioms in def-epsilon-cstar-algebra, the defect bound for V, and the external graph estimates give universal constants K_b,K_d such that ||p_V(0,0)||<delta-(C_pol-K_b)*D and theta:=sup||Dp_V-I||<=K_d*(epsilon_r+delta) on the convex box ||a||<2delta, ||q||<3delta/2. Choose C_pol>K_b+K_d and the universal guard so theta<1. Then ||p_V(0,0)||<delta-K_d*D<=(1-theta)*delta. Hence some rho<delta satisfies ||p_V(0,0)||/(1-theta)<rho, and F(z):=z-p_V(z) is a theta-contraction of the closed max-norm rho-ball into itself. Its unique fixed point z=(a,q) has p_V(a,q)=0. The same derivative estimate integrated on line segments makes p_V injective on the full convex box, so this zero is the only one there. Finally p_V(a,q)=0 is exactly V=[V bold-dot (J+a+g_V(a))] bold-dot (J+q), with ||q||<delta and the bracketed factor in calU by lem-stage1-unitary-graph-control.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Self-contained coordinate estimates from the allowed inputs. Let e:=epsilon_r and let V be as in node 1.2.2, so V lies in calUbar_delta. From def-epsilon-cstar-algebra, (1-e)||V||^2<=||V^dagger bold-dot V||<=1+2delta; hence ||V|| is universally bounded under the guard. For every Z, ||V^dagger bold-dot(V bold-dot Z)-Z|| is at most the sum of the associator error e||V||^2||Z|| and ||(V^dagger bold-dot V-J) bold-dot Z||<=2(1+e)delta||Z||. Thus ||L_{V^dagger}L_V-I||<=C(e+delta)<1/2. Neumann inversion of L_{V^dagger}L_V makes L_V injective, hence bijective in finite dimension, and gives ||L_V^{-1}||<=M for a universal M. Apply the registered external lem-stage1-unitary-graph-control at scale delta. With A(a):=a+g_V(a), exact unitality and bilinearity give exactly p_V(a,q)=A(a)+q+L_V^{-1}((V bold-dot A(a)) bold-dot q). Decompose X=icalH direct-sum calH by T(X):=((X-X^dagger)/2,(X+X^dagger)/2); both projections have norm at most one and ||a+q||<=2 max(||a||,||q||). The external bounds ||Dg_V||<=C_ch(e+delta), ||g_V(0)+(V^dagger bold-dot V-J)/2||<=C_ch*(e*delta+delta^2), together with ||a||<2delta, ||q||<3delta/2, ||g_V(a)||<2delta, the product bound, and ||L_V^{-1}||<=M, yield by differentiating the displayed exact formula ||D(T p_V)-I||<=K_d(e+delta) for a universal K_d. Also p_V(0,0)=g_V(0), so, writing D:=e*delta+delta^2 and K_b:=C_ch, ||T p_V(0,0)||=||g_V(0)||<delta-(C_pol-K_b)D. No sibling node is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Corrected margin, existence, and full-box uniqueness. Choose C_pol>K_b+K_d and shrink the universal guard so theta:=K_d(epsilon_r+delta)<1/4. The strict base-point estimate from the preceding child gives B:=||T p_V(0,0)||<delta-(C_pol-K_b)D<delta-K_d D<=(1-theta)delta; the final comparison is deliberately non-strict, and strictness comes from the preceding inequality. Choose B/(1-theta)<rho<delta. On the closed max-norm rho-ball, F(z):=z-T p_V(z) satisfies ||F(z)-F(w)||<=theta||z-w|| and ||F(z)||<=B+theta*rho<rho. Completeness and the contraction theorem give a unique fixed point z=(a,q) in that ball, equivalently p_V(a,q)=0. Moreover for any z,w in the full convex box ||a||<2delta, ||q||<3delta/2, integration along the segment and the derivative estimate give ||T p_V(z)-T p_V(w)-(z-w)||<=theta||z-w||. Therefore two zeros satisfy ||z-w||<=theta||z-w|| and are equal. This establishes uniqueness on the full box without node 1.2.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.3

**Statement:** Conclusion and dependency repair. Since L_V is invertible, p_V(a,q)=0 is equivalent by its defining exact formula to [V bold-dot(J+a+g_V(a))] bold-dot(J+q)=V. The fixed point has ||a||,||q||<rho<delta, so a is in the external graph lemma domain B^{icalH}_{2delta}(0), and that lemma makes U:=V bold-dot(J+a+g_V(a)) an element of calU. Thus V=U bold-dot(J+q) with ||q||<delta, and the preceding child gives the required uniqueness. Children 1.2.2.1 and 1.2.2.2 derive every estimate and the injectivity argument directly from the two registered definitions and lem-stage1-unitary-graph-control; pending siblings 1.1.2 and 1.2.1 are not dependencies. The corrected chain is B<delta-K_d D<=(1-theta)delta, so the equality case identified by the verifier is harmless.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The local coordinate result implies that Pi_delta is a globally injective C^1 local diffeomorphism, hence a C^1 diffeomorphism onto its open image S_delta, with the stated inverse and its normalization on calU, as shown in node 1.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Local statement: in a graph chart about U in calU supplied by lem-stage1-unitary-graph-control, write U'=U bold-dot (J+a+g_U(a)) and H'=J+q. After applying the fixed linear target coordinate L_U^{-1}(.-U), Pi_delta is exactly p_U(a,q). Nodes 1.1.2 and 1.2.1 show its derivative is invertible for ||q||<delta, so Pi_delta is C^1 and a local C^1 diffeomorphism at every (U,H). Consequently its image S_delta is open, and any globally defined inverse is C^1 on the local images.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Global step: under the universal smallness guard, if X=U_i bold-dot (J+q_i) with U_i in calU, q_i in calH, and ||q_i||<delta for i=1,2, then U_1=U_2 and q_1=q_2. Independently, Pi_delta is a C^1 local diffeomorphism at every point of calU x B_delta^{calH}(J). Hence Pi_delta is a C^1 diffeomorphism onto its open image S_delta; its inverse (u_delta,h_delta) satisfies X=u_delta(X) bold-dot h_delta(X), and u_delta(U)=U, h_delta(U)=J for U in calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Let e=epsilon_r. For every U in calU, the C*-lower bound and U^dagger bold-dot U=J give (1-e)||U||^2<=1. Also ||L_{U^dagger}L_U-I||<=e||U||^2 by the associator axiom. Thus, once e<=1/8, ||U||<2, L_U is invertible in finite dimension, and ||L_U^{-1}||<=K for a universal K (indeed ||Z||<=(1-e||U||^2)^{-1}(1+e)||U|| ||L_U Z||). If X=U bold-dot(J+q), ||q||<delta, then X-U=U bold-dot q and ||L_X-L_U||<= (1+e)^2||U||delta. The root guard may therefore be decreased so that ||L_U^{-1}(L_X-L_U)||<=1/2; the Neumann lemma gives invertibility of L_X and ||L_X^{-1}||<=2K, hence X has the right inverse L_X^{-1}J. Expanding around q=0 without losing the q factor, X^dagger bold-dot X-J=[U^dagger bold-dot(U bold-dot q)-q]+[(q bold-dot U^dagger) bold-dot U-q]+(q bold-dot U^dagger) bold-dot(U bold-dot q)+2q. The two bracketed terms are associators, so ||X^dagger bold-dot X-J||<=2delta+2e||U||^2delta+(1+e)^3||U||^2delta^2. After the same universal guard this is <=8delta, so X lies in calUbar_{4delta}. Finally A:=L_X^{-1}(U-X) obeys ||A||<8delta after decreasing the guard (for e<=1/8 the displayed bounds allow ||L_X^{-1}||<=3 and ||U-X||<3delta). These conclusions hold for each factorization i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Apply lem-stage1-unitary-graph-control to the base X at scale 4delta, which is allowed by the root guard and the preceding child. For A_i:=L_X^{-1}(U_i-X), write a_i=(A_i-A_i^dagger)/2 in icalH and b_i=(A_i+A_i^dagger)/2 in calH. The involution is isometric, so ||a_i||,||b_i||<=||A_i||<8delta. Since U_i=X bold-dot(J+A_i) and U_i^dagger bold-dot U_i=J, the defining expression f_X(A_i) is zero. Uniqueness in the established graph lemma therefore gives b_i=g_X(a_i), so U_i=X bold-dot(J+a_i+g_X(a_i)). For ||a||<8delta and ||q||<delta define p_X(a,q):=L_X^{-1}([X bold-dot(J+a+g_X(a))] bold-dot(J+q)-X). Exact unitality and bilinearity, with no reassociation, give p_X(a,q)=a+g_X(a)+q+L_X^{-1}((X bold-dot(a+g_X(a))) bold-dot q). The graph bounds, the preceding uniform bounds for X and L_X^{-1}, and the product axiom imply ||Dp_X-I_0||<=C_0(e+delta) on this convex box, where I_0(a,q)=a+q and C_0 is universal: explicitly the error derivative is Dg_X plus L_X^{-1} applied to (X bold-dot(da+Dg_X da)) bold-dot q+(X bold-dot(a+g_X(a))) bold-dot dq; here ||Dg_X||<=C_ch(e+4delta), while ||g_X(a)||<=||g_X(0)||+C_ch(e+4delta)||a||=O(delta), using the graph estimate at 0 and ||X^dagger bold-dot X-J||<=8delta. Choose the root guard so theta:=C_0(e+delta)<1. For z,z_prime in the box, integration on the line segment gives ||p_X(z)-p_X(z_prime)-I_0(z-z_prime)||<=theta||z-z_prime||_max. Since the Hermitian and anti-Hermitian projections both have norm at most one, ||z-z_prime||_max<=||I_0(z-z_prime)||. Hence p_X(z)=p_X(z_prime) forces z=z_prime.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.3

**Statement:** For each i, the original equality X=U_i bold-dot(J+q_i) and the definition of p_X give p_X(a_i,q_i)=0 exactly. The injectivity proved in the preceding child yields (a_1,q_1)=(a_2,q_2); substituting in U_i=X bold-dot(J+a_i+g_X(a_i)) gives U_1=U_2. Thus Pi_delta is globally injective; it is surjective onto S_delta by the definition S_delta:=Pi_delta(calU x B_delta^{calH}(J)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.4

**Statement:** It remains to establish the local statement without citing a sibling. Fix (U,J+q) with U in calU and ||q||<delta. The first child gives a uniformly bounded L_U^{-1}. Use the graph chart from lem-stage1-unitary-graph-control at the exact-unitary base U and target coordinate L_U^{-1}(.-U). In these coordinates Pi_delta is the same explicit map p_U(a,q_prime) from the second child. Because U^dagger bold-dot U=J, uniqueness in the graph lemma gives g_U(0)=0; its derivative bound and the displayed differentiated formula give ||Dp_U-I_0||<=C_1(e+delta)<1 under the root guard. As I_0 is a real-linear isomorphism icalH direct-sum calH -> calX, the Neumann lemma makes Dp_U invertible. The finite-dimensional C^1 inverse function theorem makes Pi_delta a local C^1 diffeomorphism at every point, so S_delta is open. Combining this with global bijectivity from the preceding child, the local inverses agree on overlaps with the set-theoretic inverse and hence glue to a C^1 inverse (u_delta,h_delta). Its defining property is X=u_delta(X) bold-dot h_delta(X). Finally U=U bold-dot J by exact unitality and J belongs to B_delta^{calH}(J); global uniqueness gives u_delta(U)=U and h_delta(U)=J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Direct defect estimates and the zero-existence margin give calU_{delta-C_pol*(epsilon_r*delta+delta^2)} subseteq S_delta subseteq calU_{delta+C_pol*(epsilon_r*delta+delta^2)}, as shown in node 1.4; together nodes 1.1--1.4 prove the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Radius sandwich. For X=U bold-dot(J+q) in S_delta, ||q||<delta and U^dagger bold-dot U=J. By the star rule and bilinearity, X^dagger bold-dot X-J is the sum of U^dagger bold-dot(U bold-dot q), (q bold-dot U^dagger) bold-dot U, and (q bold-dot U^dagger) bold-dot(U bold-dot q). Subtract q=(U^dagger bold-dot U) bold-dot q from the first cross term and q=q bold-dot(U^dagger bold-dot U) from the second; the two differences are associators, so def-epsilon-cstar-algebra and the universal bound on ||U|| from node 1.1.1 give ||X^dagger bold-dot X-J||<2delta+C_out*(epsilon_r*delta+delta^2). Also L_X is a small perturbation of invertible L_U, hence X has a right inverse. Taking C_pol>=C_out/2 yields X in calU_{delta+C_pol*(epsilon_r*delta+delta^2)}, proving the outer inclusion. Conversely, if V lies in calU_{delta-C_pol*(epsilon_r*delta+delta^2)}, the guard makes the displayed inner radius positive and node 1.2.2 supplies a in icalH and q in calH with ||q||<delta and V=[V bold-dot(J+a+g_V(a))] bold-dot(J+q); lem-stage1-unitary-graph-control makes the bracketed factor an element of calU, so V lies in S_delta. This proves the inner inclusion. Finally take C_pol at least all finitely many absolute thresholds above and take kappa_pol>0 no larger than 1/2 and small enough that the graph guards at scales through 4delta and all Neumann bounds in nodes 1.1--1.3 hold; these choices are universal and complete the sandwich.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** Dependency-gated radius-sandwich bridge. Require validated nodes 1.1.1 and 1.2.2. For the outer inclusion, if X=U bold-dot (J+q) lies in S_delta, then U lies in calU=calUbar_0 and ||q||<delta. Apply validated node 1.1.1 to U with r=0: ||U|| and ||L_U^{-1}|| are bounded by absolute constants. Bilinearity and the product bound give ||X-U||=||U bold-dot q||<=C*delta and ||L_X-L_U||<=C*delta; the universal root guard makes ||L_U^{-1}(L_X-L_U)||<1, so the Neumann series makes L_X invertible and Y:=L_X^{-1}J is a right inverse of X. The explicit star-rule expansion in the parent has two linear terms equal to q up to associators of norm at most C*epsilon_r*delta and one quadratic term of norm at most C*delta^2, hence ||X^dagger bold-dot X-J||<2*delta+C_out*(epsilon_r*delta+delta^2). Choosing C_pol>=C_out/2 gives X in calU_{delta+C_pol*(epsilon_r*delta+delta^2)}. For the inner inclusion, validated node 1.2.2 applies to every V in calU_{delta-C_pol*(epsilon_r*delta+delta^2)} and supplies a in icalH and q in calH with ||q||<delta and V=[V bold-dot(J+a+g_V(a))] bold-dot(J+q); its cited application of lem-stage1-unitary-graph-control makes U:=V bold-dot(J+a+g_V(a)) an element of calU. Therefore V=Pi_delta(U,J+q) lies in S_delta. Finally choose one universal C_pol at least the finitely many lower bounds in validated nodes 1.1.1 and 1.2.2 and C_out/2, and choose kappa_pol in (0,1/2] below their finitely many guard thresholds; taking a finite maximum and positive finite minimum preserves universality. Thus the parent sandwich follows, and no conclusion is available from this bridge until both declared validation dependencies are validated.

**Type:** qed

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

