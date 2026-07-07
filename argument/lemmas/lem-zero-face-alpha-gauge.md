---
id: lem-zero-face-alpha-gauge
kind: lemma
contract: Zero-face alpha gauge: for an exact signed idempotent P and a hidden row vertex v with t*(v) > 0 and nonempty rho-far set, the minimum of sum_i alpha_i over all optimal hiddenness dual witnesses equals the minimum, over optimal exposers h* and optimal active (lambda, beta), of the conic-gauge value min{sum_i a_i : a_i >= 0, sum over {i : h*(p_i) = 0} of a_i*(p_i - p_v) = R(lambda, beta)}, where R(lambda, beta) is the tangential residual of the balance equation in ker h*; in particular, if {i : h*(p_i) = 0} contains only v and its geometric clones for some optimal h*, then an alpha-free optimal witness exists.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-hiddenness-dual-witness
status: proved
af: none
provenance: W40 wave (docs/waves/2026-07-07-W40-two-primitives.md): fresh-codex prover (worker AJ) + SEPARATE fresh-codex hostile verifier (VAL, VALID-WITH-CORRECTIONS — the quantifier fixed: the global minimum ranges over optimal (h*, lambda, beta), not a fixed active set; complementary-slackness geography re-derived: alpha lives ON the zero face, beta on the one-face, lambda on the t*-level; exact A_min = 0 recomputation on both W29 hidden rows)
owner: A
workspace: proofs/lem-zero-face-alpha-gauge
---

**Role (the witness's free ray, exactly priced).** The alpha family of
[[lem-hiddenness-dual-witness]] is objective-free; this shard pins its minimal size to a
conic-gauge problem on the optimal exposer's zero face. Consequences: clone-only zero faces
give alpha-free witnesses (ALL banked fixtures have A_min = 0); but the gauge can blow up —
see [[obs-realized-alpha-blowup]] (an exact idempotent with A_min = 1/eps). Aggregation
arguments (W39-AI) are unblocked EXACTLY where the zero face is clone-only or the residual
vanishes; any tall-cluster alpha control must add structure beyond LP duality.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
