---
id: lem-maincb-stage1-maximality
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN and w:C^m->A has maximum source dimension among all extended W.c0_cb*epsilon-inclusions satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, then every projection-basis image P_j=w(e_j) satisfies dim S_{P_j}=1.
defs: def-maincb-partition-state; def-maincb-witness-ledger; def-projection-basis; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-maximal-reset-selection; lem-maincb-stage1-strict-refinement; lem-maincb-reset-constant-ledger
status: stated
af: seeded
workspace: proofs/lem-maincb-stage1-maximality
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M24 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1417-1426; deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule)
owner: A
---
**Status.** `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M24 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M24. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
4 / 2 / 8. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1417-1426
