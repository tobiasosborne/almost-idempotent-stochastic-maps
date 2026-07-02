# Proof Export

## Node 1

**Statement:** Height collapse: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), and hidden top vertex v (height H = dist_1(p_v, conv W) maximal among rows), the invisible mass sigma_v and the row negative mass nu_v satisfy H * (1 - sigma_v) <= nu_v * (2 + 4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let C=conv W, a_j=P_vj, a_j^+=max(a_j,0), a_j^-=max(-a_j,0), and nu_v=sum_j a_j^-. The exact signed idempotent identities imply p_v=sum_j a_j p_j and sum_j a_j=1; with S=sum_j a_j^+=1+nu_v, the point q=S^{-1} sum_j a_j^+ p_j is a convex combination of rows and p_v=q+sum_j a_j^-(q-p_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-signed-idempotent, P^2=P and P1=1. Taking the v-th row of P^2=P gives p_v=sum_j P_vj p_j=sum_j a_j p_j, and taking the v-th row of P1=1 gives sum_j a_j=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For each real a_j, a_j=a_j^+-a_j^- with a_j^+,a_j^- >=0. Thus S=sum_j a_j^+=sum_j a_j+sum_j a_j^-=1+nu_v>=1, so q=S^{-1}sum_j a_j^+p_j is a convex combination of rows; substituting sum_j a_j^+p_j=S q and nu_v=sum_j a_j^- gives p_v=q+sum_j a_j^-(q-p_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For d_j=dist_1(p_j,C), the maximal-height hypothesis gives d_j<=H for every row, and d_j=0 on rows in C. Since sigma_v=sum_{d_j>0} a_j^+ by def-invisible-mass and dist_1(.,C) is convex by def-height, dist_1(q,C)<=S^{-1} sum_j a_j^+ d_j<=S^{-1} sigma_v H<=sigma_v H.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By def-height, C=conv W and H is the maximum over all rows of dist_1(p_i,C); hence each d_j=dist_1(p_j,C) satisfies d_j<=H, while any row p_j in C has d_j=0 by the definition of distance to a set.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** By def-invisible-mass, sigma_v=sum_{d_j>0} a_j^+. Since q=S^{-1}sum_j a_j^+p_j is a convex combination of rows and def-height states that dist_1(.,C) is convex, dist_1(q,C)<=S^{-1}sum_j a_j^+d_j<=S^{-1}sigma_v H. From S=1+nu_v>=1 and H>=0, this is at most sigma_v H.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The row-geometry clause of def-signed-idempotent gives ||p_k-p_j||_1<=2+4*delta for all rows. Since q is a convex combination of rows, ||q-p_j||_1<=2+4*delta for each j; therefore ||p_v-q||_1<=nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Let D=2+4*delta. The row-geometry clause in def-signed-idempotent says that for an exact signed idempotent with negative mass delta, every pair of rows satisfies ||p_k-p_j||_1<=D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Writing q=sum_k b_k p_k with b_k=a_k^+/S, b_k>=0, sum_k b_k=1, and D=2+4*delta, the local row-diameter bridge 1.3.2.1 gives ||p_k-p_j||_1<=D for all rows, so the triangle inequality gives ||q-p_j||_1<=sum_k b_k||p_k-p_j||_1<=D for every j. Using the locally rederived identity p_v-q=sum_j a_j^-(q-p_j) from 1.3.2.2, another triangle inequality gives ||p_v-q||_1<=sum_j a_j^-D=nu_v D=nu_v*(2+4*delta), as recorded in 1.3.2.3 and 1.3.2.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Let D=2+4*delta. The row-geometry clause of def-signed-idempotent applies to the given exact signed idempotent P with negative mass delta=delta(P), so every pair of rows satisfies ||p_k-p_j||_1 <= D.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** With a_j=P_vj, a_j^+=max(a_j,0), a_j^-=max(-a_j,0), nu_v=sum_j a_j^-, S=sum_j a_j^+, and q=S^(-1) sum_j a_j^+ p_j, def-signed-idempotent gives p_v=sum_j a_j p_j and sum_j a_j=1; hence S=1+nu_v and p_v-q=sum_j a_j^-(q-p_j).

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

##### Node 1.3.2.3

**Statement:** Writing b_k=a_k^+/S, node 1.3.2.2 gives S=1+nu_v>=1, b_k>=0, sum_k b_k=1, and q=sum_k b_k p_k. For each fixed j, the triangle inequality and node 1.3.2.1 give ||q-p_j||_1 = ||sum_k b_k(p_k-p_j)||_1 <= sum_k b_k||p_k-p_j||_1 <= D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.4

**Statement:** Using node 1.3.2.2, p_v-q=sum_j a_j^-(q-p_j) with a_j^- >= 0 and sum_j a_j^-=nu_v. Using node 1.3.2.3 in the triangle inequality gives ||p_v-q||_1 <= sum_j a_j^-||q-p_j||_1 <= sum_j a_j^- D = nu_v D = nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Combining the previous estimates gives H=dist_1(p_v,C)<=dist_1(q,C)+||p_v-q||_1<=sigma_v H+nu_v*(2+4*delta), hence H*(1-sigma_v)<=nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Because H=dist_1(p_v,C) by the hidden-top-vertex hypothesis and distance to a set is 1-Lipschitz in its point argument, H<=dist_1(q,C)+||p_v-q||_1. Nodes 1.2 and 1.3 bound the two terms by sigma_v H and nu_v*(2+4*delta), respectively, so H<=sigma_v H+nu_v*(2+4*delta); subtracting sigma_v H from both sides gives H*(1-sigma_v)<=nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** For C=conv W, the hidden-top-vertex hypothesis in def-height gives H=dist_1(p_v,C). Since C is nonempty, distance to C is 1-Lipschitz in the l1 metric: for any c in C, dist_1(p_v,C)<=||p_v-q||_1+||q-c||_1, and taking the infimum over c gives H<=dist_1(q,C)+||p_v-q||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.2

**Statement:** Let a_j=P_vj, a_j^+=max(a_j,0), a_j^-=max(-a_j,0), nu_v=sum_j a_j^-, S=sum_j a_j^+=1+nu_v, and q=S^{-1}sum_j a_j^+p_j. Then S>=1 and q is a convex combination of rows. For d_j=dist_1(p_j,C), def-height gives 0<=d_j<=H for every row and d_j=0 for rows in C. By def-invisible-mass, sigma_v=sum_{d_j>0} a_j^+. Convexity of dist_1(.,C) from def-height gives dist_1(q,C)<=S^{-1}sum_j a_j^+d_j<=S^{-1}sigma_v H<=sigma_v H.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.3

**Statement:** Let D=2+4*delta. The row-geometry clause of def-signed-idempotent gives ||p_k-p_j||_1<=D for all rows. With q=S^{-1}sum_k a_k^+p_k, q=sum_k b_k p_k for b_k=a_k^+/S, b_k>=0, sum_k b_k=1, so the triangle inequality gives ||q-p_j||_1<=sum_k b_k||p_k-p_j||_1<=D for every j. The exact-idempotent row identity p_v=sum_j a_j p_j and sum_j a_j=1 imply p_v=q+sum_j a_j^-(q-p_j), hence ||p_v-q||_1<=sum_j a_j^-D=nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

