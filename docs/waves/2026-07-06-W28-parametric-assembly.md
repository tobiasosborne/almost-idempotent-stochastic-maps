# Wave W28 — the parametric assembly codified: conj-min-a-w4 ⇒ H ≤ 13τ, + the δ=0 endpoint (2026-07-06, session 11)

**Node:** sketch v6 ledger items 8 (δ=0 endpoint, [short]) and 9 (D1 codification re-aimed at the
parametric form, B = 13), bd `aism-yxa` (re-aimed 2026-07-06). **Design:** pure-derivation pair —
fresh codex prover S + SEPARATE fresh hostile verifier VS (byte-faithfulness of imported contracts
explicitly checked). Prompts + raw answers in the session-11 scratchpad (`W28/`).

## Verdicts (verbatim first lines)

- Worker S: `PROVED (A+B, B = 13)`
- Verifier VS: `VALID (both; hypotheses as listed)`

## Results

1. **`lem-min-a-implies-height` (codified, proved/af:none).** Assuming `conj-min-a-w4`, every
   exact signed idempotent P with 0 < δ ≤ (17−12√2)/2 and W(P) nonempty has H(P) ≤ 13τ.
   Mechanism: if H > 13τ, every hidden top has H(1−σ₄) ≤ (13/2)τ — via
   σ − σ₄ ≤ 1 + ν (lem-mass-split; G₄ ⊆ invisible set needs only τ > 0), ν ≤ δ,
   δ(2+4δ) ≤ (3/2)τ (sharp at τ = 1/2) — so σ₄ ≤ 1/2 would give H ≤ 13τ; hence every hidden top
   has σ₄ > 1/2, contradicting the conjecture's "some hidden top has σ₄ ≤ 1/2". No division;
   σ₄ ≥ 1 branch explicit. VS: contracts byte-faithful; σ₄ identical functional in both shards;
   0 < δ₁ < 1/4 exact (289 > 288, 1089 < 1152); exact fixture check on the banked rank-5
   (H(1−σ₄) intermediate inequality verified by exact squaring).
2. **`lem-delta-zero-endpoint` (codified, proved/af:none).** Every exact signed idempotent with
   δ(P) = 0 has W(P) nonempty and H(P) = 0, UNCONDITIONALLY. At τ = 0 the far set includes v
   itself, every admissible exposer has minimum exactly 0, and def-exposed's test is
   t*(v) ≥ κ = 0 — all row vertices visible; rows lie in conv of the distinct row vertices.
   VS confirmed the ≥-vs-> convention from the shard text and checked a δ=0 3×3 fixture.
   (Definition-sensitivity kept loud: the statement rides on the non-strict ≥ in def-exposed.)
3. **Chain effect (sketch).** With W22's `lem-kernel-implies-hlc` and W27's
   `lem-hlc-implies-exposed-hull`, Route A's conditional spine is now fully reviewed:
   `conj-min-a-w4 ⇒ H ≤ 13τ` (this wave) gives the Kernel height clause at B = 13 for
   δ ≤ δ₁ MODULO W-nonemptiness (attacked independently in W30). No claim that conj-min-a-w4
   or the Kernel Conjecture is proved.

## Banking (orchestrator)

Registry: `lem-min-a-implies-height` (deps conj-min-a-w4, lem-parametric-halo-collapse,
lem-mass-split), `lem-delta-zero-endpoint` (deps none). Honest tiers: reviewed paper proofs (L5);
NOT af-validated, NOT L0-rigorous; conditional-on-conjecture status carried by the dep edge,
exactly as lem-kernel-implies-hlc carries conj-kernel.
