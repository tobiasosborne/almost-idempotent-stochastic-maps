---
id: lem-maincb-reset-invariant-preservation
kind: lemma
contract: For any explicit global-scalar, compressed-corner-scalar, Stage-1, Stage-2, or Stage-3 raw call into a recorded current corner A_R, assume A_R is an extended epsilon_R-C*-algebra and the literal output map u_R:B_R->A_R is an extended d_raw-inclusion (respectively isomorphism) from the raw call's named finite-dimensional C*-algebra source B_R. If d_raw <= delta_max^cb and epsilon_R <= epsilon_max^cb, then lem-maincb-error-improvement produces an error-improved map v_R:B_R->A_R satisfying d_R <= c_0^cb*epsilon_R, preserves bijectivity when u_R is bijective, and leaves the source, target corner R, and fixed amplification form unchanged.
defs: def-maincb-reset-state; def-maincb-raw-call; def-maincb-partition-state; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-error-improvement; lem-maincb-reset-constant-ledger
status: stated
af: seeded
workspace: proofs/lem-maincb-reset-invariant-preservation
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M19-R (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1317-1319,1435-1443,1557
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-6 row M19-R (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M19-R. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
3 / 2 / 7. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M19-R. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1317-1319,1435-1443,1557; argument/lemmas/lem-maincb-error-improvement.md:4
