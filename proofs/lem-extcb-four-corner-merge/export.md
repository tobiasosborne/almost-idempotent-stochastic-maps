# Proof Export

## Node 1

**Statement:** Complete four-corner merge: there are universal C_merge < infinity and a_merge > 0 such that four fixed bijective level-one corner maps satisfying def-four-corner-merging-datum with common defect rho and rho+epsilon <= a_merge combine into one extended C_merge*(rho+epsilon)-isomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Assembly, involution, and unit. For each n let pi_j=I_n tensor Pi_j and define X_jk=pi_j X pi_k, mu_n(X)=(X_jk), Gamma_n=(gamma_jk,n), alpha_n((Y_jk))=sum_jk Y_jk, and gamma_n=alpha_n Gamma_n mu_n. Exact source complementarity gives X=sum_jk X_jk and shows that gamma_n=I_n tensor gamma_1 for the single level-one map gamma_1(X)=sum_jk gamma_jk(Pi_j X Pi_k). The involution clause of def-four-corner-merging-datum gives gamma_n(X^dagger)=gamma_n(X)^dagger exactly. Its two diagonal-unit bounds and ||P_1+P_2-I||<=rho give ||gamma_n(I)-I||<=3rho (with I meaning the matrix-level unit), uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Fixed-map assembly. With pi_j=I_n tensor Pi_j, exact source relations pi_j pi_k=delta_jk pi_j and pi_1+pi_2=I give X=sum_jk pi_j X pi_k. Since gamma_jk,n=I_n tensor gamma_jk are the amplifications of the same four level-one maps, summing their values on these blocks gives gamma_n=I_n tensor gamma_1, where gamma_1(X)=sum_jk gamma_jk(Pi_j X Pi_k). Thus there is one linear level-one map, not a separately chosen family.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Star and unit calculation. Source corner adjoints obey (pi_j X pi_k)^dagger=pi_k X^dagger pi_j. The packaged merging0 involution clause in def-four-corner-merging-datum says gamma_kj,n(Z^dagger)=gamma_jk,n(Z)^dagger, so summing the four blocks yields gamma_n(X^dagger)=gamma_n(X)^dagger exactly. The source unit has only diagonal blocks pi_1,pi_2. The two diagonal-unit clauses give ||gamma_jj,n(pi_j)-I_n tensor P_j||<=rho, and amplified target complementarity gives ||I_n tensor(P_1+P_2)-I||<=rho. The triangle inequality therefore gives ||gamma_n(I)-I||<=3rho. Together with node 1.1.1 this proves node 1.1.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Once node 1.1.1 is validated, the block assembly uses the same fixed amplifications. The datum merging0 equality applied to transposed adjoint blocks proves exact star preservation, and the two diagonal-unit errors plus target complementarity give the displayed 3rho unit error. Hence node 1.1.2 and then node 1.1 follow.

**Type:** qed

**Inference:** dependency_gated_assembly

**Status:** archived

**Taint:** clean

##### Node 1.1.2.2

**Statement:** Quantitative unit bridge from the reprovisioned datum. The registered definition def-four-corner-merging-datum-2026-07-25-amended is an exact workspace snapshot of the current canonical def-four-corner-merging-datum and explicitly supplies ||P_1+P_2-I||<=rho. Put R=P_1+P_2-I. In M_n tensor A, I_n tensor R is the block diagonal diag(R,...,R); repeated application of the registered operator-space matrix-norm axiom ax_R2 gives ||I_n tensor R||=max(||R||,...,||R||)=||R||<=rho. Since the matrix-level target unit is I_n tensor I, this is precisely ||I_n tensor(P_1+P_2)-I_n tensor I||<=rho. Exact source complementarity gives I_n tensor I_B=pi_1+pi_2 and zero off-diagonal unit corners, hence gamma_n(I_n tensor I_B)=gamma_11,n(pi_1)+gamma_22,n(pi_2). Therefore gamma_n(I_n tensor I_B)-I_n tensor I=[gamma_11,n(pi_1)-I_n tensor P_1]+[gamma_22,n(pi_2)-I_n tensor P_2]+I_n tensor R. The two diagonal-unit clauses bound the first two summands by rho each, so the triangle inequality gives ||gamma_n(I_n tensor I_B)-I_n tensor I||<=3rho. Separately, involution compatibility and (pi_j X pi_k)^dagger=pi_k X^dagger pi_j yield gamma_n(X^dagger)=gamma_n(X)^dagger after relabelling j,k in the finite sum. This supplies exactly the star and unit claims of node 1.1.2 without any hidden amplification assumption.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Uniform target-corner product separation. There are universal c_prod,c_cross<infinity and e_corner>0 such that, at every amplification and for e=rho+epsilon<=e_corner, if U lies in M_n tensor S_{P_j,P_k} and V lies in M_n tensor S_{P_l,P_m}, then for k=l one has ||UV-U dot V||<=c_prod e||U||||V||, while for k!=l one has ||UV||<=c_cross e||U||||V||. This is a consequence only of def-compressed-corner, target rho-complementarity in def-four-corner-merging-datum, and the matrix-level epsilon-C*-axioms in def-extended-epsilon-cstar-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Amplified compression identification. For target rho-projections P,Q put p=I_n tensor P and q=I_n tensor Q. The operator T=L_P R_Q+R_Q L_P-1 defining Co_{P,Q} amplifies entrywise to T_n=L_p R_q+R_q L_p-1. The idempotent-producing function theta in def-compressed-corner is obtained by one fixed norm-convergent power series, so polynomial partial sums satisfy theta_N(T_n)=I_n tensor theta_N(T), and passage to the norm limit gives Co_{p,q}=I_n tensor Co_{P,Q}. Consequently M_n tensor S_{P,Q}=Im Co_{p,q}, and all universal compression-versus-left/right-multiplication and compressed-product estimates in def-compressed-corner apply uniformly in M_n tensor A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Amplified approximate orthogonality. Put p_i=I_n tensor P_i and s=p_1+p_2. The datum gives ||p_i^2-p_i||<=rho and ||s-I||<=rho. The epsilon-C*-lower inequality and product bound imply ||p_i||<=2 after a universal smallness restriction. For k!=l, bilinearity gives p_kp_l=p_k(s-I)+(p_kI-p_k)-(p_k^2-p_k); hence the product bound and approximate-unit axiom give ||p_kp_l||<=c_orth(rho+epsilon) for a universal c_orth, uniformly in n. The same calculation with k,l reversed gives both orders.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Explicit amended-definition bridge and estimate. The re-registered 2026-07-25 quantitative-complementarity clause of def-four-corner-merging-datum states that the target P_1,P_2 are rho-projections for the datum common defect rho and that ||P_1+P_2-I||<=rho. At level n, p_i=I_n tensor P_i and s=p_1+p_2 therefore satisfy p_i^dagger=p_i, ||p_i^2-p_i||<=rho, and ||s-I||<=rho (the first two differences are diagonal amplifications; the registered operator-space direct-sum norm axiom preserves their level-one norms). Put t=||p_i||. The matrix-level epsilon-C*-lower axiom and the triangle inequality give (1-epsilon)t^2<=||p_i^2||<=t+rho. If e=rho+epsilon<=1/4, then t<=2: for t>2 one has (1-epsilon)t^2>=(3/4)t^2>t+1/4>=t+rho, a contradiction. For k!=l, bilinearity gives the exact identity p_k p_l=p_k(s-I)+(p_k I-p_k)-(p_k^2-p_k). The matrix-level product and approximate-unit axioms hence give ||p_k p_l||<=2(1+epsilon)rho+2epsilon+rho<=5(rho+epsilon), where epsilon<=1 was used. Interchanging k,l gives the same bound for p_l p_k. Thus node 1.2.2 holds with c_orth=5 under the universal restriction e<=1/4, and every quantitative premise is now explicitly in the AF context.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Corner product calculation. By node 1.2.1, U in M_n tensor S_{P_j,P_k} obeys U=Co_{p_j,p_k}U and hence is O(e)||U||-close both to p_j(Up_k) and to (p_jU)p_k; similarly for V. If k=l, def-compressed-corner directly gives ||UV-U dot V||<=c_prod e||U||||V||. If k!=l, replace U,V by those left/right compressed representatives, use three epsilon-associator moves to bring the middle factors together, then apply ||p_kp_l||<=c_orth e from node 1.2.2; the replacement, associator, and final product errors total at most c_cross e||U||||V||. All constants are universal because only finitely many product/associator estimates occur and ||p_i||<=2. This proves node 1.2.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** Once nodes 1.2.1 and 1.2.2 are validated, every corner element has both uniformly accurate compressed representatives and the two middle target projections satisfy ||p_kp_l||=O(e) for k!=l. The compatible case is the compressed-product estimate in def-compressed-corner; the incompatible case is obtained by the three associator moves displayed in node 1.2.3. Thus its universal c_prod,c_cross estimates follow and discharge node 1.2.

**Type:** qed

**Inference:** dependency_gated_corner_calculus

**Status:** archived

**Taint:** clean

### Node 1.3

**Statement:** Assembled multiplicative defect. Using the target-corner estimates of node 1.2 and the compressed-product clause of def-four-corner-merging-datum, there is a universal D_mult<infinity such that for every n and X,Y in M_n tensor B, ||gamma_n(XY)-gamma_n(X)gamma_n(Y)||<=D_mult(rho+epsilon)||X||||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Dependency-gated sixteen-term expansion. Fix n, write X=sum_jk X_jk and Y=sum_lm Y_lm with ||X_jk||<=||X|| and ||Y_lm||<=||Y||, and put U_jk=gamma_jk,n(X_jk), V_lm=gamma_lm,n(Y_lm). Exact source corner multiplication gives gamma_n(XY)=sum_{j,k,m} gamma_jm,n(X_jk Y_km), while gamma_n(X)gamma_n(Y)=sum_{j,k,l,m} U_jk V_lm. For the eight terms with k=l, def-four-corner-merging-datum compares gamma_jm,n(X_jk Y_km) with U_jk dot V_km within rho||X||||Y||, and validated node 1.2 compares the compressed and ambient products within c_prod e(1+rho)^2||X||||Y|| using the datum norm bounds. Each of the eight terms with k!=l is at most c_cross e(1+rho)^2||X||||Y|| by validated node 1.2. Summing the sixteen estimates and taking e<=1/4 yields the claimed bound with, for example, D_mult=8[1+2c_prod+2c_cross], independent of n and all dimensions.

**Type:** qed

**Inference:** finite_block_expansion

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** All-level near-isometry. By lem-extcb-four-corner-norm, there are universal K_norm<infinity and e_norm>0 such that, whenever e=rho+epsilon<=e_norm, every n and X satisfy (1-K_norm e)||X||<=||gamma_n(X)||<=(1+K_norm e)||X||. The assembled map and factorization are exactly those fixed in node 1.1, so the external result applies without changing maps at different amplification levels.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Direct application of lem-extcb-four-corner-norm. The present hypothesis is exactly a def-four-corner-merging-datum with e=rho+epsilon, and validated node 1.1 identifies its assembled maps as gamma_n=alpha_n Gamma_n mu_n using the same four fixed amplifications required by that external lemma. Therefore, for e<=e_norm, lem-extcb-four-corner-norm gives (1-K_norm e)||X||<=||gamma_n(X)||<=(1+K_norm e)||X|| simultaneously for every n and X. No property of a separately chosen matrix-level map is used.

**Type:** qed

**Inference:** external_lemma_application

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Exact target coverage. There is a universal e_cov>0 such that for e=rho+epsilon<=e_cov the addition map alpha_1: direct-sum_{j,k} S_{P_j,P_k}->A is surjective. Indeed beta(Y)=(Co_{P_j,P_k}Y) satisfies ||alpha_1 beta-I_A||<=C_cov e for a universal C_cov, because each compression is O(e)-close to Y->P_j(YP_k), their sum is O(e)-close to Y->(P_1+P_2)(Y(P_1+P_2)), and P_1+P_2 is rho-close to the target unit; choose e_cov so C_cov e_cov<1 and invert alpha_1 beta by the Neumann series.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Coverage operator estimate. Define beta:A->direct-sum_{j,k} S_{P_j,P_k} by beta(Y)=(Co_{P_j,P_k}Y) and let s=P_1+P_2. By def-compressed-corner there is a universal c_0 such that ||Co_{P_j,P_k}Y-P_j(YP_k)||<=c_0(rho+epsilon)||Y|| for all four pairs. Hence alpha_1 beta(Y) is within 4c_0 e||Y|| of sum_jk P_j(YP_k)=s(Ys), the equality following only from bilinearity with the displayed parentheses. Write s=I+r, ||r||<=rho. The product and approximate-unit axioms of the target epsilon-C*-algebra, applied a fixed finite number of times, give ||s(Ys)-Y||<=c_u e||Y|| once e is in a universal admissible range (also ||s|| is then universally bounded). Therefore ||alpha_1 beta-I_A||<=C_cov e with C_cov=4c_0+c_u universal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.1

**Statement:** The amended datum is now explicitly available in this workspace under the registered name def-four-corner-merging-datum-2026-07-25-amended (its content is the ratified repository shard def-four-corner-merging-datum): it gives ||P_1+P_2-I||<=rho. Thus, for s=P_1+P_2 and r=s-I, ||r||<=rho. Assume the universal admissible range epsilon<=1 and rho<=1. By bilinearity with the indicated parentheses, s(Ys)=(I+r)(Y(I+r))=I(YI)+I(Yr)+r(YI)+r(Yr). The approximate-unit axioms give ||YI||<=(1+epsilon)||Y|| and ||I(YI)-Y||<=||I(YI)-YI||+||YI-Y||<=epsilon||YI||+epsilon||Y||<=epsilon(2+epsilon)||Y||. The product bound together with the unit bound gives ||I(Yr)||<= (1+epsilon)||Yr||<= (1+epsilon)^2 rho||Y||, ||r(YI)||<= (1+epsilon)^2 rho||Y||, and ||r(Yr)||<= (1+epsilon)^2 rho^2||Y||. Hence ||s(Ys)-Y||<=[epsilon(2+epsilon)+(1+epsilon)^2(2rho+rho^2)]||Y||<=15(rho+epsilon)||Y||. Also bilinearity gives sum_{j,k} P_j(YP_k)=s(Ys) exactly, without associativity. Combining this with the four compression errors yields ||alpha_1 beta(Y)-Y||<=(4c_0+15)(rho+epsilon)||Y||. This proves node 1.5.1 with c_u=15 and explicitly supplies the quantitative-complementarity premise requested by the challenge.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Neumann-series discharge. Choose e_cov>0 below the compression-construction radius and with C_cov e_cov<1. For e<=e_cov, node 1.5.1 makes T=alpha_1 beta satisfy ||I_A-T||<1, so T^{-1}=sum_{r>=0}(I_A-T)^r exists as a bounded operator on the complete space A. For every Y in A, Y=T(T^{-1}Y)=alpha_1(beta(T^{-1}Y)); hence alpha_1 is onto. This proves node 1.5 without assuming directness of the target corner sum.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.2.1

**Statement:** Once node 1.5.1 is validated, choose e_cov with C_cov e_cov<1. Then alpha_1 beta is invertible by its norm-convergent Neumann series, and Y=alpha_1[beta((alpha_1 beta)^{-1}Y)] for every Y in A. Hence alpha_1 is surjective and node 1.5 follows.

**Type:** qed

**Inference:** dependency_gated_neumann

**Status:** archived

**Taint:** clean

### Node 1.6

**Statement:** Exact bijectivity of the assembled level-one map. For sufficiently small e, node 1.4 makes gamma_1 injective. Exact source corner decomposition mu_1 is a bijection, and the direct sum Gamma_1 is a bijection because all four fixed level-one gamma_jk are bijective. Node 1.5 makes alpha_1 surjective. Hence gamma_1=alpha_1 Gamma_1 mu_1 is surjective, and therefore bijective; algebraically every I_n tensor gamma_1 is then bijective as well.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Dependency-gated factorization. Take e below e_norm,e_cov and 1/(2K_norm). Validated node 1.4 gives ||gamma_1(X)||>=(1-K_norm e)||X||>=||X||/2, so gamma_1 is injective. The map mu_1:B->direct-sum_{j,k} S_{Pi_j,Pi_k}, X->(Pi_j X Pi_k), is a linear bijection with inverse addition, by exact complementary orthogonal source projections. The direct sum Gamma_1 is a linear bijection because each of the four fixed level-one maps gamma_jk is bijective by hypothesis. Validated node 1.5 says alpha_1 is surjective, so gamma_1=alpha_1 Gamma_1 mu_1 is surjective. Thus gamma_1 is bijective. Finally I_n tensor gamma_1 has inverse I_n tensor gamma_1^{-1}, so all amplifications are algebraically bijective although def-extended-delta-inclusion requires only level-one bijectivity for an extended isomorphism.

**Type:** qed

**Inference:** composition_of_bijections

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Corrected conclusion under the hypotheses actually used. Let e=rho+epsilon and let e_* be the minimum of e_corner,e_norm,e_cov,1/(2K_norm), and the universal admissible compression radius. If e<=e_*, set C_merge=max{3,D_mult,K_norm}. Then nodes 1.1 and 1.3 make every fixed amplification a C_merge*e-homomorphism, node 1.4 gives the two-sided (1 plus-or-minus C_merge*e) norm bounds, and node 1.6 gives bijectivity of the single level-one map; hence def-extended-delta-inclusion gives an extended C_merge*(rho+epsilon)-isomorphism. Thus the valid merge statement has the smallness hypothesis rho+epsilon<=a_merge (take a_merge=e_*), not merely rho<=a_merge. The root contract as presently worded is false without this correction.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.7.1

**Statement:** After nodes 1.1,1.3,1.4,1.6 are validated, take the universal constants exactly as in node 1.7. Exact star and the unit/multiplication bounds make every fixed amplification a C_merge(rho+epsilon)-homomorphism; lem-extcb-four-corner-norm supplies the matching two-sided bounds; and exact level-one bijectivity supplies the isomorphism clause. Def-extended-delta-inclusion then gives the root conclusion.

**Type:** qed

**Inference:** dependency_gated_conclusion

**Status:** archived

**Taint:** clean

#### Node 1.7.2

**Statement:** Why the missing epsilon restriction cannot be derived or bypassed. Let A=C^3 with the standard self-adjoint operator-space matrix norms, coordinatewise involution, multiplication (a,b,c)(a',b',c')=(aa',bb',0), and designated unit I=(1,1,0). At every matrix level this is an extended 1-C*-algebra: multiplication is contractive and associative, involution is isometric and anti-multiplicative, the C*-lower bound has right side (1-1)||X||^2=0, and ||XI-X||,||IX-X||<=||X|| while ||I||=1. Put P_1=(1,0,0), P_2=(0,1,0). They are exact projections and P_1+P_2=I, so rho=0. For these exact multiplication projections the registered theta formula gives Co_{P_j,P_j}=E_j and Co_{P_j,P_k}=0 for j!=k (indeed the defining operator is 2E_j-I on a diagonal corner and -I off diagonal, and theta(T)=(I+sgn(T))/2=(I+T)/2 when T^2=I). Hence the four target corners are CP_1,0,0,CP_2. Take B=C^2 with its usual exact C*-structure and source projections Pi_1=(1,0), Pi_2=(0,1); its four source corners have the same description. Use the identity maps on the two diagonal one-dimensional corners and the unique maps 0->0 off diagonal. At every amplification these four fixed maps are bijective complete isometries and satisfy involution, compressed-product, diagonal-unit, and norm-control clauses with common defect rho=0. Nevertheless their assembled map is gamma:B->A, gamma(a,b)=(a,b,0), which is not surjective (and no linear bijection B->A exists since dim B=2 and dim A=3). Thus rho can be arbitrarily small while epsilon=1 and the isomorphism conclusion fails. The only valid repair is to impose rho+epsilon<=a_merge (or an equivalent epsilon ceiling), exactly as stated in amended node 1.7.

**Type:** claim

**Inference:** counterexample and corrected domain restriction

**Status:** validated

**Taint:** clean

