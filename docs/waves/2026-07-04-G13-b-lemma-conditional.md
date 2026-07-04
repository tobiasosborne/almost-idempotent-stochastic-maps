<!--
WAVE: arm G, wave 13 (prover branch) — 2026-07-04, session 7
WORKER: fresh codex exec (prompt: session scratchpad waves-scratch/PROMPT-wave13-prover.md)
ORCHESTRATOR: verification script re-run clean (exit 0, all hard asserts); worker ANSWER below VERBATIM.
TIER (worker self-assessed, orchestrator-concurred pending review): T1 = the c<0 pivot-removing
  transform + import bound (elementary paper proof, exact-verified on 3 instances, slack 0 somewhere);
  T2 = B-lemma CONDITIONAL on the single named subclaim NSC(K0). Independent codex review dispatched
  before any codification (reviewer != author).
HEADLINE STRUCTURAL FACT: in ALL three certified stress instances (incl. the 0.771 maximizer) the
  ENTIRE B-mass sits on volume-INADMISSIBLE carriers — pivot-removing minimality is blind to them;
  NSC (charge B to carrier row-negativity) is the isolated missing principle. Empirical NSC ratios on
  the three instances: B/weighted_nu = 200000000/175088281 (~1.14), 50000/17919 (~2.79), 9/4 (2.25).
-->

# Wave 13 prover answer: c<0 pivot move and B-lemma status

Worker constraints followed: I did not edit tracked files and did not run
`fr`, `bd`, or `git`. All written artifacts are under
`waves-scratch/wave13-prover/`.

Tier summary:

- T1 harvest: the `c<0` pivot-removing coordinate transform and pointwise
  collateral-import bound below. It is an elementary paper proof from the
  validated pivot-removing formulas.
- T2 harvest: the B-lemma is proved only conditional on one named residual
  subclaim, `NSC(K0)`, stated below. I do not have an unconditional proof.

## 1. The c<0 pivot-removing transform

Fix a chart `U=(u_0,u_1,u_2)`, a pivot `s`, a non-chart row `j`, and write
`c=a_s(j)`. Let `r != s` be transverse and let `t` be the remaining index.
Write `d_q=a_q(j)`.

The coordinate formulas from `lem-pivot-removing-move` are sign-agnostic.
Indeed

```text
p_j = c p_{u_s} + sum_{q != s} d_q p_{u_q},
```

so, for `c != 0`,

```text
p_{u_s} = c^{-1} p_j - sum_{q != s} (d_q/c) p_{u_q}.
```

Substituting this in

```text
p_i = a_s(i)p_{u_s} + sum_{q != s} a_q(i)p_{u_q}
```

gives, on `V_j=U-u_s+j`,

```text
a_s^j(i) = a_s(i)/c,
a_q^j(i) = a_q(i) - a_s(i)d_q/c       (q != s).
```

No sign assumption on `c` is used.

## 2. The c<0 pointwise import bound

Assume now `c<0` and put `k=-c>0`. For a fixed row `i`, abbreviate

```text
x = a_s(i),        y = a_t(i),        z = a_r(i).
```

The old and new inner quantities for `E_r` are

```text
X = x^- + y^- - (1-z),
E_r(i) = X^+,

Y = (-a_s^j(i))^+ + (-a_t^j(i))^+ - (1-a_r^j(i))
  = x^+/k + (-y + x d_t/c)^+ - 1 + z - x d_r/c,
E_r^j(i) = Y^+.
```

The positive-part cases used are:

```text
(-x/c)^+ = x^+/k                         because c=-k<0.
```

For `w=x d_t/c`, the inequality `(-y+w)^+ <= y^- + w^+` is by the four
sign cases:

```text
y <= 0, w >= 0: equality, (-y+w)^+ = y^- + w^+.
y <= 0, w <  0: (-y+w)^+ <= -y = y^-.
y >  0, w >= 0: (-y+w)^+ <= w = w^+.
y >  0, w <  0: (-y+w)^+ = 0.
```

Therefore

```text
Y <= X + R^-_{r,j}(i),
```

where the sign-flipped import remainder is

```text
R^-_{r,j}(i)
 = a_s(i)^+/(-c)
   - a_s(i)^-
   + (a_s(i)d_t/c)^+
   - a_s(i)d_r/c.                         (R-)
```

Using `(A+B)^+ <= A^+ + B^+` gives the desired pointwise bound

```text
E_r^j(i) <= E_r(i) + (R^-_{r,j}(i))^+.
```

Since the transverse left-inverse row is unchanged by the pivot-removing
move, summing against `beta_r(i)^+` gives

```text
Phi_r(V_j) <= Phi_r(U) + I^-_{r,j}(U),

I^-_{r,j}(U) := sum_i beta_r(i)^+ (R^-_{r,j}(i))^+.
```

It is useful to record the exact split. For `x=a_s(i)`:

```text
x >= 0:
  R^-_{r,j}(i) = x * (1 + d_t^- + d_r)/(-c).

x < 0:
  R^-_{r,j}(i) = x^- * ((d_t^+ - d_r)/(-c) - 1).
```

Consequently

```text
I^-_{r,j}(U)
 <= ((1+d_t^-+d_r)^+/(-c)) A_{r,s}
    + (((d_t^+-d_r)/(-c)-1)^+) B_{r,s}.
```

This is not the same algebra as the validated `c>0` CI lemma: the first
`1/|c|` term now lands on `A_{r,s}`, not on `B_{r,s}`, and the B-side
coefficient contains a subtractive `-1`.

## 3. What minimality gives, and where it stops

For a B-carrying row `i`, by definition

```text
beta_r(i)>0,        a_s(i)<0.
```

Thus the pivot-removing move through `i`, if available, is a `c<0` move.

Decompose the B-mass into:

```text
B_thin = sum_{beta_r(i)>0, a_s(i)<0, |a_s(i)| m_U < 1/2}
         beta_r(i)^+ a_s(i)^-,

B_adm  = B_{r,s} - B_thin.
```

### (a) Volume-inadmissible carriers

For rows in `B_thin`, the pivot-removing chart is not theta-half
admissible, so Phi-minimality gives no comparison. The only unconditional
size statement from volume is

```text
a_s(i)^- < 1/(2m_U),
```

and hence

```text
B_thin < (1/(2m_U)) sum_i beta_r(i)^+
       <= (1/(2m_U))(1+delta(P)).
```

Since `m_U>=1/2`, this is at best `B_thin <= 1+delta(P)`, not an
`O(delta)` estimate. This is not enough for the B-lemma. The stress
instances below show this is not cosmetic: all checked B-carriers are
volume-inadmissible.

### (b) Admissible carriers blocked by Psi

If `i` is admissible and the pivot-removing disjunction is Psi-blocked,

```text
Phi_s(U) <= Psi_i = Phi_s(V_i).
```

The new pivot row for coordinate `s` is `P_i`, not an unchanged transverse
row. The `c<0` import bound above does not control this case. I do not have
a Psi-block charge.

### (c) Admissible carriers blocked by Gamma

If `i` is admissible and Gamma-blocked, then for some `q != s`,

```text
Phi_s(U) <= Phi_q(V_i).
```

The `c<0` import bound gives the exact analogue of the CI lower-forcing
statement:

```text
Phi_s(U) - Phi_q(U) <= I^-_{q,i}(U).
```

This is a valid diagnostic, but it is still a lower bound on an import term,
not an upper bound on the carrier mass `beta_r(i)^+ a_s(i)^-`. I do not see
a way to reverse it without an additional self-support/row-negativity
principle.

## 4. Conditional B-lemma

The single residual subclaim I can isolate is the following.

`NSC(K0)` (negative self-support charge). Under the target hypotheses of the
B-lemma, for every transverse `r != s`,

```text
B_{r,s}
 <= K0 * sum_{i: beta_r(i)>0, a_s(i)<0} beta_r(i)^+ nu_i(P),
```

where `nu_i(P)=sum_l P_{il}^-` is the ambient row-negative mass of row `i`.

This is deliberately a single inequality. It is not known from the repo
record: the G6 silent-algebra family warns that pointwise
`nu_i >= const*a_s(i)^-` is false away from the argmin mechanism. The point
of `NSC` is exactly to package the missing minimality/self-support theorem.

Conditional proof. Since row `u_r` has row sum `1`,

```text
sum_i beta_r(i)^+ = 1 + sum_i beta_r(i)^- <= 1 + delta(P).
```

Also `nu_i(P) <= delta(P)` for every row. Therefore `NSC(K0)` implies

```text
B_{r,s}
 <= K0 * delta(P) * sum_{i: beta_r(i)>0, a_s(i)<0} beta_r(i)^+
 <= K0 * delta(P) * sum_i beta_r(i)^+
 <= K0 * (1+delta(P)) * delta(P).
```

Under the target cap `delta(P)<=1/4`,

```text
B_{r,s} <= (5K0/4) delta(P).
```

Thus the desired B-lemma follows conditionally with `K=5K0/4`.

This conditional result is compatible with the data constraint. The
maximizing run has `B/delta = 8400000/10897843`, so any unconditional
constant must be at least that value.

## 5. Exact verification

Script:

```text
waves-scratch/wave13-prover/verify_wave13.py
```

Command run from the repo root:

```text
python3 waves-scratch/wave13-prover/verify_wave13.py
```

Output:

```text
wave13 exact verification
Rminus = a_s^+/(-c) - a_s^- + (a_s*d_t/c)^+ - a_s*d_r/c for c<0

instance: insert-y=681/10000
  U=(0, 2, 4) s=2 r=1 m_U=197/200 delta=55319/1000000
  masses: A=42/985 B=42/985 C=0 D=0 B/delta=8400000/10897843
  cancellation A-(B+C-D)=0
  check B<=delta: True
  c<0 checks: moves=1 failures=0 min_row_slack=0
  carrier weighted_nu=18664233/500000000 B/weighted_nu=200000000/175088281
    carrier i=3 beta=7/10 a_s=-12/197 contrib=42/985 admissible=False row_nu=2666319/50000000
  admissible c<0 move summaries: none

instance: two-carrier-B
  U=(0, 2, 4) s=2 r=1 m_U=99/100 delta=99/1250
  masses: A=3/50 B=3/50 C=0 D=0 B/delta=25/33
  cancellation A-(B+C-D)=0
  check B<=delta: True
  c<0 checks: moves=1 failures=0 min_row_slack=0
  carrier weighted_nu=53757/2500000 B/weighted_nu=50000/17919
    carrier i=3 beta=33/50 a_s=-1/11 contrib=3/50 admissible=False row_nu=1629/50000
  admissible c<0 move summaries: none

instance: G12-calibration
  U=(0, 1, 2) s=2 r=1 m_U=1 delta=1/4
  masses: A=2/57 B=2/57 C=0 D=0 B/delta=8/57
  cancellation A-(B+C-D)=0
  check B<=delta: True
  c<0 checks: moves=1 failures=0 min_row_slack=0
  carrier weighted_nu=8/513 B/weighted_nu=9/4
    carrier i=4 beta=40/57 a_s=-1/20 contrib=2/57 admissible=False row_nu=1/45
  admissible c<0 move summaries: none
```

The script hard-asserts `B L=I`, `P^2=P`, and row sums `1`, then checks:

- the sign-agnostic coordinate transform against direct chart inversion;
- the pointwise `c<0` bound `E_r^j(i) <= E_r(i)+(R^-_{r,j}(i))^+`;
- the summed import inequality `Phi_r(V_j) <= Phi_r(U)+I^-_{r,j}`;
- exact cross-pivot cancellation `A=B+C-D`;
- exact B, C, delta, and carrier admissibility on the stress maximizer,
  the G12 calibration instance, and the two-carrier-B certified point.

## 6. Gap list

1. No unconditional B-lemma proof. The deliverable is conditional on
   `NSC(K0)`.
2. The volume-inadmissible carrier class is the main obstruction. It is the
   entire B-mass in all three checked examples, including the `0.771`
   stress maximizer.
3. Psi-blocked admissible `c<0` moves are not controlled by the transverse
   import bound, because the pivot beta row changes to `P_i`.
4. Gamma-blocked admissible `c<0` moves are reduced to an import term
   `I^-`, but I have only an upper import bound and no reverse inequality
   charging `beta_r^+ a_s^-`.
5. I did not use the `C <= 2 delta` Cramer-box observation as a rigorous
   input; it is still only mod-audit in the sources I read.
