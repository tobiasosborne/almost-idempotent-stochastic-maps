---
id: lem-compcb-amplification-naturality
kind: lemma
contract: Amplification naturality of the power-series functional calculus: let B be a unital Banach algebra, iota_n: B -> M_n(B) the unital amplification X -> 1_{M_n} tensor X (an isometric unital homomorphism), and f given on ||X - x_0 I|| < r by the power series f(X) = a_0 I + sum_{m>=1} a_m (X - x_0 I)^m; then for every X in B with ||X - x_0 I|| < r, f(iota_n(X)) is defined and f(iota_n(X)) = iota_n(f(X)); in particular, whenever ||(2P-I)^2 - I|| < 1, theta(iota_n(2P-I)) = iota_n(theta(2P-I)) with theta(X) = (I + sgn(X))/2.
defs: def-theta-idempotent-approximation
deps:
status: stated
af: none
provenance: factored out of proofs/lem-compcb-amplified-compression per the STUCK-abort tripwire classification (2026-07-24, challenges ch-56b93288d4201d17 / ch-dd07e65848cdbb97 / ch-32a052f1130ec348 all name this equation); statement extracted mechanically from the challenge/verifier text; UNPROVED here (status stated) pending its own af pass
owner: A
workspace: proofs/lem-compcb-amplification-naturality
---

**Status.** `stated` — the missing equation named identically by three
blocking challenges in orchestration #1 (the theta-naturality thrash cluster),
factored into its own registry shard per the campaign's DAG-dep tripwire rule
(CLAUDE.md §6; aism-q7e precedent). No proof is claimed here; the af pass on
this shard is the proof.

**Why this factoring.** `lem-compcb-amplified-compression`'s tree proved 16/25
nodes but thrashed on cross-sibling references to this one identity (pending
count non-shrinking over 3 rounds). Bottom-up discipline: validate this leaf
first, then re-seed the parent with it as an af-consumable validated dep.

**Mechanism sketch (not a proof).** `iota_n` is an isometric unital
homomorphism, so it fixes `I`, preserves powers of `(X - x_0 I)`, and carries
norm-convergent partial sums to norm-convergent partial sums; the series
defining `f` therefore commutes with `iota_n` term-by-term and in the limit.
The `theta` specialization is the composite with [[def-theta-idempotent-approximation]].
