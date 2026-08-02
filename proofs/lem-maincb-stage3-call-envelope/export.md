# Proof Export

## Node 1

**Statement:** After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum, there is a universal K_3^0 >= 1 with every Stage-3 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K3 >= max{K_3^0,1,W.L,W.c0_cb*W.L}, and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has disjoint nonempty unions U,V sharing no class and R=U union V, 0 <= epsilon <= W.e_cross/W.K3, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then lem-maincb-direct-corner-envelope certifies A_R with the Stage-3 raw-call target ambient record epsilon_R := W.L*epsilon, and t_3=W.K3*epsilon dominates epsilon_U,epsilon_V,d_U,d_V,epsilon_R, both displayed unit norms, and every other datum error, so lem-maincb-cross-class-merging-datum furnishes the explicit Stage-3 four-corner raw-call datum with rho <= C_cross^0*t_3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let c_old be the finite universal coefficient supplied by lem-maincb-error-improvement and choose c0:=c_old; node 1.1.1 proves c0>=0 directly, so the original conclusion remains valid without coefficient enlargement. Fix the corresponding L^0>=1 and e_env^0>0 witnesses supplied by lem-maincb-direct-corner-envelope. Retain the C_cross^0>=1 and e_cross^0>0 witnesses of lem-maincb-cross-class-merging-datum that the leading conditional setup of the root has already fixed; this node neither chooses nor proves existence of the compressed-corner-unit witnesses that precede those output witnesses in that external theorem. Define K_3^0:=max{1,e_cross^0/e_env^0}. Then K_3^0 is finite and universal, K_3^0>=1, and e_cross^0/K_3^0<=e_env^0; this absorbs the direct-envelope smallness prerequisite, while the ledger lower bounds on W.K3 absorb the remaining displayed Stage-3 scalar prerequisites.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Let c_old be the finite universal coefficient supplied by lem-maincb-error-improvement. It is necessarily nonnegative. Indeed, let epsilon_*:=epsilon_max^cb/2>0, take B=A=C with their exact C*-algebra structures, and take v=id_C with input delta=0. At every matrix amplification M_n, the exact C*-algebra M_n is an epsilon_*-C*-algebra (all zero-defect inequalities imply the corresponding inequalities at the nonnegative tolerance epsilon_*), so A is an extended epsilon_*-C*-algebra; likewise id_C is an extended 0-inclusion. Thus all hypotheses of lem-maincb-error-improvement hold (0<=epsilon_*<=epsilon_max^cb and 0<=0<=delta_max^cb), and it supplies a replacement map v_tilde:C->C which is an extended (c_old*epsilon_*)-inclusion. Applying the two-sided norm bounds in def-extended-delta-inclusion at level one to x=1 gives 1-c_old*epsilon_* <= ||v_tilde(1)|| <= 1+c_old*epsilon_*. Hence 1-c_old*epsilon_* <= 1+c_old*epsilon_*, so c_old*epsilon_*>=0; since epsilon_*>0, c_old>=0. Therefore choose c0:=c_old. No coefficient enlargement and no negative-tolerance application of lem-maincb-extended-inclusion-monotone is needed; the original error-improvement conclusion is retained verbatim.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Quantifier-scope justification: the root contract has the logical form: after c0 and the direct-envelope witnesses have been selected and after C_cross^0,e_cross^0 witnesses of a particular admissible instantiation of lem-maincb-cross-class-merging-datum have been fixed, there exists K_3^0. Thus C_cross^0,e_cross^0 are parameters of the conclusion to be proved, not quantities whose existence this proof must derive. Calling them witnesses of that external means the fixed pair carries the external conclusion for its already-instantiated antecedent; the preceding compressed-corner-unit witnesses are bound in that prior instantiation and never occur in the present conclusion or scalar argument. Accordingly node 1.1 only retains the root-fixed pair and does not invoke lem-maincb-compressed-corner-unit-comparison. If such an admissible cross-class witness pair has not been fixed, the leading setup of the conditional root has not been entered; the present lemma makes no unconditional existence assertion. With the fixed positive finite e_cross^0 and e_env^0, K_3^0=max{1,e_cross^0/e_env^0} is finite and universal, is at least 1, and satisfies e_cross^0/K_3^0<=e_env^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For arbitrary W and data satisfying the root hypotheses, set t_3:=W.K3*epsilon. Since W.K3>=1 and 0<=epsilon<=W.e_cross/W.K3, W.e_cross is nonnegative and multiplication by the positive W.K3 yields 0<=t_3<=W.e_cross<=e_cross^0; also epsilon<=t_3. Moreover W.K3>=K_3^0, W.e_cross<=e_cross^0, and K_3^0=max{1,e_cross^0/e_env^0} give epsilon<=e_cross^0/K_3^0<=e_env^0. Hence 0<=epsilon<=e_env^0 and 0<=epsilon<=t_3<=W.e_cross<=e_cross^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** With node 1.1 as an explicit dependency, put a:=e_cross^0>0, b:=e_env^0>0, K0:=K_3^0=max{1,a/b}, K:=W.K3, E:=W.e_cross, and x:=epsilon. Then K0>=1 and K0>=a/b, so K0>0 and, multiplying K0>=a/b by b/K0>0, a/K0<=b. The root hypotheses give K>=max{K0,1,W.L,W.c0_cb*W.L}, E<=a, and 0<=x<=E/K. Thus K>=1, hence K>0; from 0<=x<=E/K it follows that E>=0. Multiplication by K gives 0<=K*x=t_3<=E<=a, and (K-1)*x>=0 gives x<=K*x=t_3. Finally K>=K0>0 and 0<=E<=a imply x<=E/K<=a/K<=a/K0<=b. Therefore 0<=epsilon<=e_env^0 and 0<=epsilon<=t_3<=W.e_cross<=e_cross^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Apply lem-maincb-direct-corner-envelope to the same displayed A,w and the nonempty sets U,V,R. It gives A_R as an extended L^0*epsilon-C*-algebra, every relevant projection P_U,P_V,P_R the separate c0*epsilon projection bound, and every subordination and complementarity error for U subseteq R (with R minus U=V) at most L^0*epsilon. Enlarging only the ambient tolerance from L^0*epsilon to epsilon_R:=W.L*epsilon using the defining inequalities of def-epsilon-cstar-algebra and def-extended-epsilon-cstar-algebra certifies the literal Stage-3 target A_R as an extended epsilon_R-C*-algebra; the projection scale c0*epsilon remains separate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Because U and V are nonempty and disjoint and R=U union V, R is nonempty, U subseteq R, and R minus U=V. The smallness arithmetic gives 0<=epsilon<=e_env^0. The root supplies the same finite-dimensional extended epsilon-C*-algebra A and the same extended c0*epsilon-inclusion w. Thus lem-maincb-direct-corner-envelope gives P_U,P_V,P_R as c0*epsilon-projections, A_R as an extended L^0*epsilon-C*-algebra, and every stated subordination and complementarity error among P_U,P_V,P_R at most L^0*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Import the scalar conclusion through the explicit dependency on node 1.2: after the universal choices, K_3^0=max{1,e_cross^0/e_env^0}, and for the present root datum node 1.2 proves 0<=epsilon<=e_env^0. This child is not eligible for acceptance until node 1.2 is validated. The root also gives W.c0_cb=c0, so its supplied extended W.c0_cb*epsilon-inclusion w is exactly an extended c0*epsilon-inclusion into the same finite-dimensional extended epsilon-C*-algebra A. Since U and V are nonempty and disjoint with R=U union V, R is nonempty, U subseteq R, and R minus U=V. Therefore all hypotheses of lem-maincb-direct-corner-envelope hold: it yields P_U, P_V, and P_R as c0*epsilon-projections, A_R as an extended L^0*epsilon-C*-algebra, and the asserted subordination and complementarity errors among P_U, P_V, and P_R bounded by L^0*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Set epsilon_R:=W.L*epsilon. Since W.L>=L^0 and epsilon>=0, 0<=L^0*epsilon<=epsilon_R. Every product-norm, associativity, approximate-unit, and upper-error inequality in def-epsilon-cstar-algebra that holds with tolerance L^0*epsilon also holds with epsilon_R; the lower C*-inequality remains valid because 1-epsilon_R<=1-L^0*epsilon; exact involution and any exact-unit clauses are unchanged. Applying this at every amplification as required by def-extended-epsilon-cstar-algebra shows A_R is an extended epsilon_R-C*-algebra. Also L^0*epsilon<=epsilon_R forwards every direct-envelope subordination and complementarity error to the recorded target scale, while the c0*epsilon projection bounds are retained at their own scale rather than silently replaced.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** All scalar prerequisite errors are at most t_3. Namely epsilon_U,epsilon_V<=W.L*epsilon<=t_3; d_U<=c0*epsilon_U<=c0*W.L*epsilon<=t_3 and similarly for d_V; each displayed reset unit norm is <=c0*epsilon_U or <=c0*epsilon_V and hence <=t_3; epsilon_R=W.L*epsilon<=t_3; and the direct-envelope bounds L^0*epsilon and c0*epsilon, together with the supplied global unit error ||w(I)-I_A||<=c0*epsilon, are <=t_3. This uses only c0>=0, epsilon>=0, W.L>=L^0>=1, and W.K3>=max{1,W.L,c0*W.L}; no assumption c0>=1 is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The chosen error-improvement coefficient c0 is necessarily nonnegative. Let epsilon_*:=min{epsilon_max^cb/2,1/2}>0, take B=A=C with their usual exact C*-algebra structures, and take v=id_C with delta=0. Exact matrix algebras M_n(C) satisfy every epsilon_*-C*-algebra inequality, so A is an extended epsilon_*-C*-algebra; id_C is an extended 0-isomorphism; and 0<=epsilon_*<=epsilon_max^cb and 0<=0<=delta_max^cb. Applying lem-maincb-error-improvement with the fixed witness c0 produces an extended c0*epsilon_*-inclusion v_tilde:C->C (indeed bijective). At amplification n=1, the two-sided (1 plus/minus c0*epsilon_*) norm bounds from def-extended-delta-inclusion, evaluated at 1 in C, give 1-c0*epsilon_* <= ||v_tilde(1)|| <= 1+c0*epsilon_*. Hence 2*c0*epsilon_*>=0. Since epsilon_*>0, c0>=0. Thus no enlargement from a negative coefficient and no appeal to pending sibling 1.1 is needed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Using c0>=0 from the preceding child and W.c0_cb=c0, all asserted scalar chains follow directly. Since epsilon>=0, W.L>=L^0>=1, and W.K3>=max{1,W.L,c0*W.L}, multiplication by epsilon gives L^0*epsilon<=W.L*epsilon<=t_3:=W.K3*epsilon and c0*epsilon<=c0*W.L*epsilon<=t_3. Multiplying epsilon_U,epsilon_V<=W.L*epsilon by c0>=0 gives c0*epsilon_U,c0*epsilon_V<=c0*W.L*epsilon<=t_3. The root hypotheses then give d_U,d_V and the two displayed reset-unit norms at most t_3. Also epsilon_R=W.L*epsilon<=t_3. The direct-envelope L^0*epsilon errors, its separate c0*epsilon projection errors, and the supplied global unit error bounded by c0*epsilon are therefore all at most t_3.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The same w is the non-unital extended t_3-inclusion required by lem-maincb-cross-class-merging-datum. Indeed 0<=c0*epsilon<=c0*W.L*epsilon<=W.K3*epsilon=t_3. Since C^m is a finite-dimensional C*-algebra and the displayed A is the same finite-dimensional extended epsilon-C*-algebra, lem-maincb-extended-inclusion-monotone applied to B=C^m, v=w, delta=c0*epsilon and delta_prime=t_3 promotes the supplied extended c0*epsilon-inclusion to an extended t_3-inclusion. Here non-unital means no exact unitality is assumed; the separate supplied unit estimate is merely bounded by t_3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** With t=t_3, every hypothesis of lem-maincb-cross-class-merging-datum is now met: W.c0_cb=c0 and W.e_cross<=e_cross^0; A has ambient epsilon<=t_3; the same partition state comes from the extended t_3-inclusion w with one-dimensional images; U,V are disjoint nonempty unions sharing no class and R=U union V; the supplied current reset maps are the stated isomorphisms; and epsilon_U,epsilon_V,d_U,d_V, both unit errors are <=t_3<=W.e_cross with d_U<=c0*epsilon_U and d_V<=c0*epsilon_V. Therefore that external furnishes in A_R the explicit Stage-3 amplified four-corner datum with common defect rho<=C_cross^0*t_3. Independently, lem-maincb-direct-corner-envelope certifies the same target corner and the enlarged ambient record epsilon_R:=W.L*epsilon, and the preceding scalar bounds show t_3 dominates epsilon_U,epsilon_V,d_U,d_V,epsilon_R and every supplied or direct-envelope datum error. This four-corner datum is the input datum for the Stage-3 raw call; consistently with def-maincb-raw-call, it is not mislabeled as the raw-call record output map, which must be the downstream derived level-one map and its fixed amplifications.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** The fixed error-improvement coefficient c0 is nonnegative, and the Stage-3 scalar smallness bounds follow without using any sibling. Indeed let eta=epsilon_max^cb/2>0, take B=A=C with its exact C*-algebra structure (hence an extended eta-C*-algebra at every matrix level), and take v=id_C, an extended 0-isomorphism. The hypotheses of lem-maincb-error-improvement hold because 0<=eta<=epsilon_max^cb and 0<=0<=delta_max^cb, so it supplies a bijective extended (c0*eta)-inclusion v_tilde:C->C. At amplification n=1 and x=1, the two-sided norm bounds in def-extended-delta-inclusion give (1-c0*eta)||1|| <= ||v_tilde(1)|| <= (1+c0*eta)||1||. If c0*eta<0 the left endpoint is strictly larger than the right endpoint, impossible; hence c0*eta>=0 and, since eta>0, c0>=0. Now define K_3^0=max{1,e_cross^0/e_env^0}. It is universal, finite, at least 1, and e_cross^0/K_3^0<=e_env^0. For root data put t_3=W.K3*epsilon. Since W.K3>=1 and epsilon>=0, W.K3>0 and epsilon<=t_3. From epsilon<=W.e_cross/W.K3 one gets 0<=t_3<=W.e_cross<=e_cross^0. Also W.K3>=K_3^0 and W.e_cross<=e_cross^0 give epsilon<=e_cross^0/K_3^0<=e_env^0. Thus 0<=epsilon<=e_env^0 and epsilon<=t_3<=W.e_cross<=e_cross^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** Using the bounds just proved, apply lem-maincb-direct-corner-envelope directly to the displayed A,w and the nonempty R=U union V (and to U subseteq R, whose complement in R is V). It yields P_U,P_V,P_R as c0*epsilon-projections, A_R as an extended L^0*epsilon-C*-algebra, and all stated subordination and complementarity errors at most L^0*epsilon. Set epsilon_R=W.L*epsilon. Since W.L>=L^0 and epsilon>=0, L^0*epsilon<=epsilon_R. Clause by clause in def-epsilon-cstar-algebra, increasing a nonnegative tolerance preserves the product-norm, associativity, approximate-unit, and upper-error bounds, weakens the lower C*-bound, and leaves the exact involution and exact-unit clauses unchanged. Applying this at every matrix amplification as required by def-extended-epsilon-cstar-algebra proves that this same A_R is an extended epsilon_R-C*-algebra and forwards the L^0*epsilon errors to epsilon_R, while retaining the distinct c0*epsilon projection scale.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.3

**Statement:** All hypotheses of lem-maincb-cross-class-merging-datum can now be checked from the root data and the first child, without any pending sibling. Since c0>=0, W.L>=1, epsilon>=0, and W.K3>=c0*W.L, one has 0<=c0*epsilon<=c0*W.L*epsilon<=t_3. Hence lem-maincb-extended-inclusion-monotone, with B=C^m, v=w, delta=c0*epsilon and delta_prime=t_3, promotes the supplied extended c0*epsilon-inclusion to an extended t_3-inclusion. Further, epsilon_U,epsilon_V<=W.L*epsilon<=t_3; and d_U and the U-unit norm are each <=c0*epsilon_U<=c0*W.L*epsilon<=t_3, with the identical argument for V. The original inequalities d_U<=c0*epsilon_U and d_V<=c0*epsilon_V are retained. Together with epsilon<=t_3<=W.e_cross, W.c0_cb=c0, W.e_cross<=e_cross^0, the one-dimensional images, the stated disjoint nonempty class unions and R=U union V, and the supplied reset isomorphisms, these are exactly the hypotheses of lem-maincb-cross-class-merging-datum at t=t_3. It therefore furnishes in A_R the explicit Stage-3 amplified four-corner datum with rho<=C_cross^0*t_3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.4

**Statement:** The complete Stage-3 envelope follows from the three preceding children. Besides the reset quantities already bounded there, epsilon_R=W.L*epsilon<=t_3 because W.K3>=W.L; each direct-envelope L^0*epsilon error is <=epsilon_R<=t_3; and each c0*epsilon projection error and the supplied global unit error are <=c0*W.L*epsilon<=t_3. Thus t_3 dominates every displayed supplied or direct-envelope datum error while the cross-class external supplies rho<=C_cross^0*t_3. The amplified four-corner datum is the input datum for the Stage-3 raw call. Under def-maincb-raw-call it is not itself asserted to be the raw-call record output: that record separately stores the downstream literal output level-one map, its fixed amplifications, target, and scales.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

