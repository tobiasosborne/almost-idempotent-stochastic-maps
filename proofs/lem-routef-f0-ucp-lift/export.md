# Proof Export

## Node 1

**Statement:** Route F F0 UCP lift: let n >= 1, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C) and J: C^n -> M_n the diagonal inclusion, let Q: l_inf^n -> l_inf^n be row-stochastic, and let Q_C: C^n -> C^n be the canonical complex-linear extension of Q; then Phi := J Q_C D: M_n -> M_n is a unital completely positive map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** The canonical complex-linear extension Q_C:C^n->C^n of the row-stochastic Q is UCP.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-stochastic, row-stochasticity means Q has nonnegative matrix entries and Q 1=1; hence Q_C is unital and positive on the commutative C*-algebra C^n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** If x=(x_j) is positive in C^n, then every x_j is a nonnegative real number, so (Q_C x)_i=sum_j q_ij x_j>=0 because q_ij>=0; also Q_C(1)=Q(1)=1. Thus Q_C is positive and unital.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By def-ucp-map, a positive map out of a commutative C*-algebra is automatically completely positive; combined with unitality, Q_C is UCP.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The diagonal extraction D:M_n->C^n and diagonal inclusion J:C^n->M_n are UCP.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** D is unital, and for every r>=1 and every positive block matrix X=[X_ab] in M_r(M_n), (id_{M_r} tensor D)(X) is the n-tuple of principal compressions [(X_ab)_{ii}]_{a,b=1}^r (i=1,...,n), each positive in M_r; hence D is CP and therefore UCP by def-ucp-map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** J is unital, and for every r>=1 a positive element (A_1,...,A_n) of M_r(C^n)=direct-sum_{i=1}^n M_r is sent by id_{M_r} tensor J, up to the canonical permutation of tensor factors, to the positive block-diagonal matrix diag(A_1,...,A_n) in M_{rn}; hence J is CP and therefore UCP by def-ucp-map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** By the UCP composition fact in def-ucp-map, the composition Phi=J Q_C D is UCP once the preceding two claims hold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

