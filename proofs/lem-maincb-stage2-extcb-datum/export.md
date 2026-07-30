# Proof Export

## Node 1

**Statement:** There are universal C_s2 >= 1 and e_s2 > 0, with the e_ca threshold and universal C_ca coefficient of lem-compcb-corner-algebra absorbed into e_s2 and C_s2, such that, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has nonempty U, j notin U, dim S^A_{P_k,P_j} = 1 for every k in U, and R = U union {j}, and a supplied current reset state v_U:M_{|U|}->A_U is an extended isomorphism satisfying epsilon_U, d_U <= t <= e_s2 and d_U <= c_0^cb*epsilon_U, then lem-compcb-corner-algebra makes A_R an extended epsilon_{A_R}-C*-algebra, lem-maincb-nested-corner-comparison makes P_U^R, P_j^R quantitative projections in A_R, and together with the lem-maincb-outer-compression-transfer outer-compressed isomorphism they satisfy every def-extcb-datum clause - approximate complementarity to I_{A_R}, one-dimensional S_{P_j^R}, nonzero S_{P_U^R,P_j^R}, and total error e = delta + epsilon_{A_R} - with e <= C_s2*t, forming the explicit Stage-2 raw-call closed EXT-CB datum in A_R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Universal ledger. Let C_nest,e_nest, e_ncd, C_out,e_out, e_sim, and C_ca,e_ca be the universal witnesses of the correspondingly named registered externals. In the fixed-source use of lem-extcb-corner-dimension-additivity below, let e_21>0 be a sufficient-accuracy threshold for the single fixed pair of source algebras C^2 and C; because this pair is fixed, e_21 is a universal numerical constant, not a threshold depending on m or |U|. Set C_delta=max{1,C_nest,C_out}, C_s2=max{1,C_delta+2*C_ca}, and e_s2=min{1/2,e_nest,e_ncd,e_out,e_sim,e_ca/2,e_21}. These are positive finite universal constants. Thus t<=e_s2 and epsilon_A<=t imply t<= every threshold used below and t+epsilon_A<=2t<=e_ca. The universal c_0^cb in the reset-state hypothesis is the coefficient supplied by lem-maincb-error-improvement; that lemma is not otherwise invoked because v_U is already an isomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Original-corner geometry. Put e_U=sum_{k in U}e_k and e_R=e_U+e_j in C^m, so by linearity P_U=w(e_U), P_R=w(e_R)=P_U+P_j. Then P_U,P_j,P_R are t-projections in A, P_R is nonvanishing, all four left/right subordination errors of P_U and P_j to P_R are at most t, A_R=S^A_{P_R}, and P_U^R=Co^A_{P_R}(P_U), P_j^R=Co^A_{P_R}(P_j) are the nested compressed elements.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Projection and nonvanishing check. The elements e_U,e_j,e_R are norm-one Hermitian projections of C^m because U and R=U union {j} are nonempty and j notin U. Unpacking the level-one part of the extended t-inclusion w gives involution preservation, ||w(xy)-w(x)w(y)||<=t||x||||y||, and (1-t)||x||<=||w(x)||<=(1+t)||x||. Hence P_U,P_j,P_R are Hermitian with idempotence defect at most t, so are t-projections by def-delta-projection. Also 1-t<=||P_R||<=1+t, so P_R satisfies the nonvanishing alternative | ||P_R||-1 |<=t<=t+epsilon_A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Subordination and notation. The coordinate identities e_Ue_R=e_Re_U=e_U and e_je_R=e_Re_j=e_j, inserted in the same t-multiplicative-defect inequality, give ||P_UP_R-P_U||, ||P_RP_U-P_U||, ||P_jP_R-P_j||, ||P_RP_j-P_j||<=t. Linearity of w gives P_R=P_U+P_j. The supplied def-maincb-partition-state defines A_R=S^A_{P_R}; defining P_U^R=Co^A_{P_R}(P_U) and P_j^R=Co^A_{P_R}(P_j) gives precisely the equalities required by the nested-corner externals. This completes the geometry node.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Target algebra and quantitative projections. Applying lem-compcb-corner-algebra to P_R gives A_R the compressed product, inherited involution and unit I_{A_R}=Co^A_{P_R}(P_R), making it an extended epsilon_{A_R}-C*-algebra for epsilon_{A_R}=C_ca*(t+epsilon_A)<=2*C_ca*t. Applying lem-maincb-nested-corner-comparison to (R,P,Q)=(P_R,P_U,P_j) gives that P_U^R and P_j^R are C_nest*t-projections in A_R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Outer-compressed diagonal isomorphism. The reset state gives v_U:M_|U|->A_U=S^A_{P_U} as an extended d_U-isomorphism, hence as an extended t-isomorphism since d_U<=t. By lem-maincb-outer-compression-transfer applied to R=P_R and P=P_U, T=Co^{A_R}_{P_U^R} o Co^A_{P_R} o v_U is an extended C_out*t-isomorphism M_|U|->S^{A_R}_{P_U^R}, with T_n=I_n tensor T for every n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Dimension clauses. One has dim S^{A_R}_{P_j^R}=1 and S^{A_R}_{P_U^R,P_j^R} is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** One-dimensional target corner. By def-one-dimensional-delta-projection, the hypothesis that P_j is one-dimensional says dim S^A_{P_j,P_j}=1. Apply lem-maincb-nested-corner-dimension-transport to (R,P,Q)=(P_R,P_j,P_j). Node 1.2 provides the t-projections, nonvanishing P_R, the repeated left/right subordination bounds, A_R=S^A_{P_R}, and P_j^R=Co^A_{P_R}(P_j); node 1.1 gives t<=e_ncd. Therefore dim S^{A_R}_{P_j^R,P_j^R}=dim S^A_{P_j,P_j}=1, i.e. dim S^{A_R}_{P_j^R}=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Nonzero target cross-corner at a fixed-source threshold. Choose k_0 in nonempty U. If U={k_0}, then P_U=P_{k_0}, and the hypothesis dim S^A_{P_{k_0},P_j}=1 directly makes S^A_{P_U,P_j} nonzero. Otherwise V=U\{k_0} is nonempty. Define exact non-unital *-monomorphisms alpha:C^2->C^m and beta:C->C^m by alpha(a,b)=a e_{k_0}+b e_V and beta(c)=c e_j. Disjoint nonempty coordinate blocks make alpha and beta completely isometric, so w o alpha and w o beta inherit at every amplification the t-homomorphism and two-sided (1+-t) bounds of w. Their units map to P_U and P_j and their projection bases map to (P_{k_0},P_V) and (P_j). Since t<=e_21, lem-extcb-corner-dimension-additivity for this fixed pair gives a linear bijection S^A_{P_U,P_j} -> S^A_{P_{k_0},P_j} direct_sum S^A_{P_V,P_j}; its first summand has dimension one, so the source is nonzero. In either case, lem-maincb-nested-corner-dimension-transport applied to (P_R,P_U,P_j), using node 1.2 and t<=e_ncd from node 1.1, gives dim S^{A_R}_{P_U^R,P_j^R}=dim S^A_{P_U,P_j}>0. Together with the preceding child this proves both dimension clauses without any variable-dimensional additivity threshold.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Exact complementarity. The compression Co^A_{P_R} is linear by def-compressed-corner. Hence P_U^R+P_j^R=Co^A_{P_R}(P_U+P_j)=Co^A_{P_R}(P_R)=I_{A_R}, so the complementarity error is zero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Final EXT-CB datum and raw-call assembly. Put delta=C_delta*t. The preceding nodes give delta-projections P_U^R,P_j^R, ||P_U^R+P_j^R-I_{A_R}||=0<=delta, the extended delta-isomorphism T:M_|U|->S^{A_R}_{P_U^R}, dim S^{A_R}_{P_j^R}=1, and S^{A_R}_{P_U^R,P_j^R} nonzero. Thus every def-extcb-datum clause holds in the extended epsilon_{A_R}-C*-algebra A_R, with e=delta+epsilon_{A_R}<=(C_delta+2*C_ca)t<=C_s2*t. Recording the Stage-2 tag, supplied U-reset state, source M_|U|, target S^{A_R}_{P_U^R}, base scale t, post-helper scale e, output T and amplifications I_n tensor T, target defect epsilon_{A_R}, and raw defect delta gives exactly the explicit def-maincb-raw-call asserted by the root.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

