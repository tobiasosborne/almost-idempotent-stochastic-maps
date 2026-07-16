# W71 POTI-0 zero-overlap growing-rank refuter

## Verdict

**BLOCKED on both exact repair families; no full hypothesis-class entrant and no
refuter.**  This is a family-level verdict, not an emptiness claim.  The
registered conjecture `conj-dtr-zero-oriented-surplus-exclusion` remains
undecided.

This report, [search.py](search.py), and [certificates.json](certificates.json)
are **L3 exact constructive/numerical evidence only, never a proof**.  All
advertised quantities are `fractions.Fraction` values and all claims printed by
the verifier are exact assertions.

The best reachable POTI-0 mechanism is **(i) support disjointness**:
\(\rho(1)=0\) and \(G_\phi=0\) survive both repairs at genuine ranks
\(4,8,16,32\).  They survive only outside the full gate.  Mechanism (ii),
positive overlap with orientation starvation, was not reached.

## Exact repair axis and binding inequality

For rank \(m\), let

\[
 \tau=\frac1{2^{20}m},\qquad
 a=1-\frac1m+\frac{\tau}{20}.
\]

The construction has \(m\) distinct anchor rows, \(m\) distinct rotating
probe rows, and one public row.  Its factorization satisfies

\[
 P=LB,\qquad BL=I_m,\qquad P^2=P
\]

entrywise.  The rank certificate is \(BL=I_m\); rank growth is not cloning or
transient inflation.  A parameter \(\beta\) puts total public-root mass
\(\beta\) on the probe-carrier fibers.  Direct row enumeration gives the exact
law

\[
 \boxed{\max_i\nu(P_i)=\beta a.}
\]

The proposed D population has mass \(1/8\), split equally among the probe
fibers.  On those same fibers, \(P_{f^*}^+\) has mass \(\beta/m\) each.
Consequently this family can satisfy R0 carrier ownership only if

\[
 \beta\ge\frac18,
\]

whereas the row-negativity gate requires

\[
 \beta\le\frac{\tau^2}{a}.
\]

These two inequalities have a positive exact gap in every tested member:

| rank | \(\tau\) | negativity upper \(\tau^2/a\) | ownership lower | exact gap |
|---:|---:|---:|---:|---:|
| 4 | 1/4194304 | 5/65970698715136 | 1/8 | 8246337339387/65970698715136 |
| 8 | 1/8388608 | 5/307863257874432 | 1/8 | 38482907234299/307863257874432 |
| 16 | 1/16777216 | 5/1319413957525504 | 1/8 | 164926744690683/1319413957525504 |
| 32 | 1/33554432 | 5/5453577682157568 | 1/8 | 681697210269691/5453577682157568 |

This is the exact binding inequality for this construction family only.  It is
not a dimension-free obstruction and therefore is not a proof of the
conjecture.

## Family A: exact-negativity calibration

Set \(\beta=\tau^2/a\).  Then the actual negative mass, not merely a prescribed
tolerance, satisfies

\[
 \delta(P)=\max_i\nu(P_i)=\tau^2
\]

exactly.  The local DTR-shaped carriers retain \(h_u=0\), strict actor residual
\(>3\delta\), \(\operatorname{Tail}_1(u)>\tau/8\), and the union floor.  The
original selected support consists of anchor fibers while the proposed D
support consists of probe fibers, so \(\rho(1)=G_\phi=0\).

The ownership defect is exact:

\[
 \sup_{0\le g\le1}\{\eta_D^*(g)-P_{f^*}^+(g)\}
 =\frac18-\frac{\tau^2}{a}.
\]

It approaches \(1/8\) with rank.  Hence the displayed D population cannot be
the original D part of a legal selected-corner certificate; R0, B1--B5, and R1
are unavailable.

| rank | actual \(\delta(P)\) | R0 ownership excess | \(H-16\tau\) | \(D_{\rm EC}\) | \(D_{\rm leaf}\) |
|---:|---:|---:|---:|---:|---:|
| 4 | 1/17592186044416 | 8246337339387/65970698715136 | -1/262144 | -57724361375739/527765589721088 | 16777215/1073741824 |
| 8 | 1/70368744177664 | 38482907234299/307863257874432 | -1/524288 | -269380350640123/2462906062995456 | 33554431/2147483648 |
| 16 | 1/281474976710656 | 164926744690683/1319413957525504 | -1/1048576 | -1154487212834811/10555311660204032 | 67108863/4294967296 |
| 32 | 1/1125899906842624 | 681697210269691/5453577682157568 | -1/2097152 | -4771880471887867/43628621457260544 | 134217727/8589934592 |

Negative \(D_{\rm EC}\) here is a formal diagnostic on a non-entrant, not a
refutation.  \(D_{\rm leaf}>0\) throughout.

## Family B: scalar ownership repair

Set \(\beta=1/8\).  The carrierwise scalar inequality
\(\eta_D^*\le P_{f^*}^+\) is then repaired with equality in the formal panel,
and support disjointness still holds because the original selected set uses
only anchor indices.  This does **not** manufacture a legal selected-corner
certificate or the other R0 outputs; those remain failed/not reached.  The
repair instead exposes the exact finance cost

\[
 \max_i\nu(P_i)=\frac18\left(1-\frac1m+\frac\tau{20}\right)>\tau^2.
\]

| rank | ownership excess | max row negativity | excess over \(\tau^2\) | \(D_{\rm EC}\) | \(D_{\rm leaf}\) |
|---:|---:|---:|---:|---:|---:|
| 4 | 0 | 62914561/671088640 | 8246337339387/87960930222080 | -3/32 | 16777215/1073741824 |
| 8 | 0 | 146800641/1342177280 | 38482907234299/351843720888320 | -3/32 | 33554431/2147483648 |
| 16 | 0 | 314572801/2684354560 | 164926744690683/1407374883553280 | -3/32 | 67108863/4294967296 |
| 32 | 0 | 650117121/5368709120 | 681697210269691/5629499534213120 | -3/32 | 134217727/8589934592 |

Thus rank growth does not distribute this root-ownership repair cost: the
maximum row negativity tends to \(1/8\).

## Tallness and the remaining global gates

Tallness is still the first global wall.  Every factor row in both families is
a probability vector in the anchor simplex.  Each anchor is visible using the
explicit admissible exposer \(h_s(\ell)=1-\ell_s\), and the map
\(\ell\mapsto\ell B\) is injective because \(BL=I_m\).  Therefore

\[
 K(P)=\operatorname{conv}\{p_{a_s}\}\subseteq C_{\mathcal W},
 \qquad H=0,
\]

so \(H-16\tau=-16\tau\) at every rank and every tested \(\tau\).  This is the
seventh exact batch in the inherited sequence in which the attempted global
repair remains short.

The formal depth panel then has every row in \(\mathcal L_v\), so
\(P_v^+(\mathcal L_v)=1\) and

\[
 \ell_T-P_v^+(\mathcal L_v)<0
\]

by the exact fractions in `certificates.json`.  A legal ultra-\(\omega\)
package and the selected-corner extraction are not reached.  The realized B5
label is `NOT_REACHED`; **the B5 population is not \(\eta_D^*\)**.

At fixed genuine rank 8, the independent sweep
\(\tau=1/(8\cdot2^p)\), \(p=16,18,20,22\), keeps
\(\delta(P)=\tau^2\) exactly while \(H/\tau=0\),
\(P_v^+(\mathcal L_v)=1\), and the ownership excess
\(1/8-\tau^2/a\) tends toward \(1/8\).  Neither rank nor scale improves a
global gate.

## POTI panel and theorem assertions

For every member of both families:

- \(\rho(1)=0\), \(t_\phi(u)=0\),
  \([t_\phi(u)-D_0\delta]_+=0\), and \(G_\phi=0\);
- the predeclared TC parameters are
  \((r_0,\alpha,\lambda)=(1/320,1/2,1/2)\), and
  \(r_{\alpha,\lambda}=0\), so the TC antecedent is false;
- there is no POTI+ window entrant, so no \(\kappa_{\rm POTI}\) exists;
- the asserted L5 orderings
  \(D_{\rm EC}\ge D_{\rm POTI}/S\) and
  \(D_{\rm leaf}\ge D_{\rm EC}\) both pass exactly.  In fact the first is
  equality throughout.

For the ownership-repaired family,

\[
 D_{\rm POTI}=-\frac{21}{256},\qquad
 D_{\rm EC}=-\frac3{32},\qquad
 D_{\rm leaf}=\frac1{64}-\frac\tau{256}>0.
\]

The full incidence tables, their four radial bins relative to \(p_{f^*}\) and
\(p_v\), and the shallow/deep split are printed by `search.py` and frozen in
`certificates.json`.  All anchor fibers occupy the far/far radial bin; all
probe and top fibers occupy the near/near bin; the other two bins are empty.

## Mandatory regressions and by-catch

- **W66/W63 plateau — PASS.** \(\ell/\tau=1/1024=2\tau\), route `C0`,
  tallness fails, and \(D_{\rm leaf}=8191/524288>0\).
- **W55 \(A_0=5\) — PASS.** Finance-row negativity is
  \(21475229695/4294967296>\tau^2=1/65536\); the actor residual is small,
  so it is a T-esc shape and not DTR.
- **W69 rank 8 — PASS.** The exact baseline has local
  \(D_{\rm EC}=-7/64\), R0 ownership excess \(1/8\), \(H/\tau=0\), and
  empty/not-reached ultra \(\omega\).  Its new panel is
  \(\rho(1)=0\), \(G_\phi=0\), and \(D_{\rm POTI}=-7/64\).

There is no entrant to POTI+, no W65-leaf refuter, and no entrant to any full
creative leaf class.  The W66 `C0` classification is a regression route on a
short fixture, not full leaf by-catch.

Reproduce with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -u search.py
```
