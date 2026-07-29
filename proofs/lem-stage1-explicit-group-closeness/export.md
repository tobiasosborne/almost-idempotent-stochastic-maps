# Proof Export

## Node 1

**Statement:** Explicit group-input polar closeness: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU satisfies ||u_delta(U bold-dot V) - U bold-dot V|| <= C_grp*epsilon_r and ||u_delta(U^dagger) - U^dagger|| <= C_grp*epsilon_r for every U, V in calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Constant choice and typed polar inverse: take C_pol^0,kappa_pol^0 from the validated external lem-stage1-polar-retraction, set C_pol=C_pol^0, kappa_pol=min(kappa_pol^0,1/16), C_grp=5, and rho=delta-C_pol*(epsilon_r*delta+delta^2). These are universal with C_grp,C_pol>=1 and kappa_pol in (0,1/2]. Under the root hypotheses, epsilon_r+delta<=1/16 and rho>5*epsilon_r>=0. The hypotheses of lem-stage1-polar-retraction hold, so its displayed map Pi_delta:calU x B^{calH}_delta(J)->S_delta, Pi_delta(U,H)=U bold-dot H, has a unique inverse pair (u_delta,h_delta):S_delta->calU x B^{calH}_delta(J); for every X in S_delta this typed pair obeys X=u_delta(X) bold-dot h_delta(X), u_delta(X) in calU, h_delta(X) in B^{calH}_delta(J), hence ||h_delta(X)-J||<delta, and calU_rho is contained in S_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Raw input estimates and domain typing: with the constants, rho, and typed inverse pair fixed in 1.1, every U,V in calU satisfy ||(U bold-dot V)^dagger bold-dot (U bold-dot V)-J||<=3*epsilon_r and U bold-dot V has a right inverse, while ||(U^dagger)^dagger bold-dot U^dagger-J||<=2*epsilon_r and U^dagger has the right inverse U. Consequently U bold-dot V and U^dagger both belong to calU_rho and hence to S_delta, so the fixed maps u_delta,h_delta may be evaluated at both displayed inputs.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Unitary norm and right-inverse data: for W in calU, def-approximate-unitary-space gives W^dagger bold-dot W=J and an R with W bold-dot R=J. The exact-unit clause of def-epsilon-cstar-algebra gives ||J||=1, while its C*-lower bound gives 1=||W^dagger bold-dot W||>=(1-epsilon_r)||W||^2; by the smallness derived in 1.1, epsilon_r<=1/16, so ||W||^2<=1/(1-epsilon_r)<=16/15.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Opposite-product defect: for W in calU and R as in 1.2.1, exact unitality and the associator axiom give ||R-W^dagger||=||(W^dagger bold-dot W) bold-dot R-W^dagger bold-dot (W bold-dot R)||<=epsilon_r||W||^2||R||. Thus epsilon_r||W||^2<=1/15 implies ||R||<=15||W||/14. Since J=W bold-dot R, the product-norm axiom and ||W^dagger||=||W|| yield ||W bold-dot W^dagger-J||=||W bold-dot(W^dagger-R)||<=epsilon_r*(1+epsilon_r)||W||^3||R||<=((17/16)*(15/14)*(256/225))*epsilon_r<=2*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Product defect: for U,V in calU and X=U bold-dot V, the involution axiom gives X^dagger=V^dagger bold-dot U^dagger. Two applications of the associator axiom compare (V^dagger bold-dot U^dagger) bold-dot (U bold-dot V) first with ((V^dagger bold-dot U^dagger) bold-dot U) bold-dot V and then with (V^dagger bold-dot (U^dagger bold-dot U)) bold-dot V=(V^dagger bold-dot J) bold-dot V=J. The product-norm axiom and 1.2.1 therefore give ||X^dagger bold-dot X-J||<=2*epsilon_r*(1+epsilon_r)||U||^2||V||^2<=(544/225)*epsilon_r<=3*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** Self-contained numerical bridge (independent of sibling 1.2.1): the fixed root guard and constant choice give C_pol>=1 and C_pol*(epsilon_r+delta)<=kappa_pol<=1/16, hence 0<=epsilon_r<=1/16. For each W in calU, the definition of calU gives W^dagger bold-dot W=J, while exact unitality and the C*-lower axiom give 1=||J||=||W^dagger bold-dot W||>=(1-epsilon_r)||W||^2; since 1-epsilon_r>0, ||W||^2<=1/(1-epsilon_r)<=16/15. Thus for U,V in calU both ||U||^2 and ||V||^2 are at most 16/15. Now set A=(V^dagger bold-dot U^dagger) bold-dot (U bold-dot V), B=((V^dagger bold-dot U^dagger) bold-dot U) bold-dot V, and C=(V^dagger bold-dot (U^dagger bold-dot U)) bold-dot V. The associator and product-norm axioms give ||A-B||<=epsilon_r||V^dagger bold-dot U^dagger||||U||||V||<=epsilon_r*(1+epsilon_r)||U||^2||V||^2 and ||B-C||<=(1+epsilon_r)||((V^dagger bold-dot U^dagger) bold-dot U)-V^dagger bold-dot(U^dagger bold-dot U)|| ||V||<=epsilon_r*(1+epsilon_r)||U||^2||V||^2. Since U^dagger bold-dot U=J and exact unitality gives C=(V^dagger bold-dot J) bold-dot V=V^dagger bold-dot V=J, while the involution axiom gives A=(U bold-dot V)^dagger bold-dot(U bold-dot V), the triangle inequality yields the defect bound <=2*epsilon_r*(1+epsilon_r)*(16/15)^2<=(544/225)*epsilon_r<=3*epsilon_r. This proves the numerical conclusion entirely inside the subtree of 1.2.3, including when epsilon_r=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Exact right inverse for the product: for X=U bold-dot V, the product-norm estimate and 1.2.1 give ||X||^2<=(1+epsilon_r)^2*(16/15)^2<=289/225. If X bold-dot Y=0, exact unitality, the product-norm axiom, the associator axiom, and 1.2.3 imply ||Y||<=||(J-X^dagger bold-dot X) bold-dot Y||+||(X^dagger bold-dot X) bold-dot Y-X^dagger bold-dot (X bold-dot Y)||<=((1+epsilon_r)*3*epsilon_r+epsilon_r||X||^2)||Y||<=(51/256+289/3600)||Y||<(1/2)||Y||. Hence Y=0. Bilinearity makes L_X:Y->X bold-dot Y linear; because the algebra is finite-dimensional, injectivity makes L_X surjective, so some R_X satisfies X bold-dot R_X=J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** Domain conclusion for the fixed inverse: X_*=U^dagger has the exact right inverse U, and the involution axiom plus 1.2.2 gives ||(X_*)^dagger bold-dot X_*-J||=||U bold-dot U^dagger-J||<=2*epsilon_r. The product X_p=U bold-dot V has a right inverse by 1.2.4 and defect at most 3*epsilon_r by 1.2.3. Since rho>5*epsilon_r by 1.1, each defect is strictly below 2*rho (when epsilon_r=0, both defects vanish and rho>0). By def-approximate-unitary-space both inputs lie in calU_rho; the inclusion from lem-stage1-polar-retraction recorded in 1.1 puts both in S_delta, where the already-fixed typed pair (u_delta,h_delta) is defined.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.5.1

**Statement:** Validated-premise domain bridge: fix U,V in calU and put X_p=U bold-dot V and X_*=U^dagger. By validated 1.2.2 instantiated at W=U, ||U bold-dot U^dagger-J||<=2*epsilon_r. The involution axiom gives (X_*)^dagger=U, while U in calU gives U^dagger bold-dot U=J; hence ||(X_*)^dagger bold-dot X_*-J||<=2*epsilon_r and X_* bold-dot U=J, so U is a right inverse of X_*. By validated 1.2.3 and 1.2.4, ||X_p^dagger bold-dot X_p-J||<=3*epsilon_r and X_p has a right inverse. Validated 1.1 gives rho>5*epsilon_r and calU_rho subseteq S_delta for its fixed typed inverse pair. If epsilon_r>0, both 2*epsilon_r and 3*epsilon_r are strictly less than 2*rho; if epsilon_r=0, both defects vanish and rho>0, so the same strict inequalities hold. Therefore def-approximate-unitary-space places X_* and X_p in calU_rho, hence in S_delta, and the single typed pair (u_delta,h_delta) fixed in 1.1 is defined at both inputs.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.5.1.1

**Statement:** Replacement product-input estimate independent of pending 1.2.3: put e=epsilon_r and X=U bold-dot V. Validated 1.1 gives 0<=e<=1/16. Since U,V are in calU, def-approximate-unitary-space gives U^dagger bold-dot U=V^dagger bold-dot V=J; the C*-lower axiom and ||J||=1 give ||U||^2,||V||^2<=1/(1-e). The involution axiom gives X^dagger=V^dagger bold-dot U^dagger. Applying the associator axiom first to (V^dagger bold-dot U^dagger,U,V), and then to (V^dagger,U^dagger,U) followed by the product-norm axiom for right multiplication by V, yields ||X^dagger bold-dot X-J||<=2*e*(1+e)*||U||^2*||V||^2<=2*e*(17/16)*(16/15)^2=(544/225)*e<3*e when e>0, while it is 0 when e=0. Moreover ||X||^2<=(1+e)^2||U||^2||V||^2<=(17/15)^2=289/225. If X bold-dot Y=0, exact unitality, the product-norm axiom and the associator axiom give ||Y||<=((1+e)*3*e+e||X||^2)||Y||<=(51/256+289/3600)||Y||<(1/2)||Y||, hence Y=0. Thus the finite-dimensional linear map L_X is injective and therefore surjective, so X has a right inverse. This proves both product-input requirements without 1.2.3 or 1.2.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.5.1.2

**Statement:** Corrected domain conclusion using only validated premises and the replacement child: for X_*=U^dagger, validated 1.2.2 gives ||(X_*)^dagger bold-dot X_*-J||=||U bold-dot U^dagger-J||<=2*epsilon_r, and X_* bold-dot U=U^dagger bold-dot U=J gives a right inverse. The preceding replacement child gives X_p=U bold-dot V a right inverse and defect at most 3*epsilon_r. Validated 1.1 gives rho>5*epsilon_r and calU_rho subseteq S_delta. Hence both defects are strictly below 2*rho (also when epsilon_r=0, since then they vanish and rho>0), so def-approximate-unitary-space places X_* and X_p in calU_rho and therefore in S_delta, where the single typed inverse pair fixed by 1.1 is defined. No use is made of pending node 1.2.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Polar closeness and conclusion: under epsilon_r+delta<=1/16, if X lies in S_delta and ||X^dagger bold-dot X-J||<=3*epsilon_r, then the typed inverse pair fixed in 1.1 satisfies ||u_delta(X)-X||<=5*epsilon_r. Apply this first to X=U bold-dot V and then to X=U^dagger using 1.2; since C_grp=5, both inequalities required by the root follow for the same displayed u_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Polar square comparison for the fixed pair: write u=u_delta(X), h=h_delta(X), and a=h-J for the typed inverse pair supplied in 1.1. Then X=u bold-dot h, u lies in calU, h is Hermitian, and ||a||<delta. Thus ||u||^2<=1/(1-epsilon_r)<=16/15 by the C*-lower bound applied to u^dagger bold-dot u=J, while ||h||<=1+delta<=17/16. The involution axiom gives X^dagger=h bold-dot u^dagger. Two associator comparisons, from (h bold-dot u^dagger) bold-dot (u bold-dot h) to ((h bold-dot u^dagger) bold-dot u) bold-dot h and then to (h bold-dot (u^dagger bold-dot u)) bold-dot h=h bold-dot h, together with the product-norm axiom give ||X^dagger bold-dot X-h bold-dot h||<=2*epsilon_r*(1+epsilon_r)||h||^2||u||^2<=(9826/3840)*epsilon_r<=3*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Quadratic absorption: exact unitality and bilinearity give h bold-dot h-J=(J+a) bold-dot (J+a)-J=2a+a bold-dot a. Combining the assumed defect ||X^dagger bold-dot X-J||<=3*epsilon_r with 1.3.1 yields 2||a||<=6*epsilon_r+(1+epsilon_r)||a||^2. The guard in 1.1 gives ||a||<delta<=1/16 and epsilon_r<=1/16, hence (1+epsilon_r)||a||^2<=(17/256)||a||. Therefore (495/256)||a||<=6*epsilon_r and ||a||<=(1536/495)*epsilon_r<=4*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Return to the same first inverse component: exact right unitality and the typed identity X=u_delta(X) bold-dot h_delta(X) from 1.1 give ||u_delta(X)-X||=||u bold-dot J-u bold-dot h||=||u bold-dot(J-h)||<=(1+epsilon_r)||u||||a||. Using ||u||<=sqrt(16/15) from 1.3.1, epsilon_r<=1/16 from 1.1, and 1.3.2 gives ||u_delta(X)-X||<=(17/sqrt(15))*epsilon_r<=5*epsilon_r. Applying this bound to the two S_delta inputs typed in 1.2 (whose defects are at most 3*epsilon_r) proves the two root inequalities for the single inverse component u_delta fixed in 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

