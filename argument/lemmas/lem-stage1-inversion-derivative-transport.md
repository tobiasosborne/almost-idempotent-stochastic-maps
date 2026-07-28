---
id: lem-stage1-inversion-derivative-transport
kind: lemma
contract: Parameterized inversion-derivative transport: there exist C_der^0, C_ch^0, C_pol^0, C_grp^0 >= 1 and kappa_der^0, kappa_ch^0, kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_der >= C_der^0, C_ch >= C_ch^0, C_pol >= C_pol^0, C_grp >= C_grp^0, 0 < kappa_der <= kappa_der^0, 0 < kappa_ch <= kappa_ch^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0, every s in {+1, -1}, and every 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, and g_{sJ}: B_{2delta}^{icalH}(0) -> B_{2delta}^{calH}(0) for the unique C^1 map such that, for every A in B_{2delta}^{icalH}(0), f_{sJ}(A + g_{sJ}(A)) = 0, where f_{sJ}(B) = (1/2)*(((J + B^dagger) bold-dot (sJ)^dagger) bold-dot (sJ bold-dot (J + B)) - J), define chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)) and the global C^1 map sigma(U) = u_delta(U^dagger); then sigma maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart and, with F_s(A) = phi_{sJ}^par(sigma(chi_s(A))), one has ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for every A in B_r^{icalH}(0).
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-explicit-group-closeness; lem-stage1-polar-retraction; lem-stage1-unitary-graph-control
status: stated
af: seeded
workspace: proofs/lem-stage1-inversion-derivative-transport
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13g, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional domain restriction, audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 728-762, 857-892, 943; parameterized chart/derivative/guard monotonicity; AUDIT-S1-POLAR-v4.md sect-1.7, sect-3.
owner: A
---

**Status.** **RETRACTED from the rigorous record 2026-07-28** (see
`docs/LEARNINGS.md` 2026-07-28 entry; bug bead `aism-e1qs`). The
2026-07-28 W95 run-2 af validation (then the 107th rigorous result;
13/13 live nodes, taint clean) was found DEFECTIVE by an independent
fresh-codex adjudication
(`docs/plans/2026-07-28-13E-BINDER-design/ADJUDICATION-T0-ALLEGATION.md`,
T2): the polar and graph identifications in export nodes 1.3 (first
half) and 1.4 are sound, but the "consequently" step of node 1.3, node
1.5.5's use of `lem-stage1-smooth-unitary-operations` as a
synchronization lemma, and decisively node 1.6's substitution of the
parent's derivative estimate (stated for the anaphoric sigma_I) into the
root's explicitly-bound F_s are underivable from the registered
externals — no typed preimage witness attaches the parent's u_I to the
explicit Pi_delta inverse (the same missing-h_X obstruction as W93; the
retraction of the parent `lem-stage1-inversion-derivative-control` on
the same day removes its authority in any case). Status mechanically
demoted proved→stated, af validated→seeded; workspace and both run
ledgers retained. Re-derivation on an explicit-binder dependency spine
is part of the 13e repair campaign (design round v2). The CONTRACT is
not in dispute, only the proof.

**Run 2 (2026-07-28, W95): root validated then RETRACTED same day** —
run-2 details preserved for the record: 6 rounds, 13/13 live nodes,
one e-binding challenge repaired in-run; oracle + `fr verify` passed at
banking time; the defect was caught hours later by the W97 design-audit
chain (audit finding 2 → adjudication), not by the run's own verifier
cohort.

**Run 1 (2026-07-28, W95): STUCK — deps widened, contract byte-unchanged.**
The first orchestration (tier routine) aborted after 11 rounds with 15/16
nodes validated and the root pending: fresh-verifier-validated audit nodes
(1.3.1–1.3.3, 1.4.1, 1.5 in the run-1 ledger) recorded that the sole
allowed external (the parent control lemma) binds u_delta and g_{sJ} as
bare anaphors, so three root premises were underivable from the exact
allowed inputs: (E1) u_delta is the first component of the inverse of
Pi_delta, (E2) g_{sJ} is the unique C^1 solution of f_{sJ} = 0 on
B_{2delta}^{icalH}(0), (E3) sigma(U) = u_delta(U^dagger) is globally C^1.
All three are carried verbatim by existing af-validated results, so the
deps line was widened (13e-precedent deps-only widening; the contract is
BYTE-UNCHANGED): `lem-stage1-polar-retraction` (E1),
`lem-stage1-unitary-graph-control` (E2, at V = sJ),
`lem-stage1-smooth-unitary-operations` (E3), plus that lemma's three
antecedents `lem-stage1-approximate-group-laws`,
`lem-stage1-smooth-unitary-atlas`, `lem-stage1-smooth-polar-inverse` so
its conditional conclusion is dischargeable from allowed inputs. The
workspace was re-seeded for run 2 (run-1 classification preserved here and
in the fr log, cycle 796).

**W97 amendment (2026-07-28, deps-only).** Deps replaced per the endorsed
rebuild design (`DESIGN-13E-BINDER-v3.md` §1.10; audit chain v3/v3.2,
final VERDICT LAND): the retracted control parent, the retired
smooth-operations parent, the retired group-laws parent, atlas, and smooth
polar inverse are all dropped; the two explicit bridges + polar retraction
+ unitary graph control are the typed providers (audit-v3 confirms they
suffice for the global C^1 sigma — dagger is real-linear, so neither
smooth upgrade is needed). Contract and defs BYTE-UNCHANGED (13g remains
row-13 clause (A_7) verbatim). Elevation queue row 8 (target/hard cap
22/25), audit-v2's fixed explicit-closeness-witness repair: fix
(G_d,P_d,k_d), (G_c,P_c,k_c), (P_r,k_r), (C_g,k_g) FIRST; universal
D_0,k_D,C_der^0,kappa_der^0 are built before the receiving tuple enters;
no step absorbs the unbounded receiving C_grp. Neither the defective
run-2 tree nor the archived run-1 branch is a proof base — cleanly
RE-SEED at elevation (superseding the "re-elevation base" phrasing above).
