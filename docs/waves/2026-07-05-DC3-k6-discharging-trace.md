<!--
WAVE: decision-check DC3 (K<1>6 master-decomposition discharging trace) — 2026-07-05, session 8.
WORKER: fresh codex exec (prompt: session scratchpad PROMPT-dc3-k6-trace.md). Worker answer VERBATIM below.
ORCHESTRATOR: worker script rerun clean (exit 0, all hard asserts). Headline: the additive
  three-term master shape of sketch K<1>6 is RED as written — (R2) FanRes > 0 REALIZED (T0) on the
  D6 legal-leak instances while the master formula has no FanRes term; (R3) silent rows REALIZED
  (T0) with NO sketch tribe (D3 centered fan p,m; D6 p_B); (R1) double-charge interface risk
  REALIZED at T1 on the G13 stress rows (registered-silent high-self rows chargeable through both
  the C_RH budget and the naked delta term). Worker's nesting-aware restatement is T2 (proposal).
TIER: T0 traces/certificates; T1 R1 interface reading; T2 proposed restatement.
-->

# DC3 K<1>6 master-decomposition discharging trace

Tier legend used here: T0 = exact repo-file reconstruction or exact Fraction arithmetic in this script; T1 = elementary bookkeeping from T0 definitions; T2 = proposed restatement/inference; T3 = speculation. No T3 claim is used.

## Scope and rule audit

- [T0] I used only tracked repo files as sources and wrote only under `waves-scratch/dc3-k6-trace/`.
- [T0] I did not run `fr`, `bd`, or mutable `git` commands.
- [T0] Certificate arithmetic is exact `fractions.Fraction`; every listed instance hard-asserts `B*L=I_3`, `P^2=P`, row sums, cap, chosen theta-half `Phi`-argmin, and chosen maximal pivot.

## Classification rules used

- [T0] Registered terms are read from `argument/lemmas/conj-sc.md` and `argument/lemmas/conj-rh.md`: fan rows are beta-positive leaking rows with a volume-permitted negative one-row cover; active orphans are beta-positive, `E_s>0`, strict legal, and have no volume-permitted negative cover; lambda-positive orphans are the same legal/no-negative-cover case with `mu_s>0,E_s=0`; silent rows are beta-positive rows for which every active-preserving cover containing the row and keeping `u_s` has Schur factor at most `1/2`; B-carriers are rows with `beta_r(i)>0` and `a_s(i)<0` for a transverse `r`.
- [T1] I implemented volume permission as `Schur factor * m_U >= 1/2`, where `m_U=Vol(U)/Vol_max`, matching the theta-half chart condition used in the wave records. Strict legal one-row covers use `>1/2`; no equality case occurred in the traced rows.
- [T2] The sketch tribe rule is the literal K<1>1 wording from `docs/plans/2026-07-04-top-down-proof-sketch.md`: fan-financed first, orphan next, self-supported when `P_jj>1/2` (the wave-record empirical threshold; the registry has no pinned threshold), otherwise no sketch tribe. B-carriers that are not `Phi_s` demand rows are marked auxiliary.

## Zoo summary and FanRes hunt

| instance | delta | U | s | Phi_s | FanRes_s(U) | G+S+SIGMA | FanRes verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G12 calibration | 1/4 | (0, 1, 2) | 2 | 1/36 | 0 | 1/4 + 0 + 2495/24624 = 8651/24624 | GREEN FanRes=0 |
| G13 insert-y=681/10000 | 55319/1000000 | (0, 2, 4) | 2 | 219870541/7880000000 | 0 | 0 + 82401/1576000000 + 19988231/2000000000 = 3958281757/394000000000 | GREEN FanRes=0 |
| G13 two-carrier-B | 99/1250 | (0, 2, 4) | 2 | 1951/50000 | 0 | 213/50000 + 0 + 2124639/312500000 = 3455889/312500000 | GREEN FanRes=0 |
| obs-orphan-amplifier h=1/10 | 7/30 | (0, 1, 2) | 2 | 1/10 | 0 | 1/10 + 0 + 7/60 = 13/60 | GREEN FanRes=0 |
| obs-orphan-amplifier h=1/20 | 27/110 | (0, 1, 2) | 2 | 7/40 | 0 | 1/20 + 0 + 27/220 = 19/110 | GREEN FanRes=0 |
| obs-orphan-amplifier h=1/100 | 637/2550 | (0, 1, 2) | 2 | 47/200 | 0 | 1/100 + 0 + 637/5100 = 172/1275 | GREEN FanRes=0 |
| D3 centered fan | 1/10 | (0, 1, 2) | 2 | 1/20 | 0 | 0 + 0 + 1/20 = 1/20 | GREEN FanRes=0 |
| D6 legal-leak A | 10/41 | (1, 2, 3) | 2 | 10/41 | 1649713/2870000 | 10/41 + 0 + 25041/336200 = 107041/336200 | RED FanRes>0 |
| D6 legal-leak B | 1217/5000 | (1, 2, 3) | 2 | 4659/20000 | 2077/4000 | 561/2500 + 171/20000 + 480961/5000000 = 1645711/5000000 | RED FanRes>0 |

- [T0] The all-existing-certificates-have-`FanRes=0` claim is refuted on this zoo: `D6 legal-leak A, D6 legal-leak B` have exact positive `FanRes_s(U)`.
- [T0] Because `FanRes>0` is already realized, I did not run an additional construction hunt; the prompt requested that only if all zoo values were zero.

## Row-level red/green discharging trace

### G12 calibration

| row | exact row data | K<1>1 tribe | registered class | paying term(s) | flags |
| --- | --- | --- | --- | --- | --- |
| 3:j | beta_s=5/12; E=1/15; mu=1/3; self=11/36; nu=499/2052 | orphan | active orphan | C_RH budget | FanRes row=0; GREEN exact-once under chosen route |
| 4:k | beta_s=0; E=0; mu=0; self=2/3; nu=1/45 | self-support carrier (auxiliary) | B-carrier(r=1) | self-support delta term | FanRes row=0; AUX B-carrier not Phi_s demand |

### G13 insert-y=681/10000

| row | exact row data | K<1>1 tribe | registered class | paying term(s) | flags |
| --- | --- | --- | --- | --- | --- |
| 1:c1 | beta_s=19988231/40000000; E=11/197; mu=8/197; self=203/400; nu=1/50 | self-supported | silent | C_RH/SC budget; self-support delta term | FanRes row=0; RED R1 double-charge risk; R3 registered-silent taxonomy |
| 3:j | beta_s=-7/400; E=0; mu=0; self=343/500; nu=2666319/50000000 | self-support carrier (auxiliary) | B-carrier(r=1) | self-support delta term | FanRes row=0; AUX B-carrier not Phi_s demand |

### G13 two-carrier-B

| row | exact row data | K<1>1 tribe | registered class | paying term(s) | flags |
| --- | --- | --- | --- | --- | --- |
| 1:c1 | beta_s=193149/250000; E=5/99; mu=4/99; self=3911/5000; nu=11/1250 | self-supported | silent | C_RH/SC budget; self-support delta term | FanRes row=0; RED R1 double-charge risk; R3 registered-silent taxonomy |
| 3:j | beta_s=-99/5000; E=0; mu=0; self=3201/5000; nu=1629/50000 | self-support carrier (auxiliary) | B-carrier(r=1) | self-support delta term | FanRes row=0; AUX B-carrier not Phi_s demand |

### obs-orphan-amplifier h=1/10

| row | exact row data | K<1>1 tribe | registered class | paying term(s) | flags |
| --- | --- | --- | --- | --- | --- |
| 3:o0 | beta_s=1/4; E=1/5; mu=2/5; self=5/12; nu=7/30 | orphan | active orphan | C_RH budget | FanRes row=0; GREEN exact-once under chosen route |
| 4:o1 | beta_s=1/4; E=1/5; mu=2/5; self=5/12; nu=7/30 | orphan | active orphan | C_RH budget | FanRes row=0; GREEN exact-once under chosen route |

### obs-orphan-amplifier h=1/20

| row | exact row data | K<1>1 tribe | registered class | paying term(s) | flags |
| --- | --- | --- | --- | --- | --- |
| 3:o0 | beta_s=1/4; E=7/20; mu=9/20; self=5/11; nu=27/110 | orphan | active orphan | C_RH budget | FanRes row=0; GREEN exact-once under chosen route |
| 4:o1 | beta_s=1/4; E=7/20; mu=9/20; self=5/11; nu=27/110 | orphan | active orphan | C_RH budget | FanRes row=0; GREEN exact-once under chosen route |

### obs-orphan-amplifier h=1/100

| row | exact row data | K<1>1 tribe | registered class | paying term(s) | flags |
| --- | --- | --- | --- | --- | --- |
| 3:o0 | beta_s=1/4; E=47/100; mu=49/100; self=25/51; nu=637/2550 | orphan | active orphan | C_RH budget | FanRes row=0; GREEN exact-once under chosen route |
| 4:o1 | beta_s=1/4; E=47/100; mu=49/100; self=25/51; nu=637/2550 | orphan | active orphan | C_RH budget | FanRes row=0; GREEN exact-once under chosen route |

### D3 centered fan

| row | exact row data | K<1>1 tribe | registered class | paying term(s) | flags |
| --- | --- | --- | --- | --- | --- |
| 3:p | beta_s=1/4; E=1/10; mu=1/10; self=1/4; nu=1/10 | NONE: silent gap | silent | C_RH/SC budget | FanRes row=0; RED R3 no sketch tribe; R3 registered-silent taxonomy |
| 4:m | beta_s=1/4; E=1/10; mu=1/10; self=1/4; nu=1/10 | NONE: silent gap | silent | C_RH/SC budget | FanRes row=0; RED R3 no sketch tribe; R3 registered-silent taxonomy |

### D6 legal-leak A

| row | exact row data | K<1>1 tribe | registered class | paying term(s) | flags |
| --- | --- | --- | --- | --- | --- |
| 4:m_A | beta_s=12459/41000; E=4/5; mu=4/5; self=28459/41000; nu=10/41 | fan-financed | fan row | fan term; explicit FanRes term needed | FanRes row=18709/51250; RED R2 FanRes missing from master formula |
| 5:p_B | beta_s=1/1000; E=1/10; mu=1/10; self=1/1000; nu=15/82 | NONE: silent gap | silent | C_RH/SC budget | FanRes row=0; RED R3 no sketch tribe; R3 registered-silent taxonomy |
| 6:m_B | beta_s=1/1000; E=7/10; mu=7/10; self=1/1000; nu=15/82 | fan-financed | fan row | fan term; explicit FanRes term needed | FanRes row=602009/2870000; RED R2 FanRes missing from master formula |

### D6 legal-leak B

| row | exact row data | K<1>1 tribe | registered class | paying term(s) | flags |
| --- | --- | --- | --- | --- | --- |
| 4:m_A | beta_s=381/1000; E=3/5; mu=3/5; self=609/1000; nu=1217/5000 | fan-financed | fan row | fan term; explicit FanRes term needed | FanRes row=2077/4000; RED R2 FanRes missing from master formula |
| 5:p_B | beta_s=29/1000; E=3/20; mu=3/20; self=17/1000; nu=149/1250 | NONE: silent gap | silent | C_RH/SC budget | FanRes row=0; RED R3 no sketch tribe; R3 registered-silent taxonomy |

## Composition verdict

- [T0] R2 is realized, not hypothetical: D6 legal-leak A and B have positive exact `FanRes_s(U)`, while K<1>6's written master formula has no `FanRes` term.
- [T0] R3 is realized on exact silent rows. D3 centered fan has beta-positive leaking rows `p,m` registered as silent, with no fan-financed/orphan/self-supported sketch tribe under the stated rule. D6 also has a degenerate/silent `p_B` row in each traced certificate.
- [T1] R1 is realized as an interface risk on the G13 stress rows: the high-self leaking row is registered silent/NF_s, so `conj-sc`/`conj-rh` would charge it through the shared `C_RH` budget, while the sketch's self-support horn also routes it to the naked delta term via PRT/NSC.
- [T1] Therefore the additive three-term master shape is RED as written: the row ledger is not exactly-once unless the assembly is restated to be nesting-aware and to include or discharge `FanRes`.

## Minimal proposed K<1>6 restatement

[T2] Proposed contract sentence, supported only as an audit target, not as a proof:

> For a capped theta-half `Phi`-argmin chart and maximal pivot `s`, decompose beta-positive demand by a verified disjoint registered partition: fan-cover rows, active/lambda orphan rows, silent/high-self NF rows, and transverse B-carrier auxiliary charges; assemble `Phi_s` by first applying the nested `SC -> RH` route to all non-fan `NF_s` demand (including silent/high-self rows), then add the fan-cover payment with its explicit `FanRes_s(U)` residual, and add the `B`/NSC naked-delta term only for auxiliary B-carrier mass not already counted as `NF_s` demand.

[T2] Minimal edits implied by the trace: (i) make the SC-to-RH nesting explicit, so self-support demand is not also added as a sibling term; (ii) include an explicit `+ C_fan*FanRes_s(U)` term or prove a separate `FanRes_s(U)=O(delta)` lemma; (iii) either prove silent rows are covered by the nested NF route or add a fourth silent-row clause.

## Rerun command

```bash
python3 waves-scratch/dc3-k6-trace/dc3_k6_trace.py
```

## Scratch artifacts

- `waves-scratch/dc3-k6-trace/dc3_k6_trace.py`
- `waves-scratch/dc3-k6-trace/REPORT.md`

## Hard asserts

Per instance (all nine zoo instances): `B*L=I_3`; `P^2=P`; every row sum is `1`; `delta <= 1/4`;
displayed `delta`; chosen `U` is a theta-half `Phi`-argmin; chosen `U` is theta-half; chosen `s`
is a maximal pivot; displayed `Phi` vector; displayed `B_{1,2}` (where applicable); cross-pivot
cancellation `A=B+C-D` for `r=0` and `r=1`. (Full 100-line assert list in the worker's
`waves-scratch/dc3-k6-trace/REPORT.md`; script rerun exit 0 confirmed by the orchestrator.)
