---
id: lem-maincb-stage3-raw-merge
kind: lemma
contract: There are universal D_3 < infinity and e_3 > 0, with e_3 <= a_merge/(C_cross+1), such that every amplified four-corner datum in A_R with common defect rho <= C_cross*t and target ambient defect epsilon_{A_R} <= t <= e_3 satisfies rho + epsilon_{A_R} <= a_merge and yields an extended D_3*t-isomorphism B_U oplus B_V -> A_R.
defs: def-maincb-raw-call; def-four-corner-merging-datum; def-operator-space; def-extended-delta-inclusion
deps: lem-maincb-cross-class-merging-datum; lem-extcb-four-corner-merge
status: stated
af: seeded
workspace: proofs/lem-maincb-stage3-raw-merge
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M17 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1325-1359,1443
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-4.4 row M17 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M17. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
3 / 2 / 7. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M17. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1325-1359,1443; argument/lemmas/lem-extcb-four-corner-merge.md:4,18-25
