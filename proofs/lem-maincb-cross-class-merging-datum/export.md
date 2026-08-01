# Proof Export

## Node 1

**Statement:** After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, and fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, there are universal C_cross^0 >= 1 and 0 < e_cross^0 <= e_corner_unit such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0 and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has disjoint nonempty unions U,V sharing no class and R=U union V, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy epsilon_U,epsilon_V,d_U,d_V <= t <= W.e_cross, d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= t, and ||v_V(I_{B_V})-u_{A_V}|| <= t, then lem-maincb-compressed-corner-unit-comparison and the nested-corner, outer-compression, and zero-cross-corner constructions form the explicit Stage-3 amplified four-corner datum in A_R with common defect rho <= C_cross^0*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Provider and smallness ledger. Choose the universal c0 furnished by lem-maincb-error-improvement, then fix the corresponding L,e_env furnished by lem-maincb-direct-corner-envelope, and fix C_corner_unit,e_corner_unit furnished by lem-maincb-compressed-corner-unit-comparison. Also denote by C_nest,e_nest, C_out,e_out, e_zero, C_ca,e_ca, e_cmp_amp, and e_cmp_id the universal witnesses furnished by lem-maincb-nested-corner-comparison, lem-maincb-outer-compression-transfer, lem-maincb-cross-union-zero-corners, lem-compcb-corner-algebra, lem-compcb-amplified-compression, and lem-compcb-amplified-compression-identities. Enlarge the defect coefficients to be at least 1. Set K_target=C_nest+2*C_ca and C_cross^0=max{1,C_nest,C_out,C_corner_unit,2*C_ca}. Choose e_cross^0>0 no larger than e_corner_unit,e_env,e_nest,e_out,e_zero,e_ca/2,e_cmp_amp/2,e_cmp_id/2,e_cmp_amp/K_target,e_cmp_id/K_target, and 1/2. These are positive finite universal choices and 0<e_cross^0<=e_corner_unit.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Original ambient geometry. Under the root hypotheses, t<=W.e_cross<=e_cross^0. In C^m write e_U=sum_{j in U}e_j, e_V=sum_{j in V}e_j, and e_R=e_U+e_V. Disjoint nonempty U,V make these nonzero norm-one self-adjoint projections with e_U e_R=e_R e_U=e_U and e_V e_R=e_R e_V=e_V. By the partition-state identities and linearity, w(e_X)=P_X for X=U,V,R and P_R=P_U+P_V. At level one the extended t-inclusion w makes P_U,P_V,P_R t-projections and gives all four left/right subordination errors of P_U,P_V to P_R at most t. Its lower norm bound gives ||P_R||>=1-t>=1/2, so P_R is nonvanishing. Since epsilon_A<=t, A may be regarded as an extended t-C*-algebra. Thus the geometric hypotheses of lem-maincb-nested-corner-comparison and lem-maincb-outer-compression-transfer hold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Two-sided norm control establishes the required nonvanishing alternative. At amplification n=1, the two-sided norm bounds in the extended t-inclusion w apply to e_R. Since ||e_R||=1 and w(e_R)=P_R, they give 1-t <= ||P_R|| <= 1+t. Therefore | ||P_R||-1 | <= t <= t+epsilon_A. Together with the already established fact that P_R is a t-projection, this verifies the second alternative in def-delta-projection with explicit universal O-coefficient 1; hence P_R is nonvanishing. Consequently the nonvanishing hypothesis required by lem-maincb-nested-corner-comparison and lem-maincb-outer-compression-transfer is satisfied.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Target corner and target projections. Apply lem-compcb-corner-algebra to the nonvanishing t-projection P_R: epsilon_A+t<=2t<=e_ca, so A_R=S^A_{P_R}, with compressed product and unit u_R=Co^A_{P_R}(P_R), is an extended 2*C_ca*t-C*-algebra. Apply lem-maincb-nested-corner-comparison to (R,P,Q)=(P_R,P_U,P_V). It gives P_U^R=Co^A_{P_R}(P_U) and P_V^R=Co^A_{P_R}(P_V) as C_nest*t-projections in A_R. Hence the target ambient defect and both target projection defects are at most C_cross^0*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Explicit diagonal transports. Each reset tag says v_X:B_X->A_X=S^A_{P_X} is an extended d_X-isomorphism for X=U,V, with its fixed amplifications. Because 0<=d_X<=t, weakening its defect bounds makes v_X an extended t-isomorphism. Apply lem-maincb-outer-compression-transfer for (R,P,v)=(P_R,P_X,v_X). This produces the explicit fixed level-one map T_X=Co^{A_R}_{P_X^R} o Co^A_{P_R} o v_X:B_X->S^{A_R}_{P_X^R}, an extended C_out*t-isomorphism, and proves T_X,n=I_n tensor T_X for every n. Thus involution compatibility, compressed-product compatibility, and two-sided norm control for each diagonal map have defect at most C_out*t<=C_cross^0*t at every amplification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Diagonal-unit clauses. For X=U,V, the hypotheses just used are exactly those of lem-maincb-outer-compression-transfer, t<=e_cross^0<=e_corner_unit, and the root gives ||v_X(I_{B_X})-u_{A_X}||<=t. The second clause of lem-maincb-compressed-corner-unit-comparison therefore applies to the same explicit map T_X and gives ||T_X,n(I_n tensor I_{B_X})-I_n tensor P_X^R||<=C_corner_unit*t<=C_cross^0*t for every n>=1. These are precisely the two diagonal-unit estimates required by def-four-corner-merging-datum; no identification of P_X^R with its compressed-corner unit is made.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Zero off-diagonal transports. By lem-maincb-cross-union-zero-corners, t<=e_zero and the displayed partition hypotheses give S^A_{P_U,P_V}=S^A_{P_V,P_U}=0 and S^{A_R}_{P_U^R,P_V^R}=S^{A_R}_{P_V^R,P_U^R}=0. In each direction choose the unique level-one zero map 0->0. For the original corners delta+epsilon_A<=2t, and for the target corners delta+epsilon_target<=(C_nest+2*C_ca)*t=K_target*t; the choice of e_cross^0 permits lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities in both ambients. Hence every amplified source and target cross-corner is again zero, the amplification of each chosen map is the unique zero map, dagger exchanges the two directions, and all involution, product, unit-relevant, and norm estimates involving an off-diagonal input hold exactly.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Complementary source and target projections. In B=B_U direct-sum B_V put Pi_U=(I_{B_U},0) and Pi_V=(0,I_{B_V}); they are complementary source projections and their cross-corners vanish. In A_R, linearity of Co^A_{P_R}, P_R=P_U+P_V, and the corner-unit identity from lem-compcb-corner-algebra give P_U^R+P_V^R=Co^A_{P_R}(P_U+P_V)=Co^A_{P_R}(P_R)=u_R=I_{A_R}. Thus target complementarity has error zero, while both target projections are C_nest*t-projections, so all projection and complementarity requirements are bounded by C_cross^0*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Verification of the amplified four-corner datum. Define gamma_UU=T_U, gamma_VV=T_V, and gamma_UV,gamma_VU to be the two fixed zero maps, always amplified as I_n tensor gamma_XY. The diagonal transport result supplies involution, compressed-product, and two-sided norm control; the diagonal-unit result supplies approximation to P_U^R,P_V^R; the zero-corner result makes every clause containing an off-diagonal source element exact; and the complementarity result supplies the source and target projection clauses. Therefore the same four level-one maps at every amplification satisfy every field of def-four-corner-merging-datum with one common defect rho=C_cross^0*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Quantifiers and conclusion. The constants C_cross^0,e_cross^0 were selected only from the previously fixed universal provider witnesses, so they are universal and independent of W, all dimensions, amplification levels, the partition, and the block algebras. For every ledger W with W.c0_cb=c0 and W.e_cross<=e_cross^0, the assumption t<=W.e_cross activates every threshold above. The unused reset inequalities d_U<=W.c0_cb*epsilon_U and d_V<=W.c0_cb*epsilon_V remain valid ledger invariants, while d_U,d_V<=t are the bounds needed for the transports. The explicit nested projections, outer-compressed diagonal maps, unique zero cross-corner maps, and compressed-corner unit comparison therefore form the asserted Stage-3 amplified four-corner datum in A_R, with rho=C_cross^0*t<=C_cross^0*t, proving node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

