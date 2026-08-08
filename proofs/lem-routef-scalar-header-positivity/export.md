# Proof Export

## Node 1

**Statement:** Route F scalar-header positivity: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K is finite with K >= 1, rho_fac > 0, and eta_K > 0, these scalars are universal and independent of H, Phi, eta, n, amplification level, simple-block count, and block dimensions, and eta_K <= rho_fac <= rho_2 <= rho_T <= rho_id^corr, rho_2 <= rho_Delta', rho_2 <= rho_Delta, rho_fac <= rho_DeltaUpsilon <= rho_Upsilon <= rho_Upsilon', rho_fac <= rho_mult, and rho_fac <= rho_UpsilonDelta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** The external lem-routef-raw-factor-setting-formation supplies a scalar header W_RF before all input quantifiers, independent of H, Phi, eta, dimension, amplification level, and block data, with eta_A>0, C_E finite, epsilon_E>0, C_theta=12*(sqrt(2)-1), C_A=20+(211/8)*C_theta, rho_theta=1/8, rho_AI=eta_A, and every remaining scalar defined by def-routef-raw-factor-setting equations (1.1)-(1.8).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every real scalar header W_RF having the primitive facts and definitions listed in node 1.1, equations (1.1)-(1.8) imply that K is finite with K>=1, rho_fac>0, and eta_K>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** The primitive layer is positive and finite: sqrt(2)>1 makes C_theta=12*(sqrt(2)-1)>0 and finite; hence C_A=20+(211/8)*C_theta>0 and finite. Since C_E is a finite real scalar, bar_C_E=max{1,C_E} is finite and at least 1, so C_V=bar_C_E*C_A and C_T=C_theta+3*C_V are positive and finite. Also rho_theta=1/8>0, rho_AI=eta_A>0, and epsilon_E/C_A>0; the two reciprocal entries in (1.1) have positive finite denominators. Thus every entry defining rho_T is positive, so rho_T>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Sequentially applying (1.2) to the positive finite quantities from node 1.2.1 gives rho_unit=rho_T>0, rho_id>0, rho_id^corr>0, rho_prod=rho_T>0, C_Delta'>0 finite, rho_Delta'>0, C_Delta>0 finite, rho_Delta>0, C_2>0 finite, rho_2>0, rho_DeltaPhi>0, C_3>0 finite, and rho_3>0: each new radius is a finite minimum of already-positive terms, and the only new reciprocal has denominator 2*(C_T+C_Delta')>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Equations (1.3)-(1.5), evaluated after node 1.2.2, give positive finite C_N,C_R,C_L,C_Upsilon', then rho_Upsilon'>0 because its six entries are positive (including (2*C_R)^(-1)); next C_Upsilon>0 finite and rho_Upsilon>0 because its entries are positive (including [2*(C_T+C_Upsilon')]^(-1)); finally rho_DeltaUpsilon, rho_mult, and rho_UpsilonDelta are positive as minima of positive radii.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** By (1.6), K is the maximum of finitely many finite real numbers and includes the entry 1, so K is finite and K>=1. Validated node 1.2.2 supplies rho_2>0, while validated node 1.2.3 supplies rho_DeltaUpsilon>0, rho_mult>0, and rho_UpsilonDelta>0. These are exactly the four entries in (1.7), hence rho_fac>0. Since K>=1, (24*K)^(-1)>0; therefore (1.8) makes eta_K=min{rho_fac,(24*K)^(-1),1}>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.4.1

**Statement:** By validated nodes 1.2.1, 1.2.2, and 1.2.3, the constituent scalars C_theta, C_Delta, C_2, and C_Upsilon are finite real numbers. Hence the three nonconstant expressions in (1.6), namely C_theta+C_Delta+2*C_Upsilon, C_Upsilon+2*(C_2+C_theta+C_Delta), and C_Upsilon+2*C_Delta, are finite real numbers. Therefore (1.6) defines K as the maximum of four finite real numbers: 1 and those three expressions. Thus K is finite; since 1 is one of the four entries, K>=1.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

##### Node 1.2.4.2

**Statement:** Validated node 1.2.2 gives rho_2>0, and validated node 1.2.3 gives rho_DeltaUpsilon>0, rho_mult>0, and rho_UpsilonDelta>0. These are exactly the four entries in (1.7), so their finite minimum rho_fac is strictly positive.

**Type:** claim

**Inference:** by_definition

**Status:** archived

**Taint:** clean

##### Node 1.2.4.3

**Statement:** From child 1.2.4.1, K>=1, so 24*K>=24>0 and therefore the real reciprocal (24*K)^(-1)>0. From child 1.2.4.2, rho_fac>0, while 1>0. Thus all three entries of the minimum in (1.8) are strictly positive, and consequently eta_K=min{rho_fac,(24*K)^(-1),1}>0. Together with 1.2.4.1 and 1.2.4.2 this proves the statement of node 1.2.4.

**Type:** claim

**Inference:** by_definition

**Status:** archived

**Taint:** clean

##### Node 1.2.4.4

**Statement:** Validated node 1.2.2 gives rho_2>0, and validated node 1.2.3 gives rho_DeltaUpsilon>0, rho_mult>0, and rho_UpsilonDelta>0. These are exactly the four entries of (1.7), so their finite minimum rho_fac is strictly positive. By child 1.2.4.1, K>=1; hence 24*K>=24>0 and the real reciprocal (24*K)^(-1)>0. Since also 1>0, every entry of the minimum in (1.8) is strictly positive, so eta_K=min{rho_fac,(24*K)^(-1),1}>0. Together with child 1.2.4.1 this proves every conclusion of node 1.2.4.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every scalar header governed by def-routef-raw-factor-setting equations (1.1)-(1.8), the coordinate inequalities for the displayed finite minima imply eta_K<=rho_fac<=rho_2<=rho_T<=rho_id^corr, rho_2<=rho_Delta', rho_2<=rho_Delta, rho_fac<=rho_DeltaUpsilon<=rho_Upsilon<=rho_Upsilon', rho_fac<=rho_mult, and rho_fac<=rho_UpsilonDelta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Equation (1.8) gives eta_K<=rho_fac, and (1.7) gives rho_fac<=rho_2. Equation (1.2) gives rho_2<=rho_prod=rho_T, rho_2<=rho_Delta', and rho_2<=rho_Delta. Finally rho_T is the minimum in (1.1) of the three entries rho_theta, rho_AI, epsilon_E/C_A together with two more entries, whereas rho_id^corr=min{rho_theta,rho_AI,epsilon_E/C_A}; hence rho_T<=each of the three entries and therefore rho_T<=rho_id^corr.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Equation (1.7) gives rho_fac<=rho_DeltaUpsilon. Equation (1.5) gives rho_DeltaUpsilon<=rho_Upsilon. The definition of rho_Upsilon in (1.5) includes rho_Upsilon' among its minimum entries, so rho_Upsilon<=rho_Upsilon'. Thus rho_fac<=rho_DeltaUpsilon<=rho_Upsilon<=rho_Upsilon'.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** The two remaining coordinate inequalities follow directly from (1.7), whose minimum entries include rho_mult and rho_UpsilonDelta: rho_fac<=rho_mult and rho_fac<=rho_UpsilonDelta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Because W_RF is chosen independently before every input quantifier and all K, rho_fac, and eta_K are obtained from its scalar fields alone by the fixed formulas (1.1)-(1.8), these three scalars are universal and independent of H, Phi, eta, n, amplification level, simple-block count, and block dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

