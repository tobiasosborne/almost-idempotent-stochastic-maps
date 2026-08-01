# Proof Export

## Node 1

**Statement:** After first fixing a particular universal e_sim>0 witness furnished by lem-maincb-corner-equivalence and a particular universal e_full>0 witness furnished by lem-maincb-full-corner-identification, fix one def-maincb-witness-ledger datum W whose existence is furnished by lem-maincb-reset-constant-ledger instantiated with those same e_sim,e_full witnesses; then 0 <= epsilon <= W.epsilon_MAIN implies epsilon <= W.e_env, epsilon <= W.e1/W.K1, epsilon <= W.e_s2/W.K2, and epsilon <= W.e_cross/W.K3, while the global scalar scale epsilon, atomic scalar scale W.K_call*epsilon, and Stage-1, Stage-2, and Stage-3 scales W.K1*epsilon,W.K2*epsilon,W.K3*epsilon are all at most W.K_call*epsilon <= W.r_reset,e_sim,e_full; moreover W.L*epsilon <= W.K_call*epsilon and W.c0_cb*W.K_call*epsilon <= 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** With the particular e_sim and e_full witnesses fixed exactly as in the statement, lem-maincb-reset-constant-ledger, instantiated with those same witnesses and its compatible fixed provider witnesses, supplies a def-maincb-witness-ledger datum W all of whose fields are positive and for which W.K_call=max{1,W.L+1,W.c0_cb,W.K1,W.K2,W.K3} and W.epsilon_MAIN=min{W.e_env,W.e1/W.K1,W.e_s2/W.K2,W.e_cross/W.K3,W.r_reset/W.K_call,e_sim/W.K_call,e_full/W.K_call,[2*max{1,W.c0_cb*W.K_call}]^(-1)}.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-maincb-corner-equivalence choose the particular universal e_sim>0 witness, and by lem-maincb-full-corner-identification choose the particular universal e_full>0 witness. Fix the compatible witnesses furnished by lem-maincb-error-improvement, lem-maincb-direct-corner-envelope, lem-maincb-stage1-call-envelope, lem-maincb-stage2-call-envelope, and lem-maincb-stage3-call-envelope in the order required by lem-maincb-reset-constant-ledger. Universal instantiation of lem-maincb-reset-constant-ledger with these exact e_sim,e_full witnesses then supplies the asserted datum W, explicitly described there as supplied by lem-maincb-witness-arithmetic.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** Scope correction: node 1.1.1 is not an unconditional derivation of the provider witnesses or of W from the five abbreviated dependencies named in its second sentence. The root statement begins only after (i) the particular e_sim and e_full witnesses have been fixed and (ii) one W has been fixed whose provenance is a complete instantiation of lem-maincb-reset-constant-ledger with those same witnesses. Consequently the standing context includes, inside that provenance condition, every antecedent witness explicitly enumerated in the imported statement of lem-maincb-reset-constant-ledger: the improvement-iteration witnesses, reset-invariant-preservation witnesses, initial-raw-inclusion witnesses, Stage-1 corner-unit and raw-refinement witnesses, Stage-2 extcb-datum and raw-extension witnesses, Stage-3 merging-datum and raw-merge witnesses, and the remaining listed compatible choices. No existence claim for any omitted provider is made in this workspace, and the five-lemma list in node 1.1.1 must not be read as exhaustive or as furnishing the omitted providers.

**Type:** local_assume

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.2

**Statement:** Under that exact standing fixed-provenance context, apply conclusion-elimination to the already-complete instantiation recorded by the root phrase that W is furnished by lem-maincb-reset-constant-ledger instantiated with those same e_sim,e_full witnesses. The imported conclusion then identifies this already-fixed W as a def-maincb-witness-ledger datum supplied by lem-maincb-witness-arithmetic. This is the asserted datum used by node 1.1; it is a conditional use of the root fixed-W binder, not an attempted discharge of the provider antecedents from the allowed externals.

**Type:** local_discharge

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Unpacking the phrase supplied by lem-maincb-witness-arithmetic in the established conclusion of lem-maincb-reset-constant-ledger gives positivity of every field and the exact defining formulas W.K_call=max{1,W.L+1,W.c0_cb,W.K1,W.K2,W.K3} and W.epsilon_MAIN=min{W.e_env,W.e1/W.K1,W.e_s2/W.K2,W.e_cross/W.K3,W.r_reset/W.K_call,e_sim/W.K_call,e_full/W.K_call,[2*max{1,W.c0_cb*W.K_call}]^(-1)} for this same W and these same e_sim,e_full witnesses.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Assume 0<=epsilon<=W.epsilon_MAIN. Since a finite minimum is at most each of its entries, the displayed formula for W.epsilon_MAIN gives epsilon<=W.e_env, epsilon<=W.e1/W.K1, epsilon<=W.e_s2/W.K2, and epsilon<=W.e_cross/W.K3.

**Type:** claim

**Inference:** monotonicity

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The displayed maximum formula gives W.K_call>=1,W.K1,W.K2,W.K3. Multiplication by epsilon>=0 therefore gives epsilon<=W.K_call*epsilon and W.Ki*epsilon<=W.K_call*epsilon for i=1,2,3; the atomic scalar scale equals W.K_call*epsilon. Thus the global, atomic, and three stage scales are all at most W.K_call*epsilon.

**Type:** claim

**Inference:** multiplication_by_positive

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** From the displayed minimum formula, epsilon<=W.epsilon_MAIN is at most W.r_reset/W.K_call, e_sim/W.K_call, and e_full/W.K_call. Since W.K_call>0, multiplication by W.K_call yields W.K_call*epsilon<=W.r_reset, W.K_call*epsilon<=e_sim, and W.K_call*epsilon<=e_full.

**Type:** claim

**Inference:** multiplication_by_positive

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Use the already validated node 1.1.2, rather than the still-pending aggregate node 1.1: for this same W and these same fixed e_sim,e_full it establishes W.K_call>0 and the exact formula W.epsilon_MAIN=min{W.e_env,W.e1/W.K1,W.e_s2/W.K2,W.e_cross/W.K3,W.r_reset/W.K_call,e_sim/W.K_call,e_full/W.K_call,[2*max{1,W.c0_cb*W.K_call}]^(-1)}. Hence the elementary finite-minimum property and the standing hypothesis epsilon<=W.epsilon_MAIN give epsilon<=W.r_reset/W.K_call, epsilon<=e_sim/W.K_call, and epsilon<=e_full/W.K_call. Multiplying each inequality by the positive real W.K_call preserves its direction, and W.K_call*(a/W.K_call)=a for a=W.r_reset,e_sim,e_full because W.K_call is nonzero. Therefore W.K_call*epsilon<=W.r_reset, W.K_call*epsilon<=e_sim, and W.K_call*epsilon<=e_full.

**Type:** claim

**Inference:** multiplication_by_positive

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The maximum formula gives W.K_call>=W.L+1>=W.L, hence W.L*epsilon<=W.K_call*epsilon for epsilon>=0. Also epsilon<=[2*max{1,W.c0_cb*W.K_call}]^(-1); multiplying by the positive W.c0_cb*W.K_call and using W.c0_cb*W.K_call<=max{1,W.c0_cb*W.K_call} gives W.c0_cb*W.K_call*epsilon<=1/2.

**Type:** claim

**Inference:** multiplication_by_positive

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Use validated node 1.1.2 directly, not pending aggregate node 1.1. It gives positivity of W.c0_cb and W.K_call and the exact formulas W.K_call=max{1,W.L+1,W.c0_cb,W.K1,W.K2,W.K3} and W.epsilon_MAIN=min{W.e_env,W.e1/W.K1,W.e_s2/W.K2,W.e_cross/W.K3,W.r_reset/W.K_call,e_sim/W.K_call,e_full/W.K_call,[2*max{1,W.c0_cb*W.K_call}]^(-1)}. Thus W.K_call>=W.L+1>=W.L, and multiplication by the standing epsilon>=0 gives W.L*epsilon<=W.K_call*epsilon. Put x=W.c0_cb*W.K_call and M=max{1,x}. Positivity from node 1.1.2 gives x>0 and M>=1>0. The minimum formula together with epsilon<=W.epsilon_MAIN gives epsilon<=1/(2M). Multiplication by x>0 yields x*epsilon<=x/(2M), while x<=M and 2M>0 give x/(2M)<=M/(2M)=1/2. Hence W.c0_cb*W.K_call*epsilon<=1/2.

**Type:** claim

**Inference:** multiplication_by_positive

**Status:** validated

**Taint:** clean

