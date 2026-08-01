---
id: lem-maincb-reset-invariant-preservation
kind: lemma
contract: After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R satisfying d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, preserving bijectivity when u_R is bijective and leaving the source, target corner, and amplification form unchanged.
defs: def-maincb-reset-state; def-maincb-raw-call; def-maincb-partition-state; def-maincb-witness-ledger; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-improvement-iteration; lem-maincb-error-improvement
status: proved
af: validated
workspace: proofs/lem-maincb-reset-invariant-preservation
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M19-R (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1192-1222,1256-1319,1435-1443,1557; reuse `proofs/lem-stage1-fresh-two-point-inclusion/externals/3404276169020d3b.json`
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated 12/12 nodes clean, run 1, tier routine, 2026-08-01; oracle af-lem-maincb-reset-invariant-preservation PASS). Contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M19-R (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M19-R. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
8 / 3 / 12. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1192-1222,1256-1319,1435-1443,1557; reuse `proofs/lem-stage1-fresh-two-point-inclusion/externals/3404276169020d3b.json`

**GT external.** The near-unit clause is backed by the byte-matched
`prop_delta_hominc` external — reuse the registration at
`proofs/lem-stage1-fresh-two-point-inclusion/externals/3404276169020d3b.json`
(approximate_algebras.tex:1194-1196) verbatim at elevation time.
