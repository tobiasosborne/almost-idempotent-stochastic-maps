# W60 ENGINE BATCH — HOSTILE VERIFIER brief (fresh, batched)

You are a fresh HOSTILE VERIFIER. You did not write `PROOFS-W60-ENGINE.md` and you
owe its author nothing. **Finding a counterexample, a gap, or an error is a BIG
SUCCESS** — a wrong lemma entering this project's registry is the worst possible
outcome, far worse than a delayed one. Do not extend, improve, or complete the
proofs; judge them.

## Object of review

`PROOFS-W60-ENGINE.md` in this workspace root: five claimed lemmas E1–E5 (signed
picture; finite exact signed idempotents P² = P, P·1 = 1; full row-point fibers;
δ = row negative mass). The file begins with the author's own summary table —
distrust it.

## Reference material (ground truth for cross-checks, NOT authority for the claims)

- `definitions/def-signed-idempotent.md`, `definitions/def-negative-mass.md` — the
  canonical definitions; any mismatch between the file's conventions and these is a
  finding. NOTE the file defines δ as max_i row negative mass — check every use is
  consistent with whichever convention the definitions pin, and flag any drift.
- `context/PAPER-PROOF-w59.md` — an af-validated rank-3 special case (its Claims 1,
  2, 4). If E1/E2/E4 restricted to that setting contradict it, someone is wrong.
- `context/FINDINGS.md` — recorded dead routes. Flag any proof step that re-walks
  one (index-level path products / per-fiber budget payments / censoring without a
  norm gap / frame-specific-to-frame-free leaps).

## What to attack, per target (non-exhaustive — attack anything)

- E1: the affine-constant cancellation (does Σ_Q d_Q = 0 actually hold for
  row-HULL points q0, q1, not just rows?); the left-fixedness of q1 − q0 (is
  (q1 − q0)P = q1 − q0 proved, and does the proof use only P² = P on hull points?);
  the fiber regrouping; the Hahn–Banach normalized-class construction (right dual
  norm? attainment on ℓ¹ vs ℓ∞?).
- E2: the synthetic-row facts qP = q, q·1 = 1, ν(q) ≤ δ — each needs its own proof;
  the sign-union bookkeeping (is each row budget really paid once per union?);
  d_Q = 0 fibers; the claimed global bound Σ|d_Q| ≤ ‖a−b‖₁.
- E3: the N/F split arithmetic; the definition and use of ℓ_χ; the recentred
  sign-functional corollary (is |χ_c| really bounded by distance/ℓ? is the
  row-diameter bound proved, and correct for SIGNED rows?); vacuity conditions
  stated honestly.
- E4: THE CRITICAL ONE. Track every constant from the unit moment to the final
  ceiling δ_R(K_R, L, K_C): the sign-split of the tail, the budgets of the
  synthetic row q and of row f through p_f = p_v − A·D + r, the core cost L·‖D‖₁,
  the window τ/2 ≤ ‖D‖₁ ≤ 2τ, the A ≥ 4 usage. Try SMALL exact counterexamples
  (rank ≤ 3, few fibers) against the stated ceiling. Verify the T0 fixture
  claim (calibration (3,1,0)) against context/PAPER-PROOF-w59.md's actual display.
  Check the quantifier order: (K_R, L, K_C) fixed BEFORE δ_R.
- E5: the instantiation constants; the two-block δ = 0 fixture arithmetic; whether
  the statement is vacuous for ‖p_r − p_s‖₁ ≤ 8δ (and whether that is flagged).

## Verdict format (MANDATORY)

Write `VERDICT-W60-ENGINE.md` in the workspace root. First line: an overall one of
`ALL-VALID` / `MIXED` / `ALL-INVALID`. Then EXACTLY five verdict lines:

E1: VALID | VALID-WITH-CORRECTIONS | INVALID — <one-line reason>
E2: ...
E3: ...
E4: ...
E5: ...

Then, per target, the full audit: every checked step, every found gap with its
exact locus (quote the offending display), every correction needed (stated
precisely enough to apply mechanically), and for any INVALID a concrete
counterexample or an irreparable-gap explanation. End with a DEAD-ROUTE section:
any FINDINGS pattern you spotted, or "none".
