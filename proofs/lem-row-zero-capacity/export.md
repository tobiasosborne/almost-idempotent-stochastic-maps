# Proof Export

## Node 1

**Statement:** Row-zero capacity: for an exact signed idempotent P, a row index i, and any vector y with P y = y, 0 <= y_j <= 1 for all j, y_i = 0, and y_f >= kappa for all f in a set F, one has kappa * sum over f in F of max(P_if, 0) <= nu_i, where nu_i is the row-i negative mass.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix arbitrary data satisfying the hypotheses. Write p_j = P_ij, p_j^+ = max(p_j,0), p_j^- = max(-p_j,0), and nu_i = sum_j p_j^-; by def-negative-mass this nu_i is exactly the row-i negative mass appearing in the claim.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Row balance: by Py = y and y_i = 0, the i-th coordinate gives 0 = (Py)_i = sum_j P_ij y_j = sum_j p_j y_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For a finite square matrix P and vector y, the i-th coordinate of Py is (Py)_i = sum_j P_ij y_j by matrix-vector multiplication.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The hypothesis Py = y gives (Py)_i = y_i, and the hypothesis y_i = 0 gives (Py)_i = 0; using p_j = P_ij from 1.1 yields 0 = sum_j P_ij y_j = sum_j p_j y_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Positive-negative splitting of the row balance gives sum_j p_j^+ y_j = sum_j p_j^- y_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For each j, by the definitions p_j^+ = max(p_j,0) and p_j^- = max(-p_j,0), so p_j = p_j^+ - p_j^- and both p_j^+, p_j^- are nonnegative.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Substituting p_j = p_j^+ - p_j^- into the row balance from 1.2 gives 0 = sum_j p_j^+ y_j - sum_j p_j^- y_j; adding sum_j p_j^- y_j to both sides gives sum_j p_j^+ y_j = sum_j p_j^- y_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The negative side is bounded by row-i negative mass: since 0 <= y_j <= 1 and p_j^- >= 0 for every j, sum_j p_j^- y_j <= sum_j p_j^- = nu_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** For every j, p_j^- >= 0 and the hypothesis 0 <= y_j <= 1 gives p_j^- y_j <= p_j^-; summing these finitely many inequalities gives sum_j p_j^- y_j <= sum_j p_j^-.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** By the abbreviation in 1.1 and def-negative-mass, sum_j p_j^- is the row-i negative mass nu_i, so sum_j p_j^- y_j <= nu_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The F-positive contribution is bounded below by kappa: since y_f >= kappa for f in F and p_f^+ >= 0, kappa * sum_{f in F} p_f^+ <= sum_{f in F} p_f^+ y_f <= sum_j p_j^+ y_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** For each f in F, p_f^+ >= 0 and the hypothesis y_f >= kappa imply kappa p_f^+ <= y_f p_f^+; summing over f in F gives kappa * sum_{f in F} p_f^+ <= sum_{f in F} p_f^+ y_f.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** For every j, p_j^+ >= 0 and y_j >= 0, so p_j^+ y_j >= 0. Since F is a subset of the row index set, sum_{f in F} p_f^+ y_f <= sum_j p_j^+ y_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Combining the preceding inequalities gives kappa * sum_{f in F} max(P_if,0) = kappa * sum_{f in F} p_f^+ <= sum_j p_j^+ y_j = sum_j p_j^- y_j <= nu_i; since the data were arbitrary, the claimed universal statement follows.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** From 1.5, kappa * sum_{f in F} p_f^+ <= sum_j p_j^+ y_j. From 1.3, sum_j p_j^+ y_j = sum_j p_j^- y_j. From 1.4, sum_j p_j^- y_j <= nu_i. Chaining gives kappa * sum_{f in F} p_f^+ <= nu_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** Because p_f^+ = max(p_f,0) and p_f = P_if by 1.1, sum_{f in F} p_f^+ = sum_{f in F} max(P_if,0). Substituting this identity into the chained inequality gives the desired displayed inequality.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.3

**Statement:** The initial choice in 1.1 was arbitrary among all P, i, y, F, and kappa satisfying the root hypotheses, so universal generalization proves node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

