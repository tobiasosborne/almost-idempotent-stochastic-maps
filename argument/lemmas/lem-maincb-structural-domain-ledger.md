---
id: lem-maincb-structural-domain-ledger
kind: lemma
contract: With the earlier witnesses, set K_call := max{1,L,c_0^cb,K_1,K_2,K_3} and epsilon_MAIN := min{e_env,e_call_1,e_call_2,e_call_3,r_reset/K_call,e_sim/K_call,e_full/K_call,[2*max{1,c_0^cb*K_call}]^{-1}} > 0. Then 0 <= epsilon <= epsilon_MAIN implies epsilon <= e_env, e_call_1, e_call_2, e_call_3; the global scalar call uses t_0 = epsilon, the distinct compressed-corner scalar call uses t_atom = K_call*epsilon, and each Stage-i call uses t_i = K_i*epsilon for i in {1,2,3}. All five scales are at most K_call*epsilon <= r_reset, e_sim, e_full; for every atom j lem-maincb-direct-corner-envelope gives epsilon_{{j}} <= L*epsilon <= t_atom <= r_reset; and c_0^cb*K_call*epsilon <= 1/2.
defs: def-maincb-reset-state; def-maincb-raw-call; def-maincb-partition-state
deps: lem-maincb-error-improvement; lem-maincb-direct-corner-envelope; lem-maincb-full-corner-identification; lem-maincb-corner-equivalence; lem-maincb-reset-constant-ledger; lem-maincb-stage1-call-envelope; lem-maincb-stage2-call-envelope; lem-maincb-stage3-call-envelope
status: stated
af: seeded
workspace: proofs/lem-maincb-structural-domain-ledger
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M20 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source finite-minimum arithmetic
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-6 row M20 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M20. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M20. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** finite-minimum arithmetic; AUDIT-MAIN-STRUCTURE-v3.md sect-1D, sect-6
