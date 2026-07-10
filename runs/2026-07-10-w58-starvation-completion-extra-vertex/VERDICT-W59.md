# W59 hostile verification of `PAPER-PROOF.md`

Status: **COMPLETE**.  Every displayed estimate was independently derived;
references below are to line numbers in `work/PAPER-PROOF.md`.

## Findings

1. **MINOR — undefined index-level coordinate shorthand.**  Location: Claim 2,
   lines 125--144, especially “Using the canonical expansion
   `p_j=p_v+x_jD+y_jE`” and “The coordinate `x_j` is constant on a row-point
   fiber.”  The contract defines only \(x_Q,y_Q\) for a full row-point fiber
   \(Q\), and unlike \(c_u,d_u,e_u\) it never defines \(x_j:=x_{[j]}\) or
   \(y_j:=y_{[j]}\).  The intended meaning is unique and makes (5) correct, so
   this is not a mathematical gap, but a claimed standalone proof should add
   that abbreviation before (5).

2. **NOTE — several tableau pins are deliberately unused.**  Location:
   statement line 44 and Claims 2--5.  The proof uses the zero-top condition
   \(c_Q=0\) for exterior fibers, but never uses the numerical actor top masses
   \(c_v=1-\tau,c_w=\tau+t,c_f=-t\).  It uses the \(w\)-relation only to put
   \(x_w=-Aa\) inside \([-A,1]\); no later estimate uses its exact value.
   Likewise, zero-top for added fibers *inside* the actor hull is unnecessary.
   The explicit distinctness of the five actor fibers and the existence and
   uniqueness of all \((x_Q,y_Q)\) are also derivable from the remaining
   transversality/rank assumptions.  This is not a failure: the argument proves
   a stronger obstruction obtained by weakening those pins.  The hypothesis
   audit should not imply every displayed pin is quantitatively consumed.

## Independent derivation ledger

### Contract and coordinates

- \(P{\bf1}={\bf1}\) gives row sums one.  Hence \(D=p_z-p_v\) and
  \(E=p_o-p_v\) have coordinate sum zero, while \(p_v\) has coordinate sum
  one.  Independence of \(D,E\) therefore makes \(p_v,D,E\) independent.
  They lie in the row space and, since its dimension is three, form a basis.
  Every row has coefficient one on \(p_v\), proving existence and uniqueness
  of the claimed \((x_Q,y_Q)\).  No shard is needed.
- The actor coordinates recompute as
  \(v=(0,0),z=(1,0),o=(0,1),f=(-A,t),w=(-Aa,ta)\).  Since
  \(0<a<1\) and \(A\ge4>1\), every convex combination has
  \(-A\le x\le1\) and \(|x|\le A\).
- Although the numerical actor top pins are not needed for the contradiction,
  they are algebraically compatible with top-row reproduction:
  \(\sum_Qc_Q=1\),
  \((\tau+t)a=t\), and therefore
  \[
  \sum_Qc_Qx_Q=-A(\tau+t)a+At=0,\qquad
  \sum_Qc_Qy_Q=t(\tau+t)a-t^2=0.
  \]
  Thus the pinned coefficient row has barycenter \(p_v\); there is no hidden
  arithmetic mismatch in the tableau itself.

### Claims 1--2

- If \(\nu_i=\sum_jP_{ij}^-\le t\), row sum one gives
  \(\sum_jP_{ij}^+=1+\nu_i\).  Thus every subset mass lies in
  \([-\nu_i,1+\nu_i]\subseteq[-t,1+t]\), and
  \(\|p_i\|_1=1+2\nu_i\le1+2t\).  Claim 1 is exact.
- Idempotence gives \(DP=(p_z-p_v)P=p_z-p_v=D\).  Expanding every row in
  the basis gives
  
  \[
  D=\left(\sum_jx_jD_j\right)D+
    \left(\sum_jy_jD_j\right)E.
  \]
  
  Independence forces the first coefficient to be exactly \(1\), not merely
  bounded below.  Grouping the finite coordinate sum by equal-row fibers gives
  \(\sum_Qx_Qd_Q=1\).  These are actual matrix coefficients; no LP multiplier
  is reified as mass.

### Claims 3--4

- For an exterior support fiber \(Q\), \(0\le Y_Q\le1\) and
  \(p_Q=p_v+X_QD+Y_QE\) imply
  \(X_QD=p_Q-(1-Y_Q)p_v-Y_Qp_o\).  The three row norm bounds give
  
  \[
  |X_Q|\tau\le(1+2t)+(1-Y_Q)(1+2t)+Y_Q(1+2t)=2+4t.
  \]
  
  Both closed slab endpoints are legitimate.
- An exterior fiber cannot be an actor fiber and so has \(c_Q=0\).  Therefore
  \(P_z(Q)=d_Q\), \(P_o(Q)=e_Q\), and
  \(P_f(Q)=-Ad_Q+te_Q\).  On the union of fibers with \(d_Q<0\), the row-\(z\)
  lower subset bound gives \(\sum|d_Q|\le t\).  On the union with
  \(d_Q\ge0\), write \(D_+=\sum d_Q\) and \(E_+=\sum e_Q\).  The row-\(f\)
  lower bound and row-\(o\) upper bound give
  
  \[
  -AD_++tE_+\ge-t,\qquad E_+\le1+t,\qquad
  AD_+\le t(E_++1)\le t(2+t).
  \]
  
  This remains valid without a sign assumption on \(E_+\).  Hence
  
  \[
  \sum_{Q\in\mathscr E}|d_Q|
  \le t\left(1+\frac{2+t}{A}\right)
  \]
  
  using each genuine row-subset budget once.  No number of fibers occurs.

### Claim 5 and constants

- Nonsupport means \((c_Q,d_Q,e_Q)=(0,0,0)\), so its moment contribution is
  zero.  The support fibers are partitioned into hull and exterior fibers by
  the stated hypothesis.  On the hull, \(|x_Q|\le A\), while aggregation can
  only reduce variation:
  
  \[
  \sum_{Q\in\mathscr H}|d_Q|
  \le\sum_Q\left|\sum_{j\in Q}D_j\right|
  \le\sum_j|D_j|=\tau.
  \]
  
  Thus the hull contribution is at most \(A\tau\).  Combining this with the
  lever and exterior-variation bounds yields exactly
  
  \[
  1\le\tau\left[A+(2+4t)\left(1+\frac{2+t}{A}\right)\right].
  \]
- The paper's crude close is arithmetically correct.  From
  \(\tau\le1/256\), \(t<1/4\) and \(t<1\); hence
  \(2+4t<3\), \((2+t)/A\le(2+t)/4<3/4\), and \(A\le6\).
  Consequently the last right side is strictly less than
  \[
  \frac1{256}\left(6+3\cdot\frac74\right)
  =\frac{45}{1024}<1.
  \]
  The contradiction margin supplied by this displayed upper bound is
  \(1-45/1024=979/1024\).
- For an endpoint check stronger than the paper needs, the bracket is increasing
  in \(t\), and its \(A\)-derivative is
  \[
  1-\frac{(2+4t)(2+t)}{A^2}>0
  \]
  on the domain (already \(t<1/4,A\ge4\) makes the subtracted numerator less
  than \(27/4<16\)).  The entire right side is therefore largest at
  \(\tau=1/256,A=6\).  At the two requested \(A\)-endpoints:
  \[
  \begin{array}{c|c|c}
  A&\text{right side of (19)}&1-\text{right side}\\ \hline
  4&\dfrac{30065197057}{1099511627776}&
     \dfrac{1069446430719}{1099511627776}\\[2mm]
  6&\dfrac{18611710635}{549755813888}&
     \dfrac{531144103253}{549755813888}
  \end{array}
  \]
  Both are far below one; the \(A=6\) value is the true worst endpoint.

## K-free and clone audit

- Finiteness is used only because \(I\), the fiber partition, the grouped
  moment sum, and the two unions \(S_\pm\) are finite.  There is no infinite
  series, choice of a smallest fiber, pigeonhole step, or division by the
  number of fibers.  The theorem claims arbitrarily large *finite* fiber sets,
  exactly what the proof supports.
- The quantities \(c_Q,d_Q,e_Q\) and \(x_Q,y_Q\) are full-fiber aggregates or
  row-point coordinates.  The signs used in Claim 4 are signs of aggregate
  \(d_Q\), and each ledger is applied to a union in the original coordinate
  set.  Internal cancellation inside a clone fiber is therefore harmless.
  The sole original-coordinate variation \(\sum_j|D_j|=\tau\) is the stated
  metric pin, not a count.  Under the standard nonnegative weighted clone
  split it is invariant; irrespective of multiplicity, inequality (18) is
  valid for every matrix satisfying the contract.  No estimate contains a raw
  fiber count.

## Hypothesis audit

Every hypothesis actually used is stated:

- finiteness: finite grouping and subset unions;
- \(P^2=P\): \(DP=D\);
- \(P{\bf1}={\bf1}\) and \(\nu_i\le t\): the subset and row-norm ledgers;
- rank three plus independence of \(D,E\): the two-coordinate row-space basis;
- \(0<\tau\), \(t=\tau^2\), and \(\|D\|_1=\tau\): division in (8), variation in
  (18), and conversion of \(t/\tau\) to \(\tau\);
- \(p_f-p_v=-AD+tE\): the row-\(f\) exterior budget;
- \(A\in[4,6]\): hull coordinate bound, positive division by \(A\), and final
  close;
- full-fiber zero-top outside \(v,w,f\): \(c_Q=0\) on exterior fibers;
- actor-hull or closed-slab placement for every nonactor support fiber: the
  exhaustive support partition and lever bound.

No unstated positivity of \(e_Q\), no per-entry fiber sign, and no admissibility
condition on nonsupport fibers is used.  The redundant assumptions are exactly
those noted in Finding 2; redundancy strengthens, rather than invalidates, the
proved conclusion.

## Shard and dead-route audit

- The proof invokes no `argument/` shard.  All five claims are derived directly
  from the displayed matrix hypotheses, so there is no quotation-fidelity or
  status mismatch to audit.  The mention of
  `conj-sl1a-off-diagonal-cell` in §MECHANISM is explicitly prospective and is
  not a premise.
- There are no dual multipliers, \(\lambda P=p_v\) identifications, transition
  flows, raw-index floors, or mutually-\(\rho\)-far selections.  The symbols
  \(d_Q,e_Q\) are literal sums of entries in row differences, and the proof
  never treats them as nonnegative transition mass.

## W57/W58 inclusion check

The cross-check against `work/FORMULATION.md` succeeds:

- the parent three cases use the five rank-three actor rows with the exact
  actor relations, top pins, all-row negativity bound, and metric pin; the
  actor-only and near cases add no exterior support, while
  `hx_far_r3_nonvertex6` adds
  \(p_x=(p_v+p_f)/2\in\mathcal H\) with zero top mass;
- the exterior three cases add one zero-top \(q=(1,X,Y)\) outside the old actor
  hull with \(0\le Y\le1\); their far case additionally adds
  \(p_m=(p_v+p_f)/2\in\mathcal H\);
- \(BL=I_3\) in that formulation makes \(D,E\) independent (if
  \(\alpha D+\beta E=0\), multiply \((0,\alpha,\beta)B=0\) by \(L\)), so the
  paper's explicit transversality hypothesis does not lose a decided case;
- the raw point is \(A=5,\tau=1/256\), and the rational stability locus is
  contained in the paper's real \(A\in[4,6]\), \(0<\tau\le1/256\) domain.

Freight, distance, visible-set, and sign-cell restrictions only narrow these
six subclasses.  The closed lever estimate covers \(Y=0\) and \(Y=1\).

## Honest-limits audit

The limitations are accurate.  In rank greater than three, the coefficient
identity \(\sum_Qx_Qd_Q=1\) can still be obtained after extending
\(p_v,D,E\) to a basis, but (9) gains uncontrolled transverse terms; hence
the lever estimate and final financing close do not follow.  Lines 398--401
attribute the failure to exactly those extra terms and say that the
*two-coordinate close*, not the bare idempotence identity, fails.  The slab,
zero-top, and exact-metric limitations match the places where they are used.

## Statement-quality audit

The registry contract is one grammatical sentence, quantifies the finite
ambient set and the real parameters, fixes all constants, and has no
dimension- or fiber-count-dependent threshold.  Its fiber definitions precede
the sentence, so “support,” “zero-top,” “nonactor,” and all aggregate
coefficients are self-contained.  The implication to the fixed-\(K\) ceiling
is correct because every \(0<\tau\le\min\{1/256,1/(12(K+1))\}\) lies in the
proved universal domain, while every finite matrix has only finitely many
full row-point fibers.

## Final verdict

**VERDICT: VALID-WITH-CORRECTIONS — the obstruction and K-free strengthening
are proved, with only one missing notational abbreviation in Claim 2.**

Mechanical correction:

1. Before equation (5), add
   “For \(j\in I\), write \(x_j:=x_{[j]}\) and \(y_j:=y_{[j]}\).”
