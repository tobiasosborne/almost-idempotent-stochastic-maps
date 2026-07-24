---
id: conj-w72-poti0-fixed-level-starvation-ledger
kind: lemma
contract: Within the literal W72 POTI-0 hypothesis block of conj-dtr-zero-oriented-surplus-exclusion, with c_m = 1/4, b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), and with objects fixed in the order c_m -> (b,delta_rt) -> datum -> selected-corner certificate C* -> arbitrary clone-invariant row-point vertex kernel and arbitrary reduced display field -> full-fiber carrier set B -> (rho,t_phi,G_phi) -> arbitrary attained top-face ray certificate (Lambda,c), all measures being clone-invariant measures on the finite full row-point quotient, all coefficients signed, and all geometry row-point l1, if G_phi = 0, r = rho(1) > 0, and t_phi(u) <= D_0*delta(P) whenever rho(u) > 0, define V_48 = {R : z(p_R) < 48*tau}, L_48(u) = sum_{R in T_u cap V_48} max(c_u,R,0), e_delta = 2*delta(P)*(1 + delta(P)), and H_48 = min{min_{rho(u)>0} L_48(u), min_{rho(u)>0} P_u^+(V_48), (P_v^+(V_48)+e_delta)/r}; then H_48 > tau/16, with z = 48*tau belonging to the high-deficit complement.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull; def-invisible-mass
deps: lem-dtr-canonical-overlap; lem-top-deficit-price; lem-aesc-synthetic-finance-tail-amplification; lem-l5-positive-flow-foldback
status: proved-mod-audit
af: none
provenance: W72 POTI-0 wave (docs/waves/2026-07-16-W70-artifacts/): pinned statement POTI0-ATTACK-W72.md §1.5; standalone proof APPENDIX-W72-poti0-proofs.md §3; fresh hostile batched verdict VERDICT-poti0-batch.md line O48: VALID. Reviewer != author.
owner: B
---

**Role (W72 O48 — fixed-level starvation ledger).** On the positive-overlap zero-surplus branch, retains more than \(\tau/16\) tail and positive row mass below the one fixed \(48\tau\) deficit level and folds that population back to row \(v\).

**Mechanism transcribed from the appendix.** Top-deficit pricing bounds the high side, the AESC tail shard supplies the strict tail floor, and one [[lem-l5-positive-flow-foldback]] application uses the common test \(r1_{V_{48}}\).

**Honest scope.** This is a low-deficit population statement only; it does not imply (EC), select a direction, or introduce a second level.

**Rigour tier.** `proved-mod-audit` (fresh hostile W72 verdict). NOT af-validated.
