---
id: lem-bounded-alpha-top-slab-reduction
kind: lemma
contract: Bounded-alpha top-slab reduction: for an exact signed idempotent P with delta(P) > 0, nonempty visible set W(P), a hidden top vertex v of height H with top support functional phi (phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz), a hidden row vertex u with ||p_u - p_v||_1 < 4*tau (tau = sqrt(delta)), and any hiddenness dual witness (lambda, alpha, beta) of u with A = sum_i alpha_i <= A0 and B = sum_i beta_i < tau/4, writing z_i = H - phi(p_i), one has sum over f in F_u of lambda_f * z_f < tau*((1/2 + delta) + 4*(1 + A0)); consequently for every c > 0, the lambda-mass on {f : z_f > c*tau} is at most ((1/2 + delta) + 4*(1 + A0))/c.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-hiddenness-dual-witness
status: proved
af: none
provenance: W42 wave (docs/waves/2026-07-07-W42-terminal-questions.md): fresh-codex prover (worker AP) + SEPARATE fresh-codex hostile verifier (VAO, VALID-WITH-CORRECTIONS — the centered pairing is an EQUALITY needing no nonnegativity of z - z_u; the inequality uses only 0 <= z_i <= D; the constant D/4 = 1/2 + delta made explicit)
owner: A
workspace: proofs/lem-bounded-alpha-top-slab-reduction
---

**Role (what bounded-alpha cheap witnesses of cluster vertices must look like).** Pairing a
cluster vertex u's witness with the TOP's deficit functional (centered at u) confines the
witness's lambda-mass to the global top slab up to the alpha budget: cheap witnesses of
near-top vertices live on deep far rows OF THE SAME tall structure. This is the graph-building
half of the primal conversion — the missing half is the cluster-UNIFORM alpha bound
(FINDINGS 2026-07-07 W42: [[conj-tall-zero-face-radial-thickness]] controls only v's own
datum) or the row-to-circuit absorption bridge.

**Honest limits.** Conditional on A <= A0 (unbounded in general — [[obs-realized-alpha-blowup]]);
a top-slab confinement, NOT a starvation/exposure statement.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
