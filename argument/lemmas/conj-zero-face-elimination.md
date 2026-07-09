---
id: conj-zero-face-elimination
kind: lemma
contract: (CONJECTURE) Tall-cluster zero-face elimination: there exist universal constants a >= 4, theta_0 in (0,1), A_0 < inf, delta_0 > 0 such that for every exact signed idempotent P with 0 < delta(P) <= delta_0, every hidden top vertex v carrying >= 1 - theta_0 of its positive row mass on its rho-near top-slab cluster C = {j : ||p_j - p_v||_1 < 4*tau, dist_1(p_j, conv{p_w : w in W}) > a*tau}, and every mass-carrying cluster vertex u in C with t*(u) > 0: conv{p_f - p_u : f in T(u)} intersects t*(u)*conv{p_i - p_u : i in O(u)}, or u admits a reduced optimal display whose zero-face conic mass sum a_z is at most A_0.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
af: none
provenance: W44 wave (docs/waves/2026-07-07-W44-t1-intersection.md): the VAR-approved merged terminal statement — the three prover gaps (AR top-slab hull absorption; AS tall-cluster sign rebalancing; AT cluster separator absorption) are this ONE statement seen from the geography, LP-selection, and contradiction sides
owner: A
---

**Role (THE terminal node, sharpest form — sketch v12).** This is sketch v11's (T1) in the
vocabulary of [[lem-optimal-face-conic-reduction]]: eliminate (a_z = 0, the intersection) or
uniformly bound (sum a_z <= A_0) the zero-face conic term at every mass-carrying cluster
vertex of a tall heavy near-cluster top. Either horn feeds the alpha-gauge calculus
([[lem-zero-face-alpha-gauge]], [[lem-radial-alpha-bound]]) and closes
[[conj-low-slab-cap]] => pincer => collapse => Kernel height clause => op-classical (Route A).

**Why the hypotheses are load-bearing.** [[obs-realized-alpha-blowup]] realizes minimum
reduced alpha mass 100 OUTSIDE tall-heavy (H/tau = 1/505); the W44-AU exact rank-3 boundary
census found empty intersections ONLY outside the class (W41 HEIGHT+A: H < 4*tau, empty
width-4 cluster) and intersection certificates on every in-class banked instance
(TOP-preserving, W29 frontier) — codification of that census pends its independent
recomputation (VAU).

**Attack surfaces (from the W44 toolkit).** (a) the located hulls of
[[lem-tight-far-geography]] (top-slab T vs t*-scaled small O) + a Helly/interlacing step;
(b) the separator route: charge [[lem-separator-zero-face-obstruction]]'s nonclone zero-face
blocker via harmonicity and the cluster's coefficient ledger; (c) rank-3 first (planar
hulls; the named lem-rank3-cluster-uniform-optimal-face-interlacing candidate).

**Rigour tier.** CONJECTURE (L0-flagged). Not usable as an input anywhere.
