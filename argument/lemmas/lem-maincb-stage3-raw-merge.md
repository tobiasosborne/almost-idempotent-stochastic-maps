---
id: lem-maincb-stage3-raw-merge
kind: lemma
contract: After first fixing the universal C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum, C_merge,a_merge witnesses of lem-extcb-four-corner-merge, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_3 < infinity and e_3 > 0 such that for every def-maincb-witness-ledger datum W with W.e_cross <= min{e_cross^0,e_3}, (C_cross^0+1)*e_3 <= a_merge, and (C_merge*(C_cross^0+1)+1)*e_3 <= e_iso_unit, every amplified four-corner datum in A_R with common defect rho <= C_cross^0*t and target ambient defect epsilon_{A_R} <= t <= W.e_cross yields an extended D_3*t-isomorphism v:B_U oplus B_V->A_R satisfying ||v(I_{B_U oplus B_V})-u_{A_R}|| <= D_3*t.
defs: def-maincb-raw-call; def-maincb-witness-ledger; def-four-corner-merging-datum; def-operator-space; def-extended-delta-inclusion
deps: lem-maincb-cross-class-merging-datum; lem-extcb-four-corner-merge; lem-maincb-isomorphism-unit-control
status: stated
af: seeded
workspace: proofs/lem-maincb-stage3-raw-merge
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M17 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:430-455,1194-1222,1325-1359,1443
owner: A
---
**Status.** `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M17 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M17. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:430-455,1194-1222,1325-1359,1443
