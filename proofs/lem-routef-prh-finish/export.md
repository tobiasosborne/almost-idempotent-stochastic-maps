# Proof Export

## Node 1

**Statement:** Route F PRH finish: let A:l-infinity(k)->l-infinity(n) and M:l-infinity(n)->l-infinity(k) be positive unital maps and let Q be row-stochastic; if K >= 1, 0 <= eta <= min{(24*K)^(-1),1}, ||Q-AM||_{infinity->infinity} <= K*eta, and ||MA-I||_{infinity->infinity} <= 3*K*eta/(1-3*K*eta), then there is a stochastic idempotent E with ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Scalar preparation: under K >= 1 and 0 <= eta <= min{(24*K)^(-1),1}, define epsilon := 3*K*eta/(1-3*K*eta); then 0 <= epsilon < 1/2, epsilon <= 4*K*eta, and K*eta <= K*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** From K >= 1 and 0 <= eta <= (24*K)^(-1), positivity of K gives 0 <= x := 3*K*eta <= 1/8, hence 1-x >= 7/8 > 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For 0 <= x <= 1/8 and epsilon := x/(1-x), division by the positive denominator gives 0 <= epsilon <= (8/7)*x <= 1/7 < 1/2; since x=3*K*eta, also epsilon <= (24/7)*K*eta <= 4*K*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** For 0 <= eta <= 1, one has eta^2 <= eta; since eta and sqrt(eta) are nonnegative, equivalently eta <= sqrt(eta), and multiplication by K >= 1 yields K*eta <= K*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** PRH conclusion with an exhaustive dimension split: for epsilon := 3*K*eta/(1-3*K*eta), if 0 <= epsilon < 1/2 and ||MA-I||_{infinity->infinity} <= epsilon, then there exists a stochastic idempotent E:l-infinity(n)->l-infinity(n) with ||AM-E||_{infinity->infinity} <= 2*sqrt(2*epsilon). If k,n >= 1, this follows by applying the exact external lem-prh to A and M; otherwise the existence of both positive unital maps forces k=n=0 (the mixed zero-dimensional cases are impossible), and the unique endomorphism of l-infinity(0) is such an E with ||AM-E||_{infinity->infinity}=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Dimension-domain bridge for PRH: either k,n >= 1, in which case the positive unital maps A and M have probability-vector rows and satisfy the structural and dimension hypotheses of lem-prh, or k=n=0, in which case the unique endomorphism E of l-infinity(0) is a stochastic idempotent with ||AM-E||_{infinity->infinity}=0 and directly satisfies the conclusion required in node 1.2; the mixed cases k=0<n and n=0<k are incompatible with the existence of both displayed positive unital maps.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** The symbols k and n are dimensions of finite l-infinity spaces, hence nonnegative integers. In the branch k >= 1 and n >= 1, def-positive-approximate-retract identifies A and M as positive unital maps with probability-vector rows, so together with these dimension inequalities they satisfy every structural and dimension premise of lem-prh.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.2

**Statement:** The mixed zero-dimensional cases cannot occur. If k=0<n, then A:l-infinity(0)->l-infinity(n) would have n positive-unital probability rows of length zero, but the unique empty row has coordinate sum 0 and is not a probability vector of total mass 1. If n=0<k, the same argument applied to M:l-infinity(0)->l-infinity(k) gives a contradiction. Consequently, if k,n are not both at least 1, existence of both displayed positive unital maps forces k=n=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.3

**Statement:** If k=n=0, l-infinity(0) is the zero vector space and its unique endomorphism E is the empty 0-by-0 matrix. It is entrywise nonnegative, satisfies E*1=1 because both vectors are the unique zero vector, and satisfies E^2=E; hence E is a stochastic idempotent by def-stochastic. Moreover AM=E, so ||AM-E||_{infinity->infinity}=0 <= 2*sqrt(2*epsilon) since epsilon >= 0. Thus the existential conclusion of node 1.2 holds directly in the degenerate case, without applying lem-prh.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.4

**Statement:** The alternatives are exhaustive: either k,n >= 1 and lem-prh is legitimately applicable to A and M, or k=n=0 and the preceding explicit E proves the needed conclusion directly. This supplies the missing dimension-domain bridge and does not invoke lem-prh outside its stated k,n >= 1 domain.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** With epsilon := 3*K*eta/(1-3*K*eta), the assumed inequality ||MA-I||_{infinity->infinity} <= 3*K*eta/(1-3*K*eta) is exactly ||MA-I_k||_{infinity->infinity} <= epsilon, while this branch assumes 0 <= epsilon < 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Dimension split for the PRH conclusion: if k,n >= 1, the exact external lem-prh applied to A, M, and epsilon produces a stochastic idempotent E:l-infinity(n)->l-infinity(n) with ||AM-E||_{infinity->infinity} <= 2*sqrt(2*epsilon); if one dimension is zero, positivity and unitality force k=n=0 and the unique zero-dimensional map supplies such an E. Hence in all cases such a stochastic idempotent E exists; stochastic idempotent has the meaning fixed by def-stochastic.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** By def-positive-approximate-retract, the matrices of A:l-infinity(k)->l-infinity(n) and M:l-infinity(n)->l-infinity(k) have probability-vector rows. Since k,n are nonnegative integer dimensions, if k=0<n then every row of the n-by-0 matrix A has coordinate sum 0, contradicting the required probability-row sum 1; similarly, if n=0<k then every row of the k-by-0 matrix M has sum 0, again contradicting sum 1. Consequently exactly one of the following dimension regimes holds: k,n >= 1, or k=n=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** In the regime k,n >= 1, node 1.2.1 supplies the positive-unital (probability-row) hypotheses and node 1.2.2 supplies 0 <= epsilon < 1/2 together with ||MA-I_k||_{infinity->infinity} <= epsilon. All hypotheses of the exact external lem-prh are therefore met, so it yields a stochastic idempotent E:l-infinity(n)->l-infinity(n) satisfying ||AM-E||_{infinity->infinity} <= 2*sqrt(2*epsilon).

**Type:** case

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.3

**Statement:** In the regime k=n=0, let E be the unique linear endomorphism of l-infinity(0)={0}, equivalently the empty 0-by-0 matrix. It is entrywise nonnegative, sends the unique all-ones vector (the empty vector, equal to 0) to itself, and satisfies E^2=E; hence it is a stochastic idempotent by def-stochastic. Also AM=E=0, so ||AM-E||_{infinity->infinity}=0 <= 2*sqrt(2*epsilon), since epsilon >= 0 by node 1.2.2.

**Type:** case

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.4

**Statement:** The exhaustive dichotomy in 1.2.3.1, combined with the constructions in 1.2.3.2 and 1.2.3.3, proves that in every allowed dimension there exists a stochastic idempotent E with ||AM-E||_{infinity->infinity} <= 2*sqrt(2*epsilon).

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Norm finish: under K >= 1, 0 <= eta <= 1, 0 <= epsilon <= 4*K*eta, K*eta <= K*sqrt(eta), ||Q-AM||_{infinity->infinity} <= K*eta, and ||AM-E||_{infinity->infinity} <= 2*sqrt(2*epsilon), the triangle inequality and monotonicity of square roots imply ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Because Q-E=(Q-AM)+(AM-E), the triangle inequality for the infinity-to-infinity operator norm gives ||Q-E||_{infinity->infinity} <= ||Q-AM||_{infinity->infinity}+||AM-E||_{infinity->infinity} <= K*eta+2*sqrt(2*epsilon).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Since 0 <= epsilon <= 4*K*eta and K,eta are nonnegative, square-root monotonicity and multiplicativity on nonnegative reals give 2*sqrt(2*epsilon) <= 2*sqrt(8*K*eta) = 4*sqrt(2*K)*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Combining the preceding bounds and K*eta <= K*sqrt(eta) gives ||Q-E||_{infinity->infinity} <= K*sqrt(eta)+4*sqrt(2*K)*sqrt(eta) = (K+4*sqrt(2*K))*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Synthesis: node 1.1 supplies 0 <= epsilon < 1/2, epsilon <= 4*K*eta, and K*eta <= K*sqrt(eta) for epsilon=3*K*eta/(1-3*K*eta); node 1.2 applies lem-prh to furnish a stochastic idempotent E with the AM-to-E bound; node 1.3 then yields the required Q-to-E estimate, proving the root existential conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

