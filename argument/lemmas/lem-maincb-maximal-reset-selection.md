---
id: lem-maincb-maximal-reset-selection
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN, then the nonempty set of m admitting an extended W.c0_cb*epsilon-inclusion w:C^m->A with ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon has a maximum because the lower norm is positive and m <= dim_C A.
defs: def-maincb-reset-state; def-maincb-witness-ledger; def-projection-basis; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-structural-domain-ledger; lem-maincb-initial-reset-inclusion; lem-maincb-reset-constant-ledger
status: stated
af: seeded
workspace: proofs/lem-maincb-maximal-reset-selection
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M22 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1417; deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule)
owner: A
---
**Status.** `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M22 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M22. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1417
