# W67 routine prover — standalone proofs of the A-esc routine batch

You are a fresh, independent prover. You did NOT write AESC-ATTACK.md; treat it
as a specification, not an authority. Your workspace is this directory: the
full registry snapshot (argument/, definitions/) + context docs (context/) +
the strategy artifact AESC-ATTACK.md.

TASK: produce APPENDIX-aesc-proofs.md containing COMPLETE, STANDALONE proofs of
the FIVE routine nodes of AESC-ATTACK.md, in order:

  SF   (conj-w67-aesc-synthetic-finance-tail-amplification, §1.2:
        h_u <= 3*delta implies Tail_1(u) > tau/8, via the synthetic fixed row
        r, the fiber identity (1.9), the transverse-moment identity (1.10),
        and the sign-split arithmetic (1.11)-(1.14))
  SF-K (the fixed-K fallback (1.15) with its exact ceiling tau <= 1/(3K+19),
        stated as its own single-conclusion contract)
  HS   (conj-w67-aesc-guarded-hull-split, §1.3: the (0.4) partition with
        equality ownership and the 1/80 - 1/160 > 1/160 strict guard)
  TU   (conj-w67-aesc-common-tail-union, §1.4: (1.17), ONE
        lem-l5-positive-flow-foldback at f* on the single common test
        1_{U_B}, and the exact close tau/1280 - e_delta > tau/2560 from the
        actual delta_rt ceiling)
  SEP  (the separation geography (1.19)-(1.20): existence of the affine
        separator psi_u with linf-norm <= 1 linear part realizing
        h_u = dist_1(x_u, K(P)) for the compact convex row hull, and
        -a_u*psi_u(D_u) >= h_u > 3*delta, WITHOUT choosing a preferred
        normal — stated as its own single-conclusion contract)

RULES (violations = the proof is rejected):
- Each proof: restate the pinned contract VERBATIM from AESC-ATTACK.md (for
  SF-K and SEP, formulate the single minimal contract yourself, faithfully,
  from (1.15) and (1.19)-(1.20) — single scalar/existence conclusion, no
  'hence' clauses), list the exact registry shards consumed (with their
  hypothesis blocks checked line-by-line against the A-esc/D-cap class),
  then a complete proof with every constant's arithmetic displayed. Adopt all
  notation of context/DECOMPOSITION-W63-I.md §§0-1.1, context/DCAP-ATTACK-W65.md
  §1.1, and AESC-ATTACK.md §1.1 (D_u, a_u, x_u, h_u, chi_u, Tail_1, c_{u,Q},
  d_{u,Q}, e_{u,Q}).
- HYPOTHESIS HONESTY (the #1 hostile check downstream): you may NOT consume
  lem-icap-* shards whose hypothesis blocks assume the I-cap class. You may
  consume the seven lem-dcap-* shards on the D-cap class, the lem-ihorn-*
  bank, lem-l5-* (esp. lem-l5-positive-flow-foldback), and the af-validated
  lem-hx-* engine bank — BUT for SF the critical honesty point is:
  lem-hx-robust-scalar-starvation's literal contract is about ACTUAL rows.
  SF replaces the actual finance row by a synthetic fixed row r in K(P)
  (rP = r, r*1 = 1, nu(r) <= delta). You must therefore NOT cite the
  starvation shard's conclusion; you must REPROVE the moment estimate from
  lem-hx-transverse-moment-identity (verify that ITS hypothesis block is
  satisfied — check exactly what it requires of the carrier and the normer)
  plus displayed sign-split arithmetic, using r only through (1.6)-(1.9).
  Verify entrywise-honestly that a nearest point r exists (compactness of
  K(P)), that the argument is uniform over ALL nearest points (no favorable
  tie), and that fiber aggregation cannot increase any negative-part or l1
  budget.
- Check the strategist's arithmetic INDEPENDENTLY; known checkpoints you must
  either confirm or refute with exact numbers: (1.11) core bound 2*tau; (1.12)
  lever 6/tau (from ||p_Q - p_u||_1 <= D_0 = 2+4*delta and ||D_u||_1 >= tau/2
  — CHECK: is D_0/(tau/2) <= 6/tau actually valid for delta <= delta_rt?);
  the negative-tail coefficient C_u + delta; the positive-tail coefficient
  C_u/4 + delta (from a_u >= 4 and |e_{u,Q}| summing to <= 3*delta — CHECK
  the aggregation of |e_{u,Q}| over fibers); the close (1.13)
  1 <= 14*tau + (15/(2*tau))*C_u — CHECK this exact recombination — and
  (1.14) C_u >= (2*tau/15)*(1-14*tau) >= (121/960)*tau > tau/8 at
  tau <= 1/256. For TU: (1.17)'s direction (positive part after aggregation
  bounded by positive coefficient mass BEFORE aggregation — state and prove
  the correct inequality direction), the submeasure hypothesis of the
  foldback on the restriction of eta_D* to B, and the exact numeric close
  including e_delta/tau < 1/3840 from tau < 1/15360 (CHECK: the strategist
  claims delta_rt's third component gives tau <= c_m^2/15360 < 1/15360 —
  verify from delta_rt = min{2^-16, (c_m/4)^2, (c_m*b/120)^2} with
  c_m = 1/4, b = c_m/128 what the true ceiling is; if the claimed constant
  is wrong, flag it and compute the correct one and its consequence for
  (TU)).
- If a claimed routine step does NOT actually follow — a gap, wrong constant,
  quantifier error, hypothesis mismatch, or a sign error in (0.1)/(1.9) — DO
  NOT paper over it. Record it in a clearly marked "DEFECT" block with the
  exact failing line and, if you can, the correction. Finding a defect is a
  success.
- Signed picture; clone-invariant full-fiber quantities; no 1/t*; conic
  coefficients are geography, not transitions; one R2 foldback per common
  nonnegative test, never summed pairwise demands; equality/boundary
  ownership exactly as assigned in AESC-ATTACK.md (h = 3*delta belongs to
  D_tail; HES mass equality 1/160 belongs to HES); context/FINDINGS.md dead
  routes are ABSOLUTE.
- Everything you write remains proposed/conjecture; you promote nothing.

Write ONLY APPENDIX-aesc-proofs.md in the workspace root. Do not touch
argument/ or definitions/ or AESC-ATTACK.md.
