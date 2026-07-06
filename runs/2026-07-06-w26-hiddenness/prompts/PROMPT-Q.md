# W26 Worker Q — OBSTRUCT conj-min-a-w4: is even HIDDENNESS enough? (insufficiency-or-forced-structure, round 2)

You are a fresh, independent worker in the repo `/home/tobias/Projects/almost-idempotent-stochastic-maps`
(mathematical exploration of almost-idempotent stochastic maps; signed-idempotent picture). You are the
OBSTRUCTION side of an adversarial pair on THE frontier conjecture. The previous round (W25) proved
the old fact-set insufficient via a certified model whose "hidden" vertex was secretly exposed; the
prover's fact-set now includes TRUE HIDDENNESS. **Your mandate: test whether hiddenness closes the
gap — a second insufficiency certificate, or the forced structure that kills all models, are both
BIG SUCCESSES.** Mutually blind: do not read or write other workers' files or anything under
`runs/2026-07-06-w26*` except your own paths:
`runs/2026-07-06-w26-hiddenness/scripts/w26_worker_q.py` +
`runs/2026-07-06-w26-hiddenness/data/worker-q-report.md` (plus /tmp scratch).

## Read first (repo files)

- The definition shards (`def-signed-idempotent`, `def-negative-mass`, `def-visible-set`,
  `def-exposed`, `def-invisible-mass`, `def-height`).
- `argument/lemmas/conj-min-a-w4.md` (the target + W25 body notes);
  `docs/plans/2026-07-06-top-down-proof-sketch-v6.md` M1 block.
- The W25 precedent: `runs/2026-07-06-w25-step4-decider/data/worker-n-report.md` (fact-list
  F0-F8 + the 3x3 model) — YOUR fact-list is that one PLUS true hiddenness (below).
- The reviewed lemmas' contracts (`lem-visible-g-small`, `lem-parametric-halo-collapse`,
  `lem-genuine-disintegration`, `lem-top-concentration`) and the af-validated shards
  (`argument/INDEX.md`); the exact pipeline `runs/2026-07-02-web-regime-hunt/scripts/`.

## The augmented fact-list (what a model must now satisfy)

Everything from W25's F0-F8 (harmonicity of P*1_S for the labeled G; the collapse conclusion at
labeled-hidden tops; the Lemma-A conclusion at labeled-visible rows; the disintegration ledger;
row sums / negative mass / diameter / mass-split / sandwich) PLUS:
(F9) **TRUE HIDDENNESS of every labeled-hidden vertex**: in the REAL row geometry of your model
matrix, t*(v) < kappa = tau/4 — i.e. for every admissible exposer (affine h, h(p_v) = 0,
0 <= h <= 1 on all rows), some row at ell-1 distance >= rho = 4*tau from p_v has h(p_j) < kappa.
NOTE: t*(v) is computable exactly as a finite LP over h (the pipeline's `exposed_tstar` does
this); hard-assert t*(v) < kappa exactly, don't hand-wave it.
(F10) TRUE VISIBILITY of every labeled-visible row (t* >= kappa, exactly), and label consistency:
labeled distances = real distances to conv of the labeled-visible rows.
In other words: the model must now be geometrically HONEST about W and hiddenness — only the
GLOBAL structure (whether such a configuration extends to / behaves like a real tall idempotent)
may still be relaxed, and you must state exactly what remains relaxed (e.g. you may allow the
matrix to be any exact signed idempotent with the labeled quantities, or relax delta-window/H
thresholds — SAY SO item by item).

## Mandates (priority order)

1. **Second insufficiency certificate:** an exact model satisfying F0-F10 with a sustained web
   {g >= 1/2} and (labeled or real) H > 13*tau. If found: even hiddenness is not enough — name
   the NEXT violated true-fact (candidates: hiddenness of the DEEP CARRIER vertices vs only the
   top; the delta-window arithmetic; full entrywise idempotence beyond the modeled identities;
   W-hull convexity/absorption). This steers the whole route.
2. **Forced structure:** if F9 keeps killing your models, extract WHY as a precise statement —
   e.g. "the LP dual of t* < kappa forces a convex combination of rho-far rows within distance
   X of p_v, which with the row facts forces sigma_4 <= f(kappa, tau)" — that statement is the
   proof skeleton, handed to the prover via the orchestrator. Derive the dual form of t*(v) <
   kappa explicitly (it is a finite LP; strong duality applies) — even alone, that dual-witness
   statement is valuable output.
3. Small models first (n = 3..10); exact-Q LP feasibility over the constraints; scale only if
   infeasible; class-infeasibility is forced-structure evidence, never emptiness.

## Discipline (binding)

- Exact Q everywhere; hard-assert EVERY modeled fact incl. the exact t* LPs; print full
  matrices. Tier-tag [T0]/[T1]/[T2]/[T3]. NEVER claim emptiness from failed search.
- Do NOT run `fr` or `bd`. Do NOT `git commit`. Do NOT modify anything under `definitions/`,
  `argument/`, `proofs/`, `report/`, `docs/`, `refs/`, `scripts/`, `.frontier/`, `.beads/`.
- Final answer BEGINS with one verdict line:
  `INSUFFICIENT-EVEN-WITH-HIDDENNESS (certified model: ...; next violated true-fact: ...)` or
  `FORCED-STRUCTURE (statement: ...)` or `OPEN (frontier: ...)` — then the full report.
