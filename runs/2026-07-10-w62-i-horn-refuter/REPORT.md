# W62 L3 decider I — exact refuter search report

This report records **L3 exact constructive/numerical evidence only**. It is
not a proof of node I, not a proof of any universal obstruction, and not a
proof of L5-GAP-1. `BLOCKED` below always means blocked in the explicitly
tested family or completion class.

The verifier is [`search.py`](search.py); its frozen exact output is
[`certificates.json`](certificates.json). Every displayed matrix is checked
entrywise over `fractions.Fraction` for (P^2=P), row sums one, and its claimed
row negativity. The script also checks the displayed full fibers, visible and
hiddenness certificates, primal and dual height certificates, quotient
submeasure, ray-formula minimizing pair, (r_\omega), the exact scalar width,
and the universal-local-center inequalities wherever those quantities apply.

## Verdicts

- **Heavy summit-axis spike — BLOCKED (attempted corank-one simplex family).**
  The family realizes mass (1/4), the far/deep inequalities, and
  (Z_v(p_Q)/\tau=2\tau\to0), but its exact height is
  (H=2\delta=2\tau^2). Thus
  (H-16\tau=2\tau^2-16\tau<0).
- **Growing low-width dual-simplex fan — BLOCKED (attempted simplex-fan
  family).** The exact fan realizes masses (c_m/m=1/(4m)), the true ray LP
  value (Z_v(q_A)=2\delta), the for-all-local-centers co-top floor, and drift
  (2\delta). It fails both remaining gates:
  (H=2\delta<16\tau) and
  
  \[
    \Omega(\omega)=\frac{3+4\delta}{4(1+\delta)^2}\longrightarrow\frac34,
  \]
  
  rather than (<1/16).
- **Tall completions of the known seeds — BLOCKED (tested completion
  classes).** The two W61 seed families remain cubic-height, while the direct
  W55 rank-three left inverse violates the all-row negativity target by an
  exact order-one margin. The registered bounded-slab theorem rules out the
  broader W55 rank-three/slab class, but no unrestricted tall-completion
  obstruction is claimed here.

No genuine L5 datum and no refuter of node I was found.

## 1. Heavy summit-axis spike

### Family

For rational (0<\tau\le1/8), put (\delta=\tau^2). Use indices
(v,Q,b,f), take all rows except (v) to be coordinate rows, and set

\[
 p_v=(0,\tfrac14,\tfrac34+\delta,-\delta).
\]

This is an exact corank-one projection: because (P_{vv}=0) and every other
row is a coordinate row, (p_vP=p_v). Its sole negative mass is (\delta).
The three coordinate vertices are visible. The external vertex (v) is
hidden with exact exposedness margin

\[
 t^*(v)=\frac{\delta}{1+\delta}<\frac\tau4.
\]

The upper certificate is the affine identity

\[
 0=h(p_v)=\sum_{j\in\{Q,b\}}P_{vj}h(p_j)-\delta h(p_f),
\]

which forces one positive far row to have value at most
(\delta/(1+\delta)); the certificate in the JSON attains equality.

The visible hull is the coordinate simplex. Normalizing the positive part of
(p_v) supplies a primal closest point at distance (2\delta), while the
dual sign vector (y_Q=y_b=1,y_f=-1) supplies the same value. Hence
(H=2\delta) exactly and (v) is the (short) hidden top.

The spike fiber (Q) has (P_v^+(Q)=1/4). It is (4\tau)-far, and
(d_Q=0>H-8\tau) because (H-8\tau<0). For (q_A=p_Q), the proved ray
formula is minimized by the exhibited pair

\[
 \Lambda=3,\qquad c=p_b,
\]

whose objective is (2\delta). The matching feasible top-face vector above
also has value (2\delta), so this is the **true** LP value, not merely an
upper bound:

\[
 Z_v(p_Q)=2\delta,\qquad \frac{Z_v(p_Q)}\tau=2\tau\to0.
\]

### Range and binding margin

The exact sweep used
(\tau=1/32,1/64,1/128,1/256). At the last point,

\[
 \delta=\frac1{65536},\quad H=\frac1{32768},\quad
 H-16\tau=-\frac{2047}{32768},\quad
 \frac{Z_v(p_Q)}\tau=\frac1{128}.
\]

Thus the summit-axis interface is locally realizable with exact mass and
vanishing normalized dual value. Tallness alone disqualifies this family.
Clone splitting cannot help because the full fibers, row points, \(\ell^1\)
distances, (H), and all displayed masses are clone-invariant.

## 2. Growing dual-simplex fan

### Family and exact successes

For (m=3,4,8), use indices (v,Q_1,\ldots,Q_m,b,f), coordinate rows away
from (v), and

\[
 P_{vQ_i}=\frac1{4m},\qquad
 P_{vb}=\frac34+\delta,\qquad P_{vf}=-\delta.
\]

The selected full-fiber submeasure on the (Q_i)'s has exactly

\[
 m_{Q_i}=\frac{c_m}{m}=\frac1{4m},\qquad S=c_m=\frac14,
 \qquad q_A=\frac1m\sum_i p_{Q_i}.
\]

The same primal/dual height certificates give (H=2\delta), and the same
hiddenness identity gives (t^*(v)=\delta/(1+\delta)<\tau/4). The true ray
minimum is again certified from both sides. Here the minimizing pair is

\[
 \Lambda=3,\qquad c=p_b,
\]

and its ray vector has only two nonzero coordinates, (4\delta) at (b)
and (-4\delta) at (f). Consequently

\[
 Z_v(q_A)=8\delta-3H=2\delta,qquad
 Z_v(q_A)/\tau=2\tau\to0.
\]

The positive (G_v)-measure is the full positive part of row (v). Its
normalized barycenter is the normalized positive part, so

\[
 \|r_\omega-p_v\|_1=2\delta<\frac18.
\]

The local-center hypothesis is also exact and uniform. For every
(c\in K_v^{\rm loc}), reverse triangle inequality puts every selected
actor strictly outside the half-ball. Therefore

\[
 P_v^+(E_c\cap G_v)\ge S=\frac14
   >\frac{\tau S}{16},
 \qquad
 P_v^+(E_c\cap\mathrm{Sh}_v)=0<\frac{\tau S}{16}.
\]

This directly beats R3's theorem floor; it does not confuse a single center
with the required for-all-centers statement.

### Exact blockers

The finite extreme-sign enumeration for the scalar-width LP gives

\[
 \Omega(\omega)=\frac{3+4\delta}{4(1+\delta)^2}.
\]

The ballast has asymptotic normalized mass (3/4), and the entire selected
fan has mass (1/4); their sign split is the optimizer. At the best displayed
point (m=8,\tau=1/256),

\[
 \Omega(\omega)=\frac{3221291008}{4295098369},\qquad
 \Omega(\omega)-\frac1{16}
 =\frac{47245557759}{68721573904}>0.
\]

At that same point the local co-top margin is
(1/4-\tau/64=4095/16384), while the tallness margin is again
(-2047/32768). Thus the attempt is strong on the true ray value, quotient
mass, universal center floor, and drift, but it is neither low-width nor tall.

The tested pairs were
((m,\tau)=(3,1/64),(4,1/128),(8,1/256)). Increasing (m) does not change
the width formula in this support pattern. Removing the ballast would make
the uniform coordinate fan's width tend to one; retaining it improves the
constant only to (3/4).

## 3. Tall completions of the known seeds

### W61 thin transient graft

The matrices were reconstructed and checked for
(k=512,1024,2048), with (\tau=1/k), (\delta=\tau^2), and
(t_0=\tau/8). The visible vertices are (z,o,y); (u) is hidden with

\[
 t^*(u)=t_0-\delta(1-t_0)<\frac\tau4.
\]

An exact closest point on the segment ([z,y]) and a matching norm-one dual
vector give

\[
 H=\frac{2\delta\bigl(t_0(1+\delta)-\delta\bigr)}{1+2\delta}
   =O(\tau^3).
\]

At (k=2048),

\[
 H=\frac{4177921}{144115256795332608},\qquad
 H-16\tau=
 -\frac{1125900439535615}{144115256795332608}.
\]

The thin graft therefore misses tallness by a linear-in-(\tau) amount while
producing only cubic height. Clone lifts preserve the exact deficit. A
completion that changes the row polytope or visible set is outside this
checked clone-safe class and remains open here.

### W61 dyadic leak-financer

The context range is dyadic exponents (k=8,\ldots,16); the script
independently reconstructs and verifies the best endpoint (k=16). With
(\tau=2^{-k}), (\varepsilon=\delta/2),
(t^*(A)=\tau/8), and (\eta=\varepsilon t^*(A)=\tau^3/16), exact primal
and dual certificates give

\[
 H=\frac{2\eta}{1+\delta/2-\eta}=O(\tau^3).
\]

At (k=16),

\[
 H=\frac2{4503599627894783},\qquad
 H-16\tau=-\frac{4503599627886591}{18446744075857031168}.
\]

The full fibers are (A=\{a_0,a_1\},Z,C,D,X). The script verifies
(W=\{Z,C,D\}), the hiddenness balance

\[
 (p_D-p_A)+\varepsilon^{-1}(p_Z-p_A)
   =t^*(A)(p_C-p_A),
\]

the closest (Z,D) barycenter, and the matching top support functional.
Again, the local financing ledger survives only because the height is cubic;
clone splitting does not alter that scale.

### W55 (A_0=5, g=5\tau) starvation plateau

The pinned scalar identities were tested at (\tau=1/256),
(t=\tau^2), (a=\tau/(1+\tau)). The top coefficients

\[
 c_v=1-\tau,qquad c_w=\tau+t,qquad c_f=-t
\]

reproduce the top exactly because ((\tau+t)a=t). In the canonical
rank-three disjoint-support left inverse, the finance row necessarily has

\[
 \nu_f=A_0+(1+A_0-t)t
 =\frac{21475229695}{4294967296},
\]

whereas the target is (t=1/65536). Its exact excess is

\[
 \nu_f-t=\frac{21475164159}{4294967296}>0.
\]

So the direct completion fails the all-row-negativity gate before visible-set
or tallness tests become relevant. The registered
`lem-starvation-completion-obstruction` additionally rules out every
rank-three completion with (A\in[4,6]), (\tau\le1/256), and all added
nonactor support in the pinned actor hull or slab (0\le y_Q\le1). Its
binding identity is the unit transverse moment versus only (O(\tau))
supply. This report does not extend that theorem to higher rank or support
outside the slab.

## Dead ends and scope

- Pointwise small (Z_v(p_Q)) was never promoted to a fan conclusion; the
  quotient barycenter's **actual** ray minimum was recomputed.
- The local-center condition was checked uniformly by a metric lower
  certificate, not by sampling centers.
- Width was computed on full row-point fibers with the scalar affine
  definition. No coordinate projection was substituted for the supremum.
- Clone splitting cannot fix any displayed height or width margin because all
  relevant objects are full-fiber and row-point quantities.
- More general high-rank completions that change the visible hull, and
  genuinely low-width internally reproducing webs, remain unsearched by these
  closed-form families. Consequently none of the three `BLOCKED` verdicts is
  a universal mathematical obstruction.

## Reproduction

Run:

```text
python3 search.py
```

Expected final lines:

```text
EXACT CHECKS PASSED: 3 BLOCKED-family verdicts; 0 genuine L5 refuters.
L3 EVIDENCE ONLY — this computation is not a proof.
```
