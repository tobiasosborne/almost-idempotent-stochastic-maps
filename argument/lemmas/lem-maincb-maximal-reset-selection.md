---
id: lem-maincb-maximal-reset-selection
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN, then the nonempty set of m admitting an extended W.c0_cb*epsilon-inclusion w:C^m->A with ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon has a maximum because the lower norm is positive and m <= dim_C A.
defs: def-maincb-reset-state; def-maincb-witness-ledger; def-projection-basis; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-structural-domain-ledger; lem-maincb-initial-reset-inclusion; lem-maincb-reset-constant-ledger
status: proved
af: validated
workspace: proofs/lem-maincb-maximal-reset-selection
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M22 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1417; deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule); af-VALIDATED 2026-08-02 (first-pass 9/9 clean; oracle af-lem-maincb-maximal-reset-selection PASS)
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated, 9/9 nodes
clean, taint clean, FIRST-PASS elevation under the binding session-39
guidance, tier routine, 2026-08-02; oracle PASS). Contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M22 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M22.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9. Per-row skeleton and audit delta:
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
use.

**Provenance loci.** approximate_algebras.tex:1417
