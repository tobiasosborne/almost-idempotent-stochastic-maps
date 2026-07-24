# Proof Export

## Node 1

**Statement:** Amplified almost-containment: there are universal C_ac < infinity and e_ac > 0 such that, whenever e=delta+epsilon <= e_ac, P_1,P,Q_1,Q are delta-projections with ||P_1 P-P_1||,||Q_1 Q-Q_1|| <= delta, every n >= 1, and X in M_n tensor S_{P_1,Q_1}, one has ||Co_{P_n,Q_n}(X)-X|| <= C_ac*e*||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform amplified setup: there are universal k_co<infinity and e_0>0 such that, for e<=e_0, writing A_n=M_n tensor A and R_n=I_n tensor R, the four amplified projections P_{1,n},P_n,Q_{1,n},Q_n are delta-projections of norm at most B:=3, satisfy ||P_n P_{1,n}-P_{1,n}||<=delta and ||Q_{1,n}Q_n-Q_{1,n}||<=delta, and every pair of delta-projections R,S in A_n obeys ||Co_{R,S}(Z)-R(ZS)||<=k_co e||Z|| and ||Co_{R,S}(Z)-(RZ)S||<=k_co e||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Amplification and containment bounds: by def-extended-epsilon-cstar-algebra, A_n is an epsilon-C*-algebra, I_n tensor(-) preserves the relevant products, involution, and norm; hence each R_n for R in {P_1,P,Q_1,Q} is a delta-projection. Moreover P_nP_{1,n}-P_{1,n}=I_n tensor(PP_1-P_1)=I_n tensor(P_1P-P_1)^dagger has norm at most delta, while Q_{1,n}Q_n-Q_{1,n}=I_n tensor(Q_1Q-Q_1) has norm at most delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Uniform norm and comparison constants: if epsilon,delta<=1/2, the epsilon-C*-axioms and def-delta-projection give (1-epsilon)||R_n||^2<=||R_n^2||<=||R_n||+delta, so ||R_n||<=3. By def-compressed-corner there are universal k_co<infinity and a positive smallness threshold e_co such that in every A_n, ||Co_{R,S}(Z)-R(ZS)|| and ||Co_{R,S}(Z)-(RZ)S|| are at most k_co e||Z||. Take e_0 to be the minimum of 1/2, e_co, and the positive universal thresholds in lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Source-corner control: for X in M_n tensor S_{P_1,Q_1}, one has Co_{P_{1,n},Q_{1,n}}(X)=X and consequently ||X-P_{1,n}(XQ_{1,n})||<=k_co e||X|| and ||X-(P_{1,n}X)Q_{1,n}||<=k_co e||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Corner identification and fixed-point step: lem-compcb-amplified-compression gives M_n tensor S_{P_1,Q_1}=S_{P_{1,n},Q_{1,n}}. Thus X lies in the image of Co_{P_{1,n},Q_{1,n}} by def-compressed-corner. Writing X=Co_{P_{1,n},Q_{1,n}}(Y), the idempotence supplied by lem-compcb-amplified-compression-identities gives Co_{P_{1,n},Q_{1,n}}(X)=Co_{P_{1,n},Q_{1,n}}^2(Y)=X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Apply the two comparison estimates from node 1.1 to R=P_{1,n}, S=Q_{1,n}, Z=X. Replacing Co_{P_{1,n},Q_{1,n}}(X) by X using the fixed-point step yields ||X-P_{1,n}(XQ_{1,n})||<=k_co e||X|| and ||X-(P_{1,n}X)Q_{1,n}||<=k_co e||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Transferred almost-invariance: under the same hypotheses, both ||P_nX-X|| and ||XQ_n-X|| are at most L e||X||, where L:=k_co(2B+1)+2B(B^2+2) and B=3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Left estimate: put D=P_{1,n}(XQ_{1,n}) and Y=XQ_{1,n}. By node 1.2, ||X-D||<=k_co e||X||. Submultiplicativity, ||P_n||,||P_{1,n}||,||Q_{1,n}||<=B, 1+epsilon<=2, the epsilon-associativity axiom, and node 1.1 give ||P_nX-X||<=||P_n(X-D)||+||P_n(P_{1,n}Y)-P_{1,n}Y||+||D-X||<=2Bk_co e||X||+[epsilon B^2+(1+epsilon)delta]||Y||+k_co e||X||. Since ||Y||<=2B||X|| and epsilon,delta<=e, this is at most [k_co(2B+1)+2B(B^2+2)]e||X||=Le||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Right estimate: put D=(P_{1,n}X)Q_{1,n} and Y=P_{1,n}X. By node 1.2, ||X-D||<=k_co e||X||. Using submultiplicativity and epsilon-associativity exactly as on the left, now with ||Q_{1,n}Q_n-Q_{1,n}||<=delta from node 1.1, one gets ||XQ_n-X||<=||(X-D)Q_n||+||(YQ_{1,n})Q_n-YQ_{1,n}||+||D-X||<=2Bk_co e||X||+[epsilon B^2+(1+epsilon)delta]||Y||+k_co e||X||. Since ||Y||<=2B||X||, this is at most Le||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Final assembly: the first compression comparison and transferred almost-invariance imply ||Co_{P_n,Q_n}(X)-X||<=[k_co+(2B+1)L]e||X||; choosing e_ac=e_0 and C_ac=k_co+(2B+1)L proves node 1 with universal positive finite constants.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Validated node 1.1.2 supplies universal k_co<infinity and e_0>0, B=3, ||P_n||<=B, and ||Co_{P_n,Q_n}(X)-P_n(XQ_n)||<=k_co e||X||; validated nodes 1.3.1 and 1.3.2 supply ||P_nX-X||<=Le||X|| and ||XQ_n-X||<=Le||X||. Therefore, by linearity of left multiplication, the triangle inequality, and ||P_nY||<=(1+epsilon)||P_n||||Y|| with 1+epsilon<=2, one has ||Co_{P_n,Q_n}(X)-X||<=[k_co+(2B+1)L]e||X||. Thus C_ac:=k_co+(2B+1)L is finite and universal and e_ac:=e_0 is positive and universal, proving the asserted contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** Use only the validated premises 1.1.2, 1.3.1, and 1.3.2. Insert P_n(XQ_n) and P_nX, and use linearity of Y mapsto P_nY to obtain ||Co_{P_n,Q_n}(X)-X|| <= ||Co_{P_n,Q_n}(X)-P_n(XQ_n)|| + ||P_n(XQ_n-X)|| + ||P_nX-X||. Node 1.1.2 bounds the first term by k_co e||X|| and gives ||P_n||<=B and e_0<=1/2; nodes 1.3.2 and 1.3.1 respectively give ||XQ_n-X||<=Le||X|| and ||P_nX-X||<=Le||X||. Since epsilon<=e<=e_0<=1/2, submultiplicativity yields ||P_n(XQ_n-X)|| <= (1+epsilon)||P_n||||XQ_n-X|| <= 2BL e||X||. Consequently the displayed sum is at most [k_co+(2B+1)L]e||X||. With B=3 and finite universal k_co,L, C_ac:=k_co+(2B+1)L is finite universal, and e_ac:=e_0>0 is universal.

**Type:** claim

**Inference:** triangle inequality, linearity, and submultiplicativity from validated premises

**Status:** validated

**Taint:** clean

