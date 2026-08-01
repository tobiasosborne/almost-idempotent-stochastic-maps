# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, all atomic images are one-dimensional, and C is one equivalence class, then there is a current reset isomorphism v_C:M_{|C|}->A_C whose recorded ambient field epsilon_C is selected so that A_C is an extended epsilon_C-C*-algebra and epsilon_C <= W.L*epsilon <= W.K_call*epsilon, and which satisfies d_C <= W.c0_cb*epsilon_C and ||v_C(I_{M_{|C|}})-u_{A_C}|| <= W.c0_cb*epsilon_C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Under the hypotheses of node 1, prove the stronger assertion that for every nonempty subset U of C there is a current reset isomorphism v_U:M_{|U|}->A_U with recorded ambient field epsilon_U:=W.L*epsilon, with A_U an extended epsilon_U-C*-algebra, epsilon_U=W.L*epsilon<=W.K_call*epsilon, d_U<=W.c0_cb*epsilon_U, and ||v_U(I_{M_{|U|}})-u_{A_U}||<=W.c0_cb*epsilon_U; taking U=C then gives node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Fix throughout the particular e_sim witness from lem-maincb-corner-equivalence and the same ledger W furnished by lem-maincb-reset-constant-ledger and consumed by lem-maincb-structural-domain-ledger. From 0<=epsilon<=W.epsilon_MAIN, record all structural smallness inequalities needed below and, for every nonempty U subseteq C, select epsilon_U:=W.L*epsilon and certify A_U as an extended epsilon_U-C*-algebra with epsilon_U<=W.K_call*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** By lem-maincb-structural-domain-ledger, epsilon<=W.e_env and epsilon<=W.e_s2/W.K2; with t_atom:=W.K_call*epsilon and t_2:=W.K2*epsilon one has 0<=t_atom,t_2<=W.K_call*epsilon<=W.r_reset, t_2<=W.e_s2, and W.L*epsilon<=W.K_call*epsilon. The ledger inequalities in lem-maincb-reset-constant-ledger also give W.K2>=W.L and all Stage-2/reset producer thresholds. Hence lem-maincb-direct-corner-envelope applies to the given A,w and every nonempty U subseteq C, proving A_U is an extended W.L*epsilon-C*-algebra. Selecting epsilon_U:=W.L*epsilon therefore supplies the asserted ambient record and all scale comparisons used by the base and step.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Establish the induction base: for each j in C, construct a current reset isomorphism v_{\{j\}}:M_1->A_{\{j\}} with recorded field epsilon_{\{j\}}=W.L*epsilon and both reset bounds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Fix j in C, put A_j:=A_{\{j\}}, epsilon_j:=W.L*epsilon, and t_atom:=W.K_call*epsilon. By lem-maincb-direct-corner-envelope and the structural inequalities, A_j is an extended epsilon_j-C*-algebra with 0<=epsilon_j<=t_atom<=W.r_reset; the one-dimensional atomic-image hypothesis gives dim A_j=1. Apply the compressed-corner scalar instance of lem-maincb-initial-raw-inclusion together with the scalar producer clause of lem-maincb-reset-constant-ledger to obtain the literal scalar map u_j:C->A_j as an extended D_* t_atom-isomorphism satisfying ||u_j(I_C)-u_{A_j}||<=D_* t_atom, where D_*>=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** Apply lem-maincb-reset-invariant-preservation to that explicit scalar raw call with D=D_*, target ambient field epsilon_j, and scale t_atom. It yields v_{\{j\}}:C=M_1->A_j with d_{\{j\}}<=W.c0_cb*epsilon_j and ||v_{\{j\}}(I_{M_1})-u_{A_j}||<=W.c0_cb*epsilon_j; bijectivity is preserved, so this is the required current reset isomorphism with unchanged source, target, and amplification form.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Establish the induction step: if emptyset!=U proper-subset C already has such a current reset isomorphism and j is in C minus U, then R:=U union \{j\} has a current reset isomorphism v_R:M_{|R|}->A_R with recorded field epsilon_R=W.L*epsilon and both reset bounds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** Assume emptyset!=U proper-subset C has the stated reset, choose j in C minus U, and set R:=U union {j}, epsilon_R:=W.L*epsilon, and t_2:=W.K2*epsilon. Since U and j lie in the same equivalence class, the Stage-2 call-envelope hypotheses hold; the direct aggregate Stage-2 producer conclusion in lem-maincb-reset-constant-ledger, with the structural scale bounds, supplies the literal map u_2:M_{|U|+1}->A_R as an extended D_*t_2-isomorphism satisfying ||u_2(I)-u_{A_R}||<=D_*t_2 and eligible for reset preservation. This conclusion is obtained without separately invoking lem-maincb-stage2-raw-extension.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.3.1.1

**Statement:** By def-maincb-partition-state and def-maincb-reset-state, combine the fixed geometry for the same A,w with the induction-hypothesis current reset at nonempty U, and choose j in C minus U and R:=U union {j}. The ledger conditions W.c0_cb=c0, W.L>=L^0, W.K2>=max{K_2^0,1,W.L,W.c0_cb*W.L}, and W.e_s2<=e_s2^0 come from lem-maincb-reset-constant-ledger, while epsilon<=W.e_s2/W.K2 comes from lem-maincb-structural-domain-ledger. Hence lem-maincb-stage2-call-envelope applies and furnishes in A_R the explicit Stage-2 EXT raw-call datum at t_2:=W.K2*epsilon, with recorded target field epsilon_R:=W.L*epsilon and total post-helper defect at most C_s2^0*t_2. Also lem-maincb-structural-domain-ledger gives 0<=t_2<=W.r_reset, and W.K2>=W.L with epsilon>=0 gives epsilon_R<=t_2. Apply directly the aggregate Stage-2 producer conclusion of lem-maincb-reset-constant-ledger to this producer output and these two scale bounds: it supplies the literal map u_2:M_{|U|+1}->A_R as an extended D_*t_2-isomorphism, with ||u_2(I)-u_{A_R}||<=D_*t_2 and eligibility for lem-maincb-reset-invariant-preservation. No separate application of lem-maincb-stage2-raw-extension, no closedness assertion, and no unexported fixed-witness inequality is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.3.1.2

**Statement:** Do not separately apply lem-maincb-stage2-raw-extension or infer its two fixed-witness inequalities. Instead instantiate the aggregate Stage-2 producer conclusion exported by lem-maincb-reset-constant-ledger at t=t_2. Its producer hypotheses are satisfied by the Stage-2 call-envelope datum of node 1.1.3.1.1 together with 0<=t_2<=W.r_reset and target ambient defect epsilon_R<=t_2: the first scale bound is supplied by lem-maincb-structural-domain-ledger, and epsilon_R=W.L*epsilon<=W.K2*epsilon=t_2 because lem-maincb-reset-constant-ledger gives W.K2>=W.L. That aggregate conclusion directly furnishes the literal map u_2:M_{|U|+1}->A_R as an extended D_*t_2-isomorphism, with ||u_2(I)-u_{A_R}||<=D_*t_2 and eligibility for lem-maincb-reset-invariant-preservation.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.1.3.1.2.1

**Statement:** For t_2:=W.K2*epsilon and epsilon_R:=W.L*epsilon, lem-maincb-structural-domain-ledger gives 0<=t_2<=W.r_reset. Moreover lem-maincb-reset-constant-ledger gives W.K2>=W.L, hence epsilon_R=W.L*epsilon<=W.K2*epsilon=t_2 because epsilon>=0. Thus the aggregate ledger clause has its base-scale and target-ambient-defect bounds.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.1.3.1.2.2

**Statement:** The remaining relevant producer hypotheses are precisely those used by lem-maincb-stage2-call-envelope in the parent construction: the same A,w and partition state, nonempty U and j in the same equivalence class, the induction reset bounds, and epsilon<=W.e_s2/W.K2; its output is the explicit Stage-2 EXT raw-call datum at t_2 in A_R. Apply the single aggregate Stage-2 implication in lem-maincb-reset-constant-ledger to that producer output and the bounds from node 1.1.3.1.2.1. It directly supplies the literal u_2:M_{|U|+1}->A_R as an extended D_*t_2-isomorphism with ||u_2(I)-u_{A_R}||<=D_*t_2 and reset eligibility. This argument neither invokes lem-maincb-stage2-raw-extension separately nor asserts C_s2^0*e_2<=e_ext or (C_ext+1)*C_s2^0*e_2<=e_iso_unit.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.1.3.2

**Statement:** Since |R|=|U|+1, epsilon_R=W.L*epsilon<=t_2, and 0<=t_2<=W.r_reset, apply lem-maincb-reset-invariant-preservation to the explicit Stage-2 raw call with D=D_*. The resulting v_R:M_{|R|}->A_R is bijective and hence an extended isomorphism, has d_R<=W.c0_cb*epsilon_R and ||v_R(I_{M_{|R|}})-u_{A_R}||<=W.c0_cb*epsilon_R, and retains the same source, target corner, and amplification form, proving the induction step.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Since C is a finite nonempty equivalence class, enumerate the elements of any nonempty U subseteq C, use the singleton base on the first element, and apply the one-atom induction step successively; the reset after each Stage-2 call preserves exactly the same invariant, so the construction proves the stronger assertion without any class-size accumulation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

