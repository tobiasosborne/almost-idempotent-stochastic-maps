---
id: cor-rank-two-visible
kind: corollary
contract: Rank-two visibility: every exact signed idempotent P with rank(P) <= 2 and delta(P) <= 1/4 has W(P) nonempty.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-simplex-visibility
status: proved
af: none
provenance: W30 wave (docs/waves/2026-07-06-W30-w-nonemptiness.md): fresh-codex prover (worker T) + SEPARATE fresh-codex hostile verifier (VT, VALID — affine-rank argument expanded: rows lie in the rank-r row space intersected with the row-sum-1 hyperplane, affine dimension <= r-1, and a point/segment is a simplex on row vertices; exact rank-2 signed fixture delta=1/16 checked)
owner: A
workspace: proofs/cor-rank-two-visible
---

**Role.** Kernel(i) (W-nonemptiness) holds unconditionally at rank ≤ 2 and δ ≤ 1/4, via
[[lem-simplex-visibility]] on the point/segment row polytope. The first rank stratum of the
open production theorem; rank ≥ 3 (non-simplex polytopes) remains OPEN.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
