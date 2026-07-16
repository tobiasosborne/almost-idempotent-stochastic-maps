# Appendix: standalone proofs for the routine DTR/POTI batch

> **Status.** This appendix verifies the four proposed routine implications below. It
> does not change any registry status and does not promote any conjecture. In
> particular, POTI-0 and POTI\(+\) remain hypotheses only in the conditional
> assembly. All measures are nonnegative measures on full row-point fibers in the
> exact signed picture.

## 0. Pinned datum and common hypothesis audit

Let \(I\) be the finite index set of \(P\), and let

\[
 \mathcal Q:=I/{\sim},\qquad i\sim j\iff p_i=p_j,
\]

be the finite row-point quotient. An atom \(Q\in\mathcal Q\) is a full
row-point fiber and \(p_Q\) is its common row point. The pinned DTR datum is
exactly the datum of `context/AESC-ATTACK-W67.md` §1.6, restricted by
`DTR-ATTACK.md` (1.1)--(1.2). Thus the following facts are fixed before any
tail is measured.

1. \(c_m=1/4\), \(b=c_m/128\),
   \(\delta=\delta(P)>0\), \(\tau=\sqrt\delta\),
   \(D_0=2+4\delta\), and
   \[
     \delta\le\delta_{\rm rt}
     =\min\{2^{-16},(c_m/4)^2,(c_mb/120)^2\}\le1/4.
   \]
2. \(P\) is a finite exact signed idempotent, \(P\mathbf1=\mathbf1\) and
   \(P^2=P\); its visible set \(W\) is nonempty; \(v\) is a hidden top
   vertex of height \(H>16\tau\).
3. Every \(j\in A\) satisfies
   \(\|p_j-p_v\|_1\ge4\tau\) and
   \(\operatorname{dist}_1(p_j,C_W)>H-8\tau\). The original selected
   measure and its barycenter are
   \[
     m_A(Q)=\sum_{j\in A\cap Q}(P_{vj})_+,
     \quad S=m_A(1)\ge c_m>0,
     \quad q_A=S^{-1}\sum_Qm_A(Q)p_Q.
   \]
4. The I-base all-center exterior hypotheses, the parent bounds on
   \(r_\omega\) and \(\Omega(\omega)\), the ultra bounds
   \(\|r_\omega-p_v\|_1<b\tau\), \(\Omega(\omega)<b\tau\), and
   \(\theta<\tau/D_0\) all hold.
5. The public selected-corner certificate
   \(\mathscr C^*=(\phi,h,f^*,\eta^*)\) is one exhibited certificate from
   `lem-ihorn-selected-corner-extraction`, with
   \(M_X\le1/8\), \(M_I<1/16\), and \(M_D>1/16\). In particular,
   \(\phi\in\Phi_v\) is a top support functional. The legal kernel and every
   reduced display were then fixed arbitrarily, before classification.
6. The seven proved D-cap outputs are present. For the arguments below their
   relevant literal consequences are
   \[
      \eta_D^*(u)=\eta^*\{(x,u):p_x=p_u,\ u\text{ is type D}\},
      \qquad \eta_D^*\le P_{f^*}^+
   \]
   as full-fiber measures (`lem-dcap-root-closure`), and
   \[
      P_v^+(\mathcal L_v)<\frac{2\tau}{15},
      \qquad
      P_v^+(\mathcal E_*)\ge\frac{\tau S}{8}
   \]
   (`lem-dcap-tall-same-center-packet`). The realized B5 overlay is retained
   but is not identified with \(\eta_D^*\) and is never used below.
7. With \(B=\mathsf D_{\rm tail}\), the five proved A-esc outputs give
   \[
   \eta_D^*(B)>1/160,\qquad h_u\le3\delta,\qquad
   \min_f\|p_f-x_u\|_1>3\delta,
   \]
   \[
   \operatorname{Tail}_1(u)>\tau/8\quad(u\in B),\qquad
   P_{f^*}^+(\mathcal U_{\rm tail})>\tau/2560.
   \]
   The set \(B\) is a clone-invariant set of row-point atoms. Equality
   \(h_u=3\delta\) belongs to \(B\), actor-residual equality belongs to
   T-esc, and the mass equality \(1/160\) belongs to HES.

The certificate \(\mathscr C^*\), and therefore \(\phi\), is fixed before
\(B\), any \(\mathcal T_u\), or any tail level is measured. Put

\[
 z(p):=H-\phi(p).
\]

The pinned \(\phi\) is never replaced below.

## 1. COV — canonical root/top overlap

### Pinned contract (verbatim)

**(a) Pinned contract —**
\(\texttt{conj-w69-dtr-canonical-root-top-overlap}\).
For every pinned DTR datum, the measure

\[
 \rho(Q)=\min\{m_A(Q),\eta_D^*(B\cap Q)\}                  \tag{COV}
\]

is a canonical full-fiber common submeasure of \(m_A\) and \(\eta_D^*|_B\).

### Registry shards consumed and literal hypothesis match

- `lem-l5-mass-barycenter-dualization`: its \(P,W,v,H,A,S\) hypotheses are
  items 1--3 above. Its measure is literally
  \(m_Q=\sum_{j\in A\cap Q}(P_{vj})_+\), including the case in which \(A\)
  is not fiber-saturated. Thus it is the original \(m_A\), not
  \(\lambda_A\) and not \(a_A=S(1-\theta)\lambda_A\).
- `lem-ihorn-selected-corner-extraction`: items 1--5 are its I-base,
  ultra, thin-rim, kernel, and selected-corner hypotheses. It places
  \(\eta^*\) on row-point pairs and makes its type masses clone-invariant.
- `lem-dcap-root-closure`: items 1--6 match its common I-base block,
  \(\delta\)-ceiling, ultra bounds, thin-rim bound, fixed certificate, and
  D-cell inequalities line by line. Its literal conclusion says that
  \(\eta_D^*\) is a full-fiber measure dominated by \(P_{f^*}^+\).
- `lem-aesc-guarded-hull-split`: the A-esc priority mass and fixed displays
  are inherited in items 5--7, and its two predicates are
  \(h_u>3\delta\) and \(h_u\le3\delta\). Hence its \(B=\mathsf D_{\rm
  tail}\) is a union of full row-point atoms.

No `lem-icap-*` shard, B5 overlay, intersection-production shard, or
conditional huddle-charge assembly is consumed.

### Proof

The substantive point is that both inputs to the minimum live on the same
space. The selected measure is initially described using indices in \(A\), but
it is pushed to \(\mathcal Q\) by full-fiber aggregation:

\[
 m_A(\{Q\})=\sum_{j\in A\cap Q}(P_{vj})_+.
\]

On the other hand, `lem-dcap-root-closure` has already erased the diagonal
pair variable and defines \(\eta_D^*\) on the row-point variable \(u\). Since
that shard states full-fiber domination by \(P_{f^*}^+\), its atoms are the
same atoms \(Q\in\mathcal Q\). Because \(B\) is defined by row-point geometry
and fixed display scalars, it is a subset of \(\mathcal Q\), and

\[
 n_B(Q):=(\eta_D^*|_B)(\{Q\})=\eta_D^*(B\cap Q)
\]

is a second nonnegative atomic measure on \(\mathcal Q\). No common parent
measure is asserted or needed.

Define atom masses

\[
 \rho_Q:=\min\{m_A(Q),n_B(Q)\}\ge0
\]

and, for every \(E\subseteq\mathcal Q\), define

\[
 \rho(E):=\sum_{Q\in E}\rho_Q.                            \tag{1.1}
\]

Because \(\mathcal Q\) is finite, (1.1) is a measure: \(\rho(\varnothing)=0\),
and for pairwise disjoint \(E_1,\ldots,E_k\),

\[
 \rho\!\left(\bigcup_iE_i\right)
 =\sum_{Q\in\cup_iE_i}\rho_Q
 =\sum_i\sum_{Q\in E_i}\rho_Q
 =\sum_i\rho(E_i).
\]

Moreover, atomwise \(\rho_Q\le m_A(Q)\) and \(\rho_Q\le n_B(Q)\), so for
every \(E\subseteq\mathcal Q\),

\[
 \rho(E)\le\sum_{Q\in E}m_A(Q)=m_A(E),
 \qquad
 \rho(E)\le\sum_{Q\in E}n_B(Q)=(\eta_D^*|_B)(E).        \tag{1.2}
\]

This is an atomwise minimum followed by additive extension. It is **not** the
set function \(E\mapsto\min\{m_A(E),(\eta_D^*|_B)(E)\}\), which need not be
a measure.

Finally, under a compatible clone split, the geometric quotient
\(\mathcal Q\) is canonically unchanged. The weighted lift described in
`lem-l5-mass-barycenter-dualization` preserves the total selected weight in
each row-point fiber, even for a partially selected fiber; the selected-corner
kernel is constant on clone fibers; `lem-dcap-root-closure` makes
\(\eta_D^*\) full-fiber; and membership in \(B\) depends only on the row point
and its fixed fiber-aggregated data. Thus both atom profiles \(m_A(Q)\) and
\(n_B(Q)\) descend to the quotient and are clone-invariant. Their numerical
minimum does too. The construction makes no atom, support subset, certificate,
or tie choice, so it is canonical relative to the already pinned datum. This
proves COV. \(\square\)

## 2. POTI-R — pinned oriented-tail surplus reaches the ray

For \(u\in B\), write

\[
 c_{u,R}:=\sum_{j\in R}P_{uj},\qquad
 \mathcal T_u:=\{R\in\mathcal Q:|\chi_u(p_R)|>1\},
\]

\[
 \mathfrak t_\phi(u):=
 \sum_{R\in\mathcal T_u}(c_{u,R})_+z(p_R),
 \qquad
 \mathfrak G_\phi:=
 \sum_{u\in B}\rho(u)
 [\mathfrak t_\phi(u)-D_0\delta]_+ .                    \tag{2.1}
\]

Here and below \(\rho(u)\) means the mass of the row-point atom containing
\(u\).

### Pinned contract (verbatim)

**(a) Pinned contract —**
\(\texttt{conj-w69-dtr-pinned-deficit-oriented-tail-to-ray}\).
Every pinned DTR datum satisfies

\[
 S Z_v(q_A)\ge\mathfrak G_\phi.                            \tag{POTI-R}
\]

### Registry shards consumed and literal hypothesis match

- `lem-ihorn-selected-corner-extraction`: items 1--5 of §0 match its complete
  I-base/ultra/thin-rim block and certify that the fixed \(\phi\) is a top
  support functional at \(v\).
- `lem-top-deficit-price`: items 1--2 give an exact signed idempotent with
  \(\delta>0\), nonempty \(W\), and hidden top \(v\). Its statement applies
  to **any** top support functional and to every row index. Thus its
  nonnegativity assertion is not restricted to \(A\), to the selected corner,
  or to top-selected carriers.
- `lem-top-support-dual-face`: the same items match its hypotheses. Since the
  pinned \(\phi\in\Phi_v\), its literal characterization supplies one fixed
  \(y_\phi\in Y_v\) whose affine functional agrees with \(\phi\) on every
  row point.
- `def-signed-idempotent` and `def-negative-mass`: item 2 gives
  \(P^2=P\), \(P\mathbf1=\mathbf1\); by definition
  \(\nu_u:=\sum_j(-P_{uj})_+\le\delta(P)=\delta\) for every row \(u\).
- `lem-l5-mass-barycenter-dualization`: items 1--3 match every literal
  hypothesis, including \(H>16\sqrt\delta\), the far/deep conditions on each
  \(j\in A\), and \(S>0\). Its conclusion is for the original \(m_A\) and
  \(q_A\); no normalization change is present.
- `lem-l5-top-face-ray-formula`: items 1--3 give its exact signed
  idempotent, visible hull, hidden top, and \(q_A\in K(P)\) hypotheses. The
  last fact holds because \(q_A\) is a convex combination of row points with
  weights \(m_A(Q)/S\).

COV supplies the already proved common submeasure \(\rho\). The A-esc shards
fix \(B,\chi_u,c_{u,R}\), but neither their TU foldback conclusion nor the
root-owned union mass is used in this proof. No B5 quantity is used.

### Global pinned-deficit audit

The scope required in the sign split is genuinely available. Since
\(\phi(p_v)=H\),

\[
 z(p_Q)=H-\phi(p_Q)=\phi(p_v)-\phi(p_Q).
\]

For every row point \(Q\), not merely for \(Q\in A\) or \(Q\in B\), the
height definition and the support-functional inequalities give

\[
 \phi(p_Q)\le\operatorname{dist}_1(p_Q,C_W)\le H,
 \qquad z(p_Q)\ge0.                                     \tag{2.2}
\]

The \(1\)-Lipschitz property of \(\phi\), followed by the signed row-diameter
bound, gives

\[
 0\le z(p_Q)
 =\phi(p_v)-\phi(p_Q)
 \le\|p_v-p_Q\|_1
 \le2+4\delta=D_0.                                     \tag{2.3}
\]

Thus there is no subclass extension hidden in (2.2)--(2.3). The top-face
shard gives a single \(y_\phi\in Y_v\), fixed with the certificate, such that
on every row point

\[
 \phi(p_Q)=y_\phi\cdot p_Q-h_{C_W}(y_\phi),
 \qquad
 z(p_Q)=y_\phi\cdot(p_v-p_Q).                          \tag{2.4}
\]

### Exact reproduction and the sign split

The \(u\)-th row of \(P^2=P\) says

\[
 p_u=\sum_jP_{uj}p_j=\sum_{R\in\mathcal Q}c_{u,R}p_R,
 \qquad
 \sum_Rc_{u,R}=\sum_jP_{uj}=1.                         \tag{2.5}
\]

Because \(z\) is affine, the mass-one identity in (2.5) is exactly what is
needed, even though the coefficients are signed:

\[
 z(p_u)=\sum_Rc_{u,R}z(p_R).                            \tag{2.6}
\]

For each full fiber, scalar negative-part subadditivity gives

\[
 (-c_{u,R})_+
 =\left(-\sum_{j\in R}P_{uj}\right)_+
 \le\sum_{j\in R}(-P_{uj})_+.
\]

Summing disjoint fibers proves the requested aggregation check:

\[
 \sum_R(-c_{u,R})_+
 \le\sum_R\sum_{j\in R}(-P_{uj})_+
 =\sum_j(-P_{uj})_+
 =\nu_u\le\delta.                                     \tag{2.7}
\]

Thus full-fiber aggregation cannot increase negative coefficient mass. Split
(2.6) into positive tail coefficients, positive off-tail coefficients, and
negative coefficients. By (2.2), every discarded positive off-tail term is
nonnegative. By (2.3), if \(c_{u,R}<0\), then
\(c_{u,R}z(p_R)\ge-D_0(-c_{u,R})_+\). Therefore

\[
\begin{aligned}
 z(p_u)
 &=\sum_Rc_{u,R}z(p_R)\\
 &\ge
   \sum_{R\in\mathcal T_u}(c_{u,R})_+z(p_R)
   -D_0\sum_R(-c_{u,R})_+\\
 &\ge \mathfrak t_\phi(u)-D_0\delta.                  \tag{2.8}
\end{aligned}
\]

Since (2.2) also applies to \(u\), combining \(z(p_u)\ge0\) with (2.8)
gives

\[
 z(p_u)\ge[\mathfrak t_\phi(u)-D_0\delta]_+ .          \tag{2.9}
\]

This confirms the signs and the scope of DTR-ATTACK (1.9)--(1.10).

### Integration against the common submeasure

Every summand below is nonnegative. First, restricting the sum over all row
points to \(B\) discards only terms \(m_A(Q)z(p_Q)\ge0\). Second, COV gives
\(\rho(Q)\le m_A(Q)\) atomwise, and (2.2) gives \(z(p_Q)\ge0\). Hence

\[
\begin{aligned}
 \sum_Qm_A(Q)z(p_Q)
 &\ge\sum_{u\in B}m_A(u)z(p_u)\\
 &\ge\sum_{u\in B}\rho(u)z(p_u)\\
 &\ge\sum_{u\in B}\rho(u)
       [\mathfrak t_\phi(u)-D_0\delta]_+
 =\mathfrak G_\phi.                                   \tag{2.10}
\end{aligned}
\]

### Conversion to the original L5 mass objective and the ray

Fix an **arbitrary** attained minimizer \((\Lambda,c)\) from
`lem-l5-top-face-ray-formula`; when \(\Lambda=0\), omit \(c\). The shard's
literal conclusion gives

\[
 Z_v(q_A)=
 \|p_v-q_A+\Lambda(p_v-c)\|_1-\Lambda H.               \tag{2.11}
\]

At \(\Lambda=0\), this reads simply
\(Z_v(q_A)=\|p_v-q_A\|_1\). No minimizer is selected for a favorable
property, and every attained tie gives (2.11).

Now apply `lem-l5-mass-barycenter-dualization`. Its measure is exactly the
original \(m_A\), so no renormalization is required:

\[
\begin{aligned}
 S\bigl(\|p_v-q_A+\Lambda(p_v-c)\|_1-\Lambda H\bigr)
 &=S Z_v(q_A)\\
 &=\sup_{y\in Y_v}
   \sum_{j\in A}(P_{vj})_+\,y\cdot(p_v-p_j)\\
 &\ge\sum_{j\in A}(P_{vj})_+
        y_\phi\cdot(p_v-p_j)\\
 &=\sum_Qm_A(Q)z(p_Q)\\
 &\ge\mathfrak G_\phi.                                \tag{2.12}
\end{aligned}
\]

The penultimate equality uses (2.4) and full-fiber aggregation. Equations
(2.10)--(2.12) prove POTI-R.

There is no new foldback here. TU's earlier use of the common indicator
\(1_{\mathcal U_{\rm tail}}\) remains the sole DTR aggregation foldback;
POTI-R uses the one fixed nonnegative scalar test \(z/D_0\in[0,1]\), exact
row reproduction, and direct integration against the already common measure
\(\rho\). It introduces neither \(1/t^*\), witness averaging, nor a second
positive-flow foldback. \(\square\)

### Routine nonnegative-deficit close, including equality

Define

\[
 \mathcal D_{\rm POTI}:=
 \mathfrak G_\phi-\frac S8P_v^+(\mathcal E_*)
 +\frac{c_mS}{16}P_v^+(\mathcal L_v).
\]

If \(\mathcal D_{\rm POTI}\ge0\), with equality included, then \(S>0\) and
POTI-R give

\[
\begin{aligned}
 Z_v(q_A)
 &\ge\frac{\mathfrak G_\phi}{S}\\
 &\ge\frac18P_v^+(\mathcal E_*)
       -\frac{c_m}{16}P_v^+(\mathcal L_v).              \tag{2.13}
\end{aligned}
\]

In particular \(\mathcal D_{\rm POTI}=0\) belongs to this routine close;
\(\mathfrak G_\phi=0\) remains assigned to POTI-0 when the diagnostic is
negative.

## 3. TC — tail-coherent weakened conversion

Fix before the datum

\[
 0<r_0\le1/160,qquad0<\alpha\le1,qquad0<\lambda\le1,
\]

and define

\[
 \mathsf C_{\alpha,\lambda}:=
 \left\{u\in B:
  \sum_{\substack{R\in\mathcal T_u\\z(p_R)\ge\lambda}}
       (c_{u,R})_+
  \ge\alpha\operatorname{Tail}_1(u)\right\},
 \qquad
 r_{\alpha,\lambda}:=\rho(\mathsf C_{\alpha,\lambda}). \tag{3.1}
\]

Equality in (3.1) belongs to the coherent class.

### Pinned contract (verbatim)

**(a) Pinned contract —**
\(\texttt{conj-w69-dtr-tail-coherent-weakened-conversion}\).
If

\[
 \delta\le\delta_{\rm coh}:=
 \min\{\delta_{\rm rt},(\alpha\lambda/48)^2\},\qquad
 r_{\alpha,\lambda}\ge r_0,                               \tag{1.18}
\]

then

\[
 Z_v(q_A)>
 \frac{r_0\alpha\lambda}{16S}\tau
 \ge\gamma_{\rm coh}\tau,\qquad
 \gamma_{\rm coh}:=
 \frac{r_0\alpha\lambda}{16(1+\delta_{\rm coh})}.          \tag{TC}
\]

### Registry shards consumed and literal hypothesis match

- COV and POTI-R, proved in §§1--2, supply the full-fiber \(\rho\) and
  \(S Z_v(q_A)\ge\mathfrak G_\phi\).
- `lem-aesc-synthetic-finance-tail-amplification`: its common I-base,
  \(c_m=1/4\), \(\delta_{\rm rt}\), fixed certificate, root measure, fixed
  display, and normalized carrier hypotheses are items 1--7 of §0. For
  \(u\in B\subseteq\mathsf A_{\rm esc}\), the class definition gives
  \(g_u\ge\tau\), \(A_u\ge4\), and \(\ell_u\ge\tau/2\), while
  \(h_u=\operatorname{dist}_1(x_u,K(P))\le3\delta\). Its literal pointwise
  conclusion therefore gives
  \(\operatorname{Tail}_1(u)>\tau/8\) for every \(u\in B\).
- `def-negative-mass` and the I-base relation in
  `context/AESC-ATTACK-W67.md` (1.2) give the exact relation
  \(\tau=\sqrt\delta\), not merely an asymptotic comparison.
- From `def-signed-idempotent`, the positive mass in row \(v\) is
  \(P_v^+(1)=1+\nu_v\le1+\delta\). Since \(m_A\le P_v^+\),
  \(S\le P_v^+(1)\).

No creative residual and no B5 overlay is consumed.

### Proof and constant audit

Let \(u\in\mathsf C_{\alpha,\lambda}\). Every term in
\(\mathfrak t_\phi(u)\) is nonnegative, so restriction to the fixed level
\(z\ge\lambda\), the coherence inequality, and the strict W67 tail floor give

\[
\begin{aligned}
 \mathfrak t_\phi(u)
 &\ge
 \sum_{\substack{R\in\mathcal T_u\\z(p_R)\ge\lambda}}
      (c_{u,R})_+z(p_R)\\
 &\ge\lambda
 \sum_{\substack{R\in\mathcal T_u\\z(p_R)\ge\lambda}}
      (c_{u,R})_+\\
 &\ge\alpha\lambda\operatorname{Tail}_1(u)
 >\frac{\alpha\lambda}{8}\tau.                         \tag{3.2}
\end{aligned}
\]

The pinned relation is \(\delta=\tau^2\). Since
\(\delta\le\delta_{\rm rt}\le1/4\),

\[
 D_0=2+4\delta\le2+4(1/4)=3.                            \tag{3.3}
\]

The coherence ceiling and positivity of \(\alpha\lambda\) give

\[
 \tau=\sqrt\delta\le\frac{\alpha\lambda}{48}.
\]

Consequently the exact deficit estimate needed in (3.2) is

\[
 D_0\delta
 =D_0\tau^2
 \le3\tau^2
 \le3\frac{\alpha\lambda}{48}\tau
 =\frac{\alpha\lambda}{16}\tau.                       \tag{3.4}
\]

This is the complete version of the intermediate sentence
\(D_0\tau\le\alpha\lambda/16\) in DTR-ATTACK §1.4: multiply that true
intermediate inequality by \(\tau\) and use \(\delta=\tau^2\). The quantity
subtracted in POTI-R is \(D_0\delta\), as (3.4) records.

Combining the strict inequality in (3.2) with (3.4),

\[
 \mathfrak t_\phi(u)-D_0\delta
 >\frac{\alpha\lambda}{8}\tau
   -\frac{\alpha\lambda}{16}\tau
 =\frac{\alpha\lambda}{16}\tau>0,
\]

and hence

\[
 [\mathfrak t_\phi(u)-D_0\delta]_+
 >\frac{\alpha\lambda}{16}\tau.                       \tag{3.5}
\]

The quotient is finite, \(r_{\alpha,\lambda}\ge r_0>0\), and (3.5) is
strict at every atom of the coherent class. Therefore

\[
\begin{aligned}
 \mathfrak G_\phi
 &\ge\sum_{u\in\mathsf C_{\alpha,\lambda}}
       \rho(u)[\mathfrak t_\phi(u)-D_0\delta]_+\\
 &>r_{\alpha,\lambda}
       \frac{\alpha\lambda}{16}\tau\\
 &\ge r_0\frac{\alpha\lambda}{16}\tau.                \tag{3.6}
\end{aligned}
\]

POTI-R and \(S>0\) now give, with strictness preserved,

\[
 Z_v(q_A)\ge\frac{\mathfrak G_\phi}{S}
 >\frac{r_0\alpha\lambda}{16S}\tau.                   \tag{3.7}
\]

Finally,

\[
 S=m_A(1)\le P_v^+(1)=1+\nu_v
 \le1+\delta\le1+\delta_{\rm coh},
\]

so all quantities being positive,

\[
 \frac{r_0\alpha\lambda}{16S}\tau
 \ge\frac{r_0\alpha\lambda}
          {16(1+\delta_{\rm coh})}\tau
 =\gamma_{\rm coh}\tau.                                \tag{3.8}
\]

Equations (3.7)--(3.8) prove TC. No actual actor is assumed or inferred.
\(\square\)

### Optional exact upgrade

The optional condition and its consequence form the separate implication

\[
 \boxed{
 \frac{r_0\alpha\lambda}{16S}\tau
 \ge\frac18P_v^+(\mathcal E_*)
       -\frac{c_m}{16}P_v^+(\mathcal L_v)
 \quad\Longrightarrow\quad
 Z_v(q_A)\ge\frac18P_v^+(\mathcal E_*)
       -\frac{c_m}{16}P_v^+(\mathcal L_v).}              \tag{3.9}
\]

Indeed, TC gives a strict inequality from \(Z_v(q_A)\) to the left-hand
scalar in (3.9), and the extra hypothesis bounds that scalar below by the
right-hand target. Thus TC actually gives a strict inequality to the target;
the displayed non-strict conclusion follows. This upgrade uses neither
POTI-0 nor POTI\(+\).

## 4. ASM — conditional exact assembly and weakened assembly

### Minimal conditional contract

Assume the proposed COV conclusion for every pinned DTR datum, assume the
proposed POTI-R inequality for every pinned DTR datum, and assume the following
two named residual hypotheses:

- **POTI-0:** every pinned DTR datum with \(\mathfrak G_\phi=0\) obeys
  \[
    Z_v(q_A)\ge\frac18P_v^+(\mathcal E_*)
       -\frac{c_m}{16}P_v^+(\mathcal L_v);
  \]
- **POTI\(+\):** every pinned DTR datum with
  \[
    0<\mathfrak G_\phi<
    \frac S8P_v^+(\mathcal E_*)
       -\frac{c_mS}{16}P_v^+(\mathcal L_v)
  \]
  obeys the same displayed EC inequality.

Then every pinned DTR datum satisfies the single conclusion

\[
 \boxed{Z_v(q_A)>\frac{7c_m}{960}\tau.}                 \tag{ASM}
\]

This is a conditional contract only. It asserts no proof of POTI-0 or
POTI\(+\).

### Registry shards consumed and literal hypothesis match

- COV and POTI-R are the two proved routine implications in §§1--2.
- POTI-0 and POTI\(+\) are used only with their exact hypothesis classes
  stated above. The lower equality \(\mathfrak G_\phi=0\) belongs to POTI-0;
  equality at the upper POTI\(+\) boundary is excluded from POTI\(+\) and
  belongs to the routine diagnostic close.
- `lem-dcap-tall-same-center-packet`: items 1--6 of §0 match its complete
  I-base, all-center, ultra, thin-rim, fixed certificate, and D-cap block line
  by line. Its literal conclusions are
  \[
    P_v^+(\mathcal E_*)\ge\tau S/8\ge c_m\tau/8,
    \qquad P_v^+(\mathcal L_v)<2\tau/15.
  \]
  The second inequality is strict, and \(\mathcal E_*\) uses the one public
  center \(p_{f^*}\).
- The fact \(S\ge c_m\) is not inferred from B4 or from TU: it is a literal
  I-base hypothesis in `lem-l5-mass-barycenter-dualization`, every D-cap
  shard, and §0 item 3.

The B5 overlay, every `lem-icap-*` shard, `lem-intersection-branch-production`,
and `lem-huddle-charge-assembly` are not consumed.

### Exact EC case split

Fix an arbitrary pinned DTR datum and abbreviate

\[
 T_{\rm EC}:=\frac18P_v^+(\mathcal E_*)
       -\frac{c_m}{16}P_v^+(\mathcal L_v).
\]

If \(\mathfrak G_\phi=0\), the POTI-0 hypothesis gives
\(Z_v(q_A)\ge T_{\rm EC}\).

Suppose \(\mathfrak G_\phi>0\). If
\(\mathcal D_{\rm POTI}<0\), then rearranging its definition gives exactly

\[
 0<\mathfrak G_\phi<
 \frac S8P_v^+(\mathcal E_*)
 -\frac{c_mS}{16}P_v^+(\mathcal L_v),
\]

so POTI\(+\) gives \(Z_v(q_A)\ge T_{\rm EC}\). If instead
\(\mathcal D_{\rm POTI}\ge0\), including equality, POTI-R and division by
\(S>0\) give

\[
 \boxed{
 Z_v(q_A)\ge\frac{\mathfrak G_\phi}{S}
 \ge\frac18P_v^+(\mathcal E_*)
       -\frac{c_m}{16}P_v^+(\mathcal L_v).}              \tag{4.1}
\]

These cases are exhaustive and establish the exact EC line for every pinned
datum. COV is what makes \(\rho\), and therefore \(\mathfrak G_\phi\), a
legitimate common-measure diagnostic; it supplies no unproved positive
overlap.

### One E spend at \(p_{f^*}\), followed by the last shallow spend

Apply B4.2 once, at its literal public center \(p_{f^*}\). Multiplication by
\(1/8\), followed by the pinned \(S\ge c_m\), gives

\[
 \frac18P_v^+(\mathcal E_*)
 \ge\frac18\frac{\tau S}{8}
 =\frac{\tau S}{64}
 \ge\frac{c_m\tau}{64}.                                 \tag{4.2}
\]

Substitution into (4.1), while retaining the shallow subtraction, yields

\[
 Z_v(q_A)\ge\frac{c_m\tau}{64}
       -\frac{c_m}{16}P_v^+(\mathcal L_v).               \tag{4.3}
\]

Only now apply the strict B4.1 bound
\(P_v^+(\mathcal L_v)<2\tau/15\). Since its coefficient in (4.3) is
negative, the inequality becomes strict:

\[
\begin{aligned}
 Z_v(q_A)
 &>\frac{c_m\tau}{64}
    -\frac{c_m}{16}\frac{2\tau}{15}\\
 &=\left(\frac1{64}-\frac1{16}\frac2{15}\right)c_m\tau\\
 &=\left(\frac{15}{960}-\frac8{960}\right)c_m\tau\\
 &=\frac{7c_m}{960}\tau.                                \tag{4.4}
\end{aligned}
\]

Here \(1/64=15/960\) and
\((1/16)(2/15)=2/240=1/120=8/960\). This proves the single ASM conclusion,
with E used once and the strict T/shallow bound used last. \(\square\)

### Weakened assembly from TC alone

Fix \((r_0,\alpha,\lambda,\delta_{\rm coh})\) before the datum. For a pinned
datum satisfying (1.18), TC itself gives, without POTI-0 or POTI\(+\),

\[
 \boxed{
 Z_v(q_A)>
 \frac{r_0\alpha\lambda}{16S}\tau
 \ge\gamma_{\rm coh}\tau.}                             \tag{4.5}
\]

This is exactly the weakened variant (2.5). If the optional scalar hypothesis
(3.9) is also imposed, its separately proved implication gives EC, after which
(4.2)--(4.4) apply. Without (3.9), (4.5) is the complete weakened conclusion
and no creative residual is used.

### Diagnostic ordering

For completeness, define

\[
 \mathcal D_{\rm EC}:=
 Z_v(q_A)-\frac18P_v^+(\mathcal E_*)
 +\frac{c_m}{16}P_v^+(\mathcal L_v),
\]

\[
 \mathcal D_{\rm leaf}:=
 Z_v(q_A)-\frac{c_m\tau}{64}
 +\frac{c_m}{16}P_v^+(\mathcal L_v).
\]

POTI-R gives \(Z_v(q_A)-\mathfrak G_\phi/S\ge0\), and direct subtraction
therefore gives

\[
 \mathcal D_{\rm EC}-\frac1S\mathcal D_{\rm POTI}
 =Z_v(q_A)-\frac{\mathfrak G_\phi}{S}\ge0.              \tag{4.6}
\]

The already established one-center spend (4.2) gives
\(P_v^+(\mathcal E_*)/8\ge c_m\tau/64\), so no second use of E is made when
recording

\[
 \mathcal D_{\rm leaf}-\mathcal D_{\rm EC}
 =\frac18P_v^+(\mathcal E_*)-\frac{c_m\tau}{64}\ge0.   \tag{4.7}
\]

Thus

\[
 \boxed{
 \mathcal D_{\rm leaf}\ge\mathcal D_{\rm EC}
 \ge\frac1S\mathcal D_{\rm POTI}.}                     \tag{4.8}
\]

The order does not make the diagnostics interchangeable: a negative
\(\mathcal D_{\rm POTI}\) refutes only the sufficient routine close; a
negative \(\mathcal D_{\rm EC}\) refutes EC but need not make
\(\mathcal D_{\rm leaf}\) negative; and a negative leaf diagnostic forces
the EC diagnostic negative.

## 5. Quantifiers, boundary ownership, and forbidden-route audit

For TC the order is

\[
 c_m\longrightarrow(r_0,\alpha,\lambda,\delta_{\rm coh})
 \longrightarrow\mathfrak d
 \longrightarrow\mathscr C^*=(\phi,h,f^*,\eta^*)
 \longrightarrow\text{arbitrary kernel and displays}
 \longrightarrow B,\rho,\mathcal T_u,\mathfrak t_\phi,\mathfrak G_\phi
 \longrightarrow\text{arbitrary attained ray certificate}.
\]

For the full conditional assembly, omit the coherence parameters. In
particular, \(\phi\) is fixed before tails are observed; the ray certificate
is arbitrary among attained minimizers, with \(c\) omitted at \(\Lambda=0\);
and no favorable tie is used. Coherence-set equality belongs to the coherent
class, \(\mathfrak G_\phi=0\) belongs to POTI-0, and
\(\mathcal D_{\rm POTI}=0\) belongs to the routine close.

Every calculation above uses signed coefficients and clone-invariant
full-fiber quantities. There is no \(1/t^*\), witness averaging, synthetic-row
vertexization, certificate reselection, B5/\(\eta_D^*\) substitution, or
second foldback. No numerical fact from W55/W57/W58/W66 or the W69
growing-rank decider enters. The dead routes in `context/FINDINGS.md` are not
used.

There is therefore no mathematical defect in COV, POTI-R, TC, or the stated
conditional assembly. The only potentially misleading abbreviated line is
the TC prose \(D_0\tau\le\alpha\lambda/16\); equation (3.4) supplies the
necessary multiplication by \(\tau\) and proves the actual bound on
\(D_0\delta\). POTI-0 and POTI\(+\) themselves remain completely unproved.
