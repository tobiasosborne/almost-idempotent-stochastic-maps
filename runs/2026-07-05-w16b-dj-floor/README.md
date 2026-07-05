# Run bundle: D_J/B floor decider (wave 16b) — 2026-07-05

**Status: L3 numerical evidence. NEVER rigorous.** Exact ℚ. Codex-worker-authored (prompt in the
session scratchpad); worker script rerun by the orchestrator (exit 0). Companion wave artifact:
`docs/waves/2026-07-05-W16b-dj-floor.md`.

## Hypothesis / adversarial question

Wave 16's named decider: does the carrier self-defect floor `D_J/B` (the direct-FE conditional
route to `conj-b-restricted`) survive adversarial minimization over certified clean-block
instances, or can `D_J/B → 0` (killing the route) — with fake kills (`B` vanishing faster than
`δ`) excluded?

## Headline finding

**UNDECIDED, leaning against the direct-FE route.** The certified floor dropped from the seed
`157/500 = 0.314` to `23/1000 = 0.023` on a fresh two-carrier-insert α-family point with
`B/δ = 1343375000/2640001033 > 1/2` (NOT a fake kill), `δ = 5248511/22375000 ≤ 1/4`, clean block
at the capped argmin `(0,2,4)` intact. Family anatomy: `D_J/B = 1 − α`; the open residual is
whether `α → 1` is achievable while preserving the clean block, argmin status, maximal pivot,
and `B/δ` bounded below. No sign kill occurred (every certified positive-B row had `D_J > 0`);
no upper-side blow-up (`D_J ≤ C·δ` on everything certified).

## Honest scope + verification-scope note

All 9 wave-16 bundle points recomputed with `D_J = S_J` hard-asserted (incl. both tied charts).
**Orchestrator verification scope:** worker script rerun (exit 0) + exact arithmetic
cross-checks of the headline point's recorded quantities (`D = S`, `D/B = 23/1000`, `D/δ`
consistent). The fresh-point certificate JSON records derived quantities and family params but
NOT the full `L,B` matrices, so a matrix-level independent recheck (the DC2/W15 standard) was
NOT possible from the certificate alone — a bundle limitation. Nothing is promoted on this wave;
any follow-up wave MUST emit full matrices for its headline points.

## Command (re-run)

```bash
python3 runs/2026-07-05-w16b-dj-floor/scripts/dj_floor_decider.py
```

## Invariant / known-value check

Per point: `B·L = I₃`, `P = L·B`, `P² = P`, row sums 1, `δ ≤ 1/4`, complete θ-half enumeration,
argmin/maximal-pivot/clean-block, and the direct-FE identity `D_J = S_J`. Seed calibration:
`λ = 157/500` on the wave-15 instance reproduced.

## Next

Decide the α → 1 continuation (prove the constraint set forbids it, or certify a family with
`D_J/B → 0`): this settles whether `conj-b-restricted`'s prove-side needs a mechanism beyond
direct-FE. Queued for session 9 alongside the Route-A wall re-read (which wave 17b's slack
finding ranks higher).
