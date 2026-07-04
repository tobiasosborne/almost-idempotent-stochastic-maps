# Run bundle: small-δ certified argmin B-sweep (session-7 de-risk decider #2) — 2026-07-04

**Status: L3 numerical evidence. NEVER rigorous.** Exact ℚ arithmetic for every certified quantity
(`fractions.Fraction`). Codex-worker-authored (fresh `codex exec`, prompt archived in the session
scratchpad), orchestrator-recomputed (see Invariant), run as decider #2 of the 2026-07-04 audit's
de-risk sprint (`docs/audits/2026-07-04-operational-audit.md` §7) — the direct wave-13 gate.

## Hypothesis / decision question

Before this bundle, ALL certified capped-argmin B-lemma data sat at δ ∈ {7/30, 637/2550, 1/4} (the
cap/corner), while `conj-sc`/`conj-rh` claim the whole range `0 < δ ≤ 1/4` (evidence-audit blind spot
#1). Kill question: at small/mid δ with a clean high-self non-fan Γ-branch at a certified θ-½
Φ-argmin, does `B_{r,s}/δ` amplify (⇒ the B-lemma `B ≤ K·δ` dies cheaply) or stay bounded?

## Command (re-run)

```bash
python3 runs/2026-07-04-small-delta-b-sweep/scripts/decider_small_delta.py
```

Deterministic (finite rational parameter lists, no randomness); regenerates
`data/certified_points.{csv,json}` + `data/ANSWER.md`. Worker's original script with one mechanical
re-home patch (output dir → `data/`).

## Invariant / known-value check

The script HARD-ASSERTS: the G12 calibration instance recomputes exactly (`δ=1/4`, `B=2/57`,
`B/δ=8/57`); per instance `BL=I`, `P²=P`, `P·1=1`, δ in range, exact cross-pivot cancellation
`A=B+C−D`; complete actual-row chart enumeration per retained instance. **Orchestrator recomputation
(independent code — exact Gaussian elimination + Gram-volume enumeration over all C(6,3) charts, not
the worker's functions):** for the maximizing instance, reproduced `BL=I`, `P²=P`, row sums,
`δ=55319/1000000`, the θ-half census (8 charts), the UNIQUE argmin `U=(0,2,4)` with
`max_s Φ_s = 219870541/7880000000`, relative volume `(197/200)²`, high-self `P₁₁=203/400 > 1/2`, and
`B_{1,2} = 42/985`, `B/δ = 8400000/10897843` — all values match.

## Finding (headline + honest scope)

1. **`B/δ` does NOT vanish at small δ — it RISES: max certified `B/δ = 8400000/10897843 ≈ 0.771` at
   `δ = 55319/1000000 ≈ 0.055`** (compensated-insert family, clean high-self non-fan Γ-branch, unique
   certified θ-½ argmin; `C = 0` there). Nine further certified points across two families sit at
   `B/δ ∈ [0.69, 0.771]`, δ ∈ [0.055, 0.114]. The pre-existing picture ("all capped-argmin data is
   sub-δ", i.e. `B/δ ≤ 8/57 ≈ 0.14`) is now known to be an artifact of the δ≈cap data — at small δ
   the B-lemma constant must satisfy **`K ≥ 0.771`**.
2. **No unbounded amplification found — minimality is the binding constraint, again**: every
   amplification attempt was obstructed by (a) the θ-½ argmin SWITCHING to a chart with `Φ = 0`
   (non-argmin `B/δ` up to 50 exists but never survives argmin certification — reproducing G12), (b)
   the branch turning Ψ/mixed, (c) loss of high-self, or (d) δ leaving `[1/100, 3/20]`. The
   compensated-insert family's maximizer sits at an insert-weight boundary (`y` near `681/10000`)
   beyond which the argmin switches away.
3. **Scope limits (honest):** exactly two construction families (5-row two-carrier; 6-row
   compensated-insert), finite rational parameter lists, complete chart enumeration per retained
   instance (20 charts at n=6) — NOT an exhaustive search over rank-3 idempotents or support
   patterns; whether `B/δ` can approach or exceed 1 at argmins in richer families is OPEN;
   the branch classification ("clean high-self non-fan Γ") follows the G12 conventions as
   implemented by the worker.

**Consequence for the campaign:** decider #2 PASSES with a sharpened target — the B-lemma remains
viable (bounded `B/δ`, capped by argmin switching = exactly the minimality mechanism wave 13 would
formalize) but is now known to need `K ≈ 1`, not `K ≪ 1`: any proof or contract absorbing `B` must
budget a full δ-scale term (directly informs `aism-z98`). Wave 13 is GO, with the amplification
frontier (`sup B/δ` at argmins: 0.771 ≤ sup ≤ ?) as its quantitative companion question.

## Next

Wave 13 (`aism-5sc`): prove `B ≤ K·δ` via minimality (incl. the `c<0` pivot-removing analogue — the
named tool gap), using this bundle's maximizer as the live stress instance; alternatively continue
the amplification hunt in richer families (three-carrier, non-sparse left inverses) toward `B/δ → 1`
or beyond — crossing 1 would reshape (not kill) the skeleton's budget arithmetic; a certified
crossing of the (CI)-financed total would be the actual kill. `aism-z98` should be revisited with
this bundle in hand.
