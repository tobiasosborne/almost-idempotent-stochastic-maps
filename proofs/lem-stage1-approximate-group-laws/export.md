# Proof Export

## Node 1

**Statement:** Quantitative approximate group laws: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta of the polar map defines C^1 maps mu(U, V) = u_delta(U bold-dot V), sigma(U) = u_delta(U^dagger) on all of calU, with mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), W) - mu(U, mu(V, W))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose one universal constant triple and one common fixed-delta polar datum as follows: if (G_d,P_d,k_d), (G_c,P_c,k_c), and (P_r,k_r) are witnesses furnished respectively by lem-stage1-group-domain-membership, lem-stage1-group-closeness, and lem-stage1-polar-retraction, set C_pol=max(P_d,P_c,P_r), kappa_pol=min(k_d,k_c,k_r,1/16), and C_grp=max(G_d,8*G_c,8). For every algebra and delta satisfying the root guards, all three upstream results apply, their polar inverse data can be identified, every U bold-dot V and U^dagger lies in the resulting S_delta, and the common inverse obeys the two bounds with constant G_c.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Let (G_d,P_d,k_d), (G_c,P_c,k_c), and (P_r,k_r) be fixed universal witnesses for lem-stage1-group-domain-membership, lem-stage1-group-closeness, and lem-stage1-polar-retraction. Define P=max(P_d,P_c,P_r), k=min(k_d,k_c,k_r,1/16), and G=max(G_d,8*G_c,8). Then P,G>=1 and 0<k<=1/2. If P*(epsilon_r+delta)<=k and G*epsilon_r<delta-P*(epsilon_r*delta+delta^2), then P_i*(epsilon_r+delta)<=k_i for i=d,c,r, while G_i*epsilon_r<=G*epsilon_r<delta-P*(epsilon_r*delta+delta^2)<=delta-P_i*(epsilon_r*delta+delta^2) for i=d,c. Hence all hypotheses of those three exact named externals hold; also epsilon_r<=1/16.

**Type:** claim

**Inference:** monotone witness synchronization using the four named validated externals

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For the fixed algebra and delta, every polar datum produced above uses the same map Pi_delta:(U,H)|->U bold-dot H on the same full domain calU x B_delta^{calH}(J), so every associated S_delta is its set-theoretic image and these image sets coincide. The external lem-stage1-polar-coherence-naturality identifies their inverse components on that common image. Therefore the membership conclusions of lem-stage1-group-domain-membership, the G_c*epsilon_r estimates of lem-stage1-group-closeness, and the C^1 inverse supplied by lem-stage1-polar-retraction all concern one common u_delta:S_delta->calU; in particular U bold-dot V and U^dagger belong to S_delta for all U,V in calU.

**Type:** claim

**Inference:** monotone witness synchronization using the four named validated externals

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** By 1.1, U bold-dot V and U^dagger lie in the common open S_delta and u_delta:S_delta->calU is C^1 by lem-stage1-polar-retraction. The multiplication is continuous bilinear by def-epsilon-cstar-algebra and hence C^1 in finite dimension; dagger is conjugate-linear, hence real-linear and C^1. Therefore mu(U,V)=u_delta(U bold-dot V) and sigma(U)=u_delta(U^dagger) are globally defined C^1 maps into calU. Also J lies in calU, J bold-dot U=U bold-dot J=U, and J^dagger=J by the exact-unit clauses. Since lem-stage1-polar-retraction gives u_delta(T)=T for every T in calU, mu(J,U)=mu(U,J)=U and sigma(J)=J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the common u_delta fixed in 1.1, lem-stage1-group-closeness gives ||mu(U,V)-U bold-dot V||<=G_c*epsilon_r and ||sigma(U)-U^dagger||<=G_c*epsilon_r. Since C_grp=G>=8*G_c, each is at most C_grp*epsilon_r, including epsilon_r=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The guard in 1.1 gives epsilon_r<=1/16. For T in calU, def-approximate-unitary-space gives T^dagger bold-dot T=J, while the exact-unit clause of def-epsilon-cstar-algebra gives ||J||=1. Its C*-inequality yields (1-epsilon_r)||T||^2<=||T^dagger bold-dot T||=1. Hence ||T||<=sqrt(16/15)<4/3 (because 16/15<16/9). This also bounds ||T^dagger||=||T||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Put A=mu(U,V) and B=mu(V,W), which lie in calU by 1.2. Insert A bold-dot W, (U bold-dot V) bold-dot W, U bold-dot (V bold-dot W), and U bold-dot B between the two iterated products. The two outer differences are each <=G_c*epsilon_r by lem-stage1-group-closeness; bilinearity and the product-norm axiom bound each replacement difference by (1+epsilon_r)*(4/3)*G_c*epsilon_r<=(17/12)*G_c*epsilon_r using 1.4; and the sole reassociation difference is <=epsilon_r*(4/3)^3=(64/27)*epsilon_r by the associator axiom. Thus the total is <=(2+17/6)*G_c*epsilon_r+(64/27)*epsilon_r<=(389/54)*G_c*epsilon_r<=8*G_c*epsilon_r<=C_grp*epsilon_r, where G_c>=1. All inequalities remain non-strict at epsilon_r=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Fix U in calU and choose a right inverse R, which exists by def-approximate-unitary-space. Then ||U bold-dot U^dagger-J||<=4*epsilon_r. This estimate is derived locally below from the root smallness guard and the defining epsilon_r-C*-algebra axioms, without using sibling node 1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** The existential constants in the root proof may be, and are, chosen with kappa_pol<=1/16: shrinking a positive admissible kappa_pol to min(kappa_pol,1/16) preserves all upstream hypotheses and conclusions. Hence the root guard C_pol*(epsilon_r+delta)<=kappa_pol, together with C_pol>=1 and delta>0, gives epsilon_r<=epsilon_r+delta<=kappa_pol/C_pol<=1/16. For U in calU, def-approximate-unitary-space gives U^dagger bold-dot U=J, while the exact-unit clause of def-epsilon-cstar-algebra gives ||J||=1. The C*-inequality therefore yields (1-epsilon_r)*||U||^2<=||U^dagger bold-dot U||=1, so ||U||^2<=16/15<16/9 and ||U||=||U^dagger||<=4/3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** Choose the right inverse R supplied by def-approximate-unitary-space, so U bold-dot R=J. Exact-unit identities and U^dagger bold-dot U=J give R-U^dagger=(U^dagger bold-dot U) bold-dot R-U^dagger bold-dot (U bold-dot R). The associator axiom and involutive isometry give ||R-U^dagger||<=epsilon_r*||U^dagger||*||U||*||R||=a*||R||, where a:=epsilon_r*||U||^2. By the preceding local estimate, a<=(16/9)*epsilon_r<=1/9. Thus ||R||<=||U^dagger||+||R-U^dagger||<=4/3+a*||R||, whence (1-a)||R||<=4/3 and ||R||<=(4/3)/(8/9)=3/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.3

**Statement:** By bilinearity and U bold-dot R=J, U bold-dot U^dagger-J=U bold-dot (U^dagger-R). The product-norm axiom, followed by the two preceding local estimates, gives ||U bold-dot U^dagger-J||<=(1+epsilon_r)*||U||*||U^dagger-R||<=(1+epsilon_r)*||U||*epsilon_r*||U||^2*||R||<=(17/16)*(4/3)*(16/9)*(3/2)*epsilon_r=(34/9)*epsilon_r<=4*epsilon_r. This uses only bilinearity, the product-norm axiom, and the single associator estimate in the preceding child.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Since sigma(U) lies in calU, lem-stage1-group-closeness applies to (sigma(U),U) and gives ||mu(sigma(U),U)-sigma(U) bold-dot U||<=G_c*epsilon_r. By the product-norm axiom, 1.4, and ||sigma(U)-U^dagger||<=G_c*epsilon_r, the next difference is ||sigma(U) bold-dot U-U^dagger bold-dot U||<=(17/12)*G_c*epsilon_r. Finally U^dagger bold-dot U=J by def-approximate-unitary-space. Hence ||mu(sigma(U),U)-J||<=(29/12)*G_c*epsilon_r<=3*G_c*epsilon_r<=C_grp*epsilon_r, also at epsilon_r=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Since sigma(U) lies in calU, lem-stage1-group-closeness gives ||mu(U,sigma(U))-U bold-dot sigma(U)||<=G_c*epsilon_r. The product-norm axiom, 1.4, and ||sigma(U)-U^dagger||<=G_c*epsilon_r give ||U bold-dot sigma(U)-U bold-dot U^dagger||<=(17/12)*G_c*epsilon_r. Node 1.6 gives ||U bold-dot U^dagger-J||<=4*epsilon_r. Therefore ||mu(U,sigma(U))-J||<=(29/12)*G_c*epsilon_r+4*epsilon_r<=(77/12)*G_c*epsilon_r<=8*G_c*epsilon_r<=C_grp*epsilon_r because G_c>=1; this is endpoint-safe at epsilon_r=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

