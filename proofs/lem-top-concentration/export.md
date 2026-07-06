# Proof Export

## Node 1

**Statement:** Top concentration: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), hidden top vertex v of height H, and halo width a > 0 with H > a*tau (tau = sqrt(delta)), the positive mass v places outside the genuine set satisfies sum_{j notin G_a} P_vj^+ <= nu_v*(2+4*delta)/(H - a*tau), where G_a = {j : dist_1(p_j, conv{p_w : w in W}) > a*tau} and nu_v is the row-v negative mass.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Set C=conv{p_w:w in W}, d_j=dist_1(p_j,C), D=2+4*delta, and choose an l1/l_infty support functional phi with ||u||_inf<=1, phi<=0 on C, phi(p_v)=H; then, for t_j:=H-phi(p_j), every row satisfies 0<=t_j<=D and every j notin G_a satisfies t_j>=H-a*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Because W is nonempty, C=conv{p_w:w in W} is a nonempty compact convex subset of finite-dimensional l1 space. Since v is a hidden top vertex of height H, H=dist_1(p_v,C). The l1/l_infty distance duality formula gives u with ||u||_inf<=1 such that u.p_v - sup_{c in C} u.c = H; with b=-sup_C u.c and phi(x)=u.x+b, we have phi<=0 on C and phi(p_v)=H.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For every row p_j, phi(p_j)<=d_j:=dist_1(p_j,C): indeed phi(c)<=0 for c in C and ||u||_inf<=1 give phi(p_j)<=u.(p_j-c)<=||p_j-c||_1, then inf over c in C. Since H is the maximum row height, d_j<=H for all j; if j notin G_a, then d_j<=a*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** The functional phi(x)=u.x+b has ||u||_inf<=1, hence is 1-Lipschitz for the l1 metric. By the row-geometry clause of def-signed-idempotent, ||p_v-p_j||_1<=D:=2+4*delta for every row p_j, so t_j:=H-phi(p_j)=phi(p_v)-phi(p_j)<=D. Also phi<=0 on C and ||u||_inf<=1 imply phi(p_j)<=d_j:=dist_1(p_j,C); since v is a hidden top vertex of height H, d_j<=H for all rows, and by the definition of G_a, j notin G_a gives d_j<=a*tau. Therefore t_j>=H-d_j>=0 for all j and t_j>=H-a*tau for j notin G_a.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Dependency-scoped affine reproduction: for the support functional phi supplied by node 1.1 (so phi is affine and phi(p_v)=H), setting t_j:=H-phi(p_j), exact idempotence gives sum_j P_vj*t_j=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** From def-signed-idempotent, P*1=1 and P^2=P. The row-v equation of P^2=P is p_v=sum_j P_vj*p_j as a vector, and P*1=1 gives sum_j P_vj=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For any affine phi, affine-linearity over coefficients with total sum 1 gives phi(p_v)=sum_j P_vj*phi(p_j). Using phi(p_v)=H and sum_j P_vj=1, we get sum_j P_vj*(H-phi(p_j))=H*sum_j P_vj-sum_j P_vj*phi(p_j)=H-H=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Scoped bridge for challenge ch-68153d29c48e7b18: node 1.1 supplies the chosen affine support functional phi with phi(p_v)=H, and nodes 1.2.1 and 1.2.2 supply the exact-idempotence row equation, total-mass equation, and affine reproduction calculation. Therefore, for this phi and t_j:=H-phi(p_j), sum_j P_vj*t_j = H*sum_j P_vj - sum_j P_vj*phi(p_j) = H - phi(p_v) = H - H = 0. This is exactly the amended dependency-scoped statement of node 1.2.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The nonnegative bounded deficits t_j obey the sign-split estimate sum_j P_vj^+*t_j <= nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Write P_vj^+=max(P_vj,0) and P_vj^-=max(-P_vj,0), so P_vj=P_vj^+-P_vj^- and nu_v=sum_j P_vj^- by the row-v negative-mass notation from def-negative-mass and the contract. Establish locally that t_j satisfies 0<=t_j<=D:=2+4*delta for every j and that sum_j P_vj*t_j=0. Then sum_j P_vj^+*t_j=sum_j P_vj^-*t_j, and this common value is at most D*sum_j P_vj^-=nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Local bounded-deficit premise: let C=conv{p_w:w in W}, let phi(x)=u.x+b be the support functional used for the height H with ||u||_inf<=1, phi<=0 on C, and phi(p_v)=H, and set t_j:=H-phi(p_j), D:=2+4*delta. For every row p_j, phi(p_j)<=d_j:=dist_1(p_j,C)<=H, so t_j>=0. Also phi is 1-Lipschitz for the l1 metric and def-signed-idempotent gives ||p_v-p_j||_1<=D for every row, hence t_j=phi(p_v)-phi(p_j)<=D. Therefore 0<=t_j<=D for every j.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Local affine-reproduction premise: def-signed-idempotent gives P*1=1 and P^2=P. Taking row v in P^2=P gives p_v=sum_j P_vj*p_j as a vector, and P*1=1 gives sum_j P_vj=1. For the affine phi(x)=u.x+b, sum_j P_vj*phi(p_j)=u.(sum_j P_vj*p_j)+b*sum_j P_vj=u.p_v+b=phi(p_v)=H. Consequently sum_j P_vj*t_j=sum_j P_vj*(H-phi(p_j))=H*sum_j P_vj-sum_j P_vj*phi(p_j)=H-H=0.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

##### Node 1.3.1.3

**Statement:** Using 1.3.1.1 and 1.3.1.2, write P_vj=P_vj^+-P_vj^- with P_vj^+,P_vj^- >=0 and nu_v=sum_j P_vj^- by the row-v negative-mass notation. Then 0=sum_j P_vj*t_j=sum_j P_vj^+*t_j-sum_j P_vj^-*t_j, so sum_j P_vj^+*t_j=sum_j P_vj^-*t_j. Since 0<=t_j<=D and P_vj^- >=0 for every j, sum_j P_vj^-*t_j<=D*sum_j P_vj^-=nu_v*(2+4*delta). Thus sum_j P_vj^+*t_j<=nu_v*(2+4*delta).

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Since j notin G_a implies t_j>=H-a*tau>0, the sign-split estimate gives (H-a*tau)*sum_{j notin G_a} P_vj^+ <= nu_v*(2+4*delta), and division by H-a*tau proves the claimed bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** In the local setting of node 1.4, choose the l1/l_infty support functional phi for the distance from p_v to C=conv{p_w:w in W}, put t_j=H-phi(p_j), and put D=2+4*delta. The support-functional bounds give t_j>=0 for all j and t_j>=H-a*tau for j notin G_a; exact idempotence and the row-v negative-mass definition give the sign-split estimate sum_j P_vj^+*t_j<=nu_v*D. Hence (H-a*tau)*sum_{j notin G_a} P_vj^+ <= sum_{j notin G_a} P_vj^+*t_j <= sum_j P_vj^+*t_j <= nu_v*(2+4*delta). Since H>a*tau, division by H-a*tau gives sum_{j notin G_a} P_vj^+ <= nu_v*(2+4*delta)/(H-a*tau).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** Dependency bridge for the final division step: the only nonlocal inputs used here are exactly node 1.1, which gives t_j>=0 for all j and t_j>=H-a*tau for j notin G_a, and node 1.3, which gives sum_j P_vj^+*t_j<=nu_v*(2+4*delta). With these two dependencies explicitly declared, the rest of node 1.4.1 is pure order algebra: because P_vj^+=max(P_vj,0)>=0, multiplying the lower bound on t_j over j notin G_a gives (H-a*tau)*sum_{j notin G_a}P_vj^+<=sum_{j notin G_a}P_vj^+*t_j; since t_j>=0 and P_vj^+>=0, the restricted sum is at most the full sum; node 1.3 bounds the full sum by nu_v*(2+4*delta); and H>a*tau makes H-a*tau>0, so division by this positive scalar gives the desired bound.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.4.1.2

**Statement:** Scoped dependency bridge for node 1.4.1: assume exactly the explicitly declared dependencies 1.1 and 1.3. Dependency 1.1 supplies t_j>=0 for every j and t_j>=H-a*tau for every j notin G_a; dependency 1.3 supplies sum_j P_vj^+*t_j<=nu_v*(2+4*delta). Since P_vj^+=max(P_vj,0)>=0, summing the lower bound over j notin G_a gives (H-a*tau)*sum_{j notin G_a} P_vj^+ <= sum_{j notin G_a} P_vj^+*t_j. Because t_j>=0 and P_vj^+>=0, the restricted sum is at most sum_j P_vj^+*t_j. Applying 1.3 gives (H-a*tau)*sum_{j notin G_a} P_vj^+ <= nu_v*(2+4*delta). Finally H>a*tau makes H-a*tau>0, so division by H-a*tau yields sum_{j notin G_a} P_vj^+ <= nu_v*(2+4*delta)/(H-a*tau).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.3

**Statement:** Self-contained dependency repair for ch-0e785a8c7af38a9a: no sibling node is used. Let C=conv{p_w:w in W} and d_j=dist_1(p_j,C). Since W is nonempty and v is a hidden top vertex of height H=dist_1(p_v,C), finite-dimensional l1/l_infty distance duality supplies an affine phi(x)=u.x+b with ||u||_inf<=1, phi<=0 on C, and phi(p_v)=H. Set t_j=H-phi(p_j) and D=2+4*delta. For every row p_j, phi(p_j)<=d_j: for c in C, phi(p_j)<=phi(p_j)-phi(c)=u.(p_j-c)<=||p_j-c||_1, then take the infimum over c. Since H is the maximum row height, d_j<=H, so t_j>=0. If j notin G_a, then d_j<=a*tau by the definition G_a={j:dist_1(p_j,C)>a*tau}, hence t_j>=H-d_j>=H-a*tau. Also phi is 1-Lipschitz for l1 and def-signed-idempotent gives ||p_v-p_j||_1<=D for every row, so t_j=phi(p_v)-phi(p_j)<=D. Exact signed idempotence gives P*1=1 and P^2=P, hence sum_j P_vj=1 and p_v=sum_j P_vj p_j. Affineness gives sum_j P_vj phi(p_j)=phi(p_v)=H, so sum_j P_vj t_j=0. Writing P_vj=P_vj^+-P_vj^- with P_vj^+,P_vj^->=0 and nu_v=sum_j P_vj^- by the row-v negative-mass notation, the equality sum_j P_vj t_j=0 gives sum_j P_vj^+ t_j=sum_j P_vj^- t_j<=D*sum_j P_vj^-=nu_v*(2+4*delta). Combining this with P_vj^+>=0, t_j>=0, and t_j>=H-a*tau on j notin G_a yields (H-a*tau)*sum_{j notin G_a} P_vj^+<=sum_{j notin G_a} P_vj^+ t_j<=sum_j P_vj^+ t_j<=nu_v*(2+4*delta). Since H>a*tau, divide by the positive number H-a*tau to obtain the asserted bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

