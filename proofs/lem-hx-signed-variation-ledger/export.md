# Proof Export

## Node 1

**Statement:** For every finite exact signed idempotent P, every ordered pair (a,b) of points of the row polytope K(P), and every set S of full row-point fibers, sum_{Q in S} |d_Q| <= a^+(S) + b^+(S) + nu(a) + nu(b), where d_Q = sum_{j in Q}(a_j - b_j), r^+(S) = sum_{Q in S} sum_{j in Q} max(r_j,0), and nu(r) = sum_j max(-r_j,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix admissible P, a, b, and S. Since full row-point fibers are fibers of the index-to-row-point map, distinct Q in S are disjoint coordinate sets. Define S_+ = {Q in S : d_Q >= 0}, S_- = {Q in S : d_Q < 0}, U_+ = union_{Q in S_+} Q, and U_- = union_{Q in S_-} Q; thus S is the disjoint union of S_+ and S_-, and U_+ and U_- are disjoint coordinate unions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Writing r(U) = sum_{j in U} r_j, disjointness of the full fibers and d_Q = sum_{j in Q}(a_j-b_j) give the exact sign-split identity sum_{Q in S}|d_Q| = a(U_+) - b(U_+) + b(U_-) - a(U_-).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every finite real vector r and every coordinate subset U, with r^+(U) = sum_{j in U} max(r_j,0) and nu(r) = sum_j max(-r_j,0), one has -nu(r) <= r(U) <= r^+(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For each coordinate j, r_j <= max(r_j,0); summing over j in U gives r(U) <= r^+(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** For each coordinate j, r_j >= -max(-r_j,0); hence r(U) >= -sum_{j in U}max(-r_j,0) >= -sum_j max(-r_j,0) = -nu(r).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Applying the subset budget to a and b on U_+ gives a(U_+) - b(U_+) <= a^+(U_+) + nu(b).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Applying the subset budget to b and a on U_- gives b(U_-) - a(U_-) <= b^+(U_-) + nu(a).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Let n be finite, let a,b be real vectors indexed by {1,...,n}, and let S be a family of pairwise disjoint coordinate subsets. For d_Q := sum_{j in Q}(a_j-b_j), set S_+ := {Q in S : d_Q >= 0}, S_- := {Q in S : d_Q < 0}, U_+ := union_{Q in S_+} Q, and U_- := union_{Q in S_-} Q. Define r^+_coord(U) := sum_{j in U} max(r_j,0) for a coordinate set U and r^+_fib(T) := sum_{Q in T} sum_{j in Q} max(r_j,0) for a subfamily T of S. Then a^+_coord(U_+) <= a^+_fib(S) and b^+_coord(U_-) <= b^+_fib(S).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Let n be finite, let a,b be real vectors indexed by {1,...,n}, and let S be a family of pairwise disjoint coordinate subsets Q. For d_Q := sum_{j in Q}(a_j-b_j), define S_+ := {Q in S : d_Q >= 0}, S_- := {Q in S : d_Q < 0}, U_+ := union_{Q in S_+}Q, and U_- := union_{Q in S_-}Q. Distinguish the coordinate-set positive mass r^+_coord(U) := sum_{j in U} max(r_j,0) from the fiber-family positive mass r^+_fib(T) := sum_{Q in T} sum_{j in Q} max(r_j,0). Pairwise disjointness gives r^+_coord(U_+) = r^+_fib(S_+) and r^+_coord(U_-) = r^+_fib(S_-), because each coordinate in the respective union occurs in exactly one fiber. Since S_+ and S_- are subfamilies of S and every max(r_j,0) is nonnegative, r^+_fib(S_+) <= r^+_fib(S) and r^+_fib(S_-) <= r^+_fib(S). Hence a^+_coord(U_+) <= a^+_fib(S) and b^+_coord(U_-) <= b^+_fib(S), which are precisely the intended, now type-explicit inequalities in node 1.6.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Substituting the two sign estimates into the exact sign-split identity and then using positive-part monotonicity yields sum_{Q in S}|d_Q| <= a^+(S) + b^+(S) + nu(a) + nu(b), which is the asserted inequality for the arbitrary admissible P, a, b, and S.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

