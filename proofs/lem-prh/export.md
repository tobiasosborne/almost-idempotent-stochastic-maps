# Proof Export

## Node 1

**Statement:** Positive-retract hardening (PRH): let k,n >= 1 and let A:l-infinity(k)->l-infinity(n) and M:l-infinity(n)->l-infinity(k) be positive unital maps (equivalently, have probability-vector rows); if ||MA-I_k||_{infinity->infinity} <= epsilon with 0 <= epsilon < 1/2, then there is a stochastic idempotent E:l-infinity(n)->l-infinity(n) with ||AM-E||_{infinity->infinity} <= 2*sqrt(2*epsilon).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Zero-defect case: if epsilon=0, then ||MA-I_k||=0 gives MA=I_k; E:=AM is row-stochastic, E^2=A(MA)M=AM=E, and ||AM-E||=0, so the required conclusion holds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Positive-defect case: if 0<epsilon<1/2 under the hypotheses of node 1, then there is a stochastic idempotent E with ||AM-E||_{infinity->infinity} <= 2*sqrt(2*epsilon).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Core lemma: assume 0<epsilon<1/2 and write the probability rows of A as a_i=(a_{i1},...,a_{ik}) and those of M as mu_s=(mu_s(1),...,mu_s(n)). Put lambda=sqrt(epsilon/2), C_s={i:a_{is}>1-lambda}, and beta_s=mu_s(C_s^c). Then D_s:=sum_i mu_s(i)(1-a_{is}) <= epsilon/2 for every s, the sets C_s are pairwise disjoint, and beta_s <= epsilon/(2*lambda)=lambda<1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** Coordinate defect identity: for every s, the s-th row of MA is the probability vector sum_i mu_s(i)a_i, and therefore ||(MA)_{s,*}-e_s||_1=2(1-(MA)_{ss})=2*sum_i mu_s(i)(1-a_{is})=2D_s. The operator-norm hypothesis hence gives D_s<=epsilon/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.2

**Statement:** Threshold consequences: with lambda=sqrt(epsilon/2), if distinct s,t had i in C_s intersect C_t, then a_{is}+a_{it}>2(1-lambda)>1, contradicting that a_i is a probability vector. Thus the C_s are pairwise disjoint. Also 1-a_{is}>=lambda on C_s^c, so lambda*beta_s<=D_s<=epsilon/2; since lambda^2=epsilon/2 and 0<epsilon<1/2, beta_s<=epsilon/(2lambda)=lambda<1/2<1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.3

**Statement:** Corrected threshold estimate (replacing the false strict estimate in node 1.2.1.2): because C_s={i:a_{is}>1-lambda}, membership i in C_s^c means a_{is}<=1-lambda and hence 1-a_{is}>=lambda. Since every mu_s(i)>=0, D_s=sum_i mu_s(i)(1-a_{is})>=sum_{i in C_s^c}mu_s(i)(1-a_{is})>=lambda*sum_{i in C_s^c}mu_s(i)=lambda*beta_s. Here lambda=sqrt(epsilon/2)>0, so beta_s<=D_s/lambda<=epsilon/(2*lambda)=lambda. Moreover epsilon<1/2 gives lambda=sqrt(epsilon/2)<1/2<1. Thus the weak inequality beta_s<=lambda asserted by the parent follows; no strict inequality beta_s<lambda is claimed or needed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Exact construction lemma: given probability rows a_i and mu_s and a number 0<lambda<1/2 with pairwise disjoint C_s={i:a_{is}>1-lambda} and beta_s:=mu_s(C_s^c)<1, define nu_s(i):=mu_s(i)1_{C_s}(i)/(1-beta_s), let N have rows nu_s, and let hatA have row e_s on C_s and row a_i outside the union of the C_s. Then N and hatA are positive unital, N hatA=I_k, and E:=hatA N is a stochastic idempotent.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Conditioning and right-inverse identity: because beta_s<1, nu_s is entrywise nonnegative and sum_i nu_s(i)=mu_s(C_s)/(1-beta_s)=1. Pairwise disjointness makes hatA well-defined, and each of its rows is a probability vector. Moreover the s-th row of N hatA is sum_{i in C_s} mu_s(i)e_s/(1-beta_s)=e_s, so N hatA=I_k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Idempotent conclusion: the product E:=hatA N is a positive unital endomorphism of l-infinity(n), hence row-stochastic, and (hatA N)^2=hatA(N hatA)N=hatA I_k N=hatA N=E. Thus E is a stochastic idempotent in the sense of def-stochastic.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Error lemma: in the positive-defect setup of the core lemma, for N, hatA, and E from the exact construction lemma one has ||AM-E||_{infinity->infinity} <= epsilon/lambda+2*lambda = 2*sqrt(2*epsilon).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** Conditioning estimate: for each s, nu_s is mu_s conditioned on C_s, so ||mu_s-nu_s||_1=2*mu_s(C_s^c)=2*beta_s<=epsilon/lambda. Hence ||M-N||_{infinity->infinity}<=epsilon/lambda. Since every probability-row map A is an infinity-norm contraction, ||A(M-N)||_{infinity->infinity}<=epsilon/lambda.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** Core-replacement estimate and sum: outside the union of the C_s, the corresponding row of (A-hatA)N is zero. If i is in C_s, that row is (a_i-e_s)N=sum_t a_{it}nu_t-nu_s, whose l1 norm is at most (1-a_{is})+sum_{t not equal s}a_{it}=2(1-a_{is})<2*lambda because every nu_t is a probability vector. Thus ||(A-hatA)N||_{infinity->infinity}<=2*lambda. Since AM-E=A(M-N)+(A-hatA)N, the triangle inequality gives ||AM-E||<=epsilon/lambda+2*lambda=2*sqrt(2*epsilon).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.3.2.1

**Statement:** Local conditioning-contraction estimate, proved from the root hypotheses: put B=M-N. For each s, ||(MA)_{s,*}-e_s||_1<=epsilon; since (MA)_{s,*} is a probability vector, this norm equals 2(1-(MA)_{ss})=2*sum_i mu_s(i)(1-a_{is}), so D_s:=sum_i mu_s(i)(1-a_{is})<=epsilon/2. On C_s^c one has 1-a_{is}>=lambda, hence lambda*beta_s<=D_s and beta_s<=epsilon/(2*lambda)<1. Because nu_s is mu_s conditioned on C_s, the l1 difference on C_s has total beta_s and that on C_s^c has total beta_s, so ||mu_s-nu_s||_1=2*beta_s<=epsilon/lambda. Therefore ||B||_{infinity->infinity}<=epsilon/lambda. Finally, for every row i, sum_j |(AB)_{ij}|<=sum_s a_{is} sum_j |B_{sj}|<=max_s sum_j |B_{sj}| because a_i is a probability vector. Thus ||A(M-N)||_{infinity->infinity}=||AB||_{infinity->infinity}<=epsilon/lambda.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

