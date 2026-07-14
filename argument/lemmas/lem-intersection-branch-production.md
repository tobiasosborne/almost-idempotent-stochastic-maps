---
id: lem-intersection-branch-production
kind: lemma
contract: With the universal constant delta_B = 1/4, every exact signed idempotent P with 0 < delta(P) <= delta_B and nonempty visible set W, and every hidden top vertex v of height H > 16*tau (tau = sqrt(delta(P))) such that t*(v) is in (0,kappa), where kappa = tau/4, and conv{p_f - p_v : f in T(v)} intersects t*(v)*conv{p_i - p_v : i in O(v)}, admits either (i) a probability measure lambda_L on rows f satisfying ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv W) > H - 4*tau, whose barycenter b_L satisfies ||b_L - p_v||_1 <= 2.2*tau and for which integral h(p_f) d lambda_L(f) <= (16/13)*kappa for every admissible exposer h at v, or (ii) a sub-probability measure mu_S of total mass at least tau/(2+4*delta(P)) on rows f satisfying ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv W) <= H - 4*tau, for which integral h(p_f) d mu_S(f) <= kappa for every admissible exposer h at v.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height; def-co-top; def-actor-hull
deps: lem-optimal-face-conic-reduction; lem-always-tight-dual-support; lem-intersection-witness-confinement; lem-top-witness-third-actor
status: proved
af: none
provenance: docs/waves/2026-07-14-W68-artifacts/REPAIR-W68-bridge.md Part 2 (W68 extraction of context/l2-attack.md §§2.6–2.7; independently checked in docs/waves/2026-07-14-W68-artifacts/VERDICT-W68-BRIDGE.md; the prose-only B5 is replaced by the proved lem-top-witness-third-actor interface); wave path docs/waves/2026-07-14-W68-artifacts/
owner: A
---

**Role (the Branch-II production implication).** From the intersecting always-tight
actor-hull configuration, this lemma produces either the far co-top probability
measure forbidden by [[conj-straddling-web-exclusion]] or the far shallow
sub-probability measure forbidden by [[conj-shallow-counterweight-exclusion]].

**Mechanism.** Split the confined witness at `mu = tau/D`, where
`D = 2 + 4*delta(P)`: case (i) owns equality and renormalizes the co-top part;
case (ii) retains the shallow part with mass greater than `tau/D`.

**Honest scope.** This does NOT prove SL1a or SL1b and does not exclude either
configuration. It PRODUCES the forbidden objects from the intersection
configuration.

**Rigour tier.** L5 (fresh hostile codex verdict, W68). NOT af-validated.
