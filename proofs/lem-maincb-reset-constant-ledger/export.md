# Proof Export

## Node 1

**Statement:** After first fixing e_it,K_disp,K_floor from lem-maincb-improvement-iteration, epsilon_max^cb,delta_max^cb,c0^0 from lem-maincb-error-improvement, C_unit,epsilon_unit,delta_unit,a_unit from lem-maincb-reset-invariant-preservation, a valid enlarged c0 >= max{c0^0,K_floor,C_unit*(K_floor+1)}, L^0,e_env^0 from lem-maincb-direct-corner-envelope for this c0, e_full from lem-maincb-full-corner-identification, e_sim from lem-maincb-corner-equivalence, D_0,e_0 from lem-maincb-initial-raw-inclusion, D_1,e_1,K_1^0 from lem-maincb-stage1-call-envelope, C_s2^0,e_s2^0 from lem-maincb-stage2-extcb-datum, D_2,e_2 from lem-maincb-stage2-raw-extension, K_2^0 from lem-maincb-stage2-call-envelope, C_cross^0,e_cross^0 from lem-maincb-cross-class-merging-datum, D_3,e_3 from lem-maincb-stage3-raw-merge, and K_3^0 from lem-maincb-stage3-call-envelope, set D_* = max{1,D_0,D_1,D_2,D_3}; then there exists one def-maincb-witness-ledger datum W supplied by lem-maincb-witness-arithmetic with W.c0_cb=c0, W.L>=L^0, W.K1>=K_1^0, W.K2>=max{K_2^0,1,W.L,W.c0_cb*W.L}, W.K3>=max{K_3^0,1,W.L,W.c0_cb*W.L}, W.e_env<=e_env^0, W.e1<=e_1, W.e_s2<=min{e_s2^0,e_2}, and W.e_cross<=min{e_cross^0,e_3}, such that under the respective producer hypotheses at base scale 0 <= t <= W.r_reset and target ambient defect at most t, the literal maps u_0:C->A furnished by lem-maincb-initial-raw-inclusion and u_1:C^{m+1}->A furnished by lem-maincb-stage1-call-envelope with lem-maincb-stage1-raw-refinement are extended D_*t-inclusions, the literal maps u_2:M_{r+1}->A_R furnished by lem-maincb-stage2-call-envelope with lem-maincb-stage2-raw-extension and u_3:B_U oplus B_V->A_R furnished by lem-maincb-stage3-call-envelope with lem-maincb-stage3-raw-merge are extended D_*t-isomorphisms, and ||u_0(I_C)-I_A||,||u_1(I_{C^{m+1}})-I_A||,||u_2(I_{M_{r+1}})-u_{A_R}||,||u_3(I_{B_U oplus B_V})-u_{A_R}|| <= D_*t, so each satisfies the M02/M03 and near-unit thresholds and is eligible for lem-maincb-reset-invariant-preservation; all selected witnesses are universal and independent of dimension, amplification, block data, class count, and stage index.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** For the receiving arguments of lem-maincb-witness-arithmetic choose L:=L^0, K_1:=K_1^0, K_2:=max{K_2^0,1,L^0,c0*L^0}, K_3:=max{K_3^0,1,L^0,c0*L^0}, e_env:=e_env^0, e_1(receiving):=e_1, e_s2:=min{e_s2^0,e_2}, and e_cross:=min{e_cross^0,e_3}, while retaining the already fixed c0 and all other named provider witnesses. These choices are positive finite universal witnesses and satisfy K_2,K_3>=max{1,L,c0*L}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Set D_*:=max{1,D_0,D_1,D_2,D_3}. Apply lem-maincb-witness-arithmetic to the fixed witnesses and the receiving choices of the preceding step. It supplies one def-maincb-witness-ledger datum W with W.c0_cb=c0, W.L=L^0, W.K1=K_1^0, W.K2=max{K_2^0,1,L^0,c0*L^0}, W.K3=max{K_3^0,1,L^0,c0*L^0}, W.e_env=e_env^0, W.e1=e_1, W.e_s2=min{e_s2^0,e_2}, W.e_cross=min{e_cross^0,e_3}, and with W.r_reset and W.epsilon_MAIN given by the formulas in lem-maincb-witness-arithmetic.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The exact field identities furnished by lem-maincb-witness-arithmetic imply W.L>=L^0, W.K1>=K_1^0, W.K2>=max{K_2^0,1,W.L,W.c0_cb*W.L}, W.K3>=max{K_3^0,1,W.L,W.c0_cb*W.L}, W.e_env<=e_env^0, W.e1<=e_1, W.e_s2<=min{e_s2^0,e_2}, and W.e_cross<=min{e_cross^0,e_3}. The same external states that every field of W is positive, finite, universal, and independent of dimension, amplification, block data, class count, and stage index; the fixed provider witnesses and the displayed finite max/min choices have the same independence.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** By the definition of D_* and the exact W.r_reset formula supplied by lem-maincb-witness-arithmetic, D_*>=1 and D_*>=D_i for i=0,1,2,3, while W.r_reset<=min{e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb/D_*,e_it/(D_*+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D_*),[2*(1+K_disp)*D_*]^{-1}}. Hence every 0<=t<=W.r_reset obeys all these provider thresholds, including D_*t<=delta_max^cb and (D_*+1)t<=e_it.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Under the global-scalar producer hypotheses with target ambient defect epsilon_A<=t<=W.r_reset, lem-maincb-initial-raw-inclusion applies because t<=e_0 and furnishes u_0(lambda)=lambda*I_A as an extended D_0*t-inclusion. Since D_0*t<=D_*t, lem-maincb-extended-inclusion-monotone makes this same map with the same amplification family an extended D_*t-inclusion. Moreover u_0(I_C)=I_A exactly, so ||u_0(I_C)-I_A||=0<=D_*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Under the respective Stage-1 producer hypotheses, write the raw-call scale as t=t_1=W.K1*epsilon, with 0<=t<=W.r_reset and epsilon<=W.e1/W.K1. The construction certified by lem-maincb-stage1-call-envelope, using lem-maincb-stage1-raw-refinement, furnishes the literal u_1:C^{m+1}->A as an extended D_1*t-inclusion and gives ||u_1(I_{C^{m+1}})-I_A||<=D_1*t. Since D_1*t<=D_*t, lem-maincb-extended-inclusion-monotone and scalar transitivity give the asserted extended D_*t-inclusion and unit bound for the same literal map and amplification family.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Under the respective Stage-2 producer hypotheses, put t=t_2=W.K2*epsilon. Lem-maincb-stage2-call-envelope applies with W.L>=L^0, W.K2>=max{K_2^0,1,W.L,W.c0_cb*W.L}, and W.e_s2<=e_s2^0, and, using lem-maincb-stage2-extcb-datum, furnishes the explicit closed Stage-2 EXT-CB datum in A_R with target ambient record epsilon_R=W.L*epsilon<=t and total post-helper defect at most C_s2^0*t. The producer smallness epsilon<=W.e_s2/W.K2 gives 0<=t<=W.e_s2, and W.e_s2<=min{e_s2^0,e_2} supplies the receiving condition required by lem-maincb-stage2-raw-extension.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Apply lem-maincb-stage2-raw-extension to the Stage-2 datum just furnished and choose one resulting extended D_2*t-isomorphism v_+:M_{r+1}->A_R with ||v_+(I_{M_{r+1}})-u_{A_R}||<=D_2*t. Construct the composite Stage-2 raw-call record whose literal output is u_2:=v_+; this is a definition inside the newly constructed record, not an identification with a prior opaque output. Since D_2*t<=D_*t, lem-maincb-extended-inclusion-monotone makes this same u_2 an extended D_*t-isomorphism, in particular an extended D_*t-inclusion, and the unit estimate weakens to D_*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Under the respective Stage-3 producer hypotheses, put t=t_3=W.K3*epsilon. Lem-maincb-stage3-call-envelope applies with W.L>=L^0, W.K3>=max{K_3^0,1,W.L,W.c0_cb*W.L}, and W.e_cross<=e_cross^0, and, using lem-maincb-cross-class-merging-datum, furnishes the explicit amplified Stage-3 four-corner datum in A_R with target ambient record epsilon_R=W.L*epsilon<=t and common defect rho<=C_cross^0*t. The producer smallness epsilon<=W.e_cross/W.K3 gives 0<=t<=W.e_cross, and W.e_cross<=min{e_cross^0,e_3} supplies the receiving condition required by lem-maincb-stage3-raw-merge.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.10

**Statement:** For the Stage-3 branch, unpack the root phrase "under the respective producer hypotheses" as the hypotheses required by both named providers lem-maincb-stage3-call-envelope and lem-maincb-stage3-raw-merge. Thus the fixed C_cross^0,e_cross^0 are the particular cross-class-merging witnesses in the witness chain under which the already fixed D_3,e_3 are furnished by lem-maincb-stage3-raw-merge, and the Stage-3 datum furnished in node 1.9 is additionally assumed to have the finite-dimensional source and target data and four bijective fixed level-one corner maps required by that external. Apply lem-maincb-stage3-raw-merge to obtain an extended D_3*t-isomorphism v:B_U oplus B_V->A_R with ||v(I_{B_U oplus B_V})-u_{A_R}||<=D_3*t. Define the composite raw-call output u_3:=v. Since D_3*t<=D_*t, lem-maincb-extended-inclusion-monotone makes u_3 an extended D_*t-isomorphism (hence inclusion), and its unit estimate is at most D_*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.10.1

**Statement:** The constants are not freely rebound at this step. In the root witness-fixing order, D_3,e_3 are explicitly fixed from lem-maincb-stage3-raw-merge after C_cross^0,e_cross^0. The cited external furnishes D_3,e_3 only for the particular C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum that it stipulates are furnished by lem-maincb-cross-datum-bijectivity. Therefore any witness package satisfying the root antecedent "D_3,e_3 from lem-maincb-stage3-raw-merge" uses that same particular C_cross^0,e_cross^0 pair. This is specialization to the witness chain already contained in the allowed lem-maincb-stage3-raw-merge statement, not a new invocation of the absent bijectivity lemma.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.10.2

**Statement:** Likewise, no bijectivity conclusion is inferred from node 1.9. The root qualifies all four map conclusions by "under the respective producer hypotheses" and describes u_3 as furnished by lem-maincb-stage3-call-envelope with lem-maincb-stage3-raw-merge. For this Stage-3 composite producer, the respective hypotheses are the conjunction of the call-envelope hypotheses and the raw-merge hypotheses. Hence they explicitly include that B_U and B_V are finite-dimensional C*-algebras, A_R is a finite-dimensional extended epsilon_R-C*-algebra, and the four fixed level-one corner maps of the datum are bijective. Node 1.9 supplies the remaining raw-merge premises: the explicit datum furnished by lem-maincb-cross-class-merging-datum, epsilon_R<=t, rho<=C_cross^0*t, and 0<=t<=W.e_cross; node 1.3 supplies W.e_cross<=min{e_cross^0,e_3}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.10.3

**Statement:** All hypotheses of lem-maincb-stage3-raw-merge are therefore present under this explicitly unpacked Stage-3 case, so it yields v with the asserted D_3*t isomorphism and unit bounds. Set u_3:=v in the composite raw-call record. From D_3<=D_* and t>=0, D_3*t<=D_*t; lem-maincb-extended-inclusion-monotone preserves isomorphism for the same map and amplification family, and transitivity weakens the unit bound from D_3*t to D_*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.11

**Statement:** For each of the four newly constructed raw calls, the preceding conclusions give a finite-dimensional C*-algebra source, the unchanged target corner and amplification family, target ambient defect at most t, an extended D_*t-inclusion, and unit error at most D_*t, with D_*>=1 and 0<=t<=W.r_reset. The chosen c0 satisfies c0>=max{c0^0,K_floor,C_unit*(K_floor+1)}, and the reset-radius inequalities above are exactly those required by lem-maincb-reset-invariant-preservation with D=D_*. Thus that external applies to each call (preserving bijectivity for u_2 and u_3), so all four satisfy the M02/M03 and near-unit thresholds and are eligible for reset; together with the constructed W and the four map conclusions, this establishes the root claim.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

