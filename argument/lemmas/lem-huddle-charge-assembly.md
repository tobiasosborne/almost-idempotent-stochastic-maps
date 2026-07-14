---
id: lem-huddle-charge-assembly
kind: lemma
contract: Assume conj-straddling-web-exclusion with ceiling delta_a, conj-shallow-counterweight-exclusion with ceiling delta_b, conj-cotop-web-coupling with ceiling delta_c and constant c_* in (0,1), and conj-l5-gap-1 with universal constant c_5 (harmlessly decreased, if necessary, so that 0 < c_5 <= 1) and ceiling delta_5(c_*/2) all hold. With delta_B = 1/4 and delta_0 = min{delta_a, delta_b, delta_c, delta_5(c_*/2), delta_B, (c_5*c_*/6)^2}, no exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set W, and hidden top vertex v of height H > 16*tau carries positive coefficient mass sum_{j : ||p_j - p_v||_1 < 4*tau and dist_1(p_j, conv W) > 16*tau} max(P_vj, 0) >= 7/8.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height; def-near-cluster; def-co-top; def-actor-hull; def-top-support-functional
deps: conj-straddling-web-exclusion; conj-shallow-counterweight-exclusion; conj-cotop-web-coupling; conj-l5-gap-1; lem-intersection-branch-production; lem-hiddenness-dual-witness; lem-positive-exposedness-margin; lem-always-tight-dual-support; lem-top-deficit-price
status: proved
af: none
provenance: docs/waves/2026-07-14-W68-artifacts/REPAIR-W68-bridge.md Part 3 (conditional W68 repair of the W54 huddle-charge assembly; independently checked in docs/waves/2026-07-14-W68-artifacts/VERDICT-W68-BRIDGE.md); wave path docs/waves/2026-07-14-W68-artifacts/
owner: A
---

**Role (the W54 assembly bridge, now explicitly conditional and two-branch).**
Assuming the four open conjectures named in the contract, the bridge excludes a
heavy near cluster by splitting the nonempty always-tight actor hulls into their
intersecting and disjoint configurations. The L5 constant is harmlessly shrunk to
`c_5 = min{c_5, 1}` before fixing `delta_0`.

**Calibration and containment.** At `(a, theta_0) = (16, 1/8)`, the assembly
regime `H > 16*tau` contains the `H > 172*tau` regime of
[[conj-near-cluster-absorption]]. The assembly excludes mass at least `7/8`
already on the larger regime.

**Branch summary.** If the actor hulls intersect, [[lem-intersection-branch-production]]
produces either the SL1a object or the SL1b object, contradicting the corresponding
assumed exclusion conjecture. If the hulls are disjoint, the assumed
[[conj-cotop-web-coupling]] supplies far co-top positive mass; the assumed
[[conj-l5-gap-1]] prices it from below, while [[lem-top-deficit-price]] prices the
same charge from above, and the ceiling `(c_5*c_*/6)^2` makes the bounds
incompatible.

**HONEST STATUS.** This is a PROVED CONDITIONAL implication resting on four open
conjectures. Consuming its conclusion unconditionally is illegal.

**Supersession.** This SUPERSEDES the 2026-07-10 `stated`/INVALID version recorded
in `verdict-bridges.md` §2. The old `workspace` field is dropped.
