# Proof Export

## Node 1

**Statement:** Top-slab companion: for an exact signed idempotent P with 0 < delta(P) <= (17 - 12*sqrt(2))/2, nonempty visible set W(P), and hidden top vertex v of height H > 13*tau (tau = sqrt(delta)), there is a row f with ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv{p_w : w in W}) > H - (1/2 + delta)*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let C_W = conv{p_w : w in W}. Finite-dimensional ell1 distance duality gives an affine 1-Lipschitz functional phi with phi(p_v)=H and phi <= 0 on C_W; with psi=H-phi, one has psi(p_v)=0 and 0 <= psi(p_i) <= 2+4*delta for every row i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Since W is nonempty and finite, C_W is a nonempty compact convex polytope. The ell1 distance formula dist_1(p_v,C_W)=sup_{||u||_infty<=1}(u.p_v-sup_{c in C_W}u.c) attains its supremum, so choose u with u.p_v-sup_C u.c=H.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Using the vector u chosen in 1.1.1, define phi(x)=u.x-sup_{c in C_W}u.c. Then ||u||_infty<=1 makes phi 1-Lipschitz for the ell1 metric, phi <= 0 on C_W by construction, and phi(p_v)=H by the distance-attaining equality from 1.1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** The phrase 'the vector u chosen in 1.1.1' means precisely the validated distance-attaining vector from node 1.1.1: ||u||_infty<=1 and u.p_v - sup_{c in C_W} u.c = H. Therefore this u is not arbitrary (for example, not u=0 when H>0), and substituting x=p_v in the definition phi(x)=u.x-sup_{c in C_W}u.c gives phi(p_v)=H.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** For any c in C_W, sup_{d in C_W} u.d >= u.c, hence phi(c)=u.c-sup_{d in C_W}u.d <= 0. For any x,y, |phi(x)-phi(y)|=|u.(x-y)| <= ||u||_infty*||x-y||_1 <= ||x-y||_1 by the ||u||_infty<=1 part imported from 1.1.1, so phi is 1-Lipschitz for the ell1 metric.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** For any row p_i, phi(p_i) <= dist_1(p_i,C_W) because phi is 1-Lipschitz and phi <= 0 on C_W. Since v is a hidden top vertex of height H, def-height gives dist_1(p_i,C_W) <= H for all rows, hence psi(p_i)=H-phi(p_i) >= 0 and psi(p_v)=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** For any row p_i, psi(p_i)=phi(p_v)-phi(p_i) <= ||p_v-p_i||_1 by 1-Lipschitzness of phi, and def-signed-idempotent gives ||p_v-p_i||_1 <= 2+4*delta; hence psi(p_i) <= 2+4*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Because v is a hidden row vertex at the scales rho=4*tau and kappa=tau/4, lem-hiddenness-dual-witness supplies F_v nonempty and coefficients lambda_f, alpha_i, beta_i satisfying its balance identity, lambda_f>=0 with sum_F lambda_f=1, alpha_i,beta_i>=0, and sum_i beta_i=t*(v)<kappa.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By def-visible-set and def-exposed, the scales attached to P are tau=sqrt(delta(P)), rho=4*tau, and kappa=tau/4, and a hidden top vertex v is a hidden row vertex for these scales.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Instantiating lem-hiddenness-dual-witness with this exact signed idempotent P and hidden row vertex v gives the nonempty set F_v={j: ||p_j-p_v||_1 >= rho} and coefficients lambda_f, alpha_i, beta_i with all the nonnegativity, normalization, beta-sum, and balance properties stated in 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Applying the affine functional psi, whose value at p_v is 0, to that balance identity yields a rho-far index f in F_v with psi(p_f) < kappa*(2+4*delta) = (1/2 + delta)*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Let L be the linear part of the affine function psi. Because psi(p_v)=0, for every row index i one has L(p_i-p_v)=psi(p_i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Apply L to the balance from 1.2: sum_f lambda_f*psi(p_f)+sum_i alpha_i*psi(p_i)=sum_i beta_i*psi(p_i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** By 1.1, psi(p_i)>=0 and psi(p_i)<=D:=2+4*delta for every row. With alpha_i,beta_i>=0 and sum_i beta_i=t*(v)<kappa, the equality in 1.3.2 implies sum_f lambda_f*psi(p_f) <= sum_i beta_i*psi(p_i) <= D*sum_i beta_i < kappa*D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Since lambda_f>=0 and sum_f lambda_f=1, the strict weighted-average bound in 1.3.3 implies that some f in F_v has psi(p_f)<kappa*D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.5

**Statement:** Using kappa=tau/4 and D=2+4*delta gives kappa*D=(tau/4)*(2+4*delta)=(1/2+delta)*tau, so the f from 1.3.4 satisfies psi(p_f)<(1/2+delta)*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For the index f from the previous step, membership in F_v gives ||p_f-p_v||_1 >= rho = 4*tau; also phi(p_f)=H-psi(p_f) > H-(1/2+delta)*tau and phi <= dist_1(.,C_W), so dist_1(p_f,C_W) > H-(1/2+delta)*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The index f supplied by 1.3 lies in F_v, and by the definition imported through lem-hiddenness-dual-witness, F_v={j: ||p_j-p_v||_1 >= rho}; with rho=4*tau this gives ||p_f-p_v||_1 >= 4*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Since psi=H-phi and 1.3 gives psi(p_f)<(1/2+delta)*tau, one has phi(p_f)=H-psi(p_f)>H-(1/2+delta)*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** For every c in C_W, phi(c)<=0 and phi is 1-Lipschitz, so phi(p_f)<=phi(c)+||p_f-c||_1<=||p_f-c||_1. Taking the infimum over c in C_W gives phi(p_f)<=dist_1(p_f,C_W).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.4

**Statement:** Combining 1.4.2 and 1.4.3 gives dist_1(p_f,C_W)>H-(1/2+delta)*tau, and C_W is exactly conv{p_w : w in W}; together with 1.4.1 this is the row required by node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

