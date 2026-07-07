# Proof Export

## Node 1

**Statement:** Hiddenness dual witness: for an exact signed idempotent P and a hidden row vertex v (rho = 4*tau, kappa = tau/4, tau = sqrt(delta(P))), writing F_v = {j : ||p_j - p_v||_1 >= rho} for the rho-far row-index set (nonempty for hidden v), there exist lambda_f >= 0 (f in F_v) with sum_f lambda_f = 1 and alpha_i, beta_i >= 0 (over all row indices i) with sum_i beta_i = t*(v) < kappa, such that sum_f lambda_f*(p_f - p_v) + sum_i alpha_i*(p_i - p_v) = sum_i beta_i*(p_i - p_v).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Hiddenness gives the scalar prerequisites: F_v is nonempty and t*(v) < kappa. By def-exposed, if no row is at l1-distance at least rho from p_v then t*(v)=+infty; a hidden row vertex is not (rho,kappa)-exposed, so it cannot have t*(v)>=kappa, hence F_v is nonempty and t*(v)<kappa.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The exposedness-margin optimization is the finite primal LP: with d_i=p_i-p_v, choose u in R^n and t in R, maximize t, subject to 0 <= u.d_i <= 1 for every row index i and t <= u.d_f for every f in F_v. Its optimal value is exactly t*(v); it is feasible at u=0,t=0 and, because F_v is nonempty, it is bounded above by 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** An admissible exposer h with h(p_v)=0 is, on the finite row set, h(p_i)=u.(p_i-p_v) for the linear part u of h; conversely any u defines the affine function h(x)=u.(x-p_v), which has h(p_v)=0. Therefore admissibility 0<=h(p_i)<=1 is exactly 0<=u.d_i<=1 for all row indices i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For fixed u satisfying 0<=u.d_i<=1, the largest feasible t in the displayed LP is min_{f in F_v} u.d_f. Hence maximizing t is exactly the exposedness-margin supremum t*(v). The point u=0,t=0 is feasible, and if F_v is nonempty then t<=u.d_f<=1 for any f in F_v, so the primal objective is bounded above by 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The standard dual of that primal LP has nonnegative variables beta_i for u.d_i <= 1, alpha_i for -u.d_i <= 0, and lambda_f for t-u.d_f <= 0. It minimizes sum_i beta_i subject to sum_f lambda_f = 1 and sum_f lambda_f*d_f + sum_i alpha_i*d_i = sum_i beta_i*d_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Put the primal from 1.2 in max-with-free-variables form with x=(u,t), objective t, and inequalities u.d_i<=1, -u.d_i<=0, and t-u.d_f<=0. The dual of a finite maximization LP with free variables and <= inequalities uses nonnegative multipliers on those inequalities and imposes equality of the coefficient vector with the primal objective vector.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Applying that rule gives multipliers beta_i>=0, alpha_i>=0, lambda_f>=0 and dual objective sum_i beta_i. Equality of the t-coefficient gives sum_f lambda_f=1. Equality of the u-coefficients gives sum_i beta_i*d_i - sum_i alpha_i*d_i - sum_f lambda_f*d_f=0, equivalently sum_f lambda_f*d_f + sum_i alpha_i*d_i = sum_i beta_i*d_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Finite LP strong duality and dual attainment apply to the feasible bounded finite LP above, so there is an optimal dual solution with sum_i beta_i = t*(v). Together with t*(v)<kappa, the dual nonnegativity, lambda-normalization, and vector equality are exactly the required hiddenness witness.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The primal LP from 1.2 is finite-dimensional, feasible, and has finite optimal value t*(v). Therefore standard finite LP strong duality gives equality between the primal optimum and the dual optimum from 1.3, and dual attainment gives a dual feasible minimizer.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Choose such a dual minimizer. By 1.3 its variables satisfy lambda_f>=0, alpha_i>=0, beta_i>=0, sum_f lambda_f=1, and sum_f lambda_f*d_f + sum_i alpha_i*d_i = sum_i beta_i*d_i; by strong duality its objective sum_i beta_i equals t*(v). By 1.1 this common value is < kappa, and substituting d_i=p_i-p_v gives the witness equation in node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

