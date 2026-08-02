# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits an extended W.c0_cb*epsilon-inclusion v:C->A satisfying ||v(I_C)-I_A|| <= W.c0_cb*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix once the universal e_it,K_disp,K_floor and epsilon_max^cb,delta_max^cb,c0^0 witnesses, then fix one and the same C_unit,epsilon_unit,delta_unit,a_unit witness tuple furnished by the third-clause provider in lem-maincb-reset-output-typing and use that tuple in the reset-ledger construction; fix all remaining provider witnesses named in lem-maincb-reset-constant-ledger, put D_* = max{1,D_0,D_1,D_2,D_3}, and let W be the resulting ledger datum. For every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN, the global scalar raw call at t=epsilon satisfies every hypothesis of lem-maincb-reset-output-typing with D=D_*, epsilon_R=epsilon, B_R=C, A_R=A, and u_R(lambda)=lambda I_A; applying that lemma to this same literal map produces an extended W.c0_cb*epsilon-inclusion v:C->A satisfying ||v(I_C)-I_A|| <= W.c0_cb*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For the single witness choice fixed in 1.1, lem-maincb-reset-constant-ledger and lem-maincb-witness-arithmetic give D_* >= 1, W.c0_cb=c0 >= max{c0^0,K_floor,C_unit*(K_floor+1)}, and W.r_reset = min{e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb/D_*,e_it/(D_*+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D_*),[2*(1+K_disp)*D_*]^{-1}}. Thus W.r_reset is at most every reset threshold required by lem-maincb-reset-output-typing for D=D_*. In addition, lem-maincb-structural-domain-ledger gives, from 0 <= epsilon <= W.epsilon_MAIN, the global scalar-scale bound epsilon <= W.r_reset. All occurrences of C_unit,epsilon_unit,delta_unit,a_unit here are the one tuple fixed in 1.1, not a second existential choice.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Let the universal witnesses and W obey D_* = max{1,D_0,D_1,D_2,D_3}, D_* >= 1, W.r_reset <= e_0, and, whenever 0 <= epsilon <= W.epsilon_MAIN, epsilon <= W.r_reset, exactly as supplied by lem-maincb-reset-constant-ledger, lem-maincb-witness-arithmetic, and lem-maincb-structural-domain-ledger. For a finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN, set t=epsilon. Then epsilon <= t <= e_0, so lem-maincb-initial-raw-inclusion furnishes the literal scalar map u_0:C->A, u_0(lambda)=lambda I_A. Because 0 <= t <= W.r_reset and the target ambient defect epsilon is at most t, the initial-call clause of lem-maincb-reset-constant-ledger states that this same literal u_0 is an extended D_*t-inclusion and ||u_0(I_C)-I_A|| <= D_*t. Recording its global-scalar tag, source C, target A, scale t, target defect epsilon, literal level-one map, and fixed amplifications makes it the explicit raw call required by def-maincb-raw-call; no replacement map is introduced.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Complete the def-maincb-raw-call record by choosing its recorded raw-defect field to be d_raw := D_* t. Explicitly, take the global-scalar tag; no supplied input reset state or map (this is the initial call); source C; explicit target corner A itself; pre-helper base scale t=epsilon; no post-helper datum scale; literal level-one output u_0(lambda)=lambda I_A together with its fixed amplification family (1_{M_n} tensor u_0)_{n>=1}; recorded target ambient defect epsilon; and recorded raw-defect number d_raw=D_*t. These are exactly all fields required by def-maincb-raw-call, so they define an explicit raw-call datum. This assignment of d_raw is a record-field choice, distinct from the independently supplied assertion that the same u_0 is an extended D_*t-inclusion; the latter and ||u_0(I_C)-I_A|| <= D_*t come from the initial-call clause of lem-maincb-reset-constant-ledger.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Fix the single C_unit,epsilon_unit,delta_unit,a_unit witness tuple used in constructing W. Suppose D_* >= 1, W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)}, and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D_*,e_it/(D_*+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D_*),[2*(1+K_disp)*D_*]^{-1}}. If the global scalar datum with B_R=C, A_R=A, epsilon_R=t=epsilon, and u_R=u_0 is an explicit raw call, with 0 <= t <= W.r_reset, u_0 an extended D_*t-inclusion, ||u_0(I_C)-I_A|| <= D_*t, and epsilon_R <= t, then lem-maincb-reset-output-typing, applied with D=D_* to that same fixed witness tuple and that same literal u_0, produces a map v:C->A. Its source and target are unchanged, it is an extended W.c0_cb*epsilon-inclusion, and ||v(I_C)-I_A|| <= W.c0_cb*epsilon; these are exactly the asserted existence, typing, and near-unit conclusions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

