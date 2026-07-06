---
id: lem-delta-zero-endpoint
kind: lemma
contract: Delta-zero visible endpoint: every exact signed idempotent P with delta(P) = 0 has nonempty visible set W(P) and H(P) = 0.
defs: def-signed-idempotent; def-visible-set; def-exposed; def-height
deps: 
status: proved
af: none
provenance: W28 wave (docs/waves/2026-07-06-W28-parametric-assembly.md): fresh-codex prover (worker S, part B) + SEPARATE fresh-codex hostile verifier (VS, VALID — confirmed the non-strict >= convention from the def-exposed shard text and a delta = 0 3x3 fixture); sketch v6 ledger item 8 (the delta = 0 endpoint), previously [short, unassembled]
owner: A
workspace: proofs/lem-delta-zero-endpoint
---

**Role (the assembly's unconditional endpoint).** Closes the delta = 0 corner of the
cap => Kernel assembly: at delta = 0 (exactly stochastic idempotents, per def-signed-idempotent)
both Kernel clauses hold trivially — W nonempty and every row at height 0. Together with
[[lem-min-a-implies-height]] this makes W-nonemptiness at 0 < delta <= delta_1 the ONLY
remaining assembly gap below [[conj-min-a-w4]].

**Proof shape (worker S, T0; VS).** At delta = 0: tau = rho = kappa = 0. The far set
{j : ||p_j - p_v||_1 >= 0} is ALL rows, including v itself, so every admissible exposer
(h(p_v) = 0, 0 <= h <= 1) has minimum exactly 0 over it; def-exposed's test is t*(v) >= kappa = 0,
which holds. Hence every geometrically distinct row vertex is visible and W(P) is their full
(nonempty) set; every row lies in conv of the distinct row vertices = conv W, so H(P) = 0.

**Definition-sensitivity (kept loud).** The statement rides on def-exposed's NON-STRICT >= in
the visibility test; a change to strict > would break it (FINDINGS 2026-07-06 W28). Do not cite
this endpoint after any def-exposed revision without re-deriving.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
