---
id: lem-gmax-web-concentration
kind: lemma
contract: G-max web concentration: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), halo width a >= 4, theta in (0,1) with delta + 4*sqrt(delta) < 1 - theta, and height H > ((5a/4 + 3/2)/theta)*sqrt(delta), the observable g = P*1_{G_a} (G_a = {j : dist_1(p_j, conv{p_w : w in W}) > a*sqrt(delta)}) attains its maximum over row indices at a hidden geometrically distinct row vertex r with g_r > 1 - theta - delta, and for every t > 0: sum over {j : g_j <= g_r - t} of max(P_rj, 0) <= nu_r*(g_r - min_i g_i)/t <= delta*(1 + 2*delta)/t.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass; def-height
deps: lem-parametric-halo-collapse; lem-mass-split; lem-harmonic-affine-bridge; lem-visible-g-small
status: proved
af: none
provenance: W34 wave (docs/waves/2026-07-07-W34-gmax-self-consistency.md): fresh-codex prover (worker AB) + SEPARATE fresh-codex hostile verifier (VAB, VALID-WITH-CORRECTIONS — base hypotheses made explicit; ledger and range bounds re-derived; exact mechanics fixture on the banked W19 rank-3 at a = 1/4)
owner: A
workspace: proofs/lem-gmax-web-concentration
---

**Role (the g-max hidden vertex and its ledger).** In tall theta-flexible windows the g-max
row vertex r is HIDDEN (tops carry g > 1 − θ − δ by the collapse + sandwich; visible vertices
are capped at 4τ by [[lem-visible-g-small]]; g is affine by [[lem-harmonic-affine-bridge]] so
its row max sits at a vertex), and harmonicity's self-consistency ledger
Σ_j P_rj (g_r − g_j) = 0 (all gaps ≥ 0 at the max) concentrates r's positive mass on
near-max-g rows up to O(δ)/t. The deep web's carrier is thus pinned at a hidden vertex whose
own admissible g-exposer ([[lem-conditional-g-near-exposer]]) is hiddenness-constrained.

**No-new-squeeze (body, VAB-checked [T0]).** The CS pincer applied to the g-normalized
F = (g_r − g)/(g_r − min g) reproduces EXACTLY this ledger (t = s·(g_r − min g)) — do not
re-derive it as an independent bound.

**Factoring note (af).** The contract bundles existence + value + ledger; an af elevation
must factor it (single-minimal contracts) — see the af-contract memory.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
