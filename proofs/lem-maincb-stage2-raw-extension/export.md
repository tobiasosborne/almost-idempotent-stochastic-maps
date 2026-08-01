# Proof Export

## Node 1

**Statement:** After first fixing the universal C_s2^0,e_s2^0 witnesses of lem-maincb-stage2-extcb-datum, C_ext,e_ext witnesses of conj-extcb, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_2 < infinity and e_2 > 0 such that for every def-maincb-witness-ledger datum W with W.e_s2 <= min{e_s2^0,e_2}, C_s2^0*e_2 <= e_ext, and (C_ext+1)*C_s2^0*e_2 <= e_iso_unit, every explicit Stage-2 raw-call closed EXT-CB datum in A_R with total post-helper defect at most C_s2^0*t and 0 <= t <= W.e_s2 admits an extended D_2*t-isomorphism v_+:M_{r+1}->A_R satisfying ||v_+(I_{M_{r+1}})-u_{A_R}|| <= D_2*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Define e_2 := (1/2) min{1, e_s2^0, e_ext/C_s2^0, e_iso_unit/[C_s2^0(|C_ext+1|+1)]} and D_2 := 1 + C_s2^0(|C_ext| + |C_iso_unit|(|C_ext|+1)). These are positive/finite universal constants (in particular D_2<infinity and e_2>0), and elementary real arithmetic gives e_2<=e_s2^0, C_s2^0 e_2<=e_ext, and (C_ext+1)C_s2^0 e_2<=e_iso_unit. Moreover D_2>=C_ext C_s2^0 and D_2>=C_iso_unit(C_ext+1)C_s2^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix an arbitrary def-maincb-witness-ledger datum W and arbitrary explicit Stage-2 raw-call closed EXT-CB datum in A_R covered by node 1, with base scale 0<=t<=W.e_s2 and total post-helper defect e:=delta+epsilon_{A_R}<=C_s2^0 t. By def-extcb-datum and the precise output of lem-maincb-stage2-extcb-datum, A_R is a finite-dimensional extended epsilon_{A_R}-C*-algebra and its P,Q,v:M_r->S_P satisfy every hypothesis of conj-extcb. Also W.e_s2<=e_2 implies 0<=e<=C_s2^0 t<=C_s2^0 e_2<=e_ext.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Applying conj-extcb to the datum and smallness established in node 1.2 yields one map v_+:M_{r+1}->A_R whose every amplification is a C_ext e-isomorphism, hence v_+ is an extended C_ext e-isomorphism by def-extended-delta-inclusion. Since e<=C_s2^0 t and D_2>=C_ext C_s2^0, weakening the defect bounds at every amplification shows that v_+ is an extended D_2 t-isomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For the same v_+ supplied by node 1.3 put delta_+:=C_ext e. We split into two cases. If e=0, then epsilon_{A_R}=0 (both defects in e=delta+epsilon_{A_R} are nonnegative) and delta_+=0. Thus lem-maincb-isomorphism-unit-control applies with B=M_{r+1}, A=A_R and v=v_+ because 0<=delta_++epsilon_{A_R}=0<=e_iso_unit; it gives ||v_+(I_{M_{r+1}})-u_{A_R}||<=C_iso_unit*0=0<=D_2 t. Now suppose e>0. Since v_+ is a C_ext e-isomorphism by node 1.3, its two-sided level-one bounds applied to the nonzero identity of M_{r+1} give (1-C_ext e)||I||<=||v_+(I)||<=(1+C_ext e)||I||, whence C_ext e>=0 and therefore C_ext>=0. Consequently 0<=delta_++epsilon_{A_R}<=C_ext e+e=(C_ext+1)e<=(C_ext+1)C_s2^0 e_2<=e_iso_unit, using epsilon_{A_R}<=e, node 1.2, and node 1.1. Applying lem-maincb-isomorphism-unit-control to B=M_{r+1}, A=A_R, v=v_+ yields ||v_+(I_{M_{r+1}})-u_{A_R}||<=C_iso_unit(delta_++epsilon_{A_R})<=|C_iso_unit|(C_ext+1)C_s2^0 t<=D_2 t, where the middle inequality follows from the preceding nonnegative upper bound and the last from C_ext>=0 and the definition of D_2 in node 1.1. Thus the required unit estimate holds in both cases.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The choices in node 1.1 are independent of W,t,r and A_R. For every W and Stage-2 datum quantified in node 1, node 1.3 supplies the required extended D_2 t-isomorphism and node 1.4 supplies its required unit estimate. These two conclusions are witnessed by the same map v_+, so the existential conclusion and all universal quantifiers of node 1 follow.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

