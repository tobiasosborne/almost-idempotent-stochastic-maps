Created [DESIGN-M17-TYPING.md](/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/docs/plans/2026-08-01-M17-TYPING-design/DESIGN-M17-TYPING.md).

Amended one-line contract:

```text
contract: After first fixing the universal C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum, C_merge,a_merge witnesses of lem-extcb-four-corner-merge, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_3 < infinity and e_3 > 0 such that for every def-maincb-witness-ledger datum W with W.e_cross <= min{e_cross^0,e_3}, (C_cross^0+1)*e_3 <= a_merge, and (C_merge*(C_cross^0+1)+1)*e_3 <= e_iso_unit, every amplified four-corner datum in A_R with source B_U oplus B_V, with B_U and B_V finite-dimensional C*-algebras, with A_R a finite-dimensional extended epsilon_{A_R}-C*-algebra, whose four fixed level-one corner maps are bijective, and with 0 <= rho <= C_cross^0*t and 0 <= epsilon_{A_R} <= t <= W.e_cross yields an extended D_3*t-isomorphism v:B_U oplus B_V->A_R satisfying ||v(I_{B_U oplus B_V})-u_{A_R}|| <= D_3*t.
```

- Dischargeability: **FAIL**. M26 can discharge every added clause except bijectivity.
- Bijectivity audit: M12 proves the four maps bijective internally, but neither M12 nor M19-S3 exports that fact in its root contract. Typed-witness rules therefore make it unavailable to M26.
- Escalation: **STOP before ratification or re-seeding**. A new validated bijectivity bridge with an explicit consumer path, or a strengthened and revalidated M12/M19-S3 interface, is required. Both exceed the one-contract scope.
- Validation: `sh scripts/check-all.sh` passed with `[check-all] OK`. No protected directory was modified.