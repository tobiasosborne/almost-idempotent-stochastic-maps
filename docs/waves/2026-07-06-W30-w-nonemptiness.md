# Wave W30 — W-nonemptiness (Kernel(i)): first bricks + the anchor obstruction (2026-07-06, session 11)

**Node:** sketch v7 ledger item 6 (W-nonemptiness — consumed by conj-kernel(i) and, since W27/W28,
an explicit hypothesis of the reviewed conditional chain), bd `aism-jwg`. **Design:** mutually-blind
prove/refute pair (worker T prove ∥ worker U refute) + SEPARATE fresh hostile verifier VT on T's
claims. Prompts + raw answers in the session-11 scratchpad (`W30/`); U's exact audit script
recovered verbatim into `runs/2026-07-06-w30-w-nonemptiness/scripts/`.

## Verdicts (verbatim first lines)

- Worker T: `PARTIAL (proved: δ=0 endpoint, and δ≤1/4 W-nonemptiness when the row polytope is a
  simplex, in particular affine dimension ≤1 / rank≤2; gap: no dimension-free mechanism found
  forcing a simplex/sharp vertex from P²=P and small δ)`
- Worker U: `NOT-REFUTED (searched: exact audits + 297 admissible random Lambda-C idempotents;
  sharpest obstruction: hiddenness forces a far-row barycenter near each hidden vertex, and all
  constructions needed visible anchors for that barycenter)`
- Verifier VT: `VALID-WITH-CORRECTIONS (S and R valid as stated; V valid when
  `conv{p_j:p_j != p_v}` means geometrically distinct other rows, with singleton-polytope handled
  separately/vacuously)`

## Results

1. **`lem-simplex-visibility` (codified, proved/af:none).** Simplex row polytope on row vertices +
   δ ≤ 1/4 ⇒ every row vertex visible (barycentric exposer; margin ρ/D ≥ κ). VT: ambient affine
   extension harmless; duplicates handled; exact fixtures.
2. **`lem-sharp-vertex-visibility` (codified, proved/af:none, VT's corrected form).** A vertex
   ℓ¹-isolated by ρ from the distinct other rows is visible (separation + normalization).
3. **`cor-rank-two-visible` (codified, proved/af:none).** rank ≤ 2 + δ ≤ 1/4 ⇒ W nonempty.
4. **The refuter's structural diagnosis (worker U, T1-worker + exact audits):** every hidden
   vertex needs a far-row barycenter (the W26 witness), and in EVERY construction those
   barycenters leaned on VISIBLE anchors; 297 exact random audits, `found_W_empty=False`;
   symmetrized families turn all-visible before W can empty. **Blind convergence with T's named
   gap and with W26: the candidate mechanism for the missing dimension-free production theorem
   is "an empty W leaves every hiddenness witness anchorless".** That is the next
   W-nonemptiness wave's target (assume W = ∅, apply the witness at an extremal vertex, derive
   a contradiction).

## Banking (orchestrator)

Registry: the three shards above (VT as independent reviewer). Bundle:
`runs/2026-07-06-w30-w-nonemptiness/` (U's script + README; bounded search is L3 evidence, NO
emptiness claim). Kernel(i) ledger effect: unconditional at δ=0 (W28), at rank ≤ 2 (this wave);
OPEN at rank ≥ 3 with a named candidate mechanism. Honest tiers: reviewed paper proofs (L5);
NOT af-validated, NOT L0-rigorous.
