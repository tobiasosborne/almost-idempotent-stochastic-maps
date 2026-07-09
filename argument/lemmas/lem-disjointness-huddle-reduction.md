---
id: lem-disjointness-huddle-reduction
kind: lemma
contract: Disjointness huddle reduction: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set, a hidden top vertex v of height H > 8*tau, and a geometrically distinct row vertex u with ||p_u - p_v||_1 < 4*tau and t*(u) > 0: u is hidden with dist_1(p_u, conv{p_w : w in W}) > H - 4*tau, and if conv{p_f - p_u : f in T(u)} and t*(u)*conv{p_i - p_u : i in O(u)} are disjoint (T(u), O(u) the always-tight far/upper families of the exposedness LP at u), then there is a row vertex w with p_w != p_u, ||p_w - p_u||_1 < 4*tau, and dist_1(p_w, conv{p_w' : w' in W}) > H - 8*tau (hence w hidden); contrapositively, if no such pair (u, w) exists then the always-tight hulls at u intersect.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-ball-cluster-exposure-void; lem-always-tight-dual-support; lem-separator-zero-face-obstruction; lem-zero-face-vertex-support; lem-zero-face-localization
status: proved
af: none
provenance: W53 wave (docs/waves/2026-07-09-W53-binding-constraint-lemmaization.md): codex prover B3 (Statement A) + fresh hostile codex verifier VB3 (VALID-WITH-CORRECTIONS; corrections applied — the H-8*tau depth cited to lem-zero-face-localization, mass-carrying pinned as t*(u) > 0)
owner: A
---

**Role (the B3 collapse: top reversion is NOT an independent wall).** The W52 binding
constraint "top reversion with intersection" is exactly this contrapositive: excluding the
huddle pair forces [[conj-zero-face-elimination]]'s intersection horn at every
mass-carrying ball-cluster vertex of a tall top. Chain (VB3-checked): ball-cluster
hiddenness + depth from [[lem-ball-cluster-exposure-void]]; T, O nonempty from
[[lem-always-tight-dual-support]]; a strict separator of the disjoint compact hulls yields
a nonclone zero-face blocker ([[lem-separator-zero-face-obstruction]]); the blocker forces
the second geometrically distinct deep hidden vertex ([[lem-zero-face-vertex-support]]),
with depth > H - 8*tau by [[lem-zero-face-localization]]. Dimension-free; clone-invariant
(geometric-vertex/nonclone language throughout).

**Consumer note.** Together with [[lem-top-witness-third-actor]] the huddle is never
two-body: any in-class disjointness certificate carries the pair (u, w) PLUS a rho-far
top-slab witness actor. THE HUDDLE CHARGE (sketch v17) attacks exactly this three-body
configuration.

**Rigour tier.** L5 (reviewer != author: fresh hostile codex VB3). NOT af-validated.
