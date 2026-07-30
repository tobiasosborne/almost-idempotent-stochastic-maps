# Proof Export

## Node 1

**Statement:** There are universal C_out < infinity and e_out > 0 such that, whenever R,P are t-projections in a finite-dimensional extended t-C*-algebra, R is nonvanishing, both subordination errors of P to R are at most t, v:B->S^A_P is an extended t-isomorphism, A_R = S^A_R, P^R = Co^A_R(P), and t <= e_out, the explicitly defined map T = Co^{A_R}_{P^R} o Co^A_R o v : B->S^{A_R}_{P^R} is an extended C_out*t-isomorphism and T_n = I_n tensor T for every n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Nested-corner geometry and target algebra ledger. There are universal constants C_nest,C_ca and a positive universal threshold such that, with a=P^R=Co^A_R(P), the maps W_n=Co^{A_R}_{I_n tensor a} composed with Co^A_{I_n tensor R} carry M_n tensor S^A_P into M_n tensor S^{A_R}_a, satisfy ||W_n(X)-X||<=C_nest*t*||X||, and dim S^A_P=dim S^{A_R}_a. Moreover S^A_P, A_R, and S^{A_R}_a have their compressed extended approximate C*-algebra structures with defects bounded by universal multiples of t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Specialize the validated externals lem-maincb-nested-corner-comparison and lem-maincb-nested-corner-dimension-transport to Q=P. The two left/right subordination assumptions then supply all four repeated hypotheses. Thus a=Co^A_R(P) is a C_nest*t-projection in A_R; for every n the forward comparison W_n=Co^{A_R}_{I_n tensor a} composed with Co^A_{I_n tensor R} maps M_n tensor S^A_P to M_n tensor S^{A_R}_a and satisfies ||W_n(X)-X||<=C_nest*t*||X||; and dim S^A_P=dim S^{A_R}_a. These conclusions use the two externals by their exact registered names and no re-proof of them.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Nonvanishing and corner-algebra check. A t-projection in an extended t-C*-algebra has norm at most 2 for a universal small threshold, since (1-t)||H||^2<=||H^2||<=||H||+t. If P were in the vanishing alternative of def-delta-projection, then ||P||=O(t), and the two operator comparisons in def-compressed-corner would make the idempotent Co^A_P have operator norm O(t)<1; lem-compcb-amplified-compression-identities then forces Co^A_P=0. This contradicts S^A_P!=0, because the bijection v has nonzero unital source B. Hence P is nonvanishing. Applying lem-compcb-corner-algebra to P and to the given nonvanishing R makes S^A_P and A_R=S^A_R extended 2*C_ca*t-C*-algebras. The dimension equality in node 1.1.1 gives S^{A_R}_a!=0. If the C_nest*t-projection a were vanishing in A_R, the identical compression-operator argument, now with total error (C_nest+2*C_ca)t and using lem-compcb-amplified-compression-identities inside A_R, would force Co^{A_R}_a=0, a contradiction. Thus a is nonvanishing, and a second application of lem-compcb-corner-algebra makes S^{A_R}_a an extended C_ca*(C_nest+2*C_ca)*t-C*-algebra. All thresholds are positive universal finite minima.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Exact amplified formula, range, and involution. Put R_n=I_n tensor R and a_n=I_n tensor a. Tensor functoriality for linear maps and lem-compcb-amplified-compression applied first in A and then in A_R give I_n tensor T=Co^{A_R}_{a_n} composed with Co^A_{R_n} composed with v_n=W_n composed with v_n. The same external identifies M_n tensor S^A_P and M_n tensor S^{A_R}_a with the corresponding amplified compression ranges, so the displayed map is linear and has the asserted target. The extended t-isomorphism v preserves dagger exactly at every level. Applying lem-compcb-amplified-compression-identities to the square pairs (R_n,R_n) in A and (a_n,a_n) in A_R shows successively that both compressions preserve dagger. Hence T_n(x^dagger)=T_n(x)^dagger for every n and x.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Uniform near-isometry. By the exact formula in node 1.2 and the forward estimate of lem-maincb-nested-corner-comparison specialized as in node 1.1.1, ||T_n(x)-v_n(x)||=||W_n(v_n(x))-v_n(x)||<=C_nest*t*||v_n(x)||. Def-extended-delta-inclusion gives ||v_n(x)||<=(1+t)||x||, so for t<=1 this is at most 2*C_nest*t*||x||. Combining this with (1-t)||x||<=||v_n(x)||<=(1+t)||x|| by the triangle and reverse-triangle inequalities gives (1-K_N*t)||x||<=||T_n(x)||<=(1+K_N*t)||x|| with K_N=1+2*C_nest, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Uniform homomorphism clauses. There are universal K_M,K_U such that, at every amplification, T_n has multiplicative defect at most K_M*t and unit defect at most K_U*t; together with node 1.2 it is dagger preserving and linear.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Multiplicative telescope, conditional on nodes 1.1 and 1.3. Fix n and x,y in M_n tensor B; put b=v_n(x), c=v_n(y), beta=T_n(x), gamma=T_n(y), and distinguish the original product of A by juxtaposition from the compressed R-product dot_R, which is the ambient product of A_R. The extended t-isomorphism clause gives ||v_n(xy)-b dot_P c||<=t||x||||y||. Lem-compcb-rectangular-product in A gives ||b dot_P c-bc||<=2*C_co*t||b||||c||. The ambient product bound and ||b||,||c||<=(1+t) times the source norms give a universal bound ||v_n(xy)||<=K_B||x||||y||, hence node 1.1.1 gives ||T_n(xy)-v_n(xy)||<=C_nest*K_B*t||x||||y||. Bilinearity of the original A-product gives bc-beta gamma=(b-beta)c+beta(c-gamma); the ambient product bound, node 1.3, and the uniform norm bounds control this by K_pert*t||x||||y|| without associativity. Since beta,gamma lie in M_n tensor S_a^{A_R} and A_R=S_R^A, lem-compcb-amplified-compression identifies them with elements of the amplified R,R-corner in A. A separate application of lem-compcb-rectangular-product in A therefore gives ||beta gamma-beta dot_R gamma||<=2*C_co*t||beta||||gamma||. In A_R, whose ambient product is dot_R and whose defect is at most 2*C_ca*t, a is a C_nest*t-projection by node 1.1.1; hence lem-compcb-rectangular-product applied inside A_R gives ||beta dot_R gamma-beta dot_a gamma||<=C_co*(C_nest+2*C_ca)*t||beta||||gamma||. Lem-compcb-amplified-compression identifies all amplified compressed products used here. Summing the six successive differences T_n(xy)-v_n(xy), v_n(xy)-b dot_P c, b dot_P c-bc, bc-beta gamma, beta gamma-beta dot_R gamma, and beta dot_R gamma-beta dot_a gamma gives ||T_n(xy)-T_n(x) dot_a T_n(y)||<=K_M*t||x||||y|| for a universal K_M independent of n and all dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** Missing product bridge. At amplification n, beta,gamma are in M_n tensor S_a^{A_R} by node 1.2. Because A_R=S_R^A, lem-compcb-amplified-compression identifies this space as a subspace of the amplified R,R-corner S^A_{R_n,R_n}, where R_n=I_n tensor R. Apply lem-compcb-rectangular-product in A to the compatible R_n,R_n factors: since R is a t-projection and A is an extended t-C*-algebra, its total error is 2*t, so ||beta gamma-beta dot_R gamma||<=2*C_co*t||beta||||gamma||. Here dot_R=Co^A_{R_n,R_n}(beta gamma) is also exactly the ambient multiplication of M_n tensor A_R: the corner-algebra structure uses the compressed R-product, and tensor linearity together with lem-compcb-amplified-compression identifies its amplification with Co^A_{R_n,R_n}. Separately, inside A_R, node 1.1 gives algebra defect 2*C_ca*t and projection defect C_nest*t for a; the same external then yields ||beta dot_R gamma-beta dot_a gamma||<=C_co*(C_nest+2*C_ca)*t||beta||||gamma||. Thus ||beta gamma-beta dot_a gamma|| is bounded by C_co*(2+C_nest+2*C_ca)*t||beta||||gamma||, supplying exactly the omitted intermediate term.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Unit telescope, conditional on nodes 1.1 and 1.3. Let u_P=Co^A_P(P) and u_a=Co^{A_R}_a(a) be the compressed units. The t-homomorphism unit clause gives ||v_n(1)-I_n tensor u_P||<=t. On M_n tensor S^A_P, node 1.1.1 gives ||W_n||<=1+C_nest*t, so the contribution of this unit error to ||T_n(1)-I_n tensor u_a|| is at most (1+C_nest*t)t. It remains to compare W_n(I_n tensor u_P) with I_n tensor u_a. The t-projection estimate ||P||<=2, the compression-to-raw-map bound in def-compressed-corner, and ||P^2-P||<=t give ||u_P-P||<=K_0*t: for example use the raw association (P^2)P and the exact bilinear identity (P^2)P-P=(P^2-P)P+(P^2-P). The same compression comparison bounds Co_R and Co^{A_R}_a uniformly because ||R||,||a||<=2. Since a=Co_R(P) and u_a=Co^{A_R}_a(a), exact linearity gives W_1(u_P)-u_a=Co^{A_R}_a Co_R(u_P-P), and lem-compcb-amplified-compression tensors this identity to every n. Hence ||W_n(I_n tensor u_P)-I_n tensor u_a||<=K_1*t. Thus the unit defect is at most K_U*t for universal K_U. Together with node 1.2, the two children establish every homomorphism clause claimed by node 1.4.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Bijectivity. Node 1.1.1 makes W_1 a linear map S^A_P->S^{A_R}_a with ||W_1(X)-X||<=C_nest*t||X||. If C_nest*t<1 and W_1(X)=0, then ||X||<=C_nest*t||X||, hence X=0, so W_1 is injective. Lem-maincb-nested-corner-dimension-transport, specialized to Q=P as in node 1.1.1, gives equality of the finite dimensions of its domain and codomain; therefore W_1 is surjective and hence bijective. Since v:B->S^A_P is bijective by the assumed extended t-isomorphism, T=W_1 composed with v is bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Final assembly. After nodes 1.1--1.5 are validated, choose one positive universal e_out below all comparison, compression, corner-algebra, rectangular-product, nonvanishing, and Neumann-free dimension thresholds used there, and choose C_out=max{1,C_ca*(C_nest+2*C_ca),K_N,K_M,K_U}. Then every T_n is a C_out*t-inclusion, T is bijective, and the exact formula T_n=I_n tensor T holds, proving node 1.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

