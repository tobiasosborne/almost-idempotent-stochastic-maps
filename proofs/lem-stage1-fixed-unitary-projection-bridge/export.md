# Proof Export

## Node 1

**Statement:** Fixed-unitary projection bridge: there are universal C_bridge<infinity and e_bridge^r>0 such that every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=e_bridge^r and 1<dim_C calX<infinity contains a nontrivial C_bridge*epsilon_r-projection P for the product bold-dot and unit J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Constant selection and the single upstream application: invoke lem-stage1-extra-fixed-class exactly once, obtaining universal C_fix>=1, e_fix^r>0 and r:=r_bidx>0 and, for every admissible algebra with epsilon_r<=e_fix^r, its displayed U in calU_e satisfying sigma(U)=U, ||U-U^dagger||<=C_fix*epsilon_r, and ||U-J||,||U+J||>=r. Define K:=3+4*C_fix/r, C_bridge:=max{C_fix,K}, and e_bridge^r:=min{e_fix^r,1/2,1/C_fix,r/C_fix}; these are universal with C_bridge<infinity and e_bridge^r>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Conditional fixed-unitary bridge: let C_fix>=1 and r>0, let 0<=epsilon<=min{1/2,1/C_fix,r/C_fix}, and let U belong to calU in an exact-unit epsilon-C*-algebra and satisfy ||U-U^dagger||<=C_fix*epsilon and ||U-J||,||U+J||>=r. Then for A:=(U+U^dagger)/2 and P:=(J+A)/2=(2J+U+U^dagger)/4, P is a nontrivial C_bridge*epsilon-projection, where C_bridge=max{C_fix,3+4*C_fix/r}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Unitary norm and Hermitian construction: because U belongs to calU, def-approximate-unitary-space gives U^dagger bold-dot U=J. The def-epsilon-cstar-algebra lower C*-bound and ||J||=1 give (1-epsilon)||U||^2<=1, hence ||U||<=sqrt(2)<2. For A=(U+U^dagger)/2, P=(J+A)/2 and Q=J-P=(J-A)/2, involutivity, conjugate linearity, and J^dagger=J give A^dagger=A, P^dagger=P, Q^dagger=Q, and ||A||<=||U||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Exact fixed-term defect identities: define Q:=J-P=(J-A)/2 in this node. Bilinearity and the exact two-sided unit from def-epsilon-cstar-algebra give P bold-dot P-P=(A bold-dot A-J)/4 and Q bold-dot Q-Q=P bold-dot P-P. Moreover A bold-dot A-U^dagger bold-dot U=(A-U^dagger) bold-dot A+U^dagger bold-dot(A-U), while ||A-U||=||A-U^dagger||=||U-U^dagger||/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Defect estimate: writing eta=||U-U^dagger||, the product-norm axiom in def-epsilon-cstar-algebra, ||A||<=||U||<2, epsilon<=1/2, and U^dagger bold-dot U=J imply ||A bold-dot A-J||<=(1+epsilon)*(eta/2)*(||A||+||U||)<=3*eta. Hence ||P bold-dot P-P||=||Q bold-dot Q-Q||<=3*C_fix*epsilon/4<=C_fix*epsilon<=C_bridge*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Separation excludes small norms quantitatively: define Q:=J-P=(J-A)/2. Then the exact identities U+J=2P+(U-A) and U-J=-2Q+(U-A), together with ||U-A||<=C_fix*epsilon/2<=r/2 and the assumed two distance bounds, imply ||P||>=r/4 and ||Q||>=r/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.4.1

**Statement:** With Q:=J-P=(J-A)/2, the definitions 2P=J+A and 2Q=J-A give U+J=2P+(U-A) and U-J=-2Q+(U-A). Also ||U-A||=||U-U^dagger||/2<=C_fix*epsilon/2<=r/2. Hence r<=||U+J||<=2||P||+||U-A||<=2||P||+r/2 and r<=||U-J||<=2||Q||+||U-A||<=2||Q||+r/2. Subtracting r/2 and dividing by 2 yields ||P||>=r/4 and ||Q||>=r/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** Near-one norm estimate and nontriviality: for either R=P or R=Q, put n=||R|| and d=||R bold-dot R-R||. Hermiticity, the epsilon-C* lower bound, the product upper bound, and the triangle inequality give (1-epsilon)n^2<=n+d and n<=(1+epsilon)n^2+d. Since epsilon<=1/2 and d<=C_fix*epsilon<=1, the first inequality gives n<3. Using n>=r/4, the first inequality when n>=1 and the second when n<=1 yield |n-1|<=3*epsilon+d/n<=(3+4*C_fix/r)*epsilon<=C_bridge*epsilon. Thus P and Q=J-P both satisfy the nonvanishing alternative in def-delta-projection; with Hermiticity and the defect bound, that definition says P is a nontrivial C_bridge*epsilon-projection.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Explicit composition, including epsilon_r=0: fix an admissible algebra with 0<=epsilon_r<=e_bridge^r and take C_fix,r,U from node 1.1. Since e_bridge^r<=min{1/2,1/C_fix,r/C_fix}, one has 0<=epsilon_r<=min{1/2,1/C_fix,r/C_fix}; node 1.1 also gives U in calU, ||U-U^dagger||<=C_fix*epsilon_r, and ||U-J||,||U+J||>=r. Hence node 1.2 applies with epsilon:=epsilon_r and yields its P as a nontrivial C_bridge*epsilon_r-projection. This remains valid at epsilon_r=0: the required hypothesis is the non-strict inequality ||U-U^dagger||<=0, supplied by node 1.1, never the false strict inequality 0<0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

