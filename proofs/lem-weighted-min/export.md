# Proof Export

## Node 1

**Statement:** Weighted minimum bound: let p_1, ..., p_m be positive reals with sum_i p_i = 1 and let n_1, ..., n_m be real numbers; then min over i in {1, ..., m} of n_i <= sum_i p_i * n_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** There is an index k in {1, ..., m} such that n_k = min over i in {1, ..., m} of n_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For this index k, n_k <= n_i for every i in {1, ..., m}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the index k supplied by nodes 1.1 and 1.2, so that n_k <= n_i for every i in {1, ..., m}, we have p_i * n_k <= p_i * n_i for every i in {1, ..., m}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By validated node 1.2, for every i in {1, ..., m}, n_k <= n_i for the chosen index k.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** For an arbitrary i in {1, ..., m}, the root hypothesis gives p_i > 0; multiplying n_k <= n_i from node 1.3.1 by this positive real preserves the inequality, hence p_i * n_k <= p_i * n_i. Since i was arbitrary, the inequality holds for every i.

**Type:** claim

**Inference:** universal_generalization

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Summing these inequalities over i gives (sum_i p_i) * n_k <= sum_i p_i * n_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Since sum_i p_i = 1 and n_k is the minimum, the preceding inequality is exactly min_i n_i <= sum_i p_i * n_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

