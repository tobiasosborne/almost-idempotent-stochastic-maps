# BRIEF — hostile audit of DESIGN-RECFIELD-REPAIR.md (fresh verifier)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-RECFIELD-REPAIR.md`; assume it is wrong until proven otherwise.
It repairs the verifier-refuted recorded-field clauses with explicit
`ENV(R): epsilon_R <= W.L*epsilon` hypotheses for supplied states and
M04-certificate selection for constructed states, amending SIX contracts
(M19-S2, M19-S3, M20, M25, M26, M27) and claiming M12, M18, M21-M24, M28
are sound as landed. Finding an error in EITHER direction is a BIG
SUCCESS: an unrepaired defect re-parks a tree; an over-strong hypothesis
breaks a consumer derivation; a false "sound" verdict ships a refutable
contract to elevation.

## Audit against (read all)

1. `docs/plans/2026-08-01-RECFIELD-REPAIR-design/BRIEF-RECFIELD-REPAIR.md`
   (what was asked; every deliverable and constraint).
2. The countermodel evidence: `proofs/lem-maincb-stage2-call-envelope/ledger/`
   (challenges ch-5db0cccd95d6fcc7, ch-dfa6b07f88648996; validated
   countermodel nodes 1.1.2, 1.1.5.1). Does the ENV repair actually
   dissolve the countermodel — and does ANY repaired row still assert a
   bound on a free recorded field?
3. The current landed contracts (`argument/lemmas/lem-maincb-*.md`) and
   `DESIGN-MAINCB-REPAIR-v2.md` sect-4 (what is being amended).
4. The frozen T0 set (14 pre-session + lem-maincb-isomorphism-unit-control,
   lem-maincb-witness-arithmetic, lem-maincb-compressed-corner-unit-comparison,
   lem-maincb-stage2-raw-extension, lem-maincb-reset-invariant-preservation —
   all banked 2026-08-01). Independently verify NO repaired contract forces
   any change to them or to a registered external in a validated workspace.
5. `refs/kitaev-2405.02434/approximate_algebras.tex:1414-1444` (the
   induction the repaired rows must still implement) and every locus the
   design cites.
6. `definitions/def-maincb-partition-state.md`, `def-maincb-reset-state.md`
   (the design claims NO def change is needed — attack that claim), and
   `docs/LEARNINGS.md` 2026-07-28 laws i/ii.

## Specific attack surface

- **The ENV hypothesis shape:** is `epsilon_R <= W.L*epsilon` as a
  HYPOTHESIS dischargeable by every caller in the induction
  (M28's per-class calls, M27's binary merges, M23's refinement loop)?
  Trace the actual call chain: who SUPPLIES a state to M19-S2/S3 and can
  that caller PROVE the ENV bound at supply time (via M04-certificate
  selection in M25/M26's constructions)? An undischargeable hypothesis
  makes the induction vacuous — that is a ROUTE-LEVEL ALARM.
- **The M04-certificate selection move:** M04 exports existence of a
  bound; "selecting" the certificate at construction time must be
  typed-witness-lawful (laws i/ii), not a new anaphor.
- **The five "sound" verdicts** (M12, M18, M21-M24, M28): hunt for a
  remaining free-recorded-field assertion in each — the exact defect
  pattern — especially M21 (epsilon fields at C->A), M22's selection
  class, and M28's final assembly bounds.
- **The M25 strengthening:** necessary for which consumer, and does the
  strengthened form remain provable from M16 + M19-R (both frozen T0)?
- **Interface re-check:** M19-S3 -> M12 (M12's hypotheses
  epsilon_U,epsilon_V,d_U,d_V <= t and the two unit estimates — does the
  repaired M19-S3 still derive ALL of them?), M26 -> M27 -> M28, and
  M20's comparison exports to M21-M28.
- **Dimension-freeness:** no class-count/stage-index leak introduced by
  ENV threading through the induction.
- **Budgets/re-seed guidance:** plausible vs the caps; the M19-S2
  re-seed correctly archives the countermodel nodes.

## Deliverable — write `docs/plans/2026-08-01-RECFIELD-REPAIR-design/AUDIT-RECFIELD-REPAIR.md`

- Verdict per repaired contract (6) AND per "sound" verdict (rest of the
  unbanked rows): VALID / VALID-WITH-CORRECTIONS (exact corrected text) /
  REFUTED (show why, countermodel if possible).
- The call-chain dischargeability trace for ENV (explicit).
- Final disposition: DESIGN-CONFIRMED (ready for user ratification, with
  exact corrections listed) / DESIGN-REFUTED / ROUTE-ALARM.
- Cite every check with exact loci (file:line).

## Hard constraints

- Write ONLY the AUDIT file. No repairs beyond stating exact corrections;
  no status promotion. NOT-IN-LOCAL-REFS discipline (L1): a claimed
  ground truth absent at its cited locus is a FINDING.
