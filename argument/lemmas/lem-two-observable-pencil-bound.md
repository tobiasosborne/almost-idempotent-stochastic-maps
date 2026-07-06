---
id: lem-two-observable-pencil-bound
kind: lemma
contract: Two-observable pencil bound: for an exact signed idempotent P, a hidden row vertex v (per def-exposed, with a full hiddenness dual witness (lambda, alpha, beta) as in lem-hiddenness-dual-witness), and ANY affine F with F(p_v) = 0 and 0 <= F(p_j) <= E on all rows with E > 0, one has sum over f in F_v of lambda_f * F(p_f) < (tau/4)*E and sum over j of max(P_vj, 0) * F(p_j) <= nu_v * E.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-hiddenness-dual-witness
status: proved
af: none
provenance: W33 wave (docs/waves/2026-07-07-W33-harmonic-affine-bridge.md): fresh-codex prover (worker AA) + SEPARATE fresh-codex hostile verifier (VAA, VALID-WITH-CORRECTIONS — lambda must come from a full witness tuple; exact nontrivial fixture check on the W29 frontier instance, both inequalities, the second with EQUALITY); unifies the pairing (lem-hiddenness-depth-markov's engine) and the CS pincer (lem-cs-low-slab-pincer) over the whole admissible affine pencil
owner: A
workspace: proofs/lem-two-observable-pencil-bound
---

**Role (the pencil form of both coupling channels at once).** Every admissible affine F
(in particular every member of the (ψ, g_v − g) pencil, affine by
[[lem-harmonic-affine-bridge]]) satisfies BOTH: the witness-side bound (λ-average < κE — the
depth-Markov engine at F = ψ) and the coefficient-side bound (P_v⁺-weighted average ≤ ν_v E —
the CS pincer). The coupling question is exactly whether some F separates the two measures;
this shard is the clean interface for optimizing over the pencil (a 2-variable LP per
configuration, worker AA's formulation).

**Honest limits.** Both bounds point the SAME way (small on the witness side, small on the
coefficient side at high F) — no infeasibility from the pencil alone (worker AA [T2],
VAA-confirmed); the low slab remains uncontrolled.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
