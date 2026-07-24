# Proof Export

## Node 1

**Statement:** Single-compression transfer: there are universal C_co < infinity and e_co > 0 such that restricting an extended alpha-inclusion to one ideal and following it by one compatible amplified compression produces an extended C_co*(alpha+epsilon)-inclusion whenever alpha+epsilon <= e_co.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Precise compatible setup and universal ledger: let A be an extended epsilon-C*-algebra, B an exact unital C*-algebra, J a unital direct-summand ideal with unit q, and v:B->A an extended alpha-inclusion. The compatible single compression is defined by P=v(q) and T=Co_P composed with v restricted to J. For e=alpha+epsilon below one universal threshold, P is a nonvanishing alpha-projection, S_P is an extended C_ca*e-C*-algebra, and universal constants D,K<infinity used below may be chosen independently of B,J,A,n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Projection induced by the ideal unit. Since q=q^dagger=q^2 and ||q||=1 in the exact C*-algebra B, def-extended-delta-inclusion gives P^dagger=v(q^dagger)=P, ||P^2-P||=||v(q)v(q)-v(q^2)||<=alpha, and 1-alpha<=||P||<=1+alpha. Thus P is an alpha-projection by def-delta-projection and is nonvanishing for small e because its norm lies in the second alternative with abs(||P||-1)<=alpha<=e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Target algebra and constant ledger. Let C_ca,e_ca be the universal witnesses in lem-compcb-corner-algebra. Applied with delta=alpha, that external makes S_P, with compressed product, inherited involution and u_P=Co_P(P), an extended C_ca*e-C*-algebra whenever e<=e_ca. By the operator comparison asserted in def-compressed-corner there are universal k_cmp<infinity and e_cmp0>0 such that at every amplified level ||Co_{P_n}(Z)-(P_n Z)P_n||<=k_cmp*e*||Z||. Let D=2*k_cmp+5 and K_N=D+1. Together with the universal witnesses C_r,e_r from lem-compcb-rectangular-product and the thresholds from lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities, all constants and their finite minimum are universal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** At every n>=1, T_n=id_{M_n} tensor T equals Co_{P_n} composed with v_n on M_n tensor J, has range in M_n tensor S_P, is linear, preserves dagger exactly, and sends the source unit I_n tensor q exactly to the amplified compressed unit Co_{P_n}(P_n).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Amplified formula and range. By lem-compcb-amplified-compression, id_{M_n} tensor Co_P=Co_{P_n} and M_n tensor S_P=S_{P_n}, where P_n=I_n tensor P. Therefore T_n(x)=Co_{P_n}(v_n(x)) for x in M_n tensor J and lies in Image(Co_{P_n})=S_{P_n}=M_n tensor S_P. Both v_n and Co_{P_n} are linear by def-extended-delta-inclusion and def-compressed-corner, so T_n is linear.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Exact dagger and unit clauses. The star clause of the extended alpha-inclusion gives v_n(x^dagger)=v_n(x)^dagger. Lem-compcb-amplified-compression-identities with the square pair P_n,P_n gives Co_{P_n}(Z^dagger)=Co_{P_n}(Z)^dagger, hence T_n(x^dagger)=T_n(x)^dagger. The unit of M_n tensor J is q_n=I_n tensor q and v_n(q_n)=I_n tensor v(q)=P_n, so T_n(q_n)=Co_{P_n}(P_n)=I_n tensor Co_P(P)=I_n tensor u_P, where the last equality again uses lem-compcb-amplified-compression. Thus the unit defect is zero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Context-dependent derivation. Import validated node 1.1: J has unit q, P=v(q), T=Co_P composed with v restricted to J, and P is an alpha-projection, with e=alpha+epsilon below the universal thresholds for the amplified-compression results. For n>=1 put v_n=id_{M_n} tensor v, P_n=I_n tensor P, and q_n=I_n tensor q. Tensor functoriality for linear maps gives T_n=id_{M_n} tensor (Co_P composed with v|_J)=(id_{M_n} tensor Co_P) composed with v_n. Lem-compcb-amplified-compression changes this exactly to Co_{P_n} composed with v_n and identifies Image(Co_{P_n})=S_{P_n}=M_n tensor S_P, proving the formula and range; linearity follows because v_n and Co_{P_n} are linear. For x in M_n tensor J, the exact star clause for the extended alpha-inclusion and lem-compcb-amplified-compression-identities for the square pair (P_n,P_n) give T_n(x^dagger)=Co_{P_n}(v_n(x)^dagger)=Co_{P_n}(v_n(x))^dagger=T_n(x)^dagger. Finally v_n(q_n)=I_n tensor v(q)=P_n, so T_n(q_n)=Co_{P_n}(P_n)=I_n tensor Co_P(P), the last equality being lem-compcb-amplified-compression. Thus every clause of node 1.2 follows in the setup supplied by node 1.1.

**Type:** claim

**Inference:** by validated setup and amplified compression identities

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Uniform compression-closeness estimate: there are universal D<infinity and e_d>0 such that, whenever e<=e_d, every n>=1 and x in M_n tensor J satisfy ||T_n(x)-v_n(x)||<=D*e*||x||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Ideal-support estimates before compression. Put q_n=I_n tensor q, P_n=v_n(q_n), and Z=v_n(x). Since q_n x=x q_n=x in M_n tensor J, the multiplicative clause of the extended alpha-inclusion gives ||P_n Z-Z||<=alpha||x|| and ||ZP_n-Z||<=alpha||x||. Its norm bounds also give ||P_n||<=1+alpha and ||Z||<=(1+alpha)||x||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Compression comparison and assembly. Def-compressed-corner, applied in the epsilon-C*-algebra M_n tensor A to the alpha-projection P_n, gives ||Co_{P_n}(Z)-(P_n Z)P_n||<=k_cmp*e||Z|| with the universal k_cmp of node 1.1.2. If e<=1/2, the epsilon-C*-product bound and node 1.3.1 yield ||(P_n Z)P_n-Z||<=||(P_n Z-Z)P_n||+||ZP_n-Z||<=[(1+epsilon)(1+alpha)+1]*alpha||x||<=5e||x||. Also k_cmp*e||Z||<=2*k_cmp*e||x||. Thus ||T_n(x)-v_n(x)||<=D*e||x|| for D=2*k_cmp+5, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** The validated external lem-compcb-amplified-almost-containment is consistent with and strengthens the same compatibility principle when a restricted range is already presented as an inner compressed corner: under its stated projection-containment hypotheses it directly supplies a universal amplified compression-closeness bound. The present canonical ideal compression needs no extra range hypothesis because nodes 1.3.1-1.3.2 derive that bound directly from q_n x=x q_n=x.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The compression-closeness estimate and the two-sided bounds for the extended alpha-inclusion imply (1-K_N*e)||x||<=||T_n(x)||<=(1+K_N*e)||x|| at every n, for the universal K_N=D+1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** For any n and x, node 1.3 gives ||T_n(x)-v_n(x)||<=D*e||x||, while def-extended-delta-inclusion gives (1-alpha)||x||<=||v_n(x)||<=(1+alpha)||x||. The triangle and reverse-triangle inequalities therefore give ||T_n(x)||<=[1+alpha+D*e]||x||<=[1+(D+1)e]||x|| and ||T_n(x)||>=[1-alpha-D*e]||x||>=[1-(D+1)e]||x||. This is uniform in n and proves the claim with K_N=D+1.

**Type:** claim

**Inference:** triangle and reverse-triangle inequalities

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** With the compressed product on S_P, there is a universal K_M<infinity such that every n and x,y in M_n tensor J satisfy ||T_n(xy)-T_n(x) dot T_n(y)||<=K_M*e*||x||||y|| whenever e is below the common threshold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Four-term multiplicativity telescope. For fixed n and x,y in M_n tensor J, insert v_n(xy), v_n(x)v_n(y), and T_n(x)T_n(y) to obtain ||T_n(xy)-T_n(x) dot T_n(y)|| <= ||T_n(xy)-v_n(xy)|| + ||v_n(xy)-v_n(x)v_n(y)|| + ||v_n(x)v_n(y)-T_n(x)T_n(y)|| + ||T_n(x)T_n(y)-T_n(x) dot T_n(y)||. This uses only the ambient and compressed products already defined.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Uniform bounds for the four terms. The first is at most D*e||x||||y|| by node 1.3 and exact source submultiplicativity; the second is at most alpha||x||||y|| by the extended inclusion. For the third, insert T_n(x)v_n(y), use the epsilon-C*-product bound, node 1.3, ||v_n(z)||<=(1+alpha)||z||, and node 1.4 to get at most 2*D*(K_N+3)*e||x||||y|| when e<=1. Since T_n(x),T_n(y) lie in the amplified square corner, lem-compcb-rectangular-product gives for the fourth at most C_r*e||T_n(x)||||T_n(y)||<=C_r*(1+K_N)^2*e||x||||y||. Therefore K_M:=D+1+2*D*(K_N+3)+C_r*(1+K_N)^2 is finite, universal, and bounds the sum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.2.1

**Statement:** Bounds for the first two telescope terms, conditional on the registered compression estimate. By node 1.3 applied to xy, ||T_n(xy)-v_n(xy)||<=D*e||xy||<=D*e||x||||y||, since M_n tensor J is an exact C*-algebra and hence its product is submultiplicative. By the multiplicative clause of the extended alpha-inclusion, ||v_n(xy)-v_n(x)v_n(y)||<=alpha||x||||y||<=e||x||||y||.

**Type:** claim

**Inference:** application of registered estimate and definitions

**Status:** validated

**Taint:** clean

###### Node 1.5.2.1.1

**Statement:** Source-algebra typing and norm control from the validated setup. Node 1.1 says that B is an exact unital C*-algebra and J is a unital direct-summand ideal of B. Hence J, with the inherited multiplication, involution, and norm, is a C*-subalgebra: for x,y in M_n tensor J, the matrix product xy again lies in M_n tensor J. The standard matrix amplification M_n tensor J is therefore an exact C*-algebra, so its C*-norm is submultiplicative and ||xy||<=||x||||y||. Node 1.1 also supplies e=alpha+epsilon with alpha,epsilon>=0 and v:B->A an extended alpha-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.2.1.2

**Statement:** Apply validated node 1.3 to the now correctly typed element xy in M_n tensor J: ||T_n(xy)-v_n(xy)||<=D*e||xy||<=D*e||x||||y||. Since v is an extended alpha-inclusion, def-extended-delta-inclusion says v_n is an alpha-homomorphism at every n; its multiplicative clause gives ||v_n(xy)-v_n(x)v_n(y)||<=alpha||x||||y||<=e||x||||y|| because alpha<=alpha+epsilon=e. These are precisely the first two telescope bounds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.2.2

**Statement:** Bound for the third telescope term, conditional on the registered compression and norm estimates. Insert T_n(x)v_n(y). The epsilon-C*-product bound, node 1.3, the inclusion norm bound, and node 1.4 give ||v_n(x)v_n(y)-T_n(x)T_n(y)|| <= (1+epsilon)[||v_n(x)-T_n(x)|| ||v_n(y)||+||T_n(x)|| ||v_n(y)-T_n(y)||] <= D*e*(1+epsilon)*[(1+alpha)+(1+K_N*e)]||x||||y||. Since 0<=alpha,epsilon<=e<=1, this is at most 2*D*(K_N+3)*e||x||||y||.

**Type:** claim

**Inference:** telescope and epsilon-product bound

**Status:** validated

**Taint:** clean

##### Node 1.5.2.3

**Statement:** Product naturality and the fourth-term bound. Node 1.2.1 gives T_n(x),T_n(y) in S_{P_n}=M_n tensor S_P. If A=[a_ij] and B=[b_ij] lie there, the level-n product obtained by amplifying the compressed product on S_P has entries sum_k Co_P(a_ik b_kj), which by linearity equal Co_P(sum_k a_ik b_kj). Thus A dot_n B=(id_{M_n} tensor Co_P)(AB)=Co_{P_n}(AB), using lem-compcb-amplified-compression. It is therefore exactly the compatible square-corner product estimated by lem-compcb-rectangular-product, not a different product. Consequently ||T_n(x)T_n(y)-T_n(x) dot_n T_n(y)||<=C_r*e||T_n(x)|| ||T_n(y)||<=C_r*(1+K_N)^2*e||x||||y||, where node 1.4 and e<=1 give the last inequality.

**Type:** claim

**Inference:** matrix-product computation and external rectangular estimate

**Status:** validated

**Taint:** clean

##### Node 1.5.2.4

**Statement:** Summing the four bounds from nodes 1.5.2.1--1.5.2.3 in the telescope of validated node 1.5.1 gives [D+1+2*D*(K_N+3)+C_r*(1+K_N)^2]*e||x||||y||. Hence K_M:=D+1+2*D*(K_N+3)+C_r*(1+K_N)^2 is finite and universal. The explicit dependency and requires-validated edges ensure this conclusion cannot be accepted before nodes 1.3 and 1.4; the range fact is taken from already validated node 1.2.1, and product naturality was proved in node 1.5.2.3, so no dependency on the circular sibling 1.5.3 is needed.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** The rectangular-product application is legitimate at every n: for each z in M_n tensor J, T_n(z)=Co_{P_n}(v_n(z)) and idempotence of Co_{P_n} puts T_n(z) in S_{P_n}=M_n tensor S_P. Hence T_n(x),T_n(y) form the compatible amplified square-corner pair (P_n,P_n,P_n); product naturality identifies the amplified S_P product with Co_{P_n}(T_n(x)T_n(y)), so lem-compcb-rectangular-product applies with a threshold independent of n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.3.1

**Statement:** Product naturality under amplification: for every n and A=(a_ij),B=(b_ij) in M_n tensor S_P, if dot_amp denotes the multiplication on M_n tensor S_P obtained by amplifying the compressed product a dot_P b=Co_P(ab), then (A dot_amp B)_ij=sum_k Co_P(a_ik b_kj)=Co_P(sum_k a_ik b_kj). Therefore A dot_amp B=(id_{M_n} tensor Co_P)(AB)=Co_{P_n}(AB), where the final equality is lem-compcb-amplified-compression. By def-compressed-corner, Co_{P_n}(AB) is exactly the rectangular compressed product for the compatible triple (P_n,P_n,P_n), not merely an element of the same underlying space.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.3.2

**Statement:** Local range proof, independent of nodes 1.2 and 1.5.2. Fix n>=1 and z in M_n tensor J. By validated node 1.1, T=Co_P composed with v|_J, P=v(q), and P is an alpha-projection. Hence T_n(z)=(id_{M_n} tensor Co_P)(v_n(z))=Co_{P_n}(v_n(z)), where P_n=I_n tensor P, by lem-compcb-amplified-compression. By lem-compcb-amplified-compression-identities, Co_{P_n} is idempotent, so Co_{P_n}(T_n(z))=Co_{P_n}^2(v_n(z))=T_n(z). Thus T_n(z) belongs to Img(Co_{P_n})=S_{P_n} by def-compressed-corner; and lem-compcb-amplified-compression gives S_{P_n}=M_n tensor S_P. Applying this to z=x and z=y proves that both actual factors T_n(x),T_n(y) lie in M_n tensor S_P. All invoked thresholds depend only on the universal externals and not on n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.3.3

**Statement:** Now apply validated node 1.5.3.1 to A=T_n(x), B=T_n(y), whose hypotheses are supplied by the preceding local range proof: the amplified compressed-corner product equals Co_{P_n}(T_n(x)T_n(y)), exactly the rectangular compressed product for the compatible triple (P_n,P_n,P_n). Therefore lem-compcb-rectangular-product applies and yields ||T_n(x) dot_amp T_n(y)-T_n(x)T_n(y)|| <= C_co*e*||T_n(x)||*||T_n(y)||, with a universal threshold independent of n. This establishes the legitimacy assertion without using pending node 1.2 or pending node 1.5.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Taking C_co=max{C_ca,K_N,K_M} and e_co to be the positive minimum of all thresholds used above proves that T is an extended C_co*(alpha+epsilon)-inclusion into the compressed corner; the constants are universal and no amplification level or ideal dimension enters.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Let e_co be the minimum of 1/2, e_ca, e_cmp0, e_r, e_d and the positive thresholds in lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities, and put C_co=max{1,C_ca,K_N,K_M}. Node 1.1 gives the target compressed corner as an extended C_ca*e-C*-algebra. Node 1.2 proves at every n that T_n is linear, has the correct target, preserves dagger, and has zero unit defect. The validation-gated direct estimate in node 1.6.1.2 gives multiplicative defect at most K_M*e, without using pending node 1.5, and node 1.4 gives the two-sided (1 plus-or-minus K_N*e) norm bounds. Consequently the guarded assembly in node 1.6.1.4 applies def-extended-delta-inclusion to show that every amplification is a C_co*e-inclusion. Since e=alpha+epsilon and all constants and thresholds are universal, T is the required extended C_co*(alpha+epsilon)-inclusion.

**Type:** claim

**Inference:** definition of extended inclusion and universal constant minimum

**Status:** validated

**Taint:** clean

##### Node 1.6.1.1

**Statement:** Dependency-explicit final assembly. After nodes 1.1, 1.2, 1.4, and 1.5 have been validated, fix n>=1. Node 1.1 supplies the target extended C_ca*e-C*-algebra and universal constants/thresholds; node 1.2 supplies linearity, target membership, exact dagger preservation, and zero unit defect for T_n; node 1.5 supplies multiplicative defect at most K_M*e*||x||||y||; and node 1.4 supplies (1-K_N*e)||x||<=||T_n(x)||<=(1+K_N*e)||x||. For C_co=max{1,C_ca,K_N,K_M}, these are respectively bounded by the C_co*e target-algebra parameter, C_co*e-homomorphism defects, and C_co*e two-sided norm distortion. Hence T_n is a C_co*e-inclusion by def-extended-delta-inclusion. Since n was arbitrary, T is an extended C_co*e-inclusion. With e=alpha+epsilon and e_co the stated positive finite minimum of the universal thresholds, this is exactly the claimed extended C_co*(alpha+epsilon)-inclusion, with constants independent of n and the ideal dimension.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.6.1.2

**Statement:** Direct multiplicativity estimate without using pending node 1.5. Fix n>=1 and x,y in M_n tensor J. The validated telescope 1.5.1 bounds the defect by four terms. For the first, validated 1.1 identifies J as an ideal in the exact C*-algebra B, hence M_n tensor J is an exact C*-algebra and ||xy||<=||x||||y||; validated 1.3 applied to xy gives at most D*e||x||||y||. For the second, def-extended-delta-inclusion applied to the extended alpha-inclusion v gives at most alpha||x||||y||<=e||x||||y||. Validated 1.5.2.2 bounds the third term by 2*D*(K_N+3)*e||x||||y||, and validated 1.5.2.3 bounds the fourth by C_r*(1+K_N)^2*e||x||||y||. Therefore, with K_M:=D+1+2*D*(K_N+3)+C_r*(1+K_N)^2, one has ||T_n(xy)-T_n(x) dot T_n(y)||<=K_M*e||x||||y||. All constants and thresholds are universal by 1.1, and the estimate is uniform in n.

**Type:** claim

**Inference:** triangle inequality and validated uniform estimates

**Status:** validated

**Taint:** clean

##### Node 1.6.1.3

**Statement:** Dependency-correct final assembly, independent of pending node 1.5. Once direct multiplicativity node 1.6.1.2 and validated nodes 1.1, 1.2, and 1.4 are validated premises, fix n>=1. Node 1.1 supplies the target extended C_ca*e-C*-algebra and the universal threshold ledger; node 1.2 supplies linearity, correct target, exact dagger preservation, and zero unit defect for T_n; node 1.6.1.2 supplies multiplicative defect at most K_M*e||x||||y||; and node 1.4 supplies (1-K_N*e)||x||<=||T_n(x)||<=(1+K_N*e)||x||. With C_co=max{1,C_ca,K_N,K_M}, every required defect and target parameter is at most C_co*e, so T_n is a C_co*e-inclusion by def-extended-delta-inclusion. Since n is arbitrary, T is an extended C_co*e-inclusion. Substituting e=alpha+epsilon and taking e_co to be the positive minimum of the universal thresholds gives the root contract, uniformly in n and the ideal dimension. This derivation has no dependency on node 1.5.

**Type:** qed

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.6.1.4

**Statement:** Guarded final assembly replacing the unsound dependency on pending node 1.5. Require validation of nodes 1.1, 1.2, 1.4, and 1.6.1.2. Then for arbitrary n, node 1.1 gives the extended C_ca*e-C*-algebra target and universal thresholds, node 1.2 gives the linear, target, dagger, and zero-unit-defect clauses, node 1.6.1.2 gives multiplicative defect <=K_M*e||x||||y||, and node 1.4 gives the two-sided (1 plus-or-minus K_N*e) norm bounds. For C_co=max{1,C_ca,K_N,K_M}, def-extended-delta-inclusion makes T_n a C_co*e-inclusion. Universality and arbitrariness of n make T an extended C_co*e-inclusion; e=alpha+epsilon and the universal threshold minimum yield the contract. No premise from pending node 1.5 is used.

**Type:** qed

**Inference:** definition of extended inclusion from guarded validated premises

**Status:** validated

**Taint:** clean

