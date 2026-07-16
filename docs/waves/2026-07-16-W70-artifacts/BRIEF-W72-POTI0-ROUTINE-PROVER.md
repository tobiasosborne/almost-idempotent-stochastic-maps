# W72 routine prover — standalone proofs of the POTI-0 routine batch

You are a fresh, independent prover. You did NOT write POTI0-ATTACK.md; treat
it as a specification, not an authority. Your workspace is this directory: the
full registry snapshot (argument/, definitions/) + context docs (context/) +
the strategy artifact POTI0-ATTACK.md (workspace root).

TASK: produce APPENDIX-poti0-proofs.md containing COMPLETE, STANDALONE proofs
of the FOUR routine nodes of POTI0-ATTACK.md, in order:

  S0   (conj-w72-poti0-exact-cause-split, §1.2: every pinned datum with
        G_phi = 0 lies in exactly one of Z = {r = 0} and O = {r > 0 with
        t_phi(u) <= D_0*delta whenever rho(u) > 0}; equality ownership
        r = 0 to Z)
  RX   (conj-w72-poti0-root-selection-exchange-ledger, §1.3: on r = 0,
        sigma_B >= w_*M_B - e_delta, via the selected-root provenance
        w_* > 0, the atomwise zero-overlap support fact m_A(C_B) = 0, and
        ONE lem-l5-positive-flow-foldback with source m_* = w_*1_{Q_*} and
        the single common test g_* = w_*1_{C_B} — the undivided ledger
        (1.8) with source-mass-scaled error exactly w_*e_delta)
  O48  (conj-w72-poti0-fixed-level-starvation-ledger, §1.5: on O,
        H_48 > tau/16 — the high-level truncation (1.14), the pointwise
        remainders (1.15) from the banked tau/8 tail floor, and ONE
        lem-l5-positive-flow-foldback with source rho and the single
        common test g_48 = r1_{V_48}, undivided ledger (1.17) with error
        exactly r*e_delta, division only by r > 0)
  ASM2 (the assembly §2.1-§2.2: formulate the single minimal conditional
        contract yourself, faithfully — GIVEN S0, RX, O48 proved and GIVEN
        the two creative residuals RDSE (§1.4 contract) and LDHR-48 (§1.6
        contract) as hypotheses, every pinned datum with G_phi = 0 obeys
        the exact (EC) line, and consuming B4.2 once at p_f* then B4.1
        last yields the strict close Z_v(q_A) > (7*c_m/960)*tau via
        (2.2)-(2.5))

RULES (violations = the proof is rejected):
- Each proof: restate the pinned contract VERBATIM from POTI0-ATTACK.md (for
  ASM2, formulate the single minimal conditional contract yourself from
  §2.1-§2.2 — single conclusion, hypotheses named explicitly, no 'hence'
  clauses), list the exact registry shards consumed (with their hypothesis
  blocks checked line-by-line against the pinned POTI-0 datum — the literal
  hypothesis block of conj-dtr-zero-oriented-surplus-exclusion in
  argument/), then a complete proof with every constant's arithmetic
  displayed. Adopt the notation of POTI0-ATTACK.md §1.1 and its sources
  (context/DTR-ATTACK-W69.md §§0-1.1, context/AESC-ATTACK-W67.md §1.1,
  context/DCAP-ATTACK-W65.md §1.1, context/DECOMPOSITION-W63-I.md §§0-1.1):
  m_A, S, q_A, B, eta_B, M_B, C_B, Q_*, w_*, sigma_B, rho, r, z, D_0,
  e_delta, t_phi, G_phi, T_u, V_48, L_48, H_48, E_*, L_v, c_m, and the ray
  objects (Lambda, c), R_A(Lambda, c), Z_v(q_A), Y_v.
- HYPOTHESIS HONESTY (the #1 hostile check downstream):
  (i) The W70 interface is proved L5 and consumable: lem-dtr-canonical-
  overlap (COV), lem-dtr-oriented-tail-ray-conversion (POTI-R),
  lem-dtr-tail-coherent-conversion (TC), lem-dtr-poti-assembly. Open each
  consumed shard and verify its hypothesis block against the pinned datum.
  (ii) SELECTED-ROOT PROVENANCE is the crux of RX: the claim w_* =
  m_A(Q_{f*}) > 0 rests on lem-ihorn-selected-corner-extraction choosing
  f* in supp(lambda_A) and lem-ihorn-cotop-sl1a-package defining lambda_A
  as a normalized restriction of m_A/S. Open BOTH shards and verify these
  are their literal statements — including on partially selected clone
  fibers (does f* in supp(lambda_A) really imply the FULL FIBER Q_{f*} has
  m_A(Q_{f*}) > 0?). If the literal statements do not deliver w_* > 0,
  record a DEFECT with the exact gap.
  (iii) The FOLDBACK discipline: both RX and O48 invoke
  lem-l5-positive-flow-foldback — open it; check its source/submeasure and
  test hypotheses (is m_* = w_*1_{Q_*} <= m_A <= P_v^+ a legal source? is
  rho <= m_A legal? are g_* and g_48 legal common nonnegative tests with
  the claimed bounds? is the error term literally source-mass-scaled as
  claimed, i.e. w_*e_delta resp. r*e_delta?). Verify the claimed exact
  form of e_delta = 2*delta*(1+delta) against the shard.
  (iv) The ZERO-OVERLAP support fact (1.7): rho(1) = 0 must imply
  m_A(C_B) = 0 ATOMWISE (for every Q with eta_B(Q) > 0, min{m_A(Q),
  eta_B(Q)} = 0 forces m_A(Q) = 0) — display this, do not wave at it.
  (v) O48's truncation (1.14): the division by 48*tau requires z >= 48*tau
  on the discarded set and t_phi(u) <= D_0*delta from S0's O-membership;
  verify D_0*delta/(48*tau) = D_0*tau/48 <= tau/16 exactly at D_0 <= 3
  (with tau = sqrt(delta) — cite the pinned relation). Verify the strict
  subtraction from the banked tail floor: cite the exact lem-aesc-* shard
  giving Tail_1(u) > tau/8 and check its hypothesis block holds for every
  u in B (not just overlapped carriers), then restrict to rho(u) > 0.
  (vi) Boundary ownership: z = 48*tau belongs to the HIGH-deficit
  complement; r = 0 owns equality in S0; G_phi = 0 stays in POTI-0.
  (vii) You may NOT consume: any lem-icap-* shard, lem-huddle-charge-
  assembly, lem-intersection-branch-production, any B5-overlay quantity as
  eta_D*, any numerical (L3) fact (W69/W71 fixtures are calibration only),
  or the RDSE/LDHR-48 contracts anywhere except as named hypotheses of
  ASM2.
- Check the strategist's arithmetic INDEPENDENTLY; known checkpoints you
  must confirm or refute with exact numbers:
  (1) RX (1.8): w_*^2*P_f*^+(C_B) <= w_**P_v^+(C_B) + w_**e_delta — every
  factor, then the division by w_* > 0, P_f*^+(C_B) >= M_B (from
  lem-dcap-root-closure: eta_B <= P_f*^+), and (1.7) to reach
  sigma_B >= w_*M_B - e_delta; the strict variant sigma_B > w_*/160 -
  e_delta from M_B > 1/160.
  (2) O48 (1.14): sum over z >= 48*tau of (c_{u,R})_+ <= t_phi(u)/(48*tau)
  <= D_0*tau/48 <= tau/16; (1.15): L_48(u) > tau/8 - tau/16 = tau/16 and
  P_u^+(V_48) >= L_48(u) > tau/16 — check the second inequality's
  justification (does positive fiber aggregation give P_u^+(V_48) >=
  L_48(u)? mind possible negative coefficients — (c_{u,R})_+ vs P_u^+
  scope); (1.17): r^2*tau/16 < r*sum_Q rho(Q)*P_Q^+(V_48) <=
  r*P_v^+(V_48) + r*e_delta — check BOTH inequalities including the
  source-domination step, then division by r.
  (3) H_48 (1.13): verify the three-way minimum's third entry
  (P_v^+(V_48) + e_delta)/r > tau/16 follows from (1.17), and state the
  exact final form of (O48).
  (4) ASM2 (2.1)-(2.5): the case split is exhaustive (S0), each residual
  consumed only on its own subclass, exact (EC) before any B4 spend, B4.2
  once at p_f* with S >= c_m (cite the pinned fact), B4.1 strict
  (P_v^+(L_v) < 2*tau/15 via lem-ihorn-tall-halo-saturation / the B4.1
  chain — open the shard and confirm the literal (2.4) chain), and
  1/64 = 15/960, (1/16)*(2/15) = 8/960, (15-8)/960 = 7/960, final STRICT.
  (5) The ray identity (1.4): R_A(Lambda, c) = Z_v(q_A) for EVERY attained
  certificate incl. Lambda = 0 — from lem-l5-top-face-ray-formula's
  literal statement.
- Quantifier order per POTI0-ATTACK.md (2.6); C_B, w_*, sigma_B, V_48 are
  forced after the order, never optimized; the level 48*tau is fixed once.
- If a claimed routine step does NOT follow — a gap, wrong constant,
  quantifier error, hypothesis mismatch, an unproved provenance claim in
  (ii), or an illegal foldback — DO NOT paper over it. Record it in a
  clearly marked "DEFECT" block with the exact failing line and, if you
  can, the correction. Finding a defect is a success.
- Signed picture; clone-invariant full-fiber quantities; no 1/t*; no
  witness averaging; ONE common nonnegative test per foldback (RX and O48
  each get exactly one; TU remains the only carrier-tail aggregation);
  context/FINDINGS.md dead routes are ABSOLUTE.
- Everything you write remains proposed/conjecture; you promote nothing.
  You prove NOTHING about RDSE (§1.4) and LDHR-48 (§1.6) themselves.

Write ONLY APPENDIX-poti0-proofs.md in the workspace root. Do not touch
argument/ or definitions/ or POTI0-ATTACK.md.
