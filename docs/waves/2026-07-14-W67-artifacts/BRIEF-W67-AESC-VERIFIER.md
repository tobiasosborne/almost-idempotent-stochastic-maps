# W67 batched hostile verifier — the A-esc routine batch (5 nodes)

You are a fresh, independent HOSTILE verifier. You wrote NEITHER
AESC-ATTACK.md NOR APPENDIX-aesc-proofs.md. Your job is to BREAK the five
routine proofs. Finding a counterexample, a gap, a wrong constant, a
quantifier error, or an illegal shard consumption is a BIG SUCCESS — that is
exactly what you are being asked for. Do NOT be charitable; do NOT repair
proofs silently.

Workspace: this directory — registry snapshot (argument/, definitions/),
context docs (context/), the strategy artifact AESC-ATTACK.md, and the proofs
under attack in APPENDIX-aesc-proofs.md.

TARGETS, in order (contracts pinned in AESC-ATTACK.md §§1.2-1.5, proofs in
APPENDIX-aesc-proofs.md):
  SF   conj-w67-aesc-synthetic-finance-tail-amplification
  SF-K the fixed-K fallback (1.15) with its ceiling tau <= 1/(3K+19)
  HS   conj-w67-aesc-guarded-hull-split
  TU   conj-w67-aesc-common-tail-union
  SEP  the separation geography (1.19)-(1.20)

MANDATORY HOSTILE CHECKS (beyond anything you invent):
1. HYPOTHESIS HONESTY — the #1 check, with special force on SF: the proof
   replaces the ACTUAL finance row of the af-validated
   lem-hx-robust-scalar-starvation by a SYNTHETIC fixed row r in K(P). The
   proof is legal ONLY if it never cites that shard's conclusion and instead
   reproves the moment estimate from lem-hx-transverse-moment-identity (open
   that shard: check its hypothesis block line-by-line — what does it require
   of the carrier, the endpoint pair, the normer chi_u? Is the A-esc window
   (1.4) [tau/2 <= ||D_u||_1 <= 2*tau after normalization (1.6), a_u >= 4]
   sufficient?) plus displayed arithmetic using r ONLY through the three
   facts rP = r, r*1 = 1, nu(r) <= delta and the fiber identity (1.9). Any
   silent import of actual-row status is INVALID. Same discipline for every
   other consumed shard (lem-l5-positive-flow-foldback's submeasure
   hypothesis on eta_D* restricted to B; the seven lem-dcap-* shards on the
   D-cap class; NO lem-icap-* consumption).
2. Every constant's arithmetic — recompute each chain exactly:
   (1.11) core bound 2*tau; (1.12) lever D_0/(tau/2) <= 6/tau (check at
   delta <= delta_rt: D_0 = 2+4*delta — is 2*(2+4*delta)/tau <= 6/tau, i.e.
   4+8*delta <= 6, actually valid? state the exact condition); the
   negative-tail coefficient C_u + delta; the positive-tail coefficient
   (C_u + delta + 3*delta)/a_u <= C_u/4 + delta at a_u >= 4; the
   recombination (1.13) 1 <= 2*tau + (6/tau)*((5/4)C_u + 2*delta)
   = 14*tau + (15/(2*tau))*C_u — CHECK: (6/tau)*2*delta = 12*delta/tau
   = 12*tau, plus 2*tau = 14*tau; and (6/tau)*(5/4)C_u = (15/(2*tau))C_u —
   then (1.14) C_u >= (2*tau/15)*(1-14*tau) >= (121/960)*tau > tau/8 at
   tau <= 1/256 — verify (2/15)*(1-14/256) = (2/15)*(242/256) = 121/960
   and 121/960 > 1/8 = 120/960. Check the SF-K generalization (1.15)
   arithmetic the same way with h_u <= K*delta. For TU: (1.17)'s inequality
   direction (is the positive part of an aggregated signed quantity really
   bounded the claimed way by pre-aggregation positive mass — which
   direction is safe?); the foldback close tau/1280 - e_delta > tau/2560
   i.e. e_delta < tau/2560; the prover's ceiling claim tau <= 1/245760 from
   delta_rt's third component ((c_m*b/120)^2 with c_m = 1/4, b = c_m/128 =
   1/512: c_m*b/120 = 1/245760) — verify this and whether e_delta =
   2*delta*(1+delta) < tau/2560 follows; ALSO rule on the STRATEGIST's
   original claim "tau <= c_m^2/15360 < 1/15360" — is it wrong, and if so
   does anything else in AESC-ATTACK.md depend on the wrong form?
3. Quantifier order and boundary ownership: display field fixed BEFORE h_u is
   measured; h = 3*delta owned by D_tail; HES mass equality 1/160 owned by
   HES; the nearest point r arbitrary (no favorable tie); the separator
   psi_u chosen after u but never averaged/summed across carriers.
4. R2 discipline: TU uses exactly ONE lem-l5-positive-flow-foldback call on
   ONE common nonnegative test 1_{U_B}; errors scale by source mass; no
   summed pairwise demands anywhere in the batch.
5. Sign discipline: the pinned A-esc residual is p_f - x_u with
   x_u = p_u - a_u*D_u and a_u*D_u = k_{O,u} - k_{T,u} (AESC-ATTACK.md (0.1),
   K2). Check every line of SF/SEP for a sign reversal, especially (1.7),
   (1.9), (1.20).
6. Walls: context/FINDINGS.md dead routes are absolute; check each proof
   against the kill-list codes K1-K12 of AESC-ATTACK.md §3 (esp. K4 common
   test, K5 no favorable selection, K10 ownership separation).
7. Clone invariance of every public quantity (h_u, Tail_1, U_B, the
   thresholds) under row cloning / fiber structure.

DELIVERABLE: VERDICT-aesc-batch.md with:
- One verdict line per node, in order, EXACTLY in this format:
    <node-id>: VALID | VALID-WITH-CORRECTION | INVALID | UNDECIDED
- For VALID-WITH-CORRECTION: the exact corrected statement and the exact
  failing lines of the original.
- For INVALID: the explicit counterexample or the irreparable gap, with the
  exact failing line quoted.
- A final section "CROSS-CUTTING" for any defect spanning nodes (e.g.
  notation drift between AESC-ATTACK.md and the appendix, or the strategist
  ceiling-constant discrepancy and its blast radius).

Write ONLY VERDICT-aesc-batch.md. Do not touch any other file. You promote
nothing; your verdicts are inputs to a separate banking step.
