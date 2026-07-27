# BRIEF — fresh hostile audit of DESIGN-S1-POLAR-v6.md (seventh stage; narrow)

You are a fresh, independent, HOSTILE auditor. You did NOT write any prior
design or audit on this front. `DESIGN-S1-POLAR-v6.md` claims the
prescribed finite-dimensional domain-closure repair (AUDIT-S1-POLAR-v5.md
§6 option 1) with everything else byte-stable from v5. The v5 audit already
verified: helpers 13a–13d, row-13 clauses A₁–A₄ and R, all monotonicity
directions, scalar arithmetic, carry-forward, sources, dimension-freeness,
serial order. Do NOT re-audit those UNLESS the v6 changes touch them.

## Your tasks

1. **Verify the domain closure is complete and coherent.** The
   finite-dimensional insertion must appear in ALL NINE places: base rows 6
   (`lem-stage1-approximate-group-laws`), 7
   (`lem-stage1-polar-path-admissibility`), 8
   (`lem-stage1-inversion-derivative-control`); helpers 13e, 13f, 13g; and
   row-13 clauses (A₅), (A₆), (A₇). After the insertion, trace each
   definite description in those nine contracts to a matching-domain
   producer: g_V and chart coverage from row 2 (finite-dimensional — check
   the guards match), (u_δ, h_δ) from row 4 (finite-dimensional — check the
   same δ-guard is in force at every use site), g_sJ from row 2. Any
   remaining map used on a domain wider than its producer is a REFUTATION.
   Also check the DOWNSTREAM sweep claim: every one of the six downstream
   rows and every obligation-ledger line already assumed finite dimension —
   confirm row by row.
2. **Hunt the reverse defect.** The insertion WEAKENS rows 6–8. Check no
   OTHER proposed row or helper (esp. rows 5, 9–11, helpers 13a–13d, the
   smooth rows, and the six downstream rows) consumed rows 6–8 on the wider
   domain — a consumer that quantifies over every exact-unit algebra and
   imports the now-narrower rows 6–8 would inherit exactly the defect just
   repaired. Sweep every dependency edge into rows 6/7/8 and helpers
   13e–13g.
3. **Diff integrity.** Diff v6 against v5: only the declared changes (the
   nine domain insertions, the 13e–13g budget re-projections, §0, the
   disposition table, and the downstream-sweep paragraph). Any other
   change — one word in any contract — is a finding.
4. **Provenance sanity.** v6 keeps rows 6–8's provenance cells unchanged,
   arguing the restriction is a weakening. Confirm that reading (TeX
   857–912 presents the maps for the source's exact-unit algebras; a
   finite-dimensional restriction claims less, so the loci still support
   the contracts).

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v6.md`

- Verdict per insertion site (all 9), for the definite-description trace,
  the reverse-defect sweep, diff integrity, and provenance: VALID /
  VALID-WITH-CORRECTIONS (exact) / REFUTED (concrete defect).
- Final disposition: LAND (v6 is the landable design, gated on the
  definition/ratification gate and user ratification) / REDESIGN /
  ROUTE-ALARM.
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v6.md`.
- No repairs beyond stating corrections; no status promotion; nothing here
  is rigorous. NOT IN LOCAL REFS discipline applies.
