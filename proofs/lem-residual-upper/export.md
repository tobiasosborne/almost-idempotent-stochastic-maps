# Proof Export

## Node 1

**Statement:** Residual distance bound: let C be the convex hull of finitely many points of R^n, let b_1..b_M, c_1..c_N >= 0 with m = sum_j b_j - sum_k c_k > 0, let p_j, r_k be points of R^n with q = (sum_j b_j p_j - sum_k c_k r_k) / m, and let D_k >= 0 satisfy ||x - r_k||_1 <= D_k for all x in C and each k; then m * dist_1(q, C) <= sum_j b_j * dist_1(p_j, C) + sum_k c_k * D_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Because C is a nonempty finite convex hull in R^n, it is compact; hence for every j there exists beta_j in C with ||p_j - beta_j||_1 = dist_1(p_j, C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** A nonempty convex hull of finitely many points in R^n is compact, and for each fixed p_j the map y -> ||p_j - y||_1 is continuous on C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** A continuous real-valued function on compact C attains its minimum, so choose beta_j in C minimizing y -> ||p_j - y||_1; by the definition of dist_1(p_j, C) as this infimum, ||p_j - beta_j||_1 = dist_1(p_j, C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Let B = sum_j b_j and G = sum_k c_k. Since m = B - G > 0 and all c_k >= 0, B = m + G > 0; therefore beta = (sum_j b_j beta_j) / B is a convex combination of points of C and so beta lies in C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Because every c_k is nonnegative, G = sum_k c_k is nonnegative; from m = B - G and m > 0 we get B = m + G > 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For each j, lambda_j = b_j / B is nonnegative because b_j >= 0 and B > 0, and sum_j lambda_j = (sum_j b_j) / B = 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** The point beta = sum_j lambda_j beta_j is therefore a convex combination of the points beta_j in C; since C is convex, beta lies in C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** With beta as above and q = (sum_j b_j p_j - sum_k c_k r_k) / m, the vector identity m*(q - beta) = sum_j b_j*(p_j - beta_j) + sum_k c_k*(beta - r_k) holds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Multiplying the definition of q by m gives m*q = sum_j b_j*p_j - sum_k c_k*r_k, so m*(q - beta) = sum_j b_j*p_j - sum_k c_k*r_k - m*beta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** From B = sum_j b_j and beta = (sum_j b_j*beta_j)/B we have B*beta = sum_j b_j*beta_j; from G = sum_k c_k we have G*beta = sum_k c_k*beta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Since m = B - G, m*beta = B*beta - G*beta = sum_j b_j*beta_j - sum_k c_k*beta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.1

**Statement:** In the current setup, B = sum_j b_j, G = sum_k c_k, and the root hypothesis gives m = sum_j b_j - sum_k c_k; hence m = B - G, so scalar distributivity gives m*beta = (B - G)*beta = B*beta - G*beta.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

##### Node 1.3.3.2

**Statement:** The validated node 1.3.2 supplies the identities B*beta = sum_j b_j*beta_j and G*beta = sum_k c_k*beta.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.3.3.3

**Statement:** Combining 1.3.3.1 with the two identities from 1.3.3.2, substitute B*beta = sum_j b_j*beta_j and G*beta = sum_k c_k*beta into m*beta = B*beta - G*beta to obtain m*beta = sum_j b_j*beta_j - sum_k c_k*beta, which is the asserted equality chain.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.3.3.3.1

**Statement:** The dependency-scoping premise is now satisfied: the declared dependencies 1.3.3.1 and 1.3.3.2 are validated in this workspace. Node 1.3.3.1 supplies m*beta = B*beta - G*beta, and node 1.3.3.2 supplies B*beta = sum_j b_j*beta_j and G*beta = sum_k c_k*beta. Substituting these two validated identities into the validated equality m*beta = B*beta - G*beta gives m*beta = sum_j b_j*beta_j - sum_k c_k*beta, with no appeal to an unvalidated premise.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.3.3.3.2

**Statement:** Because dependencies 1.3.3.1 and 1.3.3.2 are validated and are declared as the only inputs for this node, the substitution is now dependency-scoped: 1.3.3.1 gives m*beta = B*beta - G*beta, while 1.3.3.2 gives B*beta = sum_j b_j*beta_j and G*beta = sum_k c_k*beta; replacing B*beta and G*beta in the first equality by these equal vectors yields m*beta = sum_j b_j*beta_j - sum_k c_k*beta.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Substituting this expression for m*beta into m*(q - beta) and regrouping gives sum_j b_j*(p_j - beta_j) + sum_k c_k*(beta - r_k).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The positive-part residual satisfies ||sum_j b_j*(p_j - beta_j)||_1 <= sum_j b_j * dist_1(p_j, C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** By the triangle inequality for the l1 norm, ||sum_j b_j*(p_j - beta_j)||_1 <= sum_j ||b_j*(p_j - beta_j)||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Because b_j >= 0, absolute homogeneity gives ||b_j*(p_j - beta_j)||_1 = b_j*||p_j - beta_j||_1 for every j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** By the chosen beta_j, ||p_j - beta_j||_1 = dist_1(p_j, C) for every j; substituting this into the preceding sum gives the stated bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The negative-part residual satisfies ||sum_k c_k*(beta - r_k)||_1 <= sum_k c_k * D_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** By the triangle inequality and absolute homogeneity for the l1 norm, using c_k >= 0, ||sum_k c_k*(beta - r_k)||_1 <= sum_k c_k*||beta - r_k||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Since beta lies in C and the hypotheses give ||x - r_k||_1 <= D_k for every x in C and each k, taking x = beta yields ||beta - r_k||_1 <= D_k for every k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.2.1

**Statement:** Within this proof, beta in C is supplied by the earlier beta-in-C step 1.2: B = sum_j b_j is positive, beta = (sum_j b_j beta_j)/B = sum_j (b_j/B) beta_j, the coefficients b_j/B are nonnegative and sum to 1, each beta_j lies in C, and C is convex; hence beta lies in C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.2.1.1

**Statement:** By validated node 1.2, beta lies in C. That node proves the needed convex-combination fact from B=sum_j b_j, G=sum_k c_k, m=B-G>0, c_k>=0, b_j>=0, the chosen beta_j in C, and convexity of C; hence the present node may use beta in C through its declared dependency on 1.2.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.5.2.1.2

**Statement:** By validated node 1.2, beta lies in C. Node 1.2 proves the needed convex-combination fact: B=sum_j b_j and G=sum_k c_k satisfy B=m+G>0, the coefficients b_j/B are nonnegative and sum to 1, and beta=sum_j (b_j/B) beta_j is a convex combination of points beta_j in C. Since C is convex, beta lies in C, so the beta-in-C premise used by 1.5.2.1 is supplied by this declared validated dependency.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.5.2.2

**Statement:** For each fixed k, the root hypothesis on D_k is the universal statement: for every x in C, ||x - r_k||_1 <= D_k. Applying that statement to the particular admissible point x = beta, using beta in C from 1.5.2.1, gives ||beta - r_k||_1 <= D_k. Since k was arbitrary, the inequality holds for every k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.1

**Statement:** The admissibility premise beta in C is supplied here by the validated dependency 1.2: node 1.2 proves that, with B = sum_j b_j > 0 and beta = (sum_j b_j beta_j)/B, beta is a convex combination of points beta_j in C, hence beta lies in C. This child records that beta in C is in scope for the universal-instantiation step below.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.1.1

**Statement:** Dependency-scoped repair for ch-390c4b1b8facde9b: this child depends directly on validated node 1.2. Node 1.2 proves that B=sum_j b_j and G=sum_k c_k satisfy B=m+G>0, that beta=(sum_j b_j beta_j)/B is the convex combination sum_j (b_j/B) beta_j of points beta_j in C, and hence beta lies in C. Therefore the beta-in-C premise asserted by node 1.5.2.2.1 is now supplied through an actual logical dependency, not merely through validation gating.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.2

**Statement:** Fix an index k. The root hypothesis on D_k says that every x in C satisfies ||x - r_k||_1 <= D_k. By 1.5.2.2.1, beta lies in C; substituting x = beta into that universal statement therefore gives ||beta - r_k||_1 <= D_k for this fixed k.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.2.1

**Statement:** Dependency-scoped repair for ch-a60b50ea300c848a: this fixed-k step does not rely on pending node 1.5.2.2.1. It depends directly on validated node 1.2, which proves beta lies in C. The root hypothesis for the chosen negative index k says that every x in C satisfies ||x - r_k||_1 <= D_k. Since beta is in C by node 1.2, universal instantiation of that hypothesis at x = beta gives ||beta - r_k||_1 <= D_k for this fixed k.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.3

**Statement:** Because the preceding argument fixed only an arbitrary index k and used no property of k other than being one of the listed negative-part indices, the conclusion ||beta - r_k||_1 <= D_k holds for every k.

**Type:** claim

**Inference:** universal_generalization

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.3.1

**Statement:** Dependency-scoped repair for ch-96a8b58a8d27cb95: the universal conclusion is proved directly and does not use pending node 1.5.2.2.2. By validated node 1.2, beta lies in C. Now fix an arbitrary listed negative-part index k. The root hypothesis for D_k says that every x in C satisfies ||x - r_k||_1 <= D_k. Since beta lies in C, universal instantiation at x = beta gives ||beta - r_k||_1 <= D_k for this arbitrary k. Therefore, by universal generalization over the listed indices k, ||beta - r_k||_1 <= D_k holds for every k.

**Type:** claim

**Inference:** universal_generalization

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** Multiplying the inequalities ||beta - r_k||_1 <= D_k by c_k >= 0 and summing over k gives sum_k c_k*||beta - r_k||_1 <= sum_k c_k*D_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Since beta lies in C and m > 0, m * dist_1(q, C) <= ||m*(q - beta)||_1; combining the identity with the triangle inequality and the two residual bounds gives the claimed inequality.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Because beta lies in C, dist_1(q, C) <= ||q - beta||_1; because m > 0, multiplying gives m*dist_1(q, C) <= m*||q - beta||_1 = ||m*(q - beta)||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** Using the identity from node 1.3 and the l1 triangle inequality gives ||m*(q - beta)||_1 <= ||sum_j b_j*(p_j - beta_j)||_1 + ||sum_k c_k*(beta - r_k)||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.6.2.1

**Statement:** Under the root hypotheses and the earlier choices B = sum_j b_j, G = sum_k c_k, beta = (sum_j b_j*beta_j)/B, and m = B - G, the identity used here follows directly: multiplying q = (sum_j b_j*p_j - sum_k c_k*r_k)/m by m gives m*q = sum_j b_j*p_j - sum_k c_k*r_k, while m*beta = (B-G)*beta = sum_j b_j*beta_j - sum_k c_k*beta; subtracting these two displayed equations gives m*(q - beta) = sum_j b_j*(p_j - beta_j) + sum_k c_k*(beta - r_k).

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

##### Node 1.6.2.2

**Statement:** Let A = sum_j b_j*(p_j - beta_j) and N = sum_k c_k*(beta - r_k). By node 1.6.2.1, m*(q - beta) = A + N; therefore the l1 triangle inequality gives ||m*(q - beta)||_1 = ||A + N||_1 <= ||A||_1 + ||N||_1 = ||sum_j b_j*(p_j - beta_j)||_1 + ||sum_k c_k*(beta - r_k)||_1.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

#### Node 1.6.3

**Statement:** The final inequality follows by a local chain: beta in C and m>0 give m*dist_1(q,C) <= ||m*(q-beta)||_1; the identity m*(q-beta)=sum_j b_j*(p_j-beta_j)+sum_k c_k*(beta-r_k) and the l1 triangle inequality bound this by the sum of the positive and negative residual norms; those residual norms are bounded respectively by sum_j b_j*dist_1(p_j,C) and sum_k c_k*D_k. Therefore m*dist_1(q,C) <= sum_j b_j*dist_1(p_j,C) + sum_k c_k*D_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.6.3.1

**Statement:** Locally, because beta lies in C, dist_1(q,C) <= ||q - beta||_1; since m > 0, multiplying by m and using absolute homogeneity gives m*dist_1(q,C) <= m*||q - beta||_1 = ||m*(q - beta)||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.6.3.2

**Statement:** Locally, the algebra identity m*(q - beta) = sum_j b_j*(p_j - beta_j) + sum_k c_k*(beta - r_k), together with the l1 triangle inequality, gives ||m*(q - beta)||_1 <= ||sum_j b_j*(p_j - beta_j)||_1 + ||sum_k c_k*(beta - r_k)||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.6.3.2.1

**Statement:** In the local setup, q = (sum_j b_j*p_j - sum_k c_k*r_k)/m with m > 0, so multiplying by m gives m*q = sum_j b_j*p_j - sum_k c_k*r_k; subtracting m*beta from both sides gives m*(q - beta) = sum_j b_j*p_j - sum_k c_k*r_k - m*beta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.6.3.2.2

**Statement:** In the same local setup, write B = sum_j b_j and G = sum_k c_k. Since beta = (sum_j b_j*beta_j)/B and m = B - G, we have B*beta = sum_j b_j*beta_j and G*beta = sum_k c_k*beta, hence m*beta = (B - G)*beta = B*beta - G*beta = sum_j b_j*beta_j - sum_k c_k*beta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.6.3.2.3

**Statement:** Using 1.6.3.2.1 and substituting the expression for m*beta from 1.6.3.2.2 gives m*(q - beta) = sum_j b_j*p_j - sum_k c_k*r_k - (sum_j b_j*beta_j - sum_k c_k*beta); distributing the minus sign and grouping the j- and k-sums yields m*(q - beta) = sum_j b_j*(p_j - beta_j) + sum_k c_k*(beta - r_k).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.6.3.2.4

**Statement:** Let A = sum_j b_j*(p_j - beta_j) and N = sum_k c_k*(beta - r_k). By 1.6.3.2.3, m*(q - beta) = A + N; applying the l1 triangle inequality gives ||m*(q - beta)||_1 = ||A + N||_1 <= ||A||_1 + ||N||_1 = ||sum_j b_j*(p_j - beta_j)||_1 + ||sum_k c_k*(beta - r_k)||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.6.3.3

**Statement:** Locally, the positive residual obeys ||sum_j b_j*(p_j - beta_j)||_1 <= sum_j ||b_j*(p_j - beta_j)||_1 = sum_j b_j*||p_j - beta_j||_1 = sum_j b_j*dist_1(p_j,C), using the l1 triangle inequality, b_j >= 0, and the defining choice of beta_j as a nearest point in C to p_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.6.3.4

**Statement:** Locally, the negative residual obeys ||sum_k c_k*(beta - r_k)||_1 <= sum_k c_k*||beta - r_k||_1 <= sum_k c_k*D_k, using the l1 triangle inequality, c_k >= 0, beta in C, and the hypothesis ||x-r_k||_1 <= D_k for every x in C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.6.3.5

**Statement:** Combining the four local estimates 1.6.3.1--1.6.3.4 gives m*dist_1(q,C) <= ||m*(q - beta)||_1 <= ||sum_j b_j*(p_j - beta_j)||_1 + ||sum_k c_k*(beta - r_k)||_1 <= sum_j b_j*dist_1(p_j,C) + sum_k c_k*D_k, which is exactly the root inequality; thus the proof of 1.6.3 uses only these local children rather than pending sibling nodes 1.4, 1.5, 1.6.1, or 1.6.2.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.6.3.6

**Statement:** Combining the four local estimates gives m*dist_1(q,C) <= ||m*(q - beta)||_1 <= ||sum_j b_j*(p_j - beta_j)||_1 + ||sum_k c_k*(beta - r_k)||_1 <= sum_j b_j*dist_1(p_j,C) + sum_k c_k*D_k, which is exactly the root inequality; this dependency-linked child is the local replacement for the former appeal to sibling nodes 1.4, 1.5, 1.6.1, and 1.6.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

