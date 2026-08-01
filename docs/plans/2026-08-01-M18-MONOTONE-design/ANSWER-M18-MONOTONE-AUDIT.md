**DESIGN-REFUTED** — audit written to [AUDIT-M18-MONOTONE.md](/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/docs/plans/2026-08-01-M18-MONOTONE-design/AUDIT-M18-MONOTONE.md).

- F1: Use the consumer-normal typing `B` finite-dimensional C*-algebra, `A` finite-dimensional extended ε-C*-algebra, `v:B->A`.
- F2: Stage 2 must construct a new raw-call record with source `M_{r+1}`, target `A_R`, output `u_2:=v_+`, and raw defect `D_2*t`.
- F3: Stage 3 must construct a new record for `u_3:=v`; it cannot identify M17’s existential witness with the envelope’s pre-existing `v_R`.
- F4: With those new records, existential instantiation obeys W93 and M18’s contract remains byte-identical.
- F5: All clauses are monotone, no `delta'<1` ceiling is needed, and budgets `3/2/6` and `12/3/16` remain realistic.