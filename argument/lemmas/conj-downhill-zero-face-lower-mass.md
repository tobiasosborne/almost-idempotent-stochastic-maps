---
id: conj-downhill-zero-face-lower-mass
kind: lemma
contract: (CONJECTURE) Downhill zero-face lower mass: there exist universal constants (the tall/heavy/near-cluster tuple of conj-zero-face-elimination, c_ship > 0, c0 > 0) such that for every exact signed idempotent P in the tall heavy near-cluster regime at hidden top v with sum over {k not in C} of max(P_vk, 0) < c_ship and no cluster vertex (rho,kappa)-exposed: every mass-carrying cluster vertex u in C with t*(u) > 0 and disjoint always-tight hulls admits a separator blocker z (per lem-separator-zero-face-obstruction) with sum over {j : h*_u(p_j) >= kappa} of max(P_zj, 0) >= c0.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
af: none
provenance: W47 wave (docs/waves/2026-07-07-W47-mechanism.md): the sole open input of AY's conditional bridge, VAY-approved statement (quantifier note adopted: "some associated blocker" suffices)
owner: A
---

**Role (THE (T2) trigger — any universal c0 wins).** With this input,
[[lem-blocker-capacity-bridge]] closes (T2) by the capacity contradiction
c0*kappa <= nu_z <= delta, i.e. c0*tau/4 <= tau^2, impossible for delta < (c0/4)^2. The
scale gap (tau vs tau^2) means NO constant-fight: any universal c0, however small, closes
the terminal node's (T2) face and with it [[conj-zero-face-elimination]]'s bridge horn.

**Sharpened bridge note (W49-BD, VBD-approved):** capacity forbids ANY blocker lower bound
m_kappa(z) > 4*tau — so the exact sufficient form is any f(tau) > 4*tau, and a universal
constant c0 is sufficient but stronger than needed. Ledger-only proofs are DEAD
([[obs-thin-zero-face-blocker-graft]]): the surviving content is tall anti-thin-blocker
SELECTION (the tightness-promotion wall).

**Theatre guard (pre-committed exit, W47 wave doc).** This statement rhymes with the dead
anti-splitting/sigma-cap walls. Distinguishers: the scale advantage above, and a cheap
refutation path — an exact tall-heavy instance whose blocker is kappa-high-STARVING
(sum over the kappa-high slab of P_z^+ -> 0) refutes it. If the decider wave returns
"needs a new mechanism" instead of proof-or-counterexample, PIVOT the arm; do not re-dress.

**Rigour tier.** CONJECTURE (L0-flagged). Not usable as an input anywhere except the
explicitly conditional [[lem-blocker-capacity-bridge]].
