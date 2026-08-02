# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN, then the nonempty set of m admitting an extended W.c0_cb*epsilon-inclusion w:C^m->A with ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon has a maximum because the lower norm is positive and m <= dim_C A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose the witnesses feeding lem-maincb-reset-constant-ledger coherently, enlarging its freely chosen valid c0 if necessary so that c0 >= 0, and fix the one resulting ledger W; for 0 <= epsilon <= W.epsilon_MAIN, lem-maincb-structural-domain-ledger applied to this same W gives epsilon <= W.K_call*epsilon and W.c0_cb*W.K_call*epsilon <= 1/2, hence with delta := W.c0_cb*epsilon one has 0 <= delta <= 1/2 and therefore 1-delta >= 1/2 > 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** At the preliminary constant-choice stage allowed by lem-maincb-reset-constant-ledger, choose the valid enlarged receiving coefficient c0 to satisfy c0 >= max{c0^0,K_floor,C_unit*(K_floor+1),0}; after fixing the particular e_sim and e_full witnesses, invoke that external once and fix its single resulting ledger W with W.c0_cb=c0, and use this same W in every subsequent external application.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For 0 <= epsilon <= W.epsilon_MAIN, lem-maincb-structural-domain-ledger for that same W yields epsilon <= W.K_call*epsilon and W.c0_cb*W.K_call*epsilon <= 1/2. Since W.c0_cb>=0, multiplication of the first inequality gives W.c0_cb*epsilon <= W.c0_cb*W.K_call*epsilon; since epsilon>=0, delta:=W.c0_cb*epsilon>=0. Therefore 0<=delta<=1/2 and 1-delta>=1/2>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the same fixed W and A, lem-maincb-initial-reset-inclusion supplies an extended W.c0_cb*epsilon-inclusion v:C->A with ||v(I_C)-I_A|| <= W.c0_cb*epsilon; taking m=1 and w=v shows that the admissible-index set S is nonempty.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** If delta := W.c0_cb*epsilon satisfies delta <= 1/2, then for every m in S and its witnessing extended delta-inclusion w:C^m->A, def-extended-delta-inclusion at amplification n=1 gives ||w(x)|| >= (1-delta)||x|| >= (1/2)||x|| for all x in C^m; thus w is injective, so finite-dimensional linear algebra gives m=dim_C(C^m) <= dim_C A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Let delta<=1/2 and let w:C^m->A be an extended delta-inclusion. By def-extended-delta-inclusion, its n=1 amplification is a delta-inclusion and obeys the lower norm bound ||w(x)|| >= (1-delta)||x||. Hence ||w(x)|| >= (1/2)||x|| for every x, so w(x)=0 forces x=0 and w is injective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** For an injective complex-linear map w:C^m->A with A finite-dimensional, rank-nullity gives dim_C(C^m)=rank(w)<=dim_C A; since dim_C(C^m)=m, one has m<=dim_C A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For every finite nonnegative integer d, every nonempty set S of integers m occurring as dimensions m=dim_C(C^m) and satisfying m<=d is contained in the finite set {0,...,d}; therefore S has a maximum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

