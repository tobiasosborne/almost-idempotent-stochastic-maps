# Proof Export

## Node 1

**Statement:** Harmonic-affine bridge: for an exact signed idempotent P with rows p_i = (P_ij)_j, a vector g satisfies Pg = g if and only if there exists u with g_i = u . p_i for every row index i; in the forward direction u = g works (g_i = p_i . g), and the constant term of any affine representation is absorbable into u since all row sums equal 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Coordinate consequences of exact signed idempotence: if P is an exact signed idempotent and p_i is row i, then sum_j P_ij = 1 for each i, (Pg)_i = p_i . g for every vector g, and sum_j P_ij p_j = p_i for each i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Row sums: by def-signed-idempotent, P*1 = 1, so for each row i, sum_j P_ij = 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Matrix-vector coordinates: since p_i is row i, for every vector g one has (Pg)_i = sum_j P_ij g_j = p_i . g.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Row reproduction: by def-signed-idempotent, P^2 = P; hence for every coordinate k, (sum_j P_ij p_j)_k = sum_j P_ij P_jk = (P^2)_ik = P_ik = (p_i)_k, so sum_j P_ij p_j = p_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Forward direction: if Pg = g, then choosing u = g gives g_i = u . p_i for every row index i, because g_i = (Pg)_i = p_i . g.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Assume Pg = g. Then for each row index i, g_i = (Pg)_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Since p_i is row i, (Pg)_i = sum_j P_ij g_j = p_i . g.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Taking u = g therefore gives g_i = p_i . g = p_i . u, equivalently g_i = u . p_i under the usual dot-product notation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Constant absorption: any affine representation g_i = c + u . p_i can be rewritten as a purely linear row representation g_i = u' . p_i by taking u' = u + c*1, since every row sum is 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Assume an affine row representation g_i = c + u . p_i for all row indices i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** By the row-sum part of def-signed-idempotent, p_i . 1 = sum_j P_ij = 1 for every i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Set u' = u + c*1. Then u' . p_i = u . p_i + c*(1 . p_i) = u . p_i + c = g_i for every i, so the constant term has been absorbed into the linear coefficient.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Converse direction: if there is a vector u with g_i = u . p_i for every i, then Pg = g, because (Pg)_i = sum_j P_ij g_j = u . (sum_j P_ij p_j) = u . p_i = g_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Assume there is a vector u such that g_j = u . p_j for every row index j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** For each i, the matrix-vector formula gives (Pg)_i = sum_j P_ij g_j = sum_j P_ij (u . p_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** By linearity of the dot product, sum_j P_ij (u . p_j) = u . (sum_j P_ij p_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.4

**Statement:** By row reproduction from P^2 = P, sum_j P_ij p_j = p_i; hence (Pg)_i = u . p_i = g_i for every i, so Pg = g.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

