# Proof Export

## Node 1

**Statement:** Import reduction: let P be a rank-3 exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let U = (u_0,u_1,u_2) be an actual-row chart whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, define coordinates a_q(i) by p_i = sum_q a_q(i)p_{u_q} and beta_r(i) = P_{u_r i}; fix a pivot index s, a non-chart row j with c = a_s(j) > 0, a transverse index r != s, and let t be the remaining index, writing d_r = a_r(j) and d_t = a_t(j); define R_{r,j}(i) = (1/c - 1)*max(-a_s(i),0) + max(a_s(i)*d_t/c, 0) - a_s(i)*d_r/c, I_{r,j}(U) = sum_i max(beta_r(i),0)*max(R_{r,j}(i),0), A_{r,s} = sum_i max(beta_r(i),0)*max(a_s(i),0), and B_{r,s} = sum_i max(beta_r(i),0)*max(-a_s(i),0); then I_{r,j}(U) <= ((max(1-c,0) + max(-d_t,0) + max(d_r,0))/c)*B_{r,s} + ((max(d_t,0) + max(-d_r,0))/c)*A_{r,s}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Pointwise scalar reduction: for every summation index i, set a=a_s(i), a^+=max(a,0), a^-=max(-a,0), alpha=(max(1-c,0)+max(-d_t,0)+max(d_r,0))/c, and gamma=(max(d_t,0)+max(-d_r,0))/c. With c>0 and R_i=(1/c-1)a^-+max(a*d_t/c,0)-a*d_r/c, one has max(R_i,0) <= alpha*a^- + gamma*a^+.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** First summand bound: because c>0 and a^->=0, (1/c-1)*a^- = ((1-c)/c)*a^- <= (max(1-c,0)/c)*a^-; this covers both c<=1 and c>1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** d_t product bound: because c>0, max(a*d_t/c,0) <= (max(-d_t,0)/c)*a^- + (max(d_t,0)/c)*a^+; indeed if d_t>=0 the left side is (d_t/c)*a^+, and if d_t<0 it is ((-d_t)/c)*a^-.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** d_r linear bound: because c>0, -a*d_r/c <= (max(d_r,0)/c)*a^- + (max(-d_r,0)/c)*a^+; this follows by writing a=a^+-a^- and considering d_r>=0 and d_r<0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Combination and positive part: adding the preceding three bounds gives R_i <= alpha*a^- + gamma*a^+. Since alpha>=0, gamma>=0, a^+>=0, and a^->=0, the right side is nonnegative, so max(R_i,0) <= alpha*a^- + gamma*a^+.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Weighted summation: assuming the pointwise scalar reduction for every i, multiply it by beta_i^+=max(beta_r(i),0), sum over i, and use the definitions of I_{r,j}(U), A_{r,s}, and B_{r,s} to obtain the claimed bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Nonnegative-weight step: for each i, beta_i^+=max(beta_r(i),0) is nonnegative, so the pointwise inequality max(R_i,0) <= alpha*a_s(i)^- + gamma*a_s(i)^+ remains valid after multiplication by beta_i^+.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Finite summation step: summing the weighted inequalities over all row indices i gives sum_i beta_i^+*max(R_i,0) <= alpha*sum_i beta_i^+*a_s(i)^- + gamma*sum_i beta_i^+*a_s(i)^+.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Substitution of definitions: by the definitions in the root statement, sum_i beta_i^+*max(R_i,0)=I_{r,j}(U), sum_i beta_i^+*a_s(i)^-=B_{r,s}, sum_i beta_i^+*a_s(i)^+=A_{r,s}, alpha=(max(1-c,0)+max(-d_t,0)+max(d_r,0))/c, and gamma=(max(d_t,0)+max(-d_r,0))/c; substituting these identities is exactly the asserted inequality.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

