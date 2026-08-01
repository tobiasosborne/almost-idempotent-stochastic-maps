# Proof Export

## Node 1

**Statement:** After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_s2^0,e_s2^0 witnesses of lem-maincb-stage2-extcb-datum, there is a universal K_2^0 >= 1 with every Stage-2 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K2 >= max{K_2^0,1,W.L,W.c0_cb*W.L}, and W.e_s2 <= e_s2^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has nonempty U contained in one equivalence class, j notin U in that same class, and R=U union {j}, 0 <= epsilon <= W.e_s2/W.K2, and a supplied current reset isomorphism v_U:M_{|U|}->A_U has recorded ambient field epsilon_U <= W.L*epsilon and satisfies d_U <= W.c0_cb*epsilon_U and ||v_U(I_{M_{|U|}})-u_{A_U}|| <= W.c0_cb*epsilon_U, then lem-maincb-direct-corner-envelope certifies A_R with the Stage-2 raw-call target ambient record epsilon_R := W.L*epsilon, and t_2=W.K2*epsilon dominates epsilon_U,d_U,epsilon_R, the reset unit error, and every other datum error, so lem-maincb-stage2-extcb-datum furnishes the explicit Stage-2 EXT raw-call datum with total defect at most C_s2^0*t_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose a finite nonnegative universal coefficient c0 for which lem-maincb-error-improvement remains valid (an original finite error coefficient may be enlarged to a nonnegative one, with lem-maincb-extended-inclusion-monotone preserving the resulting inclusion conclusion). Then fix corresponding witnesses L^0 >= 1 and e_env^0 > 0 from lem-maincb-direct-corner-envelope and C_s2^0 >= 1 and e_s2^0 > 0 from lem-maincb-stage2-extcb-datum. Set K_2^0 := max{1,e_s2^0/e_env^0}. Then K_2^0 is finite and universal, K_2^0 >= 1, and e_s2^0/K_2^0 <= e_env^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** With K_2^0=max{1,e_s2^0/e_env^0}, take any ledger W and data satisfying the root hypotheses and put t_2:=W.K2*epsilon. Since W.K2>=1 and 0<=epsilon<=W.e_s2/W.K2, necessarily W.e_s2>=0 and multiplication by W.K2 gives 0<=t_2<=W.e_s2<=e_s2^0. Also epsilon<=t_2. Finally W.K2>=K_2^0 and W.e_s2<=e_s2^0 give epsilon<=e_s2^0/K_2^0<=e_env^0. Thus 0<=epsilon<=e_env^0 and 0<=epsilon<=t_2<=W.e_s2<=e_s2^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Apply lem-maincb-direct-corner-envelope to the same displayed A,w and the nonempty sets U and R. It gives A_R as an extended L^0*epsilon-C*-algebra, gives each relevant projection defect at most c0*epsilon, and bounds every subordination and complementarity error needed for U subseteq R by L^0*epsilon. Since W.L >= L^0 and epsilon >= 0, the defining inequalities of def-epsilon-cstar-algebra at every amplification remain valid with the larger tolerance epsilon_R:=W.L*epsilon; hence this is a certificate that the literal Stage-2 target A_R is an extended epsilon_R-C*-algebra, with all subordination and complementarity errors at most epsilon_R while projection defects retain their separate c0*epsilon bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Because U is nonempty, R=U union {j} is nonempty and U subseteq R. From 0<=epsilon<=W.e_s2/W.K2, W.e_s2<=e_s2^0, W.K2>=K_2^0=max{1,e_s2^0/e_env^0}, and W.K2>=1, one obtains epsilon<=e_env^0. The root supplies the same finite-dimensional extended epsilon-C*-algebra A and the same extended c0*epsilon-inclusion w. Thus lem-maincb-direct-corner-envelope gives P_U,P_{R minus U},P_R as c0*epsilon-projections, A_R as an extended L^0*epsilon-C*-algebra, and every stated subordination and complementarity error for U subseteq R at most L^0*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Under the root hypotheses, the smallness calculation 0<=epsilon<=e_env^0 and lem-maincb-direct-corner-envelope first certify the literal A_R as an extended L^0*epsilon-C*-algebra. Set epsilon_R:=W.L*epsilon. Since 0<=L^0*epsilon<=epsilon_R, each upper-error inequality in def-epsilon-cstar-algebra valid with tolerance L^0*epsilon remains valid with epsilon_R, while the lower C*-inequality remains valid because 1-epsilon_R<=1-L^0*epsilon; all exact algebraic and involution clauses are unchanged, and the same reasoning applies at every amplification in def-extended-epsilon-cstar-algebra. Hence A_R is an extended epsilon_R-C*-algebra. Moreover L^0*epsilon<=epsilon_R, so every direct-envelope subordination and complementarity error is at most epsilon_R. The separate c0*epsilon projection-defect bounds are not compared with epsilon_R here.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For the chosen nonnegative c0 and t_2=W.K2*epsilon, all scalar datum errors are at most t_2. Indeed epsilon_U<=W.L*epsilon<=t_2; d_U<=c0*epsilon_U<=c0*W.L*epsilon<=t_2; ||v_U(I)-u_{A_U}||<=c0*epsilon_U<=t_2; and epsilon_R=W.L*epsilon<=t_2. The direct-envelope bounds L^0*epsilon and c0*epsilon, and the supplied error ||w(I)-I_A||<=c0*epsilon, are also at most t_2. These inequalities use only W.K2>=max{1,W.L,c0*W.L}, W.L>=L^0>=1, c0>=0, and epsilon>=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For the same displayed w, the supplied inclusion tolerance is nonnegative and c0*epsilon<=c0*W.L*epsilon<=W.K2*epsilon=t_2, using c0>=0, epsilon>=0, W.L>=1, and W.K2>=c0*W.L. Applying lem-maincb-extended-inclusion-monotone with B=C^m, v=w, delta=c0*epsilon, and delta_prime=t_2 proves that this same w is the non-unital extended t_2-inclusion required by lem-maincb-stage2-extcb-datum. No unitality is inferred; separately, the root unit estimate obeys ||w(I)-I_A||<=c0*epsilon<=t_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** By def-maincb-partition-state, P_k=w(e_k) and k~j iff dim S^A_{P_k,P_j}=1. Because U is nonempty and U together with j lies in one equivalence class while j is not in U, every k in U satisfies k~j, so dim S^A_{P_k,P_j}=1, and R=U union {j}; the root hypothesis that the same w has one-dimensional atomic images supplies the remaining one-dimensional-image clauses.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Set t_2=W.K2*epsilon. The root inequalities give 0<=epsilon<=t_2<=W.e_s2<=e_s2^0, epsilon_U<=t_2, d_U<=c0*epsilon_U<=t_2, and the reset unit error at most t_2. They also give 0<=c0*epsilon<=t_2, so lem-maincb-extended-inclusion-monotone makes the same w an extended t_2-inclusion. By def-maincb-partition-state, same-class membership gives dim S^A_{P_k,P_j}=1 for every k in U, while the root supplies the one-dimensional images, nonempty U, j notin U, R=U union {j}, and the current reset extended isomorphism. Therefore every hypothesis of lem-maincb-stage2-extcb-datum holds with t=t_2 and its fixed witnesses C_s2^0,e_s2^0. That external furnishes the explicit Stage-2 raw-call closed EXT-CB datum in A_R with total defect e<=C_s2^0*t_2. Independently, lem-maincb-direct-corner-envelope at epsilon<=e_env^0 certifies the same literal target A_R, and monotonicity of the defining epsilon-C*-inequalities records its ambient field as epsilon_R:=W.L*epsilon. These conclusions are exactly the asserted raw-call output and target record.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

