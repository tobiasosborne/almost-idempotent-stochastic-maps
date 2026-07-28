---
id: lem-stage1-inversion-derivative-control
kind: lemma
contract: Typed inversion derivative with chart retention: there exist universal C_der, C_ch, C_pol, C_grp >= 1 and kappa_der, kappa_ch, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra, s in {+1, -1}, and 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, the globally defined sigma(U) = u_delta(U^dagger) maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart, where chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)), and F_s(A) = phi_{sJ}^par(sigma(chi_s(A))) satisfies ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for all A in B_r^{icalH}(0).
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-unitary-graph-control; lem-stage1-polar-retraction; lem-stage1-polar-coherence-naturality; lem-stage1-approximate-group-laws
status: stated
af: seeded
workspace: proofs/lem-stage1-inversion-derivative-control
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 8, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional domain restriction, audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Source loci TeX 728-762, 857-892, 943; the group/adjoint-domain edge and chart-retention guard are explicit.
owner: A
---

**Status.** **RETRACTED from the rigorous record 2026-07-28** (see
`docs/LEARNINGS.md` 2026-07-28 entry; bug bead `aism-e1qs`). The
2026-07-27 af validation (then the 97th rigorous result; 10/10 nodes,
zero challenges) was found DEFECTIVE by an independent fresh-codex
adjudication
(`docs/plans/2026-07-28-13E-BINDER-design/ADJUDICATION-T0-ALLEGATION.md`,
T1): export node 1.3 uses one polar factor W simultaneously for the exact
factorization (from the typed `lem-stage1-polar-retraction` datum) and
the closeness estimate (from the anaphorically-bound
`lem-stage1-approximate-group-laws` u_delta) — the identification
u_grp = u_pol is underivable from the registered externals (no typed
preimage witness h_X with X = u_grp(X) bold-dot h_X; coherence-naturality
is conditional on TWO typed data and only one is available). Every later
differentiated factorization depends on that unsupported step. Status
mechanically demoted proved→stated, af validated→seeded; the workspace
and ledger are retained as the re-elevation base. Re-derivation on an
explicit-binder dependency spine is part of the 13e repair campaign
(design round v2). Originally landed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 8 (final verdict LAND; carries the v6
finite-dimensional insertion) — the CONTRACT is not in dispute, only the
proof.

**Derivation obligation (design §4).** `lem-stage1-approximate-group-laws`
supplies the all-calU adjoint domain. The explicit retention guard keeps
sigma(chi_s(A)) in the same chart, so coordinate equality is legitimate.
The bad second-variable display at TeX 883–888 is unused.
