---
id: lem-stage1-group-domain-membership
kind: lemma
contract: Group-input polar-domain membership: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta:S_delta -> calU of the polar map is defined at U bold-dot V and U^dagger for every U, V in calU; moreover, U bold-dot V and U^dagger each have a right inverse.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
status: stated
af: seeded
workspace: proofs/lem-stage1-group-domain-membership
provenance: DESIGN-S1-GROUP-FACTORING.md sect-2.1, landed verbatim (row-6 balloon repair; AUDIT-S1-GROUP-FACTORING.md LAND-WITH-CORRECTIONS, contract clause PASS); derivation from lem-stage1-polar-retraction + the two registered definitions; orientation Kitaev TeX 845-868 (qualitative O(epsilon_r) only — NOT byte-citable for this quantitative contract).
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-GROUP-FACTORING.md` §2.1 (hostile verdict LAND-WITH-CORRECTIONS;
the correction was proof-body-only). Not proved in-repo; af elevation per
the design's §5.1 skeleton (9-node target, 12 hard cap). The explicit
right-inverse conclusion is intentional: membership in calU_delta requires
a right inverse, so the proof MUST include the finite-dimensional
left-multiplier argument for U bold-dot V (L_{U bold-dot V} as an
invertible perturbation of L_U L_V), not infer membership from the defect
estimate alone.

**Endpoint discipline (audit-corrected, binding).** Every estimate uses <=;
the ONE legitimate strict step: let K dominate the raw-defect coefficients,
require C_grp >= K in the proof-body witness choice, then
||X^dagger bold-dot X - J|| <= K*epsilon_r <= C_grp*epsilon_r < t < 2*t
with t = delta - C_pol*(epsilon_r*delta + delta^2) > 0 (valid at
epsilon_r = 0: it reads 0 < t < 2*t). Constants live in the proof body,
never in the contract.
