# Proof Export

## Node 1

**Statement:** After first fixing the universal C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum furnished by lem-maincb-cross-datum-bijectivity, C_merge,a_merge witnesses of lem-extcb-four-corner-merge, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_3 < infinity and e_3 > 0 such that for every def-maincb-witness-ledger datum W with W.e_cross <= min{e_cross^0,e_3}, (C_cross^0+1)*e_3 <= a_merge, and (C_merge*(C_cross^0+1)+1)*e_3 <= e_iso_unit, every explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum with source B_U oplus B_V, with B_U and B_V finite-dimensional C*-algebras, with A_R a finite-dimensional extended epsilon_{A_R}-C*-algebra, whose four fixed level-one corner maps are bijective, and with 0 <= rho <= C_cross^0*t and 0 <= epsilon_{A_R} <= t <= W.e_cross yields an extended D_3*t-isomorphism v:B_U oplus B_V->A_R satisfying ||v(I_{B_U oplus B_V})-u_{A_R}|| <= D_3*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By lem-maincb-cross-datum-bijectivity, fix universal C_cross^0 >= 1 and e_cross^0 > 0 that are valid witnesses for lem-maincb-cross-class-merging-datum. By lem-extcb-four-corner-merge and lem-maincb-isomorphism-unit-control fix their universal witnesses, taking the error coefficients C_merge and C_iso_unit nonnegative (replace either by its maximum with 0; enlarging a defect tolerance or the right side of a nonnegative norm estimate preserves the respective imported conclusion by def-extended-delta-inclusion). Put K:=C_merge*(C_cross^0+1), D_3:=max{K,C_iso_unit*(K+1)}, and e_3:=min{1,a_merge/(C_cross^0+1),e_iso_unit/(K+1)}. Then D_3<infinity and e_3>0 are universal, (C_cross^0+1)*e_3<=a_merge, and (C_merge*(C_cross^0+1)+1)*e_3<=e_iso_unit.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix an arbitrary W and an arbitrary explicit Stage-3 datum satisfying every hypothesis of node 1. Since t<=W.e_cross<=e_3, rho<=C_cross^0*t, and epsilon_{A_R}<=t, one has rho+epsilon_{A_R}<=(C_cross^0+1)*t<=(C_cross^0+1)*e_3<=a_merge. Thus this amplified four-corner merging datum, whose four fixed level-one maps are bijective, satisfies the smallness hypothesis of lem-extcb-four-corner-merge.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Apply lem-extcb-four-corner-merge to the datum of the preceding node. It yields a map v:B_U oplus B_V->A_R which is an extended delta-isomorphism for delta:=C_merge*(rho+epsilon_{A_R}).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The inequalities rho+epsilon_{A_R}<=(C_cross^0+1)*t and C_merge>=0 give 0<=delta<=K*t<=D_3*t. By the defining inequalities in def-extended-delta-inclusion, increasing a nonnegative defect parameter weakens the homomorphism-error bound and both two-sided norm bounds, while bijectivity is unchanged. Hence the map v from the preceding node is an extended D_3*t-isomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Moreover 0<=delta+epsilon_{A_R}<=(K+1)*t<=(K+1)*e_3<=e_iso_unit. Since B_U oplus B_V is a finite-dimensional C*-algebra and A_R is the stated finite-dimensional extended epsilon_{A_R}-C*-algebra, lem-maincb-isomorphism-unit-control applied to v gives ||v(I_{B_U oplus B_V})-I_{A_R}||<=C_iso_unit*(delta+epsilon_{A_R})<=C_iso_unit*(K+1)*t<=D_3*t. The designated unit I_{A_R} is the u_{A_R} appearing in node 1, so this is exactly the required unit estimate. Since W and the Stage-3 datum were arbitrary, the two conclusions prove node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

