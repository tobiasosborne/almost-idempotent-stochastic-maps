---
id: obs-height-collapse
kind: obstruction
contract: Height collapse / non-bootstrapping: for an exact signed idempotent P with delta <= 1/4, nonempty visible set W, and hidden top vertex v (height H = dist_1(p_v, conv W) maximal among rows), the invisible mass sigma_v and row negative mass nu_v satisfy H * (1 - sigma_v) <= nu_v * (2 + 4*delta); hence H = O(delta) unless sigma_v -> 1, and a hidden vertex cannot bootstrap height by feeding on a shallow web — the kernel antecedent's only open door is sigma_v -> 1, and sigma_v <= 1 - c*tau for hidden vertices would close the kernel conjecture via this bound.
defs: def-signed-idempotent; def-height; def-visible-set; def-invisible-mass; def-negative-mass
deps: 
status: heuristic
af: none
provenance: docs/waves/2026-07-02-F1-web-regime-hunt.md (arm F wave 1, opus worker; derivation from row reproduction p_v = sum_j P_vj p_j + the 2+4delta row-diameter bound); numerically 0/500 violations over the exact sweep runs/2026-07-02-web-regime-hunt/
owner: A
workspace: proofs/obs-height-collapse
---

**Arm F wave-1 harvest (2026-07-02), status HEURISTIC.** Sketch: split the exact row reproduction
`p_v = sum_j P_vj p_j` into visible-side positive mass (distance 0 from `C_W`), invisible positive mass
`sigma_v` on rows that are themselves at distance `<= H` (v is the top), and negative mass `nu_v <= delta`
paying the row-diameter price `2+4delta`; convexity of `dist_1(., C_W)` gives
`H <= sigma_v*H + nu_v*(2+4delta)`. The quantitative, clone-invariant sharpening of the record's s8 cap.

**Role:** the structural reason arm F's ~48k-instance hunt never entered the dangerous regime — `sigma_v >
tau` is cheap but INERT for height; the antecedent re-scopes to `sigma_v -> 1`. **If af-validated, this is
a candidate FINISHER input**: together with a bound `sigma_v <= 1 - c*tau` for hidden vertices it yields
`H <= delta(2+4delta)/(c*tau) = O(sqrt(delta))`, i.e. the Kernel Conjecture's height cap.

**Elevation:** natural next af target (small tree; only BSc-level convexity + the definitions).
