# Proof Export

## Node 1

**Statement:** Route F F2 positive-unital compression: let K >= 1 be a dimension-independent constant, n >= 1, Q: l_inf^n -> l_inf^n row-stochastic, D: M_n -> C^n diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), J: C^n -> M_n diagonal inclusion, Q_C: C^n -> C^n the canonical complex-linear extension of Q, and Phi = J Q_C D, B a finite-dimensional unital C*-algebra, and Delta: B -> M_n, Upsilon: M_n -> B UCP maps; if 0 <= eta <= min{(24K)^{-1},1}, ||Delta Upsilon - Phi||_cb <= K*eta, ||Upsilon Delta - I_B||_cb <= K*eta, and ||Upsilon(Delta x Delta y) - xy|| <= K*eta*||x||*||y|| for all x,y in B, then B is commutative and there are k >= 1 and a unital *-isomorphism iota_C: C^k = l_inf^k(C) -> B such that D Delta iota_C maps R^k into R^n, iota_C^{-1} Upsilon J maps R^n into R^k, and the resulting restrictions and corestrictions A := (D Delta iota_C)|_{R^k}: l_inf^k -> l_inf^n and M := (iota_C^{-1} Upsilon J)|_{R^n}: l_inf^n -> l_inf^k are positive unital maps satisfying ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** UCP complete contractivity (shared lemma): for unital C*-algebras A,C and every UCP map T:A->C in the sense of def-ucp-map, each amplification T_r=id_{M_r} tensor T is contractive, hence ||T||_cb<=1. In particular ||Delta||_cb<=1 and ||Upsilon||_cb<=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Matrix Schwarz step from 2-positivity: fix r>=1 and set S=id_{M_r} tensor T. Complete positivity and unitality make S unital and 2-positive. For a in M_r(A), the 2-by-2 block [a,1]^*[a,1]=[[a* a,a*],[a,1]] is positive in M_2(M_r(A)); applying id_{M_2} tensor S gives [[S(a* a),S(a)*],[S(a),1]]>=0. The Schur complement of the lower-right identity, equivalently positivity tested on columns of the form (xi,-S(a)xi), yields S(a)*S(a)<=S(a* a).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Norm conclusion: positivity and unitality give 0<=S(a* a)<=||a||^2 1. Together with node 1.1.1 this yields ||S(a)||^2=||S(a)*S(a)||<=||a||^2. Hence ||S||<=1 for every r; equality holds on the identity, so ||S||=1 and ||T||_cb=1. Applying this to the root UCP maps gives ||Delta||_cb,||Upsilon||_cb<=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Typed diagonal-range facts: by def-stochastic, Q_C:C^n->C^n is positive and unital; since its domain is commutative it is UCP. The diagonal inclusion J is a unital *-homomorphism and hence UCP, while D([a_ij])=(a_11,...,a_nn) is UCP because every amplification sends a positive block matrix [A_ij] to the direct sum of its positive diagonal compressions. Thus Phi=J Q_C D is UCP and, by node 1.1, contractive; Phi(a) lies in J(C^n), any two elements in its range commute, D J=I_{C^n}, and J is isometric. Moreover every positive linear map is *-preserving, so D,Delta,Upsilon,J and iota_C whenever defined carry self-adjoint elements to self-adjoint elements.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Approximate invariance: under the root hypotheses, for every b in B one has ||Delta b-Phi(Delta b)|| <= 2K*eta*||b||. Indeed Delta b-Phi Delta b = Delta(b-Upsilon Delta b)+(Delta Upsilon-Phi)(Delta b), whose two terms have norms at most K*eta*||b|| and K*eta*||Delta b||<=K*eta*||b|| by node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Approximate commutativity: under the root hypotheses, for all x,y in B, ||xy-yx|| <= 10K*eta*||x||*||y||. Put a=Delta x, b=Delta y, a0=Phi a, b0=Phi b. By node 1.3, ||a-a0||<=2K*eta||x|| and ||b-b0||<=2K*eta||y||; by nodes 1.1-1.2, ||a||,||a0||<=||x|| and ||b||,||b0||<=||y||, while [a0,b0]=0. Hence ||[a,b]||<=||[a-a0,b]||+||[a0,b-b0]||<=8K*eta||x||||y||. The two approximate-product hypotheses for (x,y) and (y,x), together with contractivity of Upsilon, give ||[x,y]||<=2K*eta||x||||y||+||Upsilon([a,b])||<=10K*eta||x||||y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Norm-two witness lemma, proved without finite-dimensional C*-classification: if a finite-dimensional unital C*-algebra B is noncommutative, then there exist contractions x,y in B with ||xy-yx||=2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Minimal-projection decomposition: every nonzero finite-dimensional unital C*-algebra B has a finite family of mutually orthogonal minimal projections p_1,...,p_m summing to 1. Indeed choose a nonzero projection minimal under subprojection, repeat in the complementary corner, and termination follows because nonzero orthogonal projections are linearly independent. For a minimal projection p, pBp=Cp: otherwise a non-scalar self-adjoint element of pBp has, by finite-dimensional spectral functional calculus, a nonzero proper spectral projection below p.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Off-diagonal corner: for the decomposition in node 1.5.1, noncommutativity implies p_i B p_j is nonzero for some i!=j. For if every off-diagonal corner vanished, then b=sum_{i,j}p_i b p_j=sum_i lambda_i(b)p_i for every b, using p_i B p_i=Cp_i, so B would be contained in the commutative span of the p_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** Matrix-unit normalization: choose distinct minimal p,q and 0!=z in pBq as in node 1.5.2. Since z* z belongs to qBq=Cq and zz* belongs to pBp=Cp, the C*-identity gives z*z=||z||^2 q and zz*=||z||^2 p. Thus v=z/||z|| obeys v*v=q and vv*=p; also pq=0 and v=pvq imply v^2=(v*)^2=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.4

**Statement:** Pauli witness: set x=p-q and y=v+v*. Then x*=x, y*=y, x*x=y*y=p+q, so ||x||=||y||=1. Direct multiplication using v=pvq, v*v=q and vv*=p gives xy-yx=2(v-v*), while (v-v*)*(v-v*)=p+q has norm 1. Hence ||xy-yx||=2, proving node 1.5.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Commutativity forcing with constants bound locally: let K>=1 and 0<=eta<=(24K)^{-1}. If B satisfies node 1.4, then B is commutative. Otherwise node 1.5 supplies contractions x,y with commutator norm 2, whereas node 1.4 gives 2<=10K*eta<=10/24=5/12<2, a contradiction.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Commutative coordinates: from node 1.6 and external projection-basis-kitaev-1361, there are k>=1 and pairwise orthogonal nonzero projections Pi_1,...,Pi_k in B with sum 1 and spanning B. The formula iota_C:C^k->B, iota_C(z_1,...,z_k)=sum_j z_j Pi_j, is a unital *-isomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.7.1

**Statement:** Projection-basis input: node 1.6 makes B a finite-dimensional commutative unital C*-algebra. The permitted byte-verbatim external projection-basis-kitaev-1361 states that such an algebra is described by a projection basis {Pi_1,...,Pi_k} with Pi_j*=Pi_j, Pi_j Pi_l=delta_{jl}Pi_l, and sum_j Pi_j=1. Because it is a basis, k>=1, every Pi_j is nonzero, and the Pi_j linearly span B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.7.2

**Statement:** Coordinate calculation: define iota_C(z)=sum_j z_j Pi_j. The relations in node 1.7.1 give iota_C(1,...,1)=1, iota_C(zw)=iota_C(z)iota_C(w), and iota_C(conjugate(z))=iota_C(z)*. Linear independence makes iota_C injective and spanning makes it surjective. Hence it is a unital *-isomorphism C^k->B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Typed positive-unital real maps: for iota_C from node 1.7, the compositions D Delta iota_C:C^k->C^n and iota_C^{-1} Upsilon J:C^n->C^k are UCP, hence positive and unital. Since positive maps are *-preserving, they map the self-adjoint parts R^k into R^n and R^n into R^k. Their restrictions/corestrictions A:l_inf^k->l_inf^n and M:l_inf^n->l_inf^k are therefore positive unital real maps.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** AM estimate: for z in R^n, use D J=I and Phi=J Q_C D to identify Qz=D Phi Jz, while AMz=D Delta Upsilon Jz. Since D and J are contractions, ||(Q-AM)z||_inf <= ||(Phi-Delta Upsilon)Jz|| <= K*eta||z||_inf. Thus ||Q-AM||_{inf->inf}<=K*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.10

**Statement:** QA-A estimate: for x in R^k, QAx-Ax=D(Phi Delta iota_C x-Delta iota_C x), because D Phi=Q_C D and Q_C restricts to Q on R^n. Node 1.3 and contractivity of D and the isometry iota_C yield ||QAx-Ax||_inf<=2K*eta||x||_inf. Hence ||QA-A||_{inf->inf}<=2K*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.11

**Statement:** Lower-modulus inference only: for x in R^k, node 1.1 and ||Upsilon Delta-I_B||_cb<=K*eta imply ||Delta iota_C x|| >= ||Upsilon Delta iota_C x|| >= (1-K*eta)||x||_inf. Node 1.3 gives ||Delta iota_C x-Phi Delta iota_C x||<=2K*eta||x||_inf, and ||Phi Delta iota_C x||=||J Q_C A x||<=||A x||_inf by contractivity of Q_C and isometry of J. Therefore ||A x||_inf >= (1-3K*eta)||x||_inf.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.12

**Statement:** Assembly: nodes 1.6-1.11 provide B commutative, k>=1, the required unital *-isomorphism iota_C, the stated real-part mapping properties and positive unital maps A,M, together with all three inequalities ||Q-AM||_{inf->inf}<=K*eta, ||QA-A||_{inf->inf}<=2K*eta, and ||Ax||_inf>=(1-3K*eta)||x||_inf for every x. This is exactly the conclusion of root node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.12.1

**Statement:** Endpoint bridge for the assembly: node 1.6 is stated for K>=1 and 0<=eta<=(24K)^{-1}, so it covers the root endpoint eta=0. Concretely, at eta=0 node 1.4 gives ||xy-yx||<=10K*0*||x||*||y||=0 for every x,y in B, hence B is commutative directly; equivalently, if B were noncommutative then node 1.5 and node 1.4 would give 2=||xy-yx||<=0, a contradiction. Thus node 1.6 supplies commutativity on the entire root interval 0<=eta<=min{(24K)^{-1},1}; node 1.7 consequently supplies iota_C also at eta=0, and nodes 1.8-1.11 then supply the mapping properties and estimates there (with right sides K*eta, 2K*eta, and 1-3K*eta evaluated at eta=0). Therefore node 1.12 assembles the root conclusion without an endpoint gap.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

