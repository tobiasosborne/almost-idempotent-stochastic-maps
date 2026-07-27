# BRIEF — S1-POLAR sixth repair (prescribed; audit-v5 binding; DOMAIN CLOSURE ONLY)

You are a fresh, independent design mathematician executing a PRESCRIBED
narrow repair. `AUDIT-S1-POLAR-v5.md` is BINDING. Its verdicts on
`DESIGN-S1-POLAR-v5.md`: helpers 13a–13d VALID; row-13 clauses A₁, A₂, A₄
(and A₃) VALID; R VALID; all monotonicity directions VALID; budget
VALID-WITH-CORRECTIONS; carry-forward, sources, dimension-freeness, serial
order VALID. ONE defect family remains (its §0): a DOMAIN-CLOSURE mismatch —
base producers 6–8 (group laws, path admissibility, inversion derivative),
helpers 13e–13g, and row-13 clauses (A₅)–(A₇) quantify over EVERY exact-unit
ε_r-C*-algebra while the graph and polar producers (rows 2 and 4) that
supply g_V and (u_δ, h_δ) are stated only for FINITE-DIMENSIONAL algebras.
A definite description ("the unique inverse") is not an existence theorem.

## The prescribed repair — audit §6 OPTION 1 (finite-dimensional closure)

Adopt the audit's option 1, which it identifies as smallest for the stated
downstream consumers (every Route-F consumer is finite-dimensional; the
Stage-1 quotient rows explicitly use finite dimension). Option 2
(all-domain producers) is DECLINED — record that decision and its rationale
in §0.

Exactly these changes:

1. In base producer rows 6 (`lem-stage1-approximate-group-laws`), 7
   (`lem-stage1-polar-path-admissibility`), and 8
   (`lem-stage1-inversion-derivative-control`): change "for every
   exact-unit ε_r-C*-algebra" to "for every FINITE-DIMENSIONAL exact-unit
   ε_r-C*-algebra". No other change to those contracts.
2. The same domain insertion in helpers 13e, 13f, 13g — AND, per the
   audit's §1 note on their budgets, ensure each of 13e–13g (like their
   bases) now introduces its maps on a domain where rows 2/4 supply them:
   with the finite-dimensional restriction this is automatic; keep the
   definite descriptions but they are now backed by the matching-domain
   producers.
3. The same domain insertion in row-13 clauses (A₅), (A₆), (A₇). (This
   restores what v4 had — but now COHERENTLY, because the producers change
   too. Cite audit-v5 §6 option 1 as the binding cause; note explicitly
   that the v4 audit's refutation of the insertion was about
   producer-mismatch, which this repair eliminates.)
4. Check the provenance cells of rows 6–8: TeX 857–912 presents these
   maps for the exact-unit algebras of the source discussion; the
   finite-dimensional restriction is a WEAKENING of the claimed statement,
   so no provenance changes — but say so.
5. Downstream sweep: verify no downstream row or obligation-ledger line
   consumed the wider domain of rows 6–8 (they are all finite-dimensional
   already — confirm row by row and state it).
6. Re-project budgets ONLY where the audit flagged them (13e–13g's 4/2
   now credible with matching-domain producers — re-state; row 13 stays
   11/3).

## What NOT to change

EVERYTHING ELSE: rows 1–5 and 9–12, helpers 13a–13d, clauses A₁–A₄ and R,
the six downstream rows, the obligation ledger, definitions,
dimension-freeness, sources, serial order — all byte-stable vs v5.

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md`

Full standalone document: §0 = exact delta vs v5 (each change against the
audit item; the option-1 decision recorded with rationale and the declined
option 2 noted), the corrected table, and a disposition table covering
EVERY finding of `AUDIT-S1-POLAR-v5.md` (CLEARED-BY / unchanged-VALID).

## Hard constraints

Design only; write ONLY inside `docs/plans/2026-07-26-S1-POLAR-design/`;
no registry/definitions mutation; no status promotion; no meta-language;
no guessed constants; NOT IN LOCAL REFS discipline.
