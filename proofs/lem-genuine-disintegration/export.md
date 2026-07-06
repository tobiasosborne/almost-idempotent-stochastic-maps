# Proof Export

## Node 1

**Statement:** Genuine-mass disintegration: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), height H, halo width a > 0 with G_a = {j : dist_1(p_j, conv W) > a*tau} nonempty (tau = sqrt(delta)), fix for every row a vertex representation p_j = sum_v lambda_jv p_v over geometrically distinct row vertices; then every row index i satisfies g_i <= M_i^a + sum_{j in G_a} P_ij^+ * (H - d_j)/(H - a*tau), where g = P*1_{G_a}, d_j = dist_1(p_j, conv W), P_ij^+ = max(P_ij, 0), and M_i^a = sum_{j in G_a} P_ij^+ * sum_{v : d_v > a*tau} lambda_jv is positive mass supported entirely on HIDDEN row vertices at depth in (a*tau, H].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let C=conv{p_w : w in W(P)} and d_j=dist_1(p_j,C). Because G_a is nonempty, some j has d_j>a*tau, while the height definition gives d_j<=H for every row; hence H>a*tau and H-a*tau>0. For any row vertex v with d_v>a*tau, v is not visible since visible vertices lie in C and have distance 0; and d_v<=H, so such vertices are hidden and have depth in (a*tau,H].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every row j, its fixed vertex representation p_j=sum_v lambda_jv p_v is a convex combination over geometrically distinct row vertices. Applying lem-residual-upper to C, the positive weights b_v=lambda_jv, no negative terms, m=sum_v lambda_jv=1, and q=p_j gives the depth-convexity bound d_j<=sum_v lambda_jv d_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For a fixed row j, the phrase vertex representation in the root hypothesis means a finite convex representation over the chosen geometrically distinct row vertices: lambda_jv>=0, sum_v lambda_jv=1, and p_j=sum_v lambda_jv p_v. The set C=conv W(P) is the convex hull of finitely many row points.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Use lem-residual-upper with C as above, positive coefficients b_v=lambda_jv, no negative coefficients c_k, m=sum_v lambda_jv=1, q=p_j, and p_v the row vertices in the representation. Its conclusion is dist_1(p_j,C)<=sum_v lambda_jv dist_1(p_v,C), i.e. d_j<=sum_v lambda_jv d_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every j in G_a, define L_j=sum_{v:d_v<=a*tau} lambda_jv and U_j=sum_{v:d_v>a*tau} lambda_jv. Then L_j+U_j=1 and the previous bound plus d_v<=a*tau on the L_j part and d_v<=H on the U_j part gives d_j<=a*tau*L_j+H*U_j=H-(H-a*tau)L_j; since H-a*tau>0, L_j<=(H-d_j)/(H-a*tau).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For j in G_a, the sets of vertices with d_v<=a*tau and d_v>a*tau partition the vertex representation, so L_j+U_j=1. Combining node 1.2 with d_v<=a*tau on the first part and d_v<=H on the second part gives d_j<=a*tau*L_j+H*U_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Dependency bridge for the depth-convexity premise: for the fixed j in G_a under discussion, validated node 1.2.2 applies to the fixed vertex representation p_j=sum_v lambda_jv p_v and gives d_j <= sum_v lambda_jv d_v. This supplies the bound that the parent previously cited as node 1.2, now through an explicit validated dependency.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Partition bridge: validated node 1.2.1 records that the fixed vertex representation has lambda_jv >= 0 and sum_v lambda_jv = 1. The two conditions d_v <= a*tau and d_v > a*tau are complementary for each represented vertex v, so L_j=sum_{v:d_v<=a*tau}lambda_jv and U_j=sum_{v:d_v>a*tau}lambda_jv satisfy L_j+U_j=sum_v lambda_jv=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.3

**Statement:** Combination bridge: split sum_v lambda_jv d_v over the two complementary classes. On the class d_v <= a*tau, nonnegativity of lambda_jv gives sum_{d_v<=a*tau} lambda_jv d_v <= a*tau*L_j. On the class d_v > a*tau, validated node 1.1 gives d_v <= H for every row vertex v, hence sum_{d_v>a*tau} lambda_jv d_v <= H*U_j. Together with node 1.3.1.1, this gives d_j <= sum_v lambda_jv d_v <= a*tau*L_j + H*U_j, while node 1.3.1.2 gives L_j+U_j=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Substitute U_j=1-L_j to get d_j<=H-(H-a*tau)L_j. Node 1.1 gives H-a*tau>0, so rearranging yields L_j<=(H-d_j)/(H-a*tau).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Dependency bridge for the algebra step: for the fixed j in G_a, node 1.3.1 supplies L_j+U_j=1 and d_j<=a*tau*L_j+H*U_j. The equality L_j+U_j=1 gives U_j=1-L_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Algebraic rearrangement: using node 1.3.2.1, substitute U_j=1-L_j in d_j<=a*tau*L_j+H*U_j to get d_j<=a*tau*L_j+H*(1-L_j)=H-(H-a*tau)*L_j. Validated node 1.1 gives H-a*tau>0, so this inequality implies (H-a*tau)*L_j<=H-d_j and therefore L_j<=(H-d_j)/(H-a*tau).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For every row index i, g_i=(P*1_{G_a})_i=sum_{j in G_a} P_ij<=sum_{j in G_a} P_ij^+. Splitting 1=L_j+U_j in each positive coefficient gives sum_{j in G_a} P_ij^+=M_i^a+sum_{j in G_a} P_ij^+ L_j, where M_i^a=sum_{j in G_a} P_ij^+ U_j. Multiplying the bound on L_j by P_ij^+>=0 and summing over j in G_a yields g_i<=M_i^a+sum_{j in G_a} P_ij^+*(H-d_j)/(H-a*tau), and the first step proves that M_i^a is positive mass supported entirely on hidden row vertices at depth in (a*tau,H].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** For each i, the definition g=P*1_{G_a} gives g_i=sum_{j in G_a} P_ij. Since P_ij<=P_ij^+=max(P_ij,0) for each j, g_i<=sum_{j in G_a} P_ij^+.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** For fixed row index i and j in G_a, set L_j=sum_{v:d_v<=a*tau} lambda_jv and U_j=sum_{v:d_v>a*tau} lambda_jv. The needed shallow-mass estimate L_j <= (H-d_j)/(H-a*tau) is proved locally from the fixed vertex representation, the residual-upper depth-convexity bound, and H-a*tau>0, rather than imported from pending node 1.3. Since P_ij^+>=0, summing this estimate over j in G_a gives sum_{j in G_a} P_ij^+ L_j <= sum_{j in G_a} P_ij^+*(H-d_j)/(H-a*tau). Also L_j+U_j=1, so sum_{j in G_a} P_ij^+ = sum_{j in G_a} P_ij^+ U_j + sum_{j in G_a} P_ij^+ L_j, and the first term is exactly M_i^a. Together with node 1.4.1 this gives the displayed bound; validated node 1.1 gives the claimed hidden-depth support of M_i^a.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.1

**Statement:** Local shallow-mass bridge: fix j in G_a. Validated node 1.2.1 gives lambda_jv>=0, sum_v lambda_jv=1, and the two complementary classes d_v<=a*tau and d_v>a*tau, so L_j+U_j=1. Validated node 1.2.2 gives d_j<=sum_v lambda_jv d_v. Splitting this sum, the d_v<=a*tau part is at most a*tau*L_j, and validated node 1.1 gives d_v<=H for every represented row vertex, so the d_v>a*tau part is at most H*U_j. Hence d_j<=a*tau*L_j+H*U_j. With U_j=1-L_j and H-a*tau>0 from validated node 1.1, this rearranges to L_j<=(H-d_j)/(H-a*tau).

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.4.2.2

**Statement:** Weighted summation bridge: for the fixed row i, P_ij^+=max(P_ij,0)>=0 for every j. Multiplying the estimate from node 1.4.2.1 by P_ij^+ and summing over the finite set G_a preserves the inequality, giving sum_{j in G_a} P_ij^+ L_j <= sum_{j in G_a} P_ij^+*(H-d_j)/(H-a*tau).

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.4.2.3

**Statement:** Assembly and support bridge: because L_j+U_j=1, sum_{j in G_a} P_ij^+=sum_{j in G_a} P_ij^+ U_j+sum_{j in G_a} P_ij^+ L_j, and by the root definition of M_i^a with U_j=sum_{v:d_v>a*tau} lambda_jv the first sum is exactly M_i^a. Combining validated node 1.4.1 with node 1.4.2.2 yields g_i<=M_i^a+sum_{j in G_a} P_ij^+*(H-d_j)/(H-a*tau). The coefficients P_ij^+ lambda_jv in M_i^a are nonnegative, and validated node 1.1 says every row vertex with d_v>a*tau is hidden with depth in (a*tau,H], so M_i^a is supported entirely on those hidden vertices.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

