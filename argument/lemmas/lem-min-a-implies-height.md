---
id: lem-min-a-implies-height
kind: lemma
contract: Conditional MIN-A height bound: assuming conj-min-a-w4, every exact signed idempotent P with 0 < delta(P) <= (17 - 12*sqrt(2))/2 and nonempty visible set W(P) satisfies H(P) <= 13*sqrt(delta(P)).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-invisible-mass; def-height
deps: conj-min-a-w4; lem-parametric-halo-collapse; lem-mass-split
status: proved
af: none
provenance: W28 wave (docs/waves/2026-07-06-W28-parametric-assembly.md): fresh-codex prover (worker S) + SEPARATE fresh-codex hostile verifier (VS, VALID — imported contracts byte-faithful, sigma_4 functional identical across shards, 0 < delta_1 < 1/4 exact via 289 > 288 and 1089 < 1152, exact fixture check on the banked rank-5 instance); the D1 assembly re-aimed at the parametric form (aism-yxa), B = 13 at width 4
owner: A
workspace: proofs/lem-min-a-implies-height
---

**Role (Route A's conditional spine, closed at B = 13).** Reduces the Kernel height clause to
the single frontier conjecture: with [[lem-kernel-implies-hlc]] and [[lem-hlc-implies-exposed-hull]]
this chain carries [[conj-min-a-w4]] all the way to op-exposed-hull's pinned-delta conclusion —
MODULO W-nonemptiness at delta > 0 (independent front, W30) and the delta_1 smallness (a
universal-constant restriction, never elide it). Mirrors the conditional pattern of
[[lem-kernel-implies-hlc]] (the conjecture hypothesis is carried by the dep edge).

**Proof shape (worker S, T1; VS).** Suppose H > 13*tau. Height is attained at a row vertex and a
positive-height maximizer is hidden (def-height). For every hidden top, apply
[[lem-parametric-halo-collapse]] at a = 4 and bound the right side: sigma - sigma_4 <= 1 + nu_v
([[lem-mass-split]]; G_4 lies in the invisible set as tau > 0), nu_v <= delta, and
delta*(2 + 4*delta) <= (3/2)*tau (sharp at tau = 1/2), giving H*(1 - sigma_4) <= (13/2)*tau. If
some hidden top had sigma_4 <= 1/2 then H <= 13*tau — contradiction; so EVERY hidden top has
sigma_4 > 1/2 (the sigma_4 >= 1 branch explicit, no division). That contradicts
[[conj-min-a-w4]]'s conclusion (SOME hidden top with sigma_4 <= 1/2). Hence H <= 13*tau.

**Honest limits.** Conditional on an open conjecture (dep edge); needs W(P) nonempty as a
hypothesis; delta <= delta_1 = (17-12*sqrt2)/2 is where conj-min-a-w4 lives — only
delta <= 1/4 is used by the unconditional half of the chain.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
