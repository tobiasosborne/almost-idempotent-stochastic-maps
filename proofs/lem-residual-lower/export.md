# Proof Export

## Node 1

**Statement:** Convex outsourcing: let C be the convex hull of finitely many points of R^n, and suppose p = sum_{j=1}^m c_j p_j + (1 - s) q with points p_j, q in R^n, coefficients c_j >= 0, s = sum_{j=1}^m c_j < 1, and dist_1(p_j, C) <= dist_1(p, C) for every j; then dist_1(p, C) <= dist_1(q, C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let D = dist_1(p, C) and d = dist_1(q, C). Since C is a finite convex hull in R^n, C is compact and convex, and the l1 distance to C is attained: for each j choose r_j in C with ||p_j - r_j||_1 = dist_1(p_j, C), and choose r in C with ||q - r||_1 = d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** A convex hull of finitely many points of R^n is the image of a standard simplex under an affine map, hence it is compact; by definition it is convex.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For any fixed x in R^n, the function z -> ||x - z||_1 is continuous on C, so compactness of C gives a minimizer z_x in C with ||x - z_x||_1 = dist_1(x, C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Apply the preceding minimizer fact with x = p_j for each j and with x = q; name the resulting minimizers r_j and r, and set D = dist_1(p, C), d = dist_1(q, C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The comparison point r_star := sum_{j=1}^m c_j r_j + (1 - s) r belongs to C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Each r_j and r lies in C by the nearest-point choices from node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** This membership step depends on node 1.1: node 1.1 explicitly chooses, for each j, a point r_j in C and also chooses r in C. Therefore the assertions r_j in C for every j and r in C are exactly part of those choices; no nearest-point property beyond the membership specified in the choices is being used here.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The coefficients c_j are nonnegative, and 1 - s is positive because s < 1; moreover sum_{j=1}^m c_j + (1 - s) = s + (1 - s) = 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Since C is convex, any finite convex combination of points of C with nonnegative coefficients summing to 1 lies in C; applying this to the points r_j and r gives r_star in C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** Use node 1.2.1 for the membership premise (r_j in C for every j and r in C) and node 1.2.2 for the coefficient premise (c_j >= 0, 1-s > 0, and sum_j c_j + (1-s) = 1). With these premises declared, the list r_1,...,r_m,r with weights c_1,...,c_m,1-s is a finite convex combination of points of C. Since C is convex, that convex combination lies in C; by the definition of r_star, this point is r_star, hence r_star in C.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.2.3.2

**Statement:** Dependency-bearing bridge: this step has validation dependencies on node 1.2.1 for the membership premise r_j in C for every j and r in C, and on node 1.2.2 for the coefficient premise c_j >= 0, 1-s > 0, and sum_j c_j + (1-s) = 1. Once those dependency nodes are validated, r_star = sum_j c_j r_j + (1-s)r is a finite convex combination of points of C; therefore convexity of C implies r_star in C. Until node 1.2.1 is validated, this step remains blocked and makes no standalone use of the membership premise.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.3.2.1

**Statement:** Challenge response for ch-e657d7b871ac7728: this bridge does not use node 1.2.1 as a currently validated premise. It requires validation of nodes 1.2.1 and 1.2.2. Once 1.2.1 is validated, it supplies exactly r_j in C for every j and r in C; once 1.2.2 is validated, it supplies c_j >= 0, 1-s > 0, and sum_j c_j + (1-s) = 1. Under those validated dependencies, r_star = sum_j c_j r_j + (1-s)r is a finite convex combination of points of C, so convexity of C gives r_star in C. Until 1.2.1 is validated, this child and its parent remain blocked, so no unvalidated membership premise is being used.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.3

**Statement:** For this r_star one has D <= ||p - r_star||_1 <= sum_{j=1}^m c_j ||p_j - r_j||_1 + (1 - s)||q - r||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Because r_star belongs to C by node 1.2 and D = dist_1(p, C), the definition of distance to a set gives D <= ||p - r_star||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** This step explicitly depends on node 1.2: once node 1.2 is validated, its statement gives r_star in C. For distance to a set, D = dist_1(p,C) is the infimum of ||p-y||_1 over y in C, so every particular y in C satisfies D <= ||p-y||_1. Applying this to y = r_star gives D <= ||p-r_star||_1.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Corrected dependency-bearing proof of the parent step: use node 1.2 for r_star in C and node 1.1.3 for the binding D = dist_1(p,C). With those two validated inputs, the definition of distance to a set gives D <= ||p-r_star||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.1.2.1

**Statement:** Dependency-bearing bridge for the distance comparison: this child depends on nodes 1.2 and 1.1.3 and requires both to be validated. Node 1.2 gives r_star in C. Node 1.1.3 sets D = dist_1(p,C). By definition, dist_1(p,C) is the infimum of ||p-y||_1 over y in C, so every y in C satisfies D <= ||p-y||_1. Taking y = r_star gives D <= ||p-r_star||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Substituting p = sum_{j=1}^m c_j p_j + (1 - s) q and r_star = sum_{j=1}^m c_j r_j + (1 - s) r gives p - r_star = sum_{j=1}^m c_j (p_j - r_j) + (1 - s)(q - r).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** The l1 triangle inequality and absolute homogeneity give ||sum_{j=1}^m c_j (p_j - r_j) + (1 - s)(q - r)||_1 <= sum_{j=1}^m c_j ||p_j - r_j||_1 + (1 - s)||q - r||_1, since c_j >= 0 and 1 - s >= 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Combining the preceding three statements yields D <= ||p - r_star||_1 <= sum_{j=1}^m c_j ||p_j - r_j||_1 + (1 - s)||q - r||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The hypotheses and the nearest-point choices give sum_{j=1}^m c_j ||p_j - r_j||_1 + (1 - s)||q - r||_1 <= s D + (1 - s) d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** For every j, the choice of r_j gives ||p_j - r_j||_1 = dist_1(p_j, C), and the hypothesis gives dist_1(p_j, C) <= D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Since each c_j >= 0, multiplying the inequalities ||p_j - r_j||_1 <= D by c_j and summing gives sum_{j=1}^m c_j ||p_j - r_j||_1 <= (sum_{j=1}^m c_j) D = s D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** The choice of r gives ||q - r||_1 = d, so (1 - s)||q - r||_1 = (1 - s)d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.3.1

**Statement:** Dependency-bearing bridge for the minimizer equality: node 1.1.3 applies the nearest-point/minimizer fact with x = q, names the resulting minimizer r, and sets d = dist_1(q, C). Therefore that imported choice gives ||q - r||_1 = d. Multiplying this equality by the scalar 1 - s gives (1 - s)||q - r||_1 = (1 - s)d; no additional nearest-point premise is being assumed inside 1.4.3.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.4.3.2

**Statement:** Dependency-bearing bridge for the minimizer equality: this step depends on node 1.1.3. Node 1.1.3 applies the nearest-point/minimizer fact with x = q, names the resulting minimizer r, and sets d = dist_1(q, C). Therefore that imported choice gives ||q - r||_1 = d. Multiplying this equality by the scalar 1 - s gives (1 - s)||q - r||_1 = (1 - s)d; no additional nearest-point premise is being assumed inside 1.4.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.4

**Statement:** Adding the two bounds gives sum_{j=1}^m c_j ||p_j - r_j||_1 + (1 - s)||q - r||_1 <= s D + (1 - s)d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Because D <= s D + (1 - s) d and s < 1, it follows that D <= d, i.e. dist_1(p, C) <= dist_1(q, C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Combining node 1.3 with node 1.4 gives D <= s D + (1 - s)d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.1

**Statement:** Dependency-bearing bridge for the combination: this step depends on nodes 1.3 and 1.4 and requires both to be validated. Let A = sum_{j=1}^m c_j ||p_j - r_j||_1 + (1 - s)||q - r||_1. Node 1.3 gives D <= ||p - r_star||_1 <= A, hence D <= A. Node 1.4 gives A <= s D + (1 - s)d. By transitivity of <=, D <= s D + (1 - s)d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.1.1.1

**Statement:** Challenge response for ch-9e721809b5c36eec: this bridge is not an unconditional proof from pending premises. It is a dependency-bearing step whose only nonlocal inputs are nodes 1.3 and 1.4, and it requires both to be validated before this child can be accepted. Once 1.3 is validated, it supplies D <= ||p - r_star||_1 <= A, where A = sum_{j=1}^m c_j ||p_j - r_j||_1 + (1 - s)||q - r||_1, hence D <= A. Once 1.4 is validated, it supplies A <= s D + (1 - s)d. Transitivity of <= then gives D <= s D + (1 - s)d. Until nodes 1.3 and 1.4 validate, this child remains blocked and does not validate the inequality.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Subtracting s D from both sides gives (1 - s)D <= (1 - s)d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** Because s < 1, the scalar 1 - s is positive, so division by 1 - s preserves the inequality and yields D <= d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.4

**Statement:** By the definitions D = dist_1(p, C) and d = dist_1(q, C), the inequality D <= d is exactly dist_1(p, C) <= dist_1(q, C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.4.1

**Statement:** Dependency-bearing bridge for the final substitution: this step depends on nodes 1.5.3 and 1.1.3. Node 1.5.3 gives D <= d. Node 1.1.3 sets D = dist_1(p, C) and d = dist_1(q, C) after applying the minimizer setup to p_j and q. Substituting these two recorded equalities into D <= d gives exactly dist_1(p, C) <= dist_1(q, C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

