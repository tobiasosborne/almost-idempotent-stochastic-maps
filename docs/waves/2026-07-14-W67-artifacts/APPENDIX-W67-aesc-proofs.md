# Appendix: standalone proofs for the W67 A-esc routine batch

> **Status.** Every W67 node proved below remains proposed / `conjecture`.
> Nothing in this appendix is promoted. All vectors and measures are in the
> exact signed picture, and all carrier and receiver sets are unions of full
> row-point fibers.

Throughout, the notation and quantifier order are those pinned in
`context/DECOMPOSITION-W63-I.md` §§0--1.1,
`context/DCAP-ATTACK-W65.md` §1.1, and `AESC-ATTACK.md` §1.1. In particular,

\[
 \delta=\delta(P)>0,\qquad \tau=\sqrt\delta,\qquad
 D_0=2+4\delta,\qquad e_\delta=2\delta(1+\delta),
\]
\[
 c_m={1\over4},\qquad b={c_m\over128}={1\over512},\qquad
 \delta_{\rm rt}=\min\left\{2^{-16},(c_m/4)^2,(c_mb/120)^2\right\}.
\]
For an A-esc carrier \(u\),

\[
 D_u=\widetilde q_u-p_u,\qquad a_u=\widetilde A_u,\qquad
 x_u=p_u-a_uD_u=p_u+k_{T,u}-k_{O,u},
\]
\[
 h_u=\operatorname{dist}_1(x_u,K(P)),\qquad
 \chi_u(x)={\operatorname{sgn}(D_u)\mathbin\cdot(x-p_u)\over\|D_u\|_1},
\]
and

\[
 {\tau\over2}\le\|D_u\|_1\le2\tau,\qquad a_u\ge4,\qquad
 a_uD_u=k_{O,u}-k_{T,u}.
\tag{A.1}
\]
On a full row-point fiber \(Q\), write

\[
 c_{u,Q}=\sum_{j\in Q}P_{uj},\qquad
 d_{u,Q}=\sum_{j\in Q}(\widetilde q_{u,j}-P_{uj}),
\]
and

\[
 \operatorname{Tail}_1(u)
 =\sum_{Q:\,|\chi_u(p_Q)|>1}(c_{u,Q})_+.
\tag{A.2}
\]
Here \(y_+=\max(y,0)\), and \(P_i^+(\mathcal F)\) always means positive
coefficient mass *before* aggregation inside each receiver fiber.

## 1. SF — synthetic-finance tail amplification

### Pinned contract (verbatim)

**(a) Pinned contract — `conj-w67-aesc-synthetic-finance-tail-amplification`.** For every carrier
with (1.4), if

\[
 \operatorname{dist}_1(p_u-a_uD_u,K(P))\le3\delta,
\]

then

\[
 \operatorname{Tail}_1(u)>\tau/8. \tag{SF}
\]

### Registry shards consumed and hypothesis audit

1. **`lem-dcap-five-way-completion-split`**, only for its normalized-carrier
   interface, not for its tail conclusion. Its hypothesis blocks match the
   pinned A-esc/D-cap datum as follows.

   - Its parameter block \(c_m\in(0,1)\),
     \(b=c_m/128\), the displayed \(\delta_{\rm rt}\), and
     \(D_0=2+4\delta(P)\) is exactly the adopted block above, with
     \(c_m=1/4\).
   - Its I-base block requires a finite exact signed idempotent, \(0<\delta\le
     1/4\), nonempty visible set, hidden top \(v\) with \(H>16\tau\), the
     prescribed far/deep selected set, its full-fiber mass \(S\ge c_m\), and
     the pinned restriction \(\omega\). These are all part of the complete
     pinned D-cap antecedent fixed in the paragraph preceding
     `AESC-ATTACK.md` (1.3); equation (1.3) adds the A-esc priority mass.
   - Its local shallow/exterior inequalities for every
     \(c\in K(P)\) with \(\|c-p_v\|_1\le1/4\), namely
     \[
       P_v^+\{Q\in\mathrm{Sh}_v:\|p_Q-c\|_1>1/2\}<\tau S/16,\qquad
       P_v^+\{Q\in G_v:\|p_Q-c\|_1>1/2\}\ge\tau S/16,
     \]
     and the coarse strict bounds
     \(\|r_\omega-p_v\|_1<1/8\), \(\Omega(\omega)<1/16\), are likewise the
     inherited I-base hypotheses.
   - Its ultra/rim block requires \(\delta\le\delta_{\rm rt}\),
     \(\|r_\omega-p_v\|_1<b\tau\), \(\Omega(\omega)<b\tau\), and
     \(\theta<\tau/D_0\); these are exactly the pinned D-cap branch.
   - Its certificate block requires the already exhibited, unreplaced
     \(\mathscr C^*\) with \(M_X\le1/8\), \(M_I<1/16\), and \(M_D>1/16\),
     followed by arbitrary reduced displays fixed before classification.
     This is precisely the D-cap quantifier order.
   - Finally, an A-esc carrier satisfies the shard's carrier block
     \(g_u\ge\tau\), \(A_u\ge4\), and \(\ell_u\ge\tau/2\). The output clauses
     used here are only
     \(\widetilde q_u\in K(P)\), (A.1), and the displayed definition of
     \(\chi_u\). We do **not** use its conclusion about
     \(\operatorname{Tail}_1\), and we do not invoke
     `lem-hx-robust-scalar-starvation`.

2. **`lem-hx-transverse-moment-identity`.** Its complete hypothesis block is
   checked directly: \(P\) is a finite exact signed idempotent;
   \(q_0=p_u\in K(P)\); \(q_1=\widetilde q_u\in K(P)\);
   \(q_0\ne q_1\) because \(\|D_u\|_1\ge\tau/2>0\); and the affine function
   \(\chi_u\) satisfies
   \(\chi_u(p_u)=0\) and
   \(\chi_u(\widetilde q_u)=\operatorname{sgn}(D_u)\cdot D_u/\|D_u\|_1=1\).
   Its fiber difference is exactly \(d_{u,Q}\). Thus the shard applies with
   the carrier and normer actually present here; it assumes neither an actual
   finance row nor an I-cap class. Its literal contract requires only these
   two endpoint values from the affine normer; it imposes no extra carrier or
   Lipschitz hypothesis.

No `lem-icap-*` shard, no starvation conclusion, and no transition
interpretation of a conic coefficient is consumed.

### Proof

Fix such a carrier \(u\), and abbreviate
\(D=D_u\), \(a=a_u\), \(\chi=\chi_u\), and
\(C=\operatorname{Tail}_1(u)\).

**The synthetic row, uniformly over every nearest point.** The row hull
\(K(P)=\operatorname{conv}\{p_1,\ldots,p_n\}\) is the convex hull of finitely
many points, hence compact. The continuous map
\(s\mapsto\|s-x_u\|_1\) therefore attains its minimum. Let \(r\) be an
*arbitrary* minimizer. Every minimizer has

\[
 \|r-x_u\|_1=h_u\le3\delta. \tag{A.3}
\]

Write \(r=\sum_i\lambda_i p_i\), where \(\lambda_i\ge0\) and
\(\sum_i\lambda_i=1\). Exact idempotence gives
\(p_iP=p_i\), because \(p_iP\) is row \(i\) of \(P^2=P\). Consequently

\[
 rP=\sum_i\lambda_i p_iP=r,\qquad
 r\mathbf1=\sum_i\lambda_i=1. \tag{A.4}
\]

The negative-part norm \(\nu(y)=\sum_j(-y_j)_+\) is convex, so

\[
 \nu(r)\le\sum_i\lambda_i\nu(p_i)\le\delta. \tag{A.5}
\]

The same facts hold for \(\widetilde q_u\in K(P)\), in particular
\(\nu(\widetilde q_u)\le\delta\). No vertex representation of \(r\) will be
used as transition mass.

Set

\[
 e_u:=r-x_u=r-p_u+aD.
\]

Then (A.3) gives \(\|e_u\|_1\le3\delta\). Aggregating this exact vector
identity over a full fiber \(Q\) gives

\[
 r_Q-c_{u,Q}+a\,d_{u,Q}=e_{u,Q}. \tag{A.6}
\]

This also confirms the sign: \(x_u=p_u-aD\), so \(r-x_u=r-p_u+aD\).

We record the aggregation inequalities entrywise. For every vector \(y\),

\[
 \left|\sum_{j\in Q}y_j\right|\le\sum_{j\in Q}|y_j|,\qquad
 \left(-\sum_{j\in Q}y_j\right)_+
 \le\sum_{j\in Q}(-y_j)_+.
\]

Because the fibers partition the coordinates, summing these inequalities gives

\[
 \sum_Q|e_{u,Q}|\le\|e_u\|_1\le3\delta,\quad
 \sum_Q(-r_Q)_+\le\nu(r)\le\delta,\quad
 \sum_Q(-\widetilde q_{u,Q})_+\le\nu(\widetilde q_u)\le\delta,
\tag{A.7}
\]
and

\[
 \sum_Q|d_{u,Q}|\le\|D\|_1\le2\tau. \tag{A.8}
\]

Thus fiber aggregation increases neither an \(\ell^1\) budget nor a
negative-part budget.

**Unit moment and global lever.** The audited transverse-moment shard gives

\[
 1=\sum_Qd_{u,Q}\chi(p_Q). \tag{A.9}
\]

For actual rows \(p_i,p_j\), mass one and negative mass at most \(\delta\)
give \(\|p_i\|_1=1+2\nu(p_i)\le1+2\delta\), and hence

\[
 \|p_i-p_j\|_1\le2+4\delta=D_0.
\]

This applies to the row points \(p_Q,p_u\). Since
\(\|D\|_1\ge\tau/2\),

\[
 |\chi(p_Q)|
 \le{\|p_Q-p_u\|_1\over\|D\|_1}
 \le{D_0\over\tau/2}
 ={4+8\delta\over\tau}
 \le{6\over\tau}. \tag{A.10}
\]

The last inequality is equivalent to \(\delta\le1/4\), which follows from
\(\delta\le\delta_{\rm rt}\le2^{-16}\). Thus the claimed \(6/\tau\) lever
is valid, with room to spare.

**Sign split.** On the core \(|\chi(p_Q)|\le1\), discard negative summands
from (A.9) and use (A.8):

\[
 \sum_{|\chi|\le1}\bigl(d_{u,Q}\chi(p_Q)\bigr)_+
 \le\sum_{|\chi|\le1}|d_{u,Q}|
 \le2\tau. \tag{A.11}
\]

On the negative tail \(\chi(p_Q)<-1\), a positive moment summand requires
\(d_{u,Q}<0\). Since \(d_{u,Q}=\widetilde q_{u,Q}-c_{u,Q}\),

\[
 (-d_{u,Q})_+=(c_{u,Q}-\widetilde q_{u,Q})_+
 \le(c_{u,Q})_++(-\widetilde q_{u,Q})_+.
\]

The first term, summed over this tail subset, is at most \(C\), while (A.7)
bounds the second by \(\delta\). Hence the negative-tail coefficient is

\[
 \sum_{\chi<-1}(-d_{u,Q})_+\le C+\delta. \tag{A.12}
\]

On the positive tail \(\chi(p_Q)>1\), a positive moment summand requires
\(d_{u,Q}>0\). From (A.6),

\[
 a(d_{u,Q})_+
 =(c_{u,Q}-r_Q+e_{u,Q})_+
 \le(c_{u,Q})_++(-r_Q)_++|e_{u,Q}|.
\]

After summing and using (A.7), \(a\ge4\), and the definition of \(C\),

\[
 \sum_{\chi>1}(d_{u,Q})_+
 \le{C+\delta+3\delta\over a}
 \le {C\over4}+\delta. \tag{A.13}
\]

This verifies both the aggregation of the error and the claimed positive-tail
coefficient.

Combining (A.9)--(A.13), using the lever only on the two tail sets, gives

\[
\begin{aligned}
 1
 &\le2\tau+{6\over\tau}
       \left[(C+\delta)+\left({C\over4}+\delta\right)\right]\\
 &=2\tau+{6\over\tau}\left({5C\over4}+2\delta\right)\\
 &=2\tau+{15C\over2\tau}+12{\delta\over\tau}\\
 &=14\tau+{15C\over2\tau},
\end{aligned} \tag{A.14}
\]

because \(\delta=\tau^2\). Rearrangement yields

\[
 C\ge{2\tau\over15}(1-14\tau). \tag{A.15}
\]

Finally \(\delta\le2^{-16}\) gives \(\tau\le1/256\), so

\[
 1-14\tau\ge1-{14\over256}={242\over256}={121\over128},
\]
and therefore

\[
 C\ge{2\tau\over15}{121\over128}
 ={121\over960}\tau
 >{120\over960}\tau={\tau\over8}. \tag{A.16}
\]

The proof used \(r\) only through (A.3)--(A.7), properties shared by every
nearest point. There was no favorable tie, actual finance row, \(1/t^*\), or
carrier-dependent foldback. This proves the proposed contract.

## 2. SF-K — fixed-\(K\) synthetic-finance fallback

### Minimal single-conclusion contract

**`conj-w67-aesc-synthetic-finance-tail-amplification-fixed-K`.** For every
fixed \(K\ge3\) and every carrier with (1.4), if

\[
 \operatorname{dist}_1(p_u-a_uD_u,K(P))\le K\delta
 \quad\hbox{and}\quad \tau\le{1\over3K+19},
\]

then

\[
 \operatorname{Tail}_1(u)\ge\tau/15. \tag{SF-K}
\]

This is one scalar conclusion; the quantitative estimate (1.15) is proved
inside the proof rather than appended as a second conclusion.

### Registry shards consumed and hypothesis audit

1. **`lem-dcap-five-way-completion-split`**, only for the normalized-carrier
   clauses. Its parameter hypotheses \(c_m\in(0,1)\), \(b=c_m/128\),
   \(\delta_{\rm rt}\), and \(D_0=2+4\delta(P)\) are the pinned ones. Its
   I-base hypotheses (finite exact signed idempotent, \(0<\delta\le1/4\),
   nonempty visible set, hidden top with \(H>16\tau\), prescribed far/deep
   selected mass \(S\ge c_m\), and the fixed \(\omega\)) are inherited by the
   complete D-cap antecedent. The two inherited local clauses are, for every
   permitted \(c\),
   \[
     P_v^+\{Q\in\mathrm{Sh}_v:\|p_Q-c\|_1>1/2\}<\tau S/16,\qquad
     P_v^+\{Q\in G_v:\|p_Q-c\|_1>1/2\}\ge\tau S/16;
   \]
   the strict coarse drift/width bounds are inherited as well. Its refined block
   \(\delta\le\delta_{\rm rt}\),
   \(\|r_\omega-p_v\|_1<b\tau\), \(\Omega(\omega)<b\tau\), and
   \(\theta<\tau/D_0\) is exactly the pinned ultra/rim branch. Its certificate
   is the unreplaced \(\mathscr C^*\) with \(M_X\le1/8\), \(M_I<1/16\), and
   \(M_D>1/16\), and all reduced displays were fixed before classification.
   Finally the A-esc carrier has \(g_u\ge\tau\), \(A_u\ge4\), and
   \(\ell_u\ge\tau/2\). Thus the clauses
   \(\widetilde q_u\in K(P)\), (A.1), and the definition of \(\chi_u\) apply.
   Its tail conclusion is not used.

2. **`lem-hx-transverse-moment-identity`.** Here \(P\) is the required finite
   exact signed idempotent; \(q_0=p_u\) and
   \(q_1=\widetilde q_u\) lie in \(K(P)\); they are distinct because
   \(\|D_u\|_1\ge\tau/2>0\); and the affine \(\chi_u\) has endpoint values
   \(0\) and \(1\). Its fiber difference is exactly \(d_{u,Q}\), and the
   shard's contract has no further normer hypothesis.

No conclusion of `lem-hx-robust-scalar-starvation` is cited, and no
`lem-icap-*` shard is used.

### Proof

Fix \(K\ge3\) and a carrier satisfying the antecedent. Compactness gives an
arbitrary nearest \(r\in K(P)\). With

\[
 e_u=r-(p_u-a_uD_u)=r-p_u+a_uD_u,
\]

every nearest point satisfies \(\|e_u\|_1=h_u\le K\delta\), and the exact
fiber identity remains

\[
 r_Q-c_{u,Q}+a_ud_{u,Q}=e_{u,Q}. \tag{A.17}
\]

Convexity and exact idempotence give
\(rP=r\), \(r\mathbf1=1\), \(\nu(r)\le\delta\), and also
\(\nu(\widetilde q_u)\le\delta\). Entrywise aggregation gives

\[
 \sum_Q|e_{u,Q}|\le K\delta,\quad
 \sum_Q(-r_Q)_+\le\delta,\quad
 \sum_Q(-\widetilde q_{u,Q})_+\le\delta,\quad
 \sum_Q|d_{u,Q}|\le2\tau. \tag{A.18}
\]

The transverse-moment identity gives
\(1=\sum_Qd_{u,Q}\chi_u(p_Q)\), and the same row-diameter calculation gives
\(|\chi_u(p_Q)|\le6/\tau\). Put
\(C=\operatorname{Tail}_1(u)\). The core coefficient is at most \(2\tau\),
the negative-tail coefficient is at most \(C+\delta\), and (A.17)--(A.18)
give the positive-tail coefficient

\[
 \sum_{\chi_u>1}(d_{u,Q})_+
 \le{C+\delta+K\delta\over a_u}
 \le {C\over4}+{K+1\over4}\delta. \tag{A.19}
\]

Consequently

\[
\begin{aligned}
1
&\le2\tau+{6\over\tau}
 \left(C+\delta+{C\over4}+{K+1\over4}\delta\right)\\
&=2\tau+{15C\over2\tau}
  +{6\over\tau}{K+5\over4}\delta\\
&=\left(2+{3(K+5)\over2}\right)\tau+{15C\over2\tau}\\
&={3K+19\over2}\tau+{15C\over2\tau}.
\end{aligned} \tag{A.20}
\]

Thus the full fixed-\(K\) estimate is exactly

\[
 C\ge{2\tau\over15}
 \left(1-{3K+19\over2}\tau\right). \tag{A.21}
\]

Under the contract's ceiling \(\tau\le1/(3K+19)\),

\[
 1-{3K+19\over2}\tau\ge1-{1\over2}={1\over2},
\]

and (A.21) gives \(C\ge\tau/15\). Equality in the ceiling is allowed and
produces the non-strict tail floor claimed. The equivalent defect ceiling is
\(\delta\le(3K+19)^{-2}\). The argument is again uniform over all nearest
points and uses no actual finance row.

## 3. HS — guarded hull split

### Pinned contract (verbatim)

**(a) Pinned contract — `conj-w67-aesc-guarded-hull-split`.** Under (1.3),

\[
 \eta_D^*(\mathsf H_{\rm out})<1/160
 \quad\Longrightarrow\quad
 \eta_D^*(\mathsf D_{\rm tail})>1/160. \tag{HS}
\]

### Registry shards consumed and hypothesis audit

No registry shard is consumed. The proof uses only the pinned mass hypothesis
\(\eta_D^*(\mathsf A_{\rm esc})\ge1/80\), the two definitions in (0.4), and
finite additivity of the nonnegative full-fiber measure \(\eta_D^*\). Thus
there is no I-cap hypothesis to check or import.

### Proof

The target point has the signed form

\[
 x_u=p_u-a_uD_u,
\]

because \(a_uD_u=k_{O,u}-k_{T,u}\). Accordingly the two declared classes are

\[
 \mathsf H_{\rm out}
 =\mathsf A_{\rm esc}\cap\{h_u>3\delta\},\qquad
 \mathsf D_{\rm tail}
 =\mathsf A_{\rm esc}\cap\{h_u\le3\delta\}.
\]

The scalar alternatives \(h_u>3\delta\) and \(h_u\le3\delta\) are disjoint
and exhaustive. In particular, the boundary \(h_u=3\delta\) belongs to
\(\mathsf D_{\rm tail}\). Hence they form a disjoint full-fiber partition of
\(\mathsf A_{\rm esc}\), and

\[
\begin{aligned}
 \eta_D^*(\mathsf D_{\rm tail})
 &=\eta_D^*(\mathsf A_{\rm esc})
   -\eta_D^*(\mathsf H_{\rm out})\\
 &\ge {1\over80}-\eta_D^*(\mathsf H_{\rm out})\\
 &>{1\over80}-{1\over160}
 ={2\over160}-{1\over160}
 ={1\over160}.
\end{aligned}
\]

The strict conclusion comes from the strict failure guard. If instead
\(\eta_D^*(\mathsf H_{\rm out})=1/160\), that guard does not fire: mass equality
belongs to HES, exactly as declared. This proves the proposed contract.

## 4. TU — one common tail-union foldback

For a clone-invariant population \(B\subseteq\mathsf D_{\rm tail}\), recall

\[
 \mathcal U_B=\left\{R:\exists u\in B\text{ with }c_{u,R}>0
                \text{ and }|\chi_u(p_R)|>1\right\}.
\tag{A.22}
\]

### Pinned contract (verbatim)

**(a) Pinned contract — `conj-w67-aesc-common-tail-union`.** If
\(\eta_D^*(B)>1/160\), every carrier in \(B\) has \(h_u\le3\delta\), and SF
holds, then

\[
 P_{f^*}^+(\mathcal U_B)>\tau/2560. \tag{TU}
\]

### Registry shards consumed and hypothesis audit

1. **`lem-dcap-root-closure`**, only for
   \(\eta_D^*\le P_{f^*}^+\) as full-fiber measures. Its antecedent is checked
   block by block against the pinned D-cap datum:

   - \(c_m\in(0,1)\), \(b=c_m/128\), \(\delta_{\rm rt}\), and \(D_0\) are the
     adopted parameters.
   - The finite exact signed idempotent, \(0<\delta\le1/4\), nonempty visible
     set, hidden tall top, far/deep selected set \(A\), full-fiber submeasure
     \(m\) of mass \(S\ge c_m\), and the prescribed \(\omega\) are the inherited
     I-base block.
   - For every \(c\in K(P)\) with \(\|c-p_v\|_1\le1/4\), the two inherited
     clauses are
     \[
       P_v^+\{Q\in\mathrm{Sh}_v:\|p_Q-c\|_1>1/2\}<\tau S/16,\qquad
       P_v^+\{Q\in G_v:\|p_Q-c\|_1>1/2\}\ge\tau S/16.
     \]
     Together with \(\|r_\omega-p_v\|_1<1/8\) and
     \(\Omega(\omega)<1/16\), these are the strict I-parent block.
   - \(\delta\le\delta_{\rm rt}\),
     \(\|r_\omega-p_v\|_1<b\tau\), \(\Omega(\omega)<b\tau\), and
     \(\theta<\tau/D_0\) are exactly the ultra/rim D-cap block.
   - The exhibited selected-corner certificate is the same fixed
     \(\mathscr C^*\) and has \(M_X\le1/8\), \(M_I<1/16\), \(M_D>1/16\).
     The arbitrary reduced displays required later in the shard were fixed in
     the prescribed order. Therefore its submeasure conclusion applies to
     this very \(\eta_D^*\) and \(f^*\); neither is replaced.

2. **`lem-l5-positive-flow-foldback`**, invoked exactly once below. Its own
   hypotheses are checked at the point of use: \(P\) is finite exact signed
   idempotent; its row index is \(v=f^*\); its nonnegative full-fiber
   submeasure is \(m=\eta_D^*|_B\); the pointwise domination
   \(m_Q\le P_{f^*}^+(Q)\) follows from the preceding shard; and its single
   test is \(g=\mathbf1_{\mathcal U_B}\in[0,1]\), so \(M=1\).

The pointwise SF inequality is an explicit antecedent of TU and was proved as
the preceding proposed node; it is not a registry shard. No I-cap shard, B5
overlay identification, pairwise family of tests, or second foldback is used.

### Proof

Fix \(u\in B\). For each receiver fiber \(R\), the elementary inequality

\[
 \left(\sum_{j\in R}P_{uj}\right)_+
 \le\sum_{j\in R}(P_{uj})_+ \tag{A.23}
\]

has the crucial direction: positive part *after* aggregation is bounded by
positive coefficient mass *before* aggregation. In the tail sum, a fiber
with \(c_{u,R}\le0\) contributes zero. Every fiber with
\(c_{u,R}>0\) and \(|\chi_u(p_R)|>1\) belongs to the common union
\(\mathcal U_B\), with this \(u\) itself as witness. Therefore

\[
\begin{aligned}
 \operatorname{Tail}_1(u)
 &=\sum_{R:\,|\chi_u(p_R)|>1}(c_{u,R})_+\\
 &\le\sum_{R\in\mathcal U_B}(c_{u,R})_+\\
 &\le\sum_{R\in\mathcal U_B}\sum_{j\in R}(P_{uj})_+
 =P_u^+(\mathcal U_B).
\end{aligned} \tag{A.24}
\]

By the SF antecedent, this proves, for every \(u\in B\),

\[
 P_u^+(\mathcal U_B)\ge\operatorname{Tail}_1(u)>\tau/8. \tag{A.25}
\]

Now let \(m=\eta_D^*|_B\). Because \(B\) is a union of full carrier fibers,
\(m\) is a nonnegative full-fiber measure, and restriction preserves the R0
domination:

\[
 0\le m_Q\le\eta_D^*(Q)\le P_{f^*}^+(Q).
\]

Apply `lem-l5-positive-flow-foldback` **once**, at \(f^*\), to the one common
test \(g=\mathbf1_{\mathcal U_B}\). Its left side is exactly the
\(\eta_D^*|_B\)-average of the positive one-step outflow to that common set.
Thus

\[
 \int_B P_u^+(\mathcal U_B)\,d\eta_D^*(u)
 \le P_{f^*}^+(\mathcal U_B)+e_\delta,
\]

or

\[
 P_{f^*}^+(\mathcal U_B)
 \ge\int_B P_u^+(\mathcal U_B)\,d\eta_D^*(u)-e_\delta.
\tag{A.26}
\]

Using (A.25) and \(\eta_D^*(B)>1/160\),

\[
 \int_B P_u^+(\mathcal U_B)\,d\eta_D^*(u)
 >{\tau\over8}\eta_D^*(B)
 >{\tau\over8}{1\over160}
 ={\tau\over1280}. \tag{A.27}
\]

The strict first inequality in (A.27) is legitimate because the carrier
fiber space is finite: the positive function
\(P_u^+(\mathcal U_B)-\tau/8\) is integrated over a set of positive
\(\eta_D^*\)-mass.

It remains to check the ceiling independently. At the pinned value
\(c_m=1/4\),

\[
 b={1\over512},\qquad
 {c_mb\over120}={1\over4\cdot512\cdot120}={1\over245760}
 ={c_m^2\over15360}.
\]

The square roots of the three components of \(\delta_{\rm rt}\) are,
respectively,

\[
 {1\over256},\qquad {c_m\over4}={1\over16},\qquad
 {c_mb\over120}={1\over245760}.
\]

Hence the third component is the minimum and the true ceiling is

\[
 \delta_{\rm rt}=\left({1\over245760}\right)^2,\qquad
 \tau\le{1\over245760}< {1\over15360}. \tag{A.28}
\]

Thus the strategist's formula
\(\tau\le c_m^2/15360<1/15360\) is correct; at \(c_m=1/4\) it is the sharper
number \(1/245760\), not \(1/15360\). Since \(\delta=\tau^2\),

\[
 {e_\delta\over\tau}
 ={2\tau^2(1+\tau^2)\over\tau}
 =2\tau(1+\tau^2)
 <4\tau
 <{4\over15360}={1\over3840}. \tag{A.29}
\]

Combining (A.26)--(A.29) gives

\[
\begin{aligned}
 P_{f^*}^+(\mathcal U_B)
 &>{\tau\over1280}-e_\delta\\
 &>{\tau\over1280}-{\tau\over3840}
 ={3\tau-\tau\over3840}
 ={\tau\over1920}
 >{\tau\over2560}.
\end{aligned}
\]

This is one common-set demand and one foldback. The direction in (A.23), the
restriction submeasure hypothesis, and the exact numeric close are all in the
required direction. This proves the proposed contract.

## 5. SEP — separation geography

### Minimal single-conclusion contract

**`conj-w67-aesc-hull-exterior-separation-geography`.** For every
\(u\in\mathsf H_{\rm out}\), there exists an affine functional \(\psi_u\),
with linear part \(\overline\psi_u\) satisfying
\(\|\overline\psi_u\|_\infty\le1\), such that

\[
 \psi_u(x_u)-\sup_{r\in K(P)}\psi_u(r)=h_u,\qquad
 -a_u\overline\psi_u(D_u)\ge h_u>3\delta. \tag{SEP}
\]

This is one existence conclusion. The notation \(\psi_u(D_u)\) in
`AESC-ATTACK.md` (1.20) means the linear part
\(\overline\psi_u(D_u)\), since an affine constant does not act on a
displacement vector.

### Registry shards consumed and hypothesis audit

No registry shard is consumed. The proof below establishes the required
finite-dimensional \(\ell^1/\ell^\infty\) separation directly from the pinned
facts that \(K(P)\) is the compact convex hull of the actual rows,
\(p_u\in K(P)\), \(x_u=p_u-a_uD_u\), \(a_u\ge4>0\), and
\(h_u>3\delta\). In particular it uses neither a preferred-normal shard nor
an I-cap hypothesis.

### Proof

Fix \(u\in\mathsf H_{\rm out}\), and put \(C=K(P)\), \(x=x_u\), and
\(h=h_u\). The set \(C\) is a nonempty compact convex subset of the
finite-dimensional coordinate space, and

\[
 h=\operatorname{dist}_1(x,C)>3\delta>0.
\]

Therefore \(x\notin C\), and the open \(\ell^1\)-ball
\(B_1(x,h)=\{y:\|y-x\|_1<h\}\) is disjoint from \(C\). Finite-dimensional
separation of the convex set \(C\) and this open convex ball supplies a
nonzero linear functional \(\ell\) such that

\[
 \sup_{r\in C}\ell(r)
 \le\inf_{y\in B_1(x,h)}\ell(y).
\tag{A.30}
\]

For the \(\ell^1/\ell^\infty\) dual pair,

\[
 \inf_{y\in B_1(x,h)}\ell(y)
 =\ell(x)-h\|\ell\|_\infty.
\]

(The infimum need not be attained because the ball is open, but its value is
the displayed dual-norm expression.) Normalize
\(L=\ell/\|\ell\|_\infty\). Then (A.30) gives

\[
 L(x)-\sup_{r\in C}L(r)\ge h. \tag{A.31}
\]

Conversely, Hölder's inequality gives, for every \(r\in C\),

\[
 L(x)-L(r)=L(x-r)\le\|L\|_\infty\|x-r\|_1=\|x-r\|_1.
\]

Taking the infimum over \(r\in C\) yields

\[
 L(x)-\sup_{r\in C}L(r)\le h. \tag{A.32}
\]

Thus equality holds in (A.31)--(A.32). Take the affine functional
\(\psi_u(y)=L(y)\) (or add any affine constant). Its linear part is \(L\),
\(\|L\|_\infty=1\le1\), and

\[
 \psi_u(x_u)-\sup_{r\in K(P)}\psi_u(r)=h_u. \tag{A.33}
\]

Since the actual row \(p_u\in K(P)\), (A.33) and
\(x_u=p_u-a_uD_u\) imply

\[
\begin{aligned}
 h_u
 &=\psi_u(x_u)-\sup_{r\in K(P)}\psi_u(r)\\
 &\le\psi_u(x_u)-\psi_u(p_u)\\
 &=L(x_u-p_u)\\
 &=-a_uL(D_u)
 =-a_u\overline\psi_u(D_u).
\end{aligned}
\]

Together with \(h_u>3\delta\), this is (SEP). The construction is
existential separately for each \(u\); it chooses no normal uniformly across
carriers, averages no separators, and treats the separator only as geography,
never as a transition.
