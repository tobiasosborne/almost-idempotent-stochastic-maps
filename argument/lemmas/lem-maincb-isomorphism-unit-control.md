---
id: lem-maincb-isomorphism-unit-control
kind: lemma
contract: There are universal C_iso_unit < infinity and e_iso_unit > 0 such that if B is a finite-dimensional C*-algebra, A is a finite-dimensional extended epsilon-C*-algebra, and v:B->A is an extended delta-isomorphism with 0 <= delta+epsilon <= e_iso_unit, then ||v(I_B)-I_A|| <= C_iso_unit*(delta+epsilon); the witnesses are independent of dimension, amplification, block data, and the particular source and target.
defs: def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps:
status: stated
af: seeded
workspace: proofs/lem-maincb-isomorphism-unit-control
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 (new row, landed verbatim); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:443-455,1477-1484; modular export of the existing delta-homomorphism unit clause, `C_iso_unit=1` (AUDIT F1)
owner: A
---
**Status.** `stated` — contract transcribed verbatim from the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 (aism-jl4g repair package, hostile-audit
chain AUDIT-MAINCB-REPAIR.md; user-ratified 2026-08-01 in-session). NOT
proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:443-455,1477-1484; modular export of the existing delta-homomorphism unit clause, `C_iso_unit=1` (AUDIT F1)
