# Proof Export

## Node 1

**Statement:** There are universal C_corner_unit < infinity and e_corner_unit > 0 such that both of the following hold: if P is a t-projection in a finite-dimensional extended t-C*-algebra A with 0 <= t <= e_corner_unit, then the compressed-corner unit u_{S_P}=Co_P(P) satisfies ||I_n tensor u_{S_P}-I_n tensor P|| <= C_corner_unit*t for every n >= 1; and, under the hypotheses of lem-maincb-outer-compression-transfer with 0 <= t <= e_corner_unit, if ||v(I_B)-u_{S_P}|| <= t then its explicit outer-compressed map T=Co^{A_R}_{P^R} o Co^A_R o v satisfies ||T_n(I_n tensor I_B)-I_n tensor P^R|| <= C_corner_unit*t for every n >= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform constants and norm bounds. There are universal M,K_cmp<infinity and e_0>0 such that whenever e=delta+epsilon<=e_0 and S is a delta-projection in any matrix level of an extended epsilon-C*-algebra, ||S||<=M, the compression comparison in def-compressed-corner may be written ||Co_{S,S}-L_S R_S||<=K_cmp*e, and ||Co_{S,S}||<=M^2*(1+epsilon)^2+K_cmp*e. Indeed the C*-lower bound and ||S^2-S||<=delta give (1-epsilon)||S||^2<=||S^2||<=||S||+delta, hence ||S||<=2 after shrinking e_0; the remaining bounds are the registered O(e) operator comparison and the product-norm axiom. All constants are independent of matrix size by def-extended-epsilon-cstar-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** General amplified compressed-unit comparison. Under node 1.1 there is a universal K_u<infinity such that, for e=delta+epsilon<=e_0, every delta-projection S in an extended epsilon-C*-algebra satisfies ||I_n tensor Co_S(S)-I_n tensor S||<=K_u*e for every n>=1. Put S_n=I_n tensor S. By def-operator-space, ||S_n||=||S|| and ||S_n^2-S_n||=||I_n tensor(S^2-S)||<=delta; by lem-compcb-amplified-compression, I_n tensor Co_S(S)=Co_{S_n}(S_n). The compression comparison gives ||Co_{S_n}(S_n)-S_n(S_n^2)||<=K_cmp*e*||S_n||. Bilinearity gives the exact identity S_n(S_n^2)-S_n=S_n(S_n^2-S_n)+(S_n^2-S_n), so the product-norm axiom bounds the latter norm by ((1+epsilon)M+1)delta. Thus one may take K_u=K_cmp*M+(1+e_0)*M+1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** First clause, derived independently of sibling nodes. Fix n>=1 and write P_n=I_n tensor P. The direct-sum norm axiom in def-operator-space gives ||P_n||=||P|| and ||P_n^2-P_n||=||I_n tensor(P^2-P)||<=t, while P_n is Hermitian; hence P_n is a t-projection in the t-C*-algebra M_n tensor A. Shrink t so t<=1/4. The C*-lower axiom and the defect bound give (1-t)||P_n||^2<=||P_n^2||<=||P_n||+t, which implies ||P_n||<=2. Unpack the registered O(delta+epsilon) compression comparison in def-compressed-corner as universal K_cmp<infinity and e_def>0 with ||Co_{S,S}-L_S R_S||<=K_cmp*(delta+epsilon) whenever delta+epsilon<=e_def. Also require 2t<=min(e_def,e_cmp), where e_cmp is the threshold in lem-compcb-amplified-compression. That external identity and u_{S_P}=Co_P(P) give I_n tensor u_{S_P}=Co_{P_n}(P_n). Therefore ||I_n tensor u_{S_P}-P_n||<=||Co_{P_n}(P_n)-P_n(P_n^2)||+||P_n(P_n^2)-P_n||. The first term is at most 2*K_cmp*t*||P_n||<=4*K_cmp*t. By bilinearity, P_n(P_n^2)-P_n=P_n(P_n^2-P_n)+(P_n^2-P_n), so the product-norm axiom bounds the second term by ((1+t)||P_n||+1)*t<=7*t/2. Thus ||I_n tensor u_{S_P}-I_n tensor P||<=(4*K_cmp+7/2)*t for every n>=1. The constants and threshold are universal and independent of n because the extended structure imposes the same t-C*-axioms at every matrix level.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Outer target scale. Under the hypotheses of lem-maincb-outer-compression-transfer, write a=P^R=Co_R^A(P) and A_R=S_R^A. There are universal K_R,K_a<infinity and e_R>0 such that A_R, with its registered compressed product, involution, and unit, is an extended K_R*t-C*-algebra and a is a K_a*t-projection in A_R whenever t<=e_R. For each matrix level, lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities identify M_n tensor A_R with the R_n-compression range, its product and dagger; def-compressed-corner supplies the O(2t) product/compression comparisons, while lem-compcb-compressed-unit-action and lem-compcb-compressed-unit-norm supply the uniform unit axioms and unit norm, so the extended algebra defect is K_R*t. The two subordination errors and the bounded compression from node 1.1 give ||a-P||<=K_1*t; the dagger identity makes a Hermitian, and Co_R(a)=a. Hence, writing dot_R for the product of A_R, a dot_R a-a=Co_R(a^2-a), and bilinearity, the ambient product bound, ||P^2-P||<=t, and the uniform bound on Co_R give ||a dot_R a-a||<=K_a*t. All constants are universal and amplification-independent.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Extended corner-algebra scale. Since R is a nonvanishing t-projection in an extended t-C*-algebra, def-compressed-corner gives S_R^A with compressed product X dot_R Y=Co_R^A(XY), inherited dagger, and unit u_R=Co_R^A(R) as an O(2t)-C*-algebra. For every n, lem-compcb-amplified-compression identifies M_n tensor S_R^A=S_{R_n}^A and identifies the amplified product and unit with compression by R_n; lem-compcb-amplified-compression-identities supplies exact idempotence and dagger compatibility. The operator-space direct-sum axiom gives ||R_n||=||R||, so nonvanishing passes to R_n, and lem-compcb-compressed-unit-action and lem-compcb-compressed-unit-norm give the unit-action and unit-norm bounds uniformly in n. Thus the O(2t) constants in the registered definition can be enlarged once to a universal K_R so that A_R=S_R^A is an extended K_R*t-C*-algebra, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Compressed target projection in the ambient norm. Put a=Co_R(P). Node 1.1 bounds ||R||,||P|| and ||Co_R|| universally. If the two subordination errors are ||RP-P||<=t and ||PR-P||<=t, then ||R(PR)-P||<=||R(PR-P)||+||RP-P||<=((1+t)||R||+1)t. The compression-to-raw-map estimate in def-compressed-corner therefore gives ||a-P||<=K_1*t for a universal K_1. Lem-compcb-amplified-compression-identities gives a^dagger=a because P^dagger=P, and its idempotence clause gives Co_R(a)=a. Consequently ||a|| is universally bounded.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** Projection defect in A_R. By bilinearity, a^2-P^2=(a-P)a+P(a-P), so the ambient product bound, node 1.4.2, and ||P^2-P||<=t give ||a^2-a||<=K_2*t. Since Co_R(a)=a and the A_R product is x dot_R y=Co_R(xy), exact linearity yields a dot_R a-a=Co_R(a^2-a). The uniform operator bound for Co_R from node 1.1 therefore gives ||a dot_R a-a||<=K_a*t for a universal K_a. Together with a^dagger=a, this makes a=P^R a K_a*t-projection in the extended K_R*t-C*-algebra A_R established in node 1.4.1, proving node 1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Target compressed-unit comparison. With a=P^R and A_R as in node 1.4, apply node 1.2 inside A_R with projection defect delta_R=K_a*t and ambient defect epsilon_R=K_R*t, after shrinking t so (K_a+K_R)t meets every threshold. Since lem-compcb-amplified-compression identifies the compressed unit at every level, there is a universal K_tar=K_u*(K_a+K_R) such that ||I_n tensor u_{S^{A_R}_{P^R}}-I_n tensor P^R||<=K_tar*t for every n>=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Dependency-scoped application. By validated node 1.2, for any delta-projection S in an extended epsilon-C*-algebra with delta+epsilon<=e_0, ||I_n tensor Co_S(S)-I_n tensor S||<=K_u*(delta+epsilon) for every n>=1. By node 1.4, under the outer-transfer hypotheses and t<=e_R, A_R is an extended K_R*t-C*-algebra and a=P^R is a K_a*t-projection in A_R, with universal K_R,K_a. Require node 1.4 to be validated and shrink t so (K_a+K_R)t<=e_0 and meets the amplified-compression threshold. Applying node 1.2 in A_R with S=a, delta=K_a*t, epsilon=K_R*t, and using u_{S^{A_R}_{P^R}}=Co^{A_R}_{P^R}(P^R), yields ||I_n tensor u_{S^{A_R}_{P^R}}-I_n tensor P^R||<=K_u*(K_a+K_R)*t for every n>=1. Thus K_tar=K_u*(K_a+K_R) is universal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Outer unit telescope and witness assembly. By lem-maincb-outer-compression-transfer, T is an extended C_out*t-isomorphism and T_n=I_n tensor T for every n. By def-extended-delta-inclusion and def-extended-epsilon-cstar-algebra, the unit clause of this extended homomorphism gives ||T_n(I_n tensor I_B)-I_n tensor u_{S^{A_R}_{P^R}}||<=C_out*t. The additional assumed bound ||v(I_B)-u_{S_P}||<=t is compatible with, but is not needed beyond, the hypotheses of this stronger conclusion. The triangle inequality and node 1.5 give ||T_n(I_n tensor I_B)-I_n tensor P^R||<=(C_out+K_tar)*t. Choose e_corner_unit as the positive minimum of e_out, e_R, e_0/2, the amplified-compression and compressed-unit thresholds, and all finitely many rescaled thresholds above, and choose C_corner_unit=max{2*K_u,C_out+K_tar}. These universal witnesses prove both clauses of node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Dependency-gated outer telescope and final witness assembly. Assume nodes 1.3 and 1.5 have been validated. The established external lem-maincb-outer-compression-transfer gives that the explicit T is an extended C_out*t-isomorphism and T_n=I_n tensor T for every n. Hence, by the unit-preservation clause in the registered definitions of extended homomorphism/inclusion, ||T_n(I_n tensor I_B)-I_n tensor u_{S^{A_R}_{P^R}}||<=C_out*t. The validated node 1.5 gives ||I_n tensor u_{S^{A_R}_{P^R}}-I_n tensor P^R||<=K_tar*t, so the triangle inequality gives ||T_n(I_n tensor I_B)-I_n tensor P^R||<=(C_out+K_tar)*t. The validated node 1.3 supplies the first-clause estimate with coefficient 4*K_cmp+7/2. Therefore choose e_corner_unit>0 as the minimum of e_out and every positive smallness threshold required in validated nodes 1.3 and 1.5, and choose C_corner_unit=max{4*K_cmp+7/2,C_out+K_tar}; these are universal and prove both clauses of node 1. The extra hypothesis ||v(I_B)-u_{S_P}||<=t is retained and is not needed after invoking the stronger outer-transfer conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** Replacement outer telescope, with no unit-preservation inference. Require validated nodes 1.1, 1.3, 1.4, and 1.5. Put C_1=4*K_cmp+7/2, x=v(I_B), u=Co_P(P)=u_{S_P}, and a=Co_R(P)=P^R. After shrinking t by universal thresholds, node 1.1 applied at every matrix level first to R in A (defect parameters delta=epsilon=t) and then to a in A_R (parameters delta=K_a*t and epsilon=K_R*t from node 1.4) gives universal bounds B_R,B_a<infinity for ||Co_{R_n}^A|| and ||Co_{a_n}^{A_R}||, where R_n=I_n tensor R and a_n=I_n tensor a. The amplified-compression identity, together with T_n=I_n tensor T from lem-maincb-outer-compression-transfer, gives T_n(I_n tensor I_B)=Co_{a_n}^{A_R}(Co_{R_n}^A(x_n)), I_n tensor u_{S^{A_R}_{P^R}}=Co_{a_n}^{A_R}(a_n), and a_n=Co_{R_n}^A(P_n), where x_n=I_n tensor x and P_n=I_n tensor P. Hence linearity and the triangle inequality give ||T_n(I_n tensor I_B)-I_n tensor u_{S^{A_R}_{P^R}}|| <= B_a*B_R*||x_n-P_n|| <= B_a*B_R*(||x_n-I_n tensor u||+||I_n tensor u-P_n||). The operator-space direct-sum axiom gives ||x_n-I_n tensor u||=||x-u||<=t, while validated node 1.3 gives ||I_n tensor u-P_n||<=C_1*t. Therefore this difference is at most B_a*B_R*(1+C_1)*t. Validated node 1.5 and one more triangle inequality yield ||T_n(I_n tensor I_B)-I_n tensor P^R|| <= (B_a*B_R*(1+C_1)+K_tar)*t. Together with node 1.3, choose C_corner_unit=max{C_1,B_a*B_R*(1+C_1)+K_tar} and choose e_corner_unit>0 as the minimum of e_out and the finitely many positive thresholds required by nodes 1.1, 1.3, 1.4, 1.5 and both amplified-compression applications after their fixed universal rescalings. These universal witnesses prove both root clauses. This argument genuinely uses the additional hypothesis ||v(I_B)-u_{S_P}||<=t and does not assert that an extended approximate isomorphism preserves the unit.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

