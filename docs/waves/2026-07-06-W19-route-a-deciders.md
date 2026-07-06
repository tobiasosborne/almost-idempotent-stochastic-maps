<!--
WAVE: W19 (Route-A deciders after W18: (i) sigma_g > 1/2 exact-feasibility attack at ANY
  height; (ii) per-class hostable-mass disambiguation) — 2026-07-06, session 9, bd aism-213.
WORKERS: two fresh codex exec, mutually blind (prompts in the session scratchpad:
  PROMPT-w19a-sigma-refuter.md, PROMPT-w19b-hostable-mass.md). Worker B answer VERBATIM below;
  worker A full report banked VERBATIM at runs/2026-07-06-w19-sigma-frontier/data/
  worker-report.md (summary + pointer below). Workers ran no fr/bd/git, edited no tracked file.
ORCHESTRATOR: mechanical bank; did NOT judge the mathematics (L5). Worker-B checker exit 0 +
  independent exact recomputation (P_B idempotence, delta, ratio 18400/74551, the self-inclusive
  violation 229/3200 > 1/20). Worker-A script rerun from the banked bundle (exit 0; two
  mechanical re-home patches, W17b precedent) + independent algebraic recomputation of three
  headline matrices; geometric certifications remain worker-asserted (pipeline calibrated
  against two banked exact witnesses).
HEADLINE:
  (B, paper) The folklore per-class "hostable mass = O(tau) poke depth" is NOT provable at any
  nontrivial scale from the current toolkit (only the trivial M_X <= 1+delta); it needs TWO
  missing inputs — a sound exposedness-production rule (B4-FAIL-1-wounded) AND a
  coefficient-poke charge (never previously named). T0 sharpening: the SELF-INCLUSIVE reading
  is exactly CONTRADICTED by banked instance B (rho-component mass 229/3200 > poke value 1/20)
  — any future cluster lemma must exclude self mass. External calibration 0.2468*delta
  (0.0533*tau): consistent with both scales, asymptotics undecided. Consequence table: the
  C/delta and C/tau class counts are NOT blocked by recorded certificates; the multiplicative
  route dies only in the no-nontrivial-bound outcome. Named codification target:
  conj-external-poke-charge(A) (a conjecture, NOT the folklore as written).
  (A, exact) sigma_g > 1/2 NOT-REALIZED-HERE — and the binding constraint is IDENTIFIED:
  EXPOSEDNESS ABSORPTION, not mass capacity (the exact LP relaxation places 5/4 on designated
  recipients; exact geometry then makes them visible, H = 0). New record halo-robust mass
  sigma_g = 5991/80000 ~ 0.075 (rank 5, genuine SELF recipient) — above the W17b census max
  1/25, still ~6.7x below the cap. Duplicate-splitting q = 5/84 over m = 2/4/8 near-coincident
  recipients leaves total sigma_g EXACTLY unchanged (single quotient class — clone-consistency
  realized); the hidden/absorbed frontier on that design sits between 5/84 and 1/16. NOT an
  emptiness claim. NAMED RESIDUAL: geometrically DISTINCT multi-class designs untested — the
  direct empirical probe of B's per-class question and of the W18 C/tau-count opening.
TIER: worker-tagged (T0 exact loci/certificates; T1 short proofs / exact computations;
  T2 gaps/conditional readings). Nothing rigorous; no registry status changed (codification
  follow-up filed in bd).
-->

# W19 — Route-A deciders: sigma_g frontier (exact) + per-class hostable mass (paper)

---

## Worker B — per-class hostable-mass disambiguation (verbatim ANSWER-B.md)

# W19 worker B -- per-class hostable-mass disambiguation

Q1 verdict: [T1] A per-class coefficient bound is provable only in the trivial form `M_X <= 1+nu_v <= 1+delta <= 5/4`; no current definition/proved lemma gives `O(tau)` or `O(delta)` for a hidden genuine recipient cluster.
Q2 verdict: [T2] The folklore scale is not settled. Conditional on an extra coefficient-poke charge it is `O(tau)`; conditional on a row-negativity charge it is `O(delta)`; the exact instance-B lower witness is consistent with both.
Q3 verdict: [T1/T2] CAP-1/2 needs `#classes <= 1/(2*A*delta)` under an `A*delta` per-class bound, `#classes <= 1/(2*A*tau)` under an `A*tau` bound, and is dead by this route with no nontrivial per-class bound. The recorded c10/`obs-fwr-gap` walls block the old `O(1)` quotient-count route, not these delta-dependent counts.

Tier convention: [T0] exact repo locus or exact arithmetic certified by `check_answer_b.py`; [T1] short proof from [T0] inputs and af-validated/proved shards; [T2] named gap/conditional reading; [T3] speculation. I did not read or touch `ANSWER-A.md`. Scratch helper: `waves-scratch/w19-route-a-deciders/check_answer_b.py`, run by `python3 waves-scratch/w19-route-a-deciders/check_answer_b.py`, exits `[check_answer_b] OK`.

## Q1 -- precise statement

[T0] Scales and objects are as in `def-visible-set`, `def-exposed`, `def-height`, and `def-invisible-mass`: `tau=sqrt(delta)`, `rho=4*tau`, `kappa=tau/4`, `W=W(P)`, and `C_W=conv{p_w:w in W}`. A row vertex is hidden iff it is not `(rho,kappa)`-exposed.

[T1] I use this precise cluster definition. For a hidden top vertex `v`, an external genuine recipient cluster `X` is a nonempty set of indices `j != v` such that `P_vj>0`, `dist_1(p_j,C_W)>tau/4`, no member of `X` is in `W` (nonvertices are allowed but not exposed), and the rows in `X` have prescribed diameter `max_{i,j in X} ||p_i-p_j||_1 <= r_X`. Its hosted mass is
`M_X := sum_{j in X} P_vj`.
This external convention is necessary: if self `j=v` is allowed, instance B below makes the rho-component `{3,4}` have mass larger than the natural poke parameter `t*/(1-t*)`.

[T1] The sharpest unconditional statement I can prove from the current validated toolkit is:

`M_X <= sum_j P_vj^+ = 1+nu_v <= 1+delta <= 5/4`.

Proof: `lem-mass-split` gives `sum_j P_vj^+=1+nu_v`; `def-negative-mass` gives `nu_v<=delta`; the working range gives `delta<=1/4`. Since `X` is a subset of positive recipient indices, the displayed inequality follows.

[T1] The residual lemmas do not improve this to a per-cluster bound. `lem-residual-lower` and `lem-residual-upper` are already packaged in `conj-halo-collapse` as
`H*(1-sigma_g) <= (sigma-sigma_g)*tau/4 + nu_v*(2+4*delta)`.
This bounds height once `1-sigma_g` is bounded below; it does not bound `sigma_g`, and therefore does not bound a single `M_X` from above.

[T1] Hiddenness alone is not a coefficient statement. `t*(x)<kappa` says the admissible-exposer margin of row vertex `x` is small after exempting the `rho`-ball. It contains no `P_vj`, and the `rho`-ball exemption is exactly where a near-coincident hidden cluster can sit.

[T2] Minimal extra hypothesis for the folklore `O(tau)` reading: attach to `X` a poke parameter `mu_X>=0` with the same exposedness conversion `t_X=mu_X/(1+mu_X)`, and prove a coefficient-poke charge
`M_X <= A*mu_X`.
If hiddenness gives `t_X<kappa=tau/4`, then
`mu_X < kappa/(1-kappa) = tau/(4-tau) <= 2*tau/7`
because `tau<=1/2`. Hence `M_X <= (2A/7)*tau`.

[T2] Minimal extra hypothesis for the stronger `O(delta)` reading: prove a row-negativity charge such as `M_X <= A*nu_row` with `nu_row<=delta` (for example `nu_row=nu_v`, or a specified sum of negative masses charged to the cluster). No such charge is present in `conj-no-free-frontier`, B4, or the residual lemmas.

## Q2 -- scale

### Upper side

[T1] From Q1 alone, in tau-units,
`M_X/tau <= (1+delta)/tau = 1/tau + tau`.
This is not `O(1)` as `tau -> 0`; therefore the current T1 toolkit gives no `O(tau)` or `O(delta)` ceiling.

[T2] Conditional scales:
If the missing coefficient-poke charge is proved, the bound is `O(tau)`.
If the missing row-negativity charge is proved, the bound is `O(delta)=O(tau^2)`.
Without either charge, the only proved ceiling is constant-scale.

### Lower side: exact instance B

[T0] Instance B is the exact 5x5 witness from `runs/2026-07-02-sigma-cap-refuter/` (`certify_best.py`). The full matrix is

```text
P_B =
[ 31023/32000,      43/16000,       -949/32000,      9/200,       1/80  ]
[ -457/80000,      40017/40000,     -377/80000,      1/200,       1/200 ]
[ -51/1250,        303/80000,       76661/80000,     11/160,      1/100 ]
[ 23129/50000,     -74551/1600000,  819923/1600000, 961/16000,   23/2000]
[ 7770491/12800000,-20353/640000,   4572529/12800000,17831/320000,377/32000]
```

[T0] The checker asserts `P_B^2=P_B`, row sums are `1`, `delta=74551/1600000`, `W=[0,1,2]`, row `v=3` is hidden with `t*(3)=1/21`, and row `4` is a nonvertex genuine outside recipient with
`dist_1(p_4,C_W)=18043832891/258628800000` and `dist_1(p_4,C_W)^2 > delta/16`.

[T0] For the distinct external recipient cluster `X={4}`,
`M_X=P_{3,4}=23/2000`.
Since `tau=sqrt(delta)=sqrt(745510)/4000`,

`M_X/delta = 18400/74551`,

`M_X/tau = 46/sqrt(745510)`, equivalently `(M_X/tau)^2 = 1058/372755`.

Numerically, this is `M_X/delta ~= 0.2468` and `M_X/tau ~= 0.0533`.

[T0] If instead one defines the rho-connected genuine component to include self, then `X={3,4}` because `||p_3-p_4||_1=408483/1280000` and `||p_3-p_4||_1^2 < 16*delta`. Its mass is
`P_{3,3}+P_{3,4}=229/3200`, with

`M_X/delta = 114500/74551`,

`M_X/tau = 1145/(4*sqrt(745510))`, equivalently `(M_X/tau)^2 = 262205/2385632`.

This component includes the hidden top's self coefficient, so I do not use it as the external per-class count for CAP-1/2. It is a warning that any future "cluster" lemma must state explicitly whether self mass is excluded.

[T0/T1] In this same witness, `t*(3)=1/21`, so the formal poke value from `t=mu/(1+mu)` is `mu=1/20`, and `mu<2*tau/7`. The external row-4 mass satisfies `23/2000 < 1/20`, but the self-including rho-component mass satisfies `229/3200 > 1/20`. This calibrates the ambiguity; it does not prove a charge law.

[T2] Lower-scale verdict: instance B proves a finite exact lower calibration of order `0.2468*delta` for a distinct external recipient, but it does not decide asymptotics. I did not find or build an exact one-cluster family with `M_X/delta -> infinity` and `M_X/tau` bounded below; such a family would refute the `O(delta)` reading. I also did not find a family with constant-scale hosted mass while staying hidden and genuine.

## Q3 -- CAP-1/2 consequence table

[T1] Suppose `N(v)` is the number of geometrically distinct external genuine hidden recipient classes hit by `P_v^+`, counted quotient-wise rather than by raw indices.

| per-class outcome | CAP-1/2 class count needed | do c10 / `obs-fwr-gap` block it? |
|---|---:|---|
| [T2] `M_X <= A*delta` | [T1] `N(v) <= 1/(2*A*delta)` | [T1/T2] Not blocked by the recorded certificates. The cloning obstruction kills raw-index counts, and `obs-fwr-gap` says F-WR gives no dimension-free quotient cap, but neither refutes a `C/delta` quotient cap. |
| [T2] `M_X <= A*tau` | [T1] `N(v) <= 1/(2*A*tau)` | [T1/T2] Also not blocked as stated. B4's old composition needed `O(1)` classes to turn `(#classes)*O(tau)` into `O(tau)` or a bound away from `1` by a fixed mechanism. CAP-1/2 can tolerate `C/tau` classes. |
| [T1] only `M_X <= O(1)`, or no nontrivial per-class bound | [T1] an `O(1)` quotient-class cap, or a different total-mass argument | [T1/T2] This is exactly where the recorded dead routes bind: c10/cloning forces quotient quantities, and `obs-fwr-gap` says the nearest web-rigidity machinery cannot merge dimension-many simplex-corner classes or supply a dimension-free cap. Multiplicative Route A is dead in this outcome. |

[T1] Therefore W18 Q2(b)'s correction is load-bearing: CAP-1/2 does not need the old dimension-free class count if the per-class ceiling is `O(tau)` or `O(delta)`. It needs a quantitative quotient packing bound at the matching scale.

## Q4 -- honest status and codification target

[T1] A version of the per-class bound is provable now only in the trivial mass-split form `M_X<=1+delta`. This is not useful for CAP-1/2.

[T2] No nontrivial `O(tau)` or `O(delta)` per-class hostable-mass lemma is currently T1-provable from the validated/mod-audit toolkit I checked. The folklore sentence in `conj-no-free-frontier` is conditional on two separate missing pieces: a sound exposedness-production rule (B4 FAIL-1 wounded the literal uniform `kappa=tau/4` pointwise rule), and a coefficient charge connecting the geometric poke depth to `P_vj^+` mass.

[T2] The single sharpest lemma worth codifying is not the folklore as written. A precise conjectural obligation would be:

`conj-external-poke-charge(A): For every exact signed idempotent P with 0<delta<=1/4, nonempty W, hidden top v, and every external genuine hidden recipient cluster X with a specified same-direction poke parameter mu_X satisfying t_X=mu_X/(1+mu_X)<kappa, one has sum_{j in X} P_vj <= A*mu_X.`

[T2] This would imply the `O(tau)` per-class ceiling immediately by the arithmetic in Q1. It must exclude self mass or carry a separate self-mass clause, because instance B's rho-component `{3,4}` has mass `229/3200 > 1/20 = t*(3)/(1-t*(3))`.

[T1] If the project wants only a proved shard today, the honest statement is the trivial one:

`lem-external-cluster-mass-trivial: For any exact signed idempotent P and any row v, every positive-recipient cluster X satisfies sum_{j in X} P_vj^+ <= 1+nu_v <= 1+delta(P).`

[T1] I would not codify a nontrivial per-class hostable-mass lemma yet; codify the poke-charge conjecture or leave the folklore uncodified with this gap named.

---

## Worker A — sigma_g > 1/2 exact-feasibility attack (summary; full report banked in the bundle)

Full report incl. every exact matrix and the 57-item assert list:
`runs/2026-07-06-w19-sigma-frontier/data/worker-report.md`. Rerun:
`python3 runs/2026-07-06-w19-sigma-frontier/scripts/w19_worker_a.py` (exit 0).

- **NOT-REALIZED-HERE** (explicitly not an emptiness claim). Best certified halo-robust mass:
  `sigma_g = 5991/80000 ~ 0.075` (rank 5, the genuine recipient is the hidden top ITSELF at
  `dist > tau/4`; `delta = 3983/96000`); best rank-3 distinct-partner point `229/3200`
  (= banked instance B, recomputed).
- **Binding constraint identified: exposedness absorption.** The exact LP relaxation
  (row-negativity + nonnegativity only) reaches designated outside mass `5/4`; the exact
  optimizer's geometry has `W = [3,4,5]`, `H = 0` — the recipients became visible. Mass
  capacity is NOT the wall.
- **Duplicate-split family:** hidden-column mass `q = 5/84` spread over m = 2, 4, 8
  near-coincident recipients gives total `sigma_g = 5/84` for every m (one quotient class);
  raising `q` to `1/16` flips the recipients into `W` (`H = 0`). The hidden/absorbed frontier
  on this design lies in `(5/84, 1/16]`.
- Pipeline calibrated against the banked F2 sigma-halo-nonrobust anchor (raw sigma
  `5343/5000`, `sigma_g = 0`) and instance B.

## Orchestrator actions (mechanical)

1. Worker-B checker exit 0; independent exact recomputation of the instance-B arithmetic
   (idempotence from the printed matrix, delta, external ratio `18400/74551`, and the
   self-inclusive violation `229/3200 > 1/20`).
2. Worker-A rerun from the banked bundle exit 0 (re-home patches documented in the bundle
   README); independent algebraic recomputation of three headline matrices
   (`runs/2026-07-06-w19-sigma-frontier/scripts/orchestrator_recompute.py`).
3. No registry/status change. Follow-ups filed in bd: codify `conj-external-poke-charge(A)`;
   distinct-multi-class sigma_g optimization (the named residual of both workers jointly).
