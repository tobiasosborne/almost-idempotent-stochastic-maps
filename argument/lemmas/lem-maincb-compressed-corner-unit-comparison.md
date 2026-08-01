---
id: lem-maincb-compressed-corner-unit-comparison
kind: lemma
contract: There are universal C_corner_unit < infinity and e_corner_unit > 0 such that both of the following hold: if P is a t-projection in a finite-dimensional extended t-C*-algebra A with 0 <= t <= e_corner_unit, then the compressed-corner unit u_{S_P}=Co_P(P) satisfies ||I_n tensor u_{S_P}-I_n tensor P|| <= C_corner_unit*t for every n >= 1; and, under the hypotheses of lem-maincb-outer-compression-transfer with 0 <= t <= e_corner_unit, if ||v(I_B)-u_{S_P}|| <= t then its explicit outer-compressed map T=Co^{A_R}_{P^R} o Co^A_R o v satisfies ||T_n(I_n tensor I_B)-I_n tensor P^R|| <= C_corner_unit*t for every n >= 1.
defs: def-compressed-corner; def-delta-projection; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-operator-space
deps: lem-maincb-outer-compression-transfer; lem-compcb-amplified-compression; lem-compcb-amplified-compression-identities; lem-compcb-compressed-unit-action; lem-compcb-compressed-unit-norm
status: proved
af: validated
workspace: proofs/lem-maincb-compressed-corner-unit-comparison
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 (new row, landed verbatim); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1054-1082,1435-1441,1542-1544
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated 13/13 nodes clean, run 1 + resumes under the flagged scoped cap amendment 11->15, tier routine, 2026-08-01; oracle PASS). Contract transcribed verbatim from the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 (aism-jl4g repair package, hostile-audit
chain AUDIT-MAINCB-REPAIR.md; user-ratified 2026-08-01 in-session). NOT
proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
7 / 3 / 11. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1054-1082,1435-1441,1542-1544
