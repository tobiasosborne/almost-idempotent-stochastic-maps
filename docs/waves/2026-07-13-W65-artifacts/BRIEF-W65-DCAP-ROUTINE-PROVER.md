# W65 routine prover — standalone proofs of the D-cap routine batch

You are a fresh, independent prover. You did NOT write DCAP-ATTACK.md; treat it
as a specification, not an authority. Your workspace is this directory: the
full registry snapshot (argument/, definitions/) + context docs (context/) +
the strategy artifact DCAP-ATTACK.md.

TASK: produce APPENDIX-dcap-proofs.md containing COMPLETE, STANDALONE proofs of
the seven routine nodes of DCAP-ATTACK.md §§1.2-1.8, in order:

  R0 (conj-w65-dcap-root-closure)
  B1 (conj-w65-dcap-score-bulk-transfer)
  B2 (conj-w65-dcap-kernel-bulk-census)
  B3 (conj-w65-dcap-common-ownership)
  B4 (conj-w65-dcap-tall-same-center-packet)
  B5 (conj-w65-dcap-closed-overlay)
  R1 (conj-w65-dcap-five-way-completion-split)

RULES (violations = the proof is rejected):
- Each proof: restate the pinned contract VERBATIM from DCAP-ATTACK.md, list
  the exact registry shards consumed (with their hypothesis blocks checked
  line-by-line against the D-cap class), then a complete proof with every
  constant's arithmetic displayed. Adopt all notation of
  context/DECOMPOSITION-W63-I.md §§0-1.1 and DCAP-ATTACK.md §1.1.
- HYPOTHESIS HONESTY (the #1 hostile check downstream): you may NOT consume
  lem-icap-* shards whose hypothesis blocks assume the I-cap class
  (M_I >= 1/16). B1-B5 must be proved from L0/lambda_A, the SL1a corner bank
  (lem-sl1a-score-selector, lem-sl1a-corner-ledger, lem-radial-horn-partition),
  lem-l5-positive-flow-foldback (R2), lem-ihorn-tall-halo-saturation (T),
  lem-ihorn-universal-exterior-package (E), lem-ihorn-cotop-sl1a-package (L0),
  and the zero-face bank (lem-always-tight-dual-support,
  lem-optimal-face-conic-reduction, lem-positive-exposedness-margin,
  lem-zero-face-localization). If a kernel-arbitrary W64 mechanism is reused,
  REPROVE it here in full on the D-cap class.
- If a claimed routine step does NOT actually follow — if you find a gap,
  a wrong constant, a quantifier error, or a hypothesis mismatch — DO NOT
  paper over it. Record it in a clearly marked "DEFECT" block with the exact
  failing line and, if you can, the correction. Finding a defect is a success.
- Signed picture; clone-invariant full-fiber quantities; no 1/t*; conic
  coefficients are geography, not transitions; one R2 foldback per common
  nonnegative test, never summed pairwise demands; equality/boundary ownership
  exactly as assigned in DCAP-ATTACK.md; context/FINDINGS.md dead routes are
  ABSOLUTE.
- Everything you write remains proposed/conjecture; you promote nothing.

Write ONLY APPENDIX-dcap-proofs.md in the workspace root. Do not touch
argument/ or definitions/ or DCAP-ATTACK.md.
