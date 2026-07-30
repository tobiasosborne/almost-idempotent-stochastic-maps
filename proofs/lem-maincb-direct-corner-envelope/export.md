# Proof Export

## Node 1

**Statement:** There are universal L >= 1 and e_env > 0 such that, if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= e_env, and w:C^m->A is an extended c_0^cb*epsilon-inclusion, then every nonempty U has P_U a c_0^cb*epsilon-projection, every A_U = S^A_{P_U} is an extended L*epsilon-C*-algebra, and for U subseteq R all subordination and complementarity errors among P_U, P_{R minus U}, P_R are at most L*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Universal constant ledger. Choose the witness c_0^cb in lem-maincb-error-improvement at least 1 (enlarging an inclusion-defect constant preserves every stated error inequality). Let C_ca<infinity and e_ca>0 be the universal witnesses in lem-compcb-corner-algebra. Set K:=c_0^cb+1, L:=max{1,c_0^cb,C_ca*K}, and e_env:=min{e_ca/K,1/(2*c_0^cb)}. These are positive universal constants, L>=1, and whenever 0<=epsilon<=e_env and delta:=c_0^cb*epsilon, one has delta<=1/2, delta+epsilon=K*epsilon<=e_ca, delta<=L*epsilon, and C_ca*(delta+epsilon)<=L*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Coordinate projections give nonvanishing approximate projections. For a nonempty U subseteq {1,...,m}, let e_U=sum_{j in U}e_j in C^m. By def-maincb-partition-state and linearity, P_U=sum_{j in U}P_j=w(e_U) and A_U=S^A_{P_U}. Now e_U^dagger=e_U, e_U^2=e_U, and ||e_U||=1. At amplification n=1, def-extended-delta-inclusion says that w is a delta-homomorphism with the two-sided (1 plus-or-minus delta) norm bounds, where delta=c_0^cb*epsilon. Hence P_U^dagger=P_U, ||P_U^2-P_U||=||w(e_U)w(e_U)-w(e_U^2)||<=delta, and 1-delta<=||P_U||<=1+delta. Thus P_U is a delta-projection by def-delta-projection and satisfies its nonvanishing second alternative with explicit coefficient 1, since abs(||P_U||-1)<=delta<=delta+epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Uniform corner algebra. For every nonempty U, node 1.2 supplies a nonvanishing delta-projection P_U, while node 1.1 gives delta+epsilon<=e_ca. Applying lem-compcb-corner-algebra to P_U shows that S^A_{P_U}, with the compressed product, inherited involution and compressed unit Co_{P_U}(P_U) from def-compressed-corner, is an extended C_ca*(delta+epsilon)-C*-algebra. Since C_ca*(delta+epsilon)<=L*epsilon, enlarging the common error bound in the defining inequalities makes A_U=S^A_{P_U} an extended L*epsilon-C*-algebra. The coefficient and threshold are independent of m,U,A and every amplification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** All subordination and complementarity errors are direct coordinate identities. Fix arbitrary U subseteq R subseteq {1,...,m}, put V:=R minus U, and use e_U,e_V,e_R in C^m. They satisfy e_Ue_R=e_Re_U=e_U, e_Ve_R=e_Re_V=e_V, e_Ue_V=e_Ve_U=0, and e_U+e_V=e_R. Linearity gives P_U+P_V=P_R exactly (including empty-set cases), while the delta-multiplicative clause of def-extended-delta-inclusion gives each of ||P_UP_R-P_U||, ||P_RP_U-P_U||, ||P_VP_R-P_V||, ||P_RP_V-P_V||, ||P_UP_V||, and ||P_VP_U|| at most delta (and zero whenever a relevant coordinate projection is zero). These are respectively all left/right subordination errors and the orthogonality/additivity complementarity errors among P_U,P_{R minus U},P_R; node 1.1 gives delta<=L*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Assembly after the explicit same-(A,w) notation bridge in node 1.5.1. In the root conclusion P_U and A_U are the local abbreviations P_U:=w(e_U) and A_U:=S^A_{P_U} for e_U=sum_{j in U}e_j; they are not taken from an independently supplied MAIN-CB partition state. Under the hypotheses of node 1, use the universal L,e_env of node 1.1. With this binding, node 1.2 proves the asserted c_0^cb*epsilon-projection and nonvanishing statements for every nonempty U, node 1.3 proves the extended L*epsilon-C*-algebra statement for every A_U, and node 1.4 proves every subordination and complementarity estimate for U subseteq R. Thus nodes 1.1-1.4 together with the context repair 1.5.1 establish exactly all clauses of the root contract without an additional state hypothesis.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Same-(A,w) notation bridge and repaired assembly. For each U subseteq {1,...,m}, set e_U:=sum_{j in U} e_j in C^m and bind the symbols in the root conclusion by the local abbreviations P_U:=w(e_U) and A_U:=S^A_{P_U}. These objects are determined solely by the displayed A and w; no MAIN-CB partition state is assumed or consumed, and in particular no current-union or reset-state field is needed. The abbreviations agree with the geometric P_U,A_U fields of def-maincb-partition-state whenever a state for this same (A,w) is separately supplied. With this binding, the first sentence of node 1.2 is obtained directly from the displayed definitions and linearity, rather than from existence of a partition state; the remainder of node 1.2 proves the delta-projection and nonvanishing assertions for delta=c_0^cb*epsilon. Node 1.3 then applies lem-compcb-corner-algebra to exactly A_U=S^A_{P_U}, and node 1.4 uses the same definitions P_U=w(e_U), P_{R minus U}=w(e_{R minus U}), P_R=w(e_R) to prove all subordination and complementarity bounds. Together with the constants of node 1.1, this proves every clause of node 1 without any hidden state hypothesis.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

