# w42_factor_audit — HOSTILE AUDIT of the w41_ex FACTORIZATION LEMMA

**VERDICT: FACTORIZATION CONFIRMED (constants a=2, b=6).**
For any actual-row basis `U` in the theta-1/2 class of a row-stochastic exactly-idempotent `P`
(row negative masses `<= delta`), and any pivot `s`:
`S*_s(U) <= 2 Phi_s(U) + 6 delta(P)`.
Every line of the codex proof (`experiments/out/w41_ex/proof.md`) reproduces under independent
re-derivation; the constants `(2,6)` are exactly right (each is individually tight at the box
edge / overshoot edge, so neither can be lowered by this argument). The composition
`C_sf = 2*C0 + 6` is a clean quantifier step with no slip. **(EX) at rank 3 remains open and is
correctly tagged open by w41 — it is NOT part of this audit's CONFIRMED verdict.**

Calibrated: **P(factorization S* <= 2 Phi + 6 delta correct) = 0.99**;
**P(composition C_sf = 2 C0 + 6 correct) = 0.99**. (Residual 0.01 each = the standard risk that
the upstream *definitions* of `S*`, `Phi`, the box, and `SF<=S*` carry a hidden convention slip;
the factorization GIVEN those definitions is essentially certain — it is a finite sign-case
identity I reproduced symbolically.)

---

## 0. What was audited and how (independence)

I audited **the proof line by line**, not just the codex numerics. I re-derived every step from
the prompt's definitions and wrote my OWN metric code and my OWN idempotent generators
(`falsify.py`, `families.py` import only the campaign family *constructors*, never the codex
metric/explorer logic). Scripts in this directory:

| script | what it checks |
|---|---|
| `pointwise.py` | the pointwise estimate `g <= E + 2 lambda_+` by exhaustive sign casework |
| `aggregation.py`, `aggregation2.py` | the `(DEF)` decomposition `Dpos = V + Dneg` and the `Dneg <= 3 delta` box bound (incl. a sign-convention trap I fell into and corrected) |
| `stepB.py` | `V <= Phi/2` via `2(-lambda)_+ <= E` pointwise |
| `falsify.py` | independent generator: 385 nontrivial exact idempotents, 0 violations |
| `families.py` | all named campaign families run through INDEPENDENT metrics, **every** intermediate step (i)-(vi) checked per chart/pivot |
| `composition.py` | the argmin/quantifier step and the selected-chart contract (325 instances, 0 violations) |
| `overshoot_hunt.py` | adversarial windmill + heavy-overshoot search (the w38 failure mode), 0 violations |

---

## 1. Re-derivation from scratch (the proof IS correct)

Notation (prompt): `lambda(j) = 1 - a_s(j)`, `sigma(j) = sum_{t!=s} (a_t(j))_+`,
`mu(j) = sum_{t!=s} (a_t(j))_-`, `E(j) = (sigma - 2 lambda)_+` (`= (mu - lambda)_+` via
`lambda = sigma - mu`), `beta(j) = P_{u_s j}`, `Phi_s = sum beta_+ E`,
`V_s = sum beta_+ (-lambda)_+`, `S+_s = sum beta_+ sigma`, `S*_s = S+_s + 2 V_s`.

**Reformulation (identity).** Put `g(j) = sigma(j) + 2(-lambda(j))_+`. Then
`sum beta_+ g = sum beta_+ sigma + 2 sum beta_+ (-lambda)_+ = S+_s + 2 V_s = S*_s`. ✓ exact
(`families.py` step (i): `S* = sum beta_+ g` holds on every instance).

**Step 1 — pointwise `g <= E + 2 lambda_+`.** (`pointwise.py`) Exhaustive sign split, with the
coupling `lambda = sigma - mu` enforced:
- `lambda < 0`: `E = sigma - 2 lambda = sigma + 2(-lambda) = g`, `lambda_+ = 0` ⇒ `RHS - g = 0` (equality).
- `lambda >= 0, sigma >= 2 lambda`: `E = sigma - 2 lambda`, `g = sigma` ⇒ `RHS - g = (sigma-2lam)+2lam-sigma = 0` (equality).
- `lambda >= 0, sigma < 2 lambda`: `E = 0`, `g = sigma < 2 lambda` ⇒ `RHS - g = 2 lambda - sigma > 0` (strict slack).

So `S*_s = sum beta_+ g <= sum beta_+ E + 2 sum beta_+ lambda_+ = Phi_s + 2 Dpos_s`,
`Dpos_s := sum beta_+ lambda_+`. ✓ (matches proof.md lines 70-89).

**Step 2 — `(DEF)` decomposition `Dpos = V + Dneg`.** (`aggregation2.py`) From
`beta = beta_+ - bm` (`bm = (-beta)_+`) and `lambda = lambda_+ - lambda_-`:
`0 = sum beta lambda = sum beta_+ lambda_+ - sum beta_+ lambda_- - sum bm lambda
   = Dpos - V - Dneg`, with `Dneg := sum bm(j) lambda(j)`.
Hence `Dpos = V + Dneg`. ✓ (numeric identity verified over 3000 random points; my FIRST
script `aggregation.py` had a Dneg sign flip and "failed" — I traced it to my own convention
error, NOT the proof; corrected version confirms the proof's algebra exactly).

**Step 3 — `V <= Phi/2`.** (`stepB.py`) On rows where `(-lambda)_+ > 0` we have `lambda < 0`,
so `sigma >= 0 >= 2 lambda` ⇒ `E = sigma + 2(-lambda) >= 2(-lambda)_+`. Pointwise
`2(-lambda)_+ <= E` (slack `= sigma`), hence `V = sum beta_+ (-lambda)_+ <= (1/2) sum beta_+ E = Phi_s/2`. ✓

**Step 4 — `Dneg <= 3 delta`.** (`aggregation2.py`) `Dneg = sum bm(j) lambda(j)`, with `bm >= 0`,
`sum bm = nu_{u_s} <= delta` (negative mass of pivot row), and the **theta-1/2 box**
`|a_t(j)| <= 2` ⇒ `lambda = 1 - a_s in [-1, 3]`. Upper bound: `Dneg <= sum bm * 3 = 3 nu_{u_s} <= 3 delta`. ✓
The proof uses **`lambda <= 3`** here (the correct edge — the prompt's hint about the `[-1,3]`
range). It does NOT use `lambda_+ <= 2` anywhere; the only place a box bound enters is this
`lambda <= 3` upper cap, and it is used correctly.

**Combine:** `Dpos = V + Dneg <= Phi_s/2 + 3 delta`, so
`S*_s <= Phi_s + 2 Dpos <= Phi_s + Phi_s + 6 delta = 2 Phi_s + 6 delta`. ∎

**Constants tightness.** `a = 2` is forced by Step 1 (`+2 Dpos`) combined with Step 3's `V <= Phi/2`
(factor 2 in `2*Phi/2 = Phi`, plus the original `Phi`). `b = 6 = 2 * 3` is forced by `2 * (lambda<=3)
* (mass<=delta)`. Both edges are attainable (overshoot rows with `sigma=0`, `lambda` at the box
extremes), so this argument cannot improve `(2,6)`. The codex's self-assessed P=0.995 is reasonable;
I rate 0.99.

### The cautionary cross-check (w38 history) — PASSED
The w38 refutation killed `(SIG)` "`E <= sigma`" because at theta=1/2 **overshoot rows have
`E = sigma + 2|lambda| > sigma`**. The w41 factorization does the OPPOSITE: it *keeps* the
`+2|lambda|` term (that is exactly `g`), bounds it via `E` (Step 1) and the deficit identity
(Steps 2-4). So the very term that broke w38 is the term this proof correctly carries. No
recurrence of the w38 error.

---

## 2. Adversarial corner cases (all PASS)

`families.py` runs every named family through INDEPENDENT metrics and checks **each** of (i)
`S*=Σβ+g`, (ii) `g<=E+2λ+`, (iii) `Dpos=V+Dneg`, (iv) `V<=Φ/2`, (v) `Dneg<=3δ`, (vi) `S*<=2Φ+6δ`:

| family | delta | min slack `2Φ+6δ-S*` | all steps |
|---|---:|---:|---|
| transverse_pair a=1/8 | 2/17 | 19/34 | OK |
| transverse_pair a=1/4 | 1/5 | 3/5 | OK |
| transverse_pair a=1/2 | 1/4 (boundary) | 3/4 | OK |
| staircase m=1,2,3 | 1/2 (OUTSIDE hyp) | 2, 2, 13/6 | OK |
| **perturbed_staircase m=5 eps=1/1000** (the w38 witness) | 1/2 | 12/5 | OK |
| perturbed_staircase m=1,2 | 1/2 | 2, 9/4 | OK |
| dense_pair_k7 | 6/17 | 26/17 | OK |
| no_center_path k=4,5,6 | 1/100 | 3/50 | OK |

- **beta<0 rows with large E**: handled — such rows do not enter `Phi`/`S*` (only `beta_+`); they
  feed `Dneg` (Step 4), which is bounded by mass·box.
- **many overshoot rows / windmills**: `overshoot_hunt.py` — 0 violations; `V<=Phi/2` aggregates
  correctly because it is a *pointwise* `<=` summed with nonneg weights.
- **delta at 1/4 boundary**: transverse a=1/2 (`delta=1/4`) and cluster3 (`delta=1/4`) — OK.
- **delta = 1/2 (OUTSIDE the hypothesis)**: staircase + perturbed staircase all hold. **The proof
  never uses `delta <= 1/4`** — it uses only `nu_{u_s} <= delta` and the box `lambda <= 3`, both
  valid in the entire theta-1/2 class for ANY delta. So the factorization is a class-wide fact;
  `delta <= 1/4` is needed only LATER by `(EX)`, not by the factorization. **No hidden delta<=1/4
  dependence.** (Confirmed also by 362 random instances with `delta > 1/4`, up to `delta=3`, all OK.)
- **rank 2 consistency**: factorization gives `S* <= 6 delta` when `Phi=0`; the rank-2 theorem
  (w40) gives the sharper `S* <= 2 delta`. `6 delta >= 2 delta` — **consistent, no contradiction**.
  Empirically rank-2 instances show `S*/delta <= 1` (sharper still). The two bounds agree (the
  factorization is just looser at rank 2, as expected for a rank-agnostic argument).

---

## 3. Independent numerical falsification (0 violations)

Own generators, exact rationals, AT and BEYOND the boundary:
- `falsify.py`: 385 nontrivial exact idempotents (rank 2 and 3, n=3..5), 23 inside `delta<=1/4`,
  362 with `delta>1/4` (up to delta=3). **0 violations.**
- `families.py`: 8 named families × all charts × all pivots, every step (i)-(vi). **0 step failures.**
- `composition.py`: 325 instances, selected-chart contract. **0 violations.**
- `overshoot_hunt.py`: windmill + heavy-overshoot adversarial search at box edge (`max|a|=2`,
  lambda up to 14/9). **0 violations.**

No counterexample found anywhere, including well outside the hypothesis boundary.

---

## 4. Composition / argmin / quantifier (CLEAN, C_sf = 2 C0 + 6)

`(F)` factorization is **universal in `s`**: `∀U ∀s: S*_s(U) <= 2 Phi_s(U) + 6 delta`.
`(EX)`: `∃U0: max_s Phi_s(U0) <= C0 delta`. `U* := argmin_U max_s Phi_s(U)`.

```
max_s S*_s(U*) = S*_{s0}(U*)                       (s0 the maximizer of S*)
              <= 2 Phi_{s0}(U*) + 6 delta          (F) at (U*, s0)   -- universal in s, so legal
              <= 2 (max_s Phi_s(U*)) + 6 delta     Phi_{s0} <= max_s Phi_s
              <= 2 (max_s Phi_s(U0)) + 6 delta     argmin: max_s Phi_s(U*) <= max_s Phi_s(U0)
              <= 2 C0 delta + 6 delta              (EX)
               = (2 C0 + 6) delta.
```

**No quantifier slip.** The subtle point — does `max_s S*_s <= 2 max_s Phi_s + 6 delta` follow
from the per-`s` factorization? — is YES precisely because `(F)` holds for *every* `s`
(in particular the `s0` that maximizes `S*`), and then `Phi_{s0}` is relaxed UP to `max_s Phi_s`.
The argmin minimizes `max_s Phi_s` (a per-chart scalar), so the relaxation lands on the quantity
`(EX)` controls. `composition.py`: 325 instances, the selected-chart contract
`max_s S*_s(U*) <= 2 max_s Phi_s(U*) + 6 delta` holds with 0 violations. The final
`SF_s <= S*_s` link is the separately-banked w39 `(P1)` repair (not re-derived here, but it is the
inequality direction the contract needs, and the prompt lists it as a known identity).

Therefore **`C_sf = 2 C0 + 6`** is correct; for the (still-open, empirical) `C0 = 1` this gives
`C_sf = 8`.

---

## 5. Bottom line for the orchestrator

- **BANK the factorization lemma** `S*_s(U) <= 2 Phi_s(U) + 6 delta` with `(a,b) = (2,6)`,
  valid for the **entire theta-1/2 class** (no `delta <= 1/4` needed). It is a finite sign-case
  identity plus the `(DEF)` deficit decomposition plus the `lambda <= 3` box cap; I reproduced
  every step independently and symbolically.
- **BANK the composition** `C_sf = 2 C0 + 6` (no quantifier slip).
- **Do NOT bank `(EX)` / `C0 = 1`** — w41 correctly leaves it open (empirical only). This audit
  does not touch its status; the live open problem remains exactly `(EX)` at rank >= 3.

P(factorization correct) = 0.99 · P(composition correct) = 0.99 · (EX-rank3 untouched, still open).
