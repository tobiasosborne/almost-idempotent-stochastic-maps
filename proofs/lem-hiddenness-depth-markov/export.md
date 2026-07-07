# Proof Export

## Node 1

**Statement:** Hiddenness depth-Markov: for an exact signed idempotent P with delta(P) > 0, nonempty visible set W(P), hidden top vertex v of height H, and any hiddenness dual witness (lambda, alpha, beta) of v with sum_i beta_i < kappa = tau/4 (tau = sqrt(delta)), one has for every c > 0: lambda{f in F_v : dist_1(p_f, conv{p_w : w in W}) > H - c*tau} > 1 - (1/2 + delta)/c.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let C=conv{p_w : w in W} and d_i=dist_1(p_i,C). Because W is nonempty and v is a hidden top vertex of height H, d_v=H and 0<=d_i<=H for every row i. Finite-dimensional l1 separation at p_v gives an affine functional phi with phi(p_v)=H, phi(x)<=dist_1(x,C) for all x, and linear part of l_infty norm at most 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-height, since W(P) is nonempty and v is a hidden top vertex of height H, for C=conv{p_w : w in W} and d_i=dist_1(p_i,C) one has d_v=H=max_i d_i; therefore 0<=d_i<=H for every row i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Finite-dimensional l1 support fact: for any nonempty compact convex C and any point x0 with H0=dist_1(x0,C), there exists an affine functional phi whose linear part has l_infty norm at most 1, with phi(x0)=H0 and phi(y)<=0 for every y in C; consequently phi(x)<=dist_1(x,C) for every x.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** If H0=0, the zero affine functional has linear part of l_infty norm 0, satisfies phi(x0)=0, phi(y)=0<=0 on C, and phi(x)=0<=dist_1(x,C) for all x.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** If H0>0, compactness of C gives a nearest point y0 in C with ||x0-y0||_1=H0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.3

**Statement:** For z=x0-y0, the subgradient description of the l1 norm and first-order optimality of y0 for the convex minimization problem min_{y in C} ||x0-y||_1 give a vector s with ||s||_infty<=1, s dot z=||z||_1=H0, and s dot (y-y0)<=0 for every y in C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.4

**Statement:** In the H0>0 case, let y0 be the nearest point from 1.1.2.2 and let s be the support vector supplied by 1.1.2.3; define phi(x)=s dot (x-y0). Then phi(x0)=H0, phi(y)<=0 for y in C, and the linear part has l_infty norm at most 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.4.1

**Statement:** Using the validated support-vector node 1.1.2.3 in the H0>0 case, the vector s satisfies ||s||_infty <= 1, s dot (x0-y0)=H0, and s dot (y-y0) <= 0 for every y in C. Therefore, for phi(x)=s dot (x-y0), phi(x0)=s dot (x0-y0)=H0, phi(y)=s dot (y-y0) <= 0 on C, and the linear part of phi is s, whose l_infty norm is at most 1.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.1.2.4.2

**Statement:** By validated node 1.1.2.3, in the H0>0 case the chosen support vector s satisfies ||s||_infty <= 1, s dot (x0-y0)=H0, and s dot (y-y0) <= 0 for every y in C. Hence for phi(x)=s dot (x-y0), phi(x0)=H0, phi(y)<=0 on C, and the linear part is s with l_infty norm at most 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.5

**Statement:** For any x and any y in C, phi(x)=s dot (x-y)+phi(y)<=s dot (x-y)<=||x-y||_1; taking the infimum over y in C gives phi(x)<=dist_1(x,C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Applying that support fact to x0=p_v and the above C gives the affine phi in 1.1, with phi(p_v)=H, phi(x)<=dist_1(x,C) for all x, and linear part of l_infty norm at most 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** In the context of 1.1, W is nonempty and the row set is finite, so C=conv{p_w : w in W} is a nonempty compact convex subset of finite-dimensional l1 space. By 1.1.1, dist_1(p_v,C)=H. Therefore, after the support fact 1.1.2 is validated, universal instantiation of 1.1.2 with x0=p_v and this C yields an affine phi with phi(p_v)=H, phi(x)<=dist_1(x,C) for all x, and linear part of l_infty norm at most 1.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** With psi=H-phi, every row i satisfies 0<=psi(p_i), psi(p_i)>=H-d_i, and psi(p_i)<=2+4*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** From 1.1, phi(p_i)<=d_i<=H for every row i, so psi(p_i)=H-phi(p_i) is nonnegative and psi(p_i)>=H-d_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Because phi(p_v)=H, psi(p_i)=phi(p_v)-phi(p_i). The linear part of phi has l_infty norm at most 1, hence psi(p_i)<=||p_v-p_i||_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** By the bridge psi(p_i)<=||p_v-p_i||_1 and def-signed-idempotent row geometry, for an exact signed idempotent with negative mass delta every pair of rows has l1 distance at most 2+4*delta; therefore psi(p_i)<=2+4*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** For each row i, node 1.2.2 gives psi(p_i)<=||p_v-p_i||_1. The row-geometry clause of def-signed-idempotent gives ||p_v-p_i||_1<=2+4*delta for the pair of rows p_v and p_i. Therefore psi(p_i)<=2+4*delta for every row i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Using the hiddenness witness balance from lem-hiddenness-dual-witness, applying the linear part of psi gives sum_f lambda_f*psi(p_f)+sum_i alpha_i*psi(p_i)=sum_i beta_i*psi(p_i), hence sum_f lambda_f*psi(p_f)<(1/2+delta)*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By the hypothesis that (lambda,alpha,beta) is a hiddenness dual witness, and by the external lem-hiddenness-dual-witness, lambda_f>=0 on F_v with sum_f lambda_f=1, alpha_i,beta_i>=0, sum_i beta_i<kappa=tau/4, and sum_f lambda_f*(p_f-p_v)+sum_i alpha_i*(p_i-p_v)=sum_i beta_i*(p_i-p_v).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Since psi is affine and psi(p_v)=0, applying the linear part of psi to the witness balance gives sum_f lambda_f*psi(p_f)+sum_i alpha_i*psi(p_i)=sum_i beta_i*psi(p_i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** By 1.2, psi(p_i)>=0 and psi(p_i)<=2+4*delta for every row i; with alpha_i,beta_i>=0, the equality implies sum_f lambda_f*psi(p_f)<=sum_i beta_i*psi(p_i)<kappa*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Because kappa=tau/4, kappa*(2+4*delta)=(1/2+delta)*tau, giving sum_f lambda_f*psi(p_f)<(1/2+delta)*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Consequently sum_f lambda_f*(H-d_f)<(1/2+delta)*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** For each f in F_v, 1.2 gives psi(p_f)>=H-d_f.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** The coefficients lambda_f are nonnegative, so summing the inequalities in 1.4.1 and using 1.3 gives sum_f lambda_f*(H-d_f)<=sum_f lambda_f*psi(p_f)<(1/2+delta)*tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For arbitrary c>0, Markov applied to the nonnegative variables H-d_f under the probability lambda on F_v gives lambda{f in F_v : d_f<=H-c*tau}<(1/2+delta)/c, equivalently lambda{f in F_v : d_f>H-c*tau}>1-(1/2+delta)/c.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Because delta>0 and tau=sqrt(delta), tau>0; because c>0, c*tau>0. Also, with C=conv{p_w : w in W} and d_i=dist_1(p_i,C), the fact that v is a hidden top vertex of height H gives d_i<=H for every row i; hence X_f:=H-d_f is nonnegative for every f in F_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.1

**Statement:** By def-height, since W(P) is nonempty and v is a hidden top vertex of height H, for C=conv{p_w : w in W} and d_i=dist_1(p_i,C) one has H=max_i d_i. Therefore d_f<=H for every row index f, in particular for every f in F_v, and X_f=H-d_f>=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Let A_c={f in F_v : d_f<=H-c*tau}. Then A_c={f in F_v : X_f>=c*tau}, so c*tau*lambda(A_c)<=sum_{f in A_c} lambda_f*X_f<=sum_f lambda_f*X_f.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** Using 1.4 and dividing by c*tau gives lambda(A_c)<(1/2+delta)/c.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.4

**Statement:** Since sum_f lambda_f=1 on F_v, the complement of A_c has lambda-mass greater than 1-(1/2+delta)/c; this complement is {f in F_v : d_f>H-c*tau}, which is the asserted set because d_f=dist_1(p_f,conv{p_w : w in W}).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

