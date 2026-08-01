**Disposition: DESIGN-REFUTED / DO NOT RATIFY AS WRITTEN.** Audit written to [AUDIT-CONSUMER-REPAIR.md](/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/docs/plans/2026-08-01-CONSUMER-REPAIR-design/AUDIT-CONSUMER-REPAIR.md).

- F1: M25’s validation has a genuine latent gap; demote and revalidate nodes `1.1.2.2` and `1.1.3.2` using an explicitly typed provider.
- F2: Prefer new `lem-maincb-reset-output-typing` over strengthening M19-R; M25 repair is common to both options, while the bridge avoids the M19-R/M18 cascade.
- F3: `check-refs.py` never detects changed dependency contracts; treat M18 refresh as manual import hygiene, not gate-forced revalidation.
- F4: Keep the proposed M26/M27 contracts; add the monotonicity row and typed-reset bridge directly to M26’s dependencies.
- F5: Banked M19-S2 and M19-S3 contain the same unimported monotonicity inference; demote and revalidate both with the monotonicity dependency.
- F6: Survey contracts stand, but M21 needs witness-arithmetic plus the bridge, M23 needs the bridge, and M28 needs witness-arithmetic plus monotonicity; M22/M24 stand unchanged.
- F7: Remove the fictitious M18 proof-refresh budget and add explicit repair budgets for M19-S2/M19-S3; remaining proposed budgets are conditionally credible.