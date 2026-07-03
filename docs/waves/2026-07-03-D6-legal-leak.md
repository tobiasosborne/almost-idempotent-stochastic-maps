<!--
ROLE: decision wave for arm D wave 6: legal leak at theta-half Phi-argmins.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: D wave 6
answers: bd aism-kik
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_d6_legal_leak.py, pure fractions.Fraction
arithmetic; no checker output file was written to the repo.
Verdict: leak REALIZED. Strictly legal beta-positive H-M B rows with mu>0 and
E>0 can occur at theta-half Phi-argmins. The legal baseline L_mu can coexist
with M_D>0, and F_L can be positive. Thus L_mu=F_L=0 in the previous zoo was
an accident of that zoo, not an argmin theorem.
-->

# Arm D Wave 6: Legal Leak At An Argmin

Read inputs, in the requested order:

```text
docs/waves/2026-07-03-D5-wie.md
docs/waves/2026-07-03-D4-rsi.md
docs/waves/2026-07-03-A8-schur-degeneracy.md
```

I also read `docs/waves/2026-07-03-A9-gapb-composition.md` because the prompt
explicitly invokes its Schur accounting identity and crude-Lipschitz warning.

Notation follows D5. Fix a theta-`1/2` `Phi`-argmin chart `U`, pivot `s`,
`beta_j=P_{u_sj}`, and H-M `B` rows. Let `D` be the positive-beta,
positive-`E_s` rows whose active-preserving covering swaps all have Schur
volume `<=1/2`. Let

```text
L = {j in B\D : beta_j > 0},       N = {j in B : beta_j < 0}.
```

The legal quantities are

```text
L_mu = sum_{j in L} beta_j mu_j,
F_L  = sum_{l in B} (- sum_{j in L} beta_j P_jl)_+ mu_l.
```

## T1. Schur Swap Accounting Does Not Prove Impossibility

For a one-row active-preserving swap replacing transverse pivot `t` by row
`j`, write

```text
c = a_t(j),       d_l = a_l(j)  (l != t).
```

The Schur transform is

```text
a'_t(i) = a_t(i)/c,
a'_l(i) = a_l(i) - a_t(i)d_l/c       (l != t).
```

Pivot `s` is kept, so its beta row is unchanged. Row `j` becomes a non-`s`
pivot, hence `E'_s(j)=0`. With

```text
q_j    = beta_j E_s(j),
C_s(V) = sum_{i != j} beta_i^+ (E'_s(i)-E_s(i)),
```

the same-pivot identity is exact:

```text
Phi'_s(V) = Phi_s(U) - q_j + C_s(V).                      (1)
```

The new pivot row is also explicit. The beta row for the swapped-in pivot is
the old row `P_j`:

```text
beta'_t(i) = P_ji = c beta_t(i) + sum_{l != t} d_l beta_l(i),
```

and its score is

```text
Phi'_t(V) =
  sum_i (P_ji)^+ *
    ( sum_{l != t} (-a_l(i) + a_t(i)d_l/c)_+
      - (1 - a_t(i)/c) )_+ .                              (2)
```

If `s` attains `M=Phi(U)=Phi_s(U)`, argmin minimality gives only

```text
M <= max( M - q_j + C_s(V),  max_{r != s} Phi'_r(V) ).     (3)
```

Thus either the same pivot pays (`C_s(V) >= q_j`) or another pivot rises to
at least `M`. This is A9's disjunction; it is not a contradiction.

The theta box gives no useful lower bound. From `|c|>1/2` and
`|a_l(i)|, |d_l| <= 2`, one gets only crude size estimates such as
`|a'_t(i)| <= 4` and `|a'_l(i)| <= 10`. These are upper-size controls and
dimension-dependent after summing coordinates. The only universal lower bound
for a collateral score is `0`. Even the old pivot row `u_t` does not help:
its new `E'_t(u_t)` can be positive, but its coefficient `P_{j,u_t}` need not
be positive.

Exact red test: the strict transverse pair with `a=2/5` has
`delta=10/41`, argmin chart `(e1,e2,p)`, pivot `p`, and legal row `m` with

```text
beta_m=25/82,      mu_m=E_m=4/5,      max cover determinant=4/5.
```

Swapping `m` into one transverse position drops the same pivot to `0`, but a
collateral pivot rises:

| swap | `|c|` | `Phi(V)/delta` | new pivot vector `Phi_r(V)/delta` |
|---|---:|---:|---:|
| replace `e1` by `m` | `4/5` | `3/2` | `(0, 1, 3/2)` |
| replace `e2` by `m` | `4/5` | `3/2` | `(1, 3/2, 0)` |

So strict legality and positive `E` are compatible with argmin minimality.
The proposed argmin-mechanism lemma, in the form "strict legal beta-positive
high-`mu` rows are impossible at argmins", is false. [T0/T1]

## T0. Exact Checker

The scratch checker used only `fractions.Fraction`. For every instance below
it asserted

```text
B L = I,       P = L B,       P^2 = P,       P 1 = 1,
```

computed `delta(P)` as the maximum row negative mass, enumerated every
theta-half actual-row chart, selected all `Phi`-argmins, classified every
beta-positive H-M `B` row by the strict `|det C|>1/2` covering test, and
computed `L_mu`, `F_L`, `M_D`, and the D5 `(FIN)` sides.

All construction rows below use the exact two-scale transverse template

```text
z=(1,0,0), e1=(0,1,0), e2=(0,0,1),
p_A=(1,A,-A), m_A=(1,-A,A), p_B=(1,B,-B), m_B=(1,-B,B).
```

With per-row masses `m_A,m_B` (`m_A+m_B=1/2`) and shears `c_A,c_B`, put

```text
S = 2A c_A + 2B c_B,

B_0 = (0,0,0, m_A, m_A, m_B, m_B),
B_1 = (0,1-S,S, c_A,-c_A, c_B,-c_B),
B_2 = (0,S,1-S,-c_A, c_A,-c_B, c_B).
```

Then `B L=I` identically, so `P=L B` is an exact signed idempotent.

## T0. Certificate A: `L_mu>0` Coexisting With `M_D>0`

Parameters:

```text
A=2/5,       B=3/10,
m_A=499/1000, m_B=1/1000,
c_A=10/41,  c_B=0.
```

Exact global data:

```text
delta(P)=10/41,      max chart volume=1,
theta-half argmins: (e1,e2,p_A), (e1,e2,m_A),
min Phi/delta = 1.
```

For the argmin chart `U=(e1,e2,p_A)` and pivot `s=p_A`, the H-M coordinates
of the non-class rows are

| row | coordinates in `U` |
|---|---:|
| `z`   | `(-2/5, 2/5, 1)` |
| `m_A` | `(-4/5, 4/5, 1)` |
| `p_B` | `(-1/10, 1/10, 1)` |
| `m_B` | `(-7/10, 7/10, 1)` |

Classification at this pivot:

| row | `beta` | `mu` | `E` | max cover det | `nu` | class |
|---|---:|---:|---:|---:|---:|---|
| `m_A` | `12459/41000` | `4/5` | `4/5` | `4/5` | `10/41` | strict legal |
| `p_B` | `1/1000` | `1/10` | `1/10` | `1/10` | `15/82` | `D` |
| `m_B` | `1/1000` | `7/10` | `7/10` | `7/10` | `15/82` | strict legal |

Normalized quantities:

| quantity | value / `delta` |
|---|---:|
| `L_mu` | `99959/100000` |
| `F_L` | `0` |
| `M_D` | `41/100000` |
| `R_D^nu` | `3/4000` |
| `G_class^-` | `1` |
| `S_-^mu` | `0` |
| `(FIN)` left | `99959/100000` |
| `(FIN)` right | `4003/4000` |

This is the requested coexistence: a theta-half `Phi`-argmin with a strict
legal beta-positive high-`mu` row and `M_D>0`. The leak is order `delta`, not a
higher-order perturbation. [T0]

The same exact family with `m_B=epsilon`, `c_B=0`, and the displayed `A,B,c_A`
was checked at

| `epsilon` | `L_mu/delta` | `M_D/delta` |
|---:|---:|---:|
| `1/20` | `1959/2000` | `41/2000` |
| `1/100` | `9959/10000` | `41/10000` |
| `1/1000` | `99959/100000` | `41/100000` |
| `1/10000` | `999959/1000000` | `41/1000000` |

Thus the largest certified `L_mu/delta` with `M_D>0` in this wave is
`999959/1000000`. The table is evidence, not a theorem for all `epsilon`.
[T0/T1]

## T0. Certificate B: `F_L>0`

Parameters:

```text
A=3/10,      B=3/20,
m_A=99/200, m_B=1/200,
c_A=19/100, c_B=1/25.
```

Exact global data:

```text
delta(P)=1217/5000,       max chart volume=1,
theta-half argmins: (e1,e2,p_A), (e1,e2,m_A),
min Phi/delta = 4659/4868.
```

For `U=(e1,e2,p_A)` and pivot `s=p_A`, the non-class row coordinates are

| row | coordinates in `U` |
|---|---:|
| `z`   | `(-3/10, 3/10, 1)` |
| `m_A` | `(-3/5, 3/5, 1)` |
| `p_B` | `(-3/20, 3/20, 1)` |
| `m_B` | `(-9/20, 9/20, 1)` |

Classification:

| row | `beta` | `mu` | `E` | max cover det | `nu` | class |
|---|---:|---:|---:|---:|---:|---|
| `m_A` | `381/1000` | `3/5` | `3/5` | `3/5` | `1217/5000` | strict legal |
| `p_B` | `29/1000` | `3/20` | `3/20` | `3/20` | `149/1250` | `D` |
| `m_B` | `-19/1000` | `9/20` | `9/20` | `9/20` | `149/1250` | beta-negative |

Normalized quantities:

| quantity | value / `delta` |
|---|---:|
| `L_mu` | `1143/1217` |
| `F_L` | `21717/4868000` |
| `M_D` | `87/4868` |
| `R_D^nu` | `4321/304250` |
| `G_class^-` | `1122/1217` |
| `S_-^mu` | `171/4868` |
| `(FIN)` left | `4743/4868` |
| `(FIN)` right | `591017/608500` |

Here `F_L` is positive because the legal row `m_A` has a negative entry into
the degenerate target column `p_B`:

```text
P_{m_A,p_B} = -19/1000,
beta_{m_A} P_{m_A,p_B} = -7239/1000000,
mu_{p_B}=3/20,
F_L contribution = 21717/20000000.
```

This also mildly stresses `(FIN)` at constant `1`:

```text
(FIN left)/(FIN right) = 592875/591017 > 1.
```

It does not refute `(FIN)` with a universal constant; it only says the legal
financier statement cannot be a constant-`1` tautology. [T0/T1]

## T2. What The Certificates Decide

The candidate theorem

```text
At a theta-half Phi-argmin, every beta-positive H-M B row is either
Schur-degenerate or has mu=0.
```

is false: Certificate A has two beta-positive strict legal rows with `mu>0`
and `E>0`; Certificate B has one. The more careful variant using `E>0`
instead of `mu>0` is also false.

The legal leak is not strongly coupled to the degenerate tax. In Certificate A
`M_D/delta` can be made tiny while `L_mu/delta` stays arbitrarily close to
`1` along the checked exact subfamily. Thus a proof of `(RSI)` or `(FIN)`
cannot hope to absorb `L_mu` into `M_D` by argmin minimality alone.

The legal swap comparison remains useful only as the A9 disjunction:
same-pivot payment or collateral-pivot rise. The strict examples realize the
second horn without contradiction. In particular, legal rows are not excluded
by the `delta<=1/4` cap, exact idempotence, row sums, theta-half selection, or
Phi-argmin selection.

## Verdict And Recommendation

Verdict: **(b) leak REALIZED**.

What is proved inline:

- The one-row Schur formulas (1) and (2), and the exact max-stationarity
  disjunction (3). [T1]
- Strict legal beta-positive rows with `mu>0` and `E>0` occur at exact
  theta-half `Phi`-argmins under `delta<=1/4`. [T0]
- `L_mu>0` can coexist with `M_D>0`; the largest certified ratio here is
  `L_mu/delta=999959/1000000`. [T0]
- `F_L>0` is realizable at an exact argmin; the found certificate has
  `F_L/delta=21717/4868000`. [T0]

What is not proved:

- Any universal bound for the legal-collateral horn.
- Any universal `(FIN)` constant. The `F_L` certificate only refutes the idea
  that constant `1` follows formally from the ledger.

Recommended factoring:

1. Keep `lem-beta-stationarity-excess-ledger` from D5 as algebraic
   infrastructure.
2. Do not attempt to prove `L_mu=0` or `F_L=0` at argmins; both are now
   exact-refuted.
3. Split the legal horn into a real collateral theorem:
   strict legal contributor at a maximal pivot `=> max_r Phi_r <= C_legal delta`.
   It must use more than Schur norm bounds.
4. Keep `(FIN)` legal-aware with an explicit constant `C_fin>1`; the constant
   `1` version is already stressed by Certificate B.

[T0/T2]
