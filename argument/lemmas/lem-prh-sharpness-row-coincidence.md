---
id: lem-prh-sharpness-row-coincidence
kind: lemma
contract: Row coincidence for stochastic idempotents: for every integer n >= 1, every n-by-n row-stochastic idempotent matrix F=(f_ab) over R, and all i,j in {1,...,n}, if f_ii>0 and f_ij>0 then row_i(F)=row_j(F).
defs: def-stochastic
deps:
status: stated
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md sect-7 (especially sect-7.1); docs/plans/2026-08-08-EXHUME-SHARPNESS/DESIGN-EXHUME-SHARPNESS-V2.md sects-2.1,4.1 (W139 package); docs/plans/2026-08-08-EXHUME-SHARPNESS/BRIEF-PRHSHARP-FACTOR.md Situation (BALLOON run 1 at 27 live nodes and clean-reseed BALLOON run 2 at 28 live nodes, 2026-08-08); docs/plans/2026-08-08-EXHUME-SHARPNESS/TREE-PRHSHARP-ABORTED.md (run-2 tree, 2026-08-08)
owner: A
workspace: proofs/lem-prh-sharpness-row-coincidence
---

**Status.** `stated` design transcription only.  This shard promotes nothing
and may not be seeded before fresh hostile audit and user ratification.

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
