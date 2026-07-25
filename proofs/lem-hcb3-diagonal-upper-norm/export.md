# Proof Export

## Node 1

**Statement:** Uniform diagonal Ha upper norm: there are universal C_up < infinity and e_up > 0 such that every H-CB datum with e <= e_up, every n >= 1, and every Z in M_n tensor S_P satisfy ||(Ha^Q_{P,P})_n(Z)|| <= (1+C_up*e)||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** There are universal kappa >= 0 and e_sq > 0 such that, for every H-CB datum with e <= e_sq, every n >= 1, and every Z in M_n tensor S_P, one has ||Z^dagger dot Z|| <= (1+kappa*e)||Z||^2; specifically, one may take kappa=C_ca and e_sq=e_ca from lem-compcb-corner-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** If S_P=0, then M_n tensor S_P=0 for every n, so Z=0 and the asserted square estimate is immediate for any kappa and threshold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** If S_P is nonzero, the registered compressed-corner facts imply that P is nonvanishing and give the level-one estimate ||Z^dagger dot Z|| <= (1+kappa_1*e)||Z||^2 for universal kappa_1 and all Z in S_P, after restricting e below a universal threshold. They do not imply the corresponding estimate on M_n tensor S_P uniformly in n: that conclusion requires an additional amplified-corner result, which is not among this shard's allowed dependencies. Consequently this node cannot support parent 1.1 as presently dependency-scoped.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** The level-one part follows by unpacking compressed-product-display: S_P nonzero is the nonvanishing alternative, and S_P is then an O(e)-C*-algebra; its epsilon-Banach product upper axiom applied to Z^dagger and Z, together with ||Z^dagger||=||Z||, gives ||Z^dagger dot Z|| <= (1+kappa_1*e)||Z||^2 with universal witnesses after a universal threshold restriction.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** The matrix-uniform extension is not a consequence of def-hcb-datum: that definition expressly packages data and notation only and supplies no estimates. Nor does compressed-product-display assert that all M_n tensor S_P are O(e)-C*-algebras. Thus an amplified-corner theorem (for example an allowed dependency asserting that S_P is an extended O(e)-C*-algebra) is logically necessary before parent 1.1 can be concluded.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Unpacking O(e) in the amplified C*-norm upper estimate yields universal finite kappa >= 0 and e_sq > 0, independent of the datum and n, such that ||Z^dagger dot Z|| <= (1+kappa*e)||Z||^2 whenever e <= e_sq. Together with the zero-space case this proves node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Dependency audit: compressed-product-display says only that the level-one nonvanishing corner S_P is an O(e)-C*-algebra; epsilon-banach-cstar-norm-axioms supplies the associated level-one product bound; def-hcb-datum expressly supplies data and notation but no estimates; lem-hcb2-amplified-adjointness controls the adjoint of the amplified Ha map; and lem-hcb2-product-defect controls the amplified multiplicative defect of Ha. None bounds ||Z^dagger dot Z|| by (1+O(e))||Z||^2 on M_n tensor S_P uniformly in n. Thus passing from the valid n=1 estimate to arbitrary n is not an inference from any allowed premise.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.5

**Statement:** The amplified-corner theorem previously identified as missing is now available as the allowed validated dependency lem-compcb-corner-algebra. Consequently the negative audits in nodes 1.1, 1.1.2, and 1.1.4 are obsolete: there are universal kappa=C_ca and e_sq=e_ca such that every H-CB datum with e<=e_sq, every n>=1, and every Z in M_n tensor S_P satisfy ||Z^dagger dot Z||<=(1+kappa*e)||Z||^2. Thus node 1.1.3's amplified C*-norm upper estimate is justified in the current dependency scope, and the proof may proceed through nodes 1.2 and 1.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.5.1

**Statement:** Assume S_P is nonzero and e<=e_ca. By the registered delta-projection dichotomy used in node 1.1.2, P is nonvanishing. The allowed validated dependency lem-compcb-corner-algebra therefore applies and makes S_P, with its compressed product and inherited involution, an extended alpha-C*-algebra for alpha=C_ca*e. By the registered definition of extended, for every n>=1 the amplification M_n tensor S_P is an alpha-C*-algebra with the same alpha, independent of n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.5.2

**Statement:** For Z in M_n tensor S_P, the product upper axiom in that alpha-C*-algebra and the isometry of the inherited involution give ||Z^dagger dot Z||<=(1+alpha)||Z^dagger||||Z||=(1+C_ca*e)||Z||^2. If S_P=0, node 1.1.1 gives Z=0 and the same inequality trivially. Hence kappa:=C_ca and e_sq:=e_ca are universal witnesses for every H-CB datum and every n, which is precisely the amplified estimate invoked by node 1.1.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.6

**Statement:** The validated node 1.1.5, via its validated steps 1.1.5.1--1.1.5.2, proves the amended statement with kappa=C_ca and e_sq=e_ca: if S_P is nonzero, P is nonvanishing and lem-compcb-corner-algebra makes every M_n tensor S_P a C_ca*e-C*-algebra uniformly in n, so the product upper axiom and involution isometry give ||Z^dagger dot Z|| <= (1+C_ca*e)||Z||^2; if S_P=0, then Z=0 by node 1.1.1. These two exhaustive cases establish the claimed universal amplified square estimate.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Let C_prod and e_prod be supplied by lem-hcb2-product-defect and e_adj by lem-hcb2-amplified-adjointness. For any fixed datum with e <= min(e_sq,e_prod,e_adj) and fixed n, the operator norm b_n:=||(Ha^Q_{P,P})_n|| satisfies b_n^2 <= (1+kappa*e)b_n+C_prod*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Fix a datum, n, and write h_n=(Ha^Q_{P,P})_n and b_n=||h_n||. The Ha-map is linear between the finite-dimensional amplified corner and an operator algebra, hence b_n is finite. For T=h_n(Z), the operator C*-identity gives ||T||^2=||T^dagger T||, and lem-hcb2-amplified-adjointness gives T^dagger=h_n(Z^dagger).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** Correction of the false finite-dimensional sentence: write h=(Ha^Q_{P,P})_1 and let q be the Hilbert norm from the Ha definition on S_{P,Q}. Unpacking the registered O(e) statements in def-ha-map, compressed-product-display, epsilon-banach-cstar-norm-axioms, nonvanishing-delta-projection, and one-dimensional-projection-nonvanishing, there are universal e_0>0, K_dot<infinity, c_q>0, and c_u>0 such that for e<=e_0: ||A dot B||<=K_dot||A||||B|| for every compatible level-one product, c_q^{-1}||X||<=q(X)<=c_q||X|| on S_{P,Q}, and ||u_Q||>=c_u. (Q is nonvanishing because it is one-dimensional.) We may replace e_sq by min(e_sq,e_0), without weakening node 1.1 or changing the form of the final universal threshold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.2

**Statement:** For Z in S_P and X,Y in S_{P,Q}, the defining Ha identity and the bounds of 1.2.1.1 give 2*abs(<Y,h(Z)X>)*||u_Q|| <= ||(Y^dagger dot Z) dot X||+||Y^dagger dot (Z dot X)|| <= 2*K_dot^2*||Y||||Z||||X||. Hence abs(<Y,h(Z)X>) <= K_1*q(Y)*||Z||*q(X), where K_1=K_dot^2*c_q^2/c_u. Hilbert-space duality in the q norm yields q(h(Z)X)<=K_1||Z||q(X), so ||h(Z)||<=K_1||Z||. The same defining identity is linear in Z and uniqueness against all Y gives linearity of h.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.3

**Statement:** For fixed finite n, h_n is the matrix amplification: for Z=[Z_ij], h_n(Z)=[h(Z_ij)] on the Hilbert direct sum (S_{P,Q},q)^n. Thus ||h_n(Z)|| <= (sum_{i,j}||h(Z_ij)||^2)^(1/2) <= K_1*(sum_{i,j}||Z_ij||^2)^(1/2) <= n*K_1*||Z||; the last inequality uses contractivity of matrix-coordinate compressions in the registered operator-space structure, so ||Z_ij||<=||Z||. Therefore h_n is a bounded linear map and b_n=||h_n||<=n*K_1<infinity even when S_P is infinite-dimensional. Finally, for T=h_n(Z), the operator C*-identity gives ||T||^2=||T^dagger*T||, and lem-hcb2-amplified-adjointness gives T^dagger=h_n(Z^dagger). This proves exactly the usable conclusion of node 1.2.1 without its erroneous finite-dimensional premise.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Applying lem-hcb2-product-defect with all three corner indices equal to P, first input Z^dagger, and second input Z gives ||h_n(Z^dagger)h_n(Z)-h_n(Z^dagger dot Z)|| <= C_prod*e*||Z^dagger||||Z||=C_prod*e*||Z||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Take kappa:=C_ca and e_sq:=e_ca as supplied by the allowed validated lem-compcb-corner-algebra dependency through node 1.1. For every e<=min(e_sq,e_prod,e_adj), every n>=1, and every Z in E_n:=M_n tensor S_P, nodes 1.2.3.1 and 1.2.2 together with node 1.1 give ||h_n(Z)||^2<=b_n||Z^dagger dot Z||+C_prod*e||Z||^2<=((1+kappa*e)b_n+C_prod*e)||Z||^2. If E_n={0}, then b_n=0. Otherwise E_n has a nonempty unit sphere, and taking the supremum there (using finite b_n from node 1.2.3.1) yields b_n^2<=(1+kappa*e)b_n+C_prod*e. Thus this scalar quadratic holds uniformly for every n, including the zero-corner case.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** The needed finiteness does not use finite-dimensionality of S_P. Nodes 1.2.1.1--1.2.1.3 derive directly from the registered Ha identity and level-one norm axioms a universal bound ||h(Z)||<=K_1||Z||, and then, for fixed finite n and Z=[Z_ij], identify h_n(Z)=[h(Z_ij)] on the Hilbert direct sum. Thus ||h_n(Z)||<=K_1(sum_{i,j}||Z_ij||^2)^(1/2)<=n*K_1||Z||. Consequently h_n is a bounded linear map and its operator norm b_n is a finite real number. This uses only finiteness of the matrix size n, not finite-dimensionality of the corner.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** Now b_n<infinity implies ||h_n(W)||<=b_n||W|| for every W. For arbitrary Z, the operator C*-identity and amplified adjointness from 1.2.1.3, followed by 1.2.2, give ||h_n(Z)||^2=||h_n(Z^dagger)h_n(Z)||<=||h_n(Z^dagger dot Z)||+C_prod*e||Z||^2. Applying boundedness of h_n and node 1.1 gives ||h_n(Z)||^2<=b_n||Z^dagger dot Z||+C_prod*e||Z||^2<=((1+kappa*e)b_n+C_prod*e)||Z||^2. On ||Z||=1 the right side is independent of Z; because b_n is finite and norms are nonnegative, sup_{||Z||=1}||h_n(Z)||^2=(sup_{||Z||=1}||h_n(Z)||)^2=b_n^2. Taking the supremum proves the asserted scalar inequality.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.3

**Statement:** Complete the supremum argument by splitting on the domain E_n:=M_n tensor S_P. If E_n={0}, then the bounded linear map h_n:E_n->B((S_{P,Q})^n) is the zero map, hence b_n=||h_n||=0, and b_n^2 <= (1+kappa*e)b_n+C_prod*e holds because C_prod*e>=0. If E_n is nonzero, its unit sphere is nonempty (normalize any nonzero vector), and the definition of the operator norm of the bounded linear map h_n gives b_n=sup_{||Z||=1}||h_n(Z)||. Since all values are nonnegative and b_n is finite by 1.2.3.1, sup_{||Z||=1}||h_n(Z)||^2=(sup_{||Z||=1}||h_n(Z)||)^2=b_n^2. Taking the supremum in the pointwise inequality of 1.2.3.2 therefore yields b_n^2 <= (1+kappa*e)b_n+C_prod*e. Thus the scalar inequality holds in both cases, including the allowed zero corner.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.3.3.1

**Statement:** Let E_n=M_n tensor S_P. By 1.2.3.1, h_n:E_n->B((S_{P,Q})^n) is bounded and b_n=||h_n|| is a finite nonnegative real number. If E_n={0}, then h_n is the zero map and b_n=0, so b_n^2 <= (1+kappa*e)b_n+C_prod*e because C_prod>=0 and e>=0. If E_n is nonzero, its unit sphere U is nonempty, and boundedness gives b_n=sup_{Z in U}||h_n(Z)||. The pointwise estimate in 1.2.3.2 gives ||h_n(Z)||^2 <= (1+kappa*e)b_n+C_prod*e for every Z in U. For the nonempty set of nonnegative reals {||h_n(Z)||:Z in U}, monotonicity and continuity of t->t^2 on [0,infinity), together with finiteness of b_n, give sup_{Z in U}||h_n(Z)||^2=(sup_{Z in U}||h_n(Z)||)^2=b_n^2. Taking suprema in the pointwise estimate proves b_n^2 <= (1+kappa*e)b_n+C_prod*e. Thus the scalar inequality holds in both cases.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.2.3.4

**Statement:** Take kappa:=C_ca and e_sq:=e_ca as supplied by the allowed validated corner-algebra dependency through nodes 1.1.5.1--1.1.5.2. For every e<=min(e_sq,e_prod,e_adj), every n, and every Z in E_n:=M_n tensor S_P, amplified adjointness, product defect, boundedness of h_n, and the amplified corner square estimate give ||h_n(Z)||^2<=b_n||Z^dagger dot Z||+C_prod*e||Z||^2<=((1+kappa*e)b_n+C_prod*e)||Z||^2. If E_n={0}, then b_n=0; otherwise taking the supremum over its nonempty unit sphere gives b_n^2<=(1+kappa*e)b_n+C_prod*e. Thus the scalar quadratic holds uniformly for every n, including the zero-corner case.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.3.4.1

**Statement:** The formerly missing amplified estimate is available in the current scope. If S_P is nonzero and e<=e_ca, validated node 1.1.5.1 applies lem-compcb-corner-algebra to make every E_n=M_n tensor S_P an alpha-C*-algebra with alpha=C_ca*e uniformly in n; validated node 1.1.5.2 then applies the product upper axiom and inherited involution isometry to obtain ||Z^dagger dot Z||<=(1+C_ca*e)||Z||^2. If S_P=0, then E_n=0 and the same inequality is trivial. Hence kappa=C_ca and e_sq=e_ca furnish the required estimate for all n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.3.4.2

**Statement:** Let e<=min(e_sq,e_prod,e_adj). By 1.2.3.1, h_n is bounded and b_n=||h_n|| is finite. For T=h_n(Z), the operator C*-identity and amplified adjointness give ||h_n(Z)||^2=||h_n(Z^dagger)h_n(Z)||; node 1.2.2 and the triangle inequality bound this by ||h_n(Z^dagger dot Z)||+C_prod*e||Z||^2, which boundedness and the preceding child bound by ((1+kappa*e)b_n+C_prod*e)||Z||^2. If E_n=0 then b_n=0 and the scalar inequality is immediate. If E_n is nonzero, its unit sphere is nonempty and b_n=sup_{||Z||=1}||h_n(Z)||; since b_n is finite, taking suprema and using sup ||h_n(Z)||^2=(sup ||h_n(Z)||)^2 yields b_n^2<=(1+kappa*e)b_n+C_prod*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For nonnegative b,e,kappa,C satisfying b^2 <= (1+kappa*e)b+C*e, one has b <= 1+(kappa+C)e. Hence e_up:=min(e_sq,e_prod,e_adj) and C_up:=kappa+C_prod are universal and prove the root contract for every n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Set a=1+kappa*e, x=1+(kappa+C)e, and f(t)=t^2-a*t-C*e. Direct expansion gives f(x)=C*(kappa+C)*e^2 >= 0, while f is strictly increasing on [x,infinity) because 2x-a=1+(kappa+2C)e>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** The assumed scalar inequality is f(b)<=0. If b>x, monotonicity on [x,infinity) would give f(b)>f(x)>=0, a contradiction. Thus b<=x=1+(kappa+C)e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Apply the scalar conclusion to b=b_n and C=C_prod from node 1.2. Since e_sq, e_prod, and e_adj are positive universal thresholds and kappa,C_prod are finite universal constants, e_up=min(e_sq,e_prod,e_adj)>0 and C_up=kappa+C_prod<infinity are universal. Therefore ||(Ha^Q_{P,P})_n(Z)|| <= (1+C_up*e)||Z|| for every datum with e<=e_up, every n, and every Z.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

