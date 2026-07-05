# Run bundle: broad-NSC zero-denominator refuter (decision-check DC2, wave 14 refute side) — 2026-07-05

**Status: L3 numerical/exact-certificate evidence — the REFUTATION itself is an exact certified
counterexample (T0).** Exact ℚ throughout (`fractions.Fraction`). Codex-worker-authored (prompt in
the session scratchpad), **orchestrator-recomputed with fully independent code** (see Invariant).
Companion wave artifact: `docs/waves/2026-07-05-DC2-nsc-ratio-search.md`.

## Hypothesis / adversarial question

First-ever search with the NSC ratio `R = B_{r,s} / Σ_{carriers} β_r(i)⁺ν_i(P)` as the DIRECT
objective (all prior sweeps optimized `B/δ` or `B`/budget), over ν-starved and multi-carrier
families, hunting either `R → ∞` or the zero-denominator mode `B > 0` with `Σ_carriers = 0`.

## Headline finding

**The broad form of `conj-nsc` is REFUTED — zero-denominator mode.** Exact rank-3 signed
idempotent (5×5), two-carrier family parameters `(1/200, 1/100, 0, 1/200, 20099999/20200500,
1/1000)`: `δ = 20099999/4040100000 ≈ 0.004975 ≤ 1/4`; UNIQUE θ-half Φ-argmin `U = (0,3,4)` with
`Φ = (0,0,0)`; at `s = 0`, `r = 1`: `B_{1,0} = 1/4020000000 > 0` while the ONLY carrier (row 1,
`β = 40399/4020000000 > 0`, `a_0 = −1/40399 < 0`, volume-inadmissible) is **entrywise nonnegative
in the ambient idempotent** (`ν_1 = 0`), so the charging target `Σ_carriers β⁺ν` is exactly `0`.
A three-carrier variant with the same property is also certified. Along the wave-13 amplifier
boundary family the ratio stays ≈ 1.129 — the amplifier family is NOT the NSC stress.

## Honest scope

- Kills ONLY the broad charging shape (`B` against carrier-ν). The refuting `B` is ≈ 2.5e-10 —
  astronomically below `δ` — and the argmin carries `Φ ≡ 0` (no leaking rows, hence no clean
  high-self non-fan Γ-branch), so the **branch-restricted B-lemma target (`B ≤ K·δ`) is untouched**
  and the (PRT) skeleton regime (where `M = Φ_s(U) > 0`) is not entered.
- Structural content: **chart-negativity of a carrier requires NO ambient negativity on that row,
  even AT a certified argmin** — the G6 decoupling warning, previously known only away from the
  argmin mechanism, is realized at an argmin.
- Known witnesses reconstructed and hard-asserted (K0 ratios 200000000/175088281, 50000/17919,
  9/4); full per-pair table in `data/nsc_pair_table.csv`.

## Command (re-run)

```bash
python3 runs/2026-07-05-nsc-zero-denominator-refuter/scripts/nsc_ratio_search.py   # worker search+asserts
python3 runs/2026-07-05-nsc-zero-denominator-refuter/scripts/orch_verify_refuter.py  # independent check
```

## Invariant / known-value check

Worker script hard-asserts, for every reported matrix: `B_left·L = I₃`, `P = L·B_left`, `P² = P`,
row sums `1`, `0 < δ ≤ 1/4`, complete exact chart enumeration, and the three known witness ratios.
**Orchestrator recomputation (independent code, `scripts/orch_verify_refuter.py`):** takes ONLY
the `P` matrix from `data/nsc_certificates.json` and independently re-derives coordinates (with
all-column reconstruction asserts), chart volumes, the θ-half census (4 charts), the unique argmin
`(0,3,4)` with `Φ = (0,0,0)`, `B_{1,0} = 1/4020000000`, the single carrier `i = 1` with `ν₁ = 0`
(row entrywise nonnegative), and `Σ_carriers = 0`. Exit 0 = refutation confirmed.

## Next

Successor shape for the K⟨1⟩5 mechanism is a USER decision (escalated at session 8): (a)
branch-restricted NSC (charge only at argmins carrying a clean high-self non-fan Γ-branch — no
certified instance of the hypothesis class exists yet), (b) direct branch-restricted B-lemma
`B ≤ K·δ` with its own δ-financing (the aism-z98 shape), or (c) capped (G)-emptiness. The
`conj-nsc` shard is flipped to `disproved` with this bundle as the death certificate.
