---
id: lem-maincb-binary-block-merge
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images and has disjoint nonempty unions U,V sharing no class, and current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then there is a current reset isomorphism v_{U union V}:B_U oplus B_V->A_{U union V} whose recorded ambient field epsilon_{U union V} is selected so that A_{U union V} is an extended epsilon_{U union V}-C*-algebra and epsilon_{U union V} <= W.L*epsilon, and which satisfies d_{U union V} <= W.c0_cb*epsilon_{U union V} and ||v_{U union V}(I_{B_U oplus B_V})-u_{A_{U union V}}|| <= W.c0_cb*epsilon_{U union V}.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-maincb-witness-ledger; def-four-corner-merging-datum; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-stage3-raw-merge; lem-maincb-stage3-call-envelope; lem-maincb-cross-datum-bijectivity; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger; lem-maincb-reset-constant-ledger; lem-maincb-extended-inclusion-monotone; lem-maincb-reset-output-typing
status: proved
af: validated
workspace: proofs/lem-maincb-binary-block-merge
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M26 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1194-1222,1325-1359,1443; recorded-field ENV repair per DESIGN-RECFIELD-REPAIR.md sect-3 (hostile-audited AUDIT-RECFIELD-REPAIR.md DESIGN-CONFIRMED zero corrections; user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, second ratification)); M26 deps amendment (bridge import) per DESIGN-M17-TYPING-v3.md item 3, user-ratified 2026-08-01; deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule); one-dimensional-images hypothesis RESTORED per DESIGN-CONSUMER-REPAIR.md + AUDIT-CONSUMER-REPAIR.md (F-corrections applied verbatim); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, fifth ratification); MIS-LANDING FIX 2026-08-02 (aism-wazy: the 894c983f landing pasted the typed-reset provider's contract here by error; this restores the user-ratified DESIGN-CONSUMER-REPAIR.md contract block 1 BYTE-VERBATIM — a mechanical fix, no new content); af-VALIDATED 2026-08-02 (first-pass 11/11 clean against the corrected contract; oracle af-lem-maincb-binary-block-merge PASS)
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated, 11/11 nodes
clean, taint clean, FIRST-PASS elevation of the correctly-landed ratified
contract (aism-wazy fix c8eb827b) under the binding session-39 guidance,
tier routine, 2026-08-02; oracle PASS). Previously `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M26 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M26.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
9 / 3 / 13. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Elevation guidance (BINDING, 2026-08-02; session-39 worked patterns that
cured the M19-S3/M25 re-validations).** (i) Use the typed-reset provider
conclusions with ONE explicitly fixed witness threaded through all later
uses (the same-map law); never cite two providers for one step. (ii) FIRST
child = one constant-choice node fixing all universal constants
nonnegatively and absorbing every scalar prerequisite into the chosen
universal — never assume an unregistered scalar inequality. (iii) NO node
may cite a PENDING SIBLING — shared scalar facts live in the
constant-choice node or its children. (iv) Any bijective=>isomorphism
inference cites the extended-inclusion typing explicitly at the point of
use — the one-dimensional-atomic-images hypothesis is now EXPLICIT in the
contract (the ratified F-A restore); use it, never re-derive it.

**Provenance loci.** approximate_algebras.tex:1194-1222,1325-1359,1443
