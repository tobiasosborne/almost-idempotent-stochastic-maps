# Proof Export

## Node 1

**Statement:** Depth-d halo collapse: for an exact signed idempotent P with 0 < delta(P) <= 1/4 and nonempty visible set W(P), any row index v with d = dist_1(p_v, conv{p_w : w in W}), and any halo width a > 0, writing d_j = dist_1(p_j, conv W), sigma_a(v) = sum over {j : d_j > a*tau} of max(P_vj, 0) (tau = sqrt(delta)), sigma(v) = sum over {j : d_j > 0} of max(P_vj, 0), nu_v the row negative mass, and C_a(v) = sum over {j : d_j > a*tau, d_j > d} of max(P_vj, 0)*(d_j - d), one has d*(1 - sigma_a(v)) <= (sigma(v) - sigma_a(v))*a*tau + nu_v*(2 + 4*delta) + C_a(v).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Setup and bookkeeping: let C=conv{p_w:w in W}, a_j=P_vj, a_j^+=max(a_j,0), a_j^-=max(-a_j,0), nu_v=sum_j a_j^-, H={j:d_j>a*tau}, and B={j:d_j<=a*tau}. From def-signed-idempotent, row v of P^2=P gives p_v=sum_j a_j p_j=sum_j a_j^+ p_j-sum_j a_j^- p_j; by lem-mass-split, sum_j a_j^+=1+nu_v. Also d,d_j>=0, H subset {j:d_j>0}, sigma_a<=sigma, C_a>=0, and for every x in C and every row k, ||x-p_k||_1<=2+4*delta by the row-geometry clause of def-signed-idempotent and convexity of C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Trivial branch: if sigma_a(v)>=1, then d*(1-sigma_a(v))<=0, while (sigma(v)-sigma_a(v))*a*tau, nu_v*(2+4*delta), and C_a(v) are all nonnegative by the setup facts and a>0, tau=sqrt(delta)>0, nu_v>=0; hence the required inequality holds in this branch.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Residual construction in the nontrivial branch: if sigma_a(v)<1 and m=1-sigma_a(v), define q=(sum_{j in B} a_j^+ p_j - sum_j a_j^- p_j)/m. Then m>0 and p_v=sum_{j in H} a_j^+ p_j + m*q; the coefficients a_j^+ on H together with m are nonnegative and sum to 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Convex-distance rearrangement in the nontrivial branch: under sigma_a(v)<1 and q as above, (1-sigma_a(v))*d <= C_a(v) + (1-sigma_a(v))*dist_1(q,C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Convexity step: in the branch sigma_a(v)<1, node 1.3 gives p_v=sum_{j in H} a_j^+ p_j + m*q with m=1-sigma_a(v), nonnegative weights, and total weight sigma_a(v)+m=1. Since C is convex, the norm-distance x |-> dist_1(x,C) is convex, so d=dist_1(p_v,C) <= sum_{j in H} a_j^+ d_j + m*dist_1(q,C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Deeper-row correction: for H={j:d_j>a*tau}, split H into indices with d_j<=d and d_j>d. Then sum_{j in H} a_j^+ d_j <= sigma_a(v)*d + sum_{j in H,d_j>d} a_j^+*(d_j-d) = sigma_a(v)*d + C_a(v). Combining this with the convexity step and moving sigma_a(v)*d to the left gives (1-sigma_a(v))*d <= C_a(v)+(1-sigma_a(v))*dist_1(q,C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Residual pricing in the nontrivial branch: under sigma_a(v)<1 and q as above, (1-sigma_a(v))*dist_1(q,C) <= (sigma(v)-sigma_a(v))*a*tau + nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Apply lem-residual-upper: in the branch sigma_a(v)<1, take positives (b_j,p_j)=(a_j^+,p_j) for j in B={j:d_j<=a*tau}, negatives (c_k,r_k)=(a_k^-,p_k) for all k, m=sum_{j in B}a_j^+-sum_k a_k^-=1-sigma_a(v), and q as in node 1.3. For every x in C and every k, ||x-p_k||_1<=2+4*delta by node 1.1, so with D_k=2+4*delta, lem-residual-upper gives m*dist_1(q,C) <= sum_{j in B} a_j^+ d_j + nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Price the non-halo positive rows: on B one has d_j<=a*tau, while rows with d_j=0 contribute zero. Since H={j:d_j>a*tau} and sigma(v)-sigma_a(v)=sum_{j:0<d_j<=a*tau} a_j^+, it follows that sum_{j in B} a_j^+ d_j <= a*tau*(sigma(v)-sigma_a(v)). Combining this with the lem-residual-upper inequality proves the residual-pricing claim.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Branch assembly: the trivial branch proves the root when sigma_a(v)>=1; when sigma_a(v)<1, adding the convex-distance rearrangement and residual-pricing inequalities gives d*(1-sigma_a(v)) <= C_a(v)+(sigma(v)-sigma_a(v))*a*tau+nu_v*(2+4*delta), which is exactly the root inequality.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

