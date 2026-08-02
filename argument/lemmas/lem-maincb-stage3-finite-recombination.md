---
id: lem-maincb-stage3-finite-recombination
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images and has classes C_1,...,C_q, and each initial current reset isomorphism v_{C_a}:B_{C_a}->A_{C_a} has recorded ambient field epsilon_{C_a} <= W.L*epsilon and satisfies d_{C_a} <= W.c0_cb*epsilon_{C_a} and ||v_{C_a}(I_{B_{C_a}})-u_{A_{C_a}}|| <= W.c0_cb*epsilon_{C_a}, then there is a current reset isomorphism v:oplus_a B_{C_a}->A_{union_a C_a} whose recorded ambient field epsilon_{union_a C_a} satisfies epsilon_{union_a C_a} <= W.L*epsilon, d_{union_a C_a} <= W.c0_cb*epsilon_{union_a C_a}, and ||v(I_{oplus_a B_{C_a}})-u_{A_{union_a C_a}}|| <= W.c0_cb*epsilon_{union_a C_a}.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-witness-ledger; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-structural-domain-ledger; lem-maincb-binary-block-merge; lem-maincb-reset-constant-ledger
status: proved
af: validated
workspace: proofs/lem-maincb-stage3-finite-recombination
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M27 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1443; recorded-field ENV repair per DESIGN-RECFIELD-REPAIR.md sect-3 (hostile-audited AUDIT-RECFIELD-REPAIR.md DESIGN-CONFIRMED zero corrections; user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, second ratification)); deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule); one-dimensional-images hypothesis RESTORED per DESIGN-CONSUMER-REPAIR.md + AUDIT-CONSUMER-REPAIR.md (F-corrections applied verbatim); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, fifth ratification); af-VALIDATED 2026-08-02 (first-pass 7/7 clean; oracle af-lem-maincb-stage3-finite-recombination PASS)
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated, 7/7 nodes
clean, taint clean, FIRST-PASS elevation under the binding session-39
guidance + explicit-induction rule, tier routine, 2026-08-02; oracle
PASS). Previously `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M27 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M27.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
7 / 2 / 11. Per-row skeleton and audit delta:
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
constant-choice node or its children. (iv) Explicit induction dependencies
for the finite recombination: every inductive step node names the exact
prior node(s) supplying its hypothesis — no floating 'inductively
constructed state' nodes; the binary steps invoke lem-maincb-binary-block-
merge with its now-EXPLICIT one-dimensional hypothesis forwarded from the
root, per the ratified interface-match note (M26->M27 exact match).

**Provenance loci.** approximate_algebras.tex:1443
