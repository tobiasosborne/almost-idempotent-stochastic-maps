---
id: lem-maincb-initial-raw-inclusion
kind: lemma
contract: There are universal D_0 < infinity and e_0 > 0 such that, in every finite-dimensional extended epsilon-C*-algebra with epsilon <= t <= e_0, the scalar map lambda |-> lambda*I_A is an extended D_0*t-inclusion; if dim A = 1, it is bijective.
defs: def-operator-space; def-maincb-raw-call; def-extended-delta-inclusion; def-extended-epsilon-cstar-algebra
status: proved
af: validated
workspace: proofs/lem-maincb-initial-raw-inclusion
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M14 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:430-455,1467-1475
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 7 live nodes (16 total,
9 archived from the in-run repair), root `validated`, taint clean
(`proofs/lem-maincb-initial-raw-inclusion/export.md`; oracle pass; tier
routine; parallel-af worktree run af-m14 — the FIRST result validated
under the user-ratified worktree-per-run architecture). Three
challenges raised and repaired in-run; the decisive one (no allowed
provider for ||I_A|| >= 1-epsilon) exposed the systematic missing
def-extended-epsilon-cstar-algebra vocabulary import, fixed across all
26 affected MAIN shards (commit 07784801). MAIN campaign row M14.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
4 / 2 / 8. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M14. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:430-455,1467-1475
