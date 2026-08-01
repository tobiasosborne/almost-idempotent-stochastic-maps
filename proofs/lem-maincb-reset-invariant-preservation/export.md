# Proof Export

## Node 1

**Statement:** After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R satisfying d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, preserving bijectivity when u_R is bijective and leaving the source, target corner, and amplification form unchanged.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By GT-kitaev-prop-delta-hominc and its registered implicit small-parameter convention, there are universal constants 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 such that a delta-homomorphism from an exact C*-algebra into an epsilon-C*-algebra, with epsilon <= epsilon_unit, delta <= delta_unit, and unit distance at most a_unit, has unit distance at most C_unit*(delta+epsilon). The witnesses may be chosen with a_unit strictly below the positive threshold printed in the proposition.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every D,W and raw call in the root hypotheses, lem-maincb-improvement-iteration applies to the literal map u_R and furnishes one fixed map v_R:B_R->A_R, with (v_R)_n=I_n tensor v_R, sup_n ||(v_R)_n-(u_R)_n|| <= K_disp*D*t, and v_R an extended K_floor*epsilon_R-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Write d=D*t. From epsilon_R <= t and t <= W.r_reset <= e_it/(D+1), one has d+epsilon_R <= (D+1)*t <= e_it. The raw-call hypotheses also supply that B_R is a finite-dimensional C*-algebra, A_R is an extended epsilon_R-C*-algebra, and u_R is an extended d-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Apply lem-maincb-improvement-iteration with B=B_R, A=A_R, epsilon=epsilon_R, d=D*t, and v=u_R. Its single output is a map v_R:B_R->A_R having exactly the amplification family (v_R)_n=I_n tensor v_R, displacement sup_n ||(v_R)_n-(u_R)_n|| <= K_disp*D*t, and extended-inclusion defect K_floor*epsilon_R.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The same map v_R furnished in 1.2 satisfies d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For the map v_R of 1.2, the level-one displacement and the raw unit hypothesis give ||v_R(I_{B_R})-u_{A_R}|| <= K_disp*D*t+D*t=(1+K_disp)*D*t <= a_unit. Moreover epsilon_R <= t <= epsilon_unit and K_floor*epsilon_R <= max{1,K_floor}*t <= delta_unit.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** At amplification one, the extended K_floor*epsilon_R-inclusion v_R is a K_floor*epsilon_R-homomorphism from the exact C*-algebra B_R into the epsilon_R-C*-algebra A_R. Thus 1.1 and GT-kitaev-prop-delta-hominc give ||v_R(I_{B_R})-u_{A_R}|| <= C_unit*(K_floor+1)*epsilon_R <= W.c0_cb*epsilon_R. Also its inclusion defect satisfies d_R <= K_floor*epsilon_R <= W.c0_cb*epsilon_R.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** If the literal raw map u_R is bijective, then the same map v_R furnished in 1.2 is bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** If u_R is bijective, then for every x in B_R its extended D*t-inclusion lower norm bound and the level-one displacement in 1.2 imply ||v_R(x)|| >= ||u_R(x)||-||(v_R-u_R)(x)|| >= [1-(1+K_disp)*D*t]||x|| >= (1/2)||x||, using t <= [2*(1+K_disp)*D]^{-1}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** The bound in 1.4.1 makes v_R injective. Since u_R is a linear bijection from finite-dimensional B_R onto A_R, the spaces B_R and A_R have the same finite dimension; therefore the injective linear map v_R:B_R->A_R is surjective and hence bijective.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Taking the single map v_R from 1.2, the conclusions of 1.3 and 1.4 give the required error-improved map; its displayed signature and amplification identity leave B_R, A_R, and the amplification form unchanged. The fixed c0^0 witness from lem-maincb-error-improvement is absorbed by W.c0_cb >= c0^0, while no distinct existential output of that lemma is substituted for v_R.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

