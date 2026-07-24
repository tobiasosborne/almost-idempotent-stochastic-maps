# Proof Export

## Node 1

**Statement:** Amplification naturality of the power-series functional calculus: let B be a unital Banach algebra, iota_n: B -> M_n(B) the unital amplification X -> 1_{M_n} tensor X (an isometric unital homomorphism), and f given on ||X - x_0 I|| < r by the power series f(X) = a_0 I + sum_{m>=1} a_m (X - x_0 I)^m; then for every X in B with ||X - x_0 I|| < r, f(iota_n(X)) is defined and f(iota_n(X)) = iota_n(f(X)); in particular, whenever ||(2P-I)^2 - I|| < 1, theta(iota_n(2P-I)) = iota_n(theta(2P-I)) with theta(X) = (I + sgn(X))/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Under the general hypotheses of node 1, for every X with ||X-x_0 I_B||<r, the defining series in M_n(B) converges and satisfies f(iota_n(X))=iota_n(f(X)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Unitality, multiplicativity, and isometry give iota_n(I_B)=I_M, iota_n(X)-x_0 I_M=iota_n(X-x_0 I_B), ||iota_n(X)-x_0 I_M||=||X-x_0 I_B||<r, and (iota_n(X)-x_0 I_M)^m=iota_n((X-x_0 I_B)^m) for every integer m>=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For every N, if S_N=a_0 I_B+sum_{m=1}^N a_m(X-x_0 I_B)^m and T_N=a_0 I_M+sum_{m=1}^N a_m(iota_n(X)-x_0 I_M)^m, linearity, unitality, and multiplicativity of iota_n give T_N=iota_n(S_N).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** If S_N converges in B to f(X) and T_N=iota_n(S_N) for every N, then the isometry iota_n is continuous, so T_N converges to iota_n(f(X)); since the power-series definition identifies the same T_N-limit as f(iota_n(X)), uniqueness of limits gives both definedness and f(iota_n(X))=iota_n(f(X)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Let Y=2P-I_B and assume ||Y^2-I_B||<1. Directly from the registered power-series definition of sgn and theta, theta(iota_n(Y))=iota_n(theta(Y)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For c_m=binom(-1/2,m), the binomial series h(w)=sum_{m>=0}c_m w^m has radius one and is the analytic inverse-square-root branch h(w)=(1+w)^(-1/2); hence the registered power-series functional calculus represents Z^(-1/2) by sum_{m>=0}c_m(Z-I)^m whenever ||Z-I||<1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** The coefficients c_m=binom(-1/2,m) satisfy c_0=1 and c_m/c_{m-1}=-(2m-1)/(2m) for m>=1; therefore lim_m |c_m/c_{m-1}|=1, so the ratio test gives radius of convergence exactly one for h(w)=sum_{m>=0}c_m w^m.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.2

**Statement:** On |w|<1 termwise differentiation is valid, and the coefficient recurrence gives 2(1+w)h'(w)+h(w)=0; hence d[(1+w)h(w)^2]/dw=0, while h(0)=1, so (1+w)h(w)^2=1 and h is the inverse-square-root branch normalized by h(0)=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.3

**Statement:** For a unital Banach algebra A and ||Z-I_A||<1, H=sum_{m>=0}c_m(Z-I_A)^m converges absolutely in norm; absolute convergence permits the same Cauchy products as the scalar identity, giving ZH^2=I_A, and the normalization H=I_A+terms of positive degree identifies H with the analytic branch Z^(-1/2) used by the registered power-series functional calculus.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Assuming the binomial-series representation of the inverse-square-root branch on ||Z-I||<1, isometry and multiplicativity imply (iota_n(Y)^2)^(-1/2)=iota_n((Y^2)^(-1/2)) whenever ||Y^2-I_B||<1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** If (iota_n(Y)^2)^(-1/2)=iota_n((Y^2)^(-1/2)), then the registered definitions and homomorphism properties give sgn(iota_n(Y))=iota_n(sgn(Y)) and consequently theta(iota_n(Y))=iota_n(theta(Y)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

