---
id: lem-sharp-vertex-visibility
kind: lemma
contract: Sharp-vertex visibility: for an exact signed idempotent P with delta(P) <= 1/4 and a row vertex v with dist_1(p_v, conv{p_j : p_j != p_v as vectors}) >= 4*sqrt(delta) (the hull of the geometrically distinct OTHER rows, assumed nonempty), v is (4*sqrt(delta), sqrt(delta)/4)-exposed.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: 
status: proved
af: none
provenance: W30 wave (docs/waves/2026-07-06-W30-w-nonemptiness.md): fresh-codex prover (worker T, the standalone criterion) + SEPARATE fresh-codex hostile verifier (VT, VALID-WITH-CORRECTIONS — pinned the hull to geometrically distinct other rows and flagged the singleton/empty-hull case as a separate convention, folded into the hypothesis here); first-principles ell1/ell-infty separation
owner: A
workspace: proofs/lem-sharp-vertex-visibility
---

**Role (a local exposedness certificate).** A vertex ℓ¹-isolated from all other rows by ρ is
automatically well-exposed: separation gives a linear ℓ with ‖ℓ‖_∞ ≤ 1 and gap ≥ ρ on the other
rows; g(x) = ℓ(p_v) − ℓ(x) has g(p_v) = 0, g ≥ ρ on other rows, g ≤ D on rows; normalizing by
max g gives an admissible exposer with margin ≥ ρ/D ≥ κ at δ ≤ 1/4 (VT re-derivation).
Complements [[lem-simplex-visibility]] (global hypothesis) with a per-vertex one; both are
bricks toward the OPEN dimension-free production theorem for Kernel(i).

**Honest limits (VT's corrections, folded into the contract).** The hull is over geometrically
DISTINCT other rows and is hypothesized nonempty (the one-distinct-row/singleton polytope case
is excluded here — trivially handled separately). No claim that sharp vertices exist; that
existence is the open production question.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
