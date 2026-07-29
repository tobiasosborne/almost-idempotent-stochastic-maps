---
id: lem-stage1-approximate-group-laws-transport
kind: lemma
contract: Parameterized approximate-group transport: there exist C_grp^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_grp >= C_grp^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the formulas mu(U, V) = u_delta(U bold-dot V) and sigma(U) = u_delta(U^dagger) define C^1 maps on all of calU x calU and calU, respectively, and for every U, V, Z in calU, mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), Z) - mu(U, mu(V, Z))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-explicit-group-closeness; lem-stage1-polar-retraction
status: proved
af: validated
workspace: proofs/lem-stage1-approximate-group-laws-transport
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13e, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional domain restriction, audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 845-878; parameterized estimate/guard monotonicity; AUDIT-S1-POLAR-v4.md sect-1.5, sect-3.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 13e (final verdict LAND; the v5-audit
all-domain polar-inverse defect is CLEARED-BY the finite-dimensional
insertion matched to base row 6 and polar row 4). Not proved in-repo;
af elevation per the design's projected budget 4/2.

**STUCK repair (2026-07-27, W93 run 1).** The af run aborted STUCK: three
verifier challenges correctly identified that the contract's binder "the
unique inverse (u_delta, h_delta) of Pi_delta" is not derivable from the
sole original dep (whose contract mentions only u_delta on its own
hypotheses). The missing fact is exactly the af-validated
`lem-stage1-polar-retraction` (existence, uniqueness, and the two-component
inverse of Pi_delta on calU x B^calH_delta(J)); it was added as a second
dep and byte-matched workspace external. Contract BYTE-UNCHANGED.

**STUCK repair 2 (2026-07-27, W93 run 2).** Run 2 validated 24/27 nodes but
stuck on the synchronization gap the verifiers isolated (node 1.7.5,
ch-8ee08e89/ch-a893c648): the workspace had no fact identifying the u_delta
of the group-laws contract with the first inverse component of
Pi_delta from the polar-retraction import. The registry's canonical bridge
is the af-validated `lem-stage1-polar-coherence-naturality` (any two polar
data agree on the overlap; scalar naturality); added as a third dep and
byte-matched workspace external. Contract BYTE-UNCHANGED. Prover escalated
to xhigh per the post-STUCK playbook.

**W97 amendment (2026-07-28, deps-only).** Deps replaced per the endorsed
rebuild design (`DESIGN-13E-BINDER-v3.md` §1.7; audit chain v3/v3.2, final
VERDICT LAND): the retired anaphoric parent and coherence-naturality are
dropped; the two explicit binder-closed bridges + the polar retraction are
the typed providers. Contract and defs BYTE-UNCHANGED (13e remains row-13
clause (A_5) verbatim). Elevation queue row 5 (target/hard cap 16/22): fix
witnesses (G_d,P_d,k_d), (G_c,P_c,k_c), (P_r,k_r) BEFORE quantifying over
the receiving tuple; C_grp^0 = max{G_d,8*G_c,8}. All providers display the
identical Pi_delta, so ordinary inverse uniqueness synchronizes them —
coherence-naturality is neither needed nor listed. The old 37-node paused
tree is NOT a repair base — cleanly RE-SEED at elevation.

**Build-granularity discipline (BINDING on the af tree; extends the
user-ratified row-1 discipline of 2026-07-28 — run-1 there ABORTED
[BALLOON] from sub-splitting routine norm estimates).** The target is the
design's 16-node skeleton (hard cap 22). Tree discipline per design v3
sect-1.7: (i) ONE early node fixing the provider witnesses (G_d,P_d,k_d),
(G_c,P_c,k_c), (P_r,k_r) from the three displayed externals and setting
C_grp^0 = max{G_d,8*G_c,8}, C_pol^0 = max{P_d,P_c,P_r}, kappa_pol^0 =
min{k_d,k_c,k_r,1/16} — BEFORE quantifying over the receiving tuple W
(the second BINDING process law: receiving fields transport by
monotonicity, never treated as universal constants); (ii) ONE node
showing the receiving guards imply all three fixed provider guards by
monotonicity; (iii) ONE node synchronizing the providers via ordinary
inverse uniqueness of the ONE displayed Pi_delta; (iv) ONE node per group
law (two units, two closeness bounds, associativity, two inverse laws) —
do NOT sub-split routine submultiplicativity/triangle estimates within a
law. Constants live in the proof body, never the contract; every
smallness inference cites its guard node explicitly.

**af-VALIDATED 2026-07-29 (W98, elevation queue row 5 — the FIRST 13e
validation; W93 runs 1-2 had stuck on the u_grp/u_pol synchronization
gap that the typed spine removes by construction).** Clean re-seed on
the three-provider spine. First-pass run under the binding
build-granularity discipline above (tier routine, fresh codex verifier
per node): root validated, 16/16 live nodes (EXACTLY the design target;
hard cap 22), taint clean, 6 rounds, three in-run challenges repaired
(all the epsilon_r=0 strict-inequality endpoint — bounds made
non-strict; ch-723fdaab and the 1.13/1.14 siblings) and re-verified
fresh. Export in the workspace; oracle
`af-lem-stage1-approximate-group-laws-transport` + `fr verify` PASS.
This status flip is a mechanical reflection of the codex ledger.
