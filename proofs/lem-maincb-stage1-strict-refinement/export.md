# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN and an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfies ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon and has some P_j=w(e_j) with dim S_{P_j}>1, then there is an extended W.c0_cb*epsilon-inclusion w_+:C^{m+1}->A satisfying ||w_+(I_{C^{m+1}})-I_A|| <= W.c0_cb*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix all universal witnesses in the dependency order, choosing the reset-threshold witnesses C_unit, epsilon_unit, delta_unit, a_unit once from lem-maincb-reset-output-typing and using those same witnesses in lem-maincb-reset-constant-ledger; then fix the single ledger datum W named in the contract and D_* from that ledger. These compatible choices have D_* >= 1, W.c0_cb equal to the enlarged c0, W.K1 >= K_1^0 >= 1, W.e1 <= e_1, and the W.r_reset threshold inequalities required by lem-maincb-reset-output-typing.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** After the preliminary universal witnesses named in the allowed externals have been fixed, invoke lem-maincb-reset-output-typing once and fix one particular tuple (C_unit,epsilon_unit,delta_unit,a_unit) from its leading existential; these values are positive and are the witnesses furnished by the same third clause and implicit quantifier convention named in lem-maincb-reset-constant-ledger. Also invoke lem-maincb-stage1-call-envelope once and fix its particular compatible witnesses K_1^0,D_1,e_1, with K_1^0>=1, after the preceding envelope choices.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Instantiate lem-maincb-reset-constant-ledger with exactly the witnesses fixed above, in particular the same C_unit,epsilon_unit,delta_unit,a_unit and the same Stage-1 envelope witnesses; choose its valid enlarged c0 and fix its one furnished datum W and D_*=max{1,D_0,D_1,D_2,D_3}. The external gives W.c0_cb=c0, W.K1>=K_1^0, W.e1<=e_1, and eligibility of its Stage-1 literal call for the reset thresholds. Hence D_*>=1 and W.K1>=K_1^0>=1; because the reset-threshold witnesses are the identical ones fixed from lem-maincb-reset-output-typing, that eligibility supplies precisely the W.c0_cb and W.r_reset scalar antecedents of that typed-reset lemma.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** By validated node 1.1.1, fix its one particular positive tuple (C_unit,epsilon_unit,delta_unit,a_unit) furnished by the leading existential of lem-maincb-reset-output-typing and its one particular Stage-1 tuple (K_1^0,D_1,e_1) with K_1^0 >= 1. Instantiate lem-maincb-reset-constant-ledger with these exact fixed values (together with the preceding universal witnesses required by that external), not with a second existential choice. Fix the resulting valid enlarged c0, the single furnished datum W, and D_*=max{1,D_0,D_1,D_2,D_3}. The ledger conclusion gives W.c0_cb=c0, W.K1>=K_1^0, W.e1<=e_1, D_*>=1, and Stage-1 eligibility for the reset thresholds. Therefore W.K1>=1; moreover, because the ledger invocation used literally the same reset-output tuple fixed in 1.1.1, its stated eligibility supplies the W.c0_cb lower bound and W.r_reset upper bounds for those same C_unit,epsilon_unit,delta_unit,a_unit in lem-maincb-reset-output-typing. No pending sibling or independently re-chosen existential witness is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the fixed W and any 0 <= epsilon <= W.epsilon_MAIN, put t_1=W.K1*epsilon. By lem-maincb-structural-domain-ledger, epsilon <= W.e1/W.K1 and 0 <= t_1 <= W.K_call*epsilon <= W.r_reset. Moreover W.K1 >= K_1^0 >= 1, so epsilon <= t_1. Thus both the Stage-1 producer and the global-target reset scale hypotheses hold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Under the displayed hypotheses on A,w and P_j, the explicit Stage-1 raw call supplied by lem-maincb-stage1-call-envelope and lem-maincb-stage1-raw-refinement has literal map u_1:C^{m+1}->A at t_1=W.K1*epsilon; lem-maincb-reset-constant-ledger types that same literal map as an extended D_*t_1-inclusion and gives ||u_1(I_{C^{m+1}})-I_A|| <= D_*t_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** The fixed W meets W.c0_cb=c0, W.K1>=K_1^0, and W.e1<=e_1 by lem-maincb-reset-constant-ledger; and lem-maincb-structural-domain-ledger gives epsilon<=W.e1/W.K1. Therefore the hypotheses on A,w and P_j instantiate lem-maincb-stage1-call-envelope. With its cited use of lem-maincb-stage1-raw-refinement, it furnishes one explicit Stage-1 raw call at t_1=W.K1*epsilon with a literal map u_1:C^{m+1}->A (including the stated m=1 interpretation). Fix this particular raw-call witness and this literal map once.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** For that same literal Stage-1 map u_1 (not a newly chosen map), lem-maincb-structural-domain-ledger gives 0<=t_1<=W.r_reset. Also lem-maincb-reset-constant-ledger and lem-maincb-stage1-call-envelope give W.K1>=K_1^0>=1; together with epsilon>=0 and t_1=W.K1*epsilon this yields epsilon<=t_1, so the base-scale and target-ambient-defect conditions hold. The Stage-1 clause of lem-maincb-reset-constant-ledger, whose u_1 is explicitly the one furnished by lem-maincb-stage1-call-envelope with lem-maincb-stage1-raw-refinement, then yields that this same u_1 is an extended D_*t_1-inclusion and ||u_1(I_{C^{m+1}})-I_A||<=D_*t_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** By validated node 1.3.1, fix its particular explicit Stage-1 raw-call witness at t_1=W.K1*epsilon and its literal map u_1:C^{m+1}->A; thus u_1 is exactly the map furnished by lem-maincb-stage1-call-envelope with lem-maincb-stage1-raw-refinement, not a newly chosen map. Lem-maincb-structural-domain-ledger gives 0<=t_1<=W.r_reset. Lem-maincb-reset-constant-ledger and lem-maincb-stage1-call-envelope give W.K1>=K_1^0>=1, so epsilon>=0 and t_1=W.K1*epsilon imply epsilon<=t_1. Since A has ambient defect epsilon, the target-ambient-defect bound is therefore epsilon<=t_1. Hence the Stage-1 clause of lem-maincb-reset-constant-ledger applies to this exact u_1 and yields that u_1 is an extended D_*t_1-inclusion and ||u_1(I_{C^{m+1}})-I_A||<=D_*t_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Apply lem-maincb-reset-output-typing, with D=D_*, epsilon_R=epsilon, B_R=C^{m+1}, A_R=A, and the exact literal map u_R=u_1 furnished by the Stage-1 raw call. Its hypotheses hold because D_*>=1, the fixed W has the required reset thresholds, 0<=t_1<=W.r_reset, u_1 has the stated extended D_*t_1-inclusion and near-unit bounds, and epsilon_R=epsilon<=t_1. Fix the single output witness v_1 from this application. The same-map and unchanged-source/target clauses give v_1:C^{m+1}->A, and the typing and unit clauses give that v_1 is an extended W.c0_cb*epsilon-inclusion with ||v_1(I_{C^{m+1}})-I_A|| <= W.c0_cb*epsilon. Taking w_+=v_1 proves the asserted existence.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

