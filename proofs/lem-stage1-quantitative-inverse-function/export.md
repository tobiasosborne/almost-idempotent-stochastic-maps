# Proof Export

## Node 1

**Statement:** Quantitative inverse-function control: if V:X->Y is a Banach-space isomorphism and f:B_r(x_0)->Y is C^1 with ||V^(-1)Df(x)-I|| <= c < 1, then f is injective, (1-c)||x_1-x_2|| <= ||V^(-1)(f(x_1)-f(x_2))|| <= (1+c)||x_1-x_2||, and f(B_r(x_0)) contains f(x_0)+V(B_{(1-c)r}(0)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Secant control and injectivity: under the root hypotheses, for all x_1,x_2 in B_r(x_0), (1-c)||x_1-x_2|| <= ||V^(-1)(f(x_1)-f(x_2))|| <= (1+c)||x_1-x_2||; because 1-c>0, f is injective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Define F:B_r(x_0)->X by F(x)=V^(-1)(f(x)-f(x_0)). Then F is C^1, DF(x)=V^(-1)Df(x), F(x_0)=0, and the root hypothesis is exactly ||DF(x)-I_X||<=c throughout B_r(x_0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Secant-error lemma: if a C^1 map F on the open ball B_r(x_0) satisfies ||DF(x)-I_X||<=c throughout that ball, then for all x_1,x_2 in the ball, ||F(x_1)-F(x_2)-(x_1-x_2)||<=c||x_1-x_2||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Fix x_1,x_2 in B_r(x_0), put d=x_1-x_2 and gamma(t)=x_2+td. Convexity of the ball keeps gamma([0,1]) in the domain. For q(t)=F(gamma(t))-F(x_2)-td, the chain rule gives q'(t)=(DF(gamma(t))-I_X)d and hence ||q'(t)||<=c||d|| for every t in [0,1].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** Banach-valued Newton-Leibniz estimate: if q:[0,1]->X is C^1 and ||q'(t)||<=M, then q(1)-q(0) is the norm-limit of the derivative Riemann sums (equivalently the Bochner/Riemann integral of q'), so ||q(1)-q(0)||<=integral_0^1 ||q'(t)||dt<=M. Applying this with M=c||d|| and observing q(1)-q(0)=F(x_1)-F(x_2)-d proves the secant-error estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.1

**Statement:** For any C^1 curve q:[0,1]->X with ||q′(t)||<=M, the Banach-valued fundamental theorem of calculus gives q(1)-q(0)=integral_0^1 q′(t)dt: indeed, continuity of q′ makes its tagged Riemann sums converge in norm to that integral, while the corresponding sums of increments telescope to q(1)-q(0). The norm inequality for the Bochner/Riemann integral then gives ||q(1)-q(0)||<=integral_0^1||q′(t)||dt<=M. Now fix x_1,x_2 in B_r(x_0), put d=x_1-x_2, gamma(t)=x_2+td, and q(t)=F(gamma(t))-F(x_2)-td. Validated node 1.1.2.1 establishes that gamma([0,1]) lies in the domain and that q is C^1 with ||q′(t)||<=c||d||. Apply the preceding estimate with M=c||d||. Since gamma(1)=x_1 and gamma(0)=x_2, q(1)=F(x_1)-F(x_2)-d and q(0)=0, hence ||F(x_1)-F(x_2)-(x_1-x_2)||=||q(1)-q(0)||<=c||d||=c||x_1-x_2||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Norm deduction: for vectors a,d in a normed space, ||a-d||<=c||d|| implies (1-c)||d||<=||a||<=(1+c)||d|| by the reverse and ordinary triangle inequalities; when c<1, a=0 forces d=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Quantitative image inclusion: under the root hypotheses, every y in f(x_0)+V(B_{(1-c)r}(0)) equals f(x) for some x in B_r(x_0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let g:B_r(0)->X be g(h)=V^(-1)(f(x_0+h)-f(x_0)). Then g(0)=0 and ||Dg(h)-I_X||<=c. Applying the segment argument of the secant-error lemma gives ||(g(h)-g(k))-(h-k)||<=c||h-k|| for every h,k in B_r(0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Centered covering with the correct specialization: any map g:B_r(0)->X with g(0)=0 and ||(g(h)-g(k))-(h-k)||<=c||h-k|| for 0<=c<1 satisfies B_{(1-c)r}(0) subset g(B_r(0)). For the image-inclusion application, g is specifically the map defined in node 1.2.1, g(h)=V^(-1)(f(x_0+h)-f(x_0)); for this g, if y=f(x_0)+Vz and g(h)=z, then y=f(x_0+h).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Fix z with ||z||<(1-c)r. Choose rho with 0<rho<r and ||z||<(1-c)rho, let K={h in X:||h||<=rho}, and define T(h)=z+h-g(h). For h,k in K the secant-error hypothesis gives ||T(h)-T(k)||<=c||h-k||. Taking k=0 and g(0)=0 gives ||h-g(h)||<=c||h||, hence ||T(h)||<=||z||+c rho<rho; thus T maps the complete closed ball K into itself and is a contraction.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Fixed-point construction and translation: let (M,d) be a complete metric space and let T:M->M be c-Lipschitz with 0<=c<1. For h_{n+1}=T(h_n), induction gives d(h_{n+1},h_n)<=c^n d(h_1,h_0). Thus, for m>n, the triangle inequality gives d(h_m,h_n)<=sum_{j=n}^{m-1} c^j d(h_1,h_0)<=c^n d(h_1,h_0)/(1-c), so (h_n) is Cauchy and completeness gives h_n->h in M. Moreover d(T(h),h)<=d(T(h),T(h_n))+d(h_{n+1},h)<=c d(h,h_n)+d(h_{n+1},h)->0, hence T(h)=h. Apply this to the contraction T on the complete closed ball K from 1.2.2.1, with its norm-induced metric. Then h lies in K subset B_r(0), and T(h)=h means z+h-g(h)=h, equivalently g(h)=z. Therefore every z in B_{(1-c)r}(0) lies in g(B_r(0)); and if y=f(x_0)+Vz, then g(h)=z implies f(x_0+h)=f(x_0)+Vg(h)=y, with x_0+h in B_r(x_0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.3

**Statement:** Specialization and translation, explicitly using node 1.2.1: take g(h)=V^(-1)(f(x_0+h)-f(x_0)), rather than an arbitrary map satisfying only the secant bound. For any z in B_{(1-c)r}(0), the generic covering construction in nodes 1.2.2.1 and 1.2.2.2 supplies h in B_r(0) with g(h)=z. The defining identity for this particular g is Vg(h)=f(x_0+h)-f(x_0). Hence g(h)=z implies f(x_0+h)-f(x_0)=Vz, and therefore for y=f(x_0)+Vz one has y=f(x_0+h); also x_0+h lies in B_r(x_0). No such translation is asserted for an independently chosen admissible g.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

