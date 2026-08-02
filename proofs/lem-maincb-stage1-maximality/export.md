# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN and w:C^m->A has maximum source dimension among all extended W.c0_cb*epsilon-inclusions satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, then every projection-basis image P_j=w(e_j) satisfies dim S_{P_j}=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix once and for all the single def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger, and then fix A and epsilon with the hypotheses in node 1. Define D(A,W,epsilon) to be the set of integers n for which there exists a map v:C^n->A that is an extended W.c0_cb*epsilon-inclusion in the precise sense of def-extended-delta-inclusion and satisfies ||v(I_{C^n})-I_A|| <= W.c0_cb*epsilon. By lem-maincb-maximal-reset-selection this set is nonempty and has a maximum. The maximality hypothesis on the displayed w says exactly that m=max D(A,W,epsilon); in particular no map C^{m+1}->A satisfying those same extended-inclusion and near-unit conditions exists. No new ledger or witness is chosen after this definition.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Let e_j be an arbitrary projection-basis element of C^m in the sense of def-projection-basis and put P_j=w(e_j). Applying lem-maincb-corner-nontriviality to the same fixed W,A,epsilon,w,e_j (whose hypotheses are precisely those of node 1) gives that S_{P_j} contains a nonzero element and therefore dim S_{P_j} >= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For an arbitrary projection-basis element e_j of C^m, dim S_{w(e_j)}>1 is impossible. Indeed, if dim S_{w(e_j)}>1, lem-maincb-stage1-strict-refinement, applied to the same fixed W,A,epsilon,w and this j, produces a map w_+:C^{m+1}->A which is an extended W.c0_cb*epsilon-inclusion in the precise sense of def-extended-delta-inclusion and satisfies ||w_+(I_{C^{m+1}})-I_A|| <= W.c0_cb*epsilon. Thus w_+ is an admissible map of source dimension m+1, contradicting directly the node-1 hypothesis that w has maximum source dimension among all such maps. Hence not(dim S_{w(e_j)}>1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For every finite-dimensional complex vector space S, dim S is a nonnegative integer; consequently, if dim S >= 1 and not(dim S>1), then dim S=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

