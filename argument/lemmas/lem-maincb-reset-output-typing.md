---
id: lem-maincb-reset-output-typing
kind: lemma
contract: After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R that satisfies d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, is an extended W.c0_cb*epsilon_R-inclusion, is an extended W.c0_cb*epsilon_R-isomorphism when u_R is bijective, and leaves the source, target corner, and amplification form unchanged.
defs: def-maincb-reset-state; def-maincb-raw-call; def-maincb-partition-state; def-maincb-witness-ledger; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-improvement-iteration; lem-maincb-error-improvement; lem-maincb-extended-inclusion-monotone
status: proved
af: validated
workspace: proofs/lem-maincb-reset-output-typing
provenance: AUDIT-CONSUMER-REPAIR.md F2 (auditor-verbatim contract = the design's sound strengthened-M19-R form as a standalone typed-reset row; M19-R/M18 byte-unchanged); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, fifth ratification); source approximate_algebras.tex:1192-1222,1256-1319,1435-1443; reuse proofs/lem-stage1-fresh-two-point-inclusion/externals/3404276169020d3b.json (GT-kitaev-prop-delta-hominc)
owner: A
---

**Status.** `proved` — af-VALIDATED in-repo (root validated 8/8 nodes clean, run 1 + verify resume, tier routine, 2026-08-01; oracle PASS). The typed reset provider (AUDIT-CONSUMER-REPAIR F2):
exports the SAME error-improved map as an extended W.c0_cb*epsilon_R-inclusion
(isomorphism when u_R is bijective). NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
8 / 3 / 12. Proof: construct one literal M02 iterate; type it via M02's
export + lem-maincb-extended-inclusion-monotone; derive the unit estimate via
the GT near-unit clause and conditional bijectivity for THAT same map; never
substitute M03's separate existential witness (the audit's same-map law).

**Provenance loci.** approximate_algebras.tex:1192-1222,1256-1319,1435-1443
