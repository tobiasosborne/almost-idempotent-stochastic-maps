# Proof Export

## Node 1

**Statement:** H-space coproduct-tail package over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity and (M,mu,e) is an H-space, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, and Delta=(cross product)^(-1) o mu^*; then A is a finite-dimensional graded-commutative associative unital algebra with A^0=reals*1, Delta:A->A tensor_reals A is a degree-preserving unital algebra homomorphism with Delta(1)=1 tensor 1, and for every homogeneous a in A^+ there exist a finite set J_a and homogeneous a'_j,a''_j in A^+ for j in J_a such that Delta(a)=a tensor 1+1 tensor a+sum_{j in J_a} a'_j tensor a''_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let M be a connected CW complex with finite-dimensional total real cohomology and let A=H^*(M;reals). Then the ordinary cup-product makes A a finite-dimensional graded-commutative associative unital real algebra, and connectedness gives A^0=H^0(M;reals)=reals*1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For such M, the cohomological cross product kappa:A tensor_reals A -> H^*(M times M;reals) is a degree-preserving isomorphism of unital graded rings, by the validated external lem-topology-kunneth-cross-product after checking its hypotheses.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Since the total graded real vector space A=direct_sum_{q>=0}H^q(M;reals) is finite-dimensional, each H^q(M;reals) is finite-dimensional and hence a finitely generated free real module; thus M satisfies the Y=M coefficient hypothesis of lem-topology-kunneth-cross-product for X=M.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Applying lem-topology-kunneth-cross-product with R=reals and X=Y=M, the cross product kappa:A tensor_reals A -> H^*(M times M;reals) is a ring isomorphism; the defining degree rule H^p tensor H^q -> H^(p+q) and 1 cross 1=1 make it degree-preserving and unital, so its inverse is also a degree-preserving unital ring isomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the H-space multiplication mu from def-h-space-left-inversion and Delta=kappa^(-1) o mu^*, Delta:A->A tensor_reals A is a degree-preserving unital algebra homomorphism and Delta(1)=1 tensor 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For every continuous map, singular-cohomology pullback preserves degree, cup products, and the unit; hence mu^*:H^*(M;reals)->H^*(M times M;reals) is a degree-preserving unital algebra homomorphism, and composing it with the degree-preserving unital ring isomorphism kappa^(-1) gives the same properties for Delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Let f:X->Y be continuous. For each singular n-simplex sigma:Delta^n->X define f_#(sigma)=f o sigma and extend linearly. Because restricting f o sigma to any face equals f composed with the corresponding face restriction of sigma, the alternating face formula gives boundary o f_# = f_# o boundary. For an n-cochain phi on Y define f^#phi=phi o f_#. Dualizing the preceding identity gives coboundary o f^# = f^# o coboundary. Thus f^# preserves cochain degree, carries cocycles to cocycles and coboundaries to coboundaries, and induces a degree-preserving map f^*:H^n(Y;reals)->H^n(X;reals) in every degree.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** For a singular p-cochain alpha and q-cochain beta, the Alexander-Whitney cup formula on a singular (p+q)-simplex sigma is (alpha cup beta)(sigma)=alpha(sigma restricted to the front p-face [v_0,...,v_p]) beta(sigma restricted to the back q-face [v_p,...,v_(p+q)]). Since composition with f commutes with both face restrictions, direct substitution yields f^#(alpha cup beta)=f^#alpha cup f^#beta. The degree-zero unit cochain is the function taking every singular 0-simplex to 1, so f^#1=1. These identities descend through the cochain map of the preceding child, proving that f^* preserves cup products and the unit. Apply this to f=mu:M times M->M; then mu^* is a degree-preserving unital algebra homomorphism. By validated node 1.2.2, kappa^(-1) is a degree-preserving unital ring isomorphism, so Delta=kappa^(-1) o mu^* is a degree-preserving unital algebra homomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Because mu^*(1)=1 in H^0(M times M;reals) and kappa(1 tensor 1)=1, one has Delta(1)=kappa^(-1)(mu^*(1))=1 tensor 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For every homogeneous a in A^+=direct_sum_{k>0}A^k, Delta(a) has the form a tensor 1+1 tensor a plus a finite sum of pure tensors whose two factors are homogeneous of positive degree.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Let epsilon=e^*:A->H^*({e};reals)=reals. For i_R:M->M times M, i_R(x)=(x,e), the right-unit homotopy in def-h-space-left-inversion gives mu o i_R homotopic to id_M. Homotopy invariance and naturality give i_R^*mu^*=id_A, while i_R^*kappa(x tensor y)=x cup e^*(y); therefore (id tensor epsilon) o Delta=id_A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** For i_L:M->M times M, i_L(x)=(e,x), the left-unit homotopy in def-h-space-left-inversion gives mu o i_L homotopic to id_M. Hence i_L^*mu^*=id_A and i_L^*kappa(x tensor y)=e^*(x) cup y, so (epsilon tensor id) o Delta=id_A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** If a is homogeneous of degree n>0, degree preservation puts Delta(a) in direct_sum_{p+q=n} A^p tensor A^q. Since M is connected, A^0=reals*1 and epsilon is the identity on A^0 and zero on every A^k for k>0; the two edge identities therefore force the (n,0) component to be a tensor 1 and the (0,n) component to be 1 tensor a. The remainder lies in the finite direct sum over p,q>0 with p+q=n, and each element of each algebraic tensor product A^p tensor A^q is a finite sum of pure tensors of homogeneous factors. Taking the finite union of these expansions gives a finite set J_a and homogeneous a'_j,a''_j in A^+ with Delta(a)=a tensor 1+1 tensor a+sum_{j in J_a}a'_j tensor a''_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

