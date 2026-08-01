---
id: lem-maincb-extended-inclusion-monotone
kind: lemma
contract: If B is a finite-dimensional C*-algebra, A is a finite-dimensional extended epsilon-C*-algebra, v:B->A is linear, and 0 <= delta <= delta', then if v is an extended delta-inclusion it is an extended delta'-inclusion, and if v is an extended delta-isomorphism it is an extended delta'-isomorphism and in particular an extended delta'-inclusion.
defs: def-extended-delta-inclusion; def-extended-epsilon-cstar-algebra; def-operator-space
deps:
status: proved
af: validated
workspace: proofs/lem-maincb-extended-inclusion-monotone
provenance: DESIGN-M18-MONOTONE.md with AUDIT-M18-MONOTONE.md F1 consumer-normal typing (auditor-verbatim contract); monotonicity confirmed clause-by-clause vs the locked def (F5, no delta ceiling); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, fourth ratification); source approximate_algebras.tex:443-456,1477-1484
owner: A
---

**Status.** `proved` — af-VALIDATED in-repo (root validated 3/3 nodes clean, run 1 + GT-provisioned resume, tier routine, 2026-08-01; oracle PASS). The defect-monotonicity micro-row factored out of
M18 run 1 (L4 balloon; the tree re-derived this fact once per stage map).
Contract is the hostile audit's corrected verbatim form. NOT proved
in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
3 / 2 / 6. Every clause of def-extended-delta-inclusion (the
delta-homomorphism clauses incl. the unit clause, and both two-sided norm
bounds) is monotone in delta at every amplification; bijectivity is
delta-independent.

**Provenance loci.** approximate_algebras.tex:443-456,1477-1484
