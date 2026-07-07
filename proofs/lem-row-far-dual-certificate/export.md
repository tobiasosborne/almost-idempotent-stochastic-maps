# Proof Export

## Node 1

**Statement:** Row-far dual certificate: for an exact signed idempotent P and a geometrically distinct row vertex v with delta(P) > 0 (tau = sqrt(delta), rho = 4*tau), writing L_F(v) = sum over {f : ||p_f - p_v||_1 >= rho} of max(P_vf, 0) and nu_v the row negative mass, if L_F(v) > 0 then t*(v) <= nu_v / L_F(v), where t*(v) is the exposedness margin of def-exposed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Notation and nonemptiness: set F={f: ||p_f-p_v||_1 >= rho}, w_f=max(P_vf,0), nu_v=sum_j max(-P_vj,0), and L_F=sum_{f in F} w_f. The hypothesis L_F>0 implies that F contains at least one index with w_f>0, so the far-row minimum in def-exposed is over a nonempty set and min_{f in F} h(p_f) <= min_{f in F, w_f>0} h(p_f) for every admissible exposer h.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Affine row identity: for every admissible exposer h for v in the sense of def-exposed, exact signed idempotence gives p_v=sum_j P_vj p_j and sum_j P_vj=1; since h is affine and h(p_v)=0, one has 0=sum_j P_vj h(p_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Row reproduction from def-signed-idempotent: P^2=P makes the v-th row of P equal to the v-th row of P^2, namely p_v=sum_j P_vj p_j; P1=1 gives sum_j P_vj=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Affine pairing fact: if h is affine, a_j are real coefficients with finite support, and sum_j a_j=1, then h(sum_j a_j p_j)=sum_j a_j h(p_j). In particular this applies to a_j=P_vj once sum_j P_vj=1 is known.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Combination of row reproduction with affine admissibility: applying node 1.2.2 to the coefficients a_j=P_vj and using node 1.2.1 gives h(p_v)=sum_j P_vj h(p_j); admissibility in def-exposed gives h(p_v)=0, hence 0=sum_j P_vj h(p_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Weighted inequality: for every admissible exposer h, the identity 0=sum_j P_vj h(p_j) and the bounds 0<=h(p_j)<=1 imply sum_{f in F} w_f h(p_f) <= nu_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Algebra for the weighted inequality: write h_j=h(p_j), J_+={j:P_vj>0}, and J_-={j:P_vj<0}. From 0=sum_j P_vj h_j, moving negative terms gives sum_{j in J_+} P_vj h_j=sum_{j in J_-} (-P_vj) h_j. Since w_f=max(P_vf,0), F-positive terms are a sub-sum of the nonnegative left side, so sum_{f in F} w_f h_f <= sum_{j in J_+} P_vj h_j. Since 0<=h_j<=1, the right side equals sum_{j in J_-} (-P_vj)h_j <= sum_{j in J_-} (-P_vj)=sum_j max(-P_vj,0)=nu_v by def-negative-mass.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Weighted average bound: for every admissible exposer h, since L_F>0 and w_f>=0, min_{f in F} h(p_f) <= (sum_{f in F} w_f h(p_f))/L_F <= nu_v/L_F.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Weighted-average deduction avoiding the pending parent 1.3: by node 1.1, L_F=sum_{f in F} w_f>0 and at least one far weight w_f is positive. For any admissible h, set A=(sum_{f in F} w_f h(p_f))/L_F. The direct algebra supplied under this node, using the validated row identity from node 1.2.3 and def-negative-mass, gives sum_{f in F} w_f h(p_f) <= nu_v. Since the weights w_f are nonnegative and have positive total L_F, min_{f in F} h(p_f) <= A; division by L_F>0 gives A<=nu_v/L_F.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** Direct bridge for the challenge: fix an arbitrary admissible exposer h and write h_j=h(p_j), J_+={j:P_vj>0}, and J_-={j:P_vj<0}. Node 1.2.3 gives 0=sum_j P_vj h_j. Moving the negative terms gives sum_{j in J_+} P_vj h_j=sum_{j in J_-} (-P_vj)h_j. For f in F, w_f=max(P_vf,0), so the terms w_f h_f with w_f>0 are among the nonnegative J_+ terms; hence sum_{f in F} w_f h_f <= sum_{j in J_+} P_vj h_j. Admissibility gives 0<=h_j<=1 for every row, so this is <=sum_{j in J_-}(-P_vj)=sum_j max(-P_vj,0)=nu_v by def-negative-mass. Node 1.1 gives L_F=sum_{f in F}w_f>0 and w_f>=0. Therefore A=(sum_{f in F}w_f h_f)/L_F is a weighted average over the positive far weights, min_{f in F} h(p_f)<=A, and division of the numerator bound by L_F>0 gives A<=nu_v/L_F.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Supremum step: because the preceding bound holds for every admissible exposer h, the definition t*(v)=sup_h min_{f: ||p_f-p_v||_1>=rho} h(p_f) from def-exposed gives t*(v) <= nu_v/L_F.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Supremum deduction using node 1.4: def-exposed defines t*(v) as the supremum, over admissible exposers h, of min_{f: ||p_f-p_v||_1>=rho} h(p_f). Node 1.4 says every such quantity is <=nu_v/L_F. Therefore their supremum is also <=nu_v/L_F, which is the desired conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.1

**Statement:** Direct replacement for the challenged dependency on node 1.4: for any admissible exposer h, node 1.1 gives L_F=sum_{f in F} w_f>0 with w_f>=0 on F, so min_{f in F} h(p_f) <= (sum_{f in F} w_f h(p_f))/L_F; node 1.3 gives the numerator <= nu_v, hence min_{f in F} h(p_f) <= nu_v/L_F. Therefore every value in the set whose supremum defines t*(v) in def-exposed is <=nu_v/L_F, and the elementary supremum property gives t*(v)<=nu_v/L_F. This proves the parent without using pending node 1.4 as an accepted premise.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.1.1.1

**Statement:** Dependency-correct local repair for ch-605a47af315fea46: fix an arbitrary admissible exposer h and put F={f: ||p_f-p_v||_1>=rho}, w_f=max(P_vf,0), L_F=sum_{f in F}w_f. From validated node 1.1, L_F>0 and the w_f on F are nonnegative, so the weighted average A=(sum_{f in F}w_f h(p_f))/L_F is defined and min_{f in F}h(p_f)<=A. From validated node 1.3, sum_{f in F}w_f h(p_f)<=nu_v, hence A<=nu_v/L_F and therefore min_{f in F}h(p_f)<=nu_v/L_F. Since h was arbitrary, every admissible-exposer value entering t*(v)=sup_h min_{f:||p_f-p_v||_1>=rho}h(p_f) in def-exposed is bounded above by nu_v/L_F; the elementary supremum property gives t*(v)<=nu_v/L_F. Thus the inference is now supported by declared dependencies on the validated facts instead of an undeclared use of pending node 1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.2

**Statement:** Dependency-correct supremum bridge: using only validated nodes 1.1 and 1.3, fix an arbitrary admissible exposer h. Node 1.1 gives L_F=sum_{f in F} w_f>0 and w_f>=0, hence min_{f in F} h(p_f) <= (sum_{f in F} w_f h(p_f))/L_F. Node 1.3 gives sum_{f in F} w_f h(p_f) <= nu_v, so min_{f in F} h(p_f) <= nu_v/L_F for every admissible h. Since def-exposed defines t*(v) as the supremum of these minima over admissible h, and every member of that set is bounded above by nu_v/L_F, the supremum is also bounded above by nu_v/L_F. Thus the deduction no longer requires pending node 1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

