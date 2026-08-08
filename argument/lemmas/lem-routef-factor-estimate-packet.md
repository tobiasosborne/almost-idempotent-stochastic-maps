---
id: lem-routef-factor-estimate-packet
kind: lemma
contract: Relative Route F factor-estimate packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; for every same-datum packet (B,S,Delta',Delta,Upsilon',Upsilon) supplied for this (W_RF,n,Q,eta,D,J,Q_C,Phi) by lem-routef-factor-map-packet, ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||; moreover 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.
defs: def-routef-raw-factor-setting; def-stochastic; def-almost-idempotent; def-ucp-map
deps: lem-routef-scalar-header-positivity; lem-routef-factor-map-packet; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope; lem-routef-k-finiteness; lem-routef-threshold-minimum
status: stated
af: none
provenance: The byte-frozen telescope and rows 13/14 interfaces audited in AUDIT-KLEDGER-STRENGTHENED.md findings 5-9; first-class cap factoring and same-packet projection designed in DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile audit and user ratification.
owner: A
workspace: proofs/lem-routef-factor-estimate-packet
---

**Status.** `stated`, `af: none`. This helper projects the three telescope estimates and
the terminal arithmetic for one packet; it promotes nothing at landing.

**Packet-conditional rows stay packet-conditional.** Rows 13 and 14 are invoked only
after `lem-routef-factor-map-packet` has fixed the exact serial packet required by their
frozen prefixes. Their conclusions are not used to establish the earlier pre-forall
positivity; that role belongs solely to [[lem-routef-scalar-header-positivity]].

**Coefficient and level-one boundary.** The three telescope coefficients are coordinate
entries of the maximum defining `K`. The amplified multiplicativity conclusion is kept
in full. Its later F2 use is the explicit definitional specialization
`M_1(B)=B`, `Delta_1=Delta`, and `Upsilon_1=Upsilon` recorded in the skeleton and census.

**Designed af budget.** Five designed nodes; honest live expectation 8--15 under the
observed 1.5--3x expansion; at most 4 rounds; hard cap 18. The 3x endpoint 15 is strictly
below 18.
