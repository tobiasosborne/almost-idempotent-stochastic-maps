---
id: lem-stage1-inversion-derivative-control
kind: lemma
contract: Typed inversion derivative with chart retention: there exist universal C_der, C_ch, C_pol, C_grp >= 1 and kappa_der, kappa_ch, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra, s in {+1, -1}, and 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, the globally defined sigma(U) = u_delta(U^dagger) maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart, where chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)), and F_s(A) = phi_{sJ}^par(sigma(chi_s(A))) satisfies ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for all A in B_r^{icalH}(0).
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-unitary-graph-control; lem-stage1-polar-retraction; lem-stage1-polar-coherence-naturality; lem-stage1-approximate-group-laws
status: proved
af: validated
workspace: proofs/lem-stage1-inversion-derivative-control
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 8, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional domain restriction, audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Source loci TeX 728-762, 857-892, 943; the group/adjoint-domain edge and chart-retention guard are explicit.
owner: A
---

**Status.** af-VALIDATED 2026-07-27 (97th rigorous result): first-pass —
root validated, 10/10 nodes, taint clean (tier routine: prover high /
verifiers high, zero challenges). Export in the workspace; oracle
`af-lem-stage1-inversion-derivative-control` + `fr verify` PASS. Landed
VERBATIM from the audited `DESIGN-S1-POLAR-v6.md` §3 row 8 (final verdict
LAND; carries the v6 finite-dimensional insertion).

**Derivation obligation (design §4).** `lem-stage1-approximate-group-laws`
supplies the all-calU adjoint domain. The explicit retention guard keeps
sigma(chi_s(A)) in the same chart, so coordinate equality is legitimate.
The bad second-variable display at TeX 883–888 is unused.
