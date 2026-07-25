# Proof Export

## Node 1

**Statement:** Diagonal Ha lower-modulus propagation: there are universal C_diag < infinity and e_diag > 0 such that, for every H-CB datum with e <= e_diag, if the level-one lower modulus of Ha^Q_{P,P} is at least 1/4, then ||(Ha^Q_{P,P})_n(Z)|| >= (1-C_diag*e)||Z|| for every n >= 1 and Z in M_n tensor S_P.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Quantitative setup: fix universal witnesses C_prod,e_prod from lem-hcb2-product-defect and K_sq,e_sq from lem-hcb3-uniform-square-lower, put C_diag:=K_sq+4*C_prod, and choose a universal e_diag>0 no larger than e_prod,e_sq,e_adj (from lem-hcb2-amplified-adjointness) and so small that, for 0<=e<=e_diag, A:=1-K_sq*e and B:=C_prod*e obey A>=3/4, A^2-4B>=0, 4B<1/8, and C_diag*e<=1/2. For r_-(e):=(A-sqrt(A^2-4B))/2 and r_+(e):=(A+sqrt(A^2-4B))/2, one has 0<=r_-<=4*C_prod*e<1/8 and r_+>=1-C_diag*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** The constants supplied by the three cited externals are universal and finite, so such a positive e_diag exists (also take it below any harmless threshold needed when a listed constant is zero). Rationalizing the smaller root gives r_-=2B/(A+sqrt(A^2-4B))<=2B/A<=8B/3<=4B. Since r_-+r_+=A, it follows that r_+=A-r_->=1-(K_sq+4*C_prod)e=1-C_diag*e. The imposed inequalities also give r_-<1/8 and r_+>=1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** Normalize the product-defect witness before introducing any later constants: if C_prod^0 and e_prod are witnesses supplied by lem-hcb2-product-defect, set C_prod:=max{C_prod^0,0}. Because e>=0 and ||Z||||W||>=0, C_prod^0*e*||Z||||W||<=C_prod*e*||Z||||W||, so the same defect estimate holds with C_prod; it is universal, finite, and nonnegative. Relabel this normalized witness as C_prod everywhere in node 1.1, including B:=C_prod*e and C_diag:=K_sq+4*C_prod. Hence B>=0. The other smallness requirements can be imposed simultaneously: A(0)=1 and A(e)^2-4C_prod*e is continuous with value 1 at e=0; A>=3/4 holds on a positive interval (automatically if K_sq<=0); 4C_prod*e<1/8 holds automatically if C_prod=0 and on a positive interval otherwise; and C_diag*e<=1/2 holds automatically if C_diag<=0 and on a positive interval otherwise. Intersecting these intervals with (0,e_prod], (0,e_sq], and (0,e_adj] gives a positive universal e_diag.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.2

**Statement:** For 0<=e<=e_diag, A>=3/4>0, B>=0, and A^2-4B>=0. Thus 0<=sqrt(A^2-4B)<=A and A+sqrt(A^2-4B)>0. Rationalization is therefore valid, including B=0, and gives r_-=2B/(A+sqrt(A^2-4B)). Since B>=0 and the denominator is at least A, 0<=r_-<=2B/A<=8B/3<=4B<1/8. Finally r_+=A-r_->=1-K_sq*e-4C_prod*e=1-C_diag*e>=1/2. This proves all root bounds in node 1.1 with the normalized C_prod.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Lower-modulus dichotomy on the nonzero-corner branch: assume S_P!={0}. Then for every n>=1 the set R_n:={||(Ha^Q_{P,P})_n(Z)||/||Z||:0!=Z in M_n tensor S_P} is nonempty and has a finite nonnegative infimum a_n; this a_n satisfies a_n^2>=a_n*(1-K_sq*e)-C_prod*e and consequently a_n<=r_-(e) or a_n>=r_+(e). If S_P={0}, the root estimate is instead immediate as proved in node 1.2.2.2.1, and no a_n is defined.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Pointwise square estimate: write T_n=(Ha^Q_{P,P})_n. For every Z in M_n tensor S_P, lem-hcb2-amplified-adjointness and lem-hcb2-product-defect (applied with all three corner indices equal to P, and with the factors Z^dagger,Z) imply ||T_n(Z)||^2=||T_n(Z)^dagger*T_n(Z)||>=||T_n(Z^dagger dot Z)||-C_prod*e*||Z||^2. Here the first equality is the ordinary C*-identity in the bounded-operator target, amplified adjointness identifies T_n(Z)^dagger with T_n(Z^dagger), and the matrix involution is isometric.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** By the definition of a_n, ||T_n(X)||>=a_n||X|| for every X in M_n tensor S_P; applying this with X=Z^dagger dot Z and then citing lem-hcb3-uniform-square-lower yields ||T_n(Z)||^2 >= [a_n*(1-K_sq*e)-C_prod*e]||Z||^2. Taking the infimum over nonzero Z gives a_n^2>=A*a_n-B. Since A^2-4B>=0, the quadratic x^2-Ax+B is nonnegative at x=a_n>=0, so a_n lies outside the open interval between its roots: a_n<=r_- or a_n>=r_+.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** For every Z in M_n tensor S_P, validated node 1.2.1 supplies the missing bridge ||T_n(Z)||^2 >= ||T_n(Z^dagger dot Z)||-C_prod*e*||Z||^2: it follows from amplified adjointness T_n(Z^dagger)=T_n(Z)^dagger, the product-defect estimate for the factors Z^dagger,Z with all corner indices P, and the ordinary C*-identity in the bounded-operator target.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Split first according to whether S_P is zero. If S_P={0}, then M_m tensor S_P={0} for every m and the root lower estimate is immediate, without defining any a_m. In the remaining branch S_P!={0}; then for every n the ratio set defining a_n is nonempty and bounded below, and a_n is a finite nonnegative real. In this branch the definition of a_n, lem-hcb3-uniform-square-lower, and node 1.2.2.1 give ||T_n(Z)||^2 >= [a_n(1-K_sq*e)-C_prod*e]||Z||^2 for every Z.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.2.1

**Statement:** Case S_P={0}: for every m>=1, M_m tensor S_P={0}. Thus every Z in M_m tensor S_P is zero; linearity of the amplified Ha-map gives T_m(Z)=T_m(0)=0, while (1-C_diag*e)||Z||=0. Hence the root estimate holds at every level and this case is complete without introducing a_m or an infimum over an empty set.

**Type:** case

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.2.2

**Statement:** Case S_P!={0}: choose 0!=x in S_P. For each n>=1 the element E_11 tensor x in M_n tensor S_P is nonzero (indeed the operator-space direct-sum axiom gives ||diag(x,0,...,0)||=||x||>0). Therefore R_n:={||T_n(X)||/||X||:0!=X in M_n tensor S_P} is nonempty. Every member of R_n is a finite nonnegative real, so 0<=a_n:=inf R_n<=||T_n(E_11 tensor x)||/||E_11 tensor x||<infinity; in particular a_n is a finite nonnegative real. For nonzero X, the defining property of the infimum gives ||T_n(X)||>=a_n||X||, and for X=0 the same inequality is 0>=0 by linearity. Apply it to X=Z^dagger dot Z. Since a_n>=0, lem-hcb3-uniform-square-lower may be multiplied by a_n, giving ||T_n(Z^dagger dot Z)||>=a_n||Z^dagger dot Z||>=a_n(1-K_sq*e)||Z||^2. Substitution in node 1.2.2.1 yields ||T_n(Z)||^2>=[a_n(1-K_sq*e)-C_prod*e]||Z||^2 for every Z, with no extended-real product.

**Type:** case

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.3

**Statement:** Put V_n:=M_n tensor S_P. If V_n={0}, then the desired level-n estimate is immediate: its only vector is Z=0 and the linear amplification T_n satisfies T_n(0)=0, so no lower modulus or dichotomy is invoked. Assume henceforth V_n is nonzero. Then R_n:={||T_n(Z)||/||Z||:0!=Z in V_n} is a nonempty set of finite nonnegative reals, so a_n:=inf R_n is a finite nonnegative real. For every nonzero Z, division by ||Z||^2 in node 1.2.2.2 gives (||T_n(Z)||/||Z||)^2 >= A*a_n-B. Moreover inf{r^2:r in R_n}=(inf R_n)^2=a_n^2. Taking infima therefore gives a_n^2>=A*a_n-B. Hence (a_n-r_-)(a_n-r_+)>=0; since r_-<=r_+, this is equivalent to a_n<=r_- or a_n>=r_+.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.3.1

**Statement:** Case V_n={0}: every Z in V_n equals 0. Since T_n is the linear amplification of the Ha-map, T_n(0)=0, and therefore ||T_n(Z)||=0>=(1-C_diag*e)||Z||=0. Thus the root contract at this fixed level n is already proved, and neither a_n nor any infimum over nonzero vectors is formed in this case.

**Type:** case

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.3.2

**Statement:** Case V_n is nonzero: choose Z_0!=0 in V_n. Then R_n is nonempty, every member ||T_n(Z)||/||Z|| is a finite nonnegative real, and R_n is bounded below by 0. Consequently a_n=inf R_n exists as a finite real: it is at least 0 and at most the finite ratio belonging to Z_0.

**Type:** case

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.3.3

**Statement:** For any nonempty R subset [0,infinity) with finite a=inf R, one has inf{r^2:r in R}=a^2. Indeed r>=a gives r^2>=a^2. Conversely, for every eta>0 put d=sqrt(a^2+eta)-a>0; the definition of infimum provides r in R with r<a+d=sqrt(a^2+eta), so r^2<a^2+eta. Applying this to R_n justifies taking the infimum of the squared ratios and yields a_n^2>=A*a_n-B. The root definitions give x^2-Ax+B=(x-r_-)(x-r_+) and r_-<=r_+; hence nonnegativity at x=a_n places a_n outside (r_-,r_+), i.e. a_n<=r_- or a_n>=r_+.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Amplification propagation and conclusion: Ruan block estimates give a_{2n}>=a_n/2, standard zero-corner inclusions give a_n>=a_m whenever n<=m, and the assumed a_1>=1/4 together with the dichotomy propagates a_{2^k}>=r_+(e) for every k; hence a_n>=r_+(e)>=1-C_diag*e for every n, which is the asserted estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Ruan block estimate: for Z in M_{2n} tensor S_P written as a 2-by-2 matrix (Z_ij) of n-by-n blocks, the operator-space matrix axioms give ||Z||<=2*max_{i,j}||Z_ij|| (factor Z=A*diag(Z_11,Z_12,Z_21,Z_22)*B with scalar A,B of norms sqrt(2)). Since T_{2n} is the entrywise amplification of T_n, compression to its (i,j) target block gives ||T_{2n}(Z)||>=max_{i,j}||T_n(Z_ij)||. Hence ||T_{2n}(Z)||>=a_n*max||Z_ij||>=a_n||Z||/2 and therefore a_{2n}>=a_n/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Explicitly, with n-by-n scalar identity blocks, take A=[[I,I,0,0],[0,0,I,I]] and B=[[I,0],[0,I],[I,0],[0,I]]. Then A*diag(Z_11,Z_12,Z_21,Z_22)*B=Z and ||A||=||B||=sqrt(2). Ruan ax_R1 and ax_R2 therefore give ||Z||<=2*max||Z_ij||. For each i,j, scalar coordinate projections and inclusions have norm one, so ax_R1 applied in the bounded-operator target gives ||T_n(Z_ij)||<=||T_{2n}(Z)||. These are exactly the two estimates used in node 1.3.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Monotonicity: if m=n+k, the standard zero-corner inclusion Z mapsto diag(Z,0_k) is isometric by the Ruan direct-sum axiom, and its image under T_m is diag(T_n(Z),0_k), also of the same norm. Thus a_m<=a_n, equivalently a_n>=a_m whenever n<=m.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Branchwise base and dyadic bootstrap: if S_P={0}, then the root estimate holds at every matrix level without defining any a_m. If S_P!={0}, then node 1.3.3.1 gives a_1>=r_+(e), and ordinary induction using node 1.3.3.2, as recorded in node 1.3.3.3, gives a_{2^k}>=r_+(e) for every integer k>=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.1

**Statement:** Base reduction without an empty infimum: either S_P={0}, in which case the root estimate holds at every matrix level without defining any a_m, or S_P!={0}, in which case a_1 is a finite nonnegative real and the root lower-modulus hypothesis together with nodes 1.1 and 1.2 implies a_1>=r_+(e).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.1.1

**Statement:** Split exhaustively into S_P={0} and S_P!={0}. If S_P={0}, validated node 1.2.2.2.1 proves directly that M_m tensor S_P={0} and ||T_m(Z)||>=(1-C_diag*e)||Z|| for every m and Z, so no a_m is formed. If S_P!={0}, validated node 1.2.2.2.2 proves that at n=1 the ratio set R_1 is nonempty and a_1=inf R_1 is a finite nonnegative real. The level-one lower-modulus hypothesis gives a_1>=1/4, while validated node 1.1 gives r_-(e)<1/8, hence a_1>r_-(e). Validated node 1.2, specialized to n=1 in this nonzero-corner branch, gives a_1<=r_-(e) or a_1>=r_+(e); the first alternative is impossible, so a_1>=r_+(e). Thus every declared dependency is validated and used, and both branches are discharged.

**Type:** case

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.1.1.1

**Statement:** In the branch S_P!={0}, put V_1=M_1 tensor S_P=S_P. Validated node 1.2.2.2.2 shows that the ratio set R_1 is nonempty and that a_1=inf R_1 is a finite nonnegative real. Since V_1!={0}, validated node 1.2.2.3, specialized to n=1, gives the dichotomy a_1<=r_-(e) or a_1>=r_+(e). The root hypothesis gives a_1>=1/4, while validated node 1.1 gives r_-(e)<1/8; hence a_1>r_-(e), the first alternative is impossible, and a_1>=r_+(e). This derives the required nonzero-corner base case directly from validated nodes and does not invoke pending node 1.2.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.3.3.2

**Statement:** Induction step, with dependencies explicit: suppose a_{2^k}>=r_+(e). Node 1.3.1, applied with n=2^k, gives a_{2^{k+1}}>=a_{2^k}/2. Node 1.1 gives r_+(e)>=1-C_diag*e and C_diag*e<=1/2, hence a_{2^{k+1}}>=r_+(e)/2>=(1-C_diag*e)/2>=1/4>r_-(e), the final strict inequality again being node 1.1. Applying node 1.2 at n=2^{k+1}, its alternative a_{2^{k+1}}<=r_-(e) is impossible, so a_{2^{k+1}}>=r_+(e).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.3

**Statement:** In the branch S_P!={0}, ordinary induction on k, using the nonzero-corner base assertion from node 1.3.3.1 and the induction step from node 1.3.3.2, yields a_{2^k}>=r_+(e) for every integer k>=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.3.1

**Statement:** Work throughout in the branch S_P!={0}. Validated node 1.2.2.2.2 defines every a_m (m>=1) as a finite nonnegative real, and validated node 1.3.3.1.1.1 supplies P(0): a_{2^0}=a_1>=r_+(e). For k>=0 let P(k) denote a_{2^k}>=r_+(e). Validated node 1.3.3.2 proves P(k)=>P(k+1). Therefore ordinary induction gives P(k) for every integer k>=0. No a_m is formed in the excluded branch S_P={0}, which validated node 1.2.2.2.1 discharges directly.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.3.1.1

**Statement:** In the branch S_P!={0}, validated node 1.2.2.2.2 applies for every integer m>=1, so each ratio set R_m is nonempty and a_m=inf R_m is a finite nonnegative real; hence P(k):=[a_{2^k}>=r_+(e)] is a well-formed proposition for every k>=0. Validated node 1.3.3.1.1.1 gives P(0), and validated node 1.3.3.2 gives P(k)=>P(k+1) for each k>=0. The induction axiom on the nonnegative integers therefore yields P(k) for all k>=0. This argument never defines a_m in the branch S_P={0}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** For arbitrary n choose a power of two m>=n. Node 1.3.2 gives a_n>=a_m, while node 1.3.3 gives a_m>=r_+ and node 1.1 gives r_+>=1-C_diag*e. Hence ||T_n(Z)||>=a_n||Z||>=(1-C_diag*e)||Z|| for every Z. The constants are universal and e_diag is positive, proving the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

