---
id: conj-w72-poti0-root-selection-exchange-ledger
kind: lemma
contract: Within the literal W72 POTI-0 hypothesis block of conj-dtr-zero-oriented-surplus-exclusion, with c_m = 1/4, b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), and with objects fixed in the order c_m -> (b,delta_rt) -> datum -> selected-corner certificate C* -> arbitrary clone-invariant row-point vertex kernel and arbitrary reduced display field -> full-fiber carrier set B -> (rho,t_phi,G_phi) -> arbitrary attained top-face ray certificate (Lambda,c), all measures being clone-invariant measures on the finite full row-point quotient, all coefficients signed, and all geometry row-point l1, if G_phi = 0 and r = rho(1) = 0, define eta_B(Q) = eta_D*(B cap Q), M_B = eta_B(1), C_B = {Q : eta_B(Q) > 0}, Q_* = Q_f*, w_* = m_A(Q_*), sigma_B = (P_v^+ - m_A)(C_B), and e_delta = 2*delta(P)*(1 + delta(P)); then sigma_B >= w_*M_B - e_delta.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull; def-invisible-mass
deps: lem-ihorn-cotop-sl1a-package; lem-ihorn-selected-corner-extraction; lem-dcap-root-closure; lem-dtr-canonical-overlap; lem-l5-positive-flow-foldback
status: proved-mod-audit
af: none
provenance: W72 POTI-0 wave (docs/waves/2026-07-16-W70-artifacts/): pinned statement POTI0-ATTACK-W72.md §1.3; standalone proof APPENDIX-W72-poti0-proofs.md §2; fresh hostile batched verdict VERDICT-poti0-batch.md line RX: VALID, including the partially selected clone-fiber bridge. Reviewer != author.
owner: B
---

**Role (W72 RX — selected-root exchange ledger).** Records the exact zero-overlap payment \(\sigma_B\ge w_*M_B-e_\delta\) on the full quotient carrier support.

**Mechanism transcribed from the appendix.** The I-horn package and extraction give \(w_*>0\), root closure gives \(\eta_B\le P_{f^*}^+\), zero overlap is atomwise on full fibers, and one [[lem-l5-positive-flow-foldback]] application uses the common test \(w_*1_{C_B}\).

**Honest scope.** The conclusion is unselected top-positive slack, not negativity, selected overlap, or (EC); no lower bound on \(w_*\) is claimed.

**Rigour tier.** `proved-mod-audit` (fresh hostile W72 verdict). NOT af-validated.
