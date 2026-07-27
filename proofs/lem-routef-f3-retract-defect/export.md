# Proof Export

## Node 1

**Statement:** Route F F3 retract defect: let K >= 1 be a dimension-independent constant, n,k >= 1, A: l_inf^k -> l_inf^n and M: l_inf^n -> l_inf^k positive unital maps, Q: l_inf^n -> l_inf^n row-stochastic, and eta >= 0 with 3K*eta < 1; if ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k, then ||MA - I_k||_{inf->inf} <= 3K*eta/(1-3K*eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** The positive unital map A is contractive for the l_inf norm: for every x in l_inf^k, ||Ax||_inf <= ||x||_inf.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For arbitrary x in l_inf^k and c=||x||_inf, coordinatewise -c*1_k <= x <= c*1_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** A positive linear map is order preserving; therefore positivity of A and unitality A(1_k)=1_n send the inequalities in node 1.1.1 to -c*1_n <= Ax <= c*1_n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** The coordinatewise inequalities in node 1.1.2 imply |(Ax)_i|<=c for every coordinate i, hence ||Ax||_inf<=c=||x||_inf; since x was arbitrary, A is contractive.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every x in l_inf^k, linearity and composition give the exact identity A((MA-I_k)x) = (AM-Q)(Ax) + (QA-A)x.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every x in l_inf^k, the operator-norm hypotheses, the identity in node 1.2, and contractivity from node 1.1 imply ||A((MA-I_k)x)||_inf <= 3K*eta*||x||_inf.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By node 1.2, the triangle inequality, and the definition of induced operator norm, ||A((MA-I_k)x)||_inf <= ||AM-Q||_{inf->inf}*||Ax||_inf + ||QA-A||_{inf->inf}*||x||_inf.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Since AM-Q=-(Q-AM), ||AM-Q||_{inf->inf}=||Q-AM||_{inf->inf}; substituting both assumed operator-norm bounds into node 1.3.1 and then using node 1.1 gives ||A((MA-I_k)x)||_inf <= K*eta*||x||_inf+2K*eta*||x||_inf=3K*eta*||x||_inf.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Let alpha=1-3K*eta. Since 3K*eta<1, alpha>0; applying the assumed lower bound ||Ay||_inf >= alpha*||y||_inf to y=(MA-I_k)x and combining with node 1.3 yields ||(MA-I_k)x||_inf <= [3K*eta/alpha]*||x||_inf for every x in l_inf^k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Taking the supremum over all x with ||x||_inf<=1 in the pointwise estimate of node 1.4 gives ||MA-I_k||_{inf->inf} <= 3K*eta/(1-3K*eta), which is the claimed conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

