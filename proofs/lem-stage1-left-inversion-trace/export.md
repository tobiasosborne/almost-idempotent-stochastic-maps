# Proof Export

## Node 1

**Statement:** Left-inversion trace over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, then Tr(sigma^{*k}:H^k(M;reals)->H^k(M;reals))=(-1)^k*dim_reals H^k(M;reals) for every k >= 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix k >= 0 and apply lem-stage1-left-inversion-associated-graded with A=H^*(M;reals); put V=A^k and W_p=F^{p,k-p}=(A^+)^p intersect A^k. The zeroth ideal power gives W_0=A^k=V, ideal powers give W_{p+1} contained in W_p, and W_{k+1}=0 because a product of k+1 positive-degree classes has degree at least k+1 and hence has no degree-k part. The hypothesis dim_reals A<infinity makes V finite-dimensional. The same external lemma says sigma^* preserves every F^{p,q}, so its degree-k map sigma^{*k} preserves each W_p; moreover W_p/W_{p+1}=F^{p,k-p}/F^{p+1,k-p-1}=E^{p,k-p}. Thus W_0 superset ... superset W_{k+1}=0 is a finite sigma^{*k}-invariant filtration of V.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix k >= 0, take A and F from lem-stage1-left-inversion-associated-graded, and set W_p=F^{p,k-p}. For every 0 <= p <= k, that external lemma identifies W_p/W_{p+1}=F^{p,k-p}/F^{p+1,k-p-1}=E^{p,k-p} and says the map induced there by the degree-k component sigma^{*k} is (-1)^{p+(k-p)} id=(-1)^k id.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Let T be an endomorphism of a finite-dimensional vector space V preserving a finite decreasing filtration W_0=V superset W_1 superset ... superset W_{k+1}=0. Choose a basis adapted to the filtration. The matrix of T is block triangular with diagonal blocks representing the induced maps T_p on W_p/W_{p+1}; since the trace of a block-triangular matrix is the sum of the traces of its diagonal blocks, Tr(T|V)=sum_{p=0}^k Tr(T_p|W_p/W_{p+1}).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For the finite filtration W_0=V superset W_1 superset ... superset W_{k+1}=0, the identities dim_reals W_p=dim_reals(W_p/W_{p+1})+dim_reals W_{p+1} telescope to dim_reals V=sum_{p=0}^k dim_reals(W_p/W_{p+1}).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Combining 1.1--1.4, each quotient trace in the trace sum is (-1)^k dim_reals(W_p/W_{p+1}), and the quotient dimensions sum to dim_reals V. Hence Tr(sigma^{*k}:H^k(M;reals)->H^k(M;reals))=(-1)^k dim_reals H^k(M;reals); since k >= 0 was arbitrary, this proves the root claim for every k.

**Type:** claim

**Inference:** universal_generalization

**Status:** validated

**Taint:** clean

