# Proof Export

## Node 1

**Statement:** There is a universal e_zero > 0 such that, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state has w:C^m->A a non-unital extended t-inclusion with one-dimensional images P_j, U,V are disjoint nonempty unions sharing no equivalence class, R = U union V, and t <= e_zero, then dim S^A_{P_U,P_V} = dim S^A_{P_V,P_U} = 0 and dim S^{A_R}_{P_U^R,P_V^R} = dim S^{A_R}_{P_V^R,P_U^R} = 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let e_add>0 be a universal accuracy threshold at which lem-extcb-corner-dimension-additivity applies, and set e_zero=min{e_sim,e_add,e_ncd,1/2}, where e_sim and e_ncd are the universal constants in lem-maincb-corner-equivalence and lem-maincb-nested-corner-dimension-transport. Then e_zero>0 is universal, and t<=e_zero implies all three external lemmas are applicable and t<1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Apply lem-maincb-corner-equivalence to the one-dimensional t-projections (P_j): P_j=w(e_j) is a t-projection because e_j^2=e_j and the extended t-inclusion has t-multiplicative defect. Hence the relation j~k iff dim S^A_{P_j,P_k}=1 is an equivalence relation. Since U and V are disjoint unions sharing no equivalence class, for every j in U and k in V one has j not~k and k not~j, and therefore dim S^A_{P_j,P_k} != 1 and dim S^A_{P_k,P_j} != 1. No zero-dimensional conclusion follows from the allowed inputs alone.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For every j, P_j=w(e_j) is a t-projection: the projection identity e_j^2=e_j and the t-multiplicative-defect bound for w give ||P_j^2-P_j||<=t, while the self-adjointness clause for the inclusion gives the required Hermitian condition. Since t<=e_zero<=e_sim, lem-maincb-corner-equivalence applies and makes j~k iff dim S^A_{P_j,P_k}=1 an equivalence relation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** If j is in U and k is in V, then j and k lie in distinct equivalence classes because U and V are disjoint unions sharing no class. Thus j not~k and, by symmetry, k not~j. By the defining biconditional for ~, dim S^A_{P_j,P_k}!=1 and dim S^A_{P_k,P_j}!=1. This does not imply either dimension is zero: excluding dimensions at least two requires the separate one-dimensional-corner-dimension theorem, which is not an allowed external input in this workspace.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Restrict w to the coordinate commutative C*-algebras C^U and C^V. These restrictions remain non-unital extended t-inclusions, take their units to P_U and P_V, and take their projection bases to (P_j)_{j in U} and (P_k)_{k in V}. By lem-extcb-corner-dimension-additivity and the atomwise zero dimensions, dim S^A_{P_U,P_V}=sum_{j in U,k in V} dim S^A_{P_j,P_k}=0; interchanging U,V gives dim S^A_{P_V,P_U}=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Put P_R=w(e_R)=P_U+P_V for R=U union V. Because epsilon_A<=t, A satisfies the extended t-C*-bounds. The elements P_U,P_V,P_R are t-projections; P_R is nonvanishing; and all four left/right subordination errors of P_U,P_V to P_R are at most t. The supplied def-maincb-partition-state gives A_R=S^A_{P_R}. Introduce locally P_U^R:=Co^A_{P_R}(P_U) and P_V^R:=Co^A_{P_R}(P_V); these are the exact compression equalities required by lem-maincb-nested-corner-dimension-transport, rather than notation asserted by def-maincb-partition-state.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Let e_R be the coordinate projection of C^m associated to the nonempty set R=U union V, and put P_R=w(e_R). At level one, the extended t-inclusion w is a t-homomorphism and satisfies the two-sided (1 plus-or-minus t) norm bounds. Since e_R is Hermitian and e_R^2=e_R, involution preservation and the multiplicative-defect axiom give P_R^dagger=P_R and ||P_R^2-P_R||<=t||e_R||^2=t; hence P_R is a t-projection by def-delta-projection. Also ||e_R||=1, so 1-t<=||P_R||<=1+t and therefore | ||P_R||-1 |<=t<=t+epsilon_A. This is the second alternative in def-delta-projection with explicit universal O-constant 1, so P_R is nonvanishing in the sense required by lem-maincb-nested-corner-dimension-transport.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** At amplification n=1, def-extended-delta-inclusion says that w is a t-homomorphism. Thus w preserves the involution and ||w(xy)-w(x)w(y)||<=t||x||||y||. For the coordinate projection e_R one has e_R^dagger=e_R, e_R^2=e_R, and, because R is nonempty, ||e_R||=1. Consequently P_R^dagger=w(e_R)^dagger=w(e_R^dagger)=P_R and ||P_R^2-P_R||=||w(e_R)w(e_R)-w(e_R^2)||<=t. Hence P_R is a t-projection. The two-sided norm bounds of the same inclusion give 1-t<=||P_R||<=1+t, whence | ||P_R||-1 |<=t<=t+epsilon_A. Therefore P_R satisfies the nonvanishing second alternative of def-delta-projection with universal coefficient 1, independently of the pending parent node.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Let e_U,e_V be the coordinate projections of C^m associated to U,V. At level one, def-extended-delta-inclusion says that w preserves the involution and has t-multiplicative defect, so P_U=w(e_U) and P_V=w(e_V) are t-projections. Since e_Ue_R=e_Re_U=e_U and e_Ve_R=e_Re_V=e_V, the four quantities ||P_UP_R-P_U||, ||P_RP_U-P_U||, ||P_VP_R-P_V||, and ||P_RP_V-P_V|| are at most t. The supplied def-maincb-partition-state gives A_R=S^A_{P_R}. Introduce the local notation P_U^R:=Co^A_{P_R}(P_U) and P_V^R:=Co^A_{P_R}(P_V); these are exactly the defining equalities required as hypotheses by lem-maincb-nested-corner-dimension-transport. No independent claim that compression preserves approximate projections is made or needed: the transport lemma itself is the permitted result whose conclusion is the asserted corner-dimension equality for these compressed elements.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Apply lem-maincb-nested-corner-dimension-transport first to (P_R,P_U,P_V) and then to (P_R,P_V,P_U), using the hypotheses established above. Together with the two ambient zero dimensions, this gives dim S^{A_R}_{P_U^R,P_V^R}=0 and dim S^{A_R}_{P_V^R,P_U^R}=0. Hence all four dimension equalities asserted by node 1 hold with the universal e_zero chosen above.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Shrink the final constant further to e_zero=min{e_sim,e_add,e_ncd,e_rank,1/2}, where the universal e_rank is chosen below. For any atom pair P=P_j,Q=P_k, the registered one-dimensional-projection definition gives dim S_P=dim S_Q=1. We prove dim S_{P,Q}<=1 using only the registered compression estimates. All O(t+epsilon_A) bounds below have universal constants and are O(t) since epsilon_A<=t. If S_{P,Q}=0 there is nothing to prove. Otherwise choose X in S_{P,Q} with ||X||=1 and put p~=Co_P(P), q~=Co_Q(Q). Because P,Q are images of norm-one coordinate projections under the extended t-inclusion, ||P|| and ||Q|| are bounded above and below by 1+O(t). From Z=Co_{P,Q}(Z), the estimates of Co_{P,Q} against both L_P R_Q and R_Q L_P, approximate associativity, and ||P^2-P||,||Q^2-Q||<=t give, uniformly for Z in S_{P,Q}, ||PZ-Z||+||ZQ-Z||<=C_1 t||Z||. The same compression estimates give ||p~-P||+||q~-Q||<=C_2t and hence ||p~ dot Z-Z||+||Z dot q~-Z||<=C_3t||Z||, where dot is the registered compressed product. Comparing each compressed product with the ambient product and using ambient approximate associativity also gives ||(Y dot W) dot Z-Y dot(W dot Z)||<=C_4t||Y||||W||||Z|| for the matching corners used here. Now B=X dot X^dagger lies in the one-dimensional S_P, so B=beta p~. The C*-lower bound applied to X^dagger gives ||XX^dagger||>=(1-epsilon_A)||X||^2, while compressed-product closeness gives ||B-XX^dagger||<=C_5t. Since ||p~|| is universally bounded, after decreasing e_rank we obtain |beta|>=c>0. For arbitrary Z in S_{P,Q}, write X^dagger dot Z=gamma(Z)q~; gamma is linear and |gamma(Z)|<=C_6||Z|| because ||q~|| is bounded below. The preceding unit and associator estimates yield ||beta Z-gamma(Z)X||<=C_7t||Z||. Thus T:Z↦beta^{-1}gamma(Z)X has rank at most one and ||I-T||<=C_7t/c. Choose the universal e_rank so that C_7e_rank/c<1. Then T is invertible by the Neumann lemma, and therefore dim S_{P,Q}<=rank(T)<=1. The adjoint identity Co_{P,Q}(Y)^dagger=Co_{Q,P}(Y^dagger) is a conjugate-linear bijection S_{P,Q}->S_{Q,P}, so the reverse corner also has dimension at most one. Applying this to every j in U,k in V and combining it with validated node 1.2.2, which excludes dimension one, gives dim S_{P_j,P_k}=dim S_{P_k,P_j}=0. The allowed corner-dimension additivity lemma now gives both ambient union-corner dimensions zero. Finally, validated node 1.4 supplies every hypothesis of nested-corner dimension transport, so applying that allowed lemma in both orders transports these two zeros to A_R and proves the four conclusions of node 1.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

