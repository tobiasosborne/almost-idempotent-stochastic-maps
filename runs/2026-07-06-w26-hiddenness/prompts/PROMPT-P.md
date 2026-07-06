# W26 Worker P — PROVE conj-min-a-w4 by consuming HIDDENNESS

You are a fresh, independent worker in the repo `/home/tobias/Projects/almost-idempotent-stochastic-maps`
(mathematical exploration of almost-idempotent stochastic maps; signed-idempotent picture). This is a
prove attempt on THE frontier conjecture, with the one previously-missing input now explicitly in
scope. A hostile verifier will check any claimed proof; a mutually-blind colleague attacks from the
insufficiency side — do not read or write anything under `runs/2026-07-06-w26*` or other workers'
files; write nothing to the repo (scratch under /tmp only).

## Read first (repo files)

- `definitions/def-signed-idempotent.md`, `def-negative-mass.md`, `def-visible-set.md`,
  `def-exposed.md`, `def-invisible-mass.md`, `def-height.md`.
- `argument/lemmas/conj-min-a-w4.md` — THE target, incl. its W25 body notes.
- `docs/plans/2026-07-06-top-down-proof-sketch-v6.md` — the M1 block (round-3 state).
- IMPORTABLE (quote contracts verbatim; black boxes): reviewed `lem-visible-g-small`,
  `lem-parametric-halo-collapse`, `lem-genuine-disintegration`, `lem-top-concentration`,
  `lem-kernel-implies-hlc`; ALL af-validated shards in `argument/INDEX.md`. First-principles
  derivations from the definition shards always allowed. FORBIDDEN imports: anything heuristic /
  proved-mod-audit / stated (incl. `obs-deep-leakage`, `lem-canonical-separator`,
  `lem-exposed-circuit`, `thm-well-exposed` — re-derive if needed).
- Context you must NOT contradict: the W25 insufficiency certificate
  (`runs/2026-07-06-w25-step4-decider/data/worker-n-report.md`) — any valid proof MUST use
  hiddenness (or another true fact outside the old list); if your draft never uses it, it is wrong.

## The target (contract, verbatim)

(CONJECTURE) MIN-A at width 4: for every exact signed idempotent P with
0 < delta(P) <= (17-12*sqrt(2))/2, nonempty visible set W(P), and height H > 13*tau
(tau = sqrt(delta)), some hidden top vertex v has sigma_4(v) <= 1/2, where sigma_4(v) is the
positive coefficient mass v places on rows at ell-1 distance > 4*tau from conv{p_w : w in W}.

(Equivalent-by-contradiction working form, given the imports: derive ANY contradiction from
"every hidden top has sigma_4 > 1/2" + H > 13*tau — the parametric collapse already forces the
antecedent in tall configs, so proving the conjecture = proving tall configs are impossible.)

## THE NEW INPUT — hiddenness, and how to make it quantitative

A hidden vertex v has t*(v) < kappa = tau/4: for EVERY admissible exposer h (affine, h(p_v) = 0,
0 <= h(p_j) <= 1 on all rows), SOME row with ||p_j - p_v||_1 >= rho = 4*tau has h(p_j) < kappa.
Recommended first move — make this a POSITIVE statement via LP/convex duality: t*(v) is the value
of a linear program over affine h; derive its dual. Expected shape (derive it yourself, carefully —
this is the load-bearing step): t*(v) < kappa yields a convex-combination WITNESS — weights on the
rho-far rows (and possibly the [0,1] box constraints) certifying that p_v is nearly "surrounded":
some convex combination of far rows (plus slack from the box) approximates p_v within a
kappa-controlled error. That witness is a GEOMETRIC object the old fact-list lacked: it ties the
hidden top to its far rows. Candidate uses:
- Combine the witness with `lem-top-concentration` (the top's own mass is nearly all on G_4) and
  `lem-genuine-disintegration` (deep mass sits on hidden vertices): the far rows in the witness
  are themselves at controlled distances; feed them back through row reproduction / the residual
  lemmas (`lem-residual-upper`/`-lower` af-validated) to trap H.
- The two-observable pairing: g = P*1_{G_4} (mass) and the affine deficit H - phi (from
  lem-top-concentration's support functional, first principles). The witness gives a THIRD
  object. Look for the inequality triangle among them.
- Iterate structurally, not dynamically: hiddenness holds at EVERY hidden vertex (in particular
  every deep hidden vertex carrying disintegrated mass), not just the top. Applying the witness
  at each deep vertex may cascade — but remember P^t = P: any "cascade" must be a finite
  structural argument (e.g. an extremal/minimal-counterexample choice), never a mixing limit.

## Honesty rails

- If you cannot close: the sharpest PARTIAL + a precise GAP statement is a success. Candidate
  partials worth having: the dual-witness lemma itself (clean statement + proof — codifiable);
  the cap under an extra hypothesis (e.g. all deep hidden vertices within distance X of the top);
  a proof for rank <= r or for a single quotient class.
- Recorded walls (evade honestly): one-sided ledgers; class counting; exposedness PRODUCTION
  (you may consume hiddenness/exposedness as defined, never manufacture exposedness); cloning
  (clone-invariant quantities only); sterile iteration.
- Tier-tag every step ([T0]/[T1]/[T2]); constants explicit and exact.
- Do NOT run `fr` or `bd`. Do NOT `git commit`. Do NOT modify ANY repo file.
- Final answer BEGINS with one verdict line:
  `PROVED (conj-min-a-w4)` or `PARTIAL (proved: ...; gap: ...)` or `GAP (missing: ...)` —
  then the complete derivation.
