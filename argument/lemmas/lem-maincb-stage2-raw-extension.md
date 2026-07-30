---
id: lem-maincb-stage2-raw-extension
kind: lemma
contract: There are universal D_2 < infinity and e_2 > 0, chosen with e_2 <= e_s2 and C_s2*e_2 <= e_ext, such that every explicit Stage-2 raw-call closed EXT-CB datum in A_R whose total post-helper defect is at most C_s2*t, for base scale 0 <= t <= e_2, admits an extended D_2*t-isomorphism M_{r+1}->A_R.
defs: def-maincb-raw-call; def-extcb-datum; def-operator-space; def-extended-delta-inclusion
deps: lem-maincb-stage2-extcb-datum; conj-extcb
status: stated
af: seeded
workspace: proofs/lem-maincb-stage2-raw-extension
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M16 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1378-1412,1435-1441
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-4.4 row M16 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M16. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
3 / 2 / 7. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.4 row M16. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1378-1412,1435-1441; argument/lemmas/conj-extcb.md:4
