# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images and has disjoint nonempty unions U,V sharing no class, and current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then there is a current reset isomorphism v_{U union V}:B_U oplus B_V->A_{U union V} whose recorded ambient field epsilon_{U union V} is selected so that A_{U union V} is an extended epsilon_{U union V}-C*-algebra and epsilon_{U union V} <= W.L*epsilon, and which satisfies d_{U union V} <= W.c0_cb*epsilon_{U union V} and ||v_{U union V}(I_{B_U oplus B_V})-u_{A_{U union V}}|| <= W.c0_cb*epsilon_{U union V}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Universal constants and scalar domain package: fix the universal witnesses in the order required by lem-maincb-reset-constant-ledger, use one common C_unit, epsilon_unit, delta_unit, a_unit witness package for the reset theorem, set D_*:=max{1,D_0,D_1,D_2,D_3}, and fix the supplied W. Then D_*>=1; W satisfies the coefficient, margin, Stage-3 producer, near-unit, and reset-radius requirements packaged by lem-maincb-reset-constant-ledger. Moreover lem-maincb-structural-domain-ledger gives, for every 0<=epsilon<=W.epsilon_MAIN, epsilon<=W.e_cross/W.K3 and t_3:=W.K3*epsilon satisfies 0<=t_3<=W.r_reset and t_3<=W.e_cross; also W.K3>=W.L from lem-maincb-reset-constant-ledger gives epsilon_R:=W.L*epsilon<=t_3. These choices are universal and datum-independent.

**Type:** claim

**Inference:** conjunction

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Assume the universal/scalar package just stated. Under the hypotheses of node 1, the asserted current reset isomorphism for R=U union V exists.

**Type:** claim

**Inference:** conjunction

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Apply lem-maincb-stage3-call-envelope with R:=U union V and t_3:=W.K3*epsilon. Its hypotheses are exactly the root hypotheses together with the scalar package: it selects the target ambient record epsilon_R:=W.L*epsilon, certifies A_R as an extended epsilon_R-C*-algebra, and furnishes the explicit Stage-3 amplified four-corner raw-call datum with rho<=C_cross^0*t_3. The same conclusion says t_3 dominates epsilon, epsilon_U, epsilon_V, d_U, d_V, epsilon_R, both displayed unit norms, and every other datum error, in particular 0<=W.c0_cb*epsilon<=t_3.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Assume the Stage-3 call package just stated. Then the asserted current reset isomorphism for R=U union V exists.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** The root hypothesis types w:C^m->A as an extended W.c0_cb*epsilon-inclusion, while the Stage-3 call package gives 0<=W.c0_cb*epsilon<=t_3. Since C^m is a finite-dimensional C*-algebra and A is a finite-dimensional extended epsilon-C*-algebra, lem-maincb-extended-inclusion-monotone applies and types this same w as an extended t_3-inclusion; its one-dimensional atomic images and the absence of any unitality assumption are unchanged.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Assume this extended t_3-inclusion typing of w, together with the Stage-3 call package and the root hypotheses. Then the asserted current reset isomorphism for R=U union V exists.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.2.2.2.1

**Statement:** Apply lem-maincb-cross-datum-bijectivity at t=t_3. The call package supplies epsilon<=t_3, epsilon_U,epsilon_V,d_U,d_V<=t_3, both unit bounds <=t_3, the explicit datum, and rho control; the scalar package supplies t_3<=W.e_cross and the required W witness inequalities; the root supplies disjoint nonempty U,V sharing no class and one-dimensional images; and the preceding typing supplies the required non-unital extended t_3-inclusion. Hence the four fixed level-one maps gamma_UU,gamma_UV,gamma_VU,gamma_VV in that explicit Stage-3 datum are bijective.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.2.2.2.2

**Statement:** Assume that the four fixed level-one maps of the explicit Stage-3 datum are bijective, together with the call and scalar packages. Then the asserted current reset isomorphism for R=U union V exists.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.2.2.2.2.1

**Statement:** Apply lem-maincb-stage3-raw-merge to the explicit datum: its source is B_U oplus B_V with finite-dimensional C*-algebra summands, its target is A_R, its four maps are bijective, and 0<=rho<=C_cross^0*t_3 with 0<=epsilon_R<=t_3<=W.e_cross. Using the same fixed witnesses, the Stage-3 producer conclusion packaged in lem-maincb-reset-constant-ledger names the resulting literal map u_3:B_U oplus B_V->A_R and gives that it is an extended D_*t_3-isomorphism with ||u_3(I_{B_U oplus B_V})-u_{A_R}||<=D_*t_3.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.2.2.2.2.2

**Statement:** For any such explicit Stage-3 raw call with target record epsilon_R, scale 0<=t_3<=W.r_reset, and literal map u_3 that is an extended D_*t_3-isomorphism with the displayed D_*t_3 unit bound, apply lem-maincb-reset-output-typing once with D=D_* and fix one resulting map v_R. By def-extended-delta-inclusion, u_3 being an extended isomorphism makes it bijective and in particular an extended D_*t_3-inclusion, so the typed-reset conclusion makes this same fixed v_R an extended W.c0_cb*epsilon_R-isomorphism, gives d_R<=W.c0_cb*epsilon_R and ||v_R(I_{B_U oplus B_V})-u_{A_R}||<=W.c0_cb*epsilon_R, and leaves source, target, and amplification form unchanged. Record this one v_R with R=U union V and epsilon_R=W.L*epsilon as the current reset state. Since A_R was certified extended epsilon_R-C*-algebra and epsilon_R=W.L*epsilon, all conclusions of node 1 follow.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

