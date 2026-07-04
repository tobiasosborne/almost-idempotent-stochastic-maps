---
id: conj-skinny-shadow-cap
kind: lemma
contract: Skinny two-shadow cap: there exist universal constants delta_0 > 0, c in (0,1), and C < infinity (all independent of the dimension) such that for every exact signed idempotent P (square real matrix with P^2 = P and all row sums equal to 1) with delta(P) <= delta_0, writing tau = sqrt(delta(P)), rho = 4*tau, kappa = tau/4, W for the (rho,kappa)-exposed visible set, and C_W = conv{ p_w : w in W }, the following holds: if v1 and v2 are distinct hidden row vertices of P admitting mutual-shadow decompositions p_{v1} = mu_1 * p_{v2} + (1 - mu_1) * L_1 + e_1 and p_{v2} = mu_2 * p_{v1} + (1 - mu_2) * L_2 + e_2 with L_1, L_2 in C_W, ||e_1||_1 <= rho, ||e_2||_1 <= rho, mu_1, mu_2 in [0, 1], and mu_1 * mu_2 >= 1 - c, then dist_1(p_{v1}, C_W) <= C * tau.
defs: def-signed-idempotent; def-negative-mass; def-exposed; def-visible-set
deps: 
status: conjecture
af: none
provenance: bd aism-136 codex verifier note (2026-07-02, candidate contract 1) + docs/waves/2026-07-02-B1-dual-localization.md sec 6 + docs/ingest/experiments/DELIVERABLE2_asq_proof.md:77-86 + docs/ingest/experiments/asq_coupled.py:10-23 + docs/ingest/report/sections/06-day1-belt.tex:89-95; supersedes lem-dual-localization (user decision 2026-07-04)
owner: A
workspace: proofs/conj-skinny-shadow-cap
---

**The corrected Route-B statement, superseding [[lem-dual-localization]]** (whose transcribed
contract — "reproduce `||Ebar||_1 >= H` from `P^2=P`" — is trivially true as stated: with
`v1 = Lbar + Ebar`, `Lbar in C_W`, the bound `H <= dist_1(p_v1, C_W) <= ||Ebar||_1` is a distance
tautology needing no idempotence; confirmed by an independent codex verifier, 2026-07-02).

**What this conjecture actually asks.** In the anchored two-shadow setup (each of two
non-exposed vertices is, up to an `l1`-error `<= rho`, a convex combination of the other and
visible-hull mass), the composed convex bound gives
`dist_1(p_v1, C_W) <= (1 + mu_1) * rho / (1 - mu_1 * mu_2)`, which is VACUOUS as
`mu_1 * mu_2 -> 1`; equivalently `(1 - mu_1 * mu_2) * H <= (1 + mu_1) * rho` shows the skinny
regime is *forced* whenever the height is large against `rho`
(`06-day1-belt.tex:89-95`, `asq_coupled.py:10-23`). The conjecture says exactness must close
this hole: in the skinny regime the height is capped at the `sqrt(delta)` scale anyway.

**Dead-route flag (do not re-walk).** Any proof attempt using ONLY the composed decomposition
`v1 = Lbar + Ebar` (pure convex shadow composition) is the recorded dead route — the bound above
is vacuous in exactly the regime hypothesised here. A proof must consume `P^2 = P` beyond the
composition (e.g. the clone-invariant harmonic identity of `obs-deep-leakage`, or a global
band/anti-splitting argument). Candidate contract 2 from the verifier (height-conditioned
shallow-web exclusion) was rejected as a shard: it is [[conj-kernel]] restated.

**Role.** This is the frame-free skinny-regime cap Route B needs; with it the two-shadow
composition chain toward [[op-exposed-hull]] loses its only vacuous step. It is consistent with
(and at the same `sqrt(delta)` scale as) the arm-B sigma-cap target and the af-validated
[[obs-height-collapse]] upper side.
