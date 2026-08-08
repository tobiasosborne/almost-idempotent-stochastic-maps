---
id: lem-routef-upsilon-prime-component-construction
kind: lemma
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, with C_N, C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon' there exist an integer m >= 1, nonzero finite-dimensional Hilbert spaces L_j and E_j for 1 <= j <= m, a finite-dimensional Hilbert space F, operators W_j:H->L_j tensor E_j, an isometry V:H->H tensor F, nonempty finite index sets Sigma_j, unitaries U_js on L_j and weights p_js for s in Sigma_j, positive contractions C_j on E_j, unit vectors xi_j in E_j, contractions Lambda_j:L_j->H tensor F, CP maps Upsilon'_j:B(H)->B(L_j), and a CP map Upsilon':B(H)->B such that B=direct-sum_{j=1}^m B(L_j), sum_j W_j^*W_j=I_H, Delta(X)=sum_j W_j^*(X_j tensor I_Ej)W_j for every X=(X_1,...,X_m) in B, Phi(T)=V^*(T tensor I_F)V for every T in B(H), p_js >= 0, sum_{s in Sigma_j}p_js=1, sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)Z(U_js tensor I_Ej)=I_Lj tensor (Tr_Lj(Z)/dim(L_j)) for every Z in B(L_j tensor E_j), where Tr_Lj denotes the unnormalized partial trace over L_j, R_j:=sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)W_jW_j^*(U_js tensor I_Ej)=I_Lj tensor C_j, 0 <= C_j <= I_Ej, ||C_j|| >= 1-C_R*eta, 1-<xi_j,C_j^*C_j xi_j> <= 2*C_R*eta, if hat-U_js denotes U_js in the j-th block of B and zero in every other block and iota_js(z):=U_js z tensor xi_j then Lambda_j:=sum_{s in Sigma_j}p_js*(Delta(hat-U_js^*) tensor I_F)V W_j^*iota_js, Upsilon'_j(T):=Lambda_j^*(Phi(T) tensor I_F)Lambda_j, Upsilon'(T):=(Upsilon'_j(T))_{j=1}^m, and ||Upsilon'||_cb <= 1.
defs: def-routef-raw-factor-setting; def-ucp-map
deps: lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 8 (TeX 2831-2895; K-ledger 228-245; audit 181-209); DESIGN-ROW8-FACTOR.md sects-1,4-6 (natural branch 1.2-1.4 factoring, 2026-08-08); TREE-ROW8-ABORTED.md balloon-abort classification (2026-08-08: 28 live nodes exceeded NODE_SOFT_CAP 26)
owner: A
workspace: proofs/lem-routef-upsilon-prime-component-construction
---

**Status.** `stated` design transcription only.  This shard promotes nothing and may not
be seeded before fresh hostile audit and user ratification.

**Ambient binding.** The contract repeats the family's complete global-W_RF-first and
per-input-S binding.  `Delta'` and `Delta` are quantified from their declared providers;
all remaining scalar and map notation is carried by
[[def-routef-raw-factor-setting]] or defined in the contract itself.

**Factoring role.** This row contains exactly old branches 1.2--1.4: finite-dimensional
Stinespring/Choi data, an explicit Weyl twirl, the `(2*C_R)^(-1)` nonvanishing repair, and
the componentwise CP construction.  It exports the actual witness package consumed by
[[lem-routef-upsilon-prime-left-inverse]] and the frozen main row.

**Designed af budget.** Seven nodes; honest live expectation 11--21 nodes under the
observed 1.5--3x expansion; at most 5 rounds; hard cap 26.  A cap hit is a new factoring
stop, not permission to enlarge the cap.
