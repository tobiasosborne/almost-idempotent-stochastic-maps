# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images and has classes C_1,...,C_q, and each initial current reset isomorphism v_{C_a}:B_{C_a}->A_{C_a} has recorded ambient field epsilon_{C_a} <= W.L*epsilon and satisfies d_{C_a} <= W.c0_cb*epsilon_{C_a} and ||v_{C_a}(I_{B_{C_a}})-u_{A_{C_a}}|| <= W.c0_cb*epsilon_{C_a}, then there is a current reset isomorphism v:oplus_a B_{C_a}->A_{union_a C_a} whose recorded ambient field epsilon_{union_a C_a} satisfies epsilon_{union_a C_a} <= W.L*epsilon, d_{union_a C_a} <= W.c0_cb*epsilon_{union_a C_a}, and ||v(I_{oplus_a B_{C_a}})-u_{A_{union_a C_a}}|| <= W.c0_cb*epsilon_{union_a C_a}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Constant and domain ledger: keep the single def-maincb-witness-ledger datum W already fixed in the root, namely the witness supplied by lem-maincb-reset-constant-ledger for the same fixed e_sim and e_full witnesses. By lem-maincb-structural-domain-ledger and 0 <= epsilon <= W.epsilon_MAIN, epsilon <= W.e_env, epsilon <= W.e1/W.K1, epsilon <= W.e_s2/W.K2, and epsilon <= W.e_cross/W.K3; the global scale epsilon, atomic scale W.K_call*epsilon, and Stage-1, Stage-2, Stage-3 scales W.K1*epsilon, W.K2*epsilon, W.K3*epsilon are at most W.K_call*epsilon <= W.r_reset,e_sim,e_full; also W.L*epsilon <= W.K_call*epsilon and W.c0_cb*W.K_call*epsilon <= 1/2. No new constants or replacement witness are selected in the recombination, and in particular the scalar hypotheses 0 <= epsilon <= W.epsilon_MAIN required by every use of lem-maincb-binary-block-merge are fixed once here.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Finite recombination assertion: for 1 <= k <= q put U_k=union_{a=1}^k C_a and define B^(1)=B_{C_1}, B^(k+1)=B^(k) oplus B_{C_{k+1}}. Let P(k) mean that there is one current reset isomorphism v_k:B^(k)->A_{U_k}, with its own recorded ambient field epsilon_{U_k} <= W.L*epsilon, satisfying d_{U_k} <= W.c0_cb*epsilon_{U_k} and ||v_k(I_{B^(k)})-u_{A_{U_k}}|| <= W.c0_cb*epsilon_{U_k}. Then q >= 1 and P(q); since U_q=union_a C_a and B^(q)=oplus_a B_{C_a} in this recursive notation, P(q) is exactly the current reset isomorphism and the three bounds required by the root.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Index setup: a def-maincb-partition-state contains a nonempty current subset of its finite atomic index set J, hence J is nonempty. The displayed classes C_1,...,C_q partition J into nonempty equivalence classes, so q >= 1. For U_k=union_{a=1}^k C_a, each U_k is a nonempty union of whole classes; whenever k<q, U_k and C_{k+1} are disjoint nonempty unions sharing no class. Define the finite direct sum recursively by B^(1)=B_{C_1} and B^(k+1)=B^(k) oplus B_{C_{k+1}}; consequently U_q=union_a C_a and B^(q)=oplus_a B_{C_a}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Base case P(1): U_1=C_1 and B^(1)=B_{C_1}. Take v_1 to be the one root-supplied initial current reset isomorphism v_{C_1}:B_{C_1}->A_{C_1}, without changing its witness. Its recorded field and recorded defect and unit estimates are exactly epsilon_{C_1} <= W.L*epsilon, d_{C_1} <= W.c0_cb*epsilon_{C_1}, and ||v_{C_1}(I_{B_{C_1}})-u_{A_{C_1}}|| <= W.c0_cb*epsilon_{C_1}, so it witnesses P(1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Inductive transition: fix any integer k with 1 <= k < q and assume P(k), witnessed by the particular current reset isomorphism v_k:B^(k)->A_{U_k} produced at the preceding induction index (for k=1 this is the exact witness in the base case; thereafter it is the exact output of the preceding instance of this transition). Apply lem-maincb-binary-block-merge with U=U_k, V=C_{k+1}, v_U=v_k, and v_V equal to the root-supplied initial v_{C_{k+1}}. The root supplies the same A, epsilon, W, partition state, w, near-unit estimate, and one-dimensional atomic-image hypothesis; 0 <= epsilon <= W.epsilon_MAIN is a root hypothesis; U_k and C_{k+1} are disjoint nonempty unions sharing no class by their definitions as distinct class unions; P(k) supplies all three recorded-field/defect/unit hypotheses for v_U; and the root supplies those same three hypotheses for v_V. The cited lemma returns one particular current reset isomorphism v_{k+1}:B^(k) oplus B_{C_{k+1}}->A_{U_k union C_{k+1}} with recorded field epsilon_{U_k union C_{k+1}} <= W.L*epsilon and the required defect and unit bounds. Since B^(k+1)=B^(k) oplus B_{C_{k+1}} and U_{k+1}=U_k union C_{k+1}, this exact returned witness establishes P(k+1), and it alone is threaded into the next index.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Finite-induction rule: for any integer q >= 1 and propositions P(1),...,P(q), the conjunction of P(1) and the implications P(k) => P(k+1) for every integer 1 <= k < q implies P(q). This follows by ordinary induction on k (with the q=1 case ending at the base case).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

