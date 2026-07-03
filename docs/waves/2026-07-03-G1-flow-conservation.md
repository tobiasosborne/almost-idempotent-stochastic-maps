<!--
ROLE: exploration wave for arm G wave 1: flow-conservation / legal-leak
circulation test.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 1
answers: bd aism-759
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g1_flow.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: TELESCOPES on the three registered certificates for the
negative-coordinate fan-matched weights. The D6 legal-leak term does not
amplify on these tests. This is not a proof: the live T2 gap is to show that
the negative-coordinate legal covers and the same-pivot collateral lower bound
exist in general, not only in the exact two-scale certificates.
-->

# Arm G Wave 1: Flow-Conservation Test

Read inputs, in the requested order: the session-4 synthesis in
`RESEARCH_NOTES.md`; D6; D5; D4; A9; A8; the five requested registry contracts;
and the 2026-07-03 entries of `FINDINGS.md`. [T0]

The checker rebuilt the two D6 two-scale matrices and the D4 `rho_B=21/20`
matrix from their displayed rational parameters. It asserted `B L=I`,
`P=L B`, `P^2=P`, row sums `1`, the fixed-chart D5 stationarity ledger
column by column, and the displayed deltas/ratios below. No discrepancy was
found. [T0]

## T1. Candidate Circulation Sum

Fix a theta-`1/2` `Phi`-argmin chart `U`, pivot `s`, coordinates `a(i)`,
and beta row `beta_i=P_{u_s i}`. Let `B` be the H-M nonclass rows, and split

```text
D = {j in D_s : beta_j > 0},
L = {j in B\D : beta_j > 0},       legal positive rows,
N = {j in B : beta_j < 0}.
```

For a one-row active-preserving legal swap
`sigma=(j,t)`, `j in L`, `t != s`, `|a_t(j)|>1/2`, let `V_sigma` replace the
transverse pivot `t` by row `j`. With

```text
q_j = beta_j E_s(j),        C_sigma = Phi'_s(V_sigma) - (Phi_s(U)-q_j),
Gamma_sigma = max_{r != s} Phi'_r(V_sigma),
```

A9 gives the exact disjunction

```text
Phi_s(U) <= max(Phi_s(U)-q_j+C_sigma, Gamma_sigma).       (A9)
```

The tested circulation is the weighted residual

```text
R_w =
  sum_sigma w_sigma *
    ( beta_j mu_j
      + sum_l mu_l (-beta_j P_jl)_+
      - C_sigma ).
```

Here the first term is `L_mu`; the second is a per-source upper version of
the D5 legal import leak `F_L`. If `R_w<=0`, the legal leak is financed by
same-pivot Schur collateral before any delta-budget is spent. If `R_w>0`,
the target is `R_w <= C*(G_class^- + S_-^mu + R_D^nu)`. [T1]

The intended chain is therefore

```text
weighted A9 disjunctions
  => legal collateral residual R_w
  => D5 ledger cancellation
  => M_D and/or L_mu,F_L <= C*(G_class^- + S_-^mu + R_D^nu).
```

The validated fan lemmas enter only as the local exchange rate: constant `2`
for all-mass zero-sum fan payment and sharp `2+sqrt(2)` for the D-restricted
fan payment. This wave does not prove that arbitrary legal Schur swaps reduce
to either fan model. [T0/T2]

Weights tried:

| name | formula | what it must cancel |
|---|---|---|
| uniform | `w_sigma=1` | every legal orientation, so duplicated `q_j` must cancel |
| beta | `w_sigma=beta_j` | beta-weighted orientations; still includes positive-orientation leaks |
| beta-mu | `w_sigma=beta_j mu_j=q_j` | quadratic legal mass; tests whether big rows self-dampen |
| fan-matched | `w_{j,t}=a_t(j)^-/mu_j` | the fan-lemma local rate; sums to one over the negative coordinates |

The fan-matched choice is the only one aligned with
`E_s(j)=mu_j=sum_t a_t(j)^-` in the H-M rows. It puts zero weight on the
positive-orientation swaps that trigger the A9 collateral horn in D6. [T1]

## T0. Instance A: D6 Certificate A

Certificate A has `delta=10/41`, `Phi_s(U)/delta=1`, `F_L=0`,

```text
M_D/delta=41/100000,
L_mu/delta=99959/100000,
G_class^-/delta=1,
S_-^mu/delta=0,
R_D^nu/delta=3/4000,
Budget/delta=4003/4000.
```

Legal rows are `m_A` and `m_B`; each has two volume-permitted one-row swaps.

| swap | branch in (A9) | `w_fan` | `C_sigma/delta` | ledger demand `/delta` | weighted residual `/delta` |
|---|---|---:|---:|---:|---:|
| `m_A -> e1`, `c=-4/5` | same+collateral | `1` | `18709/12500` | `12459/12500` | `-1/2` |
| `m_A -> e2`, `c=4/5` | collateral | `0` | `-41/12500` | `12459/12500` | `0` |
| `m_B -> e1`, `c=-7/10` | same+collateral | `1` | `602009/700000` | `287/100000` | `-6/7` |
| `m_B -> e2`, `c=7/10` | collateral | `0` | `-99713/100000` | `287/100000` | `0` |

Candidate totals:

| weights | demand `/delta` | collateral `/delta` | residual `/delta` | residual / Budget |
|---|---:|---:|---:|---:|
| uniform | `99959/50000` | `474713/350000` | `9/14` | `18000/28021` |
| beta | `248365043/410000000` | `1302080301/2870000000` | `17459/114800` | `174590/1148861` |
| beta-mu | `9934589953/20500000000` | `7440739953/20500000000` | `49877/410000` | `99754/820615` |
| fan-matched | `99959/100000` | `1649713/700000` | `-19/14` | `-38000/28021` |

Verdict on A: **TELESCOPE** for fan-matched weights. The positive-orientation
swaps are the leak source; including them uniformly leaves a positive
`9/14 delta` residual, still finite but not telescoped. [T0/T1]

## T0. Instance B: D6 Certificate B

Certificate B has `delta=1217/5000`, `Phi_s(U)/delta=4659/4868`, and one
legal positive row `m_A`. The legal import leak is the displayed D6 entry

```text
P_{m_A,p_B}=-19/1000,
beta_{m_A} P_{m_A,p_B}=-7239/1000000,
F_L = 21717/20000000.
```

Normalized data:

```text
M_D/delta=87/4868,
L_mu/delta=1143/1217,
F_L/delta=21717/4868000,
G_class^-/delta=1122/1217,
S_-^mu/delta=171/4868,
R_D^nu/delta=4321/304250,
Budget/delta=591017/608500.
```

The D5 one-sided legal ledger has `L_{p_B}/delta=-7239/243400`, but the full
column ledger is offset by the beta-negative and class terms; this is why the
aggregate `(FIN)` constant-`1` version is already stressed. [T0/T1]

| swap | branch in (A9) | `w_fan` | `C_sigma/delta` | ledger demand `/delta` | weighted residual `/delta` |
|---|---|---:|---:|---:|---:|
| `m_A -> e1`, `c=-3/5` | same | `1` | `10385/4868` | `4593717/4868000` | `-5791283/4868000` |
| `m_A -> e2`, `c=3/5` | collateral | `0` | `-87/4868` | `4593717/4868000` | `0` |

Candidate totals:

| weights | demand `/delta` | collateral `/delta` | residual `/delta` | residual / Budget |
|---|---:|---:|---:|---:|
| uniform | `4593717/2434000` | `5149/2434` | `-555283/2434000` | `-555283/2364068` |
| beta | `1750206177/2434000000` | `1961769/2434000` | `-211562823/2434000000` | `-211562823/2364068000` |
| beta-mu | `5250618531/12170000000` | `5885307/12170000` | `-634688469/12170000000` | `-634688469/11820340000` |
| fan-matched | `4593717/4868000` | `10385/4868` | `-5791283/4868000` | `-5791283/4728136` |

Verdict on B: **TELESCOPE** for fan-matched weights, including the exact
`F_L` legal import. Budget-only, the per-source legal demand has ratio
`4593717/4728136 < 1`; the larger full `(FIN)` left/right ratio from D6 is
`592875/591017 > 1` because it includes nonlegal one-sided ledger pieces.
[T0/T1]

## T0. Instance C: D4 `rho_B=21/20` Refuter

The D4 chart has `delta=1/5`, `Phi_s(U)/delta=21/40`,

```text
M_D/delta=21/40,
G_class^-/delta=1/4,
S_-^mu/delta=0,
R_D^nu/delta=21/20,
Budget/delta=13/10.
```

There are no legal positive rows: `p,m` are both in `D`, with one-row
factors `1/10` and two-row determinant `0`. Thus the legal circulation sum is
empty and all four tested weight rules have zero residual. [T0]

The D5 import excess is still nonzero and class-financed:

```text
W = 21/4000,        W/delta = 21/800,
(-Gamma_s)*(P_zp mu_p + P_zm mu_m) = 21/4000.
```

Verdict on C: **TELESCOPE vacuously** for the legal circulation. This instance
does not test legal leakage; it confirms the circulation must not replace the
D5 class ledger, because the killed `rho_B` contraction is repaired by the
negative pivot-class aggregate. [T0/T1]

## T2. Candidate Lemma And Forced Choices

The exact tests support the following proof target, not a theorem:

```text
Negative-side legal circulation lemma.  At a theta-1/2 Phi-argmin chart U
and maximal pivot s, let L be the beta-positive legal H-M rows. For
j in L and legal transverse positions t with a_t(j)<0, put
w_{j,t}=a_t(j)^-/mu_j. Then

L_mu + F_L
 <= sum_{j,t} w_{j,t} C_s(j,t)
    + C_legal * (G_class^- + S_-^mu + R_D^nu),

with universal C_legal, and possibly C_legal=0 for the pure legal part.
```

For the two D6 certificates the stronger per-source demand
`beta_j mu_j + sum_l mu_l(-beta_j P_jl)_+` is already dominated by the
weighted same-pivot collateral, so the tested residual constant is `0`. [T0]

The instances force these design choices:

- Use signed Schur orientations. The positive-orientation swaps have the A9
  collateral branch and carry residuals `1*delta` in A and `4659/4868*delta`
  in B before weighting. [T0]
- Normalize by negative-coordinate mass. Uniform weights duplicate `q_j` and
  leave `9/14 delta` on Certificate A. [T0/T1]
- Keep `F_L` explicit. Certificate B realizes a legal negative entry into
  `p_B`; hiding this in `L_mu` misses the stressed `(FIN)` column. [T0/T1]
- Keep `G_class^-` and `R_D^nu` in the boundary budget. D4 has no legal rows,
  but its import excess is paid exactly by negative class aggregate, while
  `M_D` is paid by `R_D^nu`. [T0/T1]

The live gaps are substantial:

- A strict legal row may have volume-permitted positive coordinates but not
  enough volume-permitted negative coordinates; the fan weights then have no
  legal swap to sit on. [T2]
- The table used one-row swaps in rank `3`. A general proof must include or
  dispose of two-block legal covers. [T2]
- The per-source import demand is stronger than aggregate `F_L`; multiple
  legal rows may cancel before the positive part. [T2]
- No argument here proves the same-pivot collateral lower bound
  `sum w C_s >= L_mu+F_L` outside the displayed certificates. [T2]

## Verdict

Headline bit: the D6 legal-leak terms `L_mu` and `F_L` **TELESCOPE** on the
certificates for the fan-matched negative-coordinate circulation. They do not
amplify, and the pre-registered kill criterion for arm G is **not triggered**.

This does not suggest (EX) is false. It suggests the circulation shape is
plausible only with oriented negative-part weights; unoriented legal-swap
averages are noisy and can leave positive residuals even on Certificate A.
[T1/T2]
