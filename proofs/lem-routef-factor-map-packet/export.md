# Proof Export

## Node 1

**Statement:** Relative Route F factor-map packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then Phi is UCP with ||Phi^2-Phi||_cb <= eta, and there exist a finite-dimensional unital C*-algebra B, one def-routef-raw-factor-setting datum S over this same W_RF supplied by lem-routef-raw-factor-setting-formation for the same (H:=C^n,Phi,eta) whose B-field is B, CP maps Delta':B->M_n and Upsilon':M_n->B, and UCP maps Delta:B->M_n and Upsilon:M_n->B such that Delta' is supplied for (W_RF,S) by lem-routef-delta-prime-closeness, Delta is supplied from that same Delta' by lem-routef-delta-normalization-closeness, Upsilon' is supplied from that same (Delta',Delta) by lem-routef-upsilon-prime-closeness, and Upsilon is supplied from that same (Delta',Delta,Upsilon') by lem-routef-upsilon-normalization-closeness.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix once and for all the global header W_RF given by lem-routef-scalar-header-positivity.  For this same header, eta_K is universal and positive and the threshold consequences needed below are eta_K <= rho_id^corr, eta_K <= rho_Delta', eta_K <= rho_Delta, eta_K <= rho_Upsilon', and eta_K <= rho_Upsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For arbitrary n,Q,eta satisfying the hypotheses of node 1 and for the displayed D,J,Q_C,Phi, the two F0 interfaces imply that Phi is UCP and ||Phi^2-Phi||_cb <= eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By lem-routef-f0-ucp-lift, the map Phi=J Q_C D attached to the arbitrary row-stochastic Q and n>=1 in node 1 is UCP.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** By lem-routef-f0-defect-identity, ||Phi^2-Phi||_cb=||Q^2-Q||_{infinity->infinity}; the hypothesis ||Q^2-Q||_{infinity->infinity}<=eta therefore gives ||Phi^2-Phi||_cb<=eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the same fixed W_RF and arbitrary data from the preceding conditional step, lem-routef-raw-factor-setting-formation applies at H=C^n and supplies a finite-dimensional unital C*-algebra B and one datum S over this same W_RF for exactly (H=C^n,Phi,eta), with B-field B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Because n>=1, H=C^n is a nonzero finite-dimensional Hilbert space.  Node 1.2 gives that Phi is UCP and has cb defect at most eta, while 0<=eta<=eta_K and node 1.1 give eta<=rho_id^corr; hence every input hypothesis of lem-routef-raw-factor-setting-formation is met for this exact triple (C^n,Phi,eta) and the fixed W_RF.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Applying lem-routef-raw-factor-setting-formation once to that exact triple and the fixed W_RF supplies a finite-dimensional unital C*-algebra B and one def-routef-raw-factor-setting datum S over this same W_RF whose H,Phi,eta,B fields are exactly C^n,Phi,eta,B (along with its other asserted fields); retain this one S without reselection.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For every such formation datum S, the two Delta interfaces apply serially at eta and supply a CP map Delta':B->M_n and then, from that same Delta', a UCP map Delta:B->M_n, with the provider relations asserted in node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** From 0<=eta<=eta_K and node 1.1, eta<=rho_Delta' and eta<=rho_Delta; thus both Delta interfaces' radius hypotheses hold for the fixed header and the single formation datum S.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Apply lem-routef-delta-prime-closeness to (W_RF,S) at this eta.  It produces a CP map Delta':B->B(C^n)=M_n supplied for exactly (W_RF,S) by that lemma; fix this particular Delta'.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** Apply lem-routef-delta-normalization-closeness to the same (W_RF,S) and the particular Delta' from the preceding step.  It produces a UCP map Delta:B->B(C^n)=M_n supplied from that same Delta' by that lemma; fix this particular Delta without changing S or Delta'.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For the same S and the Delta',Delta just supplied, the two Upsilon interfaces apply serially at eta and supply a CP map Upsilon':M_n->B and then, from that same triple (Delta',Delta,Upsilon'), a UCP map Upsilon:M_n->B, with the provider relations asserted in node 1; combining these witnesses with the preceding steps proves node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** From 0<=eta<=eta_K and node 1.1, eta<=rho_Upsilon' and eta<=rho_Upsilon; thus both Upsilon interfaces' radius hypotheses hold for the same header, datum S, and fixed Delta',Delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Apply lem-routef-upsilon-prime-closeness to the same (W_RF,S) and the particular pair (Delta',Delta).  It produces a CP map Upsilon':B(C^n)=M_n->B supplied from exactly that pair by that lemma; fix this particular Upsilon'.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** Apply lem-routef-upsilon-normalization-closeness to the same (W_RF,S) and the particular triple (Delta',Delta,Upsilon').  It produces a UCP map Upsilon:B(C^n)=M_n->B supplied from exactly that triple by that lemma.  No witness has been reselected, so the B,S,Delta',Delta,Upsilon',Upsilon obtained in nodes 1.3-1.5 have precisely the common-provider relations and map types required by node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

