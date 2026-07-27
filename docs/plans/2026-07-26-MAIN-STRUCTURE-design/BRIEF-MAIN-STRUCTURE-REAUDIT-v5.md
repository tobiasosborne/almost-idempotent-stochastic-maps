# BRIEF — fresh hostile audit of DESIGN-MAIN-STRUCTURE-v5.md (sixth stage; narrow)

You are a fresh, independent, HOSTILE auditor. You did NOT write any prior
design or audit on this front. `DESIGN-MAIN-STRUCTURE-v5.md` claims a
two-fix repair of `AUDIT-MAIN-STRUCTURE-v4.md`'s §3 defects, with
everything else copied byte-stable from v4. The v4 audit already verified:
v3 defects A/C/D cleared, M03 contract byte-equal to the landed line, P0
schema-complete with the operator-space body byte-equal to TeX 1453–1464,
zero retained-row drift v3→v4, hazards and dimension-freeness valid. Do
NOT re-audit what the v4 audit settled UNLESS the v5 changes touch it.

## Your three tasks

1. **Verify fix 1 (audit §3.1).** In M19-S2 and M19-S3: is the supplied
   partition state now EXPLICITLY for the same displayed A, w (and are the
   supplied reset state(s) tied to the U, resp. U,V, of that same state)?
   With the tie in place, do the M04 deductions ε_U, ε_V, ε_R ≤ Lε now
   attach to the corners appearing in the conclusion? Is the identity
   constraint recorded in the escalation ledger? Hunt for the same
   independent-state flaw ANYWHERE else it could recur (M12, M13, M21–M27:
   each row that quantifies both a good A, w and a state/reset data —
   check every one has the tie).
2. **Verify fix 2 (audit §3.2).** Does M13 now directly import
   `lem-compcb-corner-algebra`; does that contract
   (`argument/lemmas/lem-compcb-corner-algebra.md:4-6`) actually export
   what M13's conclusion needs (A_R an extended ε_{A_R}-algebra with a
   universal bound, from a nonvanishing approximate projection — check
   M13's hypotheses supply the nonvanishing input); are e_ca and C_ca
   absorbed into e_s2, C_s2 coherently (no other row's arithmetic
   breaks); do the serial landing step and escalation ledger record it?
3. **Diff integrity.** Diff v5 against v4: the ONLY changes may be the two
   fixes, §0, the ledger/landing-order annotations, and the §12
   disposition. Any other change — even one word in a contract cell — is
   a finding. Then run a short NEW-defect hunt confined to the changed
   text: does the added tie language introduce meta-language ("the
   contract of...") or an unbound reference? Does M13's enlarged
   dependency list stay acyclic and within budget?

## Deliverable — write `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v5.md`

- Verdict per fix: CLEARED / NOT-CLEARED (exact shortfall).
- Diff-integrity verdict and any new-defect findings.
- Final disposition: REPAIR-CONFIRMED (v5 is the landable design, gated on
  P0 + G-S1 and user ratification) / DESIGN-REFUTED / ROUTE-ALARM.
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v5.md`.
- No repairs beyond stating corrections; no status promotion; nothing here
  is rigorous. NOT IN LOCAL REFS discipline applies.
