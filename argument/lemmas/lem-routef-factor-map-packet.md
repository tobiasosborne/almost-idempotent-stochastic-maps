---
id: lem-routef-factor-map-packet
kind: lemma
contract: Relative Route F factor-map packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then Phi is UCP with ||Phi^2-Phi||_cb <= eta, and there exist a finite-dimensional unital C*-algebra B, one def-routef-raw-factor-setting datum S over this same W_RF supplied by lem-routef-raw-factor-setting-formation for the same (H:=C^n,Phi,eta) whose B-field is B, CP maps Delta':B->M_n and Upsilon':M_n->B, and UCP maps Delta:B->M_n and Upsilon:M_n->B such that Delta' is supplied for (W_RF,S) by lem-routef-delta-prime-closeness, Delta is supplied from that same Delta' by lem-routef-delta-normalization-closeness, Upsilon' is supplied from that same (Delta',Delta) by lem-routef-upsilon-prime-closeness, and Upsilon is supplied from that same (Delta',Delta,Upsilon') by lem-routef-upsilon-normalization-closeness.
defs: def-routef-raw-factor-setting; def-stochastic; def-almost-idempotent; def-ucp-map
deps: lem-routef-scalar-header-positivity; lem-routef-f0-ucp-lift; lem-routef-f0-defect-identity; lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness
status: proved
af: validated
provenance: The byte-frozen F0, formation, and rows 5/6/8/9 interfaces audited in AUDIT-KLEDGER-STRENGTHENED.md findings 5-9; first-class cap factoring designed in DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile audit and user ratification.
owner: A
workspace: proofs/lem-routef-factor-map-packet
---

**Status.** `proved`, `af: validated` (2026-08-08): root node 1 validated/clean first
pass, 16-node tree all validated/clean, fresh codex provers with separate fresh hostile
verifiers per node, cap 18 held; external oracle `af-lem-routef-factor-map-packet` +
`fr verify` PASS. Mechanical reflection of the codex ledger.

**Same-datum prefix.** The scalar helper selects one `W_RF` before every input. For one
arbitrary `n,Q,eta`, the F0 rows produce the exact same `Phi`; formation is instantiated
once at `H=C^n`; rows 5, 6, 8, and 9 are then applied serially. Every witness is explicitly
qualified by its provider, so no map or packet may be reselected.

**15-versus-16 boundary.** Row 8's public contract supplies the CP `Upsilon'` consumed by
row 9. This helper never opens the component package and has no dependency on
`lem-routef-upsilon-prime-component-construction`.

**Designed af budget.** Five designed nodes; honest live expectation 8--15 under the
observed 1.5--3x expansion; at most 4 rounds; hard cap 18. The 3x endpoint 15 is strictly
below 18.
