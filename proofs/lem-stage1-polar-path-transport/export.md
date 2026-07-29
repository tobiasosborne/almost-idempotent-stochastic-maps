# Proof Export

## Node 1

**Statement:** Parameterized polar-path transport: there exist C_path^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_path >= C_path^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, every U_0, U_1 in calU, and every q in [0, 1] satisfying ||U_1 - U_0|| <= q, C_path*q <= 1/4, and C_path*(q + epsilon_r*q + q^2) < delta - C_pol*(epsilon_r*delta + delta^2), every L_{Z_t} is invertible and every Z_t = (1-t)*U_0 + t*U_1 lies in calUbar_{C_path*(q + epsilon_r*q + q^2)} for t in [0, 1], and, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the map H(t, U_0, U_1) = u_delta(Z_t) is jointly continuous in (t, U_0, U_1), joins U_0 to U_1, and satisfies H(t, cU_0, cU_1) = c*H(t, U_0, U_1) for every c in U(1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Invoke lem-stage1-polar-path-admissibility and choose its universal witnesses A,B >= 1 and k in (0,1/2]. Invoke lem-stage1-polar-retraction-transport and choose its universal witnesses P >= 1 and rho in (0,1/2]. Define C_path^0 := A, C_pol^0 := max{B,P}, and kappa_pol^0 := min{k,rho}. Then C_path^0,C_pol^0 >= 1 and kappa_pol^0 lies in (0,1/2], and all three constants are universal; this choice is made before the receiving tuple W is quantified.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the witnesses fixed in 1.1, fix an arbitrary receiving Stage-1 polar witness tuple W and arbitrary algebra, delta,U_0,U_1,q satisfying the root hypotheses, and put g:=q+epsilon_r*q+q^2 and r:=epsilon_r*delta+delta^2. Then A<=C_path, B<=C_pol, P<=C_pol, and kappa_pol<=k,rho. Since epsilon_r,delta,q are nonnegative, the receiving hypotheses imply B*(epsilon_r+delta)<=C_pol*(epsilon_r+delta)<=kappa_pol<=k, P*(epsilon_r+delta)<=C_pol*(epsilon_r+delta)<=kappa_pol<=rho, A*q<=C_path*q<=1/4, and A*g<=C_path*g<delta-C_pol*r<=delta-B*r. Thus the scalar smallness and path guards required by the two cited upstream results hold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Apply lem-stage1-polar-path-admissibility with its witnesses A,B,k, using exactly the transferred guards in 1.2. For every t in [0,1], L_{Z_t} is invertible and Z_t=(1-t)U_0+tU_1 lies in calUbar_{A*g}. Because A*g<=C_path*g, the defining residual bound for calUbar_{A*g} implies the weaker bound for calUbar_{C_path*g}, with the same right inverse; hence Z_t lies in calUbar_{C_path*(q+epsilon_r*q+q^2)} for every t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Apply lem-stage1-polar-retraction-transport to the receiving tuple W. Its coefficient and margin hypotheses hold because P <= C_pol and 0 < kappa_pol <= rho by 1.1-1.2, while its algebra/delta smallness hypothesis is exactly the non-strict receiving guard C_pol*(epsilon_r+delta) <= kappa_pol from the root hypotheses (also recorded in 1.2); no strict inequality is needed. For the very map displayed in the root, Pi_delta:calU x B_delta^{calH}(J)->S_delta, Pi_delta(U,H)=U bold-dot H, the transport theorem therefore gives a C^1 diffeomorphism onto S_delta, with unique inverse (u_delta,h_delta), the identities X=u_delta(X) bold-dot h_delta(X), u_delta(U)=U and h_delta(U)=J, and the inclusion calU_{delta-C_pol*r} subseteq S_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For each t, 1.3 gives Z_t in calUbar_{C_path*g}, so Z_t has a right inverse and ||Z_t^dagger bold-dot Z_t-J||<=2*C_path*g. The strict receiving guard in 1.2 gives C_path*g<delta-C_pol*r, hence ||Z_t^dagger bold-dot Z_t-J||<2*(delta-C_pol*r). By def-approximate-unitary-space, Z_t lies in calU_{delta-C_pol*r}; the inclusion supplied in 1.4 therefore puts Z_t in S_delta. Consequently u_delta(Z_t) in the contract is the well-typed unique first component of the inverse of that same displayed Pi_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** The inverse (u_delta,h_delta) in 1.4 is C^1 and therefore continuous on S_delta. The affine map (t,U_0,U_1) mapsto (1-t)U_0+tU_1 is jointly continuous, and 1.5 places its value in S_delta throughout the admissible parameter domain. Therefore H(t,U_0,U_1):=u_delta((1-t)U_0+tU_1) is jointly continuous in (t,U_0,U_1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** At t=0 and t=1 the affine path gives Z_0=U_0 and Z_1=U_1. Since U_0,U_1 lie in calU and 1.4 gives u_delta(U)=U for every U in calU, H(0,U_0,U_1)=U_0 and H(1,U_0,U_1)=U_1; thus H joins the two endpoints.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Fix c in U(1) and t in [0,1], and write (u,h):=(u_delta(Z_t),h_delta(Z_t)). By 1.4-1.5, u lies in calU, h lies in B_delta^{calH}(J), and Pi_delta(u,h)=Z_t. Conjugate-linearity of dagger, bilinearity of bold-dot, and |c|=1 show directly from def-approximate-unitary-space that cu lies in calU (its unitary residual is unchanged and a right inverse rescales by conjugate(c)); also Pi_delta(cu,h)=c*Pi_delta(u,h)=cZ_t. The affine identity (1-t)cU_0+t cU_1=cZ_t holds, and the same calculation puts cU_0,cU_1 in calU and preserves all norm guards. Since Pi_delta is a diffeomorphism and hence has a unique inverse, its inverse at cZ_t is (cu,h), so u_delta(cZ_t)=c*u_delta(Z_t). Therefore H(t,cU_0,cU_1)=c*H(t,U_0,U_1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** The constants selected in 1.1 have the required universal ranges. Because the receiving W, algebra, delta, U_0,U_1 and q fixed in 1.2 were arbitrary under the root hypotheses, 1.3 proves both binder-free path conclusions, 1.4-1.5 identify and type the exact displayed polar inverse along the whole path, and 1.6-1.8 prove joint continuity, the endpoint identities, and U(1)-equivariance. Universally generalizing these conclusions and existentially generalizing the constants proves the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.10

**Statement:** Boundary-case repair for the transfers used in 1.2-1.3: with g:=q+epsilon_r*q+q^2 and r:=epsilon_r*delta+delta^2, nonnegativity gives g,r>=0. From A<=C_path and B<=C_pol one has A*g<=C_path*g and B*r<=C_pol*r, hence the root strict guard yields the valid mixed chain A*g<=C_path*g<delta-C_pol*r<=delta-B*r; in particular A*g<delta-B*r, which is exactly the strict path guard required by lem-stage1-polar-path-admissibility. Likewise kappa_pol<=min{k,rho} gives only kappa_pol<=k and kappa_pol<=rho, and these non-strict bounds suffice: B*(epsilon_r+delta)<=C_pol*(epsilon_r+delta)<=kappa_pol<=k for path admissibility and P*(epsilon_r+delta)<=C_pol*(epsilon_r+delta)<=kappa_pol<=rho for polar-retraction transport. Thus neither C_path=A, nor kappa_pol=k or rho, nor g=0 causes a gap; no false strict intermediate inequality is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

