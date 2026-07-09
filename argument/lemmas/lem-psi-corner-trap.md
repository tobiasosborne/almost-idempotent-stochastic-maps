---
id: lem-psi-corner-trap
kind: lemma
contract: Psi normalization and corner trap: for an exact signed idempotent P with 0 < delta(P) <= 1/4, a hidden top vertex v with t*(v) > 0 and disjoint always-tight hulls at v (g > 0), and a relative-interior optimal exposer h* at v: there is a legal parameter pair (ell, m) for lem-separator-zero-face-obstruction with ||ell||_inf <= 1 and |m| <= 3 + 4*delta such that psi(p) = ell(p - p_v) - m*h*(p) has row-oscillation osc(psi) <= 5 + 8*delta, satisfies that shard's full sign structure, and obeys psi >= min(g/2, g - (7/4)*tau) on T(v); moreover for every top support functional phi (z = H - phi), every row i, and all thresholds s_1, s_2, eta_1, eta_2 > 0: (a) z_i <= s_1 implies sum over {j : z_j >= s_2} of P_ij^+ <= (s_1 + nu_i*(2+4*delta))/s_2; (b) h*(p_i) <= eta_1 implies sum over {j : h*(p_j) >= eta_2} of P_ij^+ <= (eta_1 + nu_i)/eta_2; (c) at any row r attaining M = max_j psi_j: sum_j P_rj^+*(M - psi_j) <= nu_r*(5+8*delta) <= delta*(5+8*delta). All constants are free of t*(v).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-separator-zero-face-obstruction; lem-top-deficit-price
status: proved
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): Fable author L6 (sub-leaf L6.4) + fresh hostile codex verifier V-L6 (VALID-WITH-CORRECTIONS; correction applied — h* pinned to a RELATIVE-INTERIOR optimal exposer per the separator shard's hypothesis; the interval (L_O, L_T/t*) nonemptiness, |m| bound, oscillation arithmetic, and the max-principle sign-splitting of P psi = psi all checked; NO step divides by t*(v))
owner: A
---

**Role (the t*-free harmonic toolkit — the death trap neutralized).** The separator
direction psi can always be normalized with BOUNDED parameters (|m| <= 3+4*delta,
osc <= 5+8*delta) regardless of how small t*(v) is — the historic killer of
exchange-starvation arguments (any constant dividing by t* is dead). (a)+(b) form the
(z, h*)-corner trap: co-top h*-low rows reproduce from co-top h*-low rows up to explicit
Markov loss; (c) is the psi-maximum principle with O(delta) slack from the row-level
eigen-identity P psi = psi (sign-splitting, no witness comparison). These are the
mechanism bricks for attacking [[conj-cotop-web-coupling]]. Dimension-free;
clone-invariant.

**Rigour tier.** L5 (reviewer != author: fresh hostile codex V-L6; correction applied).
NOT af-validated.
