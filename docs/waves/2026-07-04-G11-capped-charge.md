<!--
ROLE: independent exploration wave for arm G wave 11: charge the (CI)
import at the cap, or prove capped (G)-emptiness.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 11
answers: bd aism-izb
Tier legend: T0 = exact repo-file fact or exact fractions.Fraction arithmetic
in this wave; T1 = elementary derivation from T0/validated inputs; T2 =
plausible target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g11_charge.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: (CHARGE) is PARTIAL only: the dominant import reduces exactly to a
cross-pivot B-L cancellation mass not present in the unified pivot-s budget.
No capped clean (G) instance was found. No capped-emptiness proof was found.
(PRT), (SC), and (RH) remain OPEN.
-->

# Arm G Wave 11: Collateral Import At The Cap

No `fr` or `bd` command was run. No existing repo file was edited. The scratch
checker rebuilt `P=L B`, asserted `B L=I_3`, `P^2=P`, row sums `1`, computed
`delta(P)`, enumerated all theta-half actual-row charts, and computed every
displayed fraction below. [T0]

Rows are indexed as `(c0,c1,c2,j,k,...)`, with base chart
`U=(c0,c1,c2)` and pivot `s=c2` unless stated otherwise.

## Task 1: Anatomy Of `I_{r,j}`

Use the validated `(CI)` statement with `c=a_s(j)>0`, transverse collateral
pivot `r`, and remaining coordinate `t`. Since `V_j` is theta-half
admissible and `m_U<=1`, one has

```text
c >= 1/(2m_U) >= 1/2.                                  (1)
```

For abbreviations

```text
A_{r,s} := sum_i beta_r(i)^+ a_s(i)^+,
B_{r,s} := sum_i beta_r(i)^+ a_s(i)^-,
C_{r,s} := sum_i beta_r(i)^- a_s(i)^+,
D_{r,s} := sum_i beta_r(i)^- a_s(i)^-,
```

the left-inverse identity gives the exact cross-pivot cancellation

```text
0 = sum_i beta_r(i) a_s(i)
  = A_{r,s} - B_{r,s} - C_{r,s} + D_{r,s},              (2)

A_{r,s} = B_{r,s} + C_{r,s} - D_{r,s} <= B_{r,s}+C_{r,s}. (3)
```

Equivalently, the positive pivot-coordinate mass seen by the transverse
beta row is financed by either beta-positive rows with negative pivot
coordinate (`B_{r,s}`) or beta-negative entries of the transverse chart row
against pivot-positive coordinates (`C_{r,s}`). This is exact B-L duality:
`sum_i P_{u_r i} a_s(i)=a_s(u_r)=0`. [T1]

Splitting the three pieces of `R_{r,j}` gives the universal reduction

```text
I_{r,j}
 <= [ ((1-c)^+)/c + d_t^-/c + d_r^+/c ] B_{r,s}
    + [ d_t^+/c + d_r^-/c ] A_{r,s}.                   (4)
```

This is the cleanest T1 output of the wave. It is not yet a charge to the
`conj-sc` budget. [T1/T2]

### (i) The `(1/c-1)a_s(i)^-` Term

For `c>=1`, this term is nonpositive and can be dropped in `R_+`. For
`1/2<=c<1`,

```text
sum_i beta_r(i)^+ ((1/c-1)a_s(i)^-)
 <= B_{r,s}.                                           (5)
```

The important budget warning is negative: `B_{r,s}` is not
`S_-^mu(s,U)`. The latter is weighted by `beta_s^-` and transverse
negativity relative to pivot `s`; here the weight is `beta_r^+` and the
negative coordinate is the pivot coordinate `a_s^-`. Nor is it directly
`SIGMA_s`, which is ambient row negativity weighted by `beta_s^+`. [T1]

A capped exact toy shows this term can be present under `delta<=1/4`:

```text
L =
[1 0 0]
[0 1 0]
[0 0 1]
[1/4 0 3/4]
[0 6/5 -1/5]

B =
[1 0 0 0 0]
[0 22/25 1/50 0 1/10]
[-3/16 0 7/16 3/4 0]

P =
[1 0 0 0 0]
[0 22/25 1/50 0 1/10]
[-3/16 0 7/16 3/4 0]
[7/64 0 21/64 9/16 0]
[3/80 132/125 -127/2000 -3/20 3/25]
```

Exact checks:

```text
delta(P)=427/2000 <= 1/4,     P^2=P,     P1=1.
```

For `j=3`, `r=1`, `c=3/4`, the import rows are:

| row | `beta_1^+` | `a_s` | `(i)` | `(ii)` | `(iii)` | `R` | import |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `c2` | `1/50` | `1` | `0` | `1/3` | `0` | `1/3` | `1/150` |
| `4` | `1/10` | `-1/5` | `1/15` | `0` | `0` | `1/15` | `1/150` |

Thus

```text
I_{1,j}=1/75,     pieces=(1/150,1/150,0),
G_class^-=3/16,  S_-^mu=0,  SIGMA=0.
```

This is only a term witness; the base chart is not the theta-half argmin.
[T0]

### (ii) The `(a_s(i)d_t/c)^+` Term

If `d_t>0`, the positive-pivot side contributes

```text
(d_t/c) A_{r,s}.
```

If `d_t<0`, only rows with `a_s(i)<0` contribute, giving

```text
(d_t^-/c) B_{r,s}.
```

At a high-self row,

```text
lambda_s(j)=1-c=d_t+d_r.
```

In the mixed sign case `d_t>0>d_r`,

```text
d_t = lambda_s(j) + d_r^- <= lambda_s(j)^+ + W_j.       (6)
```

Under the Cramer box `|a_q(i)|<=2`, a row can make this term large only if it
has `beta_r(i)>0` and either `a_s(i)>0` with `d_t>0`, or `a_s(i)<0` with
`d_t<0`. The first case is the same `A_{r,s}` mass as the dominant term
below; the second is the same cross-pivot negative mass `B_{r,s}` from (i).
[T1]

The capped toy above isolates a pure positive-pivot `(ii)` contribution from
the chart row `c2`: `beta_1(c2)=1/50`, `a_s(c2)=1`, `d_t=1/4`, `c=3/4`,
hence import `1/150`. [T0]

### (iii) The `-a_s(i)d_r/c` Term

If `d_r<0`, this is

```text
(d_r^-/c) A_{r,s}.                                     (7)
```

This is the dominant structural piece. In the G10 rejected witness it is the
same mechanism as the sharp `I_{1,j}=11/40`: a collateral row with
`beta_1^+>0`, `a_s^+>0`, and `d_r=-W_j`. [T0/T1]

The exact identity (3) is the useful split:

```text
(d_r^-/c) A_{r,s}
 = (d_r^-/c)(B_{r,s}+C_{r,s}-D_{r,s})
 <= (d_r^-/c)(B_{r,s}+C_{r,s}).                        (8)
```

The live obstruction is now narrow. `B_{r,s}` is the unfinanced cross-pivot
negative-coordinate mass from (i). `C_{r,s}` is beta-negative mass in the
transverse chart row multiplied by pivot-positive coordinates; by the Cramer
box it is at most `2 nu_{u_r}`, but `nu_{u_r}` is not a term in the pivot-s
unified budget. [T1/T2]

A capped exact toy isolates the pure `(iii)` term:

```text
L =
[1 0 0]
[0 1 0]
[0 0 1]
[0 -1/5 6/5]

B =
[1 0 0 0]
[0 19/20 3/10 -1/4]
[0 1/10 2/5 1/2]

P =
[1 0 0 0]
[0 19/20 3/10 -1/4]
[0 1/10 2/5 1/2]
[0 -7/100 21/50 13/20]
```

Exact checks:

```text
delta(P)=1/4,     P^2=P,     P1=1.
```

For `j=3`, `r=1`, `c=6/5`, `d_t=0`, `d_r=-1/5`:

| row | `beta_1^+` | `a_s` | `(i)` | `(ii)` | `(iii)` | `R` | import |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `c2` | `3/10` | `1` | `0` | `0` | `1/6` | `1/6` | `1/20` |

Thus

```text
I_{1,j}=1/20,      pieces=(0,0,1/20),
G_class^-=0,       S_-^mu=0,      SIGMA=7/200,
I/(G+S+SIGMA)=10/7.
```

Again this is not a clean `(G)` instance: the theta-half argmin is
`(c0,c1,j)` with max Phi `0`, so minimality pivots onto the self-supported
row. [T0/T1]

## Task 2: Capped Construction Attempts

### Focused Two-B-Row Sweep

Template:

```text
j=(3/5,-2/5,4/5),      k=(-1/5,4/5,2/5).
```

The exact sweep sampled 200000 rational left-inverse choices on denominator
`40`, biased around the G9/G10 columns. Counts:

```text
capped candidates:                         352
capped with base chart as theta argmin:    352
high-self, beta_s-positive, V_j admissible: 93
clean (G) branches:                          0
```

The best exact near miss is capped, high-self, beta-positive, non-fan, and
theta-half certified, but remains Psi-blocked:

```text
L =
[1 0 0]
[0 1 0]
[0 0 1]
[3/5 -2/5 4/5]
[-1/5 4/5 2/5]

B =
[169/200 7/100 -6/25 11/40 1/20]
[9/40 1/2 -1/20 -1/5 21/40]
[-1/4 0 1/2 1/2 1/4]

P =
[169/200 7/100 -6/25 11/40 1/20]
[9/40 1/2 -1/20 -1/5 21/40]
[-1/4 0 1/2 1/2 1/4]
[217/1000 -79/500 69/250 129/200 1/50]
[-89/1000 193/500 26/125 -3/200 51/100]
```

Exact checks:

```text
delta(P)=1/4,       P^2=P,       P1=1,
P_jj=129/200,       kappa_j=71/200<1/2,
beta_s(j)=1/2,      W_j=2/5.
```

Complete theta-half enumeration:

| chart | volume | Phi vector | max Phi |
|---|---:|---:|---:|
| `(c0,c1,c2)` | `1` | `(0,0,1/10)` | `1/10` |
| `(c0,c1,j)` | `4/5` | `(0,21/80,69/250)` | `69/250` |
| `(c0,c2,k)` | `4/5` | `(0,1/4,579/2000)` | `579/2000` |
| `(c0,j,k)` | `4/5` | `(0,69/500,193/1000)` | `193/1000` |
| `(c1,c2,j)` | `3/5` | `(9/40,0,217/500)` | `217/500` |

Branch data:

```text
M=1/10,       Psi_j=69/250 > M,       Gamma_j=21/80 > M.
```

Import and budget:

```text
I_{1,j}=21/80,       pieces=(0,63/400,21/200),
G_class^-=1/4,       S_-^mu=0,        SIGMA=21/200,
denom=71/200,

beta_s(j)W_j=1/5,    beta_s(j)W_j/denom=40/71,
I_{1,j}/denom=105/142.
```

This is a certified capped near miss, not a `(G)` instance. [T0]

### Spread/Offset Sweep

The G10 cap failure lives on a chart row. I tested the suggested relocation
mechanism with `n=6,7`: extra collateral rows, plus high-pivot offset rows
with negative `d_0` intended to reduce the chart-column negativity.

The exact biased sweep used 160000 rational samples. Counts:

```text
capped candidates:                         1
capped with base chart as theta argmin:    0
high-self clean (G) branches:              0
```

This is evidence only. Failed designs are not infeasibility results. [T0/T2]

## Task 3: Synthesis

The proof side did not close `(CHARGE)`. What was proved is the exact
factorization (4) plus the B-L cancellation identity (2). The dominant
question is now:

```text
Can a capped theta-half Phi-argmin with a clean high-self non-fan (G) branch
force

  B_{r,s} + C_{r,s}
  <= C*(G_class^-(s,U)+S_-^mu(s,U)+SIGMA_s(U))
     + C_fan*FanRes_s(U)?

```

This is narrower than the original import statement. It names the exact
residual row classes:

```text
B_{r,s}: beta_r-positive rows with negative pivot coordinate a_s<0.
C_{r,s}: beta_r-negative entries of the transverse chart row carried by
         pivot-positive coordinates a_s>0.
```

Neither is one of the current pivot-s budget terms. The dead pointwise route
`nu_i >= a_s(i)^-` would be exactly the wrong way to pay `B_{r,s}`. [T1/T2]

No capped clean `(G)` branch was realized. The capped near miss suggests the
cap can preserve the collateral rise while leaving `Psi_j` too large, but
this is not an emptiness theorem. [T0/T2]

## Verdict

```text
(CHARGE):    PARTIAL.
             Proved the exact reduction (4) and the identity
             sum_i P_{u_r i}a_s(i)=0. The dominant term is reduced to
             B_{r,s}+C_{r,s}, but no universal charge to
             G_class^- + S_-^mu + SIGMA + FanRes was proved.

(CAP-EMPTY): OPEN.
             No capped clean (G) instance was found, but the searches are
             finite design sweeps, not infeasibility proofs.

(REFUTE):    NOT FOUND.
             No capped certified (G) family and no growing charge ratio was
             realized.

(PRT):       OPEN, now narrowed to the cross-pivot import residual above.
(SC):        OPEN, still blocked on the high-self pivot-removing theorem.
(RH):        OPEN, no status upgrade implied.
```

Nothing here proves or refutes `(EX)`, `conj-kernel`, or `op-classical`.