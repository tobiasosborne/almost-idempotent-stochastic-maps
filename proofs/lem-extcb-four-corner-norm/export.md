# Proof Export

## Node 1

**Statement:** Four-corner assembled norm estimate: there are universal K_norm < infinity and e_norm > 0 such that, for every four-corner merging datum with e = rho+epsilon <= e_norm, every n >= 1, and every X in M_n tensor B, the assembled map gamma_n = alpha_n Gamma_n mu_n (where mu_n(X) = ((I_n tensor Pi_j) X (I_n tensor Pi_k))_{j,k}, Gamma_n is the direct sum of the four fixed amplifications gamma_{jk,n}, and alpha_n((Y_jk)) = sum_{jk} Y_jk) satisfies (1-K_norm*e)||X|| <= ||gamma_n(X)|| <= (1+K_norm*e)||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform block conditioning: there are universal c_blk>0, B_blk<infinity and e_blk>0 such that, for every datum, every n, and e=rho+epsilon<=e_blk, the assembled map satisfies c_blk||X||<=||gamma_n(X)||<=B_blk||X||. This follows from exact source cornering and quantitative target-corner extraction, not from cancellation-prone triangle estimates alone.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Exact source block decomposition. Put pi_j=I_n tensor Pi_j and X_jk=pi_j X pi_k. Since Pi_1,Pi_2 are complementary orthogonal projections in the source C*-algebra, X=sum_jk X_jk, (X^dagger)_kj=X_jk^dagger, and ||X_jk||<=||X||. Conversely addition reconstructs X, so mu_n is injective and max_jk||X_jk||<=||X||<=sum_jk||X_jk||<=4 max_jk||X_jk||, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Uniform target coordinate extraction. Put p_j=I_n tensor P_j and C_jk=I_n tensor Co_{P_j,P_k}. The quantitative rho-projection and rho-complementarity clauses in def-four-corner-merging-datum, amplified by the operator-space direct-sum axiom, give ||p_j^2-p_j||<=rho and ||p_1+p_2-I||<=rho. The epsilon-C*-lower inequality first gives ||p_j||<=2 for e<=1/4; expanding p_j p_l through p_1+p_2=I+r and using the product, unit, and associator axioms gives ||p_jp_l||<=4e for j!=l. The two compression-versus-left/right-multiplication estimates in def-compressed-corner then give universal M_c,L_c such that ||C_jk||<=M_c and, for Y_lm in M_n tensor S_{P_l,P_m}, C_lm(Y_lm)=Y_lm while ||C_jk(Y_lm)||<=L_c e||Y_lm|| whenever (j,k)!=(l,m). Hence for alpha((Y_jk))=sum Y_jk and beta(Y)=(C_jkY), with the max norm on the fourfold direct sum, ||beta alpha-I||<=3L_c e and ||beta||<=M_c, uniformly in n and all dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Amplification naturality of the compression construction. Fix target rho-projections P,Q, put p=I_n tensor P and q=I_n tensor Q, and set T=L_P R_Q+R_Q L_P-1 on A and T_n=L_p R_q+R_q L_p-1 on M_n tensor A. Matrix multiplication over A gives T_n=I_n tensor T entrywise. In def-compressed-corner, theta(S)=1/2(1+sgn(S)) is defined by the norm-convergent power series in 1-S^2 from theta-idempotent-approximation-map. Every partial polynomial therefore satisfies f_N(T_n)=I_n tensor f_N(T). The matrix-level series converges because p,q are rho-projections in the epsilon-C*-algebra M_n tensor A; taking matrix entries, which are bounded coordinate maps by the operator-space matrix-norm axioms, identifies its limit entrywise with theta(T). Consequently Co_{p,q}=theta(T_n)=I_n tensor theta(T)=I_n tensor Co_{P,Q}. This proves the missing identification directly from the permitted definitions and does not assume that an arbitrary bounded level-one map is completely bounded.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** Uniform amplified compression consequences. By the preceding naturality identity, C_jk=I_n tensor Co_{P_j,P_k} is exactly the compression Co_{p_j,p_k} constructed in the epsilon-C*-algebra M_n tensor A. Hence def-compressed-corner at matrix level supplies one universal c_0 such that both ||C_jk-L_{p_j}R_{p_k}|| and ||C_jk-R_{p_k}L_{p_j}|| are at most c_0 e. With q_0=1+epsilon<=5/4 and ||p_i||<=2, ||C_jk||<=4q_0^2+c_0e=:M_c. Moreover Im(C_lm)=M_n tensor Im(Co_{P_l,P_m})=M_n tensor S_{P_l,P_m}; thus C_lm(Y)=Y on that space. If j!=l, use C_jk near R_{p_k}L_{p_j}, Y=C_lmY near R_{p_m}L_{p_l}Y=(p_lY)p_m, the associator bound twice, and ||p_jp_l||<=4e. Successive product-norm bounds give ||C_jkY|| <= [c_0+4q_0^2c_0+32q_0^2+16q_0^3]e||Y||. If k!=m, the symmetric calculation uses C_jk near L_{p_j}R_{p_k}, Y near L_{p_l}R_{p_m}Y=p_l(Yp_m), and ||p_mp_k||<=4e, with the same universal bound. Thus any mismatched pair obeys ||C_jk(Y_lm)||<=L_c e||Y_lm|| for universal L_c, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.3

**Statement:** Coordinate estimate. For Z=(Y_lm) in the fourfold max-norm direct sum, the jk coordinate of beta alpha(Z)-Z is sum over (l,m)!=(j,k) of C_jk(Y_lm), because C_jk(Y_jk)=Y_jk. There are exactly three off-target terms, so ||beta alpha-I||<=3L_c e. Also max_jk||C_jkY||<=M_c||Y|| gives ||beta||<=M_c. These are dimension- and amplification-independent because c_0 and the epsilon-C*-axioms are uniform at every matrix level.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Apply coordinate extraction. Let Z=Gamma_n mu_n(X)=(gamma_jk,n(X_jk)) and gamma_n(X)=alpha_n(Z). The datum two-sided norm clause and node 1.1.1 give ||Z||_max>=(1-rho)max||X_jk||>=(1-rho)||X||/4 and ||gamma_n(X)||<=sum_jk (1+rho)||X_jk||<=4(1+rho)||X||. Node 1.1.2 gives (1-3L_c e)||Z||_max<=||beta alpha Z||_max<=M_c||gamma_n(X)||. Therefore ||gamma_n(X)||>=((1-3L_c e)(1-rho)/(4M_c))||X||. Take e_blk=min{1/8,(12L_c)^(-1)}. Since rho<=e<=e_blk, one has 1-3L_c e>=3/4 and 1-rho>=7/8, hence ||gamma_n(X)||>=21||X||/(128M_c)>=||X||/(16M_c); also ||gamma_n(X)||<=4(1+rho)||X||<=5||X||. Thus c_blk=1/(16M_c), B_blk=5 work universally.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Uniform assembled square defect: after a universal further smallness restriction there is D_sq<infinity such that ||gamma_n(X^dagger X)-gamma_n(X)^dagger gamma_n(X)||<=D_sq e||X||^2 for every n and X. The derivation uses only the datum cornerwise involution/product defects, compressed-product comparison, target approximate complementarity, and the coarse upper bound from node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Corner product estimates. Put p_i=I_n tensor P_i and C_jk=I_n tensor Co_{P_j,P_k}. Validated nodes 1.1.2.1 and 1.1.2.2 identify C_jk with Co_{p_j,p_k}, identify M_n tensor S_{P_j,P_k} with Im C_jk, and give universal c_0 such that every U in that corner obeys both ||U-p_j(U p_k)||<=c_0 e||U|| and ||U-(p_j U)p_k||<=c_0 e||U||, while ||p_i||<=2 and ||p_1p_2||,||p_2p_1||<=4e. If U is in the jk corner and V is in the lm corner with k!=l, set U_0=p_j(U p_k), V_0=p_l(V p_m). Bilinearity and the product-norm axiom control UV-U_0V_0 by O(e)||U||||V||. The chain (p_j(U p_k))V_0 -> p_j((U p_k)V_0) -> p_j(U(p_kV_0)) -> p_j(U((p_kp_l)(V p_m))) uses exactly three epsilon-associator estimates; the last expression is O(e)||U||||V|| because ||p_kp_l||<=4e. Hence ||UV||<=K_inc e||U||||V|| for a universal K_inc. If k=l, amplification naturality and def-compressed-corner at matrix level give ||UV-U dot V||<=c_c e||U||||V||. All constants are amplification- and dimension-independent.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** Quantitative licensed bridge. Let q=1+epsilon<=5/4 and take the universal c_0 from validated node 1.1.2.2. That node, based on naturality node 1.1.2.1, gives C_ab=Co_{p_a,p_b}, Im(C_ab)=M_n tensor S_{P_a,P_b}, ||p_i||<=2, ||p_kp_l||<=4e for k!=l, and ||W-p_a(Wp_b)||<=c_0e||W|| for W in the ab corner. For U,V as in the parent, put U_0=p_j(Up_k), V_0=p_l(Vp_m), a=Up_k, and b=Vp_m. Then ||a||<=2q||U||, ||b||<=2q||V||, ||U_0||<=4q^2||U||, and ||V_0||<=4q^2||V||. Bilinearity gives UV-U_0V_0=(U-U_0)V+U_0(V-V_0), hence ||UV-U_0V_0||<=[q c_0+4q^3 c_0]e||U||||V||. Next compare U_0V_0=(p_j a)V_0 successively with p_j(aV_0), p_j(U(p_kV_0)), and p_j(U((p_kp_l)b)). These are exactly three associator moves. Their errors are respectively at most 16q^3 epsilon, 16q^3 epsilon, and 16q^3 epsilon times ||U||||V||, after the needed product-norm multipliers. The final term has norm at most 16q^4 e||U||||V|| by ||p_kp_l||<=4e. Therefore ||UV||<={c_0(q+4q^3)+48q^3+16q^4}e||U||||V||, and q<=5/4 yields a universal K_inc. For k=l, C_jm=Co_{p_j,p_m} and the matrix-level compressed-product estimate in def-compressed-corner gives ||UV-C_jm(UV)||<=c_c e||U||||V||; amplification naturality identifies C_jm(UV) with U dot V. This proves both cases without using the pending conclusion of node 1.1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Sixteen-term square comparison. Write X=sum_ab X_ab and U_ab=gamma_ab,n(X_ab). Exact source multiplication gives (X^dagger X)_bd=sum_a X_ab^dagger X_ad. The datum involution clause gives ||U_ab^dagger-gamma_ba,n(X_ab^dagger)||<=rho||X_ab||. For the eight compatible triples (a,b,d), the datum compressed-product clause and the compatible ambient-versus-compressed estimate from node 1.2.1 compare U_ab^dagger U_ad with gamma_bd,n(X_ab^dagger X_ad), with total error at most a universal multiple of e||X||^2, using ||U_ab||<=(1+rho)||X||. The other eight terms U_ab^dagger U_cd with a!=c are bounded by node 1.2.1 by K_inc e(1+rho)^2||X||^2 each. Summation and the triangle inequality yield ||gamma_n(X^dagger X)-gamma_n(X)^dagger gamma_n(X)||<=D_sq e||X||^2 for e<=min{e_blk,1/4}, where D_sq is universal. This is precisely node 1.2.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Dependency-gated explicit error accounting (this step is not available until nodes 1.1 and 1.2.1 are validated). Let V_ab=gamma_ba,n(X_ab^dagger). For each compatible triple (a,b,d), the product-norm axiom, datum involution and two-sided norm clauses, node 1.2.1 compatible estimate, and datum compressed-product clause give ||U_ab^dagger U_ad-gamma_bd,n(X_ab^dagger X_ad)|| <= [(1+epsilon)rho(1+rho)+c_c e(1+rho)^2+rho]||X||^2 <= (4+2c_c)e||X||^2 for e<=1/4. (The first term replaces U_ab^dagger by V_ab, the second replaces ambient product V_ab U_ad by V_ab dot U_ad, and the third applies compressed-product compatibility.) For each incompatible quadruple (a,b,c,d), a!=c, node 1.2.1 applied to U_ab^dagger in S_{P_b,P_a} and U_cd in S_{P_c,P_d}, followed by the datum norm clause, gives ||U_ab^dagger U_cd|| <= K_inc e(1+rho)^2||X||^2 <= 2K_inc e||X||^2. Linearity and exact source corner multiplication yield gamma_n(X^dagger X)=sum_{a,b,d}gamma_bd,n(X_ab^dagger X_ad), whereas gamma_n(X)^dagger gamma_n(X)=sum_{a,b,c,d}U_ab^dagger U_cd. There are eight compatible and eight incompatible terms, hence the triangle inequality gives the node-1.2 bound with D_sq=8(4+2c_c+2K_inc), under the common validated smallness ceilings (including e<=min{e_blk,1/4}).

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.1.1

**Statement:** Enforced validation gate and conditional discharge. This child is not an independent substitute for nodes 1.1 and 1.2.1: it is mechanically ineligible for acceptance until both are validated. Once they are validated, node 1.2.1 supplies universal c_c and K_inc for the compatible and incompatible target-corner products, while node 1.1 supplies the common e_blk ceiling (the displayed termwise bounds themselves use only ||X_ab||<=||X|| and the datum two-sided norm clause). With e<=min{e_blk,1/4}, rho,epsilon<=e and 1+rho<=5/4, each compatible term is bounded by [(1+epsilon)rho(1+rho)+c_c e(1+rho)^2+rho]||X||^2 <= (4+2c_c)e||X||^2, and each incompatible term by K_inc e(1+rho)^2||X||^2 <= 2K_inc e||X||^2. The exact source block identity has eight compatible and eight incompatible summands, so summing gives D_sq=8(4+2c_c+2K_inc). Thus the parent follows only after, and exactly from, the two validated dependencies.

**Type:** qed

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Scalar C*-bootstrap and conclusion: using nodes 1.1 and 1.2, the exact C*-identity in the source, and the epsilon-C*-axioms in the target, there are universal K_norm and e_norm>0 such that (1-K_norm e)||X||<=||gamma_n(X)||<=(1+K_norm e)||X|| for all n and X whenever e<=e_norm.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Upper bootstrap. For fixed n let b_n=sup_{X!=0}||gamma_n(X)||/||X||. Node 1.1 gives b_n<=5. The target epsilon-C*-lower inequality and node 1.2 give, for every X, (1-epsilon)||gamma_n(X)||^2<=||gamma_n(X)^dagger gamma_n(X)||<=||gamma_n(X^dagger X)||+D_sq e||X||^2<=b_n||X||^2+D_sq e||X||^2, since the source has ||X^dagger X||=||X||^2. Taking a maximizing sequence yields (1-epsilon)b_n^2<=b_n+D_sq e. If b_n<=1 there is nothing to prove; if b_n>1, then b_n-1<=b_n(b_n-1)=b_n^2-b_n<=epsilon b_n^2+D_sq e<=(25+D_sq)e. Hence b_n<=1+(25+D_sq)e uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Lower bootstrap and universal constants. Let a_n=inf_{X!=0}||gamma_n(X)||/||X||; node 1.1 gives a_n>=c_blk and b_n<=5. The source C*-identity, node 1.2, and the target product-norm axiom give a_n||X||^2<=||gamma_n(X^dagger X)||<=||gamma_n(X)^dagger gamma_n(X)||+D_sq e||X||^2<=(1+epsilon)||gamma_n(X)||^2+D_sq e||X||^2. Taking a minimizing sequence gives a_n<=(1+epsilon)a_n^2+D_sq e. If a_n>=1 the desired lower bound is automatic; if a_n<1, then c_blk(1-a_n)<=a_n(1-a_n)=a_n-a_n^2<=epsilon a_n^2+D_sq e<=(25+D_sq)e. Thus a_n>=1-[(25+D_sq)/c_blk]e. With K_norm=max{25+D_sq,(25+D_sq)/c_blk} and e_norm the minimum of all universal smallness ceilings in nodes 1.1 and 1.2 (and, harmlessly, 1/(2K_norm)), the two bounds hold simultaneously for every n and X, which is the root contract.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Dependency-gated lower bootstrap. This node asserts only the implication from the separately proved estimates 1.1 and 1.2; it is not eligible for acceptance while either is pending. Once 1.1 and 1.2 are validated, fix n and set a=inf_{X!=0}||gamma_n(X)||/||X|| and b=sup_{X!=0}||gamma_n(X)||/||X||. Node 1.1 gives 0<c_blk<=a<=b<=5. For every X, the exact source C*-identity, node 1.2, and the target product-norm axiom give a||X||^2<=||gamma_n(X^dagger X)||<=||gamma_n(X)^dagger gamma_n(X)||+D_sq e||X||^2<=(1+epsilon)||gamma_n(X)||^2+D_sq e||X||^2. A minimizing sequence yields a<=(1+epsilon)a^2+D_sq e. If a<1, then c_blk(1-a)<=a(1-a)<=epsilon a^2+D_sq e<=(25+D_sq)e, since epsilon<=e and a<=b<=5; if a>=1 the lower estimate is immediate. Thus a>=1-((25+D_sq)/c_blk)e. Together with validated node 1.3.1, K_norm=max{25+D_sq,(25+D_sq)/c_blk} and the common smallness ceiling give both sides of the root estimate.

**Type:** qed

**Inference:** dependency_gated_scalar_bootstrap

**Status:** validated

**Taint:** clean

