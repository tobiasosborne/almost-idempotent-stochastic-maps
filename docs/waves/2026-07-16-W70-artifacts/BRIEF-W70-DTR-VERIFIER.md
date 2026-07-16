# W70 batched hostile verifier — the DTR/POTI routine batch (4 nodes)

You are a fresh, independent HOSTILE verifier. You wrote NEITHER
DTR-ATTACK.md NOR APPENDIX-dtr-proofs.md. Your job is to BREAK the four
routine proofs. Finding a counterexample, a gap, a wrong constant, a
quantifier error, or an illegal shard consumption is a BIG SUCCESS — that is
exactly what you are being asked for. Do NOT be charitable; do NOT repair
proofs silently.

Workspace: this directory — registry snapshot (argument/, definitions/),
context docs (context/), the strategy artifact DTR-ATTACK.md, and the proofs
under attack in APPENDIX-dtr-proofs.md.

TARGETS, in order (contracts pinned in DTR-ATTACK.md §§1.2-1.6 and §2,
proofs in APPENDIX-dtr-proofs.md):
  COV    conj-w69-dtr-canonical-root-top-overlap
  POTI-R conj-w69-dtr-pinned-deficit-oriented-tail-to-ray
  TC     conj-w69-dtr-tail-coherent-weakened-conversion
  ASM    the assembly reduction (§2.1-§2.2), conditional on POTI-0/POTI+

MANDATORY HOSTILE CHECKS (beyond anything you invent):
1. HYPOTHESIS HONESTY — the #1 check, with special force on POTI-R:
   (a) The pinned-deficit scope: (1.5) asserts 0 <= z(p_Q) <= D_0 and
   z(p_Q) = y_phi·(p_v - p_Q) with ONE fixed y_phi in Y_v. Open the shards
   the appendix cites for this (the lem-dcap-* / lem-l5-* banks): for
   EXACTLY which class of row points Q do their literal conclusions hold?
   The sign-split (1.9) needs 0 <= z <= D_0 at EVERY row point in carrier
   u's exact reproduction z(p_u) = sum_R c_{u,R} z(p_R) — every R with
   c_{u,R} != 0, including rows outside every selected/tail set. Any
   unproved scope extension is INVALID.
   (b) The dualization measure: lem-l5-mass-barycenter-dualization — open
   it; is its literal statement about the measure m_A actually used
   (m_A(Q) = sum_{j in A∩Q} (P_vj)_+, total mass S), or about a normalized/
   scaled variant (lambda_A, a_A)? If the appendix silently renormalizes,
   rule on whether the displayed renormalization is exact and legal.
   (c) The ray certificate: lem-l5-top-face-ray-formula — arbitrary ATTAINED
   certificate, Lambda = 0 degenerate case included; any favorable
   selection of certificate, tie, or minimizer is INVALID.
   (d) The negative-coefficient mass bound sum_R (-c_{u,R})_+ <= nu_u <=
   delta: which pinned fact defines nu_u, why <= delta, and does full-fiber
   aggregation really not increase negative-part mass? Check against the
   fiber-aggregation conventions of context/DECOMPOSITION-W63-I.md §§0-1.1.
   (e) COV's space match: do m_A and eta_D*|_B (via lem-dcap-root-closure)
   live on the SAME finite full row-point quotient BEFORE the receiverwise
   minimum? Distinguish atomwise min (extended by additivity — a measure)
   from setwise min (not additive). Verify clone invariance of rho.
   (f) ILLEGAL consumptions: any lem-icap-* shard (incompatible M_I >= 1/16
   block), lem-huddle-charge-assembly (circular inside the DTR tree),
   lem-intersection-branch-production, any B5-overlay quantity substituted
   for eta_D*, any use of POTI-0/POTI+ beyond named hypotheses of ASM, any
   numerical (L3) fact inside a proof.
2. Every constant's arithmetic — recompute each chain exactly:
   D_0 = 2+4*delta <= 3 at delta <= 1/4; the (1.9)-(1.10) sign-split; the
   (1.11) restriction (nonnegative discards only; rho <= m_A atomwise); TC:
   the pinned tau-delta relation (find the EXACT pinned relation in the
   D-cap antecedent yourself and rule whether the appendix cites it
   correctly), then delta <= (alpha*lambda/48)^2 => D_0*delta <=
   (alpha*lambda/16)*tau; (1.17)+(the W67 tail floor Tail_1(u) > tau/8,
   check the cited lem-aesc-* shard's hypothesis block) => (1.19)
   t_phi(u) > alpha*lambda*tau/8; the close (1.20) strict; G_phi >=
   r_0*alpha*lambda*tau/16; S <= P_v^+(1) <= 1+delta <= 1+delta_coh;
   gamma_coh = r_0*alpha*lambda/(16*(1+delta_coh)). ASM: B4.2's literal
   conclusion (open lem-dcap-tall-same-center-packet) => (1/8)*P_v^+(E_*)
   >= tau*S/64; the S >= c_m step (which pinned fact?); B4.1 STRICT
   P_v^+(L_v) < 2*tau/15; 1/64 = 15/960; (1/16)*(2/15) = 8/960;
   (15-8)/960 = 7/960; final strictness. Diagnostics order (4.4):
   D_EC >= D_POTI/S and D_leaf >= D_EC — verify both derivations.
3. Quantifier order and boundary ownership: certificate and displays fixed
   BEFORE tails are measured; phi never selected after seeing tails; TC
   parameters (r_0, alpha, lambda, delta_coh) fixed before the datum;
   coherence equality owned by the coherent class; G_phi = 0 owned by
   POTI-0; D_POTI = 0 owned by the routine close; h = 3*delta owned by
   D-tail; mass equality 1/160 owned by HES.
4. Foldback discipline: TU remains the ONLY DTR aggregation foldback; POTI-R
   must use only the single common nonnegative test z/D_0 and exact
   reproduction — no second foldback, no summed pairwise carrier demands,
   no carrier-dependent direction sum.
5. Sign discipline: z = H - phi; the residual conventions of
   AESC-ATTACK-W67.md (0.1)/K2 (x_u = p_u - a_u*D_u); check every line of
   the appendix for a sign reversal, especially (1.8)-(1.10) and the
   dualization evaluation z(p_Q) = y_phi·(p_v - p_Q).
6. Walls: context/FINDINGS.md dead routes are absolute; check each proof
   against DTR-ATTACK.md §3's kill-list codes K1-K14 (esp. K4 common test,
   K5 ownership, K10 no circular bridge, K13 ray legality, K14 diagnostics
   distinct).
7. Clone invariance of every public quantity (m_A, q_A, S, eta_D*|_B, rho,
   z, t_phi, G_phi, r_{alpha,lambda}) under row cloning / fiber structure.
8. ASM's conditional honesty: the contract must consume POTI-0 (§1.5) and
   POTI+ (§1.6) ONLY as named hypotheses, with the case split exhaustive
   (G_phi = 0 | D_POTI < 0 & G_phi > 0 | D_POTI >= 0) and every boundary
   owned exactly once; the conclusion must be the exact (EC) line then the
   strict (7*c_m/960)*tau close; the weakened variant (2.5) must not
   consume either residual.

DELIVERABLE: VERDICT-dtr-batch.md with:
- One verdict line per node, in order, EXACTLY in this format:
    <node-id>: VALID | VALID-WITH-CORRECTION | INVALID | UNDECIDED
- For VALID-WITH-CORRECTION: the exact corrected statement and the exact
  failing lines of the original.
- For INVALID: the explicit counterexample or the irreparable gap, with the
  exact failing line quoted.
- A final section "CROSS-CUTTING" for any defect spanning nodes (notation
  drift between DTR-ATTACK.md and the appendix, a scope extension used in
  more than one node, a wrong pinned relation propagating).

Write ONLY VERDICT-dtr-batch.md. Do not touch any other file. You promote
nothing; your verdicts are inputs to a separate banking step.
