---
id: lem-maincb-stage1-strict-refinement
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN and an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfies ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon and has some P_j=w(e_j) with dim S_{P_j}>1, then there is an extended W.c0_cb*epsilon-inclusion w_+:C^{m+1}->A satisfying ||w_+(I_{C^{m+1}})-I_A|| <= W.c0_cb*epsilon.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-maincb-witness-ledger; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-stage1-call-envelope; lem-maincb-stage1-raw-refinement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger
status: stated
af: seeded
workspace: proofs/lem-maincb-stage1-strict-refinement
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M23 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:917-969,1194-1222,1419-1426
owner: A
---
**Status.** `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M23 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M23. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
8 / 3 / 12. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:917-969,1194-1222,1419-1426
