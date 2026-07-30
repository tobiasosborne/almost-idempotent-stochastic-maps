---
id: lem-maincb-reset-constant-ledger
kind: lemma
contract: With D_* = max{1,D_0,D_1,D_2,D_3} and r_reset := min{e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb/D_*} > 0, every explicit scalar, Stage-1, Stage-2, or Stage-3 raw call with its own base scale 0 <= t <= r_reset and target ambient defect 0 <= epsilon_target <= t - where a Stage-2 call may have post-helper datum scale C_s2*t as licensed by lem-maincb-stage2-raw-extension - has d_raw <= D_* * t <= delta_max^cb and epsilon_target <= epsilon_max^cb, hence satisfies the exact hypotheses of lem-maincb-error-improvement; all witnesses are positive, finite, universal, and independent of dimension, amplification, block data, and stage index.
defs: def-maincb-raw-call; def-maincb-reset-state
deps: lem-maincb-error-improvement; lem-maincb-initial-raw-inclusion; lem-maincb-stage1-raw-refinement; lem-maincb-stage2-raw-extension; lem-maincb-stage3-raw-merge
status: stated
af: seeded
workspace: proofs/lem-maincb-reset-constant-ledger
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M18 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source finite-minimum arithmetic
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-4.4 row M18 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M18. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
4 / 2 / 8. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M18. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** finite-minimum arithmetic; approximate_algebras.tex:1317-1319,1414-1444,1557
