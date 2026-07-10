# W61 decider B report

## Verdict: FINANCING INSTANCE FOUND — local N5(ii) geometry

The constants fight is real for the currently banked ledger set.  There is an exact
dyadic family with \(\delta=\tau^2\to0\), a hidden carrier \(u=v\), and a freight
row \(x\) at separation \(\ell=\tau/2\), hence
\(\tau/4<\ell\le8\tau\), for which the exact
`lem-hx-financing-floor` demand is positive and is paid with slack.  Every unit of
the payment is the freight coefficient \(P_x^+(C)\) on one fiber with
\(z(C)=2+H\) and \(h(C)=1\); the banked top/carrier \(z\)- and \(h\)-leaks on that
fiber are both zero.  Thus the payment uses precisely the unconfined-freight-row
gap priced in N5(c), while the applicable top-deficit, harmonic, mass-split,
hiddenness-witness, and zero-face-capacity ledgers all hold exactly (the
inequality ledgers have strict slack).

This is **L3 exact constructive evidence, not a proof**.  It is not a
selected-corner counterexample: the family fails the tallness clause
\(H>16\tau\), and the displayed corner row gives zero \(\Gamma_f\)-mass to the
freight pair.  It also does not enter N6's far-carrier horn.  Consequently it
does not refute N5 or N6 as mathematical conjectures.  It does decide the more
limited question posed here: N5(ii) cannot be closed from the named scalar
ledgers at these constants without an additional budget that constrains the
freight row or couples \(\Gamma_f\) to its high-lever coefficients.  Creative
spend on a ledger-only close should stop pending that restatement.  N6 remains
undecided by this search.

## Exact family

For every tested \(k\in\{8,\ldots,32\}\), set

\[
 \tau=2^{-k},\quad \delta=\tau^2,\quad
 \varepsilon=\delta/2,\quad t=\tau/8,\quad
 K=1+\varepsilon(1-t),\quad q=\varepsilon/K,
 \quad \theta=\frac{\tau}{4(1+q)}.
\]

The certificate file records the default range \(k=8,\ldots,16\); the wider
range through \(k=32\) was also rerun exactly.  With
\(w=1+q\), the six rows, in column order
`a0,a1,z,c,d,x`, are

\[
\begin{aligned}
A_0=A_1&=(w,-q,0,0,0,0),\\
Z&=(Kw,-Kq,0,t\varepsilon,-\varepsilon,0),\\
C&=(0,0,0,1,0,0),\\
D&=(0,0,0,0,1,0),\\
X&=((1-\theta)w,-(1-\theta)q,0,\theta,0,0).
\end{aligned}
\]

The script asserts \(P\mathbf1=\mathbf1\) and \(P^2=P\) entry by entry in
`Fraction` arithmetic.  The two `A` indices form one complete row-point fiber.
The negative row masses are

\[
 (q,q,\delta,0,0,(1-\theta)q),
\]

so \(\delta(P)=\delta\) exactly.  This is the banked thin-zero-face shape with
a signed split of the `A` fiber (making the leak caps genuinely positive) and a
transient row \(X=(1-\theta)A+\theta C\).

### Hiddenness and top geometry

The affine observable

\[
 h(A)=h(Z)=0,\qquad h(C)=1,\qquad h(D)=t,
 \qquad h(X)=\theta
\]

is an optimal exposer at \(A\).  Its far set is exactly \(\{C,D\}\), and the
exact small-beta witness is

\[
 (D-A)+\varepsilon^{-1}(Z-A)=t(C-A),
\]

i.e. \(\lambda_D=1\), \(\alpha_Z=1/\varepsilon\),
\(\beta_C=t<\kappa=\tau/4\).  Hence \(t^*(A)=t\) and \(A\) is hidden.
Explicit admissible exposers in the certificate make \(Z,C,D\) visible, while
\(X\in\operatorname{conv}\{Z,C,D\}\).  Thus the visible set is exactly
\(W=\{Z,C,D\}\), \(A\) is the hidden top, and

\[
 H=2tq,\qquad H/\tau=q/4.
\]

The top support has values

\[
 \phi(A)=H,\quad \phi(Z)=\phi(D)=0,\quad \phi(C)=-2,
 \quad \phi(X)=(1-\theta)H-2\theta,
\]

with an ambient coefficient vector of \(\ell^\infty\)-norm one.  Therefore the
financing fiber `C` is genuinely deep for both banked observables:
\(z(C)=H+2\) and \(h(C)=1\).

## Financing-floor instantiation

Take the ordered row pair \((x,u)=(X,A)\), center at \(A\), and use the
recentred sign functional of the pair.  The ambient row separation and the
full-fiber variation differ because of the signed `A` clone fiber:

\[
 \ell=\|X-A\|_1=\tau/2,\qquad
 \ell_\chi=2\theta<\ell.
\]

Choose

\[
 N=\{A,Z,X\},\quad F=\{C,D\},\quad A_{\rm eng}=1,
 \quad \Lambda=1/\theta.
\]

The script verifies the exact lever values, including
\(\chi(A)=0\), \(\chi(X)=1\), \(\chi(C)=1/\theta\),
\(|\chi(Z)|<1\), and \(0<\chi(D)<1/\theta\).  The engine demand is

\[
 R=\theta(1-2\theta)-(2-\theta)q>0.
\]

The actual joint mass on \(F\) is

\[
 P_X^+(F)+P_A^+(F)=\theta+0,
\]

all at `C`, giving exact slack

\[
 \theta-R=2\theta^2+(2-\theta)q>0.
\]

This is the decisive allocation: the hidden carrier/top pays none of the
demand; the unconstrained freight row pays all of it on a fiber simultaneously
detected by \(z\ge4\tau\) and \(h\ge4\tau\).

## Ledger table

The following formulas are exact for every generated member.  The JSON gives
the fully reduced rational value for every tested \(k\).

| Banked item | Actual | Cap/floor | Exact slack |
|---|---:|---:|---:|
| engine financing on \(F\) | \(\theta\) | \(R\) | \(2\theta^2+(2-\theta)q\) |
| top-deficit weighted mass at \(v=A\) | \(0\) | \(q(2+4\delta)\) | \(q(2+4\delta)\) |
| \(z\)-leak at \(4\tau\), sharp \(\nu_v\) cap | \(0\) | \(q(2+4\delta)/(4\tau)\) | same as cap |
| \(z\)-leak at \(4\tau\), advertised \(\delta\) cap | \(0\) | \(\delta(2+4\delta)/(4\tau)\) | same as cap |
| \(h\)-leak at \(4\tau\) from \(v=A\) | \(0\) | \(q/(4\tau)\) | \(q/(4\tau)\) |
| zero-face capacity at \(A\), level \(\kappa\) | \(0\) | \(q\) | \(q\) |
| zero-face capacity at \(Z\), level \(\kappa\) | \(\delta^2/64\) | \(\delta\) | \(\delta-\delta^2/64\) |
| zero-face capacity at \(Z\), level \(4\tau\) | \(\delta^2/4\) | \(\delta\) | \(\delta-\delta^2/4\) |
| hiddenness small-beta | \(t=\tau/8\) | strict \(<\kappa=\tau/4\) | \(\tau/8\) |
| mass split at \(A,X,D,Z\) | \(\sum P_i^+\) | \(1+\nu_i\) | equality, checked exactly |

At the ceiling member \(k=8\), for example,
\(\delta=1/65536\), \(\tau=1/256\),
\(\ell=1/512\), \(q=2048/268437503\), and
\(\theta=268437503/274882100224\).  The representative exact matrix and every
large reduced rational demand/slack are in `certificates.json` to avoid replacing
exact values with rounded decimals here.

## Selected-corner audit and honest limits

Verified clauses:

- \(0<\delta(P)\le2^{-16}\), exact visible set, hidden top \(v=A\), top support
  \(\phi\), and admissible exposer \(h\);
- hidden carrier \(u=A=v\) is \(\rho\)-near the top;
- \(X,A\) satisfy the N5(ii) band and both points satisfy the local
  \(z,h<4\tau\) corner predicates, so the pair lies geometrically in the near
  block and has displacement greater than \(\gamma=\tau/4\);
- `f=D` is \(\rho\)-far, co-top under the literal inequality, and satisfies the
  exact corner score; a legal vertex kernel exists;
- numerically \(\Gamma_f(C_f)=1\), outside-corner mass is zero, and the printed
  corner-ledger floor has slack \(50972173/109051904\).

Unverified/false clauses:

- **Tallness is false:** \(H/\tau=q/4\), not \(H/\tau>16\).  Therefore
  `lem-sl1a-corner-ledger` is not formally applicable; its numerical accounting
  above is recorded but not invoked.
- **Freight aggregation is absent:** for `f=D`,
  \(\Gamma_f(X,A)=0\), \(\Gamma_f(B_N)=0\), and
  \(M_X^\gamma(B_N)=0\).  Thus the \(1/4\) block and \(1/8\) off-diagonal mass
  clauses are false.
- **N6 is absent:** the financing carrier equals the near top, rather than being
  a distinct \(\rho\)-far co-top hidden carrier.

These failures are global-completion conditions, not banked inequalities that
run out of budget.  They are exactly why this report does not call the family a
counterexample to N5/N6.

## Shapes tried and dead ends

1. **W29 frontier calibration.**  The context record has
   \(\delta=99/8000\), \(H=1/40\), hidden witnesses at \(t^*=1/81\), but
   \(G_4=\varnothing\) and \(\sigma_4=0\).  It is above the requested delta
   ceiling and supplies no deep financing fiber.  The snapshot contains the
   README, not its verifier/matrix, so it was used as a shape constraint rather
   than copied as a certificate.
2. **W35 absorption calibration.**  The recorded true-hidden cases again have
   \(R_4=0\); the positive width-\(1/4\) recipient mass is immediately adjacent
   to the documented hidden-to-visible transition.  This confirms that pushing
   mass through the carrier is the absorption-sensitive route.  The construction
   here instead puts it on the freight row, the explicitly unbanked channel.
3. **Undeformed thin-zero-face fixture.**  It gives the exact small-beta witness
   and deep fiber, but row \(A\) has \(\nu_A=0\); the \(h\)-leak cap is then met
   only at equality.  The signed full-fiber split preserves the row-point
   quotient while making \(\nu_A=q>0\), producing strict slack in every leak cap.
4. **Using the blocker \(Z\) as the carrier.**  This fails hiddenness: the
   \(\rho\)-near exemption permits an admissible exposer with margin one on its
   far set.  The correct hidden carrier is `A`; `Z` remains its zero-face blocker.
5. **Selected-corner completion.**  The first failure is not a leak budget but
   exact tallness: \(16\tau-H>0\).  Even retaining the legal corner row `D`, its
   idempotent coefficient row does not feed `X`, so the next failure is
   \(\Gamma_f(X,A)=0\).  No claim of completion is made.

## Reproduction

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -u search.py
```

This regenerates `certificates.json` for \(k=8,\ldots,16\).  A wider exact sweep
uses, for example, `--max-k 32`.  Every invariant, inequality, fiber aggregation,
matrix product, and witness balance is an exact `Fraction` assertion.  The JSON
stores matrices and ledger values as rational strings.
