<!--
ROLE: adversarial exploration wave for arm G wave 2: circulation deciders
against the negative-side legal circulation candidate.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 2
answers: bd aism-6tt
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g2_deciders.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: gap-1 orphan row UNDECIDED; pure-legal C_legal=0 SURVIVED the
certified D6 replay plus one exact near-threshold family, with worst new
Task-B ratio 814/2149 and worst replay ratio 4593717/10385000; finite
C_legal SURVIVED these families; two-block hole UNDECIDED. No amplifying
family was certified, so the reshaped kill criterion did not trigger.
-->

# Arm G Wave 2: Circulation Deciders

Read inputs, in the requested order: G1, D6, D5, D4, A9, A8, and the
2026-07-03 entries of `FINDINGS.md`. [T0]

The checker rebuilt exact signed idempotents from displayed `L,B` data and
asserted, for every certified row below,

```text
B L = I,       P = L B,       P^2 = P,       P 1 = 1.
```

It enumerated every actual-row chart with volume at least half the maximum,
computed the full `Phi` vector, and accepted a target chart only when its
maximal `Phi` equalled the exact minimum over that theta-half family. It also
computed `delta(P)`, `L_mu`, `F_L`, `G_class^-`, `S_-^mu`, `R_D^nu`, and the
same-pivot Schur collateral `C_s(j,t)` from the A9 formula. No discrepancy
with the displayed D6/G1 values was found. [T0]

## T0. Baseline Replay

D6 Certificate A replay:

```text
delta = 10/41,
theta-half argmin chart = (e1,e2,p_A),
Phi = (0, 6/41, 10/41),
legal rows = {m_A,m_B},      D rows = {p_B}.
```

The fan-matched negative-coordinate collateral gives

```text
L_mu + F_L = 99959/410000,
sum w C_s = 1649713/2870000,
(L_mu+F_L)/(sum w C_s) = 36827/86827.
```

D6 Certificate B replay:

```text
delta = 1217/5000,
theta-half argmin chart = (e1,e2,p_A),
Phi = (0, 19/500, 4659/20000),
legal rows = {m_A},          D rows = {p_B}.
```

The legal import leak is included:

```text
L_mu = 1143/5000,
F_L  = 21717/20000000,
sum w C_s = 2077/4000,
(L_mu+F_L)/(sum w C_s) = 4593717/10385000.
```

Thus the G1 telescope is exactly reproduced: both certified D6 leaks are paid
by same-pivot collateral before any `C_legal` budget is spent. [T0]

## T0. Gap 1 Orphan-Row Hunt

Target property: a strict legal beta-positive H-M row `j` with `mu_j>0` whose
all volume-permitted transverse coordinates are positive. Then
`a_t(j)^-=0` at every legal one-row position, so G1's fan-matched financing
family at `j` is empty. [T0/T1]

I ran an exact rank-3 balanced-pair search with chart `(e1,e2,p_A)`, pivot
`p_A`, and an asymmetric candidate row whose chart coordinates were

```text
(p, -e, 1-p+e),      p>1/2, 0<e<1/2.
```

The grid used

```text
p in {3/10,4/10,5/10,6/10,7/10,8/10},
e in {1/10,2/10,3/10,4/10},
pair mass q in {1/20,1/10,1/5},
c_1 in {0,1/50,1/20,1/10,1/5},
c_2 in {-1/5,-1/10,-1/20,0,1/20,1/10,1/5}.
```

Every candidate was filtered by exact `delta<=1/4` and the theta-half argmin
certificate. No certified orphan row occurred in this finite grid. [T0]

This does **not** prove orphan rows are unrealizable. The grid failure is only
evidence that the simple balanced-pair ansatz tends either to lose the argmin
or to introduce a volume-permitted negative coordinate. I do not have the
elementary implication

```text
beta_j>0, mu_j>0, strict legal at a theta-half argmin
  => some volume-permitted coordinate has a_t(j)<0.
```

That implication remains a real T2 proof target. [T2]

## T0. Near-Threshold Stress

To push the fan weight against the legal threshold, I used the exact two-scale
constructor but changed the legal coordinate to be barely strict:

```text
A=11/40, B=11/80,
m_A=499/1000, m_B=1/1000,
c_A=1/10, c_B=0.
```

For the chart `(e1,e2,p_A)`, pivot `p_A`,

```text
delta = 979/4000 <= 1/4,
Phi = (0, 1/100, 979/4000),
theta-half argmins = (e1,e2,p_A), (e1,e2,m_A).
```

The legal row is

```text
a(m_A)=(-11/20, 11/20, 1),
beta(m_A)=111/250,
mu(m_A)=11/20.
```

The exact ledger is

```text
L_mu + F_L = 1221/5000,
sum w C_s = 6447/10000,
(L_mu+F_L)/(sum w C_s) = 814/2149.
```

The boundary stress did not amplify. In this rank-3 family the negative legal
coordinate is the only negative coordinate, so the fan weight is still `1`;
this does not decide the higher-rank dilution mechanism where nonlegal
negative coordinates enlarge `mu_j`. [T0/T1]

The finite sweep

```text
epsilon in {1/2,1/3,1/4,1/5,1/10,1/20,1/50,1/100},
A=1/4+epsilon/2, B=A/2,
m_B in {1/1000,1/100,1/20},
c_A in {1/200,1/100,1/50,1/20,1/10}
```

returned no certified ratio above `814/2149`. [T0]

## T0. Cancellation Stress

Gap 3 asks whether per-source legal imports can be much larger than aggregate
`F_L` because several legal rows cancel into the same target column. I searched
the exact two-pair template with

```text
A in {3/10,7/20,2/5,9/20},
B in {1/10,3/20,1/5,1/4,3/10},  B<A, A+B>1/2,
m_B in {1/100,1/50,1/20,1/10},
c_A in {0,1/100,1/50,1/20},
c_B in {1/100,1/50,1/25,1/20,3/100,1/10}.
```

Each accepted candidate had to satisfy `delta<=1/4`, have the target chart as
a theta-half argmin, have at least two legal rows, and have positive

```text
F_per - F_L,
F_per := sum_{j in L,l in B} mu_l (-beta_j P_jl)_+.
```

No certified cancellation separation occurred in this finite grid. This is
not a proof of impossibility; it says only that the simplest two-pair
Schur-shear realization did not create the gap-3 pathology. [T0/T2]

## T0. Rank-4 / Two-Block Probe

I tried two exact rank-4 constructors for the higher-rank dilution and
two-block hole:

1. a balanced mirror construction with class vertices plus four signed rows;
2. a freer left-inverse construction where class coefficients absorb the
   signed-row moments exactly.

Both constructors still asserted `B L=I`, `P^2=P`, and row sums. They did not
produce a certified `delta<=1/4` theta-half argmin with a two-block hole. [T0]

Representative discarded probe: with chart `(e1,e2,e3,p_A)` and a legal row
having coordinates

```text
(-51/100, -49/100, 1, 1),
```

the fan weight on the only volume-permitted negative coordinate is

```text
w = (51/100)/(1) = 51/100.
```

The same-pivot ledger would still be paid in that probe,

```text
(L_mu+F_L)/(sum w C_s) = 400000/545673,
```

but the instance is **not admissible**: `delta=588/625>1/4`, and the target
chart is not an argmin (`Phi_best=6/625` at `(e1,e2,j,j*)`, while the target
chart has max `169/200`). This proves nothing about G1's candidate; it only
records why the naive rank-4 dilution design was rejected. [T0]

The two-block hole therefore remains UNDECIDED. A real decider still needs an
exact capped argmin certificate where strict legality is supplied by a
two-block cover not represented by the one-row negative fan. [T2]

## T1. What Survived

All certified argmin instances in this wave satisfy the pure legal inequality

```text
L_mu + F_L <= sum_{j,t} w_{j,t} C_s(j,t)
```

with room. The worst certified ratio newly generated here is `814/2149`; the
worst ratio among the D6 replay plus this wave is D6 Certificate B's
`4593717/10385000`. [T0/T1]

No certified family made

```text
L_mu + F_L
  - sum_{j,t} w_{j,t} C_s(j,t)
```

positive, and no certified residual needed the boundary budget
`G_class^- + S_-^mu + R_D^nu`. Thus `C_legal=0` survived these exact tests,
and a finite `C_legal` was not stressed. [T0/T1]

The evidence is still too narrow to promote the candidate. In particular:

- the orphan-row implication is unproved;
- the cancellation search was only a finite two-pair grid;
- higher-rank diluted weights did not reach a capped argmin certificate;
- no two-block legal-cover certificate was found. [T2]

## Verdict

Task-C bits:

```text
gap-1 orphan row realizable?       UNDECIDED
pure-legal C_legal=0 survives?     SURVIVED certified families
C_legal finite survives?           SURVIVED certified families
two-block hole?                    UNDECIDED
```

Arm-G headline: the negative-side legal circulation candidate is still the
right shape on the exact capped argmins I could certify. The kill criterion is
not triggered. The likely reshaping, if a future certificate forces one, is
not a larger scalar constant first; it is a broader weight family that includes
or explains orphan positive-orientation and two-block legal covers. [T1/T2]
