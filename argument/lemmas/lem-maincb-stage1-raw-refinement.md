---
id: lem-maincb-stage1-raw-refinement
kind: lemma
contract: There are universal D_1 < infinity and e_1 > 0 such that, if an explicit Stage-1 raw-call datum supplies complementary target t-projections, an old extended t-inclusion C^{m-1}->S_{P_old} when m > 1, a fresh extended t-inclusion C^2->S_{P_fresh}, fixed amplification families, and every projection, complementarity, map, and target-ambient defect is at most t <= e_1, then their sum map is an extended D_1*t-inclusion C^{m+1}->A; when m = 1, the old side is absent and the conclusion is the supplied fresh inclusion.
defs: def-maincb-reset-state; def-maincb-raw-call; def-operator-space; def-delta-projection; def-extended-delta-inclusion
deps: lem-maincb-direct-sum-inclusion-merge; lem-compcb-single-compression-transfer
status: proved
af: validated
workspace: proofs/lem-maincb-stage1-raw-refinement
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M15 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1352-1359,1419-1426
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 5-node tree, root
`validated`, taint clean 5/5
(`proofs/lem-maincb-stage1-raw-refinement/export.md`; oracle pass; tier
routine; parallel-af worktree run af-m15). One codomain-transfer
challenge repaired in-run. Route: M05 two-diagonal merge on the
old/fresh pair; the m = 1 degenerate case is the supplied fresh
inclusion. MAIN campaign row M15.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M15. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1352-1359,1419-1426
