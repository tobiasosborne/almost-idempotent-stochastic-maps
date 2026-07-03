---
id: lem-fan-payment
kind: lemma
contract: Zero-sum fan payment: let (w_1, p_1), ..., (w_m, p_m) be a finite family with vectors w_i in R^d and weights p_i > 0 satisfying sum_i p_i = 1, such that every w_i has coordinate sum zero (sum_l w_i(l) = 0) and the weighted barycenter is zero (sum_i p_i w_i = 0); write n(w) = sum_l max(-w(l), 0); then min over i* in {1, ..., m} of sum_i p_i n(w_i - w_{i*}) <= 2 * sum_i p_i n(w_i).
defs: 
deps: lem-zerosum-triangle; lem-weighted-min
status: proved-mod-audit
af: seeded
provenance: docs/waves/2026-07-03-A10-weighted-payment.md (arm A wave 10, codex; T2 "A fan all-mass inequality is proved inline" — support-averaging step: some support point v has n(v) <= N := sum_i p_i n(w_i); zero-sum triangle step: n(w - v) <= n(w) + n(v) since pos(v) = neg(v) for coordinate-sum-zero v)
owner: A
workspace: proofs/lem-fan-payment
---

**The all-mass fan payment lemma** — the discrete mechanism behind the certified plateau-2 constant
on every reduced fan family of the arm-A campaign (A2 path, A3/A6/A7 couplings): in a reduced
edge-fan chart the anchor-pivot score is exactly the weighted average `sum_i p_i n(w_i - w_*)` with
`delta = ` (shear scale) `*` (max fan negative mass), so this lemma bounds the fan-template
`Phi/delta` by `2`.

**Elevation history:** run 1 (2026-07-03) BALLOON-aborted 39 > cap 30; run 2 (resume, cap 40)
BALLOON-aborted 47 > 40 — a linear proof chain forced into a tree, cross-sibling bridges re-deriving
the averaging and triangle steps, plus one MISSING fact (`n(-z)` needs zero coordinate sum).
Classification per §6.3: FACTOR — deps [[lem-zerosum-triangle]] + [[lem-weighted-min]] registered
(aism-ugk); plan: validate both, wipe + re-seed this workspace (root contract UNCHANGED) with the
deps as af externals, re-orchestrate.

**Status:** the inline proof is the A10 codex worker's (two elementary steps, quoted in the
provenance field); it has NOT cleared an independent reviewer or af pass here, hence
`proved-mod-audit` (L0). Elevation intended (small tree expected).

**Sharpness context (A10, T0):** the over-broad variant with an ARBITRARY chosen `w_0` (instead of
the minimizer) and without the coordinate-sum-zero hypothesis is refuted exactly (scalar certificate
`G = {1, -1/4, -1/4, -1/4, -1/4}`, `w_0 = 1`, ratio `5`). The D-restricted variant (denominator
restricted to rows with `n(w_i - w_*) > 0`) is OPEN — it is the fan-template shadow of the
weighted own-negativity payment (WOP) behind [[conj-degenerate-payment]]; the lopsided uniform fan
witnesses the gap (all-mass ratio `5/8` vs D-restricted `5/4`).

**Role:** model transport inequality for the payment horn of the (EX) argmin charge; if the
D-restricted version holds, it lifts toward WOP via the row-reproduction identity (A10 T3 plan).
