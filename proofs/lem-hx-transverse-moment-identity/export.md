# Proof Export

## Node 1

**Statement:** For every finite exact signed idempotent P, all points q0 != q1 of the row polytope K(P) = conv{p_i}, and every affine function chi on R^I with chi(q0) = 0 and chi(q1) = 1, the full row-point fibers satisfy sum_Q d_Q*chi(p_Q) = 1, where d_Q = sum_{j in Q}(q1_j - q0_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Every point q in K(P)=conv{p_i} satisfies qP=q and q·1=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For every row p_i of P, p_i P=p_i and p_i·1=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** If q=sum_i alpha_i p_i with alpha_i>=0 and sum_i alpha_i=1, then linearity gives qP=q and q·1=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Writing D=q1-q0, one has DP=D and D·1=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For k in {0,1}, because q_k is a convex combination of rows, P^2=P and P1=1 imply q_k P=q_k and q_k·1=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Subtracting the k=0 identities from the k=1 identities yields (q1-q0)P=q1-q0 and (q1-q0)·1=0, i.e. DP=D and D·1=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For any affine chi(x)=L(x)+c, if DP=D and D·1=0 then sum_j D_j chi(p_j)=chi(q1)-chi(q0)=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By row-matrix multiplication, sum_j D_j p_j=DP.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Using chi(x)=L(x)+c and finite linearity, sum_j D_j chi(p_j)=L(sum_j D_j p_j)+c sum_j D_j=L(DP)+c(D·1)=L(D).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** The affine constant cancels between the endpoints, so chi(q1)-chi(q0)=L(q1-q0)=L(D); the endpoint normalization makes this difference 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Partitioning the finite index set into full row-point fibers Q gives sum_Q d_Q chi(p_Q)=sum_j D_j chi(p_j), where d_Q=sum_{j in Q}D_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The full row-point fibers Q partition the finite index set, and for every j in Q the row p_j equals the common row point p_Q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** For each fiber Q, sum_{j in Q} D_j chi(p_j)=(sum_{j in Q}D_j)chi(p_Q)=d_Q chi(p_Q); summing the finitely many fiber equalities gives the claimed regrouping.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

