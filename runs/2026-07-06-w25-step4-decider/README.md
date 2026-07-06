# Run bundle: step-4 decider — the insufficiency certificate (W25 worker N) — 2026-07-06

**Status: L3 numerical evidence carrying an exact INSUFFICIENCY certificate — a no-go of the E2
kind, relative to an explicitly enumerated fact-list; NEVER an emptiness claim about step 4
itself.** Exact ℚ throughout. One codex obstructor (prompt in the session scratchpad,
`W25/PROMPT-N.md`), mutually blind from the step-4 prover. Orchestrator reran the worker checker
(exit 0) and INDEPENDENTLY recomputed the ENTIRE certificate from the printed values
(`scripts/orchestrator_recompute.py`, 17/17 — algebra AND the explicit exposer evaluation; nothing
worker-asserted survives unchecked here, since the certificate is a single explicit 3×3).
Companion wave artifact: `docs/waves/2026-07-06-W25-step4-decider.md`.

## Hypothesis / adversarial question

G-bootstrap step 4 (bd `aism-7pe`, sketch v5 M1): can the once-applied maximum principle close the
width-4 contradiction from the imported fact-set alone (harmonicity; parametric-collapse conclusion
at labeled-hidden tops; Lemma-A conclusion at labeled-visible rows; disintegration ledger; generic
row facts)? Worker N's mandate: prove INSUFFICIENCY by exhibiting a certified model of the facts
with a sustained web and H > 13τ.

## Headline finding

**INSUFFICIENT — certified by a 3×3 exact idempotent.** `P = [[1,0,0],[0,1,0],[101/100,−1/100,0]]`,
δ = 1/100 (< δ₁ = (17−12√2)/2, exact squared-form check), labels W = {row 0}, hidden top = row 1.
Under the labels: true point distances (0, 2, 1/50), labeled H = 2 = 20τ > 13τ; g = P·1_{{1}} =
(0, 1, −1/100) exactly harmonic; the labeled-hidden top has g = 1 > 1/2 − δ; the labeled-visible
row has g = 0 ≤ 4τ; disintegration holds with zero slack. **Every imported scalar fact is
satisfied — and the configuration is a "tall sustained web."** The certificate's teeth: the
labeled-hidden top is ACTUALLY (ρ,κ)-exposed — the explicit admissible exposer h(x) = (100/101)·x₀
has far-set margin 100/101 ≥ κ = 1/40 — so the true W(P) would absorb it. **The fact-list never
consumes hiddenness (non-exposedness); that is exactly the missing input.**

## Honest scope

- Insufficiency is relative to the ENUMERATED fact-list (the worker report itemizes F0–F8) — it
  says step 4 cannot be proved from those conclusions as black boxes; it says NOTHING against
  step 4 itself (the true statement may well hold — the model violates true hiddenness).
- Blind convergence: the mutually-blind prover (worker M, same wave) independently identified the
  same missing piece from the opposite direction — its once-applied argument yields a LOWER bound
  on deep hidden-web mass and names the missing UPPER cap (`M_v⁴ + R_v ≤ 1/2 − δ`); see the wave
  doc. Codified frontier: `conj-min-a-w4`.

## Command (re-run)

```bash
python3 runs/2026-07-06-w25-step4-decider/scripts/w25_worker_n.py            # worker checker (exit 0, PASS)
python3 runs/2026-07-06-w25-step4-decider/scripts/orchestrator_recompute.py  # 17/17 from printed values
```

`data/worker-n-report.md` is the worker's full report (fact-list F0–F8, model, exposer);
`data/rerun-n-stdout.txt` is the orchestrator's captured rerun.

## Invariant / known-value check

The whole certificate is a single explicit 3×3 rational matrix: the orchestrator recompute
re-derives P² = P, row sums, δ, the exact distances, g, harmonicity, the three labeled fact
conclusions, and the exposer margin from the printed values alone — 17/17. The δ-window membership
is checked in exact squared form ((17 − 2δ)² > 288).

## Next

The named missing input drives the next wave: consume HIDDENNESS quantitatively — t*(v) < κ means
every admissible exposer fails the κ-margin against some ρ-far row; turn that universal statement
into the cap `σ₄ ≤ 1/2` at hidden tops in tall configurations (`conj-min-a-w4`; new bd issue).
Candidate machinery: the two-observable argument (mass-g + affine deficit) + the exposer-failure
witness family; `lem-canonical-separator` re-establishment is a sub-target.
