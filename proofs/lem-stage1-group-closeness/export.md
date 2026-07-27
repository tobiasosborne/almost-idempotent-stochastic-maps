# Proof Export

## Node 1

**Statement:** Group-input polar closeness: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta:S_delta -> calU of the polar map satisfies ||u_delta(U bold-dot V) - U bold-dot V|| <= C_grp*epsilon_r and ||u_delta(U^dagger) - U^dagger|| <= C_grp*epsilon_r for every U, V in calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Constant choice and polar range: take C_pol^0,kappa_pol^0 from the validated external lem-stage1-polar-retraction, set C_pol=C_pol^0, kappa_pol=min(kappa_pol^0,1/16), C_grp=5, and rho=delta-C_pol*(epsilon_r*delta+delta^2). These are universal with C_grp,C_pol>=1 and kappa_pol in (0,1/2]. Under the root hypotheses, epsilon_r+delta<=1/16 and rho>5*epsilon_r>=0; lem-stage1-polar-retraction applies and gives calU_rho subseteq S_delta together with X=u_delta(X) bold-dot h_delta(X), u_delta(X) in calU, and ||h_delta(X)-J||<delta for X in S_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Raw input estimates and domain typing: with the constants and rho of 1.1, every U,V in calU satisfy ||(U bold-dot V)^dagger bold-dot (U bold-dot V)-J||<=3*epsilon_r and U bold-dot V has a right inverse, while ||(U^dagger)^dagger bold-dot U^dagger-J||<=2*epsilon_r and U^dagger has the right inverse U. Consequently U bold-dot V and U^dagger both belong to calU_rho and hence to S_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Unitary norm and right-inverse data: for W in calU, def-approximate-unitary-space gives W^dagger bold-dot W=J and an R with W bold-dot R=J. The exact-unit clause of def-epsilon-cstar-algebra gives ||J||=1, while its C*-lower bound gives 1=||W^dagger bold-dot W||>=(1-epsilon_r)||W||^2; since epsilon_r<=1/16, ||W||^2<=1/(1-epsilon_r)<=16/15.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Opposite-product defect: for W in calU and R as in 1.2.1, the associator axiom gives ||R-W^dagger||=||(W^dagger bold-dot W) bold-dot R-W^dagger bold-dot (W bold-dot R)||<=epsilon_r||W||^2||R||. Thus epsilon_r||W||^2<=1/15 implies ||R||<=15||W||/14. Using J=W bold-dot R, the product-norm axiom, and ||W^dagger||=||W||, one obtains ||W bold-dot W^dagger-J||<=epsilon_r(1+epsilon_r)||W||^3||R||<=((17/16)*(15/14)*(256/225))*epsilon_r<=2*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Product defect: for U,V in calU and X=U bold-dot V, the involution axiom gives X^dagger=V^dagger bold-dot U^dagger. Two applications of the associator axiom compare (V^dagger bold-dot U^dagger) bold-dot (U bold-dot V) first with ((V^dagger bold-dot U^dagger) bold-dot U) bold-dot V and then with (V^dagger bold-dot (U^dagger bold-dot U)) bold-dot V=J. The product-norm axiom and 1.2.1 therefore give ||X^dagger bold-dot X-J||<=2*epsilon_r*(1+epsilon_r)||U||^2||V||^2<=(544/225)*epsilon_r<=3*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Exact right inverse for the product: for X=U bold-dot V, the product-norm estimate and 1.2.1 give ||X||^2<=(1+epsilon_r)^2*(16/15)^2<=289/225. If X bold-dot Y=0, the associator axiom and the defect bound of 1.2.3 imply ||Y||<=||(J-X^dagger bold-dot X) bold-dot Y||+||(X^dagger bold-dot X) bold-dot Y-X^dagger bold-dot (X bold-dot Y)||<=((1+epsilon_r)*3*epsilon_r+epsilon_r||X||^2)||Y||<=(51/256+289/3600)||Y||<(1/2)||Y||. Hence Y=0. Bilinearity makes the left multiplier L_X linear; on the finite-dimensional algebra it is therefore surjective, so some R_X satisfies X bold-dot R_X=J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** Domain conclusion: X_*=U^dagger has the exact right inverse U, and by the involution axiom its defect is ||U bold-dot U^dagger-J||<=2*epsilon_r from 1.2.2. The product X_p=U bold-dot V has a right inverse by 1.2.4 and defect at most 3*epsilon_r by 1.2.3. Since rho>5*epsilon_r, each defect is strictly below 2*rho (if epsilon_r=0, use rho>0 separately). By def-approximate-unitary-space both inputs lie in calU_rho, and 1.1 (lem-stage1-polar-retraction) gives calU_rho subseteq S_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Polar closeness estimate: under epsilon_r+delta<=1/16, if X lies in S_delta and ||X^dagger bold-dot X-J||<=3*epsilon_r, then the polar inverse from lem-stage1-polar-retraction satisfies ||u_delta(X)-X||<=5*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Polar square comparison: write u=u_delta(X), h=h_delta(X), and a=h-J. By lem-stage1-polar-retraction, X=u bold-dot h, u lies in calU, h is Hermitian, and ||a||<delta. Hence ||u||^2<=1/(1-epsilon_r)<=16/15 by the C*-lower bound applied to u^dagger bold-dot u=J, while ||h||<=1+delta<=17/16. The involution axiom gives X^dagger=h bold-dot u^dagger. Comparing (h bold-dot u^dagger) bold-dot (u bold-dot h) with ((h bold-dot u^dagger) bold-dot u) bold-dot h and then with (h bold-dot (u^dagger bold-dot u)) bold-dot h=h bold-dot h, the associator and product-norm axioms give ||X^dagger bold-dot X-h bold-dot h||<=2*epsilon_r*(1+epsilon_r)||h||^2||u||^2<=(9826/3840)*epsilon_r<=3*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Quadratic absorption: exact unitality and bilinearity give h bold-dot h-J=(J+a) bold-dot (J+a)-J=2a+a bold-dot a. Combining the assumed defect ||X^dagger bold-dot X-J||<=3*epsilon_r with 1.3.1 yields 2||a||<=6*epsilon_r+(1+epsilon_r)||a||^2. Since ||a||<delta<=1/16 and epsilon_r<=1/16, (1+epsilon_r)||a||^2<=(17/256)||a||. Thus (495/256)||a||<=6*epsilon_r, so ||a||<=(1536/495)*epsilon_r<=4*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Return to the polar factor: exact right unitality and X=u bold-dot h give ||u_delta(X)-X||=||u bold-dot J-u bold-dot h||=||u bold-dot (J-h)||<=(1+epsilon_r)||u||||a||. Using ||u||<=sqrt(16/15), epsilon_r<=1/16, and 1.3.2 gives ||u_delta(X)-X||<=(17/sqrt(15))*epsilon_r<=5*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

