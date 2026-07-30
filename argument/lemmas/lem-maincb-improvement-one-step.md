---
id: lem-maincb-improvement-one-step
kind: lemma
contract: There are universal K_step >= 1 and e_step > 0 such that, if B is a finite-dimensional C*-algebra, A an extended epsilon-C*-algebra, and v:B->A an extended d-inclusion with d+epsilon <= e_step, then one dagger-preserving level-one map v^+, with v_n^+ = I_n tensor v^+, satisfies sup_n ||v_n^+ - v_n|| <= K_step*d and is an extended d^+-inclusion for d^+ <= K_step*(d^2+epsilon).
defs: def-operator-space; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-fd-cstar-diagonal
status: proved
af: validated
workspace: proofs/lem-maincb-improvement-one-step
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M01 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1239-1311,1508-1535
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 12-node tree, root
`validated`, taint clean 12/12
(`proofs/lem-maincb-improvement-one-step/export.md`; oracle pass; tier
routine; parallel-af worktree run af-m01). Six challenges raised and
repaired across two runs; the two provisioning-class ones were
discharged by registering the base def-epsilon-cstar-algebra and the
byte-matched external GT-kitaev-standard-diagonal
(approximate_algebras.tex:1245-1254, quote-at-locus PASS: the standard
diagonal D with ||D||=1, unique, componentwise on direct sums) — the
exact provider for the structure-theorem invocation the verifier
challenged. MAIN campaign row M01.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
8 / 3 / 12. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M01. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1239-1311,1508-1535
