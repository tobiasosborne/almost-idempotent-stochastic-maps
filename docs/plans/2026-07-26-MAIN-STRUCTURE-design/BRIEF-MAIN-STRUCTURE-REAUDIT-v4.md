# BRIEF — fresh hostile audit of DESIGN-MAIN-STRUCTURE-v4.md (fifth stage)

You are a fresh, independent, HOSTILE auditor. You did NOT write any of the
four designs or the three prior audits. Assume `DESIGN-MAIN-STRUCTURE-v4.md`
is wrong until proven otherwise. Four factorings of this front have fallen
to fresh audits; v4 claims a PRESCRIBED narrow repair of the v3 audit's
defects A–D. The two highest-value findings would be: a prescribed
correction applied incorrectly or incompletely, or a NEW defect introduced
by the corrections themselves (a repair that breaks an adjacent row).

## Your target

`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v4.md`.

## Audit against (read all)

1. `AUDIT-MAIN-STRUCTURE-v3.md` — the binding audit whose §1 defects A–D,
   §2 P0 corrections, §4/§6 per-row corrections, and §8 diff findings v4
   claims to clear. Verify EVERY one is genuinely cleared with the exact
   prescribed content (not paraphrased into something weaker).
2. `DESIGN-MAIN-STRUCTURE-v3.md` and `DESIGN-MAIN-STRUCTURE-v2.md` — v4
   claims verbatim retention of all VALID rows and restoration of the v2
   hypotheses (extended ε-C*-algebra ambient; extended c₀^cb·ε-inclusion w,
   unit clause included). Diff the retained rows; any silent change is a
   finding. Verify the restored hypotheses match v2's actual text.
3. `AUDIT-MAIN-STRUCTURE-v2.md` — the eight §10 requirements still bind
   (P0 before M01; closed envelopes; C_s2 option; invariant row; exact
   deps; G-S1; M27/M28; complete escalation ledger).
4. The landed shards: `lem-maincb-error-improvement.md` (v4 claims M03 is
   now a BYTE-FOR-BYTE copy of its contract line 4 — verify literally,
   character by character), `conj-extcb.md`, `lem-extcb-four-corner-merge.md`,
   the `lem-compcb-*` and `lem-extcb-*` rows, `lem-thmainext-conditional.md`,
   `definitions/def-extcb-datum.md`, `def-four-corner-merging-datum.md`,
   `definitions/README.md` + `definitions/INDEX.md` (schema-completeness of
   the four P0 shard proposals; the operator-space byte-verbatim claim
   against `refs/kitaev-2405.02434/approximate_algebras.tex:1453-1464` —
   check the quoted block IS byte-verbatim).
5. TeX loci: 1054–1082, 1162–1187, 1239–1359, 1414–1450, 1453–1475,
   1508–1557.

## Specific attack surface (check each, then hunt beyond)

- **Defect-A repair (M19-S1).** Does the restored domain (extended
  ε-C*-algebra A; extended c₀^cb·ε-inclusion w WITH unit clause) actually
  kill the v3 audit's M₄ counterexample? Re-run that counterexample against
  the v4 contract: w(λ,μ) = λ(e₁₁+e₂₂)+μe₃₃ is NOT unit-preserving, so it
  must now be excluded — verify the exclusion is by the contract's stated
  hypotheses, not by prose.
- **Defect-B repair (M19-S2/S3, M25/M26/M27).** Trace the restored chain:
  does M04 + the w-defect bound now license d_U ≤ c₀^cb·ε_U ≤ c₀^cb·L·ε ≤
  K₂ε INSIDE the stated hypotheses of each row? Is any needed bound still
  only in §2 prose rather than in a contract?
- **Defect-C repair (M19-R).** Its new hypothesis must make the output an
  M03-eligible map (extended d_raw-inclusion/isomorphism from a named
  finite-dimensional C*-algebra into A_R). Check M03's contract can now be
  applied literally, and that M19-R's hypotheses are all producible by an
  M18-admissible call (no hypothesis nothing can produce).
- **Defect-D repair (t_atom).** Recompute: does M20 now prove
  ε_{j} ≤ Lε ≤ t_atom ≤ r_reset with t_atom = K_call·ε, and is
  K_call = max{1, L, c₀^cb, K₁, K₂, K₃} still produced by earlier rows
  only? Does M25's base step now import M04 directly and use the
  compressed-corner scalar call? Is the new call type registered in the
  raw-call definition's tag set (or does the definition's tag list now
  mismatch the call types M20 quantifies)?
- **The M11–M13 repairs.** ε_A ≤ t added; M07 imported directly by M12 AND
  M13; M13's output a closed EXT datum per def-extcb-datum:13-17 — check
  each against the definition's actual field list.
- **New-defect hunt.** The v3→v4 changes touch shared hypotheses: check
  every consumer of M11–M13 and M19-* for a hypothesis that v4's
  strengthened domains now fail to supply (a row demanding the OLD weaker
  domain would now be unmatchable); check the landing order still
  topologically sorts; check the escalation ledger gained the new items
  (schema-complete defs; the strengthened hypotheses as contract
  corrections vs v2 where applicable).
- **P0 schema completeness (§1).** Four shard proposals with exact
  frontmatter; operator-space byte-verbatim from 1453–1464 ONLY;
  partition-state's recorded-vs-quantified data statement present;
  two-reset-states note present.
- **Hazards + dimension-freeness.** R19/R21/R22 unchanged-valid; the
  t_atom addition and restored bounds must stay universal (any
  n/block/class/stage dependence = ROUTE-LEVEL ALARM).

## Deliverable — write `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v4.md`

- Verdict per v3-audit defect (A, B, C, D, dependency defect, P0, per-row
  corrections): CLEARED / NOT-CLEARED (show exactly what is missing).
- Verdict per changed row and per retained-row diff: VALID /
  VALID-WITH-CORRECTIONS (exact) / REFUTED (concrete defect).
- Final disposition: REPAIR-CONFIRMED (land v4 with any corrections, gated
  on P0 + G-S1) / DESIGN-REFUTED / ROUTE-ALARM.
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v4.md`.
- No repairs beyond stating corrections; no status promotion; nothing here
  is rigorous. NOT IN LOCAL REFS discipline applies.
