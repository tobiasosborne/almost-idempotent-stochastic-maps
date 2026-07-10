# Run bundle: W61 decider A — X2 thin-transient-graft refuter search: PARTIAL, X2 NOT refuted; tallness is the exact blocker (2026-07-10, session 16)

## Hypothesis

bd `aism-3nk` / route fork `aism-ur9` (Route A lane): does an exact factorized
thin-transient-graft family (delta_k -> 0, bad H-X data per `def-selected-corner`
with Gamma_f(B) >= 1/4 and M_X(B) > 1/8, truncated quotient transport cost
T_B -> 0) exist? A hit would refute the proposed X2
(`conj-w60-hx-microfreight-exclusion`, DECOMPOSITION-W60-CODEX.md §X2 — NOT
registered) and push Route A onto its H-X-selector fallback. (Rigour tag:
`numerical` — exact rational construction, L3 evidence, never proof.)

## Finding

**PARTIAL — X2 was NOT refuted.** Fresh codex xhigh worker (isolated workspace)
built an exact six-row factorized family `P = L*B`, `B*L = I` (balanced
factorized split of a carrier column, dodging the
`obs-thin-zero-face-blocker-graft` append blocker) that achieves, in exact
rationals for k = 512, 1024, 2048: Gamma_f(B_F) = 1/(1+d) -> 1 (>= 1/4),
M_X(B_F) = (3-d)/(4(1+d)) -> 3/4 (> 1/8), T_B = q(2-d)/(1+d) < 2*tau -> 0, with
a certified hidden top (exact t* and height certificates) — i.e. EVERY checked
selected-corner clause EXCEPT tallness: H = O(tau^3), so `H > 16*tau` fails
asymptotically, not at a tuning boundary. Ordinary transient-row appends die
exactly at the banked graft-convention blocker; low-rank long-chain probes
(floating, non-certifying triage only) never reached the small-delta regime.
HONEST SCOPE: constructive evidence that the graft mechanism buys freight mass,
legality, and vanishing transport but cannot buy tallness; failure of this
search is NOT a proof of X2. Decision take-away: X2's prove-or-refute lane
remains genuinely open, and TALLNESS is the resource its refuter cannot
manufacture (same wall as decider B — see the W61 wave doc).

## Command

```bash
cd runs/2026-07-10-w61-x2-graft-refuter/scripts
PYTHONDONTWRITEBYTECODE=1 python3 -u search.py   # deterministic, no seed; exact Fractions
```

## Invariant (checkable)

Every claim is an exact `fractions.Fraction` assertion inside `search.py`:
`B*L = I` (hence `P^2 = P`) entry-by-entry, row sums, delta(P) = d, the fiber
quotient, Gamma_f/M_X/T_B closed forms, the t*(u) hiddenness witness balance,
and primal+dual (1-Lipschitz support functional) height certificates. The
script exits nonzero on any mismatch and prints the exact verdict table
(reproduced independently by the orchestrator on 2026-07-10: all three k pass,
verdict PARTIAL). `data/certificates.json` stores matrices and all quantities
as rational strings, labeled partial.

## Next

Feeds the aism-ur9 route decision (with decider B). If Route A is chosen, X2
goes to a prover with the tallness resource highlighted as the load-bearing
hypothesis; the graft family here is the canonical near-miss stress fixture.
