# Run bundle: rank-4/5 skeleton-transfer decider (session-7 de-risk) — 2026-07-04

**Status: L3 numerical evidence. NEVER rigorous.** Exact ℚ arithmetic for every certified quantity
(`fractions.Fraction`; floats nowhere in certified values). Codex-worker-authored
(fresh `codex exec`, prompt archived in the session scratchpad), orchestrator-recomputed (see
Invariant), run as decider #1 of the 2026-07-04 audit's de-risk sprint
(`docs/audits/2026-07-04-operational-audit.md` §7) BEFORE any wave-13 proof work.

## Hypothesis / decision question

The entire (PRT) skeleton — pivot-removing max-stationarity disjunction (`lem-pivot-removing-move`),
collateral-import (CI) bound (`lem-collateral-import`), cross-pivot split, the open B-lemma — is stated
and tested at RANK 3 ONLY, while `conj-ex` needs every rank ≥ 3 with dimension-free constants
(audit risk #2). Kill question: transcribed naturally to rank 4 (and a cheap rank-5 probe), do the
disjunction and (CI) FAIL, or do `Φ/δ` / `B/δ` blow up — i.e., is wave-13+ effort rank-3-parochial?

## Command (re-run)

```bash
python3 runs/2026-07-04-rank4-transfer-decider/scripts/decider_rank4.py
```

Deterministic (no randomness at all); regenerates `data/certified_points.{csv,json}` + `data/ANSWER.md`.
The script is the worker's original with one mechanical re-home patch (output dir → `data/`, re-run
string) applied by the orchestrator.

## Invariant / known-value check

The script HARD-ASSERTS per instance: `BL=I`, `P²=P`, `P·1=1`, `δ ≤ 1/4` (uncapped instances excluded
by construction), exact chart Gram volumes, the exact pivot-removing volume identity
`Vol(V_j)=|a_s(j)|·Vol(U)`, the disjunction `Φ_s(U) ≤ max(Ψ_j, Γ_j)` on every θ-half positive-`c` move,
the rank-4 (CI) transcription on every checked transverse pair, and exact cross-pivot cancellation
`A = B + C − D`; it exits nonzero on any failure. Calibration: first reproduces the known rank-3
no-center value (`δ=1/100`, `Φ/δ=1`). **Orchestrator recomputation (independent code, not the worker's
functions):** for `cycle_coupling_rank4_a1_30_w1_2` and `no_center_rank4_a1_100`, re-derived
`P²=P`, row sums, `δ`, chart coordinates by exact Gaussian elimination, `Φ_s`, and `B_{r,s}` — all
values match (`δ=691/13530`, `Φ/δ = B/δ = 27031/82920`; `δ=1/100`, `Φ/δ=5/4`, `B=0` at the maximal
pivot).

## Finding (headline + honest scope)

1. **The skeleton TRANSFERS in this search: no rank-4/5 violation of the pivot-removing disjunction**
   (48 exact θ-half moves) **nor of the natural `c>0` rank-4 (CI) transcription** (144 transverse
   inequalities; worst slack exactly `0`, i.e. (CI) stays sharp).
2. **No blow-up trend**: max rank-4 `Φ/δ = 5/4` (no-center family; rank-5 probe `4/3 = 2−2/(5−2)`,
   on the known slow climb toward 2 — plateau intact, consistent with
   `runs/2026-07-02-ex-no-center-highrank/`). Max rank-4 `B/δ = 27031/82920 ≈ 0.326` and
   `(B+C)/δ = 157/460 ≈ 0.34` (cycle-coupling family) — sub-δ throughout, first nonzero-B instances
   outside rank 3 and outside the identity-block style.
3. **Convention note (orchestrator):** reported `B/δ` follows the repo's G12 convention (`s` = the
   maximal pivot, `r` transverse). Over ALL ordered pairs `(r,s)` the no-center rank-4 instance
   realizes `B_{3,0} = δ` exactly (`B/δ = 1` at a NON-maximal pivot) — harmless for the B-lemma as
   stated (branch/pivot-specific) but a real difference between the conventions; do not conflate.
4. **Scope limits (honest):** two rank-4 families (no-center × 3 scales; cyclic coupling × 3 mixtures)
   + three rank-5 probes — a finite deterministic enumeration, NOT a search over all rank-4 signed
   idempotents; (CI) checked only in its stated `c>0` regime (negative-`c` moves enter the disjunction
   only); the rank-4 `R^{(4)}` import term is the worker's natural transcription, not a validated
   contract; nothing here bears on the B-lemma's branch condition (no clean high-self non-fan
   Γ-branch was certified at rank 4 in this pass).

**Consequence for the campaign:** decider #1 PASSES — no evidence that the skeleton is rank-3-parochial;
the rank-generalization risk stays open as *proof* work but loses its "machinery visibly breaks at
rank 4" kill scenario. Wave-13 go/no-go now waits on decider #2 (small-δ argmin sweep).

## Next

Decider #2 (small-δ certified argmin sweep, in flight) completes the wave-13 go/no-go. If it also
passes: wave 13 (the B-lemma) proceeds with the `c<0` pivot-removing analogue codified first. The
rank-4 `R^{(4)}` import transcription used here is a candidate registry shard (proved-mod-audit at
most) only if/when the skeleton assembles; a rank-4 Γ-branch hunt (none certified here) is the natural
follow-up sweep if the B-lemma proof stalls on rank-3-specific structure.
