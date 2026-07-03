<!--
ROLE: independent exploration wave for arm G wave 8: B-block transfer
financing and self-support/cancellation audit.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 8
answers: bd aism-mqf
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g8_transfer.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: the exact B-block transfer system and the beta-weighted
financed-excess identity are derived below. On the G5 two-orphan family the
transfer excess is negative and the weighted left side is exactly SIGMA. On
the D4 B-block refuter the positive transfer excess is 21/4000 and is paid
exactly by the negative pivot-class aggregate, reproducing D5. This wave does
NOT prove or refute (SC). The remaining single sub-gap is a high-self
pivot-removing blocker/import theorem: volume-inadmissible, Psi-blocked, and
Gamma-blocked rows must be charged to G_class^- + S_-^mu + SIGMA + FanRes.
Consequently (RH) remains blocked.
-->

# Arm G Wave 8: Transfer Financing

Read inputs in the requested order: G7; G6; G5; D5 and D4; G4, G3, G2, G1,
A9, A8; and the 2026-07-03 sections of `FINDINGS.md`. I did not run `fr` or
`bd`, and I edited no existing file. [T0]

## T1. Exact Transverse Transfer System

Fix a rank-3 theta-half chart `U`, pivot `s`, and transverse set
`T={r:r!=s}`. For an actual row `i`, put

```text
W_i       = sum_{r in T} a_r(i)^-,
lambda_i  = sum_{r in T} a_r(i) = 1-a_s(i),
Sigma_i^+ = sum_{r in T} a_r(i)^+ = W_i + lambda_i.
```

Thus chart rows have `W_i=0`; a transverse chart row has `Sigma_i^+=1`,
while the pivot chart row has `Sigma_i^+=0`. This is the `s`-coordinate
bookkeeping: negative mass into the pivot class does not create transverse
chart-positive source, and positive mass into any chart row imports no
transverse chart negativity. The theta-half Cramer box gives
`0<=W_i,Sigma_i^+<=4` for all actual rows. [T1]

For a B row `j`, define

```text
kappa_j = 1 - P_jj^+,
S_j^-   = P_jj^- Sigma_j^+
          + sum_{i != j} P_ji^- Sigma_i^+.
```

Summing G6's negative-part inequality over `r in T` gives

```text
kappa_j W_j
  <= S_j^- + sum_{i in B, i != j} P_ji^+ W_i.           (1)
```

This is the exact self-referential system. The term `S_j^-` is the ambient
negative-coefficient source; by the Cramer box,

```text
S_j^- <= 4 nu_j.                                        (2)
```

Let `J` be the non-fan beta-positive B rows whose `W_j` is to be controlled,
and put

```text
R_j^+ = sum_{i in B\J, i != j} P_ji^+ W_i.
```

Then

```text
kappa_j W_j
  <= S_j^- + sum_{i in J, i != j} P_ji^+ W_i + R_j^+.   (3)
```

When `kappa_j>0`, the literal transfer matrix is

```text
T_ji = P_ji^+ / kappa_j      (i,j in J, i != j),          (4)
T_jj = 0.
```

Rows with `kappa_j` tiny or nonpositive are precisely the self-supported
rows; (4) is not a contraction theorem. The D4 certificate already killed
that route. [T1]

## T1. Beta-Weighted Financed Excess

Assume `beta_j>0` on `J`, and define the positive import column weight

```text
A_i^J = sum_{j in J} beta_j P_ji^+       (i in J).
```

Multiplying (3) by `beta_j` and summing over `j in J`, the internal B-transfer
has the exact coefficient identity

```text
sum_{j in J} beta_j kappa_j W_j
 - sum_{j in J} sum_{i in J, i != j} beta_j P_ji^+ W_i
 = sum_{i in J} W_i (beta_i - A_i^J).                  (5)
```

Equivalently, the positive over-unity part of the transfer operator is

```text
sum_{i in J} W_i (A_i^J - beta_i)_+.                   (6)
```

The D5 stationarity ledger applies verbatim with `J` as the source block.
Split the other sources into positive B rows `L`, beta-negative B rows `N`,
and the class/T complement `K`. For every B-column `l`,

```text
A_l^J - beta_l^+
  = N_l^J - beta_l^- - L_l - N_l - C_l,                 (7)

N_l^J = sum_{j in J} beta_j P_jl^-,
L_l   = sum_{j in L} beta_j P_jl,
N_l   = sum_{j in N} beta_j P_jl,
C_l   = sum_{h in K} beta_h P_hl.
```

For `l in J`, `beta_l^+=beta_l` and `beta_l^-=0`. Thus (6) is financed only
through the signed terms in (7): `N^J` by the beta-positive rows' own negative
mass, `-C` by class aggregates, `-N` by beta-negative rows, and `-L` by the
legal/fan residual. This is a financing identity, not a geometric series. [T1]

Combining (3), (5), and (7) gives the weighted system in the useful form

```text
sum_{i in J} W_i (beta_i - A_i^J)
 <= sum_{j in J} beta_j S_j^- + sum_{j in J} beta_j R_j^+.     (FE)
```

`(FE)` is the central formula of this wave. It explains exactly why
`||T||<1` is the wrong target: positive excess may occur, but stationarity
identifies its financiers. [T1]

## T0. Exact Checks

The scratch checker asserted `B L=I`, `P^2=P`, and row sums `1` for the G5
family and the D4 refuter, then computed (5). [T0]

### G5 two-orphan family

For `p=1/2+h`, `e=1/2-h`, `J={o0,o1}`,

```text
beta_o = 1/4,       W_o = e,       P_oo = 1/(4p),
kappa_o = 1 - 1/(4p),
A_o^J = beta_o P_oo = 1/(16p).
```

There is no off-diagonal positive B transfer. Hence

```text
A_o^J - beta_o = - beta_o kappa_o < 0,
sum_i W_i (A_i^J-beta_i)_+ = 0,
sum_j beta_j kappa_j W_j = delta/2 = SIGMA.             (8)
```

Checkpoints:

| `h` | `delta` | `SIGMA` | `kappa` | `W` | `A-beta` | positive excess |
|---:|---:|---:|---:|---:|---:|---:|
| `1/10` | `7/30` | `7/60` | `7/12` | `2/5` | `-7/48` | `0` |
| `1/100` | `637/2550` | `637/5100` | `26/51` | `49/100` | `-13/102` | `0` |

Thus the two-orphan amplifier is not a transfer-excess refuter. Its large
`W` is paid at the source by the rows' own ambient negative mass, exactly the
`SIGMA` repair identified in G6. [T0/T1]

### D4 B-block refuter

For `J={p,m}` in the D4 certificate,

```text
beta_p=beta_m=21/40,       W_p=W_m=1/10,
P_pp=P_pm=P_mp=P_mm=21/40,
kappa=19/40.
```

Therefore

```text
A_p^J=A_m^J=441/800,
A_i^J-beta_i=21/800,
sum_i W_i(A_i^J-beta_i)_+ = 21/4000.                   (9)
```

The weighted left side and off-transfer are

```text
sum beta kappa W = 399/8000,
sum off-transfer = 441/8000,
excess = 21/4000.
```

D5's class term pays this to the penny. The pivot class aggregate is
`Gamma_s=1/20-1/10=-1/20`, and the pivot representative has
`P_zp=P_zm=21/40`, so

```text
(-Gamma_s) * (P_zp W_p + P_zm W_m)
  = (1/20) * (21/40*1/10 + 21/40*1/10)
  = 21/4000.                                           (10)
```

This is the exact chart-negativity version of the D5 financing ledger. It
also confirms that the killed `rho_B=21/20` contraction is not being
reclaimed here. [T0/T1]

### G6 silent algebra checkpoint

At `e=1/4`, `kappa=1/100` in G6's notation, the single silent row has

```text
P_oo=99/100,       W_o=1/4,       nu_o=1/400.
```

Equation (1) controls only

```text
(1-P_oo) W_o = 1/400 = nu_o,
```

while `W_o/nu_o=100`. The missing factor is exactly high-self support. G7's
pivot-removing chart is admissible and drops `Phi` to zero in this checkpoint,
so this is not an (SC) refuter. [T0/T1]

## T2. High-Self Branch Accounting

For a high-self row, `(FE)` controls only `kappa_j W_j`. To control `W_j`
itself one must use G7's pivot-removing comparison.

For row `j`, let `c=a_s(j)=1-lambda_j`. The pivot-removing chart is
theta-half admissible exactly when

```text
|c| m_U >= 1/2.                                        (11)
```

If it is admissible, G7 gives the exact disjunction

```text
Phi_s(U) <= max(Psi_j, Gamma_j).                       (12)
```

The three branches have the following honest charges:

```text
volume-inadmissible:
  |a_s(j)| m_U < 1/2.
  This gives lambda_j=1-a_s(j) large when a_s(j)>=0 and
  W_j <= E_s(j)+lambda_j, but the lambda_j part is harmonic/class
  financing, not SIGMA. G5 shows cancellation before positive parts is
  essential.

Psi_j-blocked:
  Psi_j >= Phi_s(U).
  The new pivot row is P_j; its obstruction is a positive-import term
  in the new chart, to be financed by a D5-style ledger after the Schur
  transform.

Gamma_j-blocked:
  Gamma_j >= Phi_s(U).
  The obstruction is collateral Phi on a different pivot. This is the
  A9/G7 collateral horn and has no universal cap in the files read here.
```

Thus the exact remaining substatement is:

```text
(PRT)  At a rank-3 theta-half Phi-argmin, for J=NF and every high-self
       row j in J, the pivot-removing alternatives (11)-(12) satisfy

       sum_{high-self j} beta_j W_j
       <= C * (G_class^- + S_-^mu + SIGMA) + C_fan * FanRes,

       where volume-inadmissible lambda mass is charged through the
       harmonic ledger, Psi-blockers through the transformed D5 import
       ledger, and Gamma-blockers through the legal collateral residual.
```

This is stronger than the proved identity `(FE)` and is not proved here. It
is also not refuted here: G5 is not high-self, D4 is not high-self, and the G6
high-self checkpoint pivots away with no blocker. [T2]

## T2. Status Of (SC) And (RH)

The low-self part has the right algebraic shape: if `kappa_j>=tau`, then
(3), `(FE)`, and (7) reduce the problem to the exact financing terms
`S_j^-`, `R_j^+`, and `(A_i^J-beta_i)_+W_i`. The Cramer bound turns
`S_j^-` into `SIGMA`; D5 names the class, beta-negative, and legal/fan
financiers for the excess. What is missing is the high-self theorem `(PRT)`.
[T1/T2]

Therefore the verdict is:

```text
(SC): OPEN.
variant proved: none; only the transfer-financing identity (FE).
refuter family: none certified.
single sub-gap: (PRT), the high-self pivot-removing blocker/import theorem.
```

Because (SC) is open, the rank-3 repaired horn remains blocked. If `(PRT)`
and the low-self financing bounds were proved with constants, the G6 assembly
would still have to use `C_RH>=4`, forced by the G5 two-orphan family. [T2]

## Verdict

Task bits:

```text
transfer system:          DONE, exact inequality (1)/(3)
financed-excess identity: DONE, central formula (FE)
G5 test:                  exact; no positive excess; lhs=SIGMA
D4 test:                  exact; excess=21/4000 class-financed
(SC):                     OPEN, blocked on (PRT)
(RH):                     blocked; any future C_RH must be >= 4
```

Arm-G headline: beta-stationarity finances B-block over-unity exactly, so
the remaining problem is not contraction. It is the high-self
pivot-removing theorem that turns self-supported chart negativity into
class/signed/SIGMA/fan-collateral budget. [T2]
