---
id: lem-wedderburn-deflation
kind: lemma
contract: Wedderburn deflation: for an exact signed idempotent P and any probability row vector mu, the vector nu = mu*P satisfies nu*P = nu and nu*1 = 1, and D = P - 1*nu satisfies D^2 = D, D*1 = 0, and rank(D) = rank(P) - 1 (no further hypothesis; im(D) = im(P) intersect ker(nu)); trace(P) = rank(P) over the reals, and both are invariant under weighted clone lifts; for nu = p_v, every affine exposer value vector h with h(p_v) = 0 satisfies D h = h; deflation at p_v translates rows by -p_v, so a rho-near cluster maps to rows of l1-norm < rho and far rows to norm >= rho.
defs: def-signed-idempotent; def-exposed; def-visible-set
deps: lem-harmonic-affine-bridge
status: proved
af: none
provenance: W48 wave (docs/waves/2026-07-07-W48-mechanism-bricks.md; ideation candidate 4, re-derived independently): fresh-codex prover (worker BB — no added rank hypothesis needed: P1 = 1 puts the fixed line in im(P) and nu(1) = 1 keeps nu nonzero on it; weighted clone lift L(P)_ab = P_{pi(a),pi(b)} w_b with fiber weights summing to 1) + SEPARATE fresh-codex joint hostile verifier (VBW, VALID — rank argument, trace/rank, exposer fixedness, clone invariance all confirmed; clone clause requires the weighted fiber model, noted as a CONVENTIONS gap)
owner: A
---

**Role (reformulation lever).** The exposedness LP at v is exactly the fixed-vector box
program of the deflated rank-(r-1) idempotent whose v-row is zero; trace = rank is the one
exact global clone-invariant. NOTE (definitional hygiene): the weighted clone lift is used
here but lives only in ingest/wave notes, not CONVENTIONS.md — flagged, not silently adopted.
