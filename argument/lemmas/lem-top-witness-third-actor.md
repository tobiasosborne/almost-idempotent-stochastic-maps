---
id: lem-top-witness-third-actor
kind: lemma
contract: Top-witness third actor: for an exact signed idempotent P with 0 < delta(P) <= 1/4 and nonempty visible set, a hidden top vertex v of height H, and any hiddenness dual witness (lambda, alpha, beta) of v with sum_i beta_i < tau/4: for every c > 1/2 + delta, lambda{f in F_v : dist_1(p_f, conv{p_w : w in W}) > H - c*tau} > 1 - (1/2 + delta)/c, where F_v = {j : ||p_j - p_v||_1 >= 4*tau}; at c = 4 more than 13/16 of lambda sits on rho-far rows of depth > H - 4*tau; in particular no two-point set {p_v, p_z} with ||p_z - p_v||_1 < 4*tau supports the witness — a third geometrically distinct row point in the width-4 top slab, rho-far from v, carries positive lambda-mass.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-hiddenness-depth-markov; lem-hiddenness-dual-witness
status: proved
af: none
provenance: W53 wave (docs/waves/2026-07-09-W53-binding-constraint-lemmaization.md): codex prover B2 (Proposition A) + fresh hostile codex verifier VB2 (VALID-WITH-CORRECTIONS; corrections applied — the small-beta witness hypothesis sum beta_i < tau/4 made explicit; "third geometrically distinct row point" wording)
owner: A
---

**Role (the huddle is never two-body).** The W52 "forced visibility" constraint's real
static content: a tall top cannot hide using only its rho-near huddle partner — its
canonical witness ([[lem-hiddenness-dual-witness]], normalized lambda on F_v) must place
> 13/16 of its mass on rows that are simultaneously rho-FAR from v and near top height
([[lem-hiddenness-depth-markov]] at c = 4, delta <= 1/4: 1 - (3/4)/4 = 13/16). Clones of
v or z stay out of F_v, so the mass lands on a genuinely third row point: any huddle
configuration drags a rho-separated top-slab WEB with it. Dimension-free; clone-invariant.

**Consumer note.** Combined with [[lem-disjointness-huddle-reduction]] this pins the
three-body anatomy that THE HUDDLE CHARGE (sketch v17) must contradict; the (ii) handle
pairs it with [[lem-bounded-alpha-forced-far-slab]] and [[conj-tall-bounded-alpha]].

**Rigour tier.** L5 (reviewer != author: fresh hostile codex VB2). NOT af-validated.
