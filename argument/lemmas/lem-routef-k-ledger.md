---
id: lem-routef-k-ledger
kind: lemma
contract: Relative Route F factorization-and-finish ledger: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K >= 1 and eta_K > 0 are universal and independent of n, amplification level, simple-block count, and block dimensions, and for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then there exist a finite-dimensional unital C*-algebra B and UCP maps Delta: B -> M_n and Upsilon: M_n -> B such that ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||, and the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
defs: def-routef-raw-factor-setting; def-stochastic; def-almost-idempotent; def-ucp-map
deps: lem-routef-f0-ucp-lift; lem-routef-f0-defect-identity; lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope; lem-routef-k-finiteness; lem-routef-threshold-minimum; lem-routef-f2-positive-unital-compression; lem-routef-f3-retract-defect; lem-routef-prh-finish; lem-routef-scalar-header-positivity; lem-routef-factor-map-packet; lem-routef-factor-estimate-packet
status: stated
af: none
provenance: Strengthened replacement required by docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md sect-1.3 and corrected by AUDIT-F0-ASSEMBLY.md findings 1 and 3 (new fully quantified parent proof obligation, canonical Q_C typing); dependency/application rescope fixed by docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-6.2 and hostile re-audit AUDIT-LEDGER-SETTING-RESCOPE-V2.md; row-8 factoring interface from docs/plans/2026-08-08-ROW8-FACTOR/DESIGN-ROW8-FACTOR.md and its landed T0 rows; exact landing package proposed by DESIGN-KLEDGER-STRENGTHENED.md, pending its required fresh hostile audit and user ratification. That v1 package was REJECTED by AUDIT-KLEDGER-STRENGTHENED.md findings 1-4; its cleared findings 5-14 and exact public contract are retained, while cap factoring, quantifier scope, provisioning census, and report manifest are repaired by DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile re-audit and user ratification. Supersedes the narrower W74F proved-mod-audit paper-ledger contract recorded in docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md, PROOF-W74F-H-STAGE1.md, VERDICT-W74F-G-KLEDGER.md, and VERDICT-W74F-H-STAGE1.md; that historical verdict does not transfer status to this strengthened statement.
owner: A
workspace: proofs/lem-routef-k-ledger
---

**Status.** `stated`, `af: none`. This fully quantified statement is a strengthened
replacement and a new proof obligation. It is not a wording repair of the W74F paper
ledger, and no part of the old `proved-mod-audit` status is inherited. Landing this shard
promotes no mathematics.

**Closed input seam.** The public contract retains the exact F0 typing and all 15 original
T0 dependencies. The three appended helpers are proof modules, not new mathematical
assumptions: the scalar helper fixes the formation witness and its universal positive
scalars before every input; the map-packet helper fixes one serial packet for each input;
and the estimate-packet helper exports the three common-`K` estimates for that same packet.

**Same-datum application order.** Apply the dependencies in the following order, without
reselecting any datum:

