# Proof Export

## Node 1

**Statement:** Joint projected-straight-path admissibility: there exist universal C_path, C_pol >= 1, kappa_pol in (0, 1/2] such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, and U_0, U_1 in calU, if 0 <= q <= 1, ||U_1 - U_0|| <= q, C_path*q <= 1/4, and C_path*(q + epsilon_r*q + q^2) < delta - C_pol*(epsilon_r*delta + delta^2), then for Z_t = (1-t)*U_0 + t*U_1 every L_{Z_t} is invertible, every Z_t in calUbar_{C_path*(q + epsilon_r*q + q^2)}, and H(t, U_0, U_1) = u_delta(Z_t) is jointly continuous in all displayed variables, joins U_0 to U_1, and obeys H(t, cU_0, cU_1) = c*H(t, U_0, U_1) for c in U(1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Quantitative path bounds: after choosing universal constants from lem-stage1-polar-retraction with C_path=1 and a harmlessly smaller kappa_pol, every admissible straight-path point Z_t has invertible L_{Z_t} and lies in calUbar_{q+epsilon_r*q+q^2}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Choose C_pol=C_pol^0 from lem-stage1-polar-retraction, kappa_pol=min(kappa_pol^0,C_pol^0/8), and C_path=1. Then C_pol*(epsilon_r+delta)<=kappa_pol implies epsilon_r<=1/8. For every U in calU, U^dagger bold-dot U=J and the epsilon-C*-lower bound give ||U||<=1/sqrt(1-epsilon_r)<=sqrt(8/7). Approximate associativity gives ||L_{U^dagger}L_U-I||<=epsilon_r||U||^2<=1/7; hence Neumann inversion and finite dimensionality give L_U invertible with ||L_U^{-1}||<=(7/6)(1+epsilon_r)||U||<=3/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Put D=U_1-U_0. Bilinearity, involution reversal, and U_i^dagger bold-dot U_i=J give the exact identity Z_t^dagger bold-dot Z_t-J=t*(t-1)*(D^dagger bold-dot D). Consequently ||Z_t^dagger bold-dot Z_t-J||<=t*(1-t)*(1+epsilon_r)||D||^2<=(1+epsilon_r)q^2/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Since L_{Z_t}=L_{U_0}+tL_D and ||L_D||<=(1+epsilon_r)||D||, the preceding inverse bound and q<=1/4 give ||tL_{U_0}^{-1}L_D||<=(3/2)(9/8)(1/4)=27/64<1. Neumann inversion makes every L_{Z_t} invertible, so solving Z_t bold-dot R=J supplies a right inverse. Together with the defect estimate and (1+epsilon_r)q^2/4<=2*(q+epsilon_r*q+q^2), this is exactly Z_t in calUbar_{q+epsilon_r*q+q^2} by def-approximate-unitary-space.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Common polar-domain admissibility: writing rho=delta-C_pol*(epsilon_r*delta+delta^2), the strict hypothesis q+epsilon_r*q+q^2<rho and the quantitative path bounds imply Z_t lies in S_delta for every t in [0,1], by lem-stage1-polar-retraction.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let gamma=q+epsilon_r*q+q^2 and rho=delta-C_pol*(epsilon_r*delta+delta^2). The strict hypothesis gamma<rho and Z_t in calUbar_gamma imply ||Z_t^dagger bold-dot Z_t-J||<=2gamma<2rho, while Z_t has a right inverse; hence Z_t belongs to the strict set calU_rho.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** By the inner inclusion calU_{delta-C_pol*(epsilon_r*delta+delta^2)} subseteq S_delta in lem-stage1-polar-retraction, the preceding membership Z_t in calU_rho implies Z_t in S_delta for every t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Projected-path properties: because the whole straight path lies in the single open polar domain S_delta, H(t,U_0,U_1)=u_delta(Z_t) is jointly continuous, has endpoints U_0,U_1, and is U(1)-equivariant by lem-stage1-polar-retraction and lem-stage1-polar-coherence-naturality.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** The affine evaluation map (t,U_0,U_1) maps continuously to Z_t by the Banach-space operations, and u_delta is C^1, hence continuous, on the open set S_delta by lem-stage1-polar-retraction. Therefore their composition H is jointly continuous on the displayed admissible parameter domain. Also Z_0=U_0 and Z_1=U_1, and lem-stage1-polar-retraction gives u_delta(U_i)=U_i, so H joins U_0 to U_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** For c in U(1), conjugate linearity of dagger, bilinearity, and |c|=1 show (cU_i)^dagger bold-dot(cU_i)=J; scaling a right inverse of U_i by conjugate(c) supplies a right inverse of cU_i. Thus cU_i lies in calU, ||cU_1-cU_0||=||U_1-U_0||, and the rotated pair satisfies the same hypotheses. Its affine path is Z_t(cU_0,cU_1)=cZ_t, so both Z_t and cZ_t lie in S_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Apply the scalar naturality clause of lem-stage1-polar-coherence-naturality to the polar data (delta,S_delta,u_delta,h_delta) and to X=Z_t: since X and cX lie in S_delta, u_delta(cZ_t)=c*u_delta(Z_t). With the scaled-path identity, this is H(t,cU_0,cU_1)=c*H(t,U_0,U_1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

