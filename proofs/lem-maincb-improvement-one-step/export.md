# Proof Export

## Node 1

**Statement:** There are universal K_step >= 1 and e_step > 0 such that, if B is a finite-dimensional C*-algebra, A an extended epsilon-C*-algebra, and v:B->A an extended d-inclusion with d+epsilon <= e_step, then one dagger-preserving level-one map v^+, with v_n^+ = I_n tensor v^+, satisfies sup_n ||v_n^+ - v_n|| <= K_step*d and is an extended d^+-inclusion for d^+ <= K_step*(d^2+epsilon).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Every finite-dimensional C*-algebra B has a diagonal D=sum_j A_j tensor B_j in the sense of def-fd-cstar-diagonal with sum_j ||A_j|| ||B_j||=1; this representation is dimension-free.

**Type:** claim

**Inference:** proof_by_construction

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Let C be a finite-dimensional unital C*-algebra. First note the following elementary finite-dimensional spectral fact, used below rather than any classification theorem. If a=a^dagger, then exp(ita) is unitary, so spectral mapping forces spectrum(a) to be real; the spectral-radius formula together with the C*-identity gives ||a||=r(a). Hence the polynomial product over the distinct spectral values annihilates a, and Lagrange interpolation gives a=sum_lambda lambda p_lambda with pairwise orthogonal self-adjoint projections p_lambda summing to 1. In particular spectral support projections are polynomials with zero constant term.

For every nonzero dagger-ideal I of C choose a basis x_1,...,x_N and put h=sum_k(x_k^dagger x_k+x_k x_k^dagger). Let z be the spectral support projection of h. Since z is a polynomial in h with zero constant term, z lies in I. From h(1-z)=0 and positivity of each summand, (1-z)x_k^dagger x_k(1-z)=0 and (1-z)x_k x_k^dagger(1-z)=0; the C*-identity gives x_k(1-z)=0=(1-z)x_k. Thus z is the two-sided identity of I. For c in C, both cz and zc lie in I, whence zcz=cz and zcz=zc, so z is central.

Apply the spectral fact inside Z(C) and repeatedly take a nonzero projection minimal among central projections. This gives orthogonal minimal central projections z_1,...,z_m with sum z_r=1 and C=direct_sum_r C_r, C_r=z_r C. Any central self-adjoint element of C_r has central spectral projections below z_r and is therefore scalar; hence Z(C_r)=C z_r. If J is a nonzero dagger-ideal of C_r, the preceding ideal argument gives it a nonzero central identity, necessarily z_r, so J=C_r. Thus each C_r is simple.

Fix one simple C_r, writing its unit as 1. A nonzero projection exists by taking the spectral support of y^dagger y for nonzero y. Choose a nonzero projection p minimizing dim(p C_r p). If p C_r p were not C p, a non-scalar self-adjoint element in it would have a nonzero proper spectral projection q<p and q C_r q would have smaller dimension. Hence p C_r p=C p. Since C_r p C_r is a nonzero dagger-ideal, simplicity gives C_r p C_r=C_r. Set v_1=p and p_1=p. Inductively, suppose v_i^dagger v_i=p and the projections p_i=v_i v_i^dagger are pairwise orthogonal. If e=1-sum_i p_i is nonzero, an expression 1=sum_l a_l p b_l implies some x=e a_l p is nonzero. Then x^dagger x belongs to p C_r p, so x^dagger x=lambda p with lambda>0. For v=lambda^(-1/2)x one has v^dagger v=p and vv^dagger is a projection below e. Adjoining v therefore extends the family. Finite dimensionality makes the process terminate with sum_i p_i=1.

Put e_ij=v_i v_j^dagger. Orthogonality gives v_j^dagger v_k=delta_jk p, hence e_ij e_kl=delta_jk e_il and e_ij^dagger=e_ji. Moreover, for a in C_r, v_i^dagger a v_j lies in p C_r p=Cp, so p_i a p_j is a scalar multiple of e_ij. As a=sum_ij p_i a p_j, the e_ij span C_r. Therefore E_ij maps to e_ij is a bijective unital dagger-homomorphism M_q to C_r. It preserves spectra algebraically; applying ||b||=r(b) to the positive elements b=a^dagger a and using the C*-identity proves ||Phi(a)||^2=r(Phi(a^dagger a))=r(a^dagger a)=||a||^2. Thus the identification, and consequently the central direct-sum identification, is *-isometric.

It remains to construct the diagonal in a block without further structure input. In M_q index matrix units modulo q, let omega=exp(2 pi i/q), S xi_k=xi_(k+1), T xi_k=omega^k xi_k, and W_ab=S^a T^b. These are unitaries and character orthogonality gives
q^(-2) sum_(a,b) W_ab^dagger tensor W_ab = q^(-1) sum_(i,j) E_ij tensor E_ji=:D_q.
For X=E_rs, direct multiplication gives X D_q=q^(-1)sum_j E_rj tensor E_js=D_q X, hence the equality for every X; also pi(D_q)=q^(-1)sum_(i,j)E_ij E_ji=I. The displayed Weyl expression has q^2 positive coefficients q^(-2), each multiplying U^dagger tensor U with U unitary, so the sum of the corresponding norm products is exactly 1.

**Type:** claim

**Inference:** explicit_finite_dimensional_construction

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For B=direct_sum_(r=1)^m M_(q_r), independently choose in each block a Pauli unitary W_(r,a,b) and a sign sigma_r in {+1,-1}, and average U^dagger tensor U over U=direct_sum_r sigma_r W_(r,a,b). Independent sign averaging kills every cross-block tensor component, while within each block it leaves D_(q_r); hence the average is a diagonal of B. It is a convex combination of U^dagger tensor U with U unitary, so its displayed representation has sum_j||A_j||||B_j||=1, independent of m and all q_r.

**Type:** claim

**Inference:** explicit_finite_dimensional_construction

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix such a diagonal. For g(X,Y)=v(XY)-v(X)v(Y), define w_prime(X)=sum_j v(A_j)g(B_j,X), w_doubleprime(X)=w_prime(X^dagger)^dagger, w=(w_prime+w_doubleprime)/2, and v^+=v+w. For all n, I_n tensor w is exactly the correction obtained from v_n and I_n tensor D, and there is a universal C_w such that sup_n ||I_n tensor w|| <= C_w d whenever d+epsilon is sufficiently small.

**Type:** claim

**Inference:** proof_by_construction

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For X=[X_pq] in M_n tensor B, the defining matrix product gives [g_n(I_n tensor B_j,X)]_pq=g(B_j,X_pq), and then [sum_j v_n(I_n tensor A_j)g_n(I_n tensor B_j,X)]_pq=w_prime(X_pq). The adjoint rule gives the same identity for w_doubleprime. Therefore the correction constructed at every level is exactly I_n tensor w and v_n^+=I_n tensor v^+; no level-dependent choice is made.

**Type:** claim

**Inference:** entrywise_identity_and_norm_estimate

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Invoke the registered external GT-kitaev-standard-diagonal: choose D=sum_j A_j tensor B_j with A_j=p_j U_j^dagger, B_j=U_j, p_j>=0, sum_j p_j=1, and U_j unitary. Thus D is a diagonal in the sense of def-fd-cstar-diagonal and sum_j||A_j||||B_j||=1, with no classification theorem or sibling result being used. For X=[X_pq] in M_n tensor B, define g_n(S,T)=v_n(ST)-v_n(S)v_n(T) and W_prime_n(X)=sum_j v_n(I_n tensor A_j)g_n(I_n tensor B_j,X). Direct matrix multiplication gives [g_n(I_n tensor B_j,X)]_pq=g(B_j,X_pq), hence [W_prime_n(X)]_pq=w_prime(X_pq), so W_prime_n=I_n tensor w_prime; applying the level-n involution gives W_doubleprime_n=I_n tensor w_doubleprime. By the block-diagonal axiom in def-operator-space, ||I_n tensor A_j||=||A_j|| and ||I_n tensor B_j||=||B_j||. Unpacking def-extended-delta-inclusion at level n gives ||v_n(S)||<=(1+d)||S|| and, through its d-homomorphism clause, ||g_n(S,T)||<=d||S||||T||. Unpacking def-extended-epsilon-cstar-algebra through the registered def-epsilon-cstar-algebra gives ||ST||<=(1+epsilon)||S||||T|| and an isometric involution. Consequently ||W_prime_n(X)|| <= (1+epsilon)(1+d)d sum_j||A_j||||B_j||||X||=(1+epsilon)(1+d)d||X||, and the same bound holds for W_doubleprime_n. Since I_n tensor w=(W_prime_n+W_doubleprime_n)/2 and d+epsilon<=1/4 implies (1+epsilon)(1+d)<=25/16<2, one has ||I_n tensor w||<=2d uniformly in n and B.

**Type:** claim

**Inference:** entrywise_identity_and_norm_estimate

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The same correction satisfies, at every amplification, ||v_n^+(XY)-v_n^+(X)v_n^+(Y)|| <= C_m(d^2+epsilon)||X||||Y|| for a universal C_m independent of B, A, n, d, and epsilon.

**Type:** claim

**Inference:** proof_by_construction

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Fix n. The following inequalities are not extra hypotheses: def-extended-epsilon-cstar-algebra says M_n tensor A is an epsilon-C*-algebra, and registered def-epsilon-cstar-algebra therefore gives ||ST||<=(1+epsilon)||S||||T||, ||(ST)R-S(TR)||<=epsilon||S||||T||||R||, the isometric anti-multiplicative involution, and the epsilon-unit bounds. Likewise, def-extended-delta-inclusion says v_n=I_n tensor v is a d-inclusion; unpacking its d-homomorphism and two-sided norm clauses gives ||v_n(T)||<=(1+d)||T||, ||v_n(ST)-v_n(S)v_n(T)||<=d||S||||T||, ||v_n(I)-I||<=d, and dagger preservation. By the registered external GT-kitaev-standard-diagonal choose D=sum_j A_j tensor B_j with sum_j||A_j||||B_j||=1, XD=DX, and sum_j A_jB_j=I. Put a_j=I_n tensor A_j, b_j=I_n tensor B_j, g_n(X,Y)=v_n(XY)-v_n(X)v_n(Y), w_prime_n(X)=sum_j v_n(a_j)g_n(b_j,X), and F_z(X,Y)=v_n(X)z(Y)-z(XY)+z(X)v_n(Y). Direct expansion, using associativity in the source algebra B, gives v_n(X)g_n(Y,Z)-g_n(XY,Z)+g_n(X,YZ)-g_n(X,Y)v_n(Z)=(v_n(X)v_n(Y))v_n(Z)-v_n(X)(v_n(Y)v_n(Z)); the registered epsilon-associativity inequality bounds the right side by epsilon(1+d)^3||X||||Y||||Z||<=2epsilon||X||||Y||||Z|| when d+epsilon<=1/4. Expand F_(w_prime_n). Reassociate v_n(X)(v_n(a_j)g_n(b_j,Y)), replace v_n(X)v_n(a_j) by v_n(Xa_j), and use the amplified identity XD=DX to change the summed expression exactly to sum_j v_n(a_j)g_n(b_jX,Y). Reassociate the third term to put v_n(a_j) outside and apply the displayed cocycle identity to (b_j,X,Y), giving sum_j v_n(a_j)(v_n(b_j)g_n(X,Y)) up to its residual. Reassociate again, replace v_n(a_j)v_n(b_j) by v_n(a_jb_j), use sum_j a_jb_j=I, and finally replace v_n(I)g_n(X,Y) by g_n(X,Y). The seven errors, in this order, are bounded by epsilon(1+d)^2*d, (1+epsilon)d^2, epsilon(1+d)^2*d, 2(1+epsilon)(1+d)epsilon, epsilon(1+d)^2*d, (1+epsilon)d^2, and ((1+epsilon)d+epsilon)d, times ||X||||Y|| sum_j||A_j||||B_j||. Each bound follows respectively from the explicitly cited epsilon-associativity, d-multiplicativity, product, and epsilon-unit/d-unit inequalities. Since the weight sum is 1 and d+epsilon<=1/4, their sum is at most 100(d^2+epsilon)||X||||Y||. Hence ||F_(w_prime_n)(X,Y)-g_n(X,Y)||<=100(d^2+epsilon)||X||||Y|| uniformly in n.

**Type:** claim

**Inference:** cocycle_homotopy_and_quadratic_remainder

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Because v preserves the involution, g_n(Y^dagger,X^dagger)^dagger=g_n(X,Y); the definition w_doubleprime(X)=w_prime(X^dagger)^dagger therefore gives ||F_(w_doubleprime)-g_n||<=100(d^2+epsilon). Linearity of F gives the same estimate for w. The exact bilinear expansion G_(v+w)=g-F_w-w(X)w(Y), together with ||w_n||<=2d and the product bound, gives ||G_(v^+)_n(X,Y)||<=105(d^2+epsilon)||X||||Y||. Thus C_m=105 is universal.

**Type:** claim

**Inference:** cocycle_homotopy_and_quadratic_remainder

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Let v^+=v+w, where v is dagger-preserving, w_doubleprime(X)=w_prime(X^dagger)^dagger, and w=(w_prime+w_doubleprime)/2. Assume the two estimates supplied separately by the correction branches: sup_n ||I_n tensor w|| <= 2d and, at every amplification, ||v_n^+(XY)-v_n^+(X)v_n^+(Y)|| <= 105(d^2+epsilon)||X||||Y||. Then v^+ is dagger-preserving. Put q=d^2+epsilon, mu=105q, x=v^+(I_B), and y=x-I_A. The level-one displacement estimate and the d-unit bound for v give ||y|| <= 3d, while the multiplicative estimate at X=Y=I_B gives ||x^2-x|| <= mu. Expanding x=I_A+y and isolating y gives ||y|| <= mu+epsilon(1+epsilon)+2epsilon||y||+(1+epsilon)||y||^2. If d+epsilon <= 1/16, then ||y|| <= 3/16 and 2epsilon+(1+epsilon)||y|| <= 83/256; hence ||y|| <= (272/173)(mu+epsilon) < 4(mu+epsilon) <= 424q. Finally I_n tensor y is the block diagonal direct sum of n copies of y, so the operator-space direct-sum axiom gives ||I_n tensor y||=||y||. Thus every amplification has unit defect at most 424(d^2+epsilon).

**Type:** claim

**Inference:** proof_by_construction

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Put q=d^2+epsilon and mu_star=424q. Suppose u:B->A is a dagger-preserving linear map with u_n=I_n tensor u such that, for every n, ||u_n-v_n||<=2d, ||u_n(XY)-u_n(X)u_n(Y)||<=105q||X||||Y||, and ||u_n(I)-I||<=mu_star. Then, if d+epsilon<=e_step:=min{1/16,1/(8*424)}, u is an extended d^+-inclusion for d^+:=max{mu_star,4(mu_star+epsilon),2mu_star+epsilon}<=1700q. Indeed, let M_n=||u_n|| and a_n=inf_(||X||=1)||u_n(X)||. Dagger preservation, the target C*-inequality, multiplicativity, and ||X^dagger X||=||X||^2 give (1-epsilon)M_n^2<=M_n+mu_star. For R=1+4(mu_star+epsilon), (1-epsilon)R^2-R-mu_star=3(mu_star+epsilon)+(1-epsilon)[4(mu_star+epsilon)]^2-8epsilon(mu_star+epsilon)>=0 because epsilon<=1/4; hence M_n<=R. The lower norm bound for v and ||u_n-v_n||<=2d give a_n>=1-3d>=1/2. For unit X, the lower bound a_n applied to X^dagger X, followed by multiplicativity and the target product inequality, gives a_n<=(1+epsilon)||u_n(X)||^2+mu_star; taking the infimum yields a_n<=(1+epsilon)a_n^2+mu_star. If a_n>=1 there is nothing to prove, while if a_n<1, division by a_n>=1/2 gives 1-a_n<=epsilon*a_n+mu_star/a_n<=epsilon+2mu_star. Thus every amplification has the two-sided (1+-d^+) norm bounds; its multiplicative defect is at most 105q<=mu_star<=d^+, its unit defect is at most mu_star<=d^+, and it preserves the dagger. Therefore u is an extended d^+-inclusion. Since epsilon<=q, d^+<=max{424,4(424+1),2*424+1}q=1700q.

**Type:** claim

**Inference:** proof_by_construction

**Status:** validated

**Taint:** clean

