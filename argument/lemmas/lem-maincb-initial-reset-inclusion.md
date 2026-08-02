---
id: lem-maincb-initial-reset-inclusion
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits an extended W.c0_cb*epsilon-inclusion v:C->A satisfying ||v(I_C)-I_A|| <= W.c0_cb*epsilon.
defs: def-maincb-reset-state; def-maincb-raw-call; def-maincb-witness-ledger; def-operator-space; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-initial-raw-inclusion; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger; lem-maincb-reset-constant-ledger; lem-maincb-witness-arithmetic; lem-maincb-reset-output-typing
status: stated
af: seeded
workspace: proofs/lem-maincb-initial-reset-inclusion
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M21 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:430-455,1194-1222,1317-1319,1417; deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule)
owner: A
---
**Status.** `stated` — contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M21 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M21. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Elevation guidance (BINDING, 2026-08-02; session-39 worked patterns that
cured the M19-S3/M25 re-validations).** (i) Use the typed-reset provider
lem-maincb-reset-output-typing ALONE for every reset step (its conclusion
subsumes lem-maincb-reset-invariant-preservation's; dual-provider citation
for one step invites the distinct-witness challenge). A consumer of an
existential provider must fix ONE witness explicitly and thread that SAME
witness through all later uses (the same-map law). (ii) FIRST child = one
constant-choice node fixing all universal constants nonnegatively and
absorbing every scalar prerequisite into the chosen universal — never
assume an unregistered scalar inequality (e.g. c0 >= 1). (iii) NO node may
cite a PENDING SIBLING — shared scalar facts live in the constant-choice
node or its children. (iv) Any bijective=>isomorphism inference cites the
extended-inclusion typing explicitly at the point of use.

**Provenance loci.** approximate_algebras.tex:430-455,1194-1222,1317-1319,1417
