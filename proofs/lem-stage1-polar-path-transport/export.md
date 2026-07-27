# Proof Export

## Node 1

**Statement:** Parameterized polar-path transport: there exist C_path^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_path >= C_path^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, every U_0, U_1 in calU, and every q in [0, 1] satisfying ||U_1 - U_0|| <= q, C_path*q <= 1/4, and C_path*(q + epsilon_r*q + q^2) < delta - C_pol*(epsilon_r*delta + delta^2), every L_{Z_t} is invertible and every Z_t = (1-t)*U_0 + t*U_1 lies in calUbar_{C_path*(q + epsilon_r*q + q^2)} for t in [0, 1], and, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the map H(t, U_0, U_1) = u_delta(Z_t) is jointly continuous in (t, U_0, U_1), joins U_0 to U_1, and satisfies H(t, cU_0, cU_1) = c*H(t, U_0, U_1) for every c in U(1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By lem-stage1-polar-path-admissibility choose universal witnesses a = C_path_hat >= 1, b = C_pol_hat >= 1, and k = kappa_pol_hat in (0,1/2], and define the threshold constants C_path^0 := a, C_pol^0 := b, and kappa_pol^0 := k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix any Stage-1 polar witness tuple and algebraic/path data satisfying the hypotheses of node 1 for these thresholds. Then the hypotheses of lem-stage1-polar-path-admissibility hold with its witness constants a,b,k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** In every exact-unit epsilon_r-C*-algebra one has epsilon_r >= 0: applying the product-norm axiom to J bold-dot J = J and ||J|| = 1 yields 1 <= 1+epsilon_r. Hence A := q+epsilon_r*q+q^2 and B := epsilon_r*delta+delta^2 are nonnegative because q in [0,1] and delta > 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Because a <= C_path, b <= C_pol, and kappa_pol <= k, the target smallness and short-path assumptions imply b*(epsilon_r+delta) <= C_pol*(epsilon_r+delta) <= kappa_pol <= k and a*q <= C_path*q <= 1/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Using A,B >= 0, a <= C_path, and b <= C_pol, the target strict loss inequality implies a*A <= C_path*A < delta-C_pol*B <= delta-b*B. Together with q in [0,1] and ||U_1-U_0|| <= q, these are exactly all hypotheses of lem-stage1-polar-path-admissibility at a,b,k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Applying lem-stage1-polar-path-admissibility with a,b,k gives all asserted invertibility, polar-path, continuity, endpoint, and scalar-equivariance conclusions, initially with Z_t in calUbar_{a*(q+epsilon_r*q+q^2)}; monotonicity of the defining calUbar radius upgrades this to calUbar_{C_path*(q+epsilon_r*q+q^2)}, so the full conclusion of node 1 follows.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Invoke lem-stage1-polar-path-admissibility using the hypotheses established in node 1.2. For every t in [0,1] it yields invertibility of L_{Z_t}, membership Z_t in calUbar_{a*A}, and the map H(t,U_0,U_1)=u_delta(Z_t), with the same polar-inverse notation u_delta used in node 1, jointly continuous in (t,U_0,U_1), joining U_0 to U_1, and satisfying H(t,cU_0,cU_1)=c*H(t,U_0,U_1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Since a <= C_path and A >= 0, a*A <= C_path*A. By def-approximate-unitary-space, X in calUbar_r means that X has a right inverse and ||X^dagger bold-dot X-J|| <= 2r; therefore calUbar_{a*A} is contained in calUbar_{C_path*A}. Applying this to each Z_t supplies exactly the larger-radius membership required in node 1, while every other conclusion already matches verbatim.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

