# Proof Export

## Node 1

**Statement:** Level-one corner-dimension additivity: for two finite-dimensional commutative C*-algebras with projection bases and non-unital sufficiently accurate inclusions v,w, the compressed corner S_{v(I),w(I)} is linearly bijective to the direct sum over j,k of S_{v(Pi_j),w(Sigma_k)}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Setup and image relations: writing P_j=v(Pi_j), Q_k=w(Sigma_k), P_[1,j]=sum_{r<=j}P_r, and Q_[1,k]=sum_{s<=k}Q_s, every P_j,Q_k and every partial sum is a uniformly accurate Hermitian projection; P_[1,j]=P_[1,j-1]+P_j and Q_[1,k]=Q_[1,k-1]+Q_k exactly; and each new summand is uniformly approximately orthogonal to the preceding partial sum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** In each exact commutative source algebra, every basis projection and every partial sum of basis projections is a Hermitian norm-one projection, distinct basis projections multiply to zero, and the full partial sum is the unit; this follows directly from def-projection-basis.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By def-extended-delta-inclusion, v and w are linear, star-preserving, delta-multiplicative and satisfy two-sided norm bounds. Hence the image of any source projection E is Hermitian, has norm at most 1+delta, and satisfies ||v(E)^2-v(E)||<=delta (and similarly for w).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** For E_[1,j-1]=sum_{r<j}Pi_r and Pi_j, exact source orthogonality and delta-multiplicativity give ||P_[1,j-1]P_j||<=delta; star preservation gives the reverse-product bound. Linearity gives P_[1,j]=P_[1,j-1]+P_j and P_[1,p]=v(I_B). The identical argument gives all Q relations.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Binary first-index splitting lemma: there is a universal accuracy threshold such that, whenever R_0,R_1,T are uniformly bounded approximate projections, R=R_0+R_1 is an approximate projection, and R_0,R_1 are approximately orthogonal, the canonical assembly map A:S_{R_0,T} direct-sum S_{R_1,T}->S_{R,T}, A(X_0,X_1)=Co_{R,T}(X_0+X_1), is a bounded linear bijection.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Define A(X_0,X_1)=Co_{R,T}(X_0+X_1) and B(X)=(Co_{R_0,T}X,Co_{R_1,T}X). By def-compressed-corner, every Co is a bounded linear idempotent with the displayed corner as its closed range, so A and B are well-defined bounded linear maps between Banach spaces.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Uniform two-block compression calculus: with e the maximum of the ambient associativity/product-norm error, all projection defects, and the two orthogonality defects, there is a universal C such that ||BA-I||<=C e on S_{R_0,T} direct-sum S_{R_1,T} with the max norm.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** From def-compressed-corner there is a universal c_co such that Co_{U,V} differs from each parenthesization U(XV) and (UX)V by at most c_co e||X|| whenever U,V have the stated projection accuracy; hence X in S_{U,V} implies X=U(XV)+O(e)||X||. The epsilon-C*-algebra product bound, associator bound, involution, and uniform bounds on the projections permit all fixed-length replacements below with one universal accumulated constant.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** If X_i lies in S_{R_i,T}, then R_i(X_iT)=X_i+O(e)||X_i||. Expanding R=R_0+R_1, the wanted term remains and the other term is O(e)||X_i|| because R_{1-i}R_i=O(e) and one reassociation costs O(e). Therefore Co_{R,T}X_i=X_i+O(e)||X_i||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.3

**Statement:** For a in {0,1}, applying Co_{R_a,T} to Co_{R,T}X_i and using the previous approximation, compression replacement, and R_a R_i=delta_{ai}R_i+O(e), gives Co_{R_a,T}Co_{R,T}X_i=delta_{ai}X_i+O(e)||X_i||. Summing i=0,1 and using the max norm yields ||BA-I||<=C e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** The same uniform compression calculus gives ||AB-I||<=C e on S_{R,T}, after increasing the same universal C if necessary.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** For X in S_{R,T}, compression replacement gives X=R(XT)+O(e)||X||. For i=0,1 it also gives Co_{R_i,T}X=R_i(XT)+O(e)||X||; uniform boundedness of R_i,T and Co_{R_i,T} follows from the epsilon-C*-algebra product bound and the compression estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** Adding the two extraction formulas and using R_0+R_1=R gives Co_{R_0,T}X+Co_{R_1,T}X=X+O(e)||X||. Applying the bounded Co_{R,T}, and using Co_{R,T}X=X exactly, yields ABX=X+O(e)||X|| and thus ||AB-I||<=C e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Choose the universal accuracy threshold so C e<1. The Neumann series invert BA and AB; consequently (BA)^(-1)B is a left inverse of A and B(AB)^(-1) is a right inverse. A map with a left and right inverse has the two inverses equal, so A is a bounded linear bijection.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Binary second-index splitting lemma: under the analogous hypotheses T=T_0+T_1 with T_0,T_1 approximately orthogonal, the canonical map S_{R,T_0} direct-sum S_{R,T_1}->S_{R,T} is a bounded linear bijection.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By def-compressed-corner, J_{U,V}:S_{U,V}->S_{V,U}, J(X)=X^dagger, is a conjugate-linear isometric bijection because Co_{U,V}(X)^dagger=Co_{V,U}(X^dagger) and the involution is isometric.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Apply node 1.2 to the first-index split T=T_0+T_1 with fixed second index R. Conjugating its assembly bijection by J on both domain and codomain produces a complex-linear bounded bijection S_{R,T_0} direct-sum S_{R,T_1}->S_{R,T}; two conjugate-linear maps surrounding a complex-linear map give a complex-linear map, and the displayed compression-adjoint identity identifies it with the canonical second-index assembly map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Let A_L:S_{T_0,R} direct-sum S_{T_1,R}->S_{T,R} be the first-index assembly map from node 1.2 for the split T=T_0+T_1. This child explicitly depends on node 1.2 and requires node 1.2 to be validated before acceptance. By node 1.3.1, J_D(X_0,X_1)=(X_0^dagger,X_1^dagger) and J_C(Y)=Y^dagger are conjugate-linear isometric bijections from S_{R,T_0} direct-sum S_{R,T_1} to S_{T_0,R} direct-sum S_{T_1,R}, and from S_{T,R} to S_{R,T}, respectively. Thus C=J_C composed with A_L composed with J_D is a bounded complex-linear bijection. For every (X_0,X_1), the compression-adjoint identity gives C(X_0,X_1)=Co_{T,R}(X_0^dagger+X_1^dagger)^dagger=Co_{R,T}(X_0+X_1). Hence C is exactly the canonical second-index assembly map; no bijectivity is asserted before the required validation of node 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For each fixed j, repeated binary second-index splitting along Q_[1,k]=Q_[1,k-1]+Q_k gives a bounded linear bijection S_{P_j,Q}->direct-sum_k S_{P_j,Q_k}, where Q=w(I_C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Base k=1 is the identity S_{P_j,Q_1}->S_{P_j,Q_1}. For k>=2, node 1.1 supplies Q_[1,k]=Q_[1,k-1]+Q_k with uniform projection and orthogonality bounds, so node 1.3 gives S_{P_j,Q_[1,k]} linearly bijective to S_{P_j,Q_[1,k-1]} direct-sum S_{P_j,Q_k}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** For k=1, Q_[1,1]=Q_1 by the exact partial-sum identity, and the identity operator on S_{P_j,Q_1} is a bounded complex-linear bijection onto itself.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.2

**Statement:** Fix k>=2. Once nodes 1.1 and 1.3 are validated, instantiate node 1.3 with R=P_j, T_0=Q_[1,k-1], T_1=Q_k, and T=Q_[1,k]. Node 1.1 supplies every hypothesis of that instance: R,T_0,T_1,T are uniformly accurate Hermitian projections, T=T_0+T_1 exactly, and T_0,T_1 are uniformly approximately orthogonal. Hence the canonical second-index assembly map S_{P_j,Q_[1,k-1]} direct-sum S_{P_j,Q_k} -> S_{P_j,Q_[1,k]} is a bounded complex-linear bijection; its inverse gives the bijection in the direction stated in node 1.4.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Induction on the finite number q of basis projections, composing the step bijection with the preceding one and using Q_[1,q]=w(I_C), yields S_{P_j,Q}->direct-sum_{k=1}^q S_{P_j,Q_k}. A finite composition/direct sum of bounded linear bijections is a bounded linear bijection.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.1

**Statement:** For each integer m with 1<=m<=q, define D_m:S_{P_j,Q_[1,m]}->direct-sum_{k=1}^m S_{P_j,Q_k} recursively. Let D_1 be the identity (using Q_[1,1]=Q_1). For m>=2, let B_m:S_{P_j,Q_[1,m]}->S_{P_j,Q_[1,m-1]} direct-sum S_{P_j,Q_m} be the bounded linear bijection supplied by node 1.4.1, and put D_m=(D_{m-1} direct-sum id) composed with B_m. Induction gives a bounded linear bijection D_m: the direct sum of two bounded linear maps is bounded for the max norm, composition preserves boundedness, and an explicit bounded inverse is B_m^{-1} composed with (D_{m-1}^{-1} direct-sum id).

**Type:** claim

**Inference:** finite_induction

**Status:** validated

**Taint:** clean

##### Node 1.4.2.2

**Statement:** Taking m=q in node 1.4.2.1 and using node 1.1, linearity of w and sum_{k=1}^q Sigma_k=I_C imply Q_[1,q]=sum_k w(Sigma_k)=w(I_C)=Q. Substitution into D_q therefore gives the claimed bounded linear bijection S_{P_j,Q}->direct-sum_{k=1}^q S_{P_j,Q_k}.

**Type:** claim

**Inference:** substitution

**Status:** validated

**Taint:** clean

###### Node 1.4.2.2.1

**Statement:** Direct repair independent of pending node 1.4.2.1: for m=1 let D_1 be the identity S_{P_j,Q_[1,1]}=S_{P_j,Q_1}->S_{P_j,Q_1}, as in validated node 1.4.1.1. For each 2<=m<=q, validated node 1.4.1.2 supplies the canonical assembly A_m:S_{P_j,Q_[1,m-1]} direct-sum S_{P_j,Q_m}->S_{P_j,Q_[1,m]} as a bounded complex-linear bijection; let B_m=A_m^{-1}, also bounded. Recursively define D_m=(D_{m-1} direct-sum id) composed with B_m. With max norms on the finite direct sums, induction shows D_m is a bounded complex-linear bijection, since D_{m-1} direct-sum id and its inverse D_{m-1}^{-1} direct-sum id are bounded, and D_m^{-1}=B_m^{-1} composed with (D_{m-1}^{-1} direct-sum id). Finally, validated node 1.1, linearity of w, and sum_{k=1}^q Sigma_k=I_C give Q_[1,q]=sum_k w(Sigma_k)=w(I_C)=Q. Thus D_q is a bounded complex-linear bijection S_{P_j,Q}->direct-sum_{k=1}^q S_{P_j,Q_k}, proving the parent without using node 1.4.2.1.

**Type:** claim

**Inference:** finite_induction

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Repeated binary first-index splitting along P_[1,j]=P_[1,j-1]+P_j gives a bounded linear bijection S_{P,Q}->direct-sum_j S_{P_j,Q}; composing it with the finitely many fixed-j bijections gives S_{v(I_B),w(I_C)} linearly bijective to direct-sum_{j,k}S_{v(Pi_j),w(Sigma_k)}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Base j=1 is the identity. For each j>=2, a direct two-block compression argument with R_0=P_[1,j-1], R_1=P_j, R=P_[1,j], and T=Q gives a bounded linear bijection S_{R,T}->S_{R_0,T} direct-sum S_{R_1,T}; finite induction and P_[1,p]=v(I_B) then give S_{P,Q}->direct-sum_j S_{P_j,Q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.1

**Statement:** Fix j>=2 and put E_0=sum_{r<j} Pi_r, E_1=Pi_j, R_i=v(E_i), R=R_0+R_1=v(E_0+E_1)=P_[1,j], and T=Q=w(I_C). By def-projection-basis, E_0 and E_1 are Hermitian projections with E_0E_1=E_1E_0=0. By def-extended-delta-inclusion, linearity, star preservation, delta-multiplicativity, and the two-sided norm bound imply that R_0,R_1,R,T are Hermitian, uniformly bounded approximate projections and ||R_0R_1||,||R_1R_0||=O(delta). These bounds use one universal constant and are independent of j and of the number of basis projections.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.2

**Statement:** For these fixed R_0,R_1,R,T, equip S_{R_0,T} direct-sum S_{R_1,T} with the max norm and define A(X_0,X_1)=Co_{R,T}(X_0+X_1) and B(X)=(Co_{R_0,T}X,Co_{R_1,T}X). They are bounded linear maps by def-compressed-corner. Let e dominate the ambient epsilon, the four projection defects, and both orthogonality defects. The compression estimate in def-compressed-corner gives, uniformly, Y=U(YT)+O(e)||Y|| for Y in S_{U,T}. Thus for X_i in S_{R_i,T}, expansion of R=R_0+R_1 gives Co_{R,T}X_i=X_i+O(e)||X_i||: the R_i term reproduces X_i and the R_{1-i} term is O(e)||X_i|| after one reassociation and R_{1-i}R_i=O(e). Applying Co_{R_a,T}, using the same compression replacement and R_aR_i=delta_{ai}R_i+O(e), yields Co_{R_a,T}Co_{R,T}X_i=delta_{ai}X_i+O(e)||X_i||. Summing i and using the max norm proves ||BA-I||<=C_1 e for a universal C_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.3

**Statement:** For the fixed R_0,R_1,R,T from node 1.5.1.1, let e dominate the ambient epsilon, the four projection defects, and both orthogonality defects, and define A:S_{R_0,T} direct-sum S_{R_1,T}->S_{R,T} and B:S_{R,T}->S_{R_0,T} direct-sum S_{R_1,T} by A(X_0,X_1)=Co_{R,T}(X_0+X_1) and B(X)=(Co_{R_0,T}X,Co_{R_1,T}X). These are bounded linear maps by def-compressed-corner. For X in S_{R,T}, def-compressed-corner gives X=R(XT)+O(e)||X|| and Co_{R_i,T}X=R_i(XT)+O(e)||X||. Since R_0+R_1=R exactly, Co_{R_0,T}X+Co_{R_1,T}X=X+O(e)||X||. Therefore ABX=Co_{R,T}(Co_{R_0,T}X+Co_{R_1,T}X)=X+O(e)||X||, using uniform boundedness of Co_{R,T} and Co_{R,T}X=X exactly. Hence ||AB-I||<=C_2 e for a universal C_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.4

**Statement:** Choose the universal inclusion and ambient accuracy threshold so that C e<1 for C=max(C_1,C_2). Then BA and AB are invertible by their norm-convergent Neumann series. The map (BA)^(-1)B is a left inverse of A, while B(AB)^(-1) is a right inverse. Therefore A is a bounded linear bijection, and its inverse is the desired bounded bijection S_{R,T}->S_{R_0,T} direct-sum S_{R_1,T}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.5

**Statement:** Let D_1 be the identity on S_{P_1,Q}. For each 2<=j<=p, validated node 1.1 supplies the uniformly accurate projections and approximate orthogonality for R_0=P_[1,j-1], R_1=P_j, R=P_[1,j], T=Q, so validated binary splitting node 1.2 gives a bounded linear assembly bijection A_j:S_{P_[1,j-1],Q} direct-sum S_{P_j,Q}->S_{P_[1,j],Q}. Recursively set D_j=(D_{j-1} direct-sum id) composed with A_j^(-1). Then D_j is a bounded complex-linear bijection S_{P_[1,j],Q}->direct-sum_{r=1}^j S_{P_r,Q}; since P_[1,p]=v(I_B)=P, D_p gives S_{P,Q}->direct-sum_{r=1}^p S_{P_r,Q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.1.5.1

**Statement:** For each j with 2<=j<=p, instantiate validated node 1.2 with R_0=P_[1,j-1], R_1=P_j, R=P_[1,j], and T=Q. Validated node 1.1 supplies all hypotheses uniformly: R_0,R_1,R,T are uniformly accurate Hermitian projections, R=R_0+R_1 exactly, and R_0,R_1 are uniformly approximately orthogonal. Thus the canonical assembly map A_j:S_{P_[1,j-1],Q} direct-sum S_{P_j,Q}->S_{P_[1,j],Q} is a bounded complex-linear bijection, independently of pending nodes 1.5.1.3 and 1.5.1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.1.5.2

**Statement:** Define D_1=id_{S_{P_1,Q}}. If D_{j-1}:S_{P_[1,j-1],Q}->direct-sum_{r=1}^{j-1}S_{P_r,Q} is a bounded complex-linear bijection, define D_j=(D_{j-1} direct-sum id_{S_{P_j,Q}}) composed with A_j^(-1). It is a bounded complex-linear bijection, with bounded inverse A_j composed with (D_{j-1}^(-1) direct-sum id). Finite induction therefore constructs D_p:S_{P_[1,p],Q}->direct-sum_{r=1}^p S_{P_r,Q}; node 1.1 gives P_[1,p]=v(I_B)=P, yielding the asserted bijection.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Take the finite direct sum over j of the bijections from node 1.4 and compose with the preceding first-index bijection. Reassociate the finite algebraic direct sums to obtain a bounded complex-linear bijection S_{v(I_B),w(I_C)}->direct-sum_{j,k}S_{v(Pi_j),w(Sigma_k)}, exactly the root conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.2.1

**Statement:** Assume the validation prerequisites 1.5.1 and 1.4. Let F:S_{P,Q}->direct-sum_j S_{P_j,Q} be the bounded complex-linear bijection from 1.5.1, and for each j let G_j:S_{P_j,Q}->direct-sum_k S_{P_j,Q_k} be the bounded complex-linear bijection from 1.4. Equip all finite sums with the max norm. Then G=direct-sum_j G_j is bounded because max_j ||G_j||<infinity (the index set is finite), and G^{-1}=direct-sum_j G_j^{-1} is bounded for the same reason. The canonical reassociation R:(direct-sum_j direct-sum_k S_{P_j,Q_k})->direct-sum_{j,k}S_{P_j,Q_k} is a complex-linear isometric bijection. Hence H=R composed G composed F is a bounded complex-linear bijection, with bounded inverse F^{-1} composed G^{-1} composed R^{-1}. Finally P=v(I_B), Q=w(I_C), P_j=v(Pi_j), and Q_k=w(Sigma_k), so H has exactly the domain and codomain in the root contract. No bijectivity is asserted here before 1.5.1 and 1.4 are validated.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.5.2.1.1

**Statement:** Once nodes 1.5.1 and 1.4 are validated, denote their bijections by F:S_{P,Q}->direct-sum_j S_{P_j,Q} and G_j:S_{P_j,Q}->direct-sum_k S_{P_j,Q_k}. For the max norms on the finite sums, G=direct-sum_j G_j is bounded with ||G||=max_j||G_j|| and has bounded inverse direct-sum_j G_j^{-1}, whose norm is max_j||G_j^{-1}||. The coordinate-reassociation map R from direct-sum_j(direct-sum_k S_{P_j,Q_k}) to direct-sum_{j,k}S_{P_j,Q_k} is a complex-linear isometric bijection. Therefore H=R composed G composed F is a bounded complex-linear bijection and H^{-1}=F^{-1} composed (direct-sum_j G_j^{-1}) composed R^{-1}. Substituting P=v(I_B), Q=w(I_C), P_j=v(Pi_j), Q_k=w(Sigma_k) gives exactly the required map.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

