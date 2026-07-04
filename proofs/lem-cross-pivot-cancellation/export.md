# Proof Export

## Node 1

**Statement:** Cross-pivot cancellation: let P be a rank-3 exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let U = (u_0,u_1,u_2) be an actual-row chart whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, and define coordinates a_q(i) by p_i = sum_q a_q(i)p_{u_q} and beta_r(i) = P_{u_r i}; then for every pair of distinct indices r, s in {0,1,2}, sum_i beta_r(i)*a_s(i) = 0, the sum running over all row indices i of P.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** For every row index k of P, the row p_k is reproduced by the rows of P with coefficients from row k: p_k = sum_i P_{k i} p_i. Indeed, the j-th coordinate of the right hand side is sum_i P_{k i} P_{i j} = (P^2)_{k j} = P_{k j}, using def-signed-idempotent (P^2 = P).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Specializing the previous row-reproduction identity to k = u_r and using beta_r(i) = P_{u_r i} gives p_{u_r} = sum_i beta_r(i) p_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Substituting the chart-coordinate expansion p_i = sum_q a_q(i) p_{u_q} into p_{u_r} = sum_i beta_r(i) p_i and collecting the finite sums gives p_{u_r} = sum_q (sum_i beta_r(i)*a_q(i)) p_{u_q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By the coordinate definition in the root statement, for every row index i one has p_i = sum_q a_q(i) p_{u_q}, where q ranges over {0,1,2}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Under the root hypotheses, p_{u_r} = sum_i beta_r(i) p_i: by P^2 = P, the j-th coordinate of sum_i P_{u_r i} p_i is sum_i P_{u_r i} P_{i j} = (P^2)_{u_r j} = P_{u_r j}, and beta_r(i) = P_{u_r i}. By the root definition of the chart coordinates, each row has p_i = sum_q a_q(i) p_{u_q}, with q in {0,1,2}. Substituting these expansions gives p_{u_r} = sum_i beta_r(i) (sum_q a_q(i) p_{u_q}); since the row-index set is finite and q ranges over the finite set {0,1,2}, scalar distributivity and interchange of finite sums give p_{u_r} = sum_q (sum_i beta_r(i)*a_q(i)) p_{u_q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** The premises used in this node are now explicit: node 1.2 supplies p_{u_r} = sum_i beta_r(i) p_i, and validated node 1.3.1 supplies, for every row index i, the chart expansion p_i = sum_q a_q(i) p_{u_q} with q in {0,1,2}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Substituting the expansion from node 1.3.1 into the equality from node 1.2 gives p_{u_r} = sum_i beta_r(i) (sum_q a_q(i) p_{u_q}). This is just replacement of each p_i by its defining three-term chart expansion inside the finite row-index sum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.3

**Statement:** For each row index i, scalar distribution gives beta_r(i) (sum_q a_q(i) p_{u_q}) = sum_q (beta_r(i)*a_q(i)) p_{u_q}. Hence p_{u_r} = sum_i sum_q (beta_r(i)*a_q(i)) p_{u_q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.4

**Statement:** The row-index set is finite because P is a square real matrix, and q ranges over the finite set {0,1,2}. Therefore the double finite sum may be interchanged and regrouped by q, yielding p_{u_r} = sum_q (sum_i beta_r(i)*a_q(i)) p_{u_q}, which is the claimed collected expansion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Because p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, coordinates in that chart are unique. The coordinate vector of p_{u_r} in this ordered basis is the standard vector with q-coordinate delta_{q r}; comparing with the previous expansion yields sum_i beta_r(i)*a_q(i) = delta_{q r} for each q in {0,1,2}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The ordered rows p_{u_0}, p_{u_1}, p_{u_2} are assumed in the root statement to form a basis of the row space; hence any vector in the row space has at most one expansion as sum_q c_q p_{u_q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** For the chart row p_{u_r}, the standard expansion is p_{u_r} = sum_q delta_{q r} p_{u_q}, because exactly the r-th coefficient is 1 and the other two coefficients are 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** Using the row-reproduction specialization p_{u_r} = sum_i beta_r(i)*p_i and the defining chart-coordinate expansions p_i = sum_q a_q(i)*p_{u_q}, finite distributivity gives p_{u_r} = sum_q (sum_i beta_r(i)*a_q(i))*p_{u_q}. Comparing this expansion with the standard expansion p_{u_r} = sum_q delta_{q r}*p_{u_q} via uniqueness in the ordered basis p_{u_0}, p_{u_1}, p_{u_2}, each coefficient agrees, so sum_i beta_r(i)*a_q(i) = delta_{q r} for every q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.3.1

**Statement:** By node 1.2, p_{u_r} = sum_i beta_r(i)*p_i. By the chart-coordinate definition recorded in node 1.3.1, each p_i = sum_q a_q(i)*p_{u_q}. Substitution gives p_{u_r} = sum_i beta_r(i)*(sum_q a_q(i)*p_{u_q}); since the row-index set and {0,1,2} are finite, bilinearity of scalar multiplication and addition permits distributing beta_r(i) and interchanging the finite sums, yielding p_{u_r} = sum_q (sum_i beta_r(i)*a_q(i))*p_{u_q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.3.2

**Statement:** By node 1.4.2, the same vector p_{u_r} has the standard basis expansion p_{u_r} = sum_q delta_{q r}*p_{u_q}: the coefficient of p_{u_r} is 1 and the coefficients of the other two chart rows are 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.3.3

**Statement:** Nodes 1.4.3.1 and 1.4.3.2 are two expansions of the same vector p_{u_r} in the ordered basis p_{u_0}, p_{u_1}, p_{u_2}. By the uniqueness statement in node 1.4.1, the coefficient tuples must be equal coordinatewise. Therefore, for every q in {0,1,2}, sum_i beta_r(i)*a_q(i) = delta_{q r}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Taking q = s in the coordinate identity gives sum_i beta_r(i)*a_s(i) = delta_{s r}; since r and s are distinct, delta_{s r} = 0, which is exactly the claimed cross-pivot cancellation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Fix distinct r,s in {0,1,2} under the root hypotheses. Since P^2 = P, for each coordinate j the j-th coordinate of sum_i P_{u_r i} p_i is sum_i P_{u_r i} P_{i j} = (P^2)_{u_r j} = P_{u_r j} = (p_{u_r})_j. Using beta_r(i) = P_{u_r i}, this gives p_{u_r} = sum_i beta_r(i) p_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Substitute the defining chart expansion p_i = sum_q a_q(i) p_{u_q} into p_{u_r} = sum_i beta_r(i) p_i. The row index set and q in {0,1,2} are finite, so distributing scalars and interchanging the finite sums gives p_{u_r} = sum_q (sum_i beta_r(i)*a_q(i)) p_{u_q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** The rows p_{u_0}, p_{u_1}, p_{u_2} form an ordered basis of the row space, so coordinates in that basis are unique. The standard expansion of p_{u_r} is p_{u_r} = sum_q delta_{q r} p_{u_q}. Comparing this expansion with p_{u_r} = sum_q (sum_i beta_r(i)*a_q(i)) p_{u_q} gives sum_i beta_r(i)*a_q(i) = delta_{q r} for every q in {0,1,2}, and in particular sum_i beta_r(i)*a_s(i) = delta_{s r}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.4

**Statement:** Because r and s are distinct, delta_{s r} = 0. Therefore sum_i beta_r(i)*a_s(i) = 0, with the sum over all row indices i of P, which is the asserted cross-pivot cancellation for this pair r,s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.5

**Statement:** Nodes 1.5.1 through 1.5.4 compose the local proof of node 1.5: 1.5.1 gives row reproduction for p_{u_r}; 1.5.2 converts that equality into chart coordinates; 1.5.3 identifies the s-coordinate as delta_{s r} by basis uniqueness; and 1.5.4 uses r != s to make that coordinate zero. Therefore the statement of node 1.5 follows without using sibling node 1.4 as a dependency.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

