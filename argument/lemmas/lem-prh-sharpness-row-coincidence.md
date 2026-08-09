---
id: lem-prh-sharpness-row-coincidence
kind: lemma
contract: Row coincidence for stochastic idempotents: for every integer n >= 1, every n-by-n row-stochastic idempotent matrix F=(f_ab) over R, and all i,j in {1,...,n}, if f_ii>0 and f_ij>0 then row_i(F)=row_j(F).
defs: def-stochastic
deps:
status: proved
af: validated
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md sect-7 (especially sect-7.1); docs/plans/2026-08-08-EXHUME-SHARPNESS/DESIGN-EXHUME-SHARPNESS-V2.md sects-2.1,4.1 (W139 package); docs/plans/2026-08-08-EXHUME-SHARPNESS/BRIEF-PRHSHARP-FACTOR.md Situation (BALLOON run 1 at 27 live nodes and clean-reseed BALLOON run 2 at 28 live nodes, 2026-08-08); docs/plans/2026-08-08-EXHUME-SHARPNESS/TREE-PRHSHARP-ABORTED.md (run-2 tree, 2026-08-08); af elevation run 1 VALIDATED 2026-08-09 (fresh xhigh prover, separate fresh xhigh verifiers, 19/19 nodes validated, taint clean, cap 22 respected, 5+1 rounds; two in-run cross-sibling dependency challenges repaired in-tree by explicit dependency-backed child nodes; export proofs/lem-prh-sharpness-row-coincidence/export.md; fr verify pass via oracle af-lem-prh-sharpness-row-coincidence)
owner: A
workspace: proofs/lem-prh-sharpness-row-coincidence
---

**Status.** `proved` / `af: validated` (2026-08-09, run 1). Mechanical reflection
of the codex ledger: root validated with 19/19 nodes clean under hard cap 22 by a
fresh xhigh prover and separate fresh xhigh verifiers; externally banked via
`fr verify` on the export path.

**Factoring role.** This row contains the entire general-idempotent branch.
For the stationary probability `pi=row_i(F)`, its positive support is closed.
A finite source-component argument rules out edges between distinct support
components, and the edges from `i` to every support vertex force strong
connectivity.  The minimum-ratio argument then proves uniqueness of the
stationary probability on that support and hence equality of rows `i` and `j`.
No finite Markov-chain classification theorem is imported.

**Designed af budget.** Six nodes; honest live expectation 9--18 nodes under
the observed 1.5--3x expansion; at most 5 rounds; hard cap 22.  The 3x endpoint
is 18, strictly below 22.  A cap hit is a new stop-and-classify event, not
permission to enlarge the cap.
