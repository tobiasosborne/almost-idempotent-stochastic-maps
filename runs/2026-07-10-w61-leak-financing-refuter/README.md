# Run bundle: W61 decider B — leak-financing refuter at the N5(ii)/N6 constants: FINANCING INSTANCE FOUND (local N5(ii)); ledger-only close is dead as budgeted (2026-07-10, session 16)

## Hypothesis

bd `aism-kup` / route fork `aism-ur9` (Route B lane): can the engine demand of
`lem-hx-financing-floor` (ball form ~ l/(2+4delta)) be financed entirely through
leaks the banked ledgers permit at the N5(ii)/N6 constants
(DECOMPOSITION-W60-FABLE.md dispatch 3: leak allowances ~ 3*tau/4)? A financing
instance means the N5/N6 confinement conjectures cannot be closed from the named
scalar ledgers as budgeted and need restating before creative spend. (Rigour
tag: `numerical` — exact rational construction, L3 evidence, never proof.)

## Finding

**FINANCING INSTANCE FOUND — scoped to the local N5(ii) geometry.** Fresh codex
xhigh worker (isolated workspace) built an exact six-row dyadic family
(tau = 2^-k, delta = tau^2, k = 8..16 banked, k -> 32 rerun exactly): a signed
full-fiber split of the thin-zero-face fixture with a transient freight row
X = (1-theta)A + theta*C. Certified exactly: hidden top/carrier u = v = A
(small-beta witness t* = tau/8 < kappa), pair (X, A) at separation l = tau/2 in
the N5(ii) band, engine demand R = theta(1-2theta) - (2-theta)q > 0 PAID with
slack (theta - R = 2theta^2 + (2-theta)q > 0) — and the entire payment sits on
one fiber C with z(C) = 2+H, h(C) = 1 (deep for BOTH banked observables) where
the hidden top/carrier pays NOTHING: top-deficit, z-leak, h-leak, zero-face
capacity (both levels), hiddenness-witness, and mass-split ledgers all hold
exactly, the inequality ledgers with strict slack (full exact table in
REPORT.md). The financing channel is precisely the unconfined FREIGHT-ROW
coefficient priced as N5(c)'s likeliest death. HONEST SCOPE: NOT a
counterexample to N5 or N6 — tallness (H/tau = q/4, not > 16) and the
Gamma_f freight-mass clauses (Gamma_f(B_N) = 0) are false, and N6's far-carrier
horn is untouched; those failures are global-completion conditions, not budget
exhaustion. Decision take-away: N5(ii) as stated cannot be closed ledger-only —
it needs a freight-row budget or a Gamma_f-to-coefficient coupling; and
tallness is again the wall keeping the adversary out of the true class (same as
decider A).

## Command

```bash
cd runs/2026-07-10-w61-leak-financing-refuter/scripts
PYTHONDONTWRITEBYTECODE=1 python3 -u search.py   # deterministic, no seed; exact Fractions (k=8..16)
```

## Invariant (checkable)

All decisions are exact `fractions.Fraction` assertions in `search.py`:
P*1 = 1 and P^2 = P entry-by-entry, delta(P) = delta, the fiber quotient and
signed A-fiber split, the small-beta hiddenness witness balance
(D-A) + (1/eps)(Z-A) = t(C-A), exposer/visible-set certificates, the exact
lever values of the recentred functional, the engine demand R and the payment
theta with closed-form slack, and every ledger row of the REPORT table. Script
exits nonzero on any mismatch (reproduced independently by the orchestrator on
2026-07-10: k = 10..16 all pass). `data/certificates.json` stores exact
rational strings.

## Next

Feeds the aism-ur9 route decision (with decider A). If Route B is chosen, N5
must FIRST be restated with the freight-row/Gamma_f coupling budget (surface
restatement, cheap) before any creative prover runs; the dyadic family here is
the canonical stress fixture for the restated budget.
