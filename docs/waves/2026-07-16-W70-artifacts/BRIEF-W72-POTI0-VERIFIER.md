# W72 batched hostile verifier — the POTI-0 routine batch (4 nodes)

You are a fresh, independent HOSTILE verifier. You wrote NEITHER
POTI0-ATTACK.md NOR APPENDIX-poti0-proofs.md. Your job is to BREAK the four
routine proofs. Finding a counterexample, a gap, a wrong constant, a
quantifier error, or an illegal shard consumption is a BIG SUCCESS. Do NOT
be charitable; do NOT repair proofs silently.

Workspace: this directory — registry snapshot (argument/, definitions/),
context docs (context/), the strategy artifact POTI0-ATTACK.md, and the
proofs under attack in APPENDIX-poti0-proofs.md.

TARGETS, in order (contracts pinned in POTI0-ATTACK.md §§1.2-1.6 and §2,
proofs in APPENDIX-poti0-proofs.md):
  S0   conj-w72-poti0-exact-cause-split
  RX   conj-w72-poti0-root-selection-exchange-ledger
  O48  conj-w72-poti0-fixed-level-starvation-ledger
  ASM2 the assembly reduction (§2.1-§2.2), conditional on RDSE/LDHR-48

MANDATORY HOSTILE CHECKS (beyond anything you invent):
1. SELECTED-ROOT PROVENANCE (the #1 check, on RX): the claim
   w_* = m_A(Q_{f*}) > 0. Open lem-ihorn-selected-corner-extraction and
   lem-ihorn-cotop-sl1a-package: do their LITERAL statements give
   f* in supp(lambda_A) with lambda_A a normalized restriction of m_A/S,
   and does that give m_A(Q_{f*}) > 0 on the FULL FIBER Q_{f*} — including
   partially selected clone fibers (only some j in the fiber lie in A)?
   Any gap between "f* is in the support of the normalized measure" and
   "the full fiber carries positive m_A mass" is a DEFECT; rule on whether
   the appendix bridges it honestly.
2. FOLDBACK LEGALITY (RX and O48): open lem-l5-positive-flow-foldback.
   Check for EACH invocation: the source is a legal submeasure
   (m_* = w_*1_{Q_*} <= m_A <= P_v^+; rho <= m_A <= P_v^+), the test is a
   single common nonnegative full-fiber test with the claimed sup bound
   (g_* = w_*1_{C_B} <= w_*; g_48 = r1_{V_48} <= r), the error term is
   literally source-mass-scaled with the shard's own e_delta (verify
   e_delta = 2*delta*(1+delta) against the shard, not the attack doc), and
   the undivided ledgers (1.8)/(1.17) have every factor correct BEFORE the
   division by w_* > 0 resp. r > 0. A factor-of-w_* or factor-of-r error
   is exactly the kind of defect you are hunting.
3. ZERO-OVERLAP SUPPORT (RX): rho(1) = 0 => m_A(C_B) = 0 must be proved
   ATOMWISE from the atomwise minimum (for every Q with eta_B(Q) > 0,
   min{m_A(Q), eta_B(Q)} = 0 forces m_A(Q) = 0), and sigma_B = P_v^+(C_B)
   must follow exactly from (1.6)+(1.7). Check the appendix does not use
   any cancellation or setwise argument.
4. O48 ARITHMETIC: (1.14) truncation — z >= 48*tau on the discarded set,
   t_phi(u) <= D_0*delta from O-membership (S0), and
   D_0*delta/(48*tau) = D_0*tau/48 <= tau/16 at D_0 <= 3 with
   tau = sqrt(delta) (find the pinned relation yourself and check the
   citation); (1.15) — the banked tail floor Tail_1(u) > tau/8: open the
   cited lem-aesc-* shard, check its hypothesis block holds for every
   u in B under the pinned POTI-0 datum, and verify BOTH remainders
   L_48(u) > tau/16 AND P_u^+(V_48) > tau/16 — the second needs
   P_u^+(V_48) >= L_48(u): is that inequality actually justified given
   (c_{u,R})_+ vs P_u^+ scope (coefficients vs positive row mass on the
   fiber)? If the appendix equivocates between coefficient mass and
   positive row-entry mass, that is a DEFECT.
5. S0: exhaustiveness and disjointness of Z and O; every summand of G_phi
   nonnegative (needs COV's measure property + [.]_+ >= 0); r = 0 owns
   equality; no threshold split smuggled in.
6. ASM2 CONDITIONAL HONESTY: RDSE and LDHR-48 consumed ONLY as named
   hypotheses on their own disjoint subclasses; the case split exhaustive
   via S0; exact (EC) produced before any B4 spend; B4.2's literal
   conclusion (open lem-dcap-tall-same-center-packet) used once at p_f*
   with S >= c_m cited from the pinned datum; B4.1 strict via the literal
   (2.4) chain (open lem-ihorn-tall-halo-saturation and confirm
   P_v^+(L_v) < ell_T < 2*tau/15 as displayed); the arithmetic
   1/64 = 15/960, (1/16)*(2/15) = 8/960, 7/960 final, STRICT; the ray
   identity (1.4) for every attained certificate incl. Lambda = 0 (open
   lem-l5-top-face-ray-formula).
7. ILLEGAL consumptions: any lem-icap-* shard, lem-huddle-charge-assembly,
   lem-intersection-branch-production, B5-as-eta_D*, any L3 numerical fact
   (W69/W71 fixtures), TC used at the zero boundary (the attack doc §1.1
   explains why TC is inapplicable — check the appendix does not sneak it
   in), or RDSE/LDHR-48 content outside ASM2's hypotheses.
8. Quantifier order (2.6) and boundary ownership: C_B, w_*, sigma_B, V_48
   forced after the order, never optimized; the level 48*tau fixed once,
   z = 48*tau owned by the high side; G_phi = 0 stays in POTI-0;
   D_POTI = 0 in the routine close; clone invariance of every public
   quantity (w_*, M_B, sigma_B, r, V_48 membership, L_48, H_48).
9. Walls: context/FINDINGS.md dead routes absolute; POTI0-ATTACK.md §3's
   K1-K14 and F1-F23 audits — spot-check the two the attack flags as the
   nearest walls: F19 (top-deficit blind spot: O48 must NOT infer EC from
   low-deficit mass) and K5 (RX must NOT infer negativity or selected
   overlap from root ownership).

DELIVERABLE: VERDICT-poti0-batch.md with:
- One verdict line per node, in order, EXACTLY in this format:
    <node-id>: VALID | VALID-WITH-CORRECTION | INVALID | UNDECIDED
- For VALID-WITH-CORRECTION: the exact corrected statement and the exact
  failing lines of the original.
- For INVALID: the explicit counterexample or the irreparable gap, with
  the exact failing line quoted.
- A final section "CROSS-CUTTING" for any defect spanning nodes.

Write ONLY VERDICT-poti0-batch.md. Do not touch any other file. You promote
nothing; your verdicts are inputs to a separate banking step.
