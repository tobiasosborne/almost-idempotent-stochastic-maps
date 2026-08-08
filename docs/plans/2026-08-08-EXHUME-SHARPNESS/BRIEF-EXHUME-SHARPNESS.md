# BRIEF — design the sharpness-at-T0 package (ex-hume rescope / prh-sharpness route)

You are a fresh design worker (independent context). Deliver a land-ready
package that puts **sharpness of the exponent 1/2 in `op-classical`** on
the af-validated (T0) rung. `op-classical` itself (the upper bound) is
already `proved`/`af: validated`; sharpness is the last mathematical claim
of the PRD headline below T0.

## The problem with the landed `ex-hume`

`argument/lemmas/ex-hume.md` (`proved-mod-audit`, `af: seeded` at the OLD
contract) asserts the family's "distance to every stochastic idempotent
IS 2s-2s^2+2s^3" — literally false as quantified (a single value cannot be
the distance to EVERY stochastic idempotent; e.g. distances to different
idempotents differ; distance to the SET is intended). The paper's
faithfulness audit (docs/plans/2026-08-08-PAPER/AUDIT-PAPER.md finding 3)
prescribed and verified the corrected form now in `paper/main.tex` §5:
for 0<s<1, dist_{inf->inf}(P_s, I_stoch) = 2s-2s^2+2s^3; normalizing
rows' positive parts gives row-stochastic Q_s with
||P_s-Q_s|| <= 2s^2 and ||Q_s^2-Q_s|| <= 6s^2+4s^4; hence every stochastic
idempotent F has ||Q_s-F|| >= 2s-4s^2+2s^3 = 2s(1-s)^2, excluding every
exponent beta>1/2. Also note the contract's "op-npps" mention (out of
scope here) and the eponym question (registry id stays `ex-hume`; prose
should not lean on an uncitable name).

## A second route already in the registry

`argument/lemmas/lem-prh-sharpness.md` (`proved-mod-audit`, `af: none`,
NO deps, hostile-verified paper proof W74F): for every 0<lambda<1/2 there
are positive unital A: l_inf^2 -> l_inf^4, M: l_inf^4 -> l_inf^2 with
epsilon_lambda = ||MA-I_2|| = 2*lambda^2 such that EVERY stochastic
idempotent F on l_inf^4 has ||AM-F|| >= lambda = sqrt(epsilon_lambda/2).
Observe: Q_lambda := AM is itself row-stochastic and
(AM)^2 - AM = A(MA-I)M gives a defect bound O(lambda^2) — this is already
an op-classical-shaped sharpness witness with clean quantifiers.

## Task

Choose the route (or a combination) that reaches T0 sharpness with the
LEAST contract churn and the smallest sound af trees, and design it fully:

- If you rescope `ex-hume`: the corrected contract must be the
  distance-to-set / for-every-F lower-bound form with the explicit 0<s<1
  domain, the explicit stochastic witness Q_s, and a conclusion of the
  form "for no C, beta with beta>1/2 does ||Q-E|| <= C*eta^beta hold for
  all admissible row-stochastic Q" (phrase the negative precisely and
  dischargeably — a family statement plus an explicit no-uniform-bound
  corollary is acceptable; avoid undischargeable meta-quantification over
  'all proofs'). Handle the landed shard honestly (supersession recorded
  in provenance; old contract quoted as history; clean re-seed — the
  existing proofs/ex-hume workspace was seeded at the OLD contract and
  MUST be discarded/re-seeded, never resumed).
- If you go through `lem-prh-sharpness`: design its elevation (its
  contract looks clean — verify every constant against the W74F source
  PROOF-W74F-A-PRH.md sect-7) plus the small sharpness corollary row
  (e.g. `cor-classical-sharpness`) whose contract states the
  op-classical-facing negative; wire deps minimally (only on T0-elevable
  rows; `lem-classical-equiv` (T0) is available if a signed bridge is
  genuinely needed — but prefer the direct stochastic witness).
- You may also do BOTH (rescue ex-hume for the historical 3x3 family AND
  the corollary); justify the registry-surface cost if so.

## Hard constraints

1. All quantifiers explicit and dischargeable; no "distance to every X is
   <one value>" phrasing anywhere; every constant verified against its
   source (paper sect-5 formulas / W74F sect-7 / docs/ingest).
2. Deps only on rows that are T0 or elevated within your package;
   acyclic; budgets honest under the 1.5-3x expansion, hard cap <= 26 per
   target (prefer much smaller — these are explicit finite computations).
3. Statuses at landing: every new/rescoped row `stated`/`af: none` (or
   `proved-mod-audit` ONLY where the W74F hostile verdict literally
   covers the byte-identical statement — argue it if claimed); nothing
   promoted by the design.
4. Seeding packages byte-exact (def-add lists; externals at literal
   proofs/<id> paths); enumerate silently-invoked textbook facts (the
   census discipline — explicit 3x3/4x4 matrix arithmetic, l_inf operator
   norm as max row l_1 norm, etc.).
5. Landing manifest complete (Rule 9): UNWIRED entries, report
   PRD/sketch touches, the paper's §5 consistency (the paper must remain
   faithful to whatever contracts land), regenerations, gates.
6. The `op-classical` shard and every T0 row are UNTOUCHABLE except
   (optionally) adding a body-text pointer sentence — no contract or
   deps edit of any validated row.

## Inputs you MUST read

- `argument/lemmas/ex-hume.md`, `argument/lemmas/lem-prh-sharpness.md`,
  `argument/lemmas/lem-prh.md`, `argument/lemmas/thm-rank-one.md`,
  `argument/lemmas/lem-classical-equiv.md`, `argument/lemmas/op-classical.md`
- `paper/main.tex` §5 + `docs/plans/2026-08-08-PAPER/AUDIT-PAPER.md` finding 3
- `docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md` §7 and its
  batch verdict; `docs/ingest/README.md` rows for ex-hume/thm-rank-one
- `definitions/def-stochastic.md`, `def-signed-idempotent.md`,
  `def-positive-approximate-retract.md`, `def-almost-idempotent.md`
- `CLAUDE.md` §§1, 6; `FINDINGS.md` 2026-08-08; `scripts/af_constants.py`

## Deliverable

Write EXACTLY ONE file:
`docs/plans/2026-08-08-EXHUME-SHARPNESS/DESIGN-EXHUME-SHARPNESS.md` with:
(a) the route decision + justification; (b) complete land-ready shard
text for every new/rescoped row; (c) verified-constants table (formula vs
source locus); (d) af skeletons + budgets per target; (e) seeding
packages + fact census; (f) landing manifest; (g) elevation order;
(h) ranked risks for the fresh hostile audit (include: quantifier
dischargeability of the negative statement; the distance-to-set
computation's lower-bound direction; the Q_s defect constant; supersession
honesty; workspace re-seed discipline).

Head the file with: `Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD,
SEED, OR PROMOTE — pending fresh hostile audit and user ratification.`

## Discipline (non-negotiable)

Write ONLY the deliverable file. No edits to `argument/`, `definitions/`,
`proofs/`, `paper/`, `report/`. No git commit/push. No `af` mutations.
Final message: <=8 lines — route chosen, row count, budgets, any contract
you rescope.
