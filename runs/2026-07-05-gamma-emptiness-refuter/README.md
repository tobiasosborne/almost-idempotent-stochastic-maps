# Run bundle: capped clean Γ-block refuter (arm G wave 15) — 2026-07-05

**Status: L3 bundle carrying an exact certified counterexample (T0).** Exact ℚ throughout.
Codex-worker-authored (prompt in the session scratchpad), **orchestrator-recomputed with fully
independent code** (see Invariant). Companion wave artifact:
`docs/waves/2026-07-05-W15-gamma-emptiness.md`.

## Hypothesis / adversarial question

Prove or refute `conj-gamma-emptiness` (unqualified capped Γ-emptiness): at every capped θ-half
Φ-argmin with maximal pivot `s`, no admissible pivot-removing row `j` has
`Ψ_j < Φ_s(U) ≤ Γ_j` (a "clean Γ-block").

## Headline finding

**REFUTED — the first-ever certified capped clean Γ-block.** Rank-3 exact signed idempotent
(6 rows, the insert-y skeleton extended by one row): `δ = 55319/1000000 ≈ 0.0553`; unique θ-half
Φ-argmin `U = (0,2,4)` (`m_U = 197/200`), maximal pivot `s = 2`,
`M = Φ_2(U) = 219870541/7880000000 ≈ 0.0279`; row `j = 1` has `|a_s(j)|·m_U = 1` (admissible) and
`Ψ_j = 1/200 < M ≤ Γ_j = 7/250`, margins `180470541/7880000000` and `769459/7880000000`.
Consequence: **G11's 0/352 was a search-coverage artifact**, not evidence of emptiness — and the
branch-restricted B-lemma's hypothesis class is NONEMPTY (this instance carries
`B_{1,2} = 42/985`, `B/δ ≈ 0.7708`).

## Honest scope

- Kills `conj-gamma-emptiness` as stated (unqualified). The refuting row `j = 1` is high-self
  (`P_11 = 203/400 > 1/2`), so narrowing by a high-self clause would NOT save the conjecture.
- The **proof-side residual** (worker T1, from the validated import chain + θ-half Cramer box):
  `M − Φ_r(U) ≤ 17·B_{r,s} + 16δ` (c>0) and `≤ 17·B_{r,s} + 20δ` (c<0) — so a branch-restricted
  B-lemma `B ≤ K·δ` yields the (PRT) collateral conclusion with `K_G = 17K + 20`. The missing
  ingredient is exactly the B bound; nothing else.
- Calibrations reconstructed: G10 witness (`δ = 49/60 > 1/4`, uncapped) and the G11 capped
  near-miss (Ψ-blocked, `Ψ − M = 22/125 > 0`).

## Command (re-run)

```bash
python3 runs/2026-07-05-gamma-emptiness-refuter/scripts/gamma_emptiness_cert.py    # worker cert
python3 runs/2026-07-05-gamma-emptiness-refuter/scripts/orch_verify_refuter.py    # independent check
```

## Invariant / known-value check

Worker script hard-asserts `B·L = I₃`, `P = L·B`, `P² = P`, row sums 1, `trace(P) = 3`, exact δ,
COMPLETE θ-half enumeration, unique argmin + maximal pivot, the pivot-removing chart values, the
clean-block inequalities, `A = B + C − D`, `C ≤ 2δ`, and the literal (CI) import values.
**Orchestrator recomputation (independent code, `scripts/orch_verify_refuter.py`):** rebuilds `P`
from `L, B`, independently re-derives coordinates (Cramer with reconstruction asserts), volumes,
the θ-half census, the unique argmin, `M`, admissibility, `Ψ_j = 1/200`, `Γ_j = 7/250`, the
clean-block inequalities and margins, and `B_{1,2} = 42/985`. Exit 0 = refutation confirmed.

## Next

`conj-gamma-emptiness` → `disproved` (this bundle is the death certificate). The recorded,
user-adopted fallback fires: the successor target is `conj-b-restricted` (branch-restricted
δ-financed B-lemma, `B_{r,s} ≤ K·δ` at capped argmins carrying a clean Γ-block), for which this
instance is the first certified member of the hypothesis class and the natural stress seed
(`K ≥ 0.7708` forced here; the wave-13 family law suggests `K ≥ 0.77764`).
