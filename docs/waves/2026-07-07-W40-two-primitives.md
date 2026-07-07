# Wave W40 — the two primitives: the alpha gauge solved, the blow-up REALIZED, the capacity threshold general (2026-07-07, session 11)

**Node:** conj-near-cluster-absorption's two primitives (W39 reduction), bd `aism-2fi` (P0).
**Design:** two independent fresh-codex provers — AJ (alpha gauge) ∥ AK (primal exposer) — +
ONE SEPARATE fresh hostile verifier VAL over both. Prompts + raw answers in the session-11
scratchpad (`W40/`). Paper wave (VAL's exact fixture work scratch-only; the blow-up instance
is printed verbatim in the obs shard).

## Verdicts (verbatim first lines)

- Worker AJ: `PARTIAL (alpha-gauge: exact zero-face conic gauge; alpha=0 under a clean
  zero-face condition; no δ/τ-only bound from LP structure)`
- Worker AK: `PARTIAL (feasibility condition: the v-circuit permits a kappa-margin exactly
  when the target far-positive v-mass B satisfies kappa*B <= nu_v; gap: this only satisfies
  the v row equation, while full affine realizability is blocked exactly by the hiddenness
  witness circuits for the candidate cluster vertex)`
- Verifier VAL: `VALID-WITH-CORRECTIONS (AJ-G quantifier; AJ-O is actually realizable; AK-C
  needs row-local/free-anchor hypotheses; AK-D is just LP duality)`

## Results

1. **`lem-zero-face-alpha-gauge` (codified).** Minimal witness alpha = the zero-face conic
   gauge of the tangential residual (quantifier over optimal (h*, lambda, beta) — VAL's fix);
   clone-only zero faces give alpha-free witnesses; A_min = 0 on all banked fixtures.
2. **`obs-realized-alpha-blowup` (codified, kind: obstruction) — VAL's STRENGTHENING:** the
   thin-zero-face blow-up IS realizable as an exact signed idempotent (explicit 4x4, delta =
   eps, hidden v, A_min = 1/eps; exact recomputation at eps = t = 1/100). LP-only alpha
   bounds are DEAD; tall-cluster alpha control must consume extra structure (note: the
   alpha-slab leakage bound controls alpha OFF the top slab in tall regimes; the blow-up
   alpha sits ON the zero face — whether blow-up survives the tall heavy-cluster hypotheses
   is the NEW decider).
3. **`lem-row-zero-capacity` (codified).** The general W36 capacity threshold: any admissible
   harmonic candidate vanishing at row i pays kappa*(F-mass) <= nu_i. The row-local converse
   holds under free-anchor compatibility; a FULL exposer construction is equivalent (LP
   duality, AK-D — near-definitional, not codified) to non-hiddenness.
4. **The terminal fork after W40 (sketch v10):** near-cluster absorption now = EITHER
   (i) tall-cluster alpha control (does the realized blow-up coexist with H > 13-ish tau +
   heavy near cluster? — a prove-or-refute decider with exact certificates either way), OR
   (ii) a non-witness-aggregation finisher (the capacity threshold + cancellation ledger
   route, priced but unassembled).

## Banking (orchestrator)

Registry: the three shards (VAL as reviewer; the blow-up instance printed in the obs shard —
[T0] facts, verifier-recomputed). FINDINGS + sketch v10 at the round close. Honest tiers:
reviewed (L5); NOT L0; the conjecture remains OPEN with the fork above.
