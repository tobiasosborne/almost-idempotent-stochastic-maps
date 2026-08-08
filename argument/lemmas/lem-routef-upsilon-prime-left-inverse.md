---
id: lem-routef-upsilon-prime-left-inverse
kind: lemma
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, and every componentwise package (m,(L_j,E_j,W_j,Sigma_j,U_js,p_js,C_j,xi_j,Lambda_j,Upsilon'_j)_{j=1}^m,F,V,Upsilon') supplied for (W_RF,S,Delta',Delta) by lem-routef-upsilon-prime-component-construction, with C_L:=C_2+C_3+2*C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every integer q >= 1, and every Y=(Y_1,...,Y_m) in M_q(B)=direct-sum_{j=1}^m M_q(B(L_j)), ||(Upsilon'_j)_q(Delta_q(Y))-Y_j|| <= C_L*eta*||Y|| for every j, and consequently ||(Upsilon' Delta-I_B)_q(Y)|| <= C_L*eta*||Y|| and ||Upsilon' Delta-I_B||_cb <= C_L*eta.
defs: def-routef-raw-factor-setting; def-ucp-map
deps: lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate; lem-routef-degree-three-estimate; lem-routef-upsilon-prime-component-construction
status: proved
af: validated
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 8 (TeX 2831-2895; K-ledger 228-245; audit 181-209); DESIGN-ROW8-FACTOR.md sects-2,4-6 (natural branch 1.5 factoring, 2026-08-08); TREE-ROW8-ABORTED.md balloon-abort classification (2026-08-08: 28 live nodes exceeded NODE_SOFT_CAP 26)
owner: A
workspace: proofs/lem-routef-upsilon-prime-left-inverse
---

**Status.** `stated` design transcription only.  This shard promotes nothing and may not
be seeded before fresh hostile audit, user ratification, and af validation of
[[lem-routef-upsilon-prime-component-construction]].

**Ambient binding.** The contract repeats the family's complete global-W_RF-first and
per-input-S binding, then quantifies `Delta'`, `Delta`, and every component package from
their declared providers.  Thus no amplification, block, or construction symbol relies on
the design preamble.

**Factoring role.** This row contains exactly old branch 1.5.  It exports both the
component estimate and the cb estimate so the frozen main row can use it as a black box.
Probability weights and the direct-sum maximum norm introduce no multiplicity, block-count,
or amplification factor.

**Designed af budget.** Five nodes; honest live expectation 8--15 nodes under the observed
1.5--3x expansion; at most 4 rounds; hard cap 20.  A cap hit is a new factoring stop, not
permission to enlarge the cap.
