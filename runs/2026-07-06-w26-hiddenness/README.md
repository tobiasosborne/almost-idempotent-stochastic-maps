# Run bundle: W26 hiddenness wave — RELAUNCHED AND HARVESTED (2026-07-06, session 11)

**Status: wave complete.** The 2026-07-06 evening dispatch was killed mid-run by a network outage
(that state was preserved here as an interrupted-marker, commit `5facc80`); session 11 relaunched
both briefs VERBATIM (SHA256 match verified at relaunch, see Invariant) and harvested. This README
supersedes the interrupted-marker text.

## Hypothesis (the wave's question)

bd `aism-n7i` (P0), sketch v6 M1 step 4: prove `conj-min-a-w4` by consuming HIDDENNESS
(worker P: LP-dual witness of t*(v) < κ + two-observable machinery), adversarially paired with the
round-2 insufficiency game (worker Q: models must hard-assert TRUE hiddenness via exact t* LPs).

## Headline finding

Hiddenness consumed both ways, blind-convergent: worker P's LP-dual witness (VP-verified,
codified `lem-hiddenness-dual-witness` + `lem-top-slab-companion`) and worker Q's forced
far-barycenter structure are the same object from opposite sides; the W25 3×3 insufficiency
certificate is VISIBLE under canonical geometry (t* = 100/101, exact) and no second F0–F10
certificate exists in the bounded search. The remaining step-4 gap is the coupling
witness → σ₄ (W29).

## What happened (design + verdicts)

Mutually-blind pair P ∥ Q, then a separate fresh hostile verifier VP on P's claimed partial
(prompt banked in `answers/PROMPT-VP.md`). Verbatim verdict lines:

- P: `PARTIAL (proved: hiddenness LP-dual witness and top-slab far-row consequence; gap: no
  inequality couples that witness to row-v positive mass sigma_4)`
- Q: `FORCED-STRUCTURE (statement: t*(v)<kappa forces a convex combination of rho-far rows within
  kappa*(2+4*delta) of p_v; W25's self-loop model lacks this and becomes visible)`
- VP: `VALID-WITH-CORRECTIONS (both claims survive; Claim 1's strict psi inequality needs E>0,
  otherwise only <=)`

Harvest: `lem-hiddenness-dual-witness` + `lem-top-slab-companion` codified (proved/af:none, VP as
independent reviewer); the W25 3×3 insufficiency certificate shown VISIBLE under canonical
geometry (t* = 100/101); no second F0–F10 certificate found under the witness constraint.
Full narrative: `docs/waves/2026-07-06-W26-hiddenness-consumption.md`.

## Contents

- `prompts/PROMPT-P.md`, `prompts/PROMPT-Q.md` — the byte-frozen wave briefs (unchanged).
- `answers/ANSWER-{P,Q,VP}.md`, `answers/PROMPT-VP.md` — raw worker/verifier outputs (verbatim).
- `scripts/w26_worker_q.py` — worker Q's exact-arithmetic audit + bounded search (Fraction-only
  verdicts; exact rational LPs for row-vertex / exposedness / distance).
- `data/worker-q-report.md` — worker Q's report (dual/gauge form, W25 re-audit, rank-5
  calibration with exact dual witnesses, bounded-search summary).

## Command (re-run)

```bash
PYTHONDONTWRITEBYTECODE=1 python3 runs/2026-07-06-w26-hiddenness/scripts/w26_worker_q.py --samples 1000
```

Orchestrator recompute (session 11): rerun exit 0; tail matches the report (seed 26017,
115 audited exact idempotents, 5 hidden-vertex records, 0 tall-13 records, best H/τ ≈ 0.158).

## Invariant / checkable

- Brief integrity: `sha256sum prompts/*.md` →
  `90003292b3e4affb5c6eb2114e9c57aca32d58602991074f9467c51fbc06d49b  PROMPT-P.md`,
  `c3da733c1b2b7c6fc18d82d483250c6cd099322630b6430e288f2878ce1879ec  PROMPT-Q.md` (matched at
  relaunch).
- Exact fixture invariants (script-checked, exact rationals): W25 3×3 canonical audit gives
  t*(v) = 100/101, t*(s) = 1, W = {v,s}, H = 0; rank-5 calibration gives
  t*(r3) = t*(r4) = 1/41 with dual witnesses satisfying ‖p_v − q_far‖₁ = (1/41)·D exactly.

## Next

W29 (the coupling wave): consume the witness at ALL deep carrier vertices (per worker Q's
interface + `lem-genuine-disintegration`), prove-or-refute `conj-min-a-w4`; any future refuter
must satisfy the witness constraint at every hidden carrier.

## Honest scope (L3)

The search component is bounded evidence ONLY (n ≤ 10, 1000 Λ-C samples, seed 26017): no
emptiness claim. The codified lemmas are reviewed paper proofs (L5), NOT af-validated, NOT
L0-rigorous. Worker Q's stronger α-free gauge form is worker-T1 (fixture-verified, not
independently reviewed) — reconcile with VP's dual (which retains the α family) before any use.
