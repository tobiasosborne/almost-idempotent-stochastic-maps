# BRIEF — M17 typed-quantification amendment (aism-73ur)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation. Write your design to
`docs/plans/2026-08-01-M17-TYPING-design/DESIGN-M17-TYPING.md`. A separate
fresh agent hostile-audits it; the user then ratifies. This is a SMALL,
focused round — one contract.

## The established finding (verifier record, 2026-08-01, two runs)

M17 `lem-maincb-stage3-raw-merge` (`argument/lemmas/lem-maincb-stage3-raw-merge.md`,
contract from `DESIGN-MAINCB-REPAIR-v2.md` sect-4) is unprovable as worded:
its root quantifies over "every amplified four-corner datum in A_R with
common defect rho <= C_cross^0*t and target ambient defect
epsilon_{A_R} <= t <= W.e_cross", but
`def-four-corner-merging-datum` types neither A_R (as a finite-dimensional
extended epsilon_{A_R}-C*-algebra) nor B_U,B_V (as finite-dimensional
C*-algebras with B_U oplus B_V the source), while BOTH deps require those
typings: `lem-maincb-isomorphism-unit-control` (B a finite-dimensional
C*-algebra, A a finite-dimensional extended epsilon-C*-algebra) and
`lem-extcb-four-corner-merge` (four fixed BIJECTIVE level-one corner maps).
Verifiers rejected the in-tree missing-premise repair
(`proofs/lem-maincb-stage3-raw-merge/ledger/`, ch-ea9888f43d6f3f92,
ch-a7589f94ff679eed, ch-61789c52351528f5, ch-40fe16a76915988d — read all
four; the last also demands explicit C_iso_unit >= 0 handling).

## Your task

1. **The amended M17 contract** (one physical ASCII line): add the typing
   hypotheses following the PROVEN precedent of banked M19-R
   (`argument/lemmas/lem-maincb-reset-invariant-preservation.md`, T0),
   which explicitly types its corner in the hypothesis ("...into an
   extended epsilon_R-C*-corner A_R, assume A_R is an extended
   epsilon_R-C*-algebra and the literal output map ..."). Expected shape:
   hypothesize A_R a finite-dimensional extended epsilon_{A_R}-C*-algebra,
   B_U,B_V finite-dimensional C*-algebras, the datum's four corner maps
   bijective (check what lem-extcb-four-corner-merge's landed contract
   actually requires and mirror it exactly), and whatever nonnegativity
   phrasing the isomorphism-unit application needs. KEEP the conclusion
   unchanged (extended D_3*t-isomorphism with the unit bound).
2. **Consumer dischargeability**: verify clause-by-clause that M26 (its
   sole consumer, `lem-maincb-binary-block-merge`, ENV-repaired landed
   contract) can DISCHARGE every added hypothesis from what M19-S3 (T0)
   and M12 (T0) actually export — quote the exporting clauses. If any
   added hypothesis is NOT dischargeable, STOP and say so (that would be
   a deeper finding, not a typing fix).
3. **Bijectivity audit**: does M12's banked contract/export state that the
   four corner maps of its datum are bijective where four-corner-merge
   needs it? Quote `proofs/lem-maincb-cross-class-merging-datum/export.md`
   loci. If M12 exports weaker data, state the exact gap and the minimal
   fix (an M17 hypothesis, NOT an M12 amendment — M12 is frozen T0).
4. **Budget + re-seed guidance** for the parked M17 tree (6/11 validated;
   which nodes survive verbatim under the typed root).
5. **Risk register**: what a hostile verifier attacks first; top two ways
   this could be wrong.

## Hard constraints

- ONE contract amended (M17). NO other row, NO def, NO T0 row changes.
  If you conclude more must change, STOP and report why instead.
- Typed-witness laws i/ii (`docs/LEARNINGS.md` 2026-07-28); dimension-free
  constants; no numerical values in the contract.
- Ground truth loci into `refs/kitaev-2405.02434/approximate_algebras.tex`
  only (the merge source is `:1325-1359`; M17's row provenance
  `:430-455,1194-1222,1325-1359,1443`).
