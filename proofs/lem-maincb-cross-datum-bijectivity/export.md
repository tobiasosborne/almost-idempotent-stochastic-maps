# Proof Export

## Node 1

**Statement:** After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, and fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, there are universal C_cross^0 >= 1 and 0 < e_cross^0 <= e_corner_unit which are valid witnesses of lem-maincb-cross-class-merging-datum such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0 and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has disjoint nonempty unions U,V sharing no class and R=U union V, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy epsilon_U,epsilon_V,d_U,d_V <= t <= W.e_cross, d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= t, and ||v_V(I_{B_V})-u_{A_V}|| <= t, then, writing B_R:=B_U oplus B_V, q_U:=(I_{B_U},0), q_V:=(0,I_{B_V}), P_X^R:=Co^A_{P_R}(P_X) for X in {U,V}, gamma_UU:q_U B_R q_U->S^{A_R}_{P_U^R} defined by gamma_UU((b_U,0)):=Co^{A_R}_{P_U^R}(Co^A_{P_R}(v_U(b_U))), gamma_VV:q_V B_R q_V->S^{A_R}_{P_V^R} defined by gamma_VV((0,b_V)):=Co^{A_R}_{P_V^R}(Co^A_{P_R}(v_V(b_V))), gamma_UV:q_U B_R q_V={0}->S^{A_R}_{P_U^R,P_V^R}={0} the unique map, and gamma_VU:q_V B_R q_U={0}->S^{A_R}_{P_V^R,P_U^R}={0} the unique map, the explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum has these four fixed level-one maps and gamma_UU,gamma_UV,gamma_VU,gamma_VV are bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Use lem-maincb-error-improvement to choose its universal coefficient witness c0 at least 1 (enlarging a witness preserves an inclusion bound by monotonicity), then fix the corresponding L,e_env witnesses of lem-maincb-direct-corner-envelope and the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison. By lem-maincb-cross-class-merging-datum obtain C_* >= 1 and 0 < e_* <= e_corner_unit; by lem-maincb-outer-compression-transfer obtain C_out and e_out > 0; and by lem-maincb-cross-union-zero-corners obtain e_zero > 0. Put K:=max(c0,L,1), C_cross^0:=C_*, and e_cross^0:=min(e_*,e_zero,e_env,e_out/K,1/(2*K)). These are universal, C_cross^0 >= 1 and 0 < e_cross^0 <= e_corner_unit. They remain valid witnesses of lem-maincb-cross-class-merging-datum because replacing e_* by a smaller positive threshold only restricts the data W satisfying W.e_cross <= the threshold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix arbitrary W,A,w,U,V,R,v_U,v_V satisfying the root hypotheses for the witnesses chosen in 1.1. Since W.e_cross <= e_cross^0 <= e_*, every hypothesis of lem-maincb-cross-class-merging-datum holds. That lemma therefore furnishes in A_R its explicit Stage-3 amplified four-corner datum, with common defect rho <= C_cross^0*t, using the nested-corner, outer-compression, compressed-corner-unit-comparison, and zero-cross-corner constructions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The fixed U,U level-one map in the datum of 1.2 is the displayed gamma_UU, and gamma_UU is bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Set s:=K*t with K=max(c0,L,1) from 1.1. Since A has defect epsilon_A<=t, it is an extended t-C*-algebra; since c0>=1, the extended t-inclusion w is also an extended c0*t-inclusion. As t<=e_cross^0<=e_env, lem-maincb-direct-corner-envelope applied with epsilon=t gives P_R and P_U as c0*t-projections, A_R=S^A_{P_R}, and both subordination errors of P_U to P_R at most L*t. Thus A is an extended s-C*-algebra, P_R and P_U are s-projections, and those errors are at most s. Moreover R is nonempty and the level-one two-sided norm bound for w gives 1-t <= ||P_R||=||w(1_R)|| <= 1+t; together with the s-projection property this is the nonvanishing alternative of def-delta-projection. Finally the supplied reset isomorphism v_U:B_U->A_U=S^A_{P_U} is an extended d_U-isomorphism and hence an extended s-isomorphism because d_U<=t<=s. Also s=K*t<=K*e_cross^0<=e_out. Therefore every hypothesis of lem-maincb-outer-compression-transfer holds for R=P_R, P=P_U and parameter s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Use validated node 1.2 as an explicit transitive premise inherited through the parent node 1.3: the dependency list of 1.3 contains 1.2, and 1.2 establishes that the furnished Stage-3 datum uses the outer-compression construction. Independently, apply lem-maincb-outer-compression-transfer to validated node 1.3.1. It gives the explicit T_U=Co^{A_R}_{P_U^R} o Co^A_{P_R} o v_U:B_U->S^{A_R}_{P_U^R} as an extended C_out*s-isomorphism, hence T_U is bijective by def-extended-delta-inclusion. The canonical coordinate map iota_U:B_U->q_U B_R q_U, iota_U(b_U)=(b_U,0), is bijective, and the displayed root formula gives gamma_UU o iota_U=T_U, so gamma_UU=T_U o iota_U^{-1} is bijective. Finally, by the validated 1.2 premise, the datum is furnished using exactly this outer-compression construction; therefore T_U transported through iota_U is its fixed U,U level-one map, namely gamma_UU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The fixed V,V level-one map in the datum of 1.2 is the displayed gamma_VV, and gamma_VV is bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** With the same s:=K*t, apply lem-maincb-direct-corner-envelope as in 1.3.1, now to V subseteq R. It gives P_R and P_V as s-projections in the finite-dimensional extended s-C*-algebra A and both subordination errors of P_V to P_R at most s. The norm estimate 1-t <= ||P_R|| <= 1+t again makes P_R nonvanishing. The supplied reset isomorphism v_V:B_V->A_V=S^A_{P_V} is an extended d_V-isomorphism and hence an extended s-isomorphism because d_V<=t<=s. Finally s<=e_out by 1.1. Thus every hypothesis of lem-maincb-outer-compression-transfer holds for R=P_R, P=P_V and parameter s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Apply lem-maincb-outer-compression-transfer to 1.4.1. It gives T_V=Co^{A_R}_{P_V^R} o Co^A_{P_R} o v_V:B_V->S^{A_R}_{P_V^R} as an extended C_out*s-isomorphism and therefore a bijection. The canonical coordinate map iota_V:B_V->q_V B_R q_V, iota_V(b_V)=(0,b_V), is bijective, and the root definition gives gamma_VV o iota_V=T_V. Hence gamma_VV=T_V o iota_V^{-1} is bijective. Since the datum in 1.2 uses the explicit outer-compression construction, this T_V, transported through iota_V, is exactly its fixed V,V level-one map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The inequalities t <= W.e_cross <= e_cross^0 <= e_zero allow lem-maincb-cross-union-zero-corners to be applied to the fixed datum. Hence dim S^{A_R}_{P_U^R,P_V^R}=dim S^{A_R}_{P_V^R,P_U^R}=0, so both target cross-corners equal the zero vector space. Also B_R=B_U oplus B_V with q_U=(I_{B_U},0) and q_V=(0,I_{B_V}) gives q_U B_R q_V=q_V B_R q_U={0} by coordinatewise multiplication in a direct sum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** By 1.5, gamma_UV and gamma_VU are the unique maps from the zero vector space to the zero vector space. Each is bijective: its inverse is the same unique zero-to-zero map. These are exactly the fixed cross maps selected by the zero-cross-corner construction in the explicit datum of 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** For the arbitrary datum fixed in 1.2, that node supplies the required explicit Stage-3 amplified four-corner datum; 1.3 and 1.4 identify its two diagonal fixed maps with the displayed gamma_UU and gamma_VV and prove them bijective; and 1.5-1.6 identify its two cross fixed maps with the displayed gamma_UV and gamma_VU and prove them bijective. Since the datum was arbitrary and 1.1 supplies universal constants with all required inequalities and witness validity, the full root claim follows.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

