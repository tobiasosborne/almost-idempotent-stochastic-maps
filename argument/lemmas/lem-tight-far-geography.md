---
id: lem-tight-far-geography
kind: lemma
contract: Tight-far geography: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set: (i) at a hidden top vertex v of height H, every hiddenness dual witness satisfies lambda{f in T(v) : dist_1(p_f, conv W) > H - c*tau} > 1 - (1/2 + delta)/c for every c > 0, so H > (a + 1/2 + delta)*tau forces T(v) intersect G_a nonempty; (ii) if u is hidden with ||p_u - p_v||_1 < 4*tau for a hidden top v of height H and admits a witness with total alpha mass A <= A_0, that witness satisfies lambda{f in T(u) : H - phi(p_f) <= c*tau} >= 1 - K/c with K = 1/2 + delta + 4*(1 + A_0); (iii) if u is hidden with t*(u) > 0 then every i in O(u) has ||t*(u)*(p_i - p_u)||_1 <= (1/2 + delta)*tau.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-always-tight-dual-support; lem-hiddenness-depth-markov; lem-bounded-alpha-top-slab-reduction; lem-cs-low-slab-pincer
status: proved
af: none
provenance: W44 wave (docs/waves/2026-07-07-W44-t1-intersection.md): fresh-codex prover (worker AR) + SEPARATE fresh-codex hostile verifier (VAR, VALID-WITH-CORRECTIONS — hypotheses delta > 0, W nonempty, hidden-top/near-top made explicit; (i) constant and direction re-derived against lem-hiddenness-depth-markov; (ii) K verified against lem-bounded-alpha-top-slab-reduction, phi <= dist_1(., conv W) via phi <= 0 on conv W and 1-Lipschitz; (iii) via the def-signed-idempotent pairwise-l1-distance clause (2 + 4*delta) with t* < kappa = tau/4 (hiddenness) and the s = 1 pincer mass cap)
owner: A
---

**Role (the LOCATED families).** The terminal intersection question is now about two
explicitly located displacement families: witness far-mass concentrates on rho-far TOP-SLAB
rows of T (unconditionally at tops, conditionally with bounded alpha at 4-tau-near cluster
vertices), while O-displacements are (1/2 + delta)*tau-small after t*-scaling. Combined with
[[lem-optimal-face-conic-reduction]], the missing step is forcing the two located hulls to
meet ([[conj-zero-face-elimination]]).

**Rigour tier.** In-repo paper proof with fresh hostile review (L5). NOT af-validated, NOT
L0. Elevation after the support lemma (its dep chain includes the reviewed-only
lem-bounded-alpha-top-slab-reduction).
