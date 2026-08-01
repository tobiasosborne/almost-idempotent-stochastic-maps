---
id: lem-maincb-one-class-extension
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, all atomic images are one-dimensional, and C is one equivalence class, then there is a current reset isomorphism v_C:M_{|C|}->A_C whose recorded ambient field epsilon_C is selected so that A_C is an extended epsilon_C-C*-algebra and epsilon_C <= W.L*epsilon <= W.K_call*epsilon, and which satisfies d_C <= W.c0_cb*epsilon_C and ||v_C(I_{M_{|C|}})-u_{A_C}|| <= W.c0_cb*epsilon_C.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-maincb-witness-ledger; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-direct-corner-envelope; lem-maincb-corner-equivalence; lem-maincb-initial-raw-inclusion; lem-maincb-stage2-raw-extension; lem-maincb-stage2-call-envelope; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger; lem-maincb-reset-constant-ledger; lem-maincb-reset-output-typing
status: stated
af: seeded
workspace: proofs/lem-maincb-one-class-extension
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M25 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1378-1412,1430-1441; recorded-field ENV repair per DESIGN-RECFIELD-REPAIR.md sect-3 (hostile-audited AUDIT-RECFIELD-REPAIR.md DESIGN-CONFIRMED zero corrections; user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, second ratification)); deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule); DEMOTED 2026-08-01 (latent unregistered-premise gap, AUDIT-CONSUMER-REPAIR.md F1 (nodes 1.1.2.2/1.1.3.2: bijective=>isomorphism without the extended-inclusion typing); docs/LEARNINGS.md 2026-08-01; re-validation pending) per DESIGN-CONSUMER-REPAIR.md + AUDIT-CONSUMER-REPAIR.md (F-corrections applied verbatim); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, fifth ratification)
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated, 12 validated + 3 archived all clean, runs 2-3 under scoped cap 14->17 with def-extcb-datum provisioned, tier routine, 2026-08-01; oracle PASS). Contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M25 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M25. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
10 / 3 / 14. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1378-1412,1430-1441
