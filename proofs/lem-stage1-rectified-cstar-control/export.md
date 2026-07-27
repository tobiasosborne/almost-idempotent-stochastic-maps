# Proof Export

## Node 1

**Statement:** Controlled exact-unit C*-rectification: there are universal C_rect >= 1 and e_rect in (0, 1/C_rect] such that every finite-dimensional epsilon_X-C*-algebra with 0 <= epsilon_X <= e_rect admits, on the same involutive normed space, a bilinear product bold-dot and J = J^dagger for which (calX, J, bold-dot, dagger) satisfies EVERY exact-unit epsilon_r-C*-algebra axiom of def-epsilon-cstar-algebra, including ||J|| = 1, where epsilon_r = C_rect*epsilon_X, and ||J - I_X|| <= C_rect*epsilon_X, ||x bold-dot y - xy|| <= C_rect*epsilon_X*||x||*||y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Norming-functional step: for the original self-adjoint approximate unit I_X with a=||I_X|| and epsilon_X<=1/100, there exists a complex-linear functional phi with phi(I_X)=1, ||phi||<=1/a, and phi(x^dagger)=conjugate(phi(x)) for all x.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Finite-dimensional norming extension: for every nonzero u in a finite-dimensional complex normed space there is complex-linear f with ||f||=1 and f(u)=||u||. Indeed on C u put f_0(lambda u)=lambda||u||; extend G_0=Re(f_0) as a real-linear functional dominated by the norm, one real dimension at a time, defining G(m+t v)=G(m)+t c with c chosen between sup_m(G(m)-||m-v||) and inf_m(||m+v||-G(m)); the domination of G makes the lower endpoint at most the upper endpoint by the triangle inequality. After finitely many extensions set f(x)=G(x)-iG(i x). Then f is complex-linear and extends f_0; if theta=arg(f(x)), |f(x)|=Re(e^{-i theta}f(x))=G(e^{-i theta}x)<=||x||, while equality holds at u, hence ||f||=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Star symmetrization: apply node 1.1.1 to u=I_X, where a=||I_X||>=1-epsilon_X>0, and let f^sharp(x)=conjugate(f(x^dagger)). The original dagger is a conjugate-linear isometry and I_X^dagger=I_X by def-epsilon-cstar-algebra, so f^sharp is complex-linear, ||f^sharp||=1, and f^sharp(I_X)=a. Thus g=(f+f^sharp)/2 has ||g||<=1, g(I_X)=a, and g(x^dagger)=conjugate(g(x)); phi=g/a proves node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Explicit rectification step: with phi from node 1.1, define d_L(y)=y-I_X y, d_R(x)=x-x I_X, h=I_X I_X-I_X, m_0(x,y)=xy+phi(x)d_L(y)+phi(y)d_R(x)+phi(x)phi(y)h, J=I_X/a, and x bold-dot y=a m_0(x,y); then bold-dot is bilinear, J=J^dagger is its exact two-sided unit with ||J||=1, and the involution is exactly anti-multiplicative for bold-dot.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Unit and normalization algebra: m_0 is bilinear. Since phi(I_X)=1, d_L(I_X)=d_R(I_X)=I_X-I_X I_X=-h, direct substitution gives m_0(I_X,y)=y and m_0(x,I_X)=x. Hence J=I_X/a is a two-sided unit for x bold-dot y=a m_0(x,y); also J^dagger=J and ||J||=1 because I_X^dagger=I_X and a=||I_X||>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Exact star algebra: d_L(y)^dagger=d_R(y^dagger), d_R(x)^dagger=d_L(x^dagger), h^dagger=h, and phi(x^dagger)=conjugate(phi(x)). Using the original exact identity (xy)^dagger=y^dagger x^dagger from def-epsilon-cstar-algebra term-by-term in the formula for m_0 yields m_0(x,y)^dagger=m_0(y^dagger,x^dagger); multiplication by the real scalar a gives (x bold-dot y)^dagger=y^dagger bold-dot x^dagger.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Dependency bridge and explicit adjoint expansion: depend on node 1.1, which supplies the same functional phi used in node 1.2 and proves phi(z^dagger)=conjugate(phi(z)) for every z. Since I_X^dagger=I_X and the original product obeys (uv)^dagger=v^dagger u^dagger, d_L(y)^dagger=(y-I_X y)^dagger=y^dagger-y^dagger I_X=d_R(y^dagger), d_R(x)^dagger=(x-x I_X)^dagger=x^dagger-I_X x^dagger=d_L(x^dagger), and h^dagger=(I_X I_X-I_X)^dagger=I_X I_X-I_X=h. Conjugate-linearity of dagger and the scalar identity from node 1.1 therefore give m_0(x,y)^dagger=y^dagger x^dagger+phi(x^dagger)d_R(y^dagger)+phi(y^dagger)d_L(x^dagger)+phi(x^dagger)phi(y^dagger)h=m_0(y^dagger,x^dagger), where the last equality only reorders complex scalar factors. Finally a=||I_X|| is positive real, so (x bold-dot y)^dagger=(a m_0(x,y))^dagger=a m_0(y^dagger,x^dagger)=y^dagger bold-dot x^dagger.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Rectification bounds before and after normalization: the approximate-unit axioms give ||d_L(y)||<=epsilon_X||y||, ||d_R(x)||<=epsilon_X||x||, and ||h||<=epsilon_X a; with ||phi||<=1/a this implies ||m_0(x,y)-xy||<=3 epsilon_X/a ||x||||y||. Since |a-1|<=epsilon_X and ||xy||<=(1+epsilon_X)||x||||y||, Delta=a m_0-m obeys ||Delta(x,y)||<=(3 epsilon_X+epsilon_X(1+epsilon_X))||x||||y||<=5 epsilon_X||x||||y|| for epsilon_X<=1/100. This completes node 1.2 including the product-closeness assertion used later.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Quantitative axiom-transfer step: if Delta(x,y)=x bold-dot y-xy, then ||Delta(x,y)||<=5 epsilon_X||x||||y||, and the product-norm, associator, C*-lower-bound, conjugate-linear isometric involution, and exact-unit axioms of def-epsilon-cstar-algebra all hold for bold-dot with parameter 100 epsilon_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** All nonassociative axioms transfer: by node 1.2.3 put rho=5 epsilon_X so ||Delta(x,y)||<=rho||x||||y||. Then ||x bold-dot y||<= (1+epsilon_X+rho)||x||||y||=(1+6 epsilon_X)||x||||y||<=(1+100 epsilon_X)||x||||y||. Also ||x^dagger bold-dot x||>=||x^dagger x||-rho||x||^2>=(1-6 epsilon_X)||x||^2>=(1-100 epsilon_X)||x||^2. The unchanged dagger remains a conjugate-linear isometric involution; node 1.2.2 gives its exact product-reversal law, and node 1.2.1 gives the self-adjoint norm-one exact unit. Thus every axiom except the associator estimate holds with epsilon_r=100 epsilon_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Direct exact product-reversal bridge, independent of pending node 1.2.2: use the validated star-symmetrized functional of node 1.1.2, so phi(z^dagger)=conjugate(phi(z)). From I_X^dagger=I_X and the original exact reversal law in def-epsilon-cstar-algebra, d_L(y)^dagger=(y-I_X y)^dagger=y^dagger-y^dagger I_X=d_R(y^dagger), d_R(x)^dagger=(x-x I_X)^dagger=x^dagger-I_X x^dagger=d_L(x^dagger), and h^dagger=(I_X I_X-I_X)^dagger=I_X I_X-I_X=h. Therefore, for m_0(x,y)=xy+phi(x)d_L(y)+phi(y)d_R(x)+phi(x)phi(y)h, conjugate-linearity of dagger gives m_0(x,y)^dagger=y^dagger x^dagger+phi(x^dagger)d_R(y^dagger)+phi(y^dagger)d_L(x^dagger)+phi(x^dagger)phi(y^dagger)h=m_0(y^dagger,x^dagger), where only commutativity of complex scalars is used in matching the last three terms. Since a=||I_X|| is a positive real number, (x bold-dot y)^dagger=(a m_0(x,y))^dagger=a m_0(y^dagger,x^dagger)=y^dagger bold-dot x^dagger. This proves the missing axiom directly without invoking node 1.2.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Validated dependency bridge for all remaining nonassociative axioms: import nodes 1.2.1 and 1.2.3. Node 1.2.1 supplies that bold-dot is bilinear and that J is a self-adjoint two-sided exact unit with ||J||=1. Node 1.2.3 supplies ||Delta(x,y)||<=5 epsilon_X||x||||y||. The original epsilon_X-C*-axioms give ||xy||<=(1+epsilon_X)||x||||y|| and ||x^dagger x||>=(1-epsilon_X)||x||^2, while dagger is unchanged, conjugate-linear, isometric, and involutive. Hence ||x bold-dot y||<=||xy||+||Delta(x,y)||<=(1+6 epsilon_X)||x||||y||<=(1+100 epsilon_X)||x||||y||, and ||x^dagger bold-dot x||>=||x^dagger x||-||Delta(x^dagger,x)||>=(1-6 epsilon_X)||x||^2>=(1-100 epsilon_X)||x||^2, using ||x^dagger||=||x||. Together with the exact product-reversal law proved in child 1.3.1.1, these are precisely every def-epsilon-cstar-algebra axiom other than the associator estimate at epsilon_r=100 epsilon_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.1.2.1

**Statement:** Dependency-complete nonassociative-axiom assembly: depend explicitly on validated nodes 1.2.1, 1.2.3, and 1.3.1.1. Node 1.2.1 gives bilinearity of bold-dot and a self-adjoint two-sided exact unit J with ||J||=1. Node 1.2.3 gives ||Delta(u,v)||<=5 epsilon_X||u||||v||. Therefore the original product-norm and C*-lower axioms imply ||x bold-dot y||<=||xy||+||Delta(x,y)||<=(1+6 epsilon_X)||x||||y||<=(1+100 epsilon_X)||x||||y|| and ||x^dagger bold-dot x||>=||x^dagger x||-||Delta(x^dagger,x)||>=(1-6 epsilon_X)||x||^2>=(1-100 epsilon_X)||x||^2, since ||x^dagger||=||x||. The unchanged dagger retains conjugate-linearity, isometry, and involutivity from the original epsilon_X-C*-algebra, while node 1.3.1.1 supplies the exact missing identity (x bold-dot y)^dagger=y^dagger bold-dot x^dagger. Thus, by the exhaustive axiom list in def-epsilon-cstar-algebra, bilinearity, product norm, conjugate-linear isometric involution, exact product reversal, the C*-lower bound, and the self-adjoint norm-one exact two-sided unit all hold at epsilon_r=100 epsilon_X; only the associator estimate remains outside this node.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Associator transfer: write m for the original product, m'=m+Delta for bold-dot, and rho=5 epsilon_X. Expanding A'=m'(m'(x,y),z)-m'(x,m'(y,z)) gives the original associator plus m(Delta(x,y),z)-m(x,Delta(y,z))+Delta(m'(x,y),z)-Delta(x,m'(y,z)). The original bounds and ||m'(u,v)||<=(1+6 epsilon_X)||u||||v|| therefore give ||A'||<=[epsilon_X+2(1+epsilon_X)rho+2(1+6 epsilon_X)rho]||x||||y||||z||=[21 epsilon_X+70 epsilon_X^2]||x||||y||||z||<=100 epsilon_X||x||||y||||z|| for epsilon_X<=1/100. Together with node 1.3.1 this proves node 1.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Constant-closing step: choose the universal constants C_rect=100 and e_rect=1/100; nodes 1.1-1.3 then give every asserted exact-unit epsilon_r-C*-algebra axiom with epsilon_r=C_rect epsilon_X and both required closeness bounds, so they establish node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Dependency-gated closure. This step depends on nodes 1.1, 1.2, and 1.3 and may be accepted only after all three are validated. Set C_rect=100 and e_rect=1/100. These are universal, C_rect>=1, and 0<e_rect=1/C_rect. For any 0<=epsilon_X<=e_rect, node 1.2 supplies on the same involutive normed space the bilinear product bold-dot and the self-adjoint exact unit J=I_X/a of norm one, together with ||x bold-dot y-xy||<=5 epsilon_X||x||||y||; node 1.3 supplies every remaining exact-unit epsilon_r-C*-algebra axiom for epsilon_r=100 epsilon_X. Moreover, since a=||I_X|| and the original approximate-unit axiom gives |a-1|<=epsilon_X, ||J-I_X||=||(1/a-1)I_X||=|1-a|<=epsilon_X<=100 epsilon_X. The product bound 5 epsilon_X||x||||y||<=100 epsilon_X||x||||y|| gives the other required closeness estimate. Hence all clauses of node 1 hold.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

