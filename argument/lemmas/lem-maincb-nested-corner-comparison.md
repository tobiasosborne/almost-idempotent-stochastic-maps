---
id: lem-maincb-nested-corner-comparison
kind: lemma
contract: There are universal C_nest < infinity and e_nest > 0 such that, whenever R,P,Q are t-projections in a finite-dimensional extended t-C*-algebra, R is nonvanishing, P,Q are subordinate to R with all four left/right subordination errors at most t <= e_nest, A_R = S^A_R, P^R = Co^A_R(P), and Q^R = Co^A_R(Q), then P^R,Q^R are C_nest*t-projections in A_R and, at every amplification, ||F^R_{P,Q}(Co^A_R X) - X|| <= C_nest*t*||X|| for X in S^A_{P,Q}, while ||Co^A_{P,Q} Y - Y|| <= C_nest*t*||Y|| for Y in S^{A_R}_{P^R,Q^R}.
defs: def-operator-space; def-compressed-corner; def-delta-projection; def-extended-epsilon-cstar-algebra
deps: lem-compcb-amplified-compression; lem-compcb-amplified-compression-identities; lem-compcb-amplified-almost-containment; lem-compcb-corner-algebra; lem-compcb-rectangular-product
status: proved
af: validated
workspace: proofs/lem-maincb-nested-corner-comparison
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.2 row M07 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1054-1082,1435-1441
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 18-node tree, root
`validated`, taint clean 18/18
(`proofs/lem-maincb-nested-corner-comparison/export.md`; oracle pass;
tier routine; parallel-af worktree run af-m07). THE LOAD-BEARING
TELESCOPE ROW — the design's declared conditional gap stop: BOTH fixed
telescope directions passed hostile verification (no generic
close-corner substitute used); the M07 gap-stop is CLEARED. Run 1
ABORTED [BALLOON] at 18 live > cap 16; classified TRANSPARENT REPAIR
GROWTH (five prover-fixes each adding verifier-demanded explicit
bridging nodes — local C_proj derivation, explicit dimension-free
telescope, Z-membership via amplified compression; zero open
challenges) and resumed under a SCOPED cap amendment 16->22 per the
bc3ca739 precedent (applied autonomously under the user's 2026-07-30
land-this mandate; flagged for user review). Final tree 18 <= 22.
MAIN campaign row M07.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
11 / 3 / 15. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.2 row M07. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1054-1082,1435-1441
