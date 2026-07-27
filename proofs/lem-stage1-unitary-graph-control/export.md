# Proof Export

## Node 1

**Statement:** Uniform unitary graph control: there are universal C_ch >= 1, kappa_ch in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, every V in calUbar_delta, and every A^par in B^{icalH}_{2delta}(0), there is a unique g_V(A^par) in B^{calH}_{2delta}(0) with f_V(A^par + g_V(A^par)) = 0, and the corresponding V bold-dot (J + A^par + g_V(A^par)) lies in calU, where f_V(A) = (1/2)*(((J + A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J + A)) - J); moreover ||g_V(A^par) + (1/2)*(V^dagger bold-dot V - J)|| <= C_ch*(epsilon_r*delta + delta^2), ||Dg_V(A^par)|| <= C_ch*(epsilon_r + delta), and ||D_{A^perp} f_V(A^par + g_V(A^par)) - I_{calH}|| <= C_ch*(epsilon_r + delta) < 1; the resulting C^1 graph charts cover calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform multiplier control: write e=epsilon_r and s=e+delta. If 0<=e,delta and s<=1/512, V lies in calUbar_delta, and q=V^dagger bold-dot V-J, then ||V||<=1+2s, L_V is invertible, ||L_V^(-1)||<=2, and ||L_V^(-1)-L_{V^dagger}||<=8s. Moreover, whenever A has ||A||<=4delta, ||L_V^(-1)(L_{V bold-dot (J+A)}-L_V)||<=16s<1, so L_{V bold-dot (J+A)} is invertible and V bold-dot (J+A) has a right inverse.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Base multiplier estimate from the exact-unit epsilon_r-C*-axioms. Let Y be a right inverse of V, so V bold-dot Y=J. Since ||q||<=2delta and the C*-lower bound gives (1-e)||V||^2<=||V^dagger bold-dot V||<=1+2delta, s<=1/512 implies ||V||<=1+2s. Approximate associativity and exact unitality give ||V^dagger-Y||<=e||V||^2||Y||+(1+e)||q||||Y||<=4s||Y||, hence ||Y||<=||V||/(1-4s)<=2. Thus ||L_V L_Y-I||<=e||V||||Y||<1, so L_V has a right inverse. Also ||L_{V^dagger}L_V-I||<=e||V||^2+(1+e)||q||<=4s<1; therefore (L_{V^dagger}L_V)^(-1)L_{V^dagger} is a left inverse. The left and right inverses coincide, and the Neumann bounds yield ||L_V^(-1)||<=2 and ||L_V^(-1)-L_{V^dagger}||<=[4s/(1-4s)](1+e)||V||<=8s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Perturbation to the chart point. For ||A||<=4delta put X=V bold-dot (J+A)=V+V bold-dot A. The product-norm axiom and node 1.1.1 give ||L_X-L_V||<= (1+e)||X-V||<=4(1+e)^2(1+2s)delta<=8delta, whence ||L_V^(-1)(L_X-L_V)||<=16delta<=16s<1. The Neumann lemma makes L_X=L_V[I+L_V^(-1)(L_X-L_V)] invertible. Solving L_X(Y_X)=J then gives X bold-dot Y_X=J, so X has a right inverse.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Dependency-gated perturbation argument. Require validated node 1.1.1. Under the shared hypotheses e,delta >= 0, s=e+delta <= 1/512, V in calUbar_delta and ||A||<=4delta, node 1.1.1 supplies ||V||<=1+2s, invertibility of L_V, and ||L_V^(-1)||<=2. Exact unitality and bilinearity give X=V bold-dot(J+A)=V+V bold-dot A. Hence the product-norm axiom gives ||L_X-L_V||<= (1+e)||X-V||<= (1+e)^2||V||||A||<=4(1+e)^2(1+2s)delta<=8delta, where the last inequality follows from e<=s<=1/512. Therefore B=L_V^(-1)(L_X-L_V) satisfies ||B||<=16delta<=16s<=1/32<1. The Neumann series makes I+B invertible; the exact operator identity L_X=L_V(I+B) then makes L_X invertible. Setting Y_X=L_X^(-1)(J) gives X bold-dot Y_X=L_X(Y_X)=J, so X has a right inverse.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Explicit graph-equation estimates: under the hypotheses of node 1.1, define q=V^dagger bold-dot V-J and F(P,H)=f_V(P+H) on anti-Hermitian P and Hermitian H with ||P||,||H||<2delta. Then F is a C^1 map of finite-dimensional real spaces into calH and, with the explicit universal K=64, ||F(P,H)-(q/2+H)||<=K*(epsilon_r*delta+delta^2), ||D_H F(P,H)-I_calH||<=K*(epsilon_r+delta), and ||D_P F(P,H)||<=K*(epsilon_r+delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Zero-order expansion with no hidden big-O term. Put A=P+H, so ||A||<4delta and A+A^dagger=2H. Bilinearity gives 2F(P,H)=V^dagger bold-dot V-J+V^dagger bold-dot(V bold-dot A)+(A^dagger bold-dot V^dagger) bold-dot V+(A^dagger bold-dot V^dagger) bold-dot(V bold-dot A). Reassociate only the two linear terms and write V^dagger bold-dot V=J+q; then 2F=q+2H+R, where R=q bold-dot A+A^dagger bold-dot q+r_1+r_2+(A^dagger bold-dot V^dagger) bold-dot(V bold-dot A), ||r_1||,||r_2||<=e||V||^2||A||. Using ||q||<=2delta, ||V||<=1+2s from node 1.1.1, the product bound, s<=1/512, and ||A||<4delta gives ||R||<=128*(e*delta+delta^2). Hence ||F(P,H)-(q/2+H)||<=64*(e*delta+delta^2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Derivative expansion. For arbitrary Z, exact bilinearity and the exact reversal law give 2DF(P,H)[Z]=((Z^dagger bold-dot V^dagger) bold-dot(V bold-dot(J+A)))+(((J+A^dagger) bold-dot V^dagger) bold-dot(V bold-dot Z)). Reassociate the terms independent of A through V^dagger bold-dot V=J+q; their errors are bounded by e||V||^2||Z|| and their q-terms by 2(1+e)delta||Z||. Bound every term containing A directly using ||A||<4delta, ||V||<=1+2s, and the product norm. The two displayed summands then differ from Z^dagger and Z, respectively, by at most 32s||Z|| each, so ||DF(P,H)[Z]-(Z+Z^dagger)/2||<=32s||Z||<=64s||Z||. Restriction to Hermitian Z gives ||D_HF-I||<=64s, while restriction to anti-Hermitian Z gives ||D_PF||<=64s. Finally, with X=V bold-dot(J+A), exact product reversal identifies 2F=X^dagger bold-dot X-J, which is Hermitian; the displayed degree-two real polynomial is therefore C^1 from icalH times calH to calH.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Quantitative graph construction: if additionally c=64*(epsilon_r+delta)<=1/8, then for every P in B^{icalH}_{2delta}(0) there is a unique g_V(P) in B^{calH}_{2delta}(0) with F(P,g_V(P))=0. These values form a C^1 map and satisfy ||g_V(P)+q/2||<=64*(epsilon_r*delta+delta^2), ||Dg_V(P)||<=128*(epsilon_r+delta), and ||D_H F(P,g_V(P))-I_calH||<=64*(epsilon_r+delta)<1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Existence and uniqueness by the exact external lem-stage1-quantitative-inverse-function. Fix P and apply that lemma to h↦F(P,h) on B^{calH}_{2delta}(0), with the Banach-space isomorphism I_calH, center 0, radius 2delta, and derivative constant c=64s. Node 1.2 gives ||D_HF-I||<=c<1, so the map is injective and its image contains F(P,0)+B^{calH}_{2delta(1-c)}(0). Also node 1.2.1 and ||q||<=2delta give ||F(P,0)||<=delta+64(e delta+delta^2)=delta(1+c)<2delta(1-c), since c<=1/8. Hence 0 belongs to that image and determines a unique g_V(P) in the stated open ball.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Quantitative and C^1 dependence. Substituting H=g_V(P) in node 1.2.1 and using F(P,g_V(P))=0 gives ||g_V(P)+q/2||<=64(e delta+delta^2); node 1.2.2 directly gives the normal derivative estimate. For P_1,P_2, the lower Lipschitz inequality in lem-stage1-quantitative-inverse-function for h↦F(P_1,h), followed by integration of ||D_PF||<=c along the segment from P_1 to P_2, gives (1-c)||g_V(P_1)-g_V(P_2)||<=c||P_1-P_2||. Thus g_V is locally Lipschitz. Expanding the polynomial F at (P,g_V(P)) and using that Lipschitz bound shows that its Frechet derivative is Dg_V(P)=-(D_HF(P,g_V(P)))^(-1)D_PF(P,g_V(P)). The Neumann bound is ||(D_HF)^(-1)||<=1/(1-c), so ||Dg_V(P)||<=c/(1-c)<=2c=128s. Continuity of DF, of g_V, and of inversion on invertible operators makes Dg_V continuous; hence g_V is C^1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Unitary graph, covering, and constants closure: under nodes 1.1-1.3, X_V(P)=V bold-dot(J+P+g_V(P)) satisfies X_V(P)^dagger bold-dot X_V(P)=J and has a right inverse, hence belongs to calU; the C^1 injective graphs describe the local unitary locus and cover calU. Choosing the universal constants C_ch=1024 and kappa_ch=1/4 makes the root guard imply every smallness hypothesis in nodes 1.1-1.3, and their bounds strengthen to all three advertised C_ch estimates with strict normal-derivative bound <1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Exact graph, cover, and constant closure. For A=P+g_V(P), exact product reversal gives X_V(P)^dagger bold-dot X_V(P)-J=2F(P,g_V(P))=0; since ||A||<4delta, node 1.1.2 makes L_{X_V(P)} invertible and supplies a right inverse, so X_V(P) lies in calU by def-approximate-unitary-space. Since L_V is invertible, equality of two graph points forces equality of P+g_V(P), hence of their anti-Hermitian parts P; the inverse chart is phi_V^parallel. Conversely, every unitary in the coordinate box has f_V(A)=0 and the automatic right inverse, so node 1.3 identifies it with this graph. Every U in calU is covered by its self-centered chart because U lies in calUbar_delta, f_U(0)=0, and uniqueness gives g_U(0)=0. Finally set C_ch=1024 and kappa_ch=1/4. The root guard gives s<=1/4096<1/512 and 64s<=1/64<1/8, so nodes 1.1-1.3 apply; their bounds 64(epsilon_r delta+delta^2), 128s, and 64s are at most the corresponding C_ch bounds, with 64s<=C_ch s<=1/4<1. Thus the graph, cover, existence, uniqueness, membership, and all quantitative clauses of node 1 follow.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** The epsilon_r=0 boundary is included and valid. Node 1.1 assumes "0<=e,delta", i.e. 0<=e and 0<=delta, not 0<e; hence it and descendants 1.1.1-1.1.2 apply at e=0. Concretely there s=delta, exact associativity and exact unitality hold, and for a right inverse Y of V and q=V^dagger bold-dot V-J one has V^dagger=(V^dagger bold-dot V) bold-dot Y=Y+q bold-dot Y. Thus ||V^dagger-Y||<=||q||||Y||<=2delta||Y||; also L_{V^dagger}L_V=I+L_q with ||L_q||<=||q||<=2delta<1 under s<=1/4096. Together with the right inverse induced by Y this makes L_V invertible, with the same (indeed stronger) bounds used in 1.1.2. The perturbation estimate there uses only delta<=s and 16s<1, so it also applies at e=0 and gives a right inverse for X_V(P). Nodes 1.2 and 1.3 are stated under node 1.1 and likewise include e=0; their error terms simply specialize to O(delta^2) and O(delta). Therefore the root guard covers epsilon_r=0 with no omitted case.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.2

**Statement:** Dependency-gated graph and constants closure. Require validated nodes 1.1.1, 1.1.2.1, 1.3.1, and 1.3.2. Set C_ch=1024 and kappa_ch=1/4, and write e=epsilon_r, s=e+delta. The root guard gives s<=1/4096<1/512 and c=64s<=1/64<1/8, so all four dependencies apply. For P in B^{icalH}_{2delta}(0), nodes 1.3.1 and 1.3.2 give the unique H=g_V(P) in B^{calH}_{2delta}(0), its C^1 dependence, and the bounds ||H+q/2||<=64(e*delta+delta^2), ||Dg_V(P)||<=128s, and ||D_HF(P,H)-I_calH||<=64s. Put A=P+H, so ||A||<4delta. Exact product reversal and F(P,H)=0 give X=V bold-dot(J+A) with X^dagger bold-dot X-J=2F(P,H)=0; node 1.1.2.1 gives a right inverse for X, hence X lies in calU by def-approximate-unitary-space. Node 1.1.1 gives invertibility of L_V, and exact unitality gives phi_V(X)=L_V^(-1)(X-V)=A, so phi_V^parallel(X)=P. Thus the graph map is injective. Conversely, if X=V bold-dot(J+A) is unitary with ||A^parallel||,||A^perp||<2delta, then exact product reversal gives F(A^parallel,A^perp)=0, and uniqueness in 1.3.1 forces A^perp=g_V(A^parallel); therefore the graph is exactly the local unitary locus. For every U in calU, take V=U: then U lies in calUbar_delta, F(0,0)=0, and uniqueness gives g_U(0)=0, so U=X_U(0), proving the cover. Finally 64<=C_ch and 128<=C_ch yield the first two advertised bounds, while ||D_HF-I||<=64s<=C_ch*s<=1/4<1 gives the third bound with strictness. This proves every clause of node 1 using only the listed validated dependencies.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Graph-chart identification and cover. Since L_V is invertible, X_V(P_1)=X_V(P_2) implies P_1+g_V(P_1)=P_2+g_V(P_2); uniqueness of the Hermitian/anti-Hermitian decomposition gives P_1=P_2, so the C^1 parametrization is injective and its inverse is the continuous linear coordinate phi_V^parallel. More generally, if X=V bold-dot(J+A) lies in the coordinate box ||A^parallel||,||A^perp||<2delta, then X is unitary exactly when f_V(A)=0 together with the already automatic right-invertibility from node 1.1.2; node 1.3.1 identifies this zero locus exactly as A^perp=g_V(A^parallel). Finally every U in calU belongs to calUbar_delta for every delta>0. Taking V=U gives f_U(0)=0, and uniqueness yields g_U(0)=0, so U=X_U(0). Hence these C^1 graph charts cover calU.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.5

**Statement:** Constants-closing step: choose C_ch=1024 and kappa_ch=1/4. The guard C_ch*(epsilon_r+delta)<=kappa_ch implies all smallness hypotheses in nodes 1.1-1.4, and their conclusions give every existence, uniqueness, membership, estimate, C^1-chart, and covering clause of node 1 with the advertised C_ch bounds and strict normal-derivative bound <1.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.5.1

**Statement:** Dependency-gated closure. Set C_ch=1024 and kappa_ch=1/4. These are universal, C_ch>=1, and 0<kappa_ch<=1/2. For any delta>0 satisfying the root guard, s=epsilon_r+delta<=1/4096<1/512 and c=64s<=1/64<1/8. Thus nodes 1.1 and 1.2 apply, node 1.3 supplies the unique C^1 map g_V on the whole anti-Hermitian 2delta-ball, and node 1.4 supplies the unitary graph points and covering. The quantitative bounds strengthen to ||g_V(P)+q/2||<=64(epsilon_r delta+delta^2)<=C_ch(epsilon_r delta+delta^2), ||Dg_V(P)||<=128s<=C_ch s, and ||D_HF-I||<=64s<=C_ch s<=1/4<1. Since q=V^dagger bold-dot V-J and F(P,H)=f_V(P+H), these are literally the three estimates and all remaining clauses in node 1.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

