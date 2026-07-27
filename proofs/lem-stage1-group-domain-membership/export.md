# Proof Export

## Node 1

**Statement:** Group-input polar-domain membership: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta:S_delta -> calU of the polar map is defined at U bold-dot V and U^dagger for every U, V in calU; moreover, U bold-dot V and U^dagger each have a right inverse.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Invoke the registered external lem-stage1-polar-retraction and choose its universal constants C_pol >= 1 and kappa_pol in (0,1/2]; set the further universal witness C_grp:=4. Fix an arbitrary finite-dimensional exact-unit epsilon_r-C*-algebra, delta>0 satisfying the two root guards, and U,V in calU; abbreviate e:=epsilon_r and t:=delta-C_pol*(e*delta+delta^2). The external inner inclusion calU_t subseteq S_delta reduces the root to proving U bold-dot V and U^dagger belong to calU_t, including the right-inverse clause in the definition of calU_t.

**Type:** claim

**Inference:** existential_instantiation

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Guard arithmetic in the setup of node 1.1: C_pol*(e+delta)<=kappa_pol<=1/2 and C_pol>=1 give s:=e+delta<=1/2 and delta<=1/2; the second guard with C_grp=4 gives 4e<t, hence t>0. Also t=delta-C_pol*delta*s<=delta*(1-s). Since e<t<=delta*(1-e-delta), write delta=s-e. The function (s-e)*(1-s) is increasing for e<=s<=1/2 because its derivative is 1+e-2s>=e>=0; therefore e<(1/2-e)/2=1/4-e/2, so e<1/6. These are the only smallness consequences used below.

**Type:** claim

**Inference:** arithmetic

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Common multiplier estimate, using node 1.2 explicitly. For every W in calU, def-approximate-unitary-space gives W^dagger bold-dot W=J and a right inverse, while def-epsilon-cstar-algebra gives (1-e)||W||^2<=1 and ||L_{W^dagger}L_W-I||<=e||W||^2<=e/(1-e)<1/5. Thus L_W is injective and, because calX is finite-dimensional, bijective. Moreover ||L_{W^dagger}||<=(1+e)||W||<=7/5 and ||L_{W^dagger}L_W Z||>=(4/5)||Z||, so ||L_W Z||>=(4/7)||Z|| and ||L_W^{-1}||<=7/4. All inequalities use only e<1/6 from node 1.2 and exact unitality.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Product defect, using nodes 1.2 and 1.3. Put X:=U bold-dot V. The star rule gives X^dagger=V^dagger bold-dot U^dagger. Insert ((V^dagger bold-dot U^dagger) bold-dot U) bold-dot V and (V^dagger bold-dot (U^dagger bold-dot U)) bold-dot V between X^dagger bold-dot X and J. The two approximate-associativity errors are each at most e*(1+e)||U||^2||V||^2, and the final expression is (V^dagger bold-dot J) bold-dot V=V^dagger bold-dot V=J. Hence ||X^dagger bold-dot X-J||<=2e(1+e)/(1-e)^2<=4e<t<2t, where e<1/6 and t>4e are exactly node 1.2.

**Type:** claim

**Inference:** triangle_inequality

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Product right inverse, using nodes 1.2 and 1.3. Approximate associativity gives ||L_{U bold-dot V}-L_U L_V||<=e||U||||V||<=e/(1-e)<1/5. The operator A:=L_U L_V is invertible and ||A^{-1}||<=||L_V^{-1}||||L_U^{-1}||<=49/16, so ||A^{-1}(L_{U bold-dot V}-A)||<49/80<1. The Neumann lemma makes L_{U bold-dot V}=A[I+A^{-1}(L_{U bold-dot V}-A)] invertible. Therefore R_X:=L_{U bold-dot V}^{-1}J satisfies (U bold-dot V) bold-dot R_X=J and is a right inverse of U bold-dot V.

**Type:** claim

**Inference:** neumann_perturbation

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Adjoint input, using nodes 1.2 and 1.3. Def-approximate-unitary-space gives U^dagger bold-dot U=J, so U is a right inverse of U^dagger. Let R be the right inverse of U supplied by that same definition. Since L_U is bijective by node 1.3, R=L_U^{-1}J and ||R||<=7/4. Exact unitality and one associator estimate give ||U^dagger-R||=||U^dagger bold-dot(U bold-dot R)-(U^dagger bold-dot U) bold-dot R||<=e||U||^2||R||. Consequently ||U bold-dot U^dagger-J||=||U bold-dot(U^dagger-R)||<=(1+e)e||U||^3||R||<=4e<t<2t; the numerical coefficient is at most (7/6)*(6/5)^3*(7/4)=441/125<4 by e<1/6. Thus U^dagger has the required strict defect bound and an explicit right inverse.

**Type:** claim

**Inference:** associator_estimate

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Membership conclusion. Nodes 1.4 and 1.5 give ||(U bold-dot V)^dagger bold-dot(U bold-dot V)-J||<2t together with a right inverse, so def-approximate-unitary-space gives U bold-dot V in calU_t. Node 1.6 gives the same two defining properties for U^dagger, hence U^dagger is in calU_t. This also records the right inverses required separately by the root contract.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Apply the registered external lem-stage1-polar-retraction with the constants fixed in node 1.1. Its guard is the first root guard and node 1.2 gives t>0; its inner inclusion calU_t subseteq S_delta and node 1.7 therefore put U bold-dot V and U^dagger in S_delta. Hence the inverse component u_delta:S_delta->calU is defined at both points. Their right inverses were constructed in nodes 1.5 and 1.6. Since the algebra, delta, U, and V were arbitrary, the witnesses C_grp=4 together with C_pol,kappa_pol prove the root contract.

**Type:** qed

**Inference:** existential_generalization

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Endpoint-safe replacement for the endpoint-sensitive portions of nodes 1.3--1.6 (those earlier strict chains are not used here), using only validated nodes 1.1 and 1.2 and the registered definitions. For W in calU, W^dagger bold-dot W=J and (1-e)||W||^2<=1. Exact unitality and the associator axiom give ||L_{W^dagger}L_W-I||<=e||W||^2<=e/(1-e)<1/5. Hence, weakening all consequent bounds non-strictly, ||L_{W^dagger}L_W Z||>=(4/5)||Z|| and ||L_{W^dagger}||<=(1+e)||W||<=7/5, so ||L_W Z||>=(4/7)||Z||; finite dimensionality makes L_W bijective and ||L_W^{-1}||<=7/4. For X:=U bold-dot V, two associator estimates and U^dagger bold-dot U=V^dagger bold-dot V=J yield ||X^dagger bold-dot X-J||<=2e(1+e)/(1-e)^2<=4e<t<2t. Also ||L_X-L_U L_V||<=e||U||||V||<=e/(1-e)<=1/5, while ||(L_U L_V)^{-1}||<=49/16; thus the perturbation norm is <=49/80<1, L_X is invertible, and L_X^{-1}J is a right inverse of X. Finally let R be the right inverse of U supplied by calU. The preceding bijectivity gives R=L_U^{-1}J and ||R||<=7/4. Since U bold-dot R=J and U^dagger bold-dot U=J, one associator estimate gives ||U^dagger-R||<=e||U||^2||R||, hence ||U bold-dot U^dagger-J||<=(1+e)e||U||^3||R||<=4e<t<2t; U is a right inverse of U^dagger. (The coefficient bounds use only e<1/6 from node 1.2: ||W||<=6/5, 2(1+e)/(1-e)^2<=4, and (1+e)(6/5)^3(7/4)<=441/125<4.) Thus X and U^dagger lie in calU_t with explicit right inverses. By the inner inclusion calU_t subseteq S_delta from node 1.1, u_delta is defined at both. Every defect/operator estimate up to its constant multiple is <=, including when e=0; the only variable-dependent strict passage is 4e=C_grp*e<t (followed by t<2t because t>0). This independently proves the root without the challenged strict inferences.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

