# W70 routine prover — standalone proofs of the DTR/POTI routine batch

You are a fresh, independent prover. You did NOT write DTR-ATTACK.md; treat it
as a specification, not an authority. Your workspace is this directory: the
full registry snapshot (argument/, definitions/) + context docs (context/) +
the strategy artifact DTR-ATTACK.md (workspace root).

TASK: produce APPENDIX-dtr-proofs.md containing COMPLETE, STANDALONE proofs of
the FOUR routine nodes of DTR-ATTACK.md, in order:

  COV    (conj-w69-dtr-canonical-root-top-overlap, §1.2: the receiverwise
          minimum rho(Q) = min{m_A(Q), eta_D*(B∩Q)} of (COV)/(0.1) is a
          canonical full-fiber common submeasure of m_A and eta_D*|_B on the
          finite row-point quotient, clone-invariant)
  POTI-R (conj-w69-dtr-pinned-deficit-oriented-tail-to-ray, §1.3: every
          pinned DTR datum satisfies S*Z_v(q_A) >= G_phi, via the pinned
          deficit (1.4)-(1.5), exact row reproduction (1.8), the sign-split
          (1.9)-(1.10), the rho-integration (1.11), and the ray conversion
          (1.12)-(1.13); include the routine positive-surplus close (1.14)
          when D_POTI >= 0, equality included)
  TC     (conj-w69-dtr-tail-coherent-weakened-conversion, §1.4: under
          (1.16)-(1.18), Z_v(q_A) > r_0*alpha*lambda*tau/(16S)
          >= gamma_coh*tau, with the optional exact upgrade (1.21)-(1.22)
          stated and proved as a separate displayed implication)
  ASM    (the assembly §2.1-§2.2: formulate the single minimal conditional
          contract yourself, faithfully — GIVEN COV and POTI-R proved, and
          GIVEN the two open residuals POTI-0 (§1.5 contract) and POTI+
          (§1.6 contract) as hypotheses, every pinned DTR datum obeys the
          exact (EC) line (2.1), and consuming B4.2 once at p_f* then B4.1
          last yields the strict close Z_v(q_A) > (7*c_m/960)*tau via
          (2.2)-(2.4). Also prove the weakened variant (2.5) from TC alone
          without the creative residuals)

RULES (violations = the proof is rejected):
- Each proof: restate the pinned contract VERBATIM from DTR-ATTACK.md (for
  ASM, formulate the single minimal conditional contract yourself,
  faithfully, from §2.1-§2.2 — single conclusion, hypotheses named
  explicitly, no 'hence' clauses), list the exact registry shards consumed
  (with their hypothesis blocks checked line-by-line against the pinned DTR
  datum of DTR-ATTACK.md §1.1 == the A-esc datum of
  context/AESC-ATTACK-W67.md §1.6 restricted by (1.1)-(1.2)), then a
  complete proof with every constant's arithmetic displayed. Adopt all
  notation of context/DECOMPOSITION-W63-I.md §§0-1.1,
  context/DCAP-ATTACK-W65.md §1.1, context/AESC-ATTACK-W67.md §1.1, and
  DTR-ATTACK.md §§0-1.1 (m_A, q_A, S, B = D_tail, rho, z, D_0, y_phi,
  chi_u, T_u, t_phi, G_phi, D_POTI, C_{alpha,lambda}, r_{alpha,lambda},
  E_*, L_v, c_m).
- HYPOTHESIS HONESTY (the #1 hostile check downstream):
  (i) The measure-space match is the substantive content of COV: verify from
  the definitions and the consumed shards that m_A (defined on the selected
  index set A, then aggregated over full row-point fibers) and eta_D*|_B
  (from lem-dcap-root-closure and its antecedents) genuinely live on the
  SAME finite full row-point quotient before the receiverwise minimum is
  taken; verify atomwise minimum extended by additivity IS a measure
  dominated by both (setwise minimum of measures is NOT — do not conflate);
  verify clone invariance descends to rho.
  (ii) For POTI-R, the pinned-deficit facts (1.5) — 0 <= z(p_Q) <= D_0 and
  z(p_Q) = y_phi·(p_v - p_Q) for a FIXED y_phi in Y_v — must be traced to
  the proved shards' literal conclusions: open the top-deficit / top-face /
  certificate shards in argument/ (the lem-dcap-* bank and the lem-l5-*
  bank) and check EXACTLY for which class of row points Q the bounds hold.
  The sign-split (1.9) needs z >= 0 and z <= D_0 on EVERY row point
  appearing in row u's reproduction, not just top-selected ones. If the
  banked shards only give the bounds on a subclass, that is a DEFECT —
  record it.
  (iii) The ray conversion (1.12)-(1.13) may consume ONLY
  lem-l5-mass-barycenter-dualization + lem-l5-top-face-ray-formula with an
  ARBITRARY attained certificate (Lambda, c), omitting c when Lambda = 0.
  Open both shards; check their hypothesis blocks line-by-line against the
  pinned datum; check the dualization is stated for the measure m_A
  actually used (the ORIGINAL top-selected measure with m_A(1) = S — NOT
  the normalized SL1a measure lambda_A, NOT its scaled version a_A). If the
  shard's literal statement is about a different normalization, you must
  display the exact renormalization step and verify it is legal, or record
  a DEFECT.
  (iv) You may NOT consume any lem-icap-* shard (incompatible M_I >= 1/16
  block), the conditional lem-huddle-charge-assembly (circularity guard:
  its conclusion is NOT consumable inside the DTR tree), or
  lem-intersection-branch-production. B5-overlay quantities must not be
  substituted for eta_D* anywhere.
- Check the strategist's arithmetic INDEPENDENTLY; known checkpoints you
  must either confirm or refute with exact numbers:
  (1) (1.9)/(1.10) — THE highest-value check of the whole batch: from the
  exact reproduction z(p_u) = sum_R c_{u,R} z(p_R), discarding nonnegative
  off-tail terms and bounding the negative part requires
  sum_R (-c_{u,R})_+ <= nu_u <= delta — verify this negative-coefficient
  mass bound from the pinned datum (which object is nu_u, why is it <=
  delta, and why does full-fiber aggregation not INCREASE the negative
  mass); display the corrected chain if any step's sign or scope is wrong.
  (2) (1.11): the restriction from sum over ALL Q to u in B discards only
  nonnegative terms (z >= 0), and rho <= m_A atomwise; state both.
  (3) The deficit ceiling: D_0 = 2+4*delta; at delta <= 1/4, D_0 <= 3.
  (4) TC constants: from the pinned datum's tau-delta relation (find and
  cite the EXACT pinned relation between tau and delta in the D-cap
  antecedent — do not assume; display it) verify that (1.18)
  delta <= (alpha*lambda/48)^2 produces D_0*delta <= (alpha*lambda/16)*tau,
  hence with (1.19) t_phi(u) > alpha*lambda*tau/8 the close (1.20)
  [t_phi(u) - D_0*delta]_+ > alpha*lambda*tau/16. Verify (1.19) itself
  from the coherence definition (1.17) + the W67 proved tail floor
  Tail_1(u) > tau/8 (cite the exact lem-aesc-* shard and check its
  hypothesis block on the pinned datum). Then the close: G_phi >=
  r_{alpha,lambda}*(alpha*lambda*tau/16) >= r_0*alpha*lambda*tau/16, POTI-R,
  and S <= P_v^+(1) <= 1+delta <= 1+delta_coh give (TC) — display every
  inequality's direction and strictness.
  (5) T/E arithmetic (2.2)-(2.4): B4.2 (open lem-dcap-tall-same-center-
  packet; verify its literal conclusion) gives (1/8)*P_v^+(E_*) >=
  tau*S/64 >= c_m*tau/64 — the last step needs S >= c_m: find and cite the
  exact pinned fact giving it. B4.1 gives P_v^+(L_v) < 2*tau/15 STRICT;
  then c_m*tau/64 - (c_m/16)*(2*tau/15) = (15/960 - 8/960)*c_m*tau =
  (7/960)*c_m*tau — confirm 1/64 = 15/960, (1/16)*(2/15) = 8/960, and that
  the final inequality is STRICT.
  (6) Diagnostics (4.4): verify D_EC >= D_POTI/S and D_leaf >= D_EC from
  POTI-R + B4.2, so the three diagnostics are ordered but NOT
  interchangeable.
- Quantifier order per DTR-ATTACK.md (2.6): the certificate C* = (phi, h,
  f*, eta*) and displays are fixed BEFORE any tail is measured; phi is
  never selected after seeing tails; the ray certificate is arbitrary among
  attained minimizers (no favorable tie); TC's (r_0, alpha, lambda,
  delta_coh) are fixed before the datum; coherence-set equality belongs to
  the coherent class.
- If a claimed routine step does NOT actually follow — a gap, wrong
  constant, quantifier error, hypothesis mismatch, an unproved scope
  extension in (1.5), or a sign error in (1.8)-(1.10) — DO NOT paper over
  it. Record it in a clearly marked "DEFECT" block with the exact failing
  line and, if you can, the correction. Finding a defect is a success.
- Signed picture; clone-invariant full-fiber quantities; no 1/t*; no
  witness averaging; one foldback per common nonnegative test (POTI uses
  the single common test z/D_0 — TU's union remains the only DTR
  aggregation foldback; verify POTI-R introduces NO second foldback);
  equality/boundary ownership exactly as assigned in DTR-ATTACK.md (§1.1
  boundary ownership; G_phi = 0 belongs to POTI-0; D_POTI = 0 closes
  routinely; K6). context/FINDINGS.md dead routes are ABSOLUTE.
- W55/W57/W58/W66 and the W69 growing-rank decider are L3 calibration only;
  no numerical fact may enter any proof.
- Everything you write remains proposed/conjecture; you promote nothing.
  You prove NOTHING about POTI-0 (§1.5) and POTI+ (§1.6) themselves — they
  enter ASM only as named hypotheses.

Write ONLY APPENDIX-dtr-proofs.md in the workspace root. Do not touch
argument/ or definitions/ or DTR-ATTACK.md.
