# Proof Export

## Node 1

**Statement:** After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, and fixing the D_1^0,e_1^0 witnesses of lem-maincb-stage1-raw-refinement, there are universal receiving witnesses K_1^0 >= 1, D_1 >= D_1^0, and e_1 > 0 with e_1 <= min{e_1^0,e_corner_unit} and every Stage-1 producer prerequisite absorbed, such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.K1 >= K_1^0, and W.e1 <= e_1, if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.e1/W.K1, w:C^m->A is a supplied extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, and some P_j=w(e_j) has dim S_{P_j}>1, then the three Stage-1 producers, lem-maincb-compressed-corner-unit-comparison, and literal old-side compression furnish the explicit Stage-1 raw call at t_1=W.K1*epsilon whose literal map u_1:C^{m+1}->A is an extended D_1*t_1-inclusion and satisfies ||u_1(I_{C^{m+1}})-I_A|| <= D_1*t_1, when m=1, u_1 is the supplied fresh C^2->A_fresh=S_{P_fresh} inclusion followed by the canonical amplified linear embedding A_fresh->A; lem-compcb-rectangular-product, lem-maincb-compressed-corner-unit-comparison, P_fresh=w(I_C), and the displayed incoming unit estimate furnish the asserted A-valued inclusion and unit bounds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Provider and receiving-witness selection: after fixing c0 from lem-maincb-error-improvement, fix L,e_env from lem-maincb-direct-corner-envelope for this c0, C_corner_unit,e_corner_unit from lem-maincb-compressed-corner-unit-comparison, D_1^0,e_1^0 from lem-maincb-stage1-raw-refinement, C_sc,e_sc from lem-compcb-single-compression-transfer, C_rect,e_rect from lem-compcb-rectangular-product, and C_proj,e_proj,C_np,e_np,C_pair,e_pair from the three named Stage-1 producers. Choose K_1^0 at least max{1,c0+1,L,C_sc*(c0+1),C_proj*L,C_np*L,C_pair*L}; choose e_1>0 no larger than min{e_1^0,e_corner_unit,e_env,e_sc,e_rect/2,e_proj,e_np,e_pair,1}; and choose D_1 at least D_1^0 and every finite coefficient occurring in the unit telescopes and the m=1 ambient-product transfer below. These choices are positive finite universal, absorb every displayed provider threshold and coefficient, and have e_1<=min{e_1^0,e_corner_unit}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Common scale and corner geometry: for an arbitrary receiving ledger W and datum in the root, put t_1=W.K1*epsilon, P_fresh=P_j, and, if m>1, P_old=sum_{k not equal j}w(e_k). Then 0<=t_1<=W.e1<=e_1, epsilon<=t_1, c0*epsilon<=t_1, and L*epsilon<=t_1. By lem-maincb-direct-corner-envelope, P_fresh and P_old (when present) are t_1-projections, their compressed corners are extended t_1-C*-algebras by monotonicity, P_old and P_fresh have every required subordination and complementarity defect at most t_1, and P_old+P_fresh=w(I_{C^m}); moreover A itself is an extended t_1-C*-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Fresh-side producers: the selected corner A_fresh=S_{P_fresh} has dimension greater than one and extended defect at most L*epsilon<=t_1<=e_1. Therefore lem-stage1-rectified-nontrivial-projection and lem-stage1-original-complementary-pair furnish their stated nontrivial and complementary t_1-controlled projection data, while lem-stage1-fresh-two-point-inclusion furnishes nonvanishing P_prime,P_doubleprime in A_fresh, P_prime+P_doubleprime=u_{A_fresh}, and a fixed-amplification map v_fresh:C^2->A_fresh which is an extended t_1-inclusion, has v_fresh(1,1)=u_{A_fresh}, and maps the two standard basis projections to that same pair. The coefficient and threshold absorptions follow from K_1^0>=C_proj*L,C_np*L,C_pair*L and e_1<=e_proj,e_np,e_pair; no identification of separately existential pairs is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Old-side literal compression when m>1: restrict w to the coordinate ideal C^{m-1} supported off j and follow it by the compatible amplified compression Co_{P_old}; call the resulting map v_old:C^{m-1}->S_{P_old}. Since the restriction is an extended c0*epsilon-inclusion and (c0+1)*epsilon<=t_1<=e_sc, lem-compcb-single-compression-transfer and K_1^0>=C_sc*(c0+1) make v_old an extended t_1-inclusion. Linearity gives w(I_{C^{m-1}})=P_old before compression, hence v_old(I_{C^{m-1}})=Co_{P_old}(P_old)=u_{S_{P_old}}. Applying lem-maincb-compressed-corner-unit-comparison at scale t_1 gives ||v_old(I_{C^{m-1}})-P_old||<=C_corner_unit*t_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The m>1 raw call and its two conclusions: use P_old,P_fresh, v_old,v_fresh and their fixed amplification families as the literal Stage-1 datum. All projection, complementarity, map, target-ambient and smallness defects are at most t_1, so lem-maincb-stage1-raw-refinement makes the literal sum map u_1:C^{m+1}->A an extended D_1^0*t_1-inclusion, hence an extended D_1*t_1-inclusion. Its unit is u_{S_{P_old}}+u_{S_{P_fresh}}; the first clause of lem-maincb-compressed-corner-unit-comparison applied to both projections, P_old+P_fresh=w(I_{C^m}), and the incoming estimate give ||u_1(I)-I_A||<=2*C_corner_unit*t_1+c0*epsilon<=D_1*t_1. Recording the call-type, supplied input map and amplifications, source, target A, base scale t_1, this literal output and amplifications, target defect epsilon, and raw defect D_1*t_1 is exactly the explicit def-maincb-raw-call record.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** The m=1 ambient-transfer branch: here P_fresh=w(I_C), A_fresh=S_{P_fresh}, and the supplied v_fresh:C^2->A_fresh is followed by the canonical amplified linear subspace embedding A_fresh->A to define u_1:C^2->A. This composite is an extended D_1*t_1-inclusion, obeys ||u_1(I_{C^2})-I_A||<=D_1*t_1, and supplies the explicit Stage-1 raw-call record at base scale t_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Ambient multiplicative, involution, and norm clauses for m=1: at every amplification the canonical embedding S_{P_fresh}->A is the operator-subspace inclusion, so it preserves linearity, involution, and all matrix norms. For X,Y in M_n(C^2), the multiplicative defect of the composite is bounded by the fresh map defect for the compressed product plus ||v_fresh,n(X) dot v_fresh,n(Y)-v_fresh,n(X)v_fresh,n(Y)||. The first term is at most t_1||X||||Y||. For the second, P_fresh is a c0*epsilon-projection in the extended epsilon algebra A, (c0+1)*epsilon<=t_1<=e_rect, and lem-compcb-rectangular-product applies to the compatible amplified pair; since t_1<=1 and the fresh extended t_1-inclusion has upper norm at most 1+t_1<=2, this term is at most 4*C_rect*t_1||X||||Y||. Thus all non-unit extended-inclusion clauses hold with the universal coefficient 1+4*C_rect.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** Ambient unit clause for m=1: u_1(I_{C^2})=v_fresh(1,1)=u_{S_{P_fresh}}. Since P_fresh is a t_1-projection in the extended t_1-algebra A and t_1<=e_corner_unit, lem-maincb-compressed-corner-unit-comparison gives ||u_{S_{P_fresh}}-P_fresh||<=C_corner_unit*t_1. Here P_fresh=w(I_C), so the displayed incoming estimate and c0*epsilon<=t_1 give ||u_1(I_{C^2})-I_A||<=C_corner_unit*t_1+c0*epsilon<=(C_corner_unit+1)*t_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.3

**Statement:** Ambient m=1 conclusion and raw-call packaging: choose D_1 in node 1.1 at least max{1+4*C_rect,C_corner_unit+1}. The two preceding nodes then show that the literal composite u_1:C^2->A is an extended D_1*t_1-inclusion and has the required displayed unit bound. Record the Stage-1 tag, supplied input w and amplification family, source C^2, target A, base and post-helper scale t_1, the literal composite and its amplifications, target ambient defect epsilon<=t_1, and raw defect D_1*t_1; by def-maincb-raw-call this is the required explicit raw-call record, and by construction u_1 is precisely the fresh corner inclusion followed by the canonical amplified embedding.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Case completion and universality: if m>1 use the raw call and bounds above; if m=1 use the ambient-transfer raw call above, with the old side absent exactly as in lem-maincb-stage1-raw-refinement. These exhaustive cases prove the root for every receiving W. All selected witnesses are finite expressions and finite minima of the universal witnesses of the cited externals, hence are universal and independent of m, dimension, amplification level, and the particular datum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

