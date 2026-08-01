---
id: lem-maincb-binary-block-merge
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon and has disjoint nonempty unions U,V sharing no class, and current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then there is a current reset isomorphism v_{U union V}:B_U oplus B_V->A_{U union V} whose recorded ambient field epsilon_{U union V} is selected so that A_{U union V} is an extended epsilon_{U union V}-C*-algebra and epsilon_{U union V} <= W.L*epsilon, and which satisfies d_{U union V} <= W.c0_cb*epsilon_{U union V} and ||v_{U union V}(I_{B_U oplus B_V})-u_{A_{U union V}}|| <= W.c0_cb*epsilon_{U union V}.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-maincb-witness-ledger; def-four-corner-merging-datum; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-stage3-raw-merge; lem-maincb-stage3-call-envelope; lem-maincb-cross-datum-bijectivity; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger
status: stated
af: seeded
workspace: proofs/lem-maincb-binary-block-merge
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M26 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1194-1222,1325-1359,1443; recorded-field ENV repair per DESIGN-RECFIELD-REPAIR.md sect-3 (hostile-audited AUDIT-RECFIELD-REPAIR.md DESIGN-CONFIRMED zero corrections; user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, second ratification)); M26 deps amendment (bridge import) per DESIGN-M17-TYPING-v3.md item 3, user-ratified 2026-08-01
owner: A
---
**Status.** `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M26 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M26. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
9 / 3 / 13. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1194-1222,1325-1359,1443
