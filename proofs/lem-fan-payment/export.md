# Proof Export

## Node 1

**Statement:** Zero-sum fan payment: let (w_1, p_1), ..., (w_m, p_m) be a finite family with vectors w_i in R^d and weights p_i > 0 satisfying sum_i p_i = 1, such that every w_i has coordinate sum zero (sum_l w_i(l) = 0) and the weighted barycenter is zero (sum_i p_i w_i = 0); write n(w) = sum_l max(-w(l), 0); then min over i* in {1, ..., m} of sum_i p_i n(w_i - w_{i*}) <= 2 * sum_i p_i n(w_i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** For each candidate pivot k in {1, ..., m}, set A_k := sum_i p_i n(w_i - w_k), and set N := sum_i p_i n(w_i). The desired root conclusion is min over k of A_k <= 2*N.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** By lem-weighted-min applied to the weights p_k and the real numbers A_k, min over k in {1, ..., m} of A_k <= sum_k p_k A_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** The root hypotheses give p_k > 0 for every k and sum_k p_k = 1; for the finite real family A_k := sum_i p_i n(w_i - w_k), the hypotheses of lem-weighted-min are therefore satisfied.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Instantiating lem-weighted-min with n_k := A_k yields min over k in {1, ..., m} of A_k <= sum_k p_k A_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The weighted average of the pivot costs satisfies sum_k p_k A_k <= 2*N.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For every pair of indices (i,k), the root hypothesis says w_k has coordinate sum zero, so lem-zerosum-triangle applied with w := w_i and v := w_k gives n(w_i - w_k) <= n(w_i) + n(w_k).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Expanding A_k := sum_i p_i n(w_i - w_k) gives sum_k p_k A_k = sum_k p_k sum_i p_i n(w_i - w_k) = sum_{i,k} p_i p_k n(w_i - w_k).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Because p_i > 0 and p_k > 0, multiplying the pairwise inequality by p_i p_k preserves it and summing over all finite pairs gives sum_{i,k} p_i p_k n(w_i - w_k) <= sum_{i,k} p_i p_k (n(w_i) + n(w_k)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Using sum_i p_i = sum_k p_k = 1 and N := sum_i p_i n(w_i), the last double sum equals (sum_k p_k) sum_i p_i n(w_i) + (sum_i p_i) sum_k p_k n(w_k) = N + N = 2*N.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Combining min_k A_k <= sum_k p_k A_k with sum_k p_k A_k <= 2*N gives min_k A_k <= 2*N, which is exactly min over i* of sum_i p_i n(w_i - w_i*) <= 2*sum_i p_i n(w_i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The abbreviation node 1.1 fixes A_k := sum_i p_i n(w_i - w_k) for each k and N := sum_i p_i n(w_i). The already validated nodes 1.2.1 and 1.2.2 establish, for these same A_k and weights p_k, the inequality min_k A_k <= sum_k p_k A_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** Dependency import: nodes 1.1, 1.2.1, and 1.2.2 are validated and supply exactly the definitions of A_k and N and the weighted-min conclusion min_k A_k <= sum_k p_k A_k used by 1.4.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Using the definitions of A_k and N from node 1.1, the validated nodes 1.3.1 through 1.3.4 give the chain sum_k p_k A_k = sum_{i,k} p_i p_k n(w_i - w_k) <= sum_{i,k} p_i p_k (n(w_i)+n(w_k)) = 2*N; hence sum_k p_k A_k <= 2*N.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** From 1.4.1 we have min_k A_k <= sum_k p_k A_k, and from 1.4.2 we have sum_k p_k A_k <= 2*N. Transitivity of <= gives min_k A_k <= 2*N. Substituting the definitions A_k := sum_i p_i n(w_i - w_k) and N := sum_i p_i n(w_i) from 1.1, and merely renaming the pivot index k as i*, this is exactly min over i* in {1,...,m} of sum_i p_i n(w_i - w_i*) <= 2*sum_i p_i n(w_i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

