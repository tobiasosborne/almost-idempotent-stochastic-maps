---
id: lem-maincb-improvement-iteration
kind: lemma
contract: There are universal e_it > 0, K_disp < infinity, and K_floor < infinity such that, if B is a finite-dimensional C*-algebra, A is an extended epsilon-C*-algebra, and v:B->A is an extended d-inclusion with d+epsilon <= e_it, then one dagger-preserving v_tilde, with v_tilde_n = I_n tensor v_tilde, satisfies sup_n ||v_tilde_n - v_n|| <= K_disp*d and has extended defect at most K_floor*epsilon; for epsilon > 0 it is reached after finitely many correction steps, and for epsilon = 0 it is their operator-norm limit.
defs: def-operator-space; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-fd-cstar-diagonal
deps: lem-maincb-improvement-one-step
status: proved
af: validated
workspace: proofs/lem-maincb-improvement-iteration
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M02 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1313,1508-1535
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 7-node tree, root
`validated`, taint clean 7/7, FIRST-PASS zero challenges
(`proofs/lem-maincb-improvement-iteration/export.md`; oracle pass; tier
routine; parallel-af worktree run af-m02). Route: iterate the M01
one-step improvement, geometric-series displacement control K_disp*d,
K_floor*epsilon floor after finitely many steps for epsilon > 0,
operator-norm limit at epsilon = 0. MAIN campaign row M02.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M02. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1313,1508-1535
