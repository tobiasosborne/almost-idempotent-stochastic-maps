# Proof Export

## Node 1

**Statement:** There are universal C_nest < infinity and e_nest > 0 such that, whenever R,P,Q are t-projections in a finite-dimensional extended t-C*-algebra, R is nonvanishing, P,Q are subordinate to R with all four left/right subordination errors at most t <= e_nest, A_R = S^A_R, P^R = Co^A_R(P), and Q^R = Co^A_R(Q), then P^R,Q^R are C_nest*t-projections in A_R and, at every amplification, ||F^R_{P,Q}(Co^A_R X) - X|| <= C_nest*t*||X|| for X in S^A_{P,Q}, while ||Co^A_{P,Q} Y - Y|| <= C_nest*t*||Y|| for Y in S^{A_R}_{P^R,Q^R}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix universal constants K_def,e_def witnessing the O(delta+epsilon) compression-to-raw-product bounds in def-compressed-corner, and the constants and thresholds in the five named externals. After shrinking a universal e_nest, every t-projection used below, at every amplification, has uniformly bounded norm; moreover P^R=Co^A_R(P) and Q^R=Co^A_R(Q) differ from P,Q by O(t), with universal dimension-free coefficients.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Uniform norm bound: if T is any t-projection in the extended t-C*-algebra and t<=1/4, the C*-lower bound and product-norm axiom give (1-t)||T||^2 <= ||T^2|| <= ||T||+t, hence ||T||<=2. By the block-diagonal operator-space axiom, ||I_n tensor T||=||T|| for every n. Thus R,P,Q and their amplifications have norm at most 2, and every factor occurring in the fixed telescopes is uniformly bounded after the O(t) perturbations below.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Outer-compression bound: let K_def,e_def be universal witnesses for the compression-to-each-raw-map O(delta+epsilon) estimate in def-compressed-corner. Since ||PR-P||,||RP-P||<=t, product-norm and triangle inequalities give ||R(PR)-P||<=t+(1+t)||R||t and ||(RP)R-P||<=t+(1+t)||R||t; hence, for 2t<=e_def, ||P^R-P||<=K_P*t, universally. The identical argument gives ||Q^R-Q||<=K_P*t. By lem-compcb-amplified-compression these same bounds hold for I_n tensor P^R versus I_n tensor P and for Q at every n, with no n-dependent coefficient.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The external lem-compcb-corner-algebra makes A_R=S^A_R an extended O(t)-C*-algebra. In that algebra P^R and Q^R are Hermitian and have compressed-product idempotence defects O(t), hence are C_proj*t-projections for a universal C_proj.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Apply lem-compcb-corner-algebra to the nonvanishing t-projection R in the extended t-C*-algebra (so delta+epsilon=2t): for 2t<=e_ca, A_R=S^A_R with compressed product a dot_R b=Co^A_R(ab), inherited dagger, and compressed unit is an extended 2*C_ca*t-C*-algebra. By lem-compcb-amplified-compression-identities, Co_R is idempotent and dagger-preserving on the diagonal; since P,Q are Hermitian, P^R=Co_R(P) and Q^R=Co_R(Q) are Hermitian elements of A_R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Let a=P^R and p=P. Bilinearity gives a^2-p^2=(a-p)a+p(a-p), so node 1.1's uniform bounds imply ||a^2-a||<=((1+t)(||a||+||p||)K_P+1+K_P)t=K_0*t. Because a lies in range(Co_R), Co_R(a)=a; and def-compressed-corner plus the uniform bound on R makes ||Co_R|| universally bounded. Therefore ||a dot_R a-a||=||Co_R(a^2-a)||<=K_1*t. The same proof applies to Q^R. Together with the preceding exact Hermitian identities, P^R,Q^R are C_proj*t-projections in A_R for a universal C_proj.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every n and X in M_n tensor S^A_{P,Q}, amplified almost-containment gives Co^A_{R_n}(X)=X+O(t)||X||; expanding F^R_{P,Q}=Co^{A_R}_{P^R,Q^R}, replacing its two internal products by ambient products, and replacing P^R,Q^R,Co_R X by P,Q,X gives ||F^R_{P,Q}(Co^A_R X)-X|| <= C_fwd*t*||X|| with a universal coefficient independent of n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Fix n, put R_n=I_n tensor R, P_n=I_n tensor P, Q_n=I_n tensor Q, and let X lie in M_n tensor S^A_{P,Q}. In lem-compcb-amplified-almost-containment take the projection-defect and algebra parameters both equal to t and instantiate (P_1,P,Q_1,Q)=(P,R,Q,R). The hypotheses are exactly ||PR-P||<=t and ||QR-Q||<=t; hence, whenever 2t<=e_ac, Z:=Co^A_{R_n}(X) satisfies ||Z-X||<=2*C_ac*t||X|| and therefore ||Z||<=(1+2*C_ac*t)||X||. Lem-compcb-amplified-compression gives Co^A_{R_n}=I_n tensor Co^A_R and M_n tensor S^A_R=S^A_{R_n}, so Z=(I_n tensor Co^A_R)X lies in M_n tensor A_R. No estimate for P^R-P or Q^R-Q is asserted or used in this node.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** In the extended 2*C_ca*t-C*-algebra A_R, node 1.2 makes P^R,Q^R C_proj*t-projections. Thus def-compressed-corner, at level n using lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities, makes F_n=Co^{A_R}_{P^R_n,Q^R_n} differ by at most K_def*(C_proj+2*C_ca)t from each raw internal map Z maps to P^R_n dot_R (Z dot_R Q^R_n) and Z maps to (P^R_n dot_R Z) dot_R Q^R_n. Twice applying lem-compcb-rectangular-product to elements of the amplified R-corner replaces the two dot_R products by the correspondingly parenthesized ambient A-products with O(t)||X|| error. Bilinearity, the product-norm bound, node 1.1's ||P^R_n-P_n||,||Q^R_n-Q_n||=O(t), and ||Z-X||=O(t)||X|| then give ||F_n(Z)-P_n(XQ_n)||<=K_tel*t||X||. Finally X=Co^A_{P_n,Q_n}X by the amplified range/idempotence identities, and def-compressed-corner gives ||P_n(XQ_n)-Co^A_{P_n,Q_n}X||<=2*K_def*t||X||. Hence ||F_n(Z)-X||<=C_fwd*t||X||, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Validated inputs and the missing Z estimate: by validated nodes 1.1.1 and 1.1.2, for every n one has ||P_n||,||Q_n||<=2 and ||P^R_n-P_n||,||Q^R_n-Q_n||<=K_P*t; hence ||P^R_n||,||Q^R_n||<=2+K_P*t. By validated nodes 1.2.1 and 1.2.2, A_R is an extended 2*C_ca*t-C*-algebra and P^R,Q^R are C_proj*t-projections in it. Independently of pending sibling 1.3.1, apply lem-compcb-amplified-almost-containment in A with (P_1,P,Q_1,Q)=(P,R,Q,R): the hypotheses ||PR-P||,||QR-Q||<=t are among the assumed subordination errors, so when 2t<=e_ac, Z=Co^A_{R_n}(X) satisfies ||Z-X||<=2*C_ac*t||X|| and therefore ||Z||<=(1+2*C_ac*t)||X||. Lem-compcb-amplified-compression identifies Z as an element of M_n tensor A_R. These are dimension-free estimates and use only validated nodes plus an allowed external.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Use only the preceding validated-input package and the allowed externals. Write d=C_proj and alpha=2*C_ca. In the extended alpha*t-C*-algebra A_R, def-compressed-corner at level n (with lem-compcb-amplified-compression for the amplification) gives ||F_n(Z)-P^R_n dot_R (Z dot_R Q^R_n)||<=K_def*(d+alpha)*t*||Z|| once (d+alpha)t is below its universal threshold. Put W=Z dot_R Q^R_n. Applying lem-compcb-rectangular-product in the original amplified R-corner first to (Z,Q^R_n) and then to (P^R_n,W) gives ||W-ZQ^R_n||<=2*C_co*t||Z||||Q^R_n|| and ||P^R_n dot_R W-P^R_n W||<=2*C_co*t||P^R_n||||W||. The product-norm axiom also gives ||P^R_n W-P^R_n(ZQ^R_n)||<=(1+t)||P^R_n||||W-ZQ^R_n||, while the A_R product-norm bound gives ||W||<=(1+alpha*t)||Z||||Q^R_n||. The bounds in the preceding child therefore yield ||F_n(Z)-P^R_n(ZQ^R_n)||<=K_dot*t||X|| with universal K_dot. Exact bilinearity, with the displayed parenthesization fixed, gives P^R_n(ZQ^R_n)-P_n(XQ_n)=(P^R_n-P_n)(ZQ^R_n)+P_n((Z-X)Q^R_n)+P_n(X(Q^R_n-Q_n)); two uses of ||UV||<=(1+t)||U||||V|| and the preceding bounds give norm at most K_pert*t||X||. Finally X lies in M_n tensor S^A_{P,Q}=S^A_{P_n,Q_n}; lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities imply Co^A_{P_n,Q_n}(X)=X. The ambient def-compressed-corner comparison gives ||P_n(XQ_n)-X||<=2*K_def*t||X||. Hence ||F_n(Z)-X||<=(K_dot+K_pert+2*K_def)t||X||, uniformly in n, after taking the universal threshold minimum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For every n and Y in M_n tensor S^{A_R}_{P^R,Q^R}, the exact range identity Y=F^R_{P,Q}(Y), followed by the same fixed internal-product telescope in reverse and the ambient compression-to-raw-product estimate, gives ||Co^A_{P,Q}(Y)-Y|| <= C_rev*t*||Y|| with a universal coefficient independent of n. Taking C_nest=max(C_proj,C_fwd,C_rev) and e_nest no larger than all thresholds proves node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Fix n and Y in M_n tensor S^{A_R}_{P^R,Q^R}. By lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities inside A_R, this space is the range of the idempotent F_n=Co^{A_R}_{P^R_n,Q^R_n}, so F_n(Y)=Y. The def-compressed-corner comparison in A_R therefore gives ||Y-P^R_n dot_R (Y dot_R Q^R_n)||<=K_def*(C_proj+2*C_ca)t||Y|| (and likewise for the other association), after the universal threshold is imposed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** Set a=P^R=Co^A_R(P), b=Q^R=Co^A_R(Q), and let K_def,e_def witness the universal def-compressed-corner bound ||Co_{U,V}-L_U R_V||,||Co_{U,V}-R_V L_U|| <= K_def*(delta+epsilon). This branch derives its own projection parameter. For t<=1/4, the epsilon-C*-lower and product-norm axioms give ||R||,||P||,||Q||<=2. Subordination gives ||R(PR)-P||<=||R(PR-P)||+||RP-P||<=4t, and similarly for the other raw association and for Q. Hence the compression comparison for the t-projection R in the ambient t-C*-algebra gives ||a-P||,||b-Q||<=K_P*t with K_P=4*K_def+4. Shrink t so K_P*t<=1 and 2*K_def*t<=1. The same comparison with the raw map X↦R(XR) then gives a universal operator bound ||Co_R||<=8. The external lem-compcb-corner-algebra makes A_R an extended 2*C_ca*t-C*-algebra. The amplified adjoint compression identity at n=1 makes a,b Hermitian. Moreover, with K_0=8*K_P+1, bilinearity and the product-norm axiom give ||a^2-a||<=K_0*t and ||b^2-b||<=K_0*t; since Co_R(a)=a and Co_R(b)=b, one has ||a dot_R a-a||=||Co_R(a^2-a)||<=8*K_0*t and likewise for b. Thus, with C_proj=8*K_0, a,b are C_proj*t-projections in A_R, derived here without node 1.2. At level n, a_n=I_n tensor a and b_n=I_n tensor b have the same defects because the extended product is amplified entrywise and the operator-space block-diagonal axiom gives ||I_n tensor T||=||T||. Impose also (C_proj+2*C_ca)*t<=min(e_def,e_cmp). Then lem-compcb-amplified-compression identifies M_n tensor S^{A_R}_{a,b} with S^{A_R}_{a_n,b_n}, and lem-compcb-amplified-compression-identities makes F_n=Co^{A_R}_{a_n,b_n} idempotent. Therefore Y in that space satisfies F_n(Y)=Y, while def-compressed-corner inside A_R yields ||Y-a_n dot_R (Y dot_R b_n)||<=K_def*(C_proj+2*C_ca)*t*||Y|| and the analogous bound for (a_n dot_R Y) dot_R b_n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** All factors in the preceding internal products lie in M_n tensor A_R=M_n tensor S_R. Two applications of lem-compcb-rectangular-product with the compatible R_n-corners replace dot_R by the ambient A product with O(t)||Y|| error. Node 1.1 then replaces P^R_n,Q^R_n by P_n,Q_n, giving ||Y-P_n(YQ_n)||<=K'_tel*t||Y||. In the original ambient algebra, def-compressed-corner gives ||Co^A_{P_n,Q_n}(Y)-P_n(YQ_n)||<=2*K_def*t||Y||; hence ||Co^A_{P,Q}Y-Y||<=C_rev*t||Y|| under the amplified identification, uniformly in n. The constants are universal and taking the stated maximum and threshold minimum completes node 1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.1

**Statement:** Write a=P^R=Co_R(P), b=Q^R=Co_R(Q), and a_n=I_n tensor a, b_n=I_n tensor b. This step derives, without using nodes 1.1, 1.2, or 1.4.1, universal K_pert,K_raw and a universal positive threshold such that for every n and Y in M_n tensor S^{A_R}_{a,b}, ||a_n-P_n||+||b_n-Q_n||<=K_pert*t and ||Y-a_n dot_R (Y dot_R b_n)||<=K_raw*t*||Y||. Indeed, for t<=1/4, the C*-lower bound and t-projection defect give (1-t)||T||^2<=||T^2||<=||T||+t, hence ||R||,||P||,||Q||<=2. If K_def witnesses the compression-to-raw-map estimate in def-compressed-corner, then ||R(PR)-P||<=||R(PR-P)||+||RP-P||<=2(1+t)t+t and ||Co_R(P)-R(PR)||<=2*K_def*t||P||; thus ||a-P||<=K_0*t, and identically ||b-Q||<=K_0*t. The block-diagonal operator-space axiom gives the same estimates for a_n-P_n and b_n-Q_n. By lem-compcb-corner-algebra, A_R is an extended 2*C_ca*t-C*-algebra. By lem-compcb-amplified-compression-identities, a and b are Hermitian. Also Co_R has universally bounded operator norm because it is within 2*K_def*t of X maps to R(XR), while ||R||<=2. Bilinearity and the product-norm axiom give ||a^2-a||<= (1+t)||a-P||(||a||+||P||)+||P^2-P||+||P-a||<=K_1*t. Since Co_R(a)=a by idempotence, ||a dot_R a-a||=||Co_R(a^2-a)||<=K_2*t; the same holds for b. Hence a,b are K_2*t-projections in A_R. After shrinking t so (K_2+2*C_ca)t meets the amplified compression thresholds, lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities identify M_n tensor S^{A_R}_{a,b} with the range of the idempotent F_n=Co^{A_R}_{a_n,b_n}; therefore F_n(Y)=Y. Applying the compression-to-first-raw-map estimate in the extended algebra A_R gives ||Y-a_n dot_R(Y dot_R b_n)||<=K_def*(K_2+2*C_ca)*t||Y||. All displayed constants are universal and independent of n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.2

**Statement:** Use the two estimates just established to complete the reverse telescope, with no appeal to nodes 1.1 or 1.4.1. Both a_n,b_n,Y and Y dot_R b_n lie in compatible amplified R_n-corners. Lem-compcb-rectangular-product, applied first to (Y,b_n) and then to (a_n,Y dot_R b_n), gives ||Y dot_R b_n-Yb_n||<=2*C_co*t||Y||||b_n|| and ||a_n dot_R(Y dot_R b_n)-a_n(Y dot_R b_n)||<=2*C_co*t||a_n||||Y dot_R b_n||. The preceding perturbation bounds and ||P_n||,||Q_n||<=2 make ||a_n||,||b_n|| universal; the first displayed estimate then also makes ||Y dot_R b_n||<=B||Y|| universally. Consequently ||a_n dot_R(Y dot_R b_n)-a_n(Yb_n)||<=K_3*t||Y||. Exact bilinearity yields a_n(Yb_n)-P_n(YQ_n)=(a_n-P_n)(Yb_n)+P_n(Y(b_n-Q_n)), so the product-norm axiom and the perturbation bounds give ||a_n(Yb_n)-P_n(YQ_n)||<=K_4*t||Y||. Combining with ||Y-a_n dot_R(Y dot_R b_n)||<=K_raw*t||Y|| gives ||Y-P_n(YQ_n)||<=(K_raw+K_3+K_4)t||Y||. Finally def-compressed-corner in M_n tensor A gives ||Co^A_{P_n,Q_n}(Y)-P_n(YQ_n)||<=2*K_def*t||Y||. By lem-compcb-amplified-compression, Co^A_{P_n,Q_n}=I_n tensor Co^A_{P,Q}; hence ||Co^A_{P,Q}(Y)-Y||<=C_rev*t||Y|| at every amplification, where C_rev=K_raw+K_3+K_4+2*K_def is universal. Taking the threshold minimum and the maximum with the other universal coefficients is exactly the conclusion of nodes 1.4.2 and 1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

