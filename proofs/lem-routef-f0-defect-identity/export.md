# Proof Export

## Node 1

**Statement:** Route F F0 defect identity: let n >= 1, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C) and J: C^n -> M_n the diagonal inclusion, let Q: l_inf^n -> l_inf^n be row-stochastic with canonical complex-linear extension Q_C: C^n -> C^n, and put Phi := J Q_C D; then ||Phi^2 - Phi||_cb = ||Q^2 - Q||_{infinity->infinity}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Put L := Q_C^2 - Q_C. Then Phi^2 - Phi = J L D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For every x in C^n, D(J(x)) = x, because J(x) is the diagonal matrix with diagonal x and D extracts that diagonal; hence D J = I_{C^n}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Using Phi = J Q_C D and D J = I_{C^n}, composition gives Phi^2 - Phi = J Q_C (D J) Q_C D - J Q_C D = J (Q_C^2-Q_C) D = J L D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every r >= 1, under M_r(C^n) = direct-sum_{j=1}^n M_r with norm max_j ||X_j||, the amplification J_r is an isometry, D_r is a contraction, and D_r J_r = I.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** An element X of M_r(C^n) is a tuple (X_1,...,X_n) with norm max_j ||X_j||. After the canonical tensor-factor permutation, J_r(X) is block diagonal diag(X_1,...,X_n), so ||J_r X|| = max_j ||X_j||. For A in M_r(M_n), D_r(A) is the tuple of diagonal n-by-n blocks (A_{11},...,A_{nn}); each A_{jj} is a compression of A and has norm at most ||A||. Thus J_r is isometric, D_r is contractive, and direct extraction after inclusion gives D_r J_r=I.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every r >= 1, ||J_r L_r D_r|| <= ||L_r||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By the matrix-level isometry and contraction in node 1.2, submultiplicativity gives ||J_r L_r D_r|| <= ||J_r|| ||L_r|| ||D_r|| <= ||L_r|| for every r >= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For every r >= 1, ||J_r L_r D_r|| >= ||L_r||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Fix r. For every X in M_r(C^n), node 1.2 gives ||J_r X||=||X|| and D_r J_r X=X, whence ||J_r L_r D_r(J_r X)||=||J_r L_r X||=||L_r X||. Taking the supremum over nonzero X (equivalently over ||X||<=1) shows ||J_r L_r D_r|| >= ||L_r||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For every r >= 1, ||L_r|| = max_i sum_j |l_ij| = ||Q^2-Q||_{infinity->infinity}, where (l_ij) is the real matrix of Q^2-Q; consequently taking the supremum over r gives ||Phi^2-Phi||_cb = ||Q^2-Q||_{infinity->infinity}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Write L=(l_ij), the same real coefficient matrix as Q^2-Q. For X=(X_j) in M_r(C^n), (L_r X)_i=sum_j l_ij X_j, so ||L_r X||=max_i ||sum_j l_ij X_j|| <= (max_i sum_j |l_ij|)(max_j ||X_j||). Conversely choose i_0 attaining the maximum row sum and take X_j=sgn(l_{i_0j}) I_r (with sgn(0)=0); then max_j ||X_j||<=1 and the i_0 component of L_r X equals (sum_j |l_{i_0j}|)I_r. Hence ||L_r||=max_i sum_j |l_ij| for every r. By def-almost-idempotent this row maximum is exactly ||Q^2-Q||_{infinity->infinity}. By node 1.1, (Phi^2-Phi)_r=J_r L_r D_r, and nodes 1.3 and 1.4 give ||(Phi^2-Phi)_r||=||L_r|| at every r; taking sup_{r>=1}, which is the cb norm by definition, proves the asserted identity.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

