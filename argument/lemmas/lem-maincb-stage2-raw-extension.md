---
id: lem-maincb-stage2-raw-extension
kind: lemma
contract: After first fixing the universal C_s2^0,e_s2^0 witnesses of lem-maincb-stage2-extcb-datum, C_ext,e_ext witnesses of conj-extcb, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_2 < infinity and e_2 > 0 such that for every def-maincb-witness-ledger datum W with W.e_s2 <= min{e_s2^0,e_2}, C_s2^0*e_2 <= e_ext, and (C_ext+1)*C_s2^0*e_2 <= e_iso_unit, every explicit Stage-2 raw-call closed EXT-CB datum in A_R with total post-helper defect at most C_s2^0*t and 0 <= t <= W.e_s2 admits an extended D_2*t-isomorphism v_+:M_{r+1}->A_R satisfying ||v_+(I_{M_{r+1}})-u_{A_R}|| <= D_2*t.
defs: def-maincb-raw-call; def-maincb-witness-ledger; def-extcb-datum; def-operator-space; def-extended-delta-inclusion
deps: lem-maincb-stage2-extcb-datum; conj-extcb; lem-maincb-isomorphism-unit-control
status: stated
af: seeded
workspace: proofs/lem-maincb-stage2-raw-extension
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M16 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:430-455,1194-1222,1378-1412,1435-1441
owner: A
---
**Status.** `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M16 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M16. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:430-455,1194-1222,1378-1412,1435-1441
