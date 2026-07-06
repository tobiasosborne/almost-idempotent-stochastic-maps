---
id: lem-hlc-implies-exposed-hull
kind: lemma
contract: HLC implies exposed hull (pinned-delta form): if there are universal delta_0 > 0 and C_1 < inf such that every exact signed idempotent P with d = delta(P) <= delta_0 has nonempty visible set W(P) and H(P) <= C_1*sqrt(d), then with C = max{4, C_1} and c = 1/4, every such P has every row within C*sqrt(d) of conv W_{C*sqrt(d), c*sqrt(d)}(P), where W_{rho,kappa}(P) denotes the set of (rho,kappa)-exposed geometrically distinct row vertices.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height; def-near-positive-projection
deps: op-hlc
status: proved
af: none
provenance: W27 wave (docs/waves/2026-07-06-W27-hlc-exposed-hull.md): fresh-codex prover (worker R; docs/ingest/report/kernel-conjecture.tex:193-221 + the sister-repo W2d grand-assembly note as objects of study only) + SEPARATE fresh-codex hostile verifier (VR, VALID-WITH-CORRECTIONS, ingest off-limits — re-derived e_v(rho) monotonicity with the t* = +infty empty-far-set convention; exact fixture on the W25 3x3 under canonical geometry); trunk step <2>6, previously proved-mod-audit only
owner: A
workspace: proofs/lem-hlc-implies-exposed-hull
---

**Role (trunk <2>6, staleness debt PAID at reviewed tier).** Establishes [[op-exposed-hull]]'s
row-distance conclusion conditionally on [[op-hlc]] — in the PINNED-delta form d = delta(P), with
W-nonemptiness an EXPLICIT hypothesis (def-height needs it; op-hlc's contract is silent — the
same gap W30 attacks as a standalone question). Chain:
op-classical <= op-exposed-hull <= [[op-hlc]] <= [[conj-kernel]], now reviewed at every inner link.

**Proof shape (worker R, T1; VR).** W(P) = W_{4*sqrt(d), sqrt(d)/4} by def-visible-set;
e_v(rho) is monotone nondecreasing in rho (larger rho shrinks the far set; empty far set gives
t* = +infty), so W(P) is contained in W_{C*sqrt(d), c*sqrt(d)} for C >= 4, c = 1/4; hull
monotonicity + the HLC height bound give dist_1(p_i, conv W_{C sqrt d, c sqrt d}) <=
dist_1(p_i, conv W(P)) <= H(P) <= C_1*sqrt(d). The inherited localization constant
C' = max(4A, 1/sqrt(a)) is unnecessary under the direct HLC form.

**Matrix form (body, honest interface).** Row-wise ell1-projection onto conv W(P) yields Q with
rows in the hull, ||P - Q||_{inf->inf} <= C_1*sqrt(d), Q1 = 1, and delta(Q) <= d (convexity of
the negative-part functional). **Q is NOT proved stochastic and NOT proved idempotent** — the
<2>7 consumer must be audited against exactly this interface (FINDINGS 2026-07-06 W27).

**AUDIT FINDING (why "pinned-delta").** The registered [[op-exposed-hull]] contract read
literally (free upper bound delta >= delta(P), kappa = c*sqrt(delta)) is NOT proved here: the
kappa-threshold grows with loose delta while the proven margin stays sqrt(d)/4. The missing
robustness lemma (W_{4 sqrt d, sqrt d / 4} is contained in W_{C sqrt delta, c sqrt delta} for
d <= delta <= delta_0) is OPEN and named.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
