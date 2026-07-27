# BRIEF — MAIN-STRUCTURE fifth repair (prescribed; audit-v4 binding; TWO FIXES ONLY)

You are a fresh, independent design mathematician executing a PRESCRIBED
repair of exactly two defects. `AUDIT-MAIN-STRUCTURE-v4.md` is BINDING. Its
verdicts on `DESIGN-MAIN-STRUCTURE-v4.md`: v3-audit defects A, C, D and the
M07-import defect are CLEARED; M03/M04/M11/M12/M19-S1/M19-R VALID; all
retained rows byte-verified with no drift; P0 schema-complete with the
operator-space body byte-equal to TeX 1453–1464; hazards and
dimension-freeness valid. Exactly TWO defects remain (its §3):

## Fix 1 — restore the identity tie in M19-S2 and M19-S3 (audit §3.1)

v4 quantifies a good extended ambient A and a good extended inclusion w,
but then separately quantifies "a supplied MAIN partition state" without
saying the state's recorded ambient and map EQUAL the displayed A, w. Apply
the audit's exact correction: in M19-S2 and M19-S3 replace the independent
state clause by "a supplied MAIN partition state for this same A, w" (or
the v3 phrase: the partition state "comes from" this displayed
w: ℂ^m → A), and state that the supplied reset state(s) refer to the U
(respectively U, V) of that same partition state. Then the M04 deductions
ε_U, ε_V, ε_R ≤ Lε attach to the right corners. Record this identity
constraint in the interface/domain escalation ledger (v4's entries at
lines ~574–576, 599–601 mention only separately quantified bounds and two
reset states — extend them).

## Fix 2 — give M13 its ambient-algebra producer (audit §3.2)

M13 promises a closed `def-extcb-datum`, whose first field is an extended
ε-C*-algebra, but no exact dependency exports that A_R is an extended
ε_{A_R}-C*-algebra. Apply the audit's exact correction: add
`lem-compcb-corner-algebra` as a DIRECT M13 dependency; absorb its e_ca
threshold and universal corner-algebra coefficient into e_s2 and C_s2;
and add that dependency and threshold to the serial landing step and the
escalation ledger.

## What NOT to change

EVERYTHING ELSE — copy `DESIGN-MAIN-STRUCTURE-v4.md` forward byte-stable
except: the two fixes above, §0 (exact delta vs v4 citing the audit item
per change), the escalation-ledger additions, the affected landing-order
step annotations, and the disposition table (now covering EVERY finding of
`AUDIT-MAIN-STRUCTURE-v4.md`: CLEARED-BY / unchanged-VALID). Do not touch
any row the audit marked VALID or exact-retained; do not reword M12/M25–M27
(their "comes from"/tied-state phrases are already correct).

## Deliverable — write `docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md`

Full standalone document, same structure as v4.

## Hard constraints

Design only; write ONLY inside
`docs/plans/2026-07-26-MAIN-STRUCTURE-design/`; no registry/definitions
mutation; no status promotion; retained contracts verbatim; NOT IN LOCAL
REFS discipline.
