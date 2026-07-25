# Proof Export

## Node 1

**Statement:** Level-one one-dimensional corner dimension: for sufficiently small universal delta+epsilon, if P and Q are one-dimensional delta-projections then dim S_{P,Q} <= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Quantitative nonvanishing: let C_PQR and e_PQR be the universal constants from lem-extcb-one-dimensional-product and set e_0=min(e_PQR,1/(2(C_PQR+1))). If e=delta+epsilon<=e_0, P is one-dimensional, and X,Y are nonzero elements of S_{P,Q}, then X^dagger dot Y is nonzero in S_Q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Corner and norm facts: for X in S_{P,Q}, the compression-adjoint identity in def-compressed-corner gives X^dagger in S_{Q,P}; the involution axiom in def-epsilon-cstar-algebra gives ||X^dagger||=||X||; and the compressed-product definition places X^dagger dot Y in S_{Q,Q}=S_Q for Y in S_{P,Q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Product lower bound: applying lem-extcb-one-dimensional-product to the triple (Q,P,Q), whose middle projection P is one-dimensional, gives ||X^dagger dot Y|| >= (1-C_PQR*e)||X^dagger||||Y|| >= (1/2)||X||||Y||>0 for e<=e_0 and nonzero X,Y.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Linear-algebra conclusion: if Q is one-dimensional and, for every pair of nonzero X,Y in S_{P,Q}, one has X^dagger dot Y nonzero in S_Q, then dim S_{P,Q}<=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** When S_{P,Q}=0 the conclusion is immediate; otherwise fix nonzero X in S_{P,Q} and define T_X:S_{P,Q}->S_Q by T_X(Y)=X^dagger dot Y. The compressed product is bilinear by def-compressed-corner, so T_X is linear and has the stated codomain.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The assumed nonvanishing property says that T_X(Y) is nonzero whenever Y is nonzero, hence ker(T_X)={0} and T_X is injective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** By def-one-dimensional-delta-projection, Q one-dimensional means dim S_Q=1. An injective linear map from S_{P,Q} into S_Q implies dim S_{P,Q}<=dim S_Q=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

