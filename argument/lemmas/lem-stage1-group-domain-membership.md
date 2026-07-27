---
id: lem-stage1-group-domain-membership
kind: lemma
contract: Group-input polar-domain membership: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta:S_delta -> calU of the polar map is defined at U bold-dot V and U^dagger for every U, V in calU; moreover, U bold-dot V and U^dagger each have a right inverse.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
status: proved
af: validated
workspace: proofs/lem-stage1-group-domain-membership
provenance: DESIGN-S1-GROUP-FACTORING.md sect-2.1, landed verbatim (row-6 balloon repair; AUDIT-S1-GROUP-FACTORING.md LAND-WITH-CORRECTIONS, contract clause PASS); derivation from lem-stage1-polar-retraction + the two registered definitions; orientation Kitaev TeX 845-868 (qualitative O(epsilon_r) only — NOT byte-citable for this quantitative contract).
owner: A
---

**Status.** af-VALIDATED 2026-07-27 (93rd rigorous result): run 2 (fresh
tree with the provisioned smallness discipline; prover xhigh, verifiers
high) — root validated, 10/10 nodes, taint clean. Run 1 aborted STUCK on
prover-discipline thrash (see the smallness note below). Export in the
workspace; oracle + `fr verify` PASS. Landed VERBATIM from the audited
`DESIGN-S1-GROUP-FACTORING.md` §2.1 (design skeleton 9/12). The explicit
right-inverse conclusion is intentional: membership in calU_delta requires
a right inverse, so the proof MUST include the finite-dimensional
left-multiplier argument for U bold-dot V (L_{U bold-dot V} as an
invertible perturbation of L_U L_V), not infer membership from the defect
estimate alone.

**In-scope smallness (AUDIT-S1-GROUP-FACTORING (b), binding on the af
tree).** Derive IN AN EARLY NODE, from the two contract guards alone:
since C_pol, C_grp >= 1 and kappa_pol <= 1/2, guard 1 gives
epsilon_r + delta <= 1/2 and guard 2 gives
epsilon_r < delta*(1 - epsilon_r - delta); jointly epsilon_r < 1/6 (and
delta <= 1/2). EVERY subsequent smallness inference must cite that node
explicitly — e.g. 1 - 4*epsilon_r > 1/3 (NOT >= 1/2, which needs
epsilon_r <= 1/8 and is NOT derivable from the guards; absorb the worse
constant into the proof-body coefficients instead). No magic thresholds
(1/8, 1/512, ...) without an in-context derivation; no symbol may be used
outside the node that binds it (run-1 STUCK cause: ch-bfd6d8aed4ae5d34,
ch-a188b12ae64b6a56, ch-1c370a3385809d72, ch-e2b6d8a09c645676).

**Endpoint discipline (audit-corrected, binding).** Every estimate uses <=;
the ONE legitimate strict step: let K dominate the raw-defect coefficients,
require C_grp >= K in the proof-body witness choice, then
||X^dagger bold-dot X - J|| <= K*epsilon_r <= C_grp*epsilon_r < t < 2*t
with t = delta - C_pol*(epsilon_r*delta + delta^2) > 0 (valid at
epsilon_r = 0: it reads 0 < t < 2*t). Constants live in the proof body,
never in the contract.
