Completed [DESIGN-RECFIELD-REPAIR.md](/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md).

- Repair shape: explicit `ENV(R): epsilon_R <= W.L*epsilon` hypotheses for supplied states and explicit M04-certificate selection for constructed states. No definition changes.
- Defective: M19-S2, M19-S3, M20, M26, M27.
- Sound: M12, M18, M21–M25, M28. M25 is sound but strengthened for downstream sufficiency.
- Repaired contracts: 6 — M19-S2, M19-S3, M20, M25, M26, M27.
- Escalation: independent hostile audit and user ratification of those six amendments. No missing-reference, definition, or T0-invalidation escalation.
- Validation: `sh scripts/check-all.sh` passed with `[check-all] OK`.