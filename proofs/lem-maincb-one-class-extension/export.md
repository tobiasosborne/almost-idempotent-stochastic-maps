# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, all atomic images are one-dimensional, and C is one equivalence class, then there is a current reset isomorphism v_C:M_{|C|}->A_C whose recorded ambient field epsilon_C is selected so that A_C is an extended epsilon_C-C*-algebra and epsilon_C <= W.L*epsilon <= W.K_call*epsilon, and which satisfies d_C <= W.c0_cb*epsilon_C and ||v_C(I_{M_{|C|}})-u_{A_C}|| <= W.c0_cb*epsilon_C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix the universal reset witnesses compatibly, and derive the scale and corner facts needed uniformly for every nonempty subset of C.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** After fixing the common upstream witnesses, choose (C_unit,epsilon_unit,delta_unit,a_unit) from lem-maincb-reset-output-typing. Its conclusion contains every conclusion of lem-maincb-reset-invariant-preservation under the identical coefficient and radius guards, merely adding extended-inclusion and extended-isomorphism typing. Hence these same four witnesses are valid witnesses for lem-maincb-reset-invariant-preservation. Instantiate lem-maincb-reset-constant-ledger with precisely this tuple and fix its supplied W and D_*; its eligibility clause then gives W the very same guards required by lem-maincb-reset-output-typing for D=D_*. No second reset witness or second improved map is introduced.

**Type:** claim

**Inference:** logical_strengthening

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For the W fixed in node 1.1.1, apply lem-maincb-structural-domain-ledger to 0 <= epsilon <= W.epsilon_MAIN. Thus epsilon <= W.e_env and epsilon <= W.e_s2/W.K2; the scales t_atom:=W.K_call*epsilon and t_2:=W.K2*epsilon satisfy 0 <= t_atom,t_2 <= W.K_call*epsilon <= W.r_reset; and W.L*epsilon <= W.K_call*epsilon. The inequalities in lem-maincb-reset-constant-ledger also give W.K2 >= W.L and D_* >= 1.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Apply lem-maincb-direct-corner-envelope using epsilon <= W.e_env, the given extended W.c0_cb*epsilon-inclusion w, and the same A,w occurring in the supplied MAIN partition state. For every nonempty U subseteq C it gives A_U extended W.L*epsilon-C*-algebra. Select and record epsilon_U:=W.L*epsilon for each such U; then epsilon_U <= W.K_call*epsilon, and for a Stage-2 successor epsilon_R:=W.L*epsilon <= t_2 because W.K2 >= W.L. The hypothesis that C is one equivalence class already supplies the same-class facts needed below; lem-maincb-corner-equivalence is used only in the upstream fixed-witness construction of W, not to replace that hypothesis.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Using node 1.1, construct a current reset isomorphism on an arbitrary singleton subset of C by one scalar raw call and one application of lem-maincb-reset-output-typing.

**Type:** claim

**Inference:** existential_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let j be any element of the nonempty class C, put U={j}, epsilon_U:=W.L*epsilon, and t_atom:=W.K_call*epsilon. Node 1.1.3 makes A_U an extended epsilon_U-C*-algebra, and the one-dimensional atomic-image hypothesis means dim A_U=1. Nodes 1.1.2-1.1.3 give 0 <= epsilon_U <= t_atom <= W.r_reset. The scalar map u_0:C=M_1->A_U, lambda |-> lambda*u_{A_U}, furnished by lem-maincb-initial-raw-inclusion is bijective; recorded with its scalar call tag, source, target, scale, amplification family, ambient field and raw defect it is an explicit def-maincb-raw-call. By the uniform u_0 clause of lem-maincb-reset-constant-ledger, this literal map is an extended D_*t_atom-inclusion and has unit error at most D_*t_atom, so it meets the typed-reset premises.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Apply lem-maincb-reset-output-typing alone to the exact raw call of node 1.2.1 with D=D_*, t=t_atom, epsilon_R=epsilon_U, B_R=M_1 and A_R=A_U, using the compatible W guards fixed in node 1.1.1. Select its single existential output and call it v_U. That same map simultaneously has unchanged source, target and amplification family, satisfies d_U <= W.c0_cb*epsilon_U and ||v_U(I_{M_1})-u_{A_U}|| <= W.c0_cb*epsilon_U, and is an extended W.c0_cb*epsilon_U-isomorphism because the literal u_0 is bijective. Together with the recorded field epsilon_U, these fields form the required def-maincb-reset-state on U; no output of lem-maincb-reset-invariant-preservation is used.

**Type:** claim

**Inference:** existential_instantiation

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Using node 1.1, prove the invariant-preserving successor statement: let U be a nonempty proper subset of C and fix one current reset state on U whose supplied map v_U:M_{|U|}->A_U is tagged as an extended W.c0_cb*epsilon_U-isomorphism, whose recorded field is epsilon_U=W.L*epsilon, and which satisfies d_U<=W.c0_cb*epsilon_U and ||v_U(I_{M_{|U|}})-u_{A_U}||<=W.c0_cb*epsilon_U. For every j in C minus U, with R=U union {j}, there exists a current reset state on R whose supplied map v_R:M_{|R|}->A_R is tagged as an extended W.c0_cb*epsilon_R-isomorphism, whose recorded field is epsilon_R=W.L*epsilon, and which satisfies d_R<=W.c0_cb*epsilon_R and ||v_R(I_{M_{|R|}})-u_{A_R}||<=W.c0_cb*epsilon_R, obtained by the Stage-2 producer and one application of lem-maincb-reset-output-typing.

**Type:** claim

**Inference:** universal_generalization

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Assume U is a nonempty proper subset of C and fix exactly one current reset state on U whose supplied map v_U:M_{|U|}->A_U is tagged as an extended W.c0_cb*epsilon_U-isomorphism, with recorded epsilon_U:=W.L*epsilon, d_U <= W.c0_cb*epsilon_U, and ||v_U(I_{M_{|U|}})-u_{A_U}|| <= W.c0_cb*epsilon_U. Choose j in C minus U and put R:=U union {j}, epsilon_R:=W.L*epsilon, and t_2:=W.K2*epsilon. Form a supplied MAIN partition state for the same A,w by retaining the root state geometry and replacing its current-subset field by U and its reset-state reference by this exact state and exact map v_U. Since U and j lie in the hypothesized single equivalence class, nodes 1.1.2-1.1.3 supply epsilon <= W.e_s2/W.K2, the target corner A_R, all scale inequalities, and the required W coefficient conditions; hence lem-maincb-stage2-call-envelope applies to this matching partition state and exact prior isomorphism v_U and furnishes the explicit Stage-2 EXT raw-call datum in A_R with total defect at most C_s2^0*t_2.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** By def-maincb-reset-state, the strengthened input fixes one state with source M_{|U|}, target A_U, recorded epsilon_U=W.L*epsilon, its exact level-one map and amplification family, both displayed bounds, and the supplied extended-isomorphism tag. Thus the map used below is the same tagged isomorphism v_U throughout; no isomorphism conclusion is inferred from the numerical bounds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Starting from the root supplied MAIN partition state for the same A,w, retain J,A,w, the atomic images P_k, the relation, and its class family, and set the current nonempty subset field to this U and the reset-state-reference field to the exact state of node 1.3.1.1. This is a supplied MAIN partition state by def-maincb-partition-state: the definition permits any current nonempty subset of J and a reference to one separately supplied reset state. Its current subset/reference is therefore exactly U,v_U, while all geometric data remain those of the root state.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.3

**Statement:** Apply lem-maincb-stage2-call-envelope to the matching state constructed in node 1.3.1.2 and the exact tagged current reset isomorphism from node 1.3.1.1. Its remaining hypotheses hold because U is nonempty, j is outside U but in the same class, R=U union {j}, nodes 1.1.2-1.1.3 give epsilon <= W.e_s2/W.K2, epsilon_U=W.L*epsilon, epsilon_R=W.L*epsilon, t_2=W.K2*epsilon, the required scale dominations and corner typing, and node 1.1.1 fixes W with the coefficient and witness conditions of the envelope. The conclusion is the explicit Stage-2 EXT raw-call datum in A_R with total defect at most C_s2^0*t_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Use the uniform Stage-2 producer/output clause of lem-maincb-reset-constant-ledger directly, rather than separately instantiating lem-maincb-stage2-raw-extension. For the exact Stage-2 datum and exact prior map produced in node 1.3.1, with t_2:=W.K2*epsilon and epsilon_R:=W.L*epsilon, this clause furnishes its literal output u_2:M_{|U|+1}->A_R as an extended D_*t_2-isomorphism satisfying ||u_2(I_{M_{|U|+1}})-u_{A_R}|| <= D_*t_2. By def-extended-delta-inclusion, the isomorphism conclusion includes both extended D_*t_2-inclusion typing and bijectivity, exactly the typed-reset input required; no inference from bare bijectivity and no unlicensed use of the separate raw-extension theorem is made.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Node 1.3.1 supplies the Stage-2 producer hypothesis for the exact matching partition/reset state and the explicit raw-call datum. Nodes 1.1.2 and 1.1.3 give 0 <= t_2 <= W.r_reset, make A_R an extended epsilon_R-C*-algebra, and give epsilon_R <= t_2; node 1.1.1 fixes the same W,D_* from lem-maincb-reset-constant-ledger. Therefore all antecedents of that ledger's uniform u_2 producer/output clause hold. Applying that combined clause itself yields the literal u_2 for this producer as an extended D_*t_2-isomorphism with the D_*t_2 near-unit bound. This invocation does not appeal to the standalone antecedent of lem-maincb-stage2-raw-extension and hence requires neither C_s2^0*e_2 <= e_ext nor (C_ext+1)*C_s2^0*e_2 <= e_iso_unit as separately available facts.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Apply lem-maincb-reset-output-typing alone to the exact u_2 raw call of node 1.3.2 with D=D_*, t=t_2, epsilon_R=W.L*epsilon, B_R=M_{|U|+1}, and A_R. Nodes 1.1.1-1.1.3 give its W guards, D_*>=1, 0 <= t_2 <= W.r_reset, epsilon_R <= t_2, and the ambient typing. Select the theorem's one existential output v_R and retain that same map for every conclusion. It is an extended W.c0_cb*epsilon_R-isomorphism because node 1.3.2 supplies both the extended-inclusion typing and bijectivity of u_2; it has unchanged source M_{|U|+1}=M_{|R|}, target A_R and amplification family; and it satisfies d_R <= W.c0_cb*epsilon_R and ||v_R(I_{M_{|R|}})-u_{A_R}|| <= W.c0_cb*epsilon_R. Recording epsilon_R forms the required successor reset state, with no use of a reset-invariant-preservation output.

**Type:** claim

**Inference:** existential_instantiation

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Using nodes 1.1, 1.2, and 1.3, enumerate the finite nonempty class C, iterate the successor construction from the singleton base, and identify the terminal state with the reset isomorphism asserted for C.

**Type:** claim

**Inference:** finite_induction

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Because C is a finite nonempty equivalence class, enumerate C={j_1,...,j_q}, where q=|C|>=1, and set U_r={j_1,...,j_r}. Node 1.2 gives the reset state on U_1. For each 1 <= r < q, instantiate node 1.3 with the exact state produced at index r (node 1.2 when r=1, and the single output selected by the immediately preceding instance of node 1.3 thereafter), U=U_r, and j=j_{r+1}; define the next state to be that instance's single selected output on U_{r+1}. Ordinary finite induction therefore produces a reset state at every U_r without any floating inductive hypothesis or change of witness within a step.

**Type:** claim

**Inference:** finite_induction

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Fix the enumeration C={j_1,...,j_q} and U_r={j_1,...,j_r} from node 1.4.1; node 1.4.1 is used here only for this enumeration notation, not as a source of any reset invariant. The strengthened direct induction in child node 1.4.2.1, using the exact selected singleton output of node 1.2.2 as its base and the exact selected outputs of nodes 1.3.1--1.3.3 as its successors, yields one selected terminal state on U_q whose source is M_q, whose map v_q:M_q->A_{U_q} is tagged as an extended W.c0_cb*epsilon_{U_q}-isomorphism, whose recorded field is epsilon_{U_q}=W.L*epsilon, and which satisfies d_{U_q}<=W.c0_cb*epsilon_{U_q} and ||v_q(I_{M_q})-u_{A_{U_q}}||<=W.c0_cb*epsilon_{U_q}. Since U_q=C and q=|C|, set v_C:=v_q and epsilon_C:=epsilon_{U_q}. Node 1.1.3 says A_C is an extended epsilon_C-C*-algebra and epsilon_C=W.L*epsilon<=W.K_call*epsilon. Thus this selected witness has exactly the source, target, recorded ambient field, isomorphism typing, defect bound, and unit bound asserted by root node 1.

**Type:** claim

**Inference:** existential_generalization

**Status:** validated

**Taint:** clean

##### Node 1.4.2.1

**Statement:** For the fixed enumeration C={j_1,...,j_q} and U_r={j_1,...,j_r}, use the strengthened induction assertion I_r: there is one selected current reset state on U_r whose named source is M_r, whose exact map v_r:M_r->A_{U_r} is tagged as an extended W.c0_cb*epsilon_{U_r}-isomorphism, whose recorded field is epsilon_{U_r}=W.L*epsilon, and which satisfies d_{U_r}<=W.c0_cb*epsilon_{U_r} and ||v_r(I_{M_r})-u_{A_{U_r}}||<=W.c0_cb*epsilon_{U_r}. For r=1, instantiate node 1.2.2 at j_1; its single selected output has source M_1, the isomorphism tag, this recorded field, and both displayed bounds, so I_1 holds. If I_r holds for r<q, feed that exact selected state and exact map into the successor construction of nodes 1.3.1--1.3.3 with U=U_r and j=j_{r+1}. Since |U_r|=r and R=U_r union {j_{r+1}}=U_{r+1}, node 1.3.3 selects one output v_{r+1}:M_{r+1}->A_{U_{r+1}} with the same four invariant clauses, so I_{r+1} holds. Finite induction gives I_q (including when q=1, where only the base is used). Now U_q=C and q=|C|; node 1.1.3 additionally says A_C is an extended epsilon_C-C*-algebra for epsilon_C:=epsilon_{U_q}=W.L*epsilon and epsilon_C<=W.K_call*epsilon. Selecting the witness supplied by I_q therefore proves every source, target, typing, field, defect, and unit-error clause stated in node 1.4.2. This argument does not use the datum-only conclusion of node 1.4.1 as a source of the invariant.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

