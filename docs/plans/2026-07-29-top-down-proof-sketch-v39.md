# Top-down proof sketch v39: op-classical (2026-07-29, session 36 delta — the Stage-1 downstream quotient block CLOSED: T0 113 → 117; the designed elevation surface is EXHAUSTED)

## UNCHANGED from v38

The global architecture (Route F via positive approximate retract; the
signed trunk PAUSED; arms A/C/D/E/F/R/G parked tier-1-override; XE
fallback), the W97 rebuild results, row 13 (`lem-stage1-polar-constant-
ledger`) as the Stage-1 keystone, the two retired parents
(`lem-stage1-approximate-group-laws`,
`lem-stage1-smooth-unitary-operations` — retired in place), and the two
BINDING process laws + build-granularity discipline of LEARNINGS
2026-07-28 all stand as in v38. `op-classical` remains OPEN.

## Map change 1: the S1-POLAR-v6 §5 downstream block is fully T0 (four banks)

Session 36 banked, strictly serially, with the verified banking sequence
(af export → oracle → `fr verify` → mechanical flip → regenerate → gate
→ commit → push):

1. **`lem-stage1-quotient-left-inversion` (120th, T0 → 114).** 10-node
   tree; one major challenge (node 1.6, smoothness of the descended
   inversion leaning on quotient-submersion/local-section properties
   outside the allowed externals) repaired in-ledger with two
   freshly-verified bridging substeps.
2. **`lem-stage1-quotient-inversion-index-data` (121st, T0 → 115).**
   12-node tree; two major challenges on the derivative branch (the
   radius guard `e_idx^r <= e_H^r, e_quot^r` proved locally before
   applying the quotient externals; the tangent-quotient identification
   rebuilt via explicit local slice charts); includes the
   audit-mandated square-root phase-lift node.
3. **`lem-topology-finite-triangulation` (122nd, T0 → 116; bead
   `aism-j5t9` CLOSED).** First-pass, ZERO challenges, 6 nodes, on the
   SECOND clean re-seed. The path there produced a process finding
   (Map change 2). The four sed-space-verified Munkres externals
   (Thm 10.6; Def 8.1; Def 8.3; Def 1.1 "non-bounded") made the
   ballooned from-scratch unpacking unnecessary, exactly as the bead
   predicted.
4. **`lem-stage1-quotient-finite-cw` (123rd, T0 → 117).** First-pass,
   ZERO challenges, 4 nodes. The compact quotient manifold is a finite
   polyhedron with finite CW type.

With rows 1–13, maximal-simplex, and the five downstream rows all T0,
**every designed-and-landed Stage-1 elevation target is validated.**
The Stage-1 topological substrate for the Lefschetz–Hopf application
(connected finite-CW H-space with left inversion; isolated fixed point
of index +1) is now fully rigorous in-repo.

## Map change 2: the scan-OCR locus trap (FINDINGS 2026-07-29; an L1 near-miss caught pre-banking)

The first triangulation re-seed registered Def 8.1/8.3 externals whose
quotes were verbatim text of the WRONG passage: python `splitlines()`
counts the OCR txt's 117 form-feed page separators as line breaks, so
"line 3332" in splitlines-space is ~82 lines earlier than the sed/grep
locus convention. `check-refs` passed regardless — it verifies
quote-exists-somewhere, not quote-at-claimed-locus. A STUCK run
validated 5 nodes against those corrupted externals (node 1.2 cited
both and was ACCEPTED — a recorded verification near-miss: a fresh
verifier does not audit external CONTENT against `refs/`). All five
validations were discarded with the workspace; ledgers preserved in git
history. New orchestrator-side registration rule (FINDINGS): extract in
`\n`-only space AND verify quote-at-claimed-locus programmatically AND
eyeball the opening words against the page image.

## The open surface after this delta (all fronts need design or user decisions)

1. **G-S1 (the one remaining critical-path design gap).** The three
   Stage-1 split producers (`lem-stage1-rectified-nontrivial-projection`,
   `lem-stage1-original-complementary-pair`,
   `lem-stage1-fresh-two-point-inclusion`; source targets
   `approximate_algebras.tex:917-969,1419-1424`) are ABSENT from the
   registry and gated on their own not-yet-existing repaired + audited
   design. Next concrete step: a fresh codex DESIGN job + hostile audit
   (allowed in a zero-live-run window), then landing the three contracts
   (user ratification per the W78/W97 precedent). G-S1 blocks M19-S1
   through M28, NOT the MAIN pre-gate rows.
2. **MAIN pre-gate (P0 + M01–M18).** `DESIGN-MAIN-STRUCTURE-v5.md` is
   audited (REPAIR-CONFIRMED, ratified in the W78 package) but begins
   with a HARD STOP: the P0 definition gate (four datum-only def shards,
   none in the registry) — new definitions need user sign-off (Rule 7).
   Only M03 (`lem-maincb-error-improvement`) is landed, and its audited
   design REWIRES its deps from `lem-extcb-exact-target-correction` to
   M02 — so M03 must NOT be elevated against its current registry deps;
   land P0 + M01/M02 first.
3. **Polar §9 steps 28–29** (three trace rows + corrected
   `lem-stage1-extra-fixed-class`): still blocked on their own audited
   designs (not yet written).
4. **Decoupled campaigns:** the 14-row ledger, then the strengthened
   k-ledger (D4 releases), f0-assembly, root rewire LAST — unchanged
   from v36.

## Controller note

FH remains the primary arm (300+ pulls). The elevation cadence this
session was 4 banks + 3 aborts-with-diagnosis in one day at tier
routine; the external resource wall (codex usage) was not hit. The next
non-resource blocker is a stack of USER decisions: launch the G-S1
design cycle; ratify the MAIN P0 definitions; commission the trace-row
designs.
