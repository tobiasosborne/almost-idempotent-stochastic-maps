# Proof Export

## Node 1

**Statement:** D-restricted zero-sum fan payment: let (w_1, p_1), ..., (w_m, p_m) be a finite family with vectors w_i in R^d and weights p_i > 0 satisfying sum_i p_i = 1, such that every w_i has coordinate sum zero and the weighted barycenter is zero (sum_i p_i w_i = 0); write n(w) = sum_l max(-w(l), 0); let w_* be a minimizer of v -> sum_i p_i n(w_i - v) over {w_1, ..., w_m} and let A = { i : n(w_i - w_*) > 0 }; then sum_{i in A} p_i n(w_i - w_*) <= (2 + sqrt(2)) * sum_{i in A} p_i n(w_i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Setup: choose an index s with w_s = w_*; set B := {i : w_i = w_*}, q := sum_{i in B} p_i, r := sum_{i in A} p_i, D := sum_{i in A} p_i n(w_i), and N := sum_{i in A} p_i n(w_i - w_*). Then q > 0, A is the complement of B, r = 1 - q, every difference w_i - w_j has coordinate sum zero, and the root inequality is N <= (2 + sqrt(2))*D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Because w_* is a minimizer over the finite candidate set {w_1, ..., w_m}, w_* is itself one of the vectors in that set; choose s with w_s = w_*. Then s is in B, so q = sum_{i in B} p_i >= p_s > 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For each i, the difference w_i - w_* has coordinate sum zero. For any zero-sum vector x, n(x)=0 holds exactly when x=0: n(x)=0 means all coordinates are nonnegative, and coordinate sum zero then forces every coordinate to be 0. Hence n(w_i - w_*)=0 exactly when w_i=w_*, so A={i:n(w_i-w_*)>0} is the complement of B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Since A is the complement of B in {1,...,m} and sum_i p_i = 1, the abbreviations q := sum_{i in B} p_i and r := sum_{i in A} p_i satisfy r = 1 - q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Since every w_i has coordinate sum zero, every difference w_i - w_j also has coordinate sum zero. With N := sum_{i in A} p_i n(w_i - w_*) and D := sum_{i in A} p_i n(w_i), the inequality N <= (2+sqrt(2))*D is exactly the root inequality after substituting these abbreviations.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** First bound: in the setup of node 1.1, N <= D/q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For every i in A, w_* has coordinate sum zero, so lem-zerosum-triangle applied with w := w_i and v := w_* gives n(w_i - w_*) <= n(w_i) + n(w_*). Multiplying by p_i and summing over i in A gives N <= D + r*n(w_*).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Using node 1.1.2 that A is the complement of B in {1,...,m}, split the barycenter identity sum_i p_i w_i = 0 over the disjoint union B union A; since w_i = w_* on B and q := sum_{i in B} p_i, this gives q*w_* + sum_{i in A} p_i w_i = 0, hence -q*w_* = sum_{i in A} p_i w_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Node 1.1.2 says exactly that A is the complement of B in the full index set {1,...,m}; hence {1,...,m} is the disjoint union B union A. Therefore the barycenter identity sum_i p_i w_i = 0 may be written as sum_{i in B} p_i w_i + sum_{i in A} p_i w_i = 0. By the definition B := {i : w_i = w_*}, the first sum is (sum_{i in B} p_i) w_* = q*w_*. Substitution gives q*w_* + sum_{i in A} p_i w_i = 0, and moving the first term gives -q*w_* = sum_{i in A} p_i w_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Because w_* is zero-sum, n(-w_*) = n(w_*); because n is a sum of negative parts, n(c x)=c*n(x) for c>=0. Thus q*n(w_*) = n(-q*w_*) = n(sum_{i in A} p_i w_i). Repeated use of lem-negpart-subadditive gives n(sum_{i in A} p_i w_i) <= sum_{i in A} p_i n(w_i)=D, so q*n(w_*) <= D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Combining N <= D + r*n(w_*) with q*n(w_*) <= D and q>0 gives N <= D + (r/q)*D = ((q+r)/q)*D. Since r=1-q, q+r=1, so N <= D/q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** Nodes 1.2.1, 1.2.2, 1.2.3, and 1.2.4, using the setup facts q>0 and r=1-q from nodes 1.1.1 and 1.1.3, establish the first bound N <= D/q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Second bound: in the setup of node 1.1, if q < 1/2, then N <= (2*(1-q)/(1-2*q))*D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For each j in A, the minimizer property of w_* gives F(w_*) <= F(w_j), where F(v):=sum_i p_i n(w_i-v). Since A is the complement of B and w_i=w_* on B, F(w_*)=N; hence N <= F(w_j) for every j in A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Multiplying N <= F(w_j) by p_j and summing over j in A gives r*N <= sum_{j in A} p_j F(w_j). Expanding F(w_j) and splitting i over A and B gives sum_{j in A} p_j F(w_j) = sum_{i,j in A} p_i p_j n(w_i-w_j) + q*sum_{j in A} p_j n(w_*-w_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** For j in A, w_j-w_* is zero-sum, so n(w_*-w_j)=n(w_j-w_*). Therefore q*sum_{j in A} p_j n(w_*-w_j)=q*N.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** For i,j in A, w_j has coordinate sum zero, so lem-zerosum-triangle applied with w := w_i and v := w_j gives n(w_i-w_j) <= n(w_i)+n(w_j). Multiplying by p_i p_j and summing over A x A gives sum_{i,j in A} p_i p_j n(w_i-w_j) <= 2*r*D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.5

**Statement:** Combining the preceding inequalities gives r*N <= 2*r*D + q*N, so (r-q)*N <= 2*r*D. If q < 1/2, then r-q = 1-2*q > 0, and with r=1-q division gives N <= (2*(1-q)/(1-2*q))*D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.6

**Statement:** Nodes 1.3.1 through 1.3.5, using the setup facts that A is the complement of B, r=1-q, and differences are zero-sum from nodes 1.1.2, 1.1.3, and 1.1.4, establish the conditional second bound: if q < 1/2 then N <= (2*(1-q)/(1-2*q))*D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Envelope: nodes 1.1, 1.2, and 1.3 imply N <= (2 + sqrt(2))*D; substituting N = sum_{i in A} p_i n(w_i - w_*) and D = sum_{i in A} p_i n(w_i) from node 1.1 gives the root inequality.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Let C := 2 + sqrt(2) and q0 := 1/C. Then 0 < q0 < 1/2, C*q0 = 1, and a direct calculation gives 2*(1-q0)/(1-2*q0) = C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** If q >= q0, then the first bound N <= D/q from node 1.2 and D >= 0 give N <= D/q <= D/q0 = C*D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** If q < q0, then q < 1/2. The second bound from node 1.3 gives N <= 2*(1-q)/(1-2*q)*D, and since 0 <= q < q0, direct algebra gives 2*(1-q)/(1-2*q) <= C. Hence N <= C*D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.4

**Statement:** The two cases q >= q0 and q < q0 are exhaustive. Nodes 1.4.2 and 1.4.3 therefore give N <= C*D with C=2+sqrt(2). Using node 1.1 to substitute N=sum_{i in A} p_i n(w_i-w_*) and D=sum_{i in A} p_i n(w_i), this is exactly the root conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.4.1

**Statement:** Dependency check for this case-split step: node 1.2 is now epistemic_state=validated, and the other direct validation dependencies of node 1.4.4, namely 1.1, 1.3, 1.4.1, 1.4.2, and 1.4.3, are also validated. Therefore the earlier objection that 1.4.4 used an unvalidated direct dependency no longer applies; the case split may use the validated q >= q0 branch 1.4.2 and the validated q < q0 branch 1.4.3, with the substitution of N and D supplied by validated node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.4.2

**Statement:** All direct validation dependencies needed for node 1.4.4 are now satisfied: nodes 1.1, 1.2, 1.3, 1.4.1, 1.4.2, and 1.4.3 are each epistemic_state=validated. Hence the final inference in node 1.4.4 depends only on validated inputs: the exhaustive dichotomy q >= q0 or q < q0, the validated branch conclusions 1.4.2 and 1.4.3, and the validated setup/substitution facts in 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

