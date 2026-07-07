---
id: lem-optimal-face-alpha-free-characterization
kind: lemma
contract: Optimal-face alpha-free characterization: for the exposedness LP at a hidden geometrically distinct row vertex v of an exact signed idempotent P with t*(v) > 0, let T be the set of rho-far constraints and O the set of upper box constraints that are tight on the WHOLE primal optimal face; then an optimal hiddenness dual witness with alpha = 0 exists if and only if conv{p_f - p_v : f in T} intersects t*(v) * conv{p_i - p_v : i in O}.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-hiddenness-dual-witness
status: proved
af: none
provenance: W43 wave (docs/waves/2026-07-07-W43-optimal-face.md): fresh-codex prover (worker AQ) + SEPARATE fresh-codex hostile verifier (VAQ, VALID — strengthened the dual-face step: ANY dual optimum complements EVERY primal optimum (the zero-sum complementarity identity term-by-term); the O-empty edge resolved (t* > 0 forces O nonempty for alpha-free witnesses); all four W41 certificate families recomputed exactly, incl. the exact residuals 100*d_1, 100*d_5, (25625/256)*d_6 and the success combination (59/123)d_0 + (64/123)d_1 = (1/41)d_2)
owner: A
workspace: proofs/lem-optimal-face-alpha-free-characterization
---

**Role (THE terminal node's exact geometry).** The residual-cancellation question (R = 0 on
the dual optimal face — the mechanism the certificates exhibit at tops, W41/W42) is EXACTLY a
convex-intersection condition on the always-tight far and upper displacement hulls. The
program's remaining Route-A content ((T1) of sketch v11) is: prove this intersection
nonempty, CLUSTER-UNIFORMLY, at tall heavy near-cluster tops — with the full rigorous toolkit
(collapse #17, concentration #19, pincer #21, witness #20, bridge #22) bearing on the
locations of T and O. Predicts every banked instance: intersection fails exactly at the
alpha-blow-ups, holds exactly where topness cancelled the residual.

**Honest limits.** Characterization only — proves nothing about tall regimes; and membership
in T/O is ALWAYS-TIGHTNESS on the whole optimal face (the W42 hard stop: near-zero values do
not certify membership).

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous; PRIME af-elevation candidate.
