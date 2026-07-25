# Proof Export

## Node 1

**Statement:** EXT-CB: there are universal C_ext < infinity and e_ext > 0 such that if e=delta+epsilon <= e_ext, P,Q are delta-projections in an extended epsilon-C*-algebra A with ||P+Q-I|| <= delta, v:M_r->S_P is an extended delta-isomorphism, dim S_Q=1 at level one, and S_{P,Q} is nonzero, then there is one map v_+:M_{r+1}->A whose every amplification is a C_ext*e-isomorphism; the same level-one unitary and the same four corner maps carry all amplification levels, with constants independent of r, n, and dim A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Setup and level-one dimensions. Assume the root hypotheses and put e=delta+epsilon, P_1=P, P_2=Q, H_j=S_{P_j,Q}, K_1=C^r and K_2=C. By def-extcb-datum these hypotheses are an EXT-CB datum. Choose e below the universal threshold e_sel of lem-extcb1-cross-corner-dimension. That external gives dim H_1=dim S_{P,Q}=r and dim H_2=dim S_{Q,Q}=1. This is exclusively a level-one use of dim S_Q=1; no amplification of Q is called one-dimensional. Choose once and for all a unitary U_2:K_2->H_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Dimension-free exact-target correction lemma. There are universal a_corr>0 and C_corr<infinity with the following property: if B is a finite-dimensional C*-algebra, H a finite-dimensional Hilbert space, and T:B->B(H) is linear, dagger-preserving, has ||T_n(XY)-T_n(X)T_n(Y)||<=a||X||||Y|| and ||T_n(I)-I||<=a at every n, where 0<=a<=a_corr, then one unital dagger-homomorphism mu:B->B(H) satisfies ||mu_n-T_n||<=C_corr*a at every n. The same level-one mu is used at every amplification. This lemma is proved in children 1.2.1--1.2.3 from the norm-one diagonal and Newton correction, with no external theorem.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Uniform cb control, exact unitalization, and the norm-one diagonal. At each n and ||X||=1, dagger preservation and the defect estimate give ||T_n(X)||^2<=||T_n(X^dagger X)||+a, so M_n=||T_n|| satisfies M_n^2<=M_n+a and hence ||T||_cb<=2 for a<=1. Fix a state phi on B and define S_0(x)=T(x)+phi(x)(I-T(I)). States have cb norm one and phi(x^dagger)=conj(phi(x)), so S_0 is dagger-preserving, exactly unital, ||S_0-T||_cb<=a, ||S_0||_cb<=3, and direct expansion gives multiplicative defect b_0<=c_u*a with the numerical universal c_u=7. For every finite-dimensional C*-algebra B, normalized Haar measure on its compact unitary group gives D=int U^dagger tensor U dU. In finite dimension D is a finite convex combination sum_s p_s U_s^dagger tensor U_s with projective norm one; Haar invariance gives XD=DX and multiplication(D)=I. For a defect G of S, w'(x)=sum_s S(p_s U_s^dagger)G(U_s,x) satisfies ||w'||_cb<=||S||_cb||G||. At level n the same formula is entrywise I_n tensor w', because the diagonal identity moves arbitrary matrix entries. Thus every correction is one level-one map with bounds independent of n and all dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** One normalized Newton correction. Let S:B->B(H) be exactly unital, dagger-preserving, ||S||_cb<=4, with multiplicative defect G of uniform amplified bilinear norm b. Use node 1.2.1 and put w'(x)=sum_s S(p_s U_s^dagger)G(U_s,x), w''(x)=w'(x^dagger)^dagger, w=(w'+w'')/2, and S^+=S+w. Since G(y,I)=G(I,y)=0, w(I)=0; hence S^+ remains unital and dagger-preserving, with ||w||_cb<=4b. Exact associativity gives S(x)G(y,z)-G(xy,z)+G(x,yz)-G(x,y)S(z)=0. Expanding S(x)w(y)-w(xy)+w(x)S(y), using XD=DX, multiplication(D)=I, and S(I)=I, cancels G exactly to first order; every remaining term contains two defect factors. A direct triangle estimate therefore gives ||G_{S^+}||<=K_N*b^2 at every amplification for one numerical universal K_N, while ||S^+-S||_cb<=4b. Node 1.2.1 makes the identities uniform and ensures S^+ is the amplification of the same corrected level-one map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Convergence and exactness. Choose a_corr>0 so K_N*c_u*a_corr<=1/2 and 8*c_u*a_corr<1. Start from the exactly unital S_0 of node 1.2.1 and apply node 1.2.2 recursively. With b_0<=c_u*a and b_{k+1}<=K_N*b_k^2, one has b_k<=b_0*2^{-k}. Thus ||S_k-S_0||_cb<=sum_k 4b_k<=8c_u*a<1; since ||S_0||_cb<=3, every S_k has cb norm below 4 and every iteration is justified. The sequence converges in cb norm to one unital dagger-preserving linear map mu, and passing to the limit gives mu(xy)=mu(x)mu(y). Moreover ||mu-T||_cb<=||S_0-T||_cb+||mu-S_0||_cb<=(1+8c_u)a, and amplification commutes with the limit. Hence node 1.2 holds with the universal C_corr=1+8c_u=57, using the same level-one mu at all n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** Validated-dependency and induction bridge. Nodes 1.2.1 and 1.2.2 are now validated. Let b_k be the uniform amplified bilinear norm of the multiplicative defect of S_k. Node 1.2.1 gives an exactly unital dagger-preserving S_0 with ||S_0||_cb<3, b_0<=c_u*a, and ||S_0-T||_cb<=a. Assume inductively that S_k is exactly unital and dagger-preserving, ||S_k||_cb<4, and b_k<=b_0*2^{-k}. Node 1.2.2 applies and produces the same level-one map S_{k+1} at all amplifications, still exactly unital and dagger-preserving, with ||S_{k+1}-S_k||_cb<=4b_k and b_{k+1}<=K_N*b_k^2. Since K_N*b_0<=K_N*c_u*a<=1/2, b_{k+1}<=b_k/2<=b_0*2^{-(k+1)}. Moreover ||S_k-S_0||_cb<=sum_{j<k}4b_j<=8b_0<=8c_u*a<1, hence ||S_k||_cb<4 and the induction closes. This estimate also covers b_0=0: then b_k=0 for every k and every correction increment vanishes. Therefore sum_k ||S_{k+1}-S_k||_cb<=8b_0, so S_k converges in cb norm to one exactly unital dagger-preserving map mu. For each x,y, continuity of multiplication and b_k->0 give mu(xy)-mu(x)mu(y)=lim_k [S_k(xy)-S_k(x)S_k(y)]=0. Cb convergence means sup_n ||(S_k-mu)_n||->0, so every mu_n is the amplification of this same level-one mu and ||mu-T||_cb<=a+8c_u*a=57a (c_u=7). Thus the application of the now-validated Newton correction is permitted and all its hypotheses are verified at every iteration.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.3.1.1

**Statement:** Degenerate-safe geometric estimate. Replace the strict bound in the parent node by ||S_k-S_0||_cb <= sum_{j<k} 4 b_j <= 4 b_0 sum_{j=0}^{k-1}2^{-j} <= 8 b_0 <= 8 c_u a < 1. This remains valid when b_0=0: then b_k<=b_0 2^{-k}=0 for every k, so every b_k=0 and the correction bounds give ||S_{k+1}-S_k||_cb<=4b_k=0. In all cases, ||S_k||_cb <= ||S_0||_cb+||S_k-S_0||_cb < 3+1=4, because ||S_0||_cb<3 and the displacement bound is strictly less than 1. Thus the induction closes without assuming b_0>0. Likewise, sum_{k>=0}||S_{k+1}-S_k||_cb <= 4 sum_{k>=0}b_k <= 8b_0; no strict geometric-series inequality is required.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Construction of one spatial four-corner system. Define h_jk=Ha^Q_{P_j,P_k} and T=h_11 composed with v. The product, unit, upper-norm and adjoint clauses of conj-hcb together with def-extended-delta-inclusion imply, uniformly in n, that T is a dagger-preserving extended A_0*e-homomorphism for a universal A_0 (for example after enlarging C_H, A_0=4(C_H+1)). Apply node 1.2 at e small enough to get one exact unital dagger-homomorphism mu_11:M_r->B(H_1) with ||mu_11,n-h_11,n v_n||<=kappa*e, kappa=C_corr*A_0. It is nonzero, hence injective because M_r is simple, and it is onto because both spaces have dimension r^2 by node 1.1. Thus it is a spatial dagger-isomorphism: choose one unitary U_1:C^r->H_1 with mu_11(A)=U_1 A U_1^dagger. With the already fixed U_2, define mu_jk(A)=U_j A U_k^dagger for A in B(K_k,K_j). These four fixed level-one maps are exact, completely isometric, adjoint-compatible and multiplicative at all amplifications via I_n tensor U_j; no level-dependent choice is made.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** The amplified defect of T. For X,Y in M_n tensor M_r, def-extended-delta-inclusion gives ||v_n(XY)-v_n(X) dot v_n(Y)||<=delta||X||||Y||, ||v_n(X)||<=(1+delta)||X||, exact dagger preservation, and the corresponding unit estimate in the compressed algebra S_P. The upper, product, unit and adjoint clauses of conj-hcb for h_11,n therefore give ||T_n(XY)-T_n(X)T_n(Y)|| <= (1+C_H*e)delta||X||||Y||+C_H*e*(1+delta)^2||X||||Y|| and ||T_n(I)-I||<=A_0*e; dagger is exact. For e below one universal bound, both defects are <=A_0*e with A_0=4(C_H+1), independent of n,r and dim A. Thus node 1.2 applies and supplies one exact unital dagger-homomorphism mu_11 with complete distance at most kappa*e, kappa=C_corr*A_0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Endpoint/positive-parameter case split closing the correction step. The error tolerances delta and epsilon are nonnegative, so e=delta+epsilon is nonnegative. If e=0, then delta=epsilon=0. Substitution in the already established amplified estimates of node 1.3.1 gives, for every n and X,Y, ||T_n(XY)-T_n(X)T_n(Y)||<=0 and ||T_n(I)-I||<=0, while dagger preservation is exact. Hence the linear map T:M_r->B(H_1) is itself an exact unital dagger-homomorphism at level one (and its fixed amplifications have the same exact identities); define mu_11:=T. Then ||mu_11,n-T_n||=0=kappa*e for every n. If e>0, shrink the universal threshold further so that e<a_corr/A_0 and retain the preceding defect bound with correction parameter a=A_0*e. Then 0<a<a_corr, node 1.2 applies, and its single level-one unital dagger-homomorphism mu_11 satisfies ||mu_11,n-T_n||<C_corr*A_0*e=kappa*e for every n, hence also the asserted at-most bound. These two cases exhaust e>=0 and use no level-, rank-, or dimension-dependent choice.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.1.1.1

**Statement:** Validated-dependency bridge for the correction step. Require node 1.2 to be validated before the positive-parameter conclusion of this child is available. Let A_0=4(C_H+1)>0 and kappa=C_corr*A_0, and shrink the universal EXT-CB threshold so e<=a_corr/(2*A_0). Node 1.3.1 gives, at every amplification, exact dagger preservation and multiplicative and unit defects at most A_0*e for the same level-one map T. If e=0, nonnegativity of delta and epsilon gives delta=epsilon=0, so both defects vanish; hence T itself is an exact unital dagger-homomorphism and mu_11:=T has ||mu_11,n-T_n||=0=kappa*e for every n, without using node 1.2. If e>0, set a=A_0*e. Then 0<a<=a_corr/2<a_corr, so all hypotheses of the now-required validated node 1.2 hold. It supplies one level-one unital dagger-homomorphism mu_11 whose fixed amplifications satisfy ||mu_11,n-T_n||<C_corr*a=kappa*e, hence <=kappa*e, for every n. Thus the correction conclusion follows on the full e>=0 scope, but the e>0 branch is explicitly blocked until node 1.2 is validated; no unvalidated dependency is used.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.3.1.1.2

**Statement:** Dependency-gated positive-parameter application. This child requires validated node 1.2. Under the universal threshold e<=a_corr/(2*A_0), the e>0 branch has correction parameter a=A_0*e satisfying 0<a<a_corr. The amplified defect and unit estimates of node 1.3.1 and exact dagger preservation verify every hypothesis of node 1.2 for the same level-one map T, so validated node 1.2 yields one unital dagger-homomorphism mu_11 with ||mu_11,n-T_n||<C_corr*A_0*e=kappa*e at every n. The separate e=0 calculation in node 1.3.1.1 uses mu_11=T and needs no correction lemma. Consequently the complete e>=0 conclusion is available only after node 1.2 is validated.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Spatiality and all exact corners. By node 1.1 dim H_1=r. The unital mu_11 is nonzero; its kernel is a two-sided ideal in the simple algebra M_r, hence zero. Domain M_r and codomain B(H_1) both have dimension r^2, so mu_11 is onto. A unital dagger-isomorphism between full matrix algebras preserves rank-one projections and matrix units, hence choosing an orthonormal basis in their ranges gives a single unitary U_1:C^r->H_1 with mu_11(A)=U_1 A U_1^dagger. Together with the single U_2 from node 1.1, mu_jk(A)=U_j A U_k^dagger is a bijective linear isometry B(K_k,K_j)->B(H_k,H_j). Direct multiplication and adjoint calculation gives mu_jl(XY)=mu_jk(X)mu_kl(Y), mu_kj(X^dagger)=mu_jk(X)^dagger and mu_jj(I)=I. Tensoring the same identities with I_n proves complete isometry and all amplified identities without new choices.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Conditional Ha inverses, in the required order. Shrink the universal threshold so kappa*e<1 and C_H*e<1/4. Since mu_11 is invertible and ||T-mu_11||<1, T is bijective by Neumann inversion; v is bijective, so h_11 is bijective. Moreover for Z=v(A), ||h_11(Z)||/||Z|| >= (1-kappa*e)/(1+delta)>1/4. The canonical-identity closeness clause of conj-hcb makes h_12,h_21,h_22 level-one bijections by Neumann inversion and gives h_22 level-one lower modulus at least 1/4. Only now apply the conditional clauses of conj-hcb: the diagonal clause to h_11 and h_22, the off-diagonal clause to h_12 anchored at h_22, and to h_21 anchored at h_11. Hence every h_jk,n is bijective, (1-C_H*e)||Z||<=||h_jk,n(Z)||<=(1+C_H*e)||Z|| and ||h_jk,n^{-1}||<=1+C_H*e. Algebraically h_jk,n^{-1}=I_n tensor h_jk^{-1}, so the inverses are not chosen afresh at level n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Level-one triggers are established before inversion clauses. At n=1, identify T with mu_11 followed by I+mu_11^{-1}(T-mu_11); since ||T-mu_11||<=kappa*e<1 and mu_11 is isometric, the parenthesized operator is invertible by its Neumann series. Thus T and then h_11=T composed with v^{-1} are bijective. If Z=v(A), then ||h_11(Z)||>=||mu_11(A)||-kappa*e||A||=(1-kappa*e)||A||, whereas ||Z||<= (1+delta)||A||, so the lower modulus of h_11 is at least (1-kappa*e)/(1+delta)>1/4. Separately, the canonical-identity closeness estimates in conj-hcb make each of h_12,h_21,h_22 a strict-norm perturbation of its canonical level-one bijection when e is universally small. Neumann inversion gives their level-one bijectivity, and for h_22 the same estimate gives lower modulus >1/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Apply precisely the conditional H-CB clauses. The established bijectivity and lower modulus allow the diagonal clause of conj-hcb first for h_11 and h_22, yielding bijectivity of every amplification and inverse norm <=1+C_H*e. Then apply its off-diagonal clause to h_12 with diagonal anchor h_22 and to h_21 with diagonal anchor h_11; all hypotheses were established in node 1.4.1. Together with the unconditional upper bounds this gives the two-sided estimates in node 1.4 for every j,k,n. Finally, for a level-one linear bijection h_jk, tensor algebra gives (I_n tensor h_jk)(I_n tensor h_jk^{-1})=I and the reverse product, so uniqueness of inverse gives h_jk,n^{-1}=I_n tensor h_jk^{-1}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Four fixed corner maps form a merging datum. Define gamma_11=v and gamma_jk=h_jk^{-1} composed with mu_jk for (j,k)!=(1,1). These are four bijective level-one maps and their amplifications are fixed. Put d_jk,n=h_jk,n gamma_jk,n-mu_jk,n. Then ||d_11,n||<=kappa*e while d_12,n=d_21,n=d_22,n=0. Exact adjointness from conj-hcb and the spatial system gives gamma_kj,n(X^dagger)=gamma_jk,n(X)^dagger. Using the product-defect and inverse bounds from conj-hcb, the exact multiplication of mu, and the displayed d bounds gives ||gamma_jl,n(XY)-gamma_jk,n(X) dot gamma_kl,n(Y)||<=5(C_H+kappa)e||X||||Y||. The unit and upper/lower norm clauses of conj-hcb similarly give diagonal-unit error <=3(C_H+kappa)e and (1-(C_H+kappa)e)||X||<=||gamma_jk,n(X)||<=(1+2(C_H+kappa)e)||X||. Since ||P_1+P_2-I||<=delta<=e, all clauses of def-four-corner-merging-datum hold with one common rho=D_0*e, D_0=5(C_H+kappa), after harmless enlargement. Details are supplied by children 1.5.1--1.5.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Comparison, fixed amplifications, and exact adjoints. For (j,k)!=(1,1), h_jk,n gamma_jk,n=mu_jk,n because node 1.4 gives h_jk,n^{-1}=I_n tensor h_jk^{-1}; for (1,1), node 1.3 gives ||h_11,n v_n-mu_11,n||<=kappa*e. Thus the d bounds in node 1.5 hold at every n for the same four level-one maps. For the off-diagonal pair, exact H-CB adjointness gives h_kj,n(gamma_jk,n(X)^dagger)=h_jk,n(gamma_jk,n(X))^dagger=mu_jk,n(X)^dagger=mu_kj,n(X^dagger)=h_kj,n gamma_kj,n(X^dagger); injectivity of h_kj,n gives exact equality of the arguments. The diagonal transported corner is identical, while gamma_11=v preserves dagger by def-extended-delta-inclusion. Hence the involution clause is exact.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.1

**Statement:** Dependency bridge and complete derivation, valid only after nodes 1.3 and 1.4 are validated on the full EXT-CB scope (including e=0). Node 1.3 then supplies one fixed level-one spatial system mu_jk with mu_jk,n=I_n tensor mu_jk and ||h_11,n v_n-mu_11,n||<=kappa*e for every n; node 1.4 supplies level-one bijectivity of every h_jk, bijectivity (hence injectivity) of every h_jk,n, and h_jk,n^{-1}=I_n tensor h_jk^{-1}. Define gamma_11=v and gamma_jk=h_jk^{-1} mu_jk otherwise. Hence gamma_jk,n=I_n tensor gamma_jk and, for (j,k)!=(1,1), h_jk,n gamma_jk,n=(I_n tensor h_jk)(I_n tensor h_jk^{-1}mu_jk)=mu_jk,n, while d_11,n=h_11,n v_n-mu_11,n has norm at most kappa*e. Thus all comparison bounds hold also at e=0. For every (j,k)!=(1,1), including (2,2), exact H-CB adjointness and spatial adjoint compatibility give h_kj,n(gamma_jk,n(X)^dagger)=h_jk,n(gamma_jk,n(X))^dagger=mu_jk,n(X)^dagger=mu_kj,n(X^dagger)=h_kj,n gamma_kj,n(X^dagger); injectivity of h_kj,n yields gamma_jk,n(X)^dagger=gamma_kj,n(X^dagger). For (1,1), gamma_11,n=v_n preserves dagger because every amplification of an extended delta-inclusion is a delta-homomorphism, which in the star-algebra setting preserves dagger exactly. Therefore the four fixed maps satisfy the exact amplified involution clause.

**Type:** claim

**Inference:** deduction from validated prerequisites

**Status:** validated

**Taint:** clean

###### Node 1.5.1.1.1

**Statement:** Corrected validated endpoint bridge. No endpoint conclusion is inferred from the strict comparison written in node 1.3. Instead use validated child 1.5.1.1.1.2, whose explicit validated prerequisites are nodes 1.3.1.1, 1.3.2, and 1.4. Put T=h_11 composed with v. Node 1.3.1.1 supplies one fixed mu_11 with ||mu_11,n-T_n||<=kappa*e for every e>=0 and every n: it takes mu_11=T when e=0, while for e>0 its strict corrected estimate implies the non-strict bound. Node 1.3.2 supplies the same mu_11 as one spatial four-corner system mu_jk with fixed amplifications and exact adjoint compatibility. Node 1.4 supplies h_jk,n^{-1}=I_n tensor h_jk^{-1} and injectivity. Define gamma_11=v and gamma_jk=h_jk^{-1} composed with mu_jk off (1,1). Then h_jk,n gamma_jk,n=mu_jk,n off (1,1); d_11,n=h_11,n v_n-mu_11,n has norm at most kappa*e, and every other d_jk,n is zero. For each off-(1,1) corner, exact H-CB adjointness and spatial adjoint compatibility give h_kj,n(gamma_jk,n(X)^dagger)=h_kj,n gamma_kj,n(X^dagger), so injectivity yields gamma_jk,n(X)^dagger=gamma_kj,n(X^dagger). For (1,1), gamma_11,n=v_n preserves dagger exactly. Thus the comparison and exact amplified involution conclusions hold on the full e>=0 scope, without using the impossible strict estimate at e=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.1.1.1.1

**Statement:** Formal validation gate. Require validated nodes 1.3 and 1.4. Validated 1.3 includes the full endpoint split: if e=0 then delta=epsilon=0, the defects of T vanish, and mu_11=T gives ||mu_11,n-h_11,n v_n||=0=kappa*e; if e>0 the validated correction step gives a strict bound and therefore the required non-strict bound. Validated 1.4 gives h_jk,n^{-1}=I_n tensor h_jk^{-1} and injectivity. Hence h_jk,n gamma_jk,n=mu_jk,n off (1,1), d_11,n=h_11,n v_n-mu_11,n has norm at most kappa*e, and all other d_jk,n vanish. Exact H-CB adjointness, spatial adjoint compatibility, and injectivity then yield gamma_jk,n(X)^dagger=gamma_kj,n(X^dagger) off (1,1), including (2,2); for (1,1), gamma_11,n=v_n preserves dagger exactly. This establishes the comparison and involution conclusions on every e>=0 without any strict inequality at the zero endpoint.

**Type:** claim

**Inference:** deduction from validated prerequisites

**Status:** validated

**Taint:** clean

###### Node 1.5.1.1.1.2

**Statement:** Corrected endpoint dependency gate. This step does not use the strict comparison written in node 1.3. Require validated nodes 1.3.1.1, 1.3.2, and 1.4. Put T=h_11 composed with v. Validated node 1.3.1.1 supplies one level-one unital dagger-homomorphism mu_11 and its fixed amplifications with ||mu_11,n-T_n||<=kappa*e for the full e>=0 scope: at e=0 it explicitly takes mu_11=T and obtains norm 0=kappa*e, while at e>0 the validated correction gives a strict bound and hence this non-strict bound. Validated node 1.3.2 spatializes that same mu_11 by one unitary U_1 and supplies the four fixed maps mu_jk with mu_jk,n=I_n tensor mu_jk, exact spatial multiplication, and mu_jk,n(X)^dagger=mu_kj,n(X^dagger). Validated node 1.4 supplies h_jk,n^{-1}=I_n tensor h_jk^{-1} and injectivity of every h_jk,n. Define gamma_11=v and gamma_jk=h_jk^{-1} composed with mu_jk off (1,1). Then h_jk,n gamma_jk,n=mu_jk,n off (1,1), while d_11,n=h_11,n v_n-mu_11,n has ||d_11,n(X)||<=kappa*e||X||; thus all other d_jk,n vanish. For every corner off (1,1), including (2,2), exact H-CB adjointness and the spatial adjoint identity give h_kj,n(gamma_jk,n(X)^dagger)=h_jk,n(gamma_jk,n(X))^dagger=mu_jk,n(X)^dagger=mu_kj,n(X^dagger)=h_kj,n gamma_kj,n(X^dagger), so injectivity of h_kj,n yields gamma_jk,n(X)^dagger=gamma_kj,n(X^dagger). For (1,1), gamma_11,n=v_n preserves dagger exactly by def-extended-delta-inclusion. Therefore the comparison and exact amplified involution conclusions hold for every e>=0, and no endpoint conclusion is attributed to node 1.3.

**Type:** claim

**Inference:** deduction from explicitly validated endpoint and spatial prerequisites

**Status:** validated

**Taint:** clean

###### Node 1.5.1.1.1.3

**Statement:** Dependency-adoption gate addressing ch-598304ea60cdaa3e. The amended parent expressly discards the false reading of node 1.3 and derives its conclusion from already validated child 1.5.1.1.1.2. That child has validation_deps [1.3.1.1,1.3.2,1.4], explicitly handles e=0 by mu_11=T and 0=kappa*e, uses the positive-e correction only for e>0, spatializes that same mu_11, and obtains all Ha inverses and injectivity from node 1.4. Therefore the amended parent now adopts the corrected dependency chain and makes no inference from node 1.3 strict comparison.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Product estimate with every error term displayed. First ||gamma_jk,n(X)||<=||h_jk,n^{-1}||*||mu_jk,n(X)+d_jk,n(X)||<=2||X|| when C_H*e and kappa*e are at most 1/4. Put D=gamma_jl,n(XY)-gamma_jk,n(X) dot gamma_kl,n(Y). The conj-hcb product defect bounds the difference between h_jl,n of the second term and (h_jk,n gamma_jk,n(X))(h_kl,n gamma_kl,n(Y)) by 4C_H*e||X||||Y||. Substituting h gamma=mu+d, using mu_jl(XY)=mu_jk(X)mu_kl(Y), and ||d_ab,n(Z)||<=kappa*e||Z|| gives ||h_jl,n(D)|| <= [kappa+2kappa+kappa^2*e+4C_H]e||X||||Y|| <=4(C_H+kappa)e||X||||Y||. Node 1.4 gives ||h_jl,n^{-1}||<=1+C_H*e<=5/4, hence ||D||<=5(C_H+kappa)e||X||||Y||, uniformly in every index and amplification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.2.1

**Statement:** Prerequisites, with validation dependency made explicit. Require nodes 1.3 and 1.4 to be validated. Node 1.3 supplies one fixed spatial system mu_jk,n=I_n tensor mu_jk and the uniform comparison ||h_11,n v_n-mu_11,n||<=kappa e, including its separate e=0 branch. Node 1.4 supplies, for every j,k,n, bijectivity of h_jk,n, h_jk,n^{-1}=I_n tensor h_jk^{-1}, and ||h_jk,n^{-1}||<=1+C_H e. For the four maps already defined in node 1.5, gamma_11=v and gamma_jk=h_jk^{-1} mu_jk off (1,1), define d_jk,n=h_jk,n gamma_jk,n-mu_jk,n. Then d_11,n=h_11,n v_n-mu_11,n, so ||d_11,n(Z)||<=kappa e||Z||, while d_jk,n=0 off (1,1), because h_jk,n(I_n tensor h_jk^{-1})=I. Thus uniformly ||d_jk,n(Z)||<=kappa e||Z|| and every inverse used below exists with the stated bound; none of these facts is imported from an unvalidated sibling.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.2.1.1

**Statement:** Validation-gated derivation of the prerequisite package. This child has validation dependencies 1.3 and 1.4 and therefore supplies no conclusion while either node is pending. After both validate, node 1.3 supplies fixed level-one maps mu_jk with mu_jk,n=I_n tensor mu_jk and ||(h_11,n v_n-mu_11,n)(X)||<=kappa e||X|| for every n and X, on the full e>=0 scope. Node 1.4 supplies bijective h_jk,n, the identity h_jk,n^{-1}=I_n tensor h_jk^{-1}, and ||h_jk,n^{-1}||<=1+C_H e. Define gamma_11=v and, off (1,1), gamma_jk=h_jk^{-1} composed with mu_jk. Then gamma_jk,n=(I_n tensor h_jk^{-1}) composed with mu_jk,n off (1,1), so h_jk,n gamma_jk,n=(I_n tensor h_jk)(I_n tensor h_jk^{-1})mu_jk,n=mu_jk,n. Therefore d_jk,n:=h_jk,n gamma_jk,n-mu_jk,n is zero off (1,1), whereas d_11,n=h_11,n v_n-mu_11,n and hence ||d_11,n(X)||<=kappa e||X||. Consequently ||d_jk,n(X)||<=kappa e||X|| for every corner and amplification, and every inverse used in node 1.5.2 exists with the stated uniform bound. The conclusion is deliberately unavailable until validation of 1.3, so no pending correction result is used.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.5.2.2

**Statement:** Conditional norm calculation from the now-declared prerequisites. Fix compatible indices j,k,l, an amplification n, X in M_n tensor B(K_k,K_j), and Y in M_n tensor B(K_l,K_k). Shrink the universal threshold so C_H e<=1/4 and kappa e<=1/4. By node 1.5.2.1, h_jk,n gamma_jk,n(X)=mu_jk,n(X)+d_jk,n(X), ||h_jk,n^{-1}||<=1+C_H e, and ||d_jk,n(X)||<=kappa e||X||. Since every mu_jk,n is isometric, ||gamma_jk,n(X)||<= (1+C_H e)(1+kappa e)||X||<=25/16||X||<=2||X||, and similarly for Y. Put D=gamma_jl,n(XY)-gamma_jk,n(X) dot gamma_kl,n(Y). The product-defect clause of conj-hcb gives E=h_jl,n(gamma_jk,n(X) dot gamma_kl,n(Y))-(h_jk,n gamma_jk,n(X))(h_kl,n gamma_kl,n(Y)) with ||E||<=C_H e||gamma_jk,n(X)|| ||gamma_kl,n(Y)||<=4C_H e||X||||Y||. Hence, using exact spatial multiplication mu_jl,n(XY)=mu_jk,n(X)mu_kl,n(Y), h_jl,n(D)=d_jl,n(XY)-mu_jk,n(X)d_kl,n(Y)-d_jk,n(X)mu_kl,n(Y)-d_jk,n(X)d_kl,n(Y)-E. Submultiplicativity ||XY||<=||X||||Y||, isometry of mu, and the d-bounds yield ||h_jl,n(D)||<=[3kappa+kappa^2 e+4C_H]e||X||||Y||. Because kappa e<=1, kappa^2 e<=kappa, so this is <=4(C_H+kappa)e||X||||Y||. Finally node 1.5.2.1 gives ||D||<=||h_jl,n^{-1}||||h_jl,n(D)||<=(5/4)4(C_H+kappa)e||X||||Y||=5(C_H+kappa)e||X||||Y||. Every constant and threshold is independent of j,k,l,n,r and dim A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.1

**Statement:** Dependency-gated product calculation (addressing ch-e5329953fda228a2). This child has validation dependency 1.5.2.1 and therefore yields no product estimate while 1.5.2.1 is pending. Once 1.5.2.1 is validated, it supplies, for every compatible j,k,l,n, the fixed spatial isometries mu_ab,n, bijectivity with ||h_ab,n^{-1}||<=1+C_H e, and d_ab,n:=h_ab,n gamma_ab,n-mu_ab,n satisfying ||d_ab,n(Z)||<=kappa e||Z||. Under C_H e<=1/4 and kappa e<=1/4, ||gamma_jk,n(X)||<=||h_jk,n^{-1}||( ||mu_jk,n(X)||+||d_jk,n(X)|| )<=(25/16)||X||<=2||X||, and similarly ||gamma_kl,n(Y)||<=(25/16)||Y||<=2||Y||. Define D=gamma_jl,n(XY)-gamma_jk,n(X) dot gamma_kl,n(Y), and let E be the H-CB product defect, so ||E||<=4C_H e||X||||Y||. Linearity of h_jl,n, the identities h_ab,n gamma_ab,n=mu_ab,n+d_ab,n and mu_jl,n(XY)=mu_jk,n(X)mu_kl,n(Y) give exactly h_jl,n(D)=d_jl,n(XY)-mu_jk,n(X)d_kl,n(Y)-d_jk,n(X)mu_kl,n(Y)-d_jk,n(X)d_kl,n(Y)-E. Exact operator submultiplicativity in the matrix source, complete isometry of mu, and the d-bounds imply ||h_jl,n(D)||<=[3kappa+kappa^2 e+4C_H]e||X||||Y||<=4(C_H+kappa)e||X||||Y||, since kappa e<=1. Applying the supplied inverse bound and C_H e<=1/4 gives ||D||<=5(C_H+kappa)e||X||||Y||. Hence the mathematics is valid after, and only after, validation of 1.5.2.1; the dependency is not replaced by any external input.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.1.1

**Statement:** Ledger-enforced prerequisite bridge. This child has validation dependency 1.5.2.1, so it cannot be accepted before 1.5.2.1 is validated. After that validation, node 1.5.2.1 supplies the fixed spatial complete isometries mu_ab,n, the inverse bounds ||h_ab,n^{-1}||<=1+C_H e, and ||d_ab,n(Z)||<=kappa e||Z|| for d_ab,n=h_ab,n gamma_ab,n-mu_ab,n. If C_H e<=1/4 and kappa e<=1/4, then ||gamma_ab,n(Z)||<2||Z||. For D=gamma_jl,n(XY)-gamma_jk,n(X) dot gamma_kl,n(Y), the H-CB product defect E and exact spatial multiplication give h_jl,n(D)=d_jl,n(XY)-mu_jk,n(X)d_kl,n(Y)-d_jk,n(X)mu_kl,n(Y)-d_jk,n(X)d_kl,n(Y)-E. Hence ||h_jl,n(D)||<=[3kappa+kappa^2 e+4C_H]e||X||||Y||<=4(C_H+kappa)e||X||||Y||, and applying ||h_jl,n^{-1}||<=5/4 yields ||D||<=5(C_H+kappa)e||X||||Y||. Thus the parent calculation follows, but only after the ledger-enforced prerequisite validates.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.5.2.2.1.2

**Statement:** Actual validation gate. This child may be accepted only after node 1.5.2.1 is validated. Once that happens, 1.5.2.1 provides the fixed spatial complete isometries mu_ab,n, the bounds ||h_ab,n^{-1}||<=1+C_H e, and ||d_ab,n(Z)||<=kappa e||Z||. Under C_H e<=1/4 and kappa e<=1/4, the corrected calculation is ||gamma_ab,n(Z)||<=(25/16)||Z||<=2||Z|| for every Z; the H-CB defect identity gives ||h_jl,n(D)||<=[3kappa+kappa^2 e+4C_H]e||X||||Y||<=4(C_H+kappa)e||X||||Y||; and ||h_jl,n^{-1}||<=5/4 gives ||D||<=5(C_H+kappa)e||X||||Y||. No spatial map, inverse estimate, d-bound, or product conclusion is asserted before that prerequisite validates.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.1.2.1

**Statement:** For every Z, dependency 1.5.2.1 gives gamma_ab,n(Z)=h_ab,n^{-1}(mu_ab,n(Z)+d_ab,n(Z)), with ||h_ab,n^{-1}||<=1+C_H e<=5/4, ||mu_ab,n(Z)||=||Z|| by complete isometry, and ||d_ab,n(Z)||<=kappa e||Z||<=||Z||/4. Therefore ||gamma_ab,n(Z)||<=(5/4)(1+1/4)||Z||=(25/16)||Z||<=2||Z||. This non-strict estimate includes Z=0 and is the bound used in the H-CB defect estimate; the remaining displayed arithmetic is unchanged.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.5.2.2.1.2.2

**Statement:** For every Z, validated node 1.5.2.1 gives gamma_ab,n(Z)=h_ab,n^{-1}(mu_ab,n(Z)+d_ab,n(Z)), with ||h_ab,n^{-1}||<=1+C_H e<=5/4, ||mu_ab,n(Z)||=||Z|| by complete isometry, and ||d_ab,n(Z)||<=kappa e||Z||<=||Z||/4. Therefore ||gamma_ab,n(Z)||<=(5/4)(1+1/4)||Z||=(25/16)||Z||<=2||Z||. This non-strict estimate includes Z=0 and is exactly sufficient for the H-CB defect bound; all remaining arithmetic in the amended parent follows unchanged.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.5.2.2.1.3

**Statement:** Challenge-closing dependency gate. This proof step is ledger-blocked on validation of 1.5.2.1. Only after that validation do the spatial maps mu_ab,n, the inverse estimates ||h_ab,n^{-1}||<=1+C_H e, and the uniform d_ab,n bounds enter scope. With those premises, the parent identity and estimates give ||D||<=5(C_H+kappa)e||X||||Y|| exactly as displayed; before validation, this child yields no product estimate.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.5.3

**Statement:** Units, norms, bijectivity, and datum assembly. Let u_j be the compressed unit in S_{P_j}. The unit clauses of conj-hcb give ||h_jj,n(I_n tensor u_j)-I||<=C_H*e and ||u_j-P_j||<=C_H*e after enlarging C_H. Since h_jj,n gamma_jj,n(I)=I+d_jj,n(I), node 1.4 yields ||gamma_jj,n(I)-I_n tensor P_j||<=3(C_H+kappa)e. Also ||mu_jk,n(X)+d_jk,n(X)|| lies between (1-kappa*e)||X|| and (1+kappa*e)||X||. Combining this with the upper bound and inverse bound for h_jk,n gives (1-(C_H+kappa)e)||X||<=||gamma_jk,n(X)||<=(1+2(C_H+kappa)e)||X|| after universal threshold reduction. The map gamma_11=v is bijective; every other gamma_jk is a composition of the bijections mu_jk and h_jk^{-1}. Together with node 1.5.1, node 1.5.2, the delta-projection hypotheses, and ||P_1+P_2-I||<=delta<=D_0*e, these are exactly def-four-corner-merging-datum with common rho=D_0*e, D_0=5(C_H+kappa), for four fixed level-one maps at all amplifications.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.3.1

**Statement:** Dependency bridge for units, norms, bijectivity, and fixed amplifications, using only validated nodes 1.3.1, 1.3.2, and 1.4. For the same spatial map mu_11 fixed in nodes 1.3.1 and 1.3.2, node 1.3.1 gives ||h_11,n v_n(X)-mu_11,n(X)||<=kappa*e||X|| for every n and X. Define gamma_11=v and, for (j,k)!=(1,1), gamma_jk=h_jk^{-1} composed with mu_jk. Nodes 1.3.2 and 1.4 give mu_jk,n=I_n tensor mu_jk and h_jk,n^{-1}=I_n tensor h_jk^{-1}; hence every gamma_jk,n is the amplification of the same level-one gamma_jk, and h_jk,n gamma_jk,n=mu_jk,n off (1,1). Thus, writing d_jk,n=h_jk,n gamma_jk,n-mu_jk,n, one has d_jk,n=0 off (1,1) and ||d_11,n(X)||<=kappa*e||X||. For diagonal source identity I, spatiality gives mu_jj,n(I)=I. Consequently ||h_jj,n(gamma_jj,n(I)-I_n tensor u_j)||<=||d_jj,n(I)||+||I-h_jj,n(I_n tensor u_j)||<=(kappa+C_H)e. Applying ||h_jj,n^{-1}||<=1+C_H*e and adding ||I_n tensor(u_j-P_j)||<=C_H*e yields ||gamma_jj,n(I)-I_n tensor P_j||<=3(C_H+kappa)e after shrinking the universal threshold so C_H*e<=1. For arbitrary X, complete isometry of mu and the d-bound give (1-kappa*e)||X||<=||h_jk,n gamma_jk,n(X)||<=(1+kappa*e)||X||. The upper and inverse norm bounds for h from node 1.4 then give (1-(C_H+kappa)e)||X||<=||gamma_jk,n(X)||<=(1+2(C_H+kappa)e)||X|| after a universal threshold reduction. Finally gamma_11=v is bijective by the EXT-CB hypothesis, while every off-(1,1) gamma_jk is the composition of the bijections h_jk^{-1} and mu_jk. Therefore the comparison, unit and norm estimates, bijectivity, and fixed-amplification conclusions follow without node 1.5.1.

**Type:** claim

**Inference:** modus_ponens

**Status:** archived

**Taint:** clean

###### Node 1.5.3.1.1

**Statement:** Corrected availability statement (challenge ch-5031992bb44865d2). The missing comparison d_11,n=h_11,n v_n-mu_11,n with ||d_11,n(X)||<=kappa*e*||X||, supplied by node 1.5.1 and ultimately node 1.3, prevents use of the displayed d_11-based (1,1) unit/norm comparison in node 1.5.3.1 until those nodes are validated. It does not prevent bijectivity or fixed-amplification conclusions. Indeed gamma_11=v is bijective by the root hypothesis and gamma_11,n=I_n tensor v by definition of amplification. For (j,k)!=(1,1), node 1.3.2 gives a fixed bijection mu_jk with mu_jk,n=I_n tensor mu_jk, and node 1.4 gives a fixed bijection h_jk with h_jk,n^{-1}=I_n tensor h_jk^{-1}. Hence gamma_jk=h_jk^{-1} composed with mu_jk is bijective and gamma_jk,n=h_jk,n^{-1} composed with mu_jk,n=I_n tensor gamma_jk, independently of node 1.5.1 and d_11. After nodes 1.3 and 1.5.1 are validated, their d_11 comparison also licenses the conditional triangle-inequality calculation in node 1.5.3.1. No permitted external input supplies that missing comparison, and no independently established bijectivity or fixed-amplification conclusion is withheld because of it.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.3.1.1.1

**Statement:** Explicit bridge separating the available algebraic conclusions from the unavailable comparison estimate. For gamma_11=v, the EXT-CB root hypothesis makes gamma_11 bijective and amplification means gamma_11,n=I_n tensor gamma_11. For (j,k)!=(1,1), validated node 1.3.2 gives bijective mu_jk with mu_jk,n=I_n tensor mu_jk, while validated node 1.4 gives bijective h_jk and h_jk,n^{-1}=I_n tensor h_jk^{-1}. Therefore gamma_jk=h_jk^{-1} mu_jk is bijective and I_n tensor gamma_jk=(I_n tensor h_jk^{-1})(I_n tensor mu_jk)=h_jk,n^{-1} mu_jk,n=gamma_jk,n. None of these equalities uses d_11 or node 1.5.1. By contrast, the particular (1,1) comparison h_11,n gamma_11,n=mu_11,n+d_11,n with ||d_11,n||<=kappa*e is exactly the pending content of node 1.5.1 (ultimately node 1.3), so only arguments invoking that comparison must wait. This removes the former invalid inference that all four kinds of conclusion were blocked.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.3.1.2

**Statement:** Replacement validated-premise bridge addressing ch-050f3881bf97e920. Validated node 1.3.1 supplies the same level-one map mu_11 used in validated node 1.3.2 and, for every n and X, ||h_11,n v_n(X)-mu_11,n(X)||<=kappa*e||X||. Define gamma_11=v and, for (j,k)!=(1,1), gamma_jk=h_jk^{-1} composed with mu_jk. Validated node 1.4 gives h_jk,n^{-1}=I_n tensor h_jk^{-1}; hence gamma_jk,n=I_n tensor gamma_jk and h_jk,n gamma_jk,n=mu_jk,n off (1,1). Thus d_jk,n:=h_jk,n gamma_jk,n-mu_jk,n vanishes off (1,1), while d_11,n=h_11,n v_n-mu_11,n and ||d_11,n(X)||<=kappa*e||X||. This derives the formerly unavailable comparison without node 1.5.1. For diagonal source identity I, spatiality gives mu_jj,n(I)=I, so linearity and the H-CB unit estimate imply ||h_jj,n(gamma_jj,n(I)-I_n tensor u_j)||<=||d_jj,n(I)||+||I-h_jj,n(I_n tensor u_j)||<=(kappa+C_H)e. Applying ||h_jj,n^{-1}||<=1+C_H*e and adding ||I_n tensor(u_j-P_j)||<=C_H*e yields ||gamma_jj,n(I)-I_n tensor P_j||<=3(C_H+kappa)e once C_H*e<=1. For arbitrary X, complete isometry of mu and the d-bound give (1-kappa*e)||X||<=||h_jk,n gamma_jk,n(X)||<=(1+kappa*e)||X||. From ||h_jk,n||<=1+C_H*e and ||h_jk,n^{-1}||<=1+C_H*e, therefore ||gamma_jk,n(X)||>=(1-kappa*e)/(1+C_H*e)||X||>=(1-(C_H+kappa)e)||X|| and ||gamma_jk,n(X)||<=(1+C_H*e)(1+kappa*e)||X||<=(1+2(C_H+kappa)e)||X|| after shrinking so C_H*e<=1. Finally gamma_11=v is bijective by the EXT-CB hypothesis; off (1,1), gamma_jk is a composition of the validated bijections h_jk^{-1} and mu_jk. The displayed tensor identities prove all four are fixed level-one maps at every amplification. Hence all conclusions of node 1.5.3.1 follow from validated nodes 1.3.1, 1.3.2, and 1.4, independently of pending node 1.5.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.3.1.2.1

**Statement:** Ledger-licensed modus-ponens bridge. Require validated nodes 1.3.1, 1.3.2, and 1.4. Node 1.3.1 supplies, for the same spatial map mu_11 of node 1.3.2, ||h_11,n v_n(X)-mu_11,n(X)|| <= kappa*e||X|| for every n and X. Set gamma_11=v and gamma_jk=h_jk^{-1} composed with mu_jk off (1,1). By node 1.4, h_jk,n^{-1}=I_n tensor h_jk^{-1}; by node 1.3.2, mu_jk,n=I_n tensor mu_jk. Hence gamma_jk,n=I_n tensor gamma_jk and h_jk,n gamma_jk,n=mu_jk,n off (1,1). Therefore d_jk,n:=h_jk,n gamma_jk,n-mu_jk,n is zero off (1,1), while d_11,n=h_11,n v_n-mu_11,n and ||d_11,n(X)|| <= kappa*e||X||. For diagonal source identity I, spatiality gives mu_jj,n(I)=I; the triangle inequality, the H-CB unit estimate, and ||h_jj,n^{-1}|| <= 1+C_H*e give ||gamma_jj,n(I)-I_n tensor u_j|| <= (1+C_H*e)(C_H+kappa)e. Adding ||I_n tensor(u_j-P_j)|| <= C_H*e and shrinking the universal threshold so C_H*e <= 1 gives ||gamma_jj,n(I)-I_n tensor P_j|| <= 3(C_H+kappa)e. For arbitrary X, complete isometry of mu and the d-bound give (1-kappa*e)||X|| <= ||h_jk,n gamma_jk,n(X)|| <= (1+kappa*e)||X||. Using ||h_jk,n|| <= 1+C_H*e and ||h_jk,n^{-1}|| <= 1+C_H*e yields (1-(C_H+kappa)e)||X|| <= ||gamma_jk,n(X)|| <= (1+2(C_H+kappa)e)||X|| after the same universal threshold reduction. Finally gamma_11=v is bijective by the EXT-CB hypothesis, and off (1,1) gamma_jk is the composition of the bijections h_jk^{-1} and mu_jk. Thus the comparison, unit and norm estimates, bijectivity, and fixed-amplification conclusions follow solely from the three registered validated premises.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.5.3.1.3

**Statement:** Ledger-enforced replacement for the pending 1.5.1 dependency. Require validated nodes 1.3.1, 1.3.2, and 1.4. Node 1.3.1 gives ||h_11,n v_n(X)-mu_11,n(X)||<=kappa*e||X|| for every n and X for the same mu_11 spatialized in node 1.3.2. With gamma_11=v and gamma_jk=h_jk^{-1}mu_jk off (1,1), node 1.4 gives h_jk,n gamma_jk,n=mu_jk,n off (1,1); hence d_11,n=h_11,n v_n-mu_11,n and d_jk,n=0 otherwise. Therefore ||d_jk,n(X)||<=kappa*e||X|| without using node 1.5.1. The H-CB diagonal unit estimate, spatial identity mu_jj,n(I)=I, and ||h_jj,n^{-1}||<=1+C_H*e then give ||gamma_jj,n(I)-I_n tensor P_j||<=3(C_H+kappa)e when C_H*e<=1. Complete isometry of mu and the d-bound give (1-kappa*e)||X||<=||h_jk,n gamma_jk,n(X)||<=(1+kappa*e)||X||; the upper and inverse bounds for h yield (1-(C_H+kappa)e)||X||<=||gamma_jk,n(X)||<=(1+2(C_H+kappa)e)||X|| under the same universal threshold reduction. Bijectivity and fixed amplification follow because gamma_11=v and, off (1,1), gamma_jk=h_jk^{-1}mu_jk, with h_jk,n^{-1}=I_n tensor h_jk^{-1} and mu_jk,n=I_n tensor mu_jk. Thus every conclusion of node 1.5.3.1 is licensed by these three validated prerequisites, and pending node 1.5.1 is unnecessary for this bridge.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.5.3.2

**Statement:** Final datum assembly with explicit prerequisites. Require validated node 1.5.3.1 for bijectivity, fixed amplifications, diagonal-unit error, and two-sided norm control; validated node 1.5.1 for exact involution compatibility and the d-comparison; and validated node 1.5.2 for compressed-product defect at most 5(C_H+kappa)e. The target elements P_1=P and P_2=Q are delta-projections by the root hypotheses and ||P_1+P_2-I||<=delta<=e<=D_0*e, where D_0=5(C_H+kappa) after enlarging universal constants so D_0>=1. Thus, with rho=D_0*e, every clause of the amended def-four-corner-merging-datum holds for the four fixed level-one maps gamma_jk and all their amplifications. No conclusion of this child is available until all three declared dependencies are validated.

**Type:** claim

**Inference:** by_definition

**Status:** archived

**Taint:** clean

###### Node 1.5.3.2.1

**Statement:** Replacement assembly from validated descendants, so no pending premise is used. Require validated nodes 1.3.2, 1.4, 1.5.2.2.1.2, and 1.5.3.1.3. Node 1.5.3.1.3 supplies four bijective fixed level-one maps gamma_jk, their fixed amplifications gamma_jk,n=I_n tensor gamma_jk, diagonal-unit error at most 3(C_H+kappa)e, and two-sided bounds (1-(C_H+kappa)e)||X|| <= ||gamma_jk,n(X)|| <= (1+2(C_H+kappa)e)||X||. Node 1.5.2.2.1.2 supplies compressed-product defect at most 5(C_H+kappa)e. It remains only to establish the exact involution clause without pending node 1.5.1. For gamma_11=v, exact dagger preservation follows from def-extended-delta-inclusion. If (j,k)!=(1,1), exact H-CB adjointness, spatial adjoint compatibility from node 1.3.2, the identities h_jk,n gamma_jk,n=mu_jk,n and h_kj,n gamma_kj,n=mu_kj,n from node 1.5.3.1.3, and injectivity of h_kj,n from node 1.4 give h_kj,n(gamma_jk,n(X)^dagger)=h_jk,n(gamma_jk,n(X))^dagger=mu_jk,n(X)^dagger=mu_kj,n(X^dagger)=h_kj,n gamma_kj,n(X^dagger), hence gamma_jk,n(X)^dagger=gamma_kj,n(X^dagger). This includes the (2,2) corner. Let D_0=5(C_H+kappa), enlarging the universal constants if needed so D_0>=1, and rho=D_0 e. The canonical source block projections in M_{r+1}=B(K_1 direct-sum K_2) are exactly complementary. The targets P_1=P and P_2=Q are delta-projections by the root hypotheses, and ||P_1+P_2-I||<=delta<=e<=rho. Exact involution has defect 0<=rho; the product, unit, lower-norm, and upper-norm defects above are respectively bounded by D_0 e, 3(C_H+kappa)e, (C_H+kappa)e, and 2(C_H+kappa)e, all at most rho. Consequently every clause of the amended def-four-corner-merging-datum holds with the common defect rho for the same four level-one maps at every amplification. This is a complete replacement route and does not invoke pending nodes 1.5.3.1, 1.5.1, or 1.5.2.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.5.3.3

**Statement:** Replacement dependency bridge for units, norms, bijectivity, and fixed amplifications. Require validated nodes 1.3.1, 1.3.2, and 1.4. For the same spatial map mu_11 fixed in nodes 1.3.1 and 1.3.2, node 1.3.1 gives ||h_11,n v_n(X)-mu_11,n(X)||<=kappa*e||X|| for every n and X. Define gamma_11=v and, for (j,k)!=(1,1), gamma_jk=h_jk^{-1} composed with mu_jk. Nodes 1.3.2 and 1.4 give mu_jk,n=I_n tensor mu_jk and h_jk,n^{-1}=I_n tensor h_jk^{-1}, so all gamma_jk,n are fixed amplifications, h_jk,n gamma_jk,n=mu_jk,n off (1,1), and d_jk,n:=h_jk,n gamma_jk,n-mu_jk,n is zero off (1,1) while ||d_11,n(X)||<=kappa*e||X||. For diagonal identity I, mu_jj,n(I)=I, hence ||h_jj,n(gamma_jj,n(I)-I_n tensor u_j)||<=||d_jj,n(I)||+||I-h_jj,n(I_n tensor u_j)||<=(kappa+C_H)e. The inverse bound and ||u_j-P_j||<=C_H*e imply ||gamma_jj,n(I)-I_n tensor P_j||<=3(C_H+kappa)e once C_H*e<=1. For arbitrary X, complete isometry of mu gives (1-kappa*e)||X||<=||h_jk,n gamma_jk,n(X)||<=(1+kappa*e)||X||. The upper and inverse bounds for h then imply (1-(C_H+kappa)e)||X||<=||gamma_jk,n(X)||<=(1+2(C_H+kappa)e)||X|| after a universal threshold reduction. Finally gamma_11=v is bijective by the EXT-CB hypothesis, and every off-(1,1) gamma_jk is the composition of bijections h_jk^{-1} and mu_jk. Thus all bridge conclusions follow without node 1.5.1.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.5.3.4

**Statement:** Active adoption of the validated replacement assembly. Validated node 1.5.3.2.1 proves, without invoking pending nodes 1.5.3.1, 1.5.1, or 1.5.2, that the same four bijective fixed level-one maps gamma_jk and their amplifications satisfy every clause of the amended def-four-corner-merging-datum with common defect rho=D_0 e, where D_0=5(C_H+kappa) is universal and enlarged so D_0>=1. Therefore the final datum-assembly conclusion required in node 1.5.3 follows directly from 1.5.3.2.1; this sibling is the active route and the stale node 1.5.3.2 is retired.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Merge and conclude the root. Choose e_ext as the positive minimum of the thresholds in nodes 1.1--1.5, a_merge/(D_0+1), and the finitely many Neumann and 1/4 bounds; it is universal. Node 1.5 supplies four fixed bijective level-one corner maps satisfying def-four-corner-merging-datum with rho=D_0*e and rho+epsilon<=(D_0+1)e<=a_merge. Apply lem-extcb-four-corner-merge (whose assembled norm component is lem-extcb-four-corner-norm) to obtain the single sum map v_+:M_{r+1}->A. It is an extended C_merge*(rho+epsilon)-isomorphism, hence an extended C_ext*e-isomorphism for C_ext=C_merge*(D_0+1). Its n-th map is I_n tensor v_+, assembled from I_n tensor U_1, I_n tensor U_2 and the same four gamma_jk. All constants used are universal and therefore independent of r,n,dim A and block data. This is exactly node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

