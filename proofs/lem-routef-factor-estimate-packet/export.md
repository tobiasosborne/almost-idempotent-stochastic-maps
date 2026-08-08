# Proof Export

## Node 1

**Statement:** Relative Route F factor-estimate packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; for every same-datum packet (B,S,Delta',Delta,Upsilon',Upsilon) supplied for this (W_RF,n,Q,eta,D,J,Q_C,Phi) by lem-routef-factor-map-packet, ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||; moreover 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix the global W_RF supplied by lem-routef-scalar-header-positivity. For arbitrary root input (n,Q,eta,D,J,Q_C,Phi) and an arbitrary same-datum packet (B,S,Delta_prime,Delta,Upsilon_prime,Upsilon) supplied by lem-routef-factor-map-packet, that packet has the exact serial provenance required by the three telescope lemmas; K is finite, universal, and K >= 1, and 0 <= eta <= eta_K <= rho_fac <= rho_DeltaUpsilon, rho_mult, rho_UpsilonDelta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-routef-scalar-header-positivity, choose one global W_RF supplied by lem-routef-raw-factor-setting-formation. For its scalars (1.6)-(1.8), K is finite, universal, and K >= 1, while eta_K > 0 and eta_K <= rho_fac <= rho_DeltaUpsilon, rho_mult, rho_UpsilonDelta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For arbitrary n,Q,eta,D,J,Q_C,Phi satisfying the root hypotheses, lem-routef-factor-map-packet gives Phi the required UCP/defect properties and supplies a packet (B,S,Delta_prime,Delta,Upsilon_prime,Upsilon) over this same W_RF in the serial order: S is supplied by formation for (H:=C^n,Phi,eta), Delta_prime by delta-prime closeness, Delta from Delta_prime by delta normalization, Upsilon_prime from (Delta_prime,Delta) by upsilon-prime closeness, and Upsilon from that triple by upsilon normalization. Hence every same-datum packet quantified in the root has precisely this provenance.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** For any such same-datum packet, lem-routef-k-finiteness identifies rho_fac as a common domain for the three factorization estimates. Combining the root assumption 0 <= eta <= eta_K with 1.1.1 gives 0 <= eta <= rho_DeltaUpsilon, 0 <= eta <= rho_mult, and 0 <= eta <= rho_UpsilonDelta, while 1.1.2 gives every serial supply hypothesis required by lem-routef-delta-upsilon-telescope, lem-routef-multiplicative-telescope, and lem-routef-upsilon-delta-telescope.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every arbitrary root input and same-datum packet fixed in 1.1, ||Delta Upsilon-Phi||_cb <= K*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By the serial provenance and domain inequalities in 1.1, lem-routef-delta-upsilon-telescope applies to this same packet and gives ||Delta Upsilon-Phi||_cb <= (C_theta+C_Delta+2*C_Upsilon)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** By equation (1.6) in def-routef-raw-factor-setting, C_theta+C_Delta+2*C_Upsilon <= K. Since eta >= 0, multiplication preserves this inequality; combining it with 1.2.1 yields ||Delta Upsilon-Phi||_cb <= K*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every arbitrary root input and same-datum packet fixed in 1.1, ||Upsilon Delta-I_B||_cb <= K*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By the serial provenance and domain inequalities in 1.1, lem-routef-upsilon-delta-telescope applies to this same packet and gives ||Upsilon Delta-I_B||_cb <= (C_Upsilon+2*C_Delta)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** By equation (1.6) in def-routef-raw-factor-setting, C_Upsilon+2*C_Delta <= K. Since eta >= 0, multiplication preserves this inequality; combining it with 1.3.1 yields ||Upsilon Delta-I_B||_cb <= K*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For every arbitrary root input and same-datum packet fixed in 1.1, every integer r >= 1 and all X,Y in M_r(B) satisfy ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** By the serial provenance and domain inequalities in 1.1, lem-routef-multiplicative-telescope applies to this same packet; hence for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= [C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** By equation (1.6) in def-routef-raw-factor-setting, C_Upsilon+2*(C_2+C_theta+C_Delta) <= K. Since eta, ||X||, and ||Y|| are nonnegative, multiplication preserves this inequality; combining it with 1.4.1 proves the asserted estimate simultaneously for every r >= 1 and all X,Y in M_r(B).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For every arbitrary root input and same-datum packet fixed in 1.1, 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** For this same packet, lem-routef-threshold-minimum applies. Its eta_K is exactly equation (1.8), eta_K=min{rho_fac,(24*K)^(-1),1}; therefore the root assumption 0 <= eta <= eta_K gives 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

