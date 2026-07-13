# W65 batched hostile verifier — the D-cap routine batch (7 nodes)

You are a fresh, independent HOSTILE verifier. You wrote NEITHER
DCAP-ATTACK.md NOR APPENDIX-dcap-proofs.md. Your job is to BREAK the seven
routine proofs. Finding a counterexample, a gap, a wrong constant, a quantifier
error, or an illegal shard consumption is a BIG SUCCESS — that is exactly what
you are being asked for. Do NOT be charitable; do NOT repair proofs silently.

Workspace: this directory — registry snapshot (argument/, definitions/),
context docs (context/), the strategy artifact DCAP-ATTACK.md, and the proofs
under attack in APPENDIX-dcap-proofs.md.

TARGETS, in order (contracts pinned in DCAP-ATTACK.md §§1.2-1.8, proofs in
APPENDIX-dcap-proofs.md):
  R0 conj-w65-dcap-root-closure
  B1 conj-w65-dcap-score-bulk-transfer
  B2 conj-w65-dcap-kernel-bulk-census
  B3 conj-w65-dcap-common-ownership
  B4 conj-w65-dcap-tall-same-center-packet
  B5 conj-w65-dcap-closed-overlay   (note the prover's own DEFECT B5.U and
     correction (B5.C) — verify the corrected statement AND rule on whether
     the correction is the unique/legal reading)
  R1 conj-w65-dcap-five-way-completion-split

MANDATORY HOSTILE CHECKS (beyond anything you invent):
1. HYPOTHESIS HONESTY: for EVERY registry shard consumed, open the shard file
   in argument/lemmas/ and check its hypothesis block line-by-line against the
   D-cap class. Any use of a lem-icap-* shard whose hypotheses assume
   M_I >= 1/16 (the I-cap class) is an instant INVALID for that node.
2. Every constant's arithmetic: recompute each displayed inequality chain
   (e.g. the 1/42 census, c_m/768, (2+delta)e_delta, 2tau/15, 1/80 = 5/80
   arithmetic, the (3,1,1) robust-starvation call and its 2^-16 ceiling,
   gamma_dis = 7c_m/960, the normalization (1.6)-(1.7)).
3. Quantifier order and boundary ownership: the certificate/kernel/display
   field are fixed BEFORE classification; every equality case has a declared
   owner; no favorable selection anywhere.
4. R2 discipline: exactly one common nonnegative test per foldback; errors
   scale by source mass, not root/class counts; no summed pairwise demands.
5. Legality of the robust-starvation call in R1: the actual row fiber, A >= 4,
   the [tau/2, 2tau] synthetic endpoint after (1.6), the O(delta) residual,
   and the fiber-aggregate tail definition (1.8) must match
   lem-hx-robust-scalar-starvation's hypothesis block EXACTLY.
6. Walls: context/FINDINGS.md dead routes are absolute; check each proof
   against the kill-list codes K1-K10 of DCAP-ATTACK.md §3.
7. Clone invariance of every public quantity and threshold.

DELIVERABLE: VERDICT-dcap-batch.md with:
- One verdict line per node, in order, EXACTLY in this format:
    <node-id>: VALID | VALID-WITH-CORRECTION | INVALID | UNDECIDED
- For VALID-WITH-CORRECTION: the exact corrected statement and the exact
  failing lines of the original.
- For INVALID: the explicit counterexample or the irreparable gap, with the
  exact failing line quoted.
- A final section "CROSS-CUTTING" for any defect that spans nodes (e.g. a
  notation drift between DCAP-ATTACK.md and the appendix).
- Rule explicitly on DEFECT B5.U / correction (B5.C).

Write ONLY VERDICT-dcap-batch.md. Do not touch any other file. You promote
nothing; your verdicts are inputs to a separate banking step.
