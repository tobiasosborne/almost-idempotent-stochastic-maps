# Proof Export

## Node 1

**Statement:** After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_s2^0,e_s2^0 witnesses of lem-maincb-stage2-extcb-datum, there is a universal K_2^0 >= 1 with every Stage-2 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K2 >= max{K_2^0,1,W.L,W.c0_cb*W.L}, and W.e_s2 <= e_s2^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has nonempty U contained in one equivalence class, j notin U in that same class, and R=U union {j}, 0 <= epsilon <= W.e_s2/W.K2, and a supplied current reset isomorphism v_U:M_{|U|}->A_U has recorded ambient field epsilon_U <= W.L*epsilon and satisfies d_U <= W.c0_cb*epsilon_U and ||v_U(I_{M_{|U|}})-u_{A_U}|| <= W.c0_cb*epsilon_U, then lem-maincb-direct-corner-envelope certifies A_R with the Stage-2 raw-call target ambient record epsilon_R := W.L*epsilon, and t_2=W.K2*epsilon dominates epsilon_U,d_U,epsilon_R, the reset unit error, and every other datum error, so lem-maincb-stage2-extcb-datum furnishes the explicit Stage-2 EXT raw-call datum with total defect at most C_s2^0*t_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose the universal c0 furnished by lem-maincb-error-improvement, then fix the corresponding witnesses L^0>=1 and e_env^0>0 from lem-maincb-direct-corner-envelope and C_s2^0>=1 and e_s2^0>0 from lem-maincb-stage2-extcb-datum. Define K_2^0:=max{1,e_s2^0/e_env^0}; this is universal, finite, at least 1, and satisfies e_s2^0/K_2^0<=e_env^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For arbitrary W and data satisfying the root hypotheses, put t_2:=W.K2*epsilon. Then 0<=t_2<=W.e_s2<=e_s2^0, epsilon<=e_env^0, and each of epsilon, W.L*epsilon, and W.c0_cb*W.L*epsilon is at most t_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Because W.K2>=1 and epsilon>=0, t_2=W.K2*epsilon is nonnegative; multiplying epsilon<=W.e_s2/W.K2 by the positive W.K2 gives t_2<=W.e_s2<=e_s2^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Using W.K2>=K_2^0, W.e_s2<=e_s2^0, and K_2^0=max{1,e_s2^0/e_env^0}, the same upper bound gives epsilon<=W.e_s2/W.K2<=e_s2^0/K_2^0<=e_env^0. Multiplying W.K2>=1, W.K2>=W.L, and W.K2>=W.c0_cb*W.L by epsilon>=0 gives respectively epsilon<=t_2, W.L*epsilon<=t_2, and W.c0_cb*W.L*epsilon<=t_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The hypotheses of lem-maincb-direct-corner-envelope hold for the displayed A,w and the nonempty sets U and R. Applying it gives A_R as an extended L^0*epsilon-C*-algebra; P_U, P_{R minus U}=P_j, and P_R as c0*epsilon-projections; and every stated subordination and complementarity error among them at most L^0*epsilon. Since W.L>=L^0, record the monotone upper ambient parameter epsilon_R:=W.L*epsilon: A_R is an extended epsilon_R-C*-algebra and the subordination and complementarity errors are at most epsilon_R<=t_2. The projection defects are not asserted to be at most epsilon_R; instead they are bounded separately by c0*epsilon<=W.c0_cb*W.L*epsilon<=t_2. Thus every direct-corner datum error required for the Stage-2 call is at most t_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For the separate projection bound, c0=W.c0_cb and the projection-defect parameter c0*epsilon is nonnegative. Because W.L>=L^0>=1 and epsilon>=0, c0*epsilon<=W.c0_cb*W.L*epsilon; node 1.2 gives W.c0_cb*W.L*epsilon<=t_2. In contrast, the L^0*epsilon envelope applies only to the ambient, subordination, and complementarity errors, for which L^0*epsilon<=W.L*epsilon=epsilon_R<=t_2.

**Type:** claim

**Inference:** monotonicity

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The supplied reset and incoming map meet all analytic input bounds for lem-maincb-stage2-extcb-datum at t=t_2: epsilon_U<=W.L*epsilon<=t_2; d_U<=W.c0_cb*epsilon_U<=W.c0_cb*W.L*epsilon<=t_2; the reset unit error obeys the same bound and is carried as an invariant (not used to manufacture any EXT clause); A has epsilon<=t_2; and w, originally an extended W.c0_cb*epsilon-inclusion, is also a non-unital extended t_2-inclusion because W.c0_cb*epsilon<=t_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The partition geometry meets the remaining hypotheses of lem-maincb-stage2-extcb-datum: U is nonempty, j is not in U, R=U union {j}, all atomic images P_k are one-dimensional, and because U and j lie in the same equivalence class, def-maincb-partition-state gives dim S^A_{P_k,P_j}=1 for every k in U, hence in particular the required cross-corner is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Apply lem-maincb-stage2-extcb-datum to the original ambient A, the partition state, w, U,j,R, and reset v_U with t=t_2. The preceding bounds give epsilon_U,d_U<=t_2<=e_s2^0 and d_U<=c0*epsilon_U, while the geometry gives every remaining premise. Therefore it furnishes in A_R the explicit closed def-extcb-datum, packaged as the Stage-2 def-maincb-raw-call with target ambient record epsilon_R=W.L*epsilon, and its total defect is at most C_s2^0*t_2; together with the direct-corner and carried-unit bounds this is exactly the root conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** By nodes 1.1-1.5, every hypothesis of lem-maincb-stage2-extcb-datum holds with its ambient variable equal to the original A and t=t_2: smallness and domination are supplied by 1.2 and 1.4, the required partition and corner dimensions by 1.5, and the selected A_R ambient record plus all direct-corner errors by 1.3. Invoke lem-maincb-stage2-extcb-datum exactly once. Its conclusion is the explicit Stage-2 raw-call closed def-extcb-datum in A_R with total defect at most C_s2^0*t_2; retaining epsilon_R=W.L*epsilon and the separately carried reset-unit bound yields precisely node 1.6.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.6.1.1

**Statement:** Keep the two ambient-defect records distinct. The invocation of lem-maincb-stage2-extcb-datum produces an extended epsilon_{A_R}-C*-algebra A_R and a closed EXT-CB datum whose own total error is e_EXT=delta+epsilon_{A_R}<=C_s2^0*t_2. Independently, node 1.3 supplies the number epsilon_R=W.L*epsilon as the target-ambient-defect field of the enclosing def-maincb-raw-call and proves that A_R is also an extended epsilon_R-C*-algebra, with epsilon_R<=t_2. By def-maincb-raw-call, that recorded target field is part of the literal-call record; the definition does not identify it with the epsilon occurring in an enclosed def-extcb-datum or redefine the datum's total error. Thus package the unchanged Stage-2 closed datum (using epsilon_{A_R} and retaining e_EXT<=C_s2^0*t_2) inside the raw-call record whose separate target field is epsilon_R. No substitution epsilon_{A_R}:=epsilon_R and no estimate delta+epsilon_R<=C_s2^0*t_2 is asserted or needed; the reset-unit bound is likewise only separately carried.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

