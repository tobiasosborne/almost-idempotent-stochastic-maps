# BRIEF — hostile audit of DESIGN-M17-TYPING-v2.md (fresh verifier)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-M17-TYPING-v2.md`; assume it is wrong until proven otherwise. It
proposes ONE new bridge row (`lem-maincb-cross-datum-bijectivity`) plus the
typed M17 contract. Finding an error in either direction is a BIG SUCCESS.
The design itself names its two kill-shots — attack those first:

1. **The same-datum identification.** The bridge names the four maps
   explicitly (gamma_UU, gamma_UV, gamma_VU, gamma_VV via displayed
   compression formulas) and asserts these ARE the four fixed maps of the
   datum M12 furnishes. Byte-compare against M12's banked contract and its
   validated export (`argument/lemmas/lem-maincb-cross-class-merging-datum.md:4`,
   `proofs/lem-maincb-cross-class-merging-datum/export.md`): does M12's
   conclusion pin its datum's maps to exactly these formulas, or could a
   verifier claim the datum's maps are only existentially given (the
   anaphora/same-witness defect pattern, W93 / AUDIT-MAINCB-REPAIR §3.3)?
2. **The shared shrunken-witness selection.** The bridge asserts its
   C_cross^0, e_cross^0 "are valid witnesses of
   lem-maincb-cross-class-merging-datum". Is that a lawful typed-witness
   move (provider fixed first) or does it smuggle a cross-shard existential
   identification the verifiers refuse?

Then:
- **Bijectivity provability**: the diagonal maps are compositions of
  compressions applied to extended isomorphisms; verify from EXPORTED T0
  clauses only (`lem-maincb-outer-compression-transfer`,
  `lem-maincb-cross-union-zero-corners`,
  `lem-maincb-nested-corner-comparison`, the compcb block —
  quote the exact exporting clauses the design cites and check they say
  what the design needs, esp. level-one bijectivity preservation under
  Co-compressions and that the zero corners are actually {0} under M12's
  hypotheses). Any needed fact that is neither exported nor at a cited
  refs/ locus is a FINDING.
- **The typed M17 contract**: the "furnished by / certified bijective by"
  phrasing — lawful binding or anaphor? The sign-safe C_iso_unit chain
  (v1's ch-40fe16a76915988d) — actually incorporated?
- **Discharge chain** M26 -> M19-S3 -> (M12 + bridge) -> M17: re-derive it
  yourself clause-by-clause from the landed/banked contracts.
- **No-T0-invalidation** and def-layer: zero amendments claimed — verify.
- **Budgets** (bridge; M17 6-node re-seed) and the retained countermodel
  red test.

## Deliverable — write `docs/plans/2026-08-01-M17-TYPING-design/AUDIT-M17-TYPING-v2.md`

Verdict per row (bridge, typed M17): VALID / VALID-WITH-CORRECTIONS (exact
text) / REFUTED. The discharge-chain re-derivation. Final disposition:
DESIGN-CONFIRMED / DESIGN-REFUTED / ROUTE-ALARM. Exact loci for every check.

## Hard constraints

Write ONLY the AUDIT file. Do NOT run git commit, git push, fr, or bd —
bookkeeping belongs to the orchestrator. No repairs beyond exact
corrections; no status promotion; NOT-IN-LOCAL-REFS discipline (L1).
