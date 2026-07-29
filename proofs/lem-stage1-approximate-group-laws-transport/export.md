# Proof Export

## Node 1

**Statement:** Parameterized approximate-group transport: there exist C_grp^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_grp >= C_grp^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the formulas mu(U, V) = u_delta(U bold-dot V) and sigma(U) = u_delta(U^dagger) define C^1 maps on all of calU x calU and calU, respectively, and for every U, V, Z in calU, mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), Z) - mu(U, mu(V, Z))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Provider witnesses and transported constants. Invoke lem-stage1-explicit-group-domain-membership once to fix universal G_d,P_d >= 1 and k_d in (0,1/2]; invoke lem-stage1-explicit-group-closeness once to fix universal G_c,P_c >= 1 and k_c in (0,1/2]; and invoke lem-stage1-polar-retraction once to fix universal P_r >= 1 and k_r in (0,1/2]. Define C_grp^0=max{G_d,8G_c,8}, C_pol^0=max{P_d,P_c,P_r}, and kappa_pol^0=min{k_d,k_c,k_r,1/16}. Then C_grp^0,C_pol^0 >= 1 and 0<kappa_pol^0<=1/2, and these constants are fixed before any receiving def-stage1-polar-witness-data tuple is quantified.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Transport of every provider guard. Fix an arbitrary receiving tuple W, finite-dimensional exact-unit epsilon_r-C*-algebra, and delta as in node 1, using the constants of 1.1; write e=epsilon_r and q=e*delta+delta^2. Since P_d,P_c,P_r <= C_pol and kappa_pol <= k_d,k_c,k_r, the receiving inequality C_pol*(e+delta)<=kappa_pol gives P_i*(e+delta)<=k_i for i=d,c,r. Since G_d,G_c<=C_grp and P_d,P_c<=C_pol, C_grp*e<delta-C_pol*q gives G_i*e<delta-P_i*q for i=d,c. Also C_pol>=1, delta>0, and C_pol*(e+delta)<=kappa_pol<=1/16 imply 0<=e<1/16. Thus all three fixed provider hypotheses hold for this same algebra and delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Typed conclusions of the three allowed providers. Under 1.2, lem-stage1-explicit-group-domain-membership supplies its unique inverse (u_d,h_d) of the displayed Pi_delta and says every U bold-dot V and U^dagger lies in S_delta and has a right inverse. Under the same hypotheses, lem-stage1-explicit-group-closeness supplies its unique inverse (u_c,h_c) and the bounds ||u_c(U bold-dot V)-U bold-dot V||<=G_c*e and ||u_c(U^dagger)-U^dagger||<=G_c*e. Finally lem-stage1-polar-retraction supplies a C^1 diffeomorphism Pi_delta from calU x B_delta^{calH}(J) onto S_delta, with unique C^1 inverse (u_r,h_r), u_r(U)=U and h_r(U)=J for U in calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Synchronization by ordinary inverse uniqueness. In all three provider conclusions of 1.3, Pi_delta has literally the same displayed formula Pi_delta(U,H)=U bold-dot H, the same domain calU x B_delta^{calH}(J), and the same image S_delta:=Pi_delta(calU x B_delta^{calH}(J)). Hence uniqueness of the inverse of this one bijection gives (u_d,h_d)=(u_c,h_c)=(u_r,h_r). They therefore equal the (u_delta,h_delta) named in node 1; in particular every domain, closeness, C^1, and retraction assertion in 1.3 concerns that same u_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Elementary uniform norm estimates used below. For every T in calU, def-approximate-unitary-space gives T^dagger bold-dot T=J and a right inverse R with T bold-dot R=J. The C*-lower bound in def-epsilon-cstar-algebra and ||J||=1 give ||T||<=a:=(1-e)^(-1/2). Therefore, for 0<=e<1/16, multiplying a perturbation on either side by a unitary costs at most (1+e)a<2, and the associator of three unitaries has norm at most e*a^3<=2e (with equality possible at e=0). Moreover exact unitality and the associator bound give ||R-T^dagger||=||(T^dagger bold-dot T) bold-dot R-T^dagger bold-dot (T bold-dot R)||<=e||T||^2||R||, whence ||R||<=||T||(1-e)/(1-2e); consequently ||T bold-dot T^dagger-J||<=e(1+e)/((1-e)(1-2e))<=2e (again allowing equality at e=0). These estimates also apply when T is mu(A,B) or sigma(A), since u_delta takes values in calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Global definition and C^1 regularity of the operations. By 1.3-1.4, U bold-dot V and U^dagger lie in S_delta for every U,V in calU, so mu(U,V)=u_delta(U bold-dot V) and sigma(U)=u_delta(U^dagger) are defined on all of calU x calU and calU and take values in calU. By lem-stage1-polar-retraction, u_delta is C^1 on S_delta; bilinearity of bold-dot and conjugate-linearity of dagger from def-epsilon-cstar-algebra make the two input maps C^1 (as real maps) in finite dimension. Their compositions mu and sigma are therefore C^1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Left unit law. For U in calU, exact unitality gives J bold-dot U=U, and the retraction identity synchronized in 1.4 gives u_delta(U)=U. Hence mu(J,U)=u_delta(J bold-dot U)=U.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Right unit law. For U in calU, exact unitality gives U bold-dot J=U, and the retraction identity synchronized in 1.4 gives u_delta(U)=U. Hence mu(U,J)=u_delta(U bold-dot J)=U.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Unit inversion law. Exact-unit compatibility with the involution in def-epsilon-cstar-algebra gives J^dagger=J, while 1.4 gives u_delta(J)=J. Thus sigma(J)=u_delta(J^dagger)=J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.10

**Statement:** Product closeness. The synchronized closeness provider in 1.3-1.4 gives ||mu(U,V)-U bold-dot V||=||u_delta(U bold-dot V)-U bold-dot V||<=G_c*e. Since C_grp>=C_grp^0>=8G_c>=G_c, this is at most C_grp*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.11

**Statement:** Inverse closeness. The synchronized closeness provider in 1.3-1.4 gives ||sigma(U)-U^dagger||=||u_delta(U^dagger)-U^dagger||<=G_c*e. Since C_grp>=C_grp^0>=8G_c>=G_c, this is at most C_grp*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.12

**Statement:** Approximate associativity of mu. Put A=mu(mu(U,V),Z) and B=mu(U,mu(V,Z)). By 1.10 at the provider strength G_c, the two outer retraction errors contribute G_c*e each. Replacing mu(U,V) by U bold-dot V and mu(V,Z) by V bold-dot Z inside one multiplication contributes less than 2G_c*e on each side by 1.5, and the intervening algebra associator contributes less than 2e. Hence ||A-B||<=(6G_c+2)e. From C_grp>=8G_c and C_grp>=8, one has 6G_c+2<=C_grp, proving ||mu(mu(U,V),Z)-mu(U,mu(V,Z))||<=C_grp*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.13

**Statement:** Left approximate inverse law. Since sigma(U) is in calU, product closeness gives ||mu(sigma(U),U)-sigma(U) bold-dot U||<=G_c*e. By inverse closeness and the non-strict multiplication estimate in the amended node 1.5, ||sigma(U) bold-dot U-U^dagger bold-dot U||<=(1+e)*||sigma(U)-U^dagger||*||U||<=2G_c*e; this remains valid when e=0. Also U^dagger bold-dot U=J by def-approximate-unitary-space. Hence the triangle inequality gives ||mu(sigma(U),U)-J||<=3G_c*e<=C_grp*e, because C_grp>=C_grp^0>=8G_c.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.14

**Statement:** Right approximate inverse law. Product closeness gives ||mu(U,sigma(U))-U bold-dot sigma(U)||<=G_c*e. By inverse closeness and the multiplication estimate of 1.5, ||U bold-dot sigma(U)-U bold-dot U^dagger||<=(1+e)*||U||*||sigma(U)-U^dagger||<=2G_c*e; this remains non-strict when e=0. The defect estimate derived in 1.5 gives ||U bold-dot U^dagger-J||<=e*(1+e)/((1-e)*(1-2e))<=2e for every 0<=e<1/16, including e=0. Hence the triangle inequality yields ||mu(U,sigma(U))-J||<=(3G_c+2)*e<=C_grp*e: indeed C_grp>=8G_c gives 3G_c<=(3/8)C_grp and C_grp>=8 gives 2<=C_grp/4, so 3G_c+2<=(5/8)C_grp<=C_grp.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.15

**Statement:** Assembly. Nodes 1.1-1.14 provide universal constants of the required ranges, transport all hypotheses to the three allowed providers, identify their inverse components with the single (u_delta,h_delta) bound in the contract, establish global C^1 maps, and prove every displayed identity and estimate for arbitrary W, algebra, delta, and U,V,Z. Universal generalization and the definitions of mu and sigma therefore yield node 1 exactly.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

