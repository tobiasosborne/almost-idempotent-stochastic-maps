# Run bundle: B/δ amplifier hunt at certified argmins (arm G wave 13, amplifier branch) — 2026-07-04

**Status: L3 numerical evidence. NEVER rigorous.** Exact ℚ for every certified quantity
(`fractions.Fraction`). Codex-worker-authored (prompt in the session scratchpad), orchestrator-recomputed
(see Invariant). Companion to the wave artifact `docs/waves/2026-07-04-G13-b-amplifier.md` and the prover
harvest `docs/waves/2026-07-04-G13-b-lemma-conditional.md`.

## Hypothesis / adversarial question

Push `sup B/δ` at CERTIFIED capped θ-½ Φ-argmins carrying a clean high-self non-fan Γ-branch. Graded
targets: (i) beat the decider-#2 record `8400000/10897843 ≈ 0.771`; (ii) reach/cross `1`; (iii) compare
`B` against the literal (CI)-financed total and the G12 pivot-s budget terms.

## Command (re-run)

```bash
python3 runs/2026-07-04-b-amplifier-hunt/scripts/amplifier_wave13.py
```

Deterministic; regenerates `data/certified_points.{csv,json}` + `data/ANSWER.md`. Worker's script with
one mechanical re-home patch (output dir → `data/`).

## Invariant / known-value check

Script HARD-ASSERTS the two calibrations (G12: `δ=1/4, B=2/57`; decider-#2 maximizer:
`δ=55319/1000000, B=42/985`) and per-point `BL=I`, `P²=P`, row sums, complete chart enumeration.
**Orchestrator recomputation (independent code):** for the record instance, re-derived `P²=P`, row sums,
`δ = 590855669597640985598471/10775740230179796072754000`, the θ-half census (8 charts), the exact
two-chart argmin TIE `{(0,1,3),(0,2,4)}`, and `B = 42/985` with
`B/δ = 90516217933510287011133600/116398566910735274162898787 ≈ 0.77764` — all match.

## Finding (headline + honest scope)

1. **New record, tiny margin, and an apparent LAW:** best certified `B/δ ≈ 0.77764` (up from 0.771). The
   compensated-insert family has an exact switch boundary (`y* = 2679363/39161780`; variable-row law
   `y = 2679363/(49000(22a+799))`), and the family's limiting `B/δ` is an ALGEBRAIC number
   `≈ 0.777640312383967` attained at an irrational row-loss balance — certified rational points approach
   it from both sides. `sup B/δ` in this family is ≈ 0.7776, **well below 1** (target (ii): NO).
2. **Cloning does not amplify** (n=7/9 duplicate inserts reproduce the same ratio — consistent with
   clone-invariance); extra-carrier and rotated-bridge probes LOSE the clean Γ-branch (Ψ/mixed or
   low-self) — obstructions, not records.
3. **`B` is not covered by the existing budgets:** at the record point `B` exceeds the literal
   (CI)-financed total (`B − (Φ_r+I) = 637/49250 > 0`) and the G12 pivot-s budget terms by factor
   `≈ 4.24` (`B/budget = 122028518735365200000/28788997641448048423`), extending the kill-test's 1.82.
   **Orchestrator correction (do not over-read):** the wave prompt's target (iii) called this a skeleton
   kill — that was MIS-SPECIFIED; the skeleton bounds `I` BY `B` (import reduction), so this crossing
   does not break the chain. Its true content: the B-term requires its OWN δ-scale financing (the
   NSC / `aism-z98` shape) — none of the existing budget terms can absorb it.
4. **Scope limits (honest):** compensated-insert boundary analysis + rational approximants to one
   algebraic balance + duplicate inserts + small extra-carrier/rotated-bridge sets; 9 certified points;
   NOT an exhaustive rank-3 search; the 0.7776 "law" is family-specific — richer families could exceed
   it (nothing here bounds `sup B/δ` in general).

## Next

The B-lemma now lives at NSC(K0) (`docs/waves/2026-07-04-G13-b-lemma-conditional.md`, review-approved):
prove `B ≤ K0·Σ_carriers β⁺ν` — a self-support/row-negativity principle, NOT a chart-move comparison
(all certified B-mass is volume-inadmissible). Empirical K0 across all certified data ≈ 2.8; the record
instance here is the sharpest stress case. Amplification follow-up only if NSC resists: hunt families
where the carrier row-negativity ν_i is starved relative to B (the NSC refuter shape).
