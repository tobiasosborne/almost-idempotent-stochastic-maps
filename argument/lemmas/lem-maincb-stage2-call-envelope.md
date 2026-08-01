---
id: lem-maincb-stage2-call-envelope
kind: lemma
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_s2^0,e_s2^0 witnesses of lem-maincb-stage2-extcb-datum, there is a universal K_2^0 >= 1 with every Stage-2 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K2 >= max{K_2^0,1,W.L,W.c0_cb*W.L}, and W.e_s2 <= e_s2^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has nonempty U contained in one equivalence class, j notin U in that same class, and R=U union {j}, 0 <= epsilon <= W.e_s2/W.K2, and a supplied current reset isomorphism v_U:M_{|U|}->A_U has recorded ambient field epsilon_U <= W.L*epsilon and satisfies d_U <= W.c0_cb*epsilon_U and ||v_U(I_{M_{|U|}})-u_{A_U}|| <= W.c0_cb*epsilon_U, then lem-maincb-direct-corner-envelope certifies A_R with the Stage-2 raw-call target ambient record epsilon_R := W.L*epsilon, and t_2=W.K2*epsilon dominates epsilon_U,d_U,epsilon_R, the reset unit error, and every other datum error, so lem-maincb-stage2-extcb-datum furnishes the explicit Stage-2 EXT raw-call datum with total defect at most C_s2^0*t_2.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-maincb-witness-ledger; def-extcb-datum; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-error-improvement; lem-maincb-direct-corner-envelope; lem-maincb-stage2-extcb-datum; lem-maincb-extended-inclusion-monotone
status: proved
af: validated
workspace: proofs/lem-maincb-stage2-call-envelope
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M19-S2 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1363-1412,1428-1441; recorded-field ENV repair per DESIGN-RECFIELD-REPAIR.md sect-3 (hostile-audited AUDIT-RECFIELD-REPAIR.md DESIGN-CONFIRMED zero corrections; user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, second ratification)); DEMOTED 2026-08-01 (latent unregistered-premise gap, AUDIT-CONSUMER-REPAIR.md F5 (node 1.4: unimported monotonicity); docs/LEARNINGS.md 2026-08-01; re-validation pending) per DESIGN-CONSUMER-REPAIR.md + AUDIT-CONSUMER-REPAIR.md (F-corrections applied verbatim); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, fifth ratification)
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated 12/12 nodes clean, ENV-repaired re-seed + resumes under scoped cap amendment 11->14, tier routine, 2026-08-01; oracle PASS; run 1 of the pre-ENV contract was REFUTED by a validated M_2 countermodel — preserved in git history as the red test). Contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M19-S2 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M19-S2. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
7 / 3 / 11. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1363-1412,1428-1441
