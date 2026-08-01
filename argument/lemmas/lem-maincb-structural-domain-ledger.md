---
id: lem-maincb-structural-domain-ledger
kind: lemma
contract: After first fixing a particular universal e_sim>0 witness furnished by lem-maincb-corner-equivalence and a particular universal e_full>0 witness furnished by lem-maincb-full-corner-identification, fix one def-maincb-witness-ledger datum W whose existence is furnished by lem-maincb-reset-constant-ledger instantiated with those same e_sim,e_full witnesses; then 0 <= epsilon <= W.epsilon_MAIN implies epsilon <= W.e_env, epsilon <= W.e1/W.K1, epsilon <= W.e_s2/W.K2, and epsilon <= W.e_cross/W.K3, while the global scalar scale epsilon, atomic scalar scale W.K_call*epsilon, and Stage-1, Stage-2, and Stage-3 scales W.K1*epsilon,W.K2*epsilon,W.K3*epsilon are all at most W.K_call*epsilon <= W.r_reset,e_sim,e_full; every atomic corner defect is at most W.L*epsilon <= W.K_call*epsilon and W.c0_cb*W.K_call*epsilon <= 1/2.
defs: def-maincb-reset-state; def-maincb-raw-call; def-maincb-partition-state; def-maincb-witness-ledger
deps: lem-maincb-error-improvement; lem-maincb-direct-corner-envelope; lem-maincb-full-corner-identification; lem-maincb-corner-equivalence; lem-maincb-reset-constant-ledger; lem-maincb-stage1-call-envelope; lem-maincb-stage2-call-envelope; lem-maincb-stage3-call-envelope
status: stated
af: seeded
workspace: proofs/lem-maincb-structural-domain-ledger
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M20 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source finite max/min arithmetic
owner: A
---
**Status.** `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M20 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M20. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
7 / 3 / 11. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** finite max/min arithmetic
