# Proof Export

## Node 1

**Statement:** After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R that satisfies d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, is an extended W.c0_cb*epsilon_R-inclusion, is an extended W.c0_cb*epsilon_R-isomorphism when u_R is bijective, and leaves the source, target corner, and amplification form unchanged.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Unpack the third clause of GT-kitaev-prop-delta-hominc using its registered implicit quantifier convention. There are universal C_unit>0, epsilon_unit>0, delta_unit>0 and a_unit>0, chosen with a_unit strictly below the positive near-unit threshold in that clause, such that every level-one delta-homomorphism f between epsilon-C*-algebras with epsilon<=epsilon_unit, delta<=delta_unit, and ||f(I)-I||<=a_unit satisfies ||f(I)-I||<=C_unit*(delta+epsilon). These constants are independent of all algebras, dimensions, maps, D, W and t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix D, W and one raw call as in node 1, and put q=(1+K_disp)*D*t. The ledger radius inequalities and epsilon_R<=t give epsilon_R<=epsilon_max^cb, D*t<=delta_max^cb, D*t+epsilon_R<=e_it, epsilon_R<=epsilon_unit, K_floor*epsilon_R<=delta_unit, and q<=min{a_unit,1/2}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Apply lem-maincb-improvement-iteration to the literal map u_R with d=D*t and epsilon=epsilon_R. It produces one specific dagger-preserving map v_R:B_R->A_R, with amplifications (v_R)_n=I_n tensor v_R, such that sup_n||(v_R)_n-(u_R)_n||<=K_disp*D*t and v_R is an extended K_floor*epsilon_R-inclusion; this is the map retained throughout the proof, including at epsilon_R=0 where the provider specifies the operator-norm limit.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For the same v_R from node 1.3, the n=1 map bound and ||I_{B_R}||=1 give ||v_R(I_{B_R})-u_R(I_{B_R})||<=K_disp*D*t. The raw-call unit hypothesis and the triangle inequality therefore give ||v_R(I_{B_R})-u_{A_R}||<=q<=a_unit. Since an extended K_floor*epsilon_R-inclusion is at level one a K_floor*epsilon_R-homomorphism, the source exact C*-algebra is also an epsilon_R-C*-algebra, and the target is an epsilon_R-C*-algebra, node 1.1 and GT-kitaev-prop-delta-hominc apply with delta=K_floor*epsilon_R. Hence ||v_R(I_{B_R})-u_{A_R}||<=C_unit*(K_floor+1)*epsilon_R<=W.c0_cb*epsilon_R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Record d_R=K_floor*epsilon_R for this v_R. Then d_R<=W.c0_cb*epsilon_R. Also K_floor*epsilon_R<=W.c0_cb*epsilon_R, so definitional weakening of the amplified homomorphism and two-sided norm inequalities, equivalently lem-maincb-extended-inclusion-monotone in the finite-dimensional MAIN corner setting, makes this same v_R an extended W.c0_cb*epsilon_R-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** If u_R is bijective, its extended D*t-inclusion lower norm bound and node 1.3 imply ||v_R(x)||>=||u_R(x)||-||(v_R-u_R)(x)||>=(1-(1+K_disp)*D*t)||x||=(1-q)||x||>=||x||/2 for every x in B_R. Thus v_R is injective. Bijectivity of u_R identifies the finite dimensions of B_R and A_R, so v_R is bijective. By def-extended-delta-inclusion it is an extended K_floor*epsilon_R-isomorphism, and lem-maincb-extended-inclusion-monotone upgrades it to an extended W.c0_cb*epsilon_R-isomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** The map satisfying all conclusions is the single iteration output v_R of node 1.3, not the separate existential replacement offered by lem-maincb-error-improvement. Nodes 1.4-1.6 give its unit estimate, recorded defect, extended inclusion, and conditional extended-isomorphism typing. Because node 1.3 constructs v_R with literal type B_R->A_R and amplifications I_n tensor v_R, the source, target corner, and amplification form are unchanged. Together with the universal choices in node 1.1 this establishes every clause of node 1.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

