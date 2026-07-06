# Proof Export

## Node 1

**Statement:** Parametric halo collapse: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), hidden top vertex v of height H, and any halo width a > 0, writing sigma_a for the positive coefficient mass v places on rows at ell-1 distance > a*tau from conv W (tau = sqrt(delta)), sigma for the invisible mass, and nu_v for the row negative mass, one has H*(1 - sigma_a) <= (sigma - sigma_a)*a*tau + nu_v*(2 + 4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Setup and notation: let alpha_j=P_vj, alpha_j^+=max(alpha_j,0), alpha_j^-=max(-alpha_j,0), C=conv{p_w:w in W(P)}, d_j=dist_1(p_j,C), tau=sqrt(delta), and A={j:d_j>a*tau}. Then d_v=H, d_j<=H for every row j, sigma_a=sum_{j in A} alpha_j^+, sigma=sum_{d_j>0} alpha_j^+, nu_v=sum_j alpha_j^-, 0<=sigma_a<=sigma, and every x in C is within 2+4*delta in l1 of every row p_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** From def-height and def-visible-set, C is the visible-row hull, d_v=dist_1(p_v,C)=H for the hidden top vertex v, and d_j<=H for every row j because H is the maximum row distance from C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** From def-invisible-mass and the definition of A={j:d_j>a*tau}, sigma=sum_{d_j>0} alpha_j^+ and sigma_a=sum_{j in A} alpha_j^+ with A subset {j:d_j>0}; hence 0<=sigma_a<=sigma, sigma-sigma_a is the positive mass on rows with 0<d_j<=a*tau, and nu_v=sum_j alpha_j^- by def-negative-mass for row v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** From the row-geometry clause of def-signed-idempotent, any two rows have l1 distance at most 2+4*delta; since C is the convex hull of visible rows, every x in C is a convex combination of rows and therefore ||x-p_k||_1<=2+4*delta for every row p_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Case sigma_a>=1: the desired inequality holds because H>=0 makes H*(1-sigma_a)<=0, while sigma-sigma_a>=0, a*tau>0, nu_v>=0, and 2+4*delta>=0 make the right-hand side nonnegative.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Case sigma_a<1, row-reproduction split: define q=(sum_{j notin A} alpha_j^+ p_j - sum_k alpha_k^- p_k)/(1-sigma_a). Then 1-sigma_a>0 and p_v=sum_{j in A} alpha_j^+ p_j + (1-sigma_a)*q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By def-signed-idempotent, P^2=P gives row reproduction p_v=sum_j alpha_j p_j=sum_j alpha_j^+ p_j - sum_k alpha_k^- p_k. By lem-mass-split, sum_j alpha_j^+=1+nu_v=sum_j alpha_k^-+1, so sum_{j notin A} alpha_j^+ - sum_k alpha_k^- = 1-sigma_a; since this case assumes sigma_a<1, substituting the displayed q gives the asserted split.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Case sigma_a<1, lower residual bound: applying lem-residual-lower to C, p=p_v, coefficients alpha_j^+ on j in A, and the q from the row-reproduction split gives H<=dist_1(q,C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The split from node 1.3 has p_v=sum_{j in A} alpha_j^+ p_j +(1-sigma_a)q with coefficients alpha_j^+>=0 and s=sum_{j in A} alpha_j^+=sigma_a<1. For each j in A, node 1.1 gives dist_1(p_j,C)=d_j<=H=dist_1(p_v,C). Hence lem-residual-lower applies (with the empty-A case giving q=p_v directly) and yields H<=dist_1(q,C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Case sigma_a<1, upper residual bound: applying lem-residual-upper to the same q with positive weights alpha_j^+ for j notin A, negative weights alpha_k^- for all negative coefficients, and D_k=2+4*delta gives (1-sigma_a)*dist_1(q,C)<=sum_{j notin A} alpha_j^+ d_j + nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** For lem-residual-upper set b_j=alpha_j^+ and p_j=p_j for indices j notin A, set c_k=alpha_k^- and r_k=p_k for all negative coefficients, and set m=sum_{j notin A}alpha_j^+-sum_k alpha_k^-=1-sigma_a>0 by node 1.3. The displayed formula for q is exactly (sum b_j p_j - sum c_k r_k)/m. Node 1.1 gives ||x-r_k||_1<=2+4*delta for all x in C, so D_k=2+4*delta is admissible; since sum_k c_k=nu_v, lem-residual-upper yields the asserted bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Halo pricing: sum_{j notin A} alpha_j^+ d_j <= (sigma-sigma_a)*a*tau, because the d_j=0 terms contribute zero and the remaining j notin A with d_j>0 have d_j<=a*tau and total positive mass sigma-sigma_a.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Conclusion: in the case sigma_a<1, multiply H<=dist_1(q,C) by the positive factor 1-sigma_a and combine the upper residual bound and halo pricing to obtain H*(1-sigma_a) <= (sigma-sigma_a)*a*tau + nu_v*(2+4*delta); with the sigma_a>=1 case this proves the root claim.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

