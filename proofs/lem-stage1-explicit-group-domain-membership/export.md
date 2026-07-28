# Proof Export

## Node 1

**Statement:** Explicit group-input polar-domain membership: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU is defined at U bold-dot V and U^dagger for every U, V in calU; moreover, U bold-dot V and U^dagger each have a right inverse.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Invoke the registered external lem-stage1-polar-retraction and choose its universal constants C_pol >= 1 and kappa_pol in (0,1/2]; choose the further universal witness C_grp:=4. These constants are fixed for the rest of the proof.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix an arbitrary finite-dimensional exact-unit epsilon_r-C*-algebra and delta>0 satisfying the two root guards. Apply lem-stage1-polar-retraction under the first guard to obtain the displayed C^1 diffeomorphism Pi_delta:calU x B_delta^{calH}(J)->S_delta and, before choosing any group inputs, bind its unique typed inverse pair (u_delta,h_delta):S_delta->calU x B_delta^{calH}(J). Put e:=epsilon_r and t:=delta-C_pol*(e*delta+delta^2). The external gives the inner inclusion calU_t subseteq S_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Now fix arbitrary U,V in calU. Guard arithmetic gives s:=e+delta<=1/2, t>4e>=0, delta<=1/2, and e<1/6: indeed C_pol*s<=kappa_pol<=1/2 with C_pol>=1 gives s<=1/2, while the second guard gives 4e<t; also t=delta-C_pol*delta*s<=delta*(1-s)=(s-e)*(1-s), whose maximum for e<=s<=1/2 is (1/2-e)/2, so e<t<=(1/2-e)/2 implies e<1/6.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Common left-multiplier estimate, using the preceding guard node: for every W in calU, def-approximate-unitary-space gives W^dagger bold-dot W=J and a right inverse, while def-epsilon-cstar-algebra gives (1-e)||W||^2<=1 and ||L_{W^dagger}L_W-I||<=e||W||^2<=e/(1-e)<1/5. Hence L_W is injective and, since calX is finite-dimensional, bijective. Moreover ||W||<=6/5, ||L_{W^dagger}||<=(1+e)||W||<=7/5, and ||L_{W^dagger}L_W Z||>=(4/5)||Z||, so ||L_W Z||>=(4/7)||Z|| and ||L_W^{-1}||<=7/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Product defect: put X:=U bold-dot V. The star rule gives X^dagger=V^dagger bold-dot U^dagger. Two applications of the approximate-associativity axiom, inserting ((V^dagger bold-dot U^dagger) bold-dot U) bold-dot V and (V^dagger bold-dot (U^dagger bold-dot U)) bold-dot V, and then U^dagger bold-dot U=V^dagger bold-dot V=J, give ||X^dagger bold-dot X-J||<=2e(1+e)||U||^2||V||^2<=2e(1+e)/(1-e)^2<=4e<t<2t. This uses only the registered definitions and the guard estimates above.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Product right inverse: approximate associativity gives ||L_X-L_U L_V||<=e||U||||V||<=e/(1-e)<1/5. The operator A:=L_U L_V is invertible by the common multiplier node and ||A^{-1}||<=49/16, so ||A^{-1}(L_X-A)||<49/80<1. The Neumann perturbation lemma makes L_X invertible; therefore R_X:=L_X^{-1}J satisfies X bold-dot R_X=J and is a right inverse of X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Bind e:=epsilon_r and X:=U bold-dot V locally, with U,V in calU fixed by the parent context. The root guards imply e<1/6: setting s:=e+delta and t:=delta-C_pol*delta*s, one has s<=1/2 and 4e<t<=delta*(1-s)=(s-e)*(1-s)<=(1/2-e)/2, hence e<1/6. For any W in calU, W^dagger bold-dot W=J by def-approximate-unitary-space, while the C*-lower bound and exact unit give (1-e)||W||^2<=||W^dagger bold-dot W||=1, so ||W||^2<=1/(1-e) and ||W||<6/5. Approximate associativity gives ||L_{W^dagger}L_W-I||<=e||W||^2<=e/(1-e)<1/5. Thus L_W is injective (if L_W Z=0, then ||Z||<=(e/(1-e))||Z||), hence bijective in finite dimension. Also ||L_{W^dagger}||<=(1+e)||W||<7/5 and ||L_{W^dagger}L_W Z||>(4/5)||Z||, whence ||L_W Z||>(4/7)||Z|| and ||L_W^{-1}||<=7/4. Applying this self-contained derivation to W=U,V, A:=L_U L_V is invertible with A^{-1}=L_V^{-1}L_U^{-1} and ||A^{-1}||<=49/16. Approximate associativity and ||U||||V||<=1/(1-e) give ||L_X-A||<=e||U||||V||<=e/(1-e)<1/5. Therefore ||A^{-1}(L_X-A)||<49/80<1. By the Neumann lemma, A^{-1}L_X=I+A^{-1}(L_X-A), hence L_X, is invertible. Consequently R_X:=L_X^{-1}J satisfies X bold-dot R_X=L_X(R_X)=J, so X has the required right inverse.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Adjoint defect and right inverse: def-approximate-unitary-space gives U^dagger bold-dot U=J, so U is already a right inverse of U^dagger. Let R be the right inverse of U supplied by that definition. Bijectivity of L_U from the common multiplier node gives R=L_U^{-1}J and ||R||<=7/4. Exact unitality and one associator estimate yield ||U^dagger-R||=||U^dagger bold-dot(U bold-dot R)-(U^dagger bold-dot U) bold-dot R||<=e||U||^2||R||. Hence ||U bold-dot U^dagger-J||<= (1+e)e||U||^3||R||<=4e<t<2t, using e<1/6, ||U||<=6/5, and (7/6)*(6/5)^3*(7/4)=441/125<4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** The product-defect and product-right-inverse nodes show X=U bold-dot V lies in calU_t by def-approximate-unitary-space. The adjoint node shows U^dagger lies in calU_t, because its defining defect is ||(U^dagger)^dagger bold-dot U^dagger-J||=||U bold-dot U^dagger-J||<2t and U is its right inverse. Thus both required right inverses are also explicitly recorded.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** By the typed polar data bound before the group inputs, lem-stage1-polar-retraction supplies calU_t subseteq S_delta. The preceding membership node therefore puts U bold-dot V and U^dagger in the domain S_delta of the already bound map u_delta:S_delta->calU, so u_delta is defined at both points. Since the algebra, delta, U, and V were arbitrary, C_grp=4 together with the external C_pol,kappa_pol proves every clause of the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.9.1

**Statement:** By validated node 1.2, for t:=delta-C_pol*(epsilon_r*delta+delta^2), the already bound inverse has first component u_delta:S_delta->calU and the polar external gives calU_t subseteq S_delta. By validated node 1.8, U bold-dot V and U^dagger both lie in calU_t, and it also establishes that each has a right inverse. Hence the inclusion places both points in S_delta, so the fixed map u_delta is defined at both. Together with the universal choices C_grp=4 and C_pol,kappa_pol from validated node 1.1, and the arbitrary algebra, delta, U,V fixed in validated nodes 1.2-1.3, this proves every clause of the root contract.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.9.2

**Statement:** By node 1.2, with t:=delta-C_pol*(epsilon_r*delta+delta^2), the inverse pair was bound before U,V and its first component is u_delta:S_delta->calU, while calU_t subseteq S_delta. Node 1.8 proves U bold-dot V in calU_t and U^dagger in calU_t and proves that each point has a right inverse. Therefore U bold-dot V and U^dagger belong to S_delta, so the already bound u_delta is defined at both. Node 1.1 supplies the universal choices C_grp=4 and C_pol,kappa_pol, and nodes 1.2-1.3 supply the arbitrary guarded algebra, delta, U,V; universal generalization now yields every clause of the root contract.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

