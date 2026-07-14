---
id: conj-l5-gap-1
kind: lemma
contract: There exists a universal c_5 > 0 such that, for every fixed universal c_m > 0, there exists a universal delta_5 = delta_5(c_m) > 0 for which the following holds: whenever P is an exact signed idempotent with 0 < delta(P) <= delta_5 and nonempty visible set W, v is a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), and A is a subset of {j : ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau} satisfying sum_{j in A} max(P_vj, 0) >= c_m, some top support functional phi at v satisfies sum_{j in A} max(P_vj, 0)*(H - phi(p_j)) >= c_5*c_m*tau.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height; def-co-top; def-top-support-functional
deps:
status: conjecture
af: none
provenance: docs/waves/2026-07-10-remediation-artifacts/verdict-bridges.md item 2; docs/waves/2026-07-14-W68-artifacts/REPAIR-W68-bridge.md Part 1; docs/waves/2026-07-14-W68-artifacts/VERDICT-W68-BRIDGE.md line P1
owner: B
---

**Role (the registered W54 L5-GAP-1 target).** This is a registration only; no
proof is claimed. The W62-W67 `lem-l5-*`, `lem-ihorn-*`, `lem-icap-*`,
`lem-dcap-*`, and `lem-aesc-*` interfaces form the reduction/attack tree for this
target. That relation is recorded here in the body only: those interfaces are not
asserted to prove the conjecture and are not dependencies of this shard.

**Simplex-obstruction warning.** The pointwise sibling
[[conj-summit-cylinder-exclusion]] does not imply this mass statement by selecting
one functional per row and averaging. The simplex obstruction permits every atom
to have a favorable dual direction while the mass barycenter re-enters the summit
cylinder. Consistently with [[lem-intersection-witness-confinement]], no
averaged-witness mechanism is used here.
