# Proof Export

## Node 1

**Statement:** Canonical Ha inverse estimate: there are universal C_sp,inv < infinity and e_sp,inv > 0 such that every H-CB datum with e <= e_sp,inv has the special maps Ha^Q_{P,Q} and Ha^Q_{Q,P} completely bijective, with their amplified inverses differing from the corresponding canonical inverses by at most C_sp,inv*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix universal constants C_J,e_J and C_sp,e_sp supplied respectively by lem-hcb4-canonical-gram and lem-hcb4-canonical-closeness, and set e_sp,inv=min{e_J,e_sp,1/[4(C_J+C_sp+1)]} and C_sp,inv=4(C_sp+1). For every H-CB datum with e<=e_sp,inv, every n>=1, and each of the two special ordered corners (P,Q) and (Q,P), the corresponding canonical amplification J_n is bijective and satisfies ||J_n^{-1}||<=4/3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For either special corner and every n, the canonical map J_n is the amplified coefficient-space identification (column map or adjoint row map) of def-canonical-corner-identifications, hence is an algebraic linear bijection onto its indicated operator corner and has the corresponding canonical inverse.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By lem-hcb4-canonical-gram, ||J_n Z|| >= (1-C_J e)||Z|| for all Z; since e<=1/[4(C_J+C_sp+1)], one has C_J e<=1/4, so applying this inequality to Z=J_n^{-1}Y gives ||J_n^{-1}Y||<=4||Y||/3 and therefore ||J_n^{-1}||<=4/3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Quantitative Neumann step for the present special corners (whose target space Y is Banach): if J:X->Y is a bounded bijection with ||J^{-1}||<=4/3 and A:X->Y satisfies ||A-J||<=C_sp e and C_sp e<=1/4, then A is bijective and ||A^{-1}-J^{-1}||<=(8/3)C_sp e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Put T=(A-J)J^{-1}:Y->Y. Then A=(I_Y+T)J and ||T||<=||A-J|| ||J^{-1}||<=(4/3)C_sp e<=1/3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For either special corner at every fixed n, the target Y is Banach. Hence B(Y) is Banach, and ||T||<=1/3<1 makes the Neumann series sum_{k>=0}(-T)^k converge in B(Y) to the two-sided inverse of I_Y+T, with ||(I_Y+T)^{-1}||<=1/(1-||T||)<=3/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Completeness of the actual targets follows from closedness of the compressed corner, not merely from its inner-product display.  In an H-CB datum, A is complete and the corresponding compressed corner is S_{P,Q}=Img(Co_{P,Q})=Ker(I-Co_{P,Q}), where Co_{P,Q} is a bounded idempotent; hence S_{P,Q} is Banach in the inherited norm.  At n=1, lem-hcb4-canonical-gram and the formula J_{P,Q,1}(Z)c=Zc identify ||J_{P,Q,1}(Z)|| with the Euclidean norm ||Z||_Euc and give (1-C_J e)||Z||<=||Z||_Euc<=(1+C_J e)||Z||, so for C_J e<=1/4 the Euclidean norm is equivalent to the complete inherited norm.  Thus S_{P,Q} is complete for ||.||_Euc, its finite Hilbertian sum C^n tensor S_{P,Q} is complete, and both B(C^n,C^n tensor S_{P,Q}) and B(C^n tensor S_{P,Q},C^n), the column and row targets from def-ha-map and def-canonical-corner-identifications, are Banach.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.1.1

**Statement:** Closed-corner completeness in the inherited norm: the extended epsilon-C*-algebra A in def-hcb-datum is complete.  For its corresponding compressed corner, Co_{P,Q} is the bounded compression idempotent on A and S_{P,Q}=Img(Co_{P,Q})=Ker(I-Co_{P,Q}).  Since I-Co_{P,Q} is continuous, its kernel is closed in A; a closed subspace of the Banach space A is Banach, so S_{P,Q} is complete in the inherited norm.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.1.1.1

**Statement:** The missing input is now explicitly provisioned in this workspace as the registered definition def-compressed-corner (AF definition id c76ab4d9feb7af17). Its byte-matched text states verbatim that Co_{P,Q}: A -> A satisfies Co_{P,Q}^2=Co_{P,Q} and that S_{P,Q}=Img(Co_{P,Q})=Ker(1-Co_{P,Q}) is a closed linear subspace of A. Thus this step does not infer closedness merely from operator-algebra-theta-framing or from def-hcb-datum; it invokes def-compressed-corner directly.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.1.1.2

**Statement:** The registered definition def-extended-epsilon-cstar-algebra states that A is complete. Hence the closed linear subspace S_{P,Q} supplied by def-compressed-corner is complete in the inherited norm (if a sequence in S_{P,Q} is Cauchy, it converges in A, and closedness puts its limit back in S_{P,Q}). Therefore S_{P,Q} is Banach in the inherited norm.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.1.2

**Statement:** Transfer to the Euclidean norm: at level n=1, def-canonical-corner-identifications gives J_{P,Q,1}(Z)c=Zc, so the target operator norm induced by def-ha-map is ||J_{P,Q,1}(Z)||=||Z||_Euc.  Applying lem-hcb4-canonical-gram with n=1 yields (1-C_J e)||Z||<=||Z||_Euc<=(1+C_J e)||Z||.  Here C_J e<=1/4, so the two norms are equivalent.  Therefore every Euclidean-Cauchy sequence is inherited-norm Cauchy, converges in S_{P,Q} by the preceding closedness, and the upper comparison makes it converge Euclideanly; hence (S_{P,Q},||.||_Euc) is complete.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.1.3

**Statement:** The registered coordinate-sum inner-product display makes C^n tensor S_{P,Q} the finite Hilbertian direct sum of n copies of the now-complete Euclidean space S_{P,Q}; it is therefore complete.  For normed E and Banach F, B(E,F) is Banach: an operator-norm Cauchy sequence converges pointwise in F, and the pointwise limit is bounded and is the operator-norm limit.  Taking (E,F)=(C^n,C^n tensor S_{P,Q}) and (C^n tensor S_{P,Q},C^n) proves that both actual targets are Banach.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Let S_N=sum_{k=0}^N(-T)^k in the Banach algebra B(Y). The bound sum_{k>=0}||T||^k<=1/(1-||T||) shows that (S_N) converges in B(Y) to some S with ||S||<=1/(1-||T||). The finite geometric identities (I_Y+T)S_N=S_N(I_Y+T)=I_Y-(-T)^{N+1}, followed by ||T||^{N+1}->0, give (I_Y+T)S=S(I_Y+T)=I_Y. Thus S=(I_Y+T)^{-1}, and ||T||<=1/3 gives ||S||<=3/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** From A^{-1}=J^{-1}(I_Y+T)^{-1} and (I_Y+T)^{-1}-I_Y=-(I_Y+T)^{-1}T, conclude ||A^{-1}-J^{-1}||<= (4/3)(3/2)(4/3)C_sp e=(8/3)C_sp e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Apply the preceding two facts and lem-hcb4-canonical-closeness at every matrix level to both special Ha maps; this proves complete bijectivity and the uniform inverse-difference bound required by node 1 with the displayed universal constants.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For a fixed n and either special corner, lem-hcb4-canonical-closeness gives ||A_n-J_n||<=C_sp e, while node 1.1 gives that J_n is bijective with ||J_n^{-1}||<=4/3; moreover e<=1/[4(C_J+C_sp+1)] implies C_sp e<=1/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Node 1.2 therefore makes A_n bijective and yields ||A_n^{-1}-J_n^{-1}||<=(8/3)C_sp e<=4(C_sp+1)e=C_sp,inv e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** The argument holds for every n>=1 with the same constants and for A_n=(Ha^Q_{P,Q})_n and A_n=(Ha^Q_{Q,P})_n; hence both special Ha maps are completely bijective and their amplified inverses obey the asserted uniform estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

