---
id: obs-fwr-gap
kind: obstruction
contract: F-WR forbidden-gap dichotomy: for a centered exact self-indexed common-pattern 2-web with X = ||p_i - p_j||_1 and eps = 2.1*(s_i+s_j) + 4*delta, F-WR forces X <= eps + X^2/2, i.e. X outside (approx eps, 2 - eps) - coincident or antipodal, no mid-separated webs; the exact s5 certificate has X = 2003/2000 strictly inside the gap (delta = 1841/1600000, eps = 2681/400000), so its shallow band is provably not a common-pattern web, and web-rigidity cannot supply the dimension-free shallow-class count (the wide branch is saturated by simplex-corner configurations with dimension-many classes).
defs: def-signed-idempotent; def-height; def-visible-set; def-negative-mass
deps: lem-wiggle-rigidity
status: heuristic
af: none
provenance: docs/waves/2026-07-02-B2-fwr-band-probe.md (arm B wave 2, opus worker); s5 rational arithmetic independently recomputed by the orchestrator over exact Fractions (P^2=P, delta, ||p4-p5||_1 = 2003/2000, eps, gap membership - all confirmed); s5 matrix from docs/ingest/experiments/d14_leakage.py:293-303
owner: A
workspace: proofs/obs-fwr-gap
---

**Arm B wave-2 harvest (2026-07-02), status HEURISTIC** — the dichotomy DERIVATION (centered 2-web:
`r_web = X/2` turns [[lem-wiggle-rigidity]] into `X^2/2 - X + eps >= 0`) and the corner-saturation
argument are unreviewed; the s5 arithmetic is exact and was independently recomputed (see provenance).

**Role (obstruction):** closes the web-rigidity family for the anti-splitting question. F-WR is a
coincidence-or-antipodality dichotomy, not a clustering bound: it cannot merge simplex-corner clusters
and places no dimension-free cap on their number; deficit-shallow does not imply ell-1-skinny (s5: two
rows at deficit 0 with separation 2003/2000); and self-indexing is not clone-invariant. Together with
[[obs-deep-leakage]] this exhausts the v-local + web-rigidity families — the class-count bound must
come from a quotient packing statement (signed quantitative Baake-Sumner; kernel-conjecture.tex:284-306,
316-322).

**Elevation candidate:** the dichotomy step is a 2-line quadratic argument over [[lem-wiggle-rigidity]]
plus an exact-rational instance check — a small `af` tree once its input is validated or byte-pinned.
