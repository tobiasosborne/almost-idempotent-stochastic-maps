STATUS: UNVERIFIED PROVER OUTPUT

# W74F-H — Stage-1 split packet and corrected \(K\)-ledger delta

Date: 2026-07-24  
Role: fresh prover; a separate fresh hostile verifier must attack this output  
Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`  
Checked SHA256:
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`

This artifact supplies only the packet missing from
`LEDGER-W74F-G-K.md` and the consequent bookkeeping delta. It does not
alter the \(K\) formula, PRH, H-CB, or EXT-CB.

## 0. Packet statement

Let \(\mathcal X\) be the current finite-dimensional corner algebra in
MAIN-CB Stage 1. Write \(I_{\mathcal X}\) for its declared unit and
\(\varepsilon_X\) for its extended \(C^*\)-defect. Assume
\[
  \dim\mathcal X>1,\qquad 0\leq\varepsilon_X\leq e_{\rm split}.
\tag{0.1}
\]
There are universal constants
\[
 C_{\rm split}\geq1,\qquad e_{\rm split}>0
\tag{0.2}
\]
with the following properties.

1. The construction of `lem_nontriv_projection` at `tex:915-969`
   produces Hermitian \(P',P''\in\mathcal X\), with
   \(P''=I_{\mathcal X}-P'\), such that
   \[
   \begin{gathered}
   P'+P''=I_{\mathcal X},\\
   \|(P')^2-P'\|,\ \|(P'')^2-P''\|,\
   \|P'P''\|,\ \|P''P'\|
      \leq C_{\rm split}\varepsilon_X,\\
   \bigl|\|P'\|-1\bigr|,\ 
   \bigl|\|P''\|-1\bigr|
      \leq C_{\rm split}\varepsilon_X.
   \end{gathered}
\tag{0.3}
   In particular, after the radius in (0.2) is shrunk once,
   \[
      \|P'\|,\|P''\|\geq\frac12,
   \tag{0.4}
   \]
   so both projections are nonvanishing in the sense of
   `tex:926-929`.

2. The fresh map at `tex:1423-1424`,
   \[
   v_{\rm comm}^{(2)}:\mathbb C^2\longrightarrow\mathcal X,\qquad
   v_{\rm comm}^{(2)}(\lambda,\mu)=\lambda P'+\mu P'',
   \tag{0.5}
   \]
   is an extended \(C_{\rm split}\varepsilon_X\)-inclusion. Thus its
   unit defect is \(0\), its involution defect is \(0\), and, for every
   amplification level \(n\),
   \[
   \begin{aligned}
   &\|v_n(xy)-v_n(x)v_n(y)\|_n
      \leq C_{\rm split}\varepsilon_X\|x\|\,\|y\|,\\
   &(1-C_{\rm split}\varepsilon_X)\|x\|
      \leq\|v_n(x)\|_n
      \leq(1+C_{\rm split}\varepsilon_X)\|x\|.
   \end{aligned}
\tag{0.6}
   \]

3. Suppose, as in Stage 1, that the preceding maximal commutative map
   has just been reset to an extended
   \(c_0^{\rm cb}\varepsilon_X\)-inclusion. Its old-side restriction
   and one compression,
   \[
   v_{\rm comm}^{(1)}(\Pi_j)
     =\operatorname{Co}_{P_{[1,m-1]}}(P_j),
      \qquad 1\leq j\leq m-1,
   \tag{0.7}
   \]
   is also an extended \(C_{\rm split}\varepsilon_X\)-inclusion. When
   \(m=1\), this old side is absent and there is nothing to estimate.

All constants in (0.2)-(0.7) are independent of
\(\dim\mathcal X\), \(\dim\mathcal A\), amplification level, the number
of commutative summands, all simple-block dimensions, and the stage
index.

## 1. Decomposition of the printed construction

### SPLIT-A — exact-unit rectification and the nontrivial projection

The source's phrase “without loss of generality” at `tex:934-935`
invokes Proposition `prop_unit`, `tex:672-687`. Applied to
\(\mathcal X\), it gives, on the same normed vector space and with the
same involution, a product \(\mathbin{\boldsymbol\cdot}\) and an exact
unit \(J\) satisfying
\[
 \|J-I_{\mathcal X}\|\leq C_{\rm unit}\varepsilon_X,\qquad
 \|x\mathbin{\boldsymbol\cdot}y-xy\|
   \leq C_{\rm unit}\varepsilon_X\|x\|\|y\|,
\tag{1.1}
\]
and the rectified algebra has defect at most
\(C_{\rm unit}\varepsilon_X\). Here \(C_{\rm unit}\) is universal and
the assertion is used only for
\(\varepsilon_X\leq e_{\rm unit}\), for a universal
\(e_{\rm unit}>0\).

The hidden analytic input in this step is now named. The proof of
`prop_unit` uses the quantitative inverse-function lemma
`tex:562-592` and the inverses of \(L_J,R_J\). Choose a universal
Neumann margin \(e_{\rm Neu}>0\) so that every operator called
\(1+T\) in `tex:681-686`, `710-725`, and `758-843` has
\(\|T\|\leq1/2\). This is stronger than the printed requirement
\(\|T\|<1\), and gives inverse norm at most \(2\). Choose a universal
\(e_{\rm IFT}>0\) so that every contraction constant in
`lem_invfun`, `lem_gV`, and `prop_polar` is at most \(1/2\).

In the rectified algebra, `tex:690-892` constructs the approximate
unitary manifold \(\mathcal U\), its polar retraction \(u\), and
\[
 \sigma(U)=u(U^\dagger).
\tag{1.2}
\]
The construction uses fixed-radius Banach-space balls, the Neumann
margin above, and the inverse/implicit-function theorem. Thus there
are universal \(C_{\rm U}\) and \(e_{\rm U}>0\) such that all the
polar, group-law, and derivative errors used at `tex:857-943` are at
most \(C_{\rm U}\varepsilon_X\) whenever
\(\varepsilon_X\leq e_{\rm U}\).

There is one further quantitative input compressed into
`tex:943`: a universal isolation radius. To make it explicit, choose a
fixed chart radius \(r_{\rm iso}>0\) inside the polar neighborhood.
At \(I\), equation `der_gr_inverse`, together with
\(L_I=R_I=1\), gives
\[
 D\sigma=-1+O(\varepsilon_X).
\tag{1.3}
\]
On the fixed \(r_{\rm iso}\)-ball the same source estimates give
\[
 D(\sigma-\operatorname{id})=-2+O(r_{\rm iso}+\varepsilon_X).
\tag{1.4}
\]
First choose \(r_{\rm iso}\) universally small and then choose a
universal \(e_{\rm iso}>0\) so the last error has norm at most
\(1/2\). The quantitative inverse-function lemma then makes \(I\) the
only fixed point in that ball. Multiplication by \(-1\) gives the same
statement at \(-I\). This supplies the “constant-size neighborhoods”
asserted at `tex:943`; neither radius is allowed to depend on the
dimension.

The topological part at `tex:945-968` now has no metric coefficient to
lose. The quotient \(\breve{\mathcal U}\) is a positive-dimensional
compact connected orientable \(H\)-space, and the Lefschetz-Hopf/Hopf
argument gives a fixed point other than the scalar class
\(\breve e\). Lifting that point as at `tex:945` gives a fixed point
\(U\) of \(\sigma\) outside both isolation balls.

Since \(\sigma(U)=U\), the polar estimate `tex:845-868` gives
\[
 \|U^\dagger-U\|\leq C_{\rm U}\varepsilon_X.
\tag{1.5}
\]
Set, as at `tex:939`,
\[
 P_0=\frac14(2J+U+U^\dagger).
\tag{1.6}
\]
It is Hermitian. Expanding \(P_0\mathbin{\boldsymbol\cdot}P_0-P_0\),
using \(U^\dagger\mathbin{\boldsymbol\cdot}U=J\),
\(U\mathbin{\boldsymbol\cdot}U^\dagger=J+O(\varepsilon_X)\) from
`tex:861-864`, and (1.5), gives
\[
 \|P_0\mathbin{\boldsymbol\cdot}P_0-P_0\|
   \leq C_{\rm proj}\varepsilon_X
\tag{1.7}
\]
for a universal \(C_{\rm proj}\).

The separation from \(\pm J\) makes this projection nontrivial. Indeed,
from (1.5)-(1.6),
\[
 \|U+J\|\leq2\|P_0\|+O(\varepsilon_X),\qquad
 \|U-J\|\leq2\|J-P_0\|+O(\varepsilon_X).
\tag{1.8}
\]
The isolation radius therefore excludes the small alternative in
`P_alternatives`, `tex:926-929`, for both \(P_0\) and \(J-P_0\).
The other alternative gives
\[
 \bigl|\|P_0\|-1\bigr|,
 \ \bigl|\|J-P_0\|-1\bigr|
 \leq C_{\rm nv}\varepsilon_X
\tag{1.9}
\]
for a universal \(C_{\rm nv}\).

Return to the original corner product and unit by defining
\[
 P'=P_0,\qquad P''=I_{\mathcal X}-P'.
\tag{1.10}
\]
Equations (1.1), (1.7), and
\(\|J-I_{\mathcal X}\|=O(\varepsilon_X)\) show that both original
projection defects are at most \(C_{\rm np}\varepsilon_X\).
The same comparison transfers (1.9). Finally, using the approximate
unit laws in \(\mathcal X\),
\[
 \begin{aligned}
 \|P'P''\|
 &=\|P'I_{\mathcal X}-(P')^2\|
 \leq\varepsilon_X\|P'\|+C_{\rm np}\varepsilon_X,\\
 \|P''P'\|
 &=\|I_{\mathcal X}P'-(P')^2\|
 \leq\varepsilon_X\|P'\|+C_{\rm np}\varepsilon_X.
 \end{aligned}
\tag{1.11}
\]
Here \(C_{\rm np}\) is chosen to dominate the fixed sums of
\(C_{\rm unit},C_{\rm proj},C_{\rm nv},C_{\rm U}\) occurring in
(1.7)-(1.11). After this one increase, (0.3)-(0.4) follow.

There is no additional holomorphic-functional-calculus radius hidden
in `tex:915-969`: that construction uses the inverse/implicit-function
and polar machinery just named. The sign-functional-calculus condition
\(4\delta<1\) at `tex:524-532` enters the already existing compression
packet `tex:1054-1064`; its common positive radius remains part of
COMP-CB/\(\delta_{\max}^{\rm cb}\), and is included below through
\(e_{\rm old}\).

### SPLIT-B — the fresh two-point inclusion, including all levels

Let \(q_1=P'\), \(q_2=P''\), and let \(d\) be the maximum of the four
defects in the second line of (0.3). Thus
\[
 d\leq C_{\rm np}\varepsilon_X.
\tag{1.12}
\]
For
\[
 x=(A,B),\qquad y=(C,D)
 \quad\text{in}\quad
 M_n(\mathbb C^2)=M_n\oplus M_n,
\]
the amplification of (0.5) is
\[
 v_n(A,B)=A\otimes q_1+B\otimes q_2.
\tag{1.13}
\]
The multiplicativity defect is the sum of exactly four elementary
tensors:
\[
\begin{aligned}
v_n(x)v_n(y)-v_n(xy)
={}&AC\otimes(q_1^2-q_1)+AD\otimes q_1q_2\\
 &+BC\otimes q_2q_1+BD\otimes(q_2^2-q_2).
\end{aligned}
\tag{1.14}
\]
By the isometric amplification identity at `tex:1475`,
\(\|T\otimes z\|=\|T\|\|z\|\), and by
\(\|(A,B)\|=\max\{\|A\|,\|B\|\}\),
\[
 \|v_n(x)v_n(y)-v_n(xy)\|_n
 \leq4d\,\|x\|\,\|y\|.
\tag{1.15}
\]
This is an all-level estimate. It is not an entrywise matrix sum, and
its factor \(4\) is the fixed number of products in a two-point
algebra, not an amplification or block-count factor. Involution is
preserved exactly, and
\[
 v_n(I_n,I_n)=I_n\otimes(q_1+q_2)
             =I_n\otimes I_{\mathcal X},
\tag{1.16}
\]
so the unit defect is zero at every level.

It remains to obtain the inclusion lower bound without assuming it.
If \(\max\{\|A\|,\|B\|\}=1\) and \(\|A\|=1\), right multiplication by
\(I_n\otimes q_1\), (1.12), and `tex:1475` give
\[
\begin{aligned}
\|v_n(A,B)(I_n\otimes q_1)-A\otimes q_1\|_n
 &\leq2d,\\
\|v_n(A,B)(I_n\otimes q_1)\|_n
 &\leq(1+\varepsilon_X)\|v_n(A,B)\|_n\|q_1\|.
\end{aligned}
\tag{1.17}
\]
Because \(\|q_1\|\geq1/2\), a universal shrink of the input radius gives
\(\|v_n(A,B)\|_n\geq1/4\). If \(\|B\|=1\), use \(q_2\) instead. Hence
the preliminary lower modulus \(1/4\) holds for every \(n\).

Choose \(e_{\rm pair}>0\) so that
\[
 8C_{\rm np}e_{\rm pair}<\frac14
\tag{1.18}
\]
and so that the common small-radius hypotheses of
`prop_delta_hominc`, `tex:1194-1222`, apply at every level. Applying
that proposition to (1.15) in the extended
\(\varepsilon_X\)-\(C^*\)-algebra \(M_n\otimes\mathcal X\) sharpens
the preliminary modulus and the automatic upper bound to
\[
 (1-C_{\rm pair}\varepsilon_X)\|x\|
 \leq\|v_n(x)\|_n
 \leq(1+C_{\rm pair}\varepsilon_X)\|x\|
\tag{1.19}
\]
with one universal \(C_{\rm pair}\), independent of \(n\). Equations
(1.15), (1.16), and (1.19) prove SPLIT-B.

### SPLIT-C — the old-side inclusion

The map in (0.7) must not be estimated by summing its \(m-1\) basis
images. It is the restriction of the preceding extended inclusion to
the ideal \(\mathbb C^{m-1}\), followed by the single amplified
compression
\[
 1_{M_n}\otimes\operatorname{Co}_{P_{[1,m-1]}}
 =\operatorname{Co}_{I_n\otimes P_{[1,m-1]}}.
\tag{1.20}
\]
The restriction preserves the same extended defect. The one
compression-transfer packet in COMP-CB therefore gives
\[
 \operatorname{def}_{\rm ext}(v_{\rm comm}^{(1)})
 \leq C_{\rm old}\varepsilon_X,\qquad
 C_{\rm old}:=C_{\rm co}(1+c_0^{\rm cb}),
\tag{1.21}
\]
on a universal positive input radius \(e_{\rm old}\). There is no
\(m\)-factor: (1.20) is one map at every level. This is precisely the
compression-side packet already covered by \(C_{\rm co}\); it is
listed here because `tex:1419-1425` uses both (0.7) and (0.5).

## 2. Constant ledger and independence

The packet constants may be chosen as follows:
\[
\begin{aligned}
e_{\rm np}
  &:=
  \min\left\{
   e_{\rm unit},e_{\rm Neu},e_{\rm IFT},e_{\rm U},e_{\rm iso},
   \frac1{2C_{\rm np}}
  \right\},\\
C_{\rm split}
  &:=
  \max\{1,C_{\rm np},4C_{\rm np},C_{\rm pair},C_{\rm old}\},\\
e_{\rm split}
  &:=
  \min\left\{
    e_{\rm np},e_{\rm pair},e_{\rm old},
    \frac1{2C_{\rm split}}
  \right\}.
\end{aligned}
\tag{2.1}
\]

| constant | producing inequality/input | reason for universality |
|---|---|---|
| \(C_{\rm unit},e_{\rm unit}\) | exact-unit comparison (1.1) | `prop_unit` is a fixed Banach-space estimate; `tex:458` excludes dependence on additional data |
| \(e_{\rm Neu}\) | every Neumann error is \(\leq1/2\) | fixed operator-norm margin, independent of the underlying Banach-space dimension |
| \(e_{\rm IFT}\) | every inverse/implicit-function contraction is \(\leq1/2\) | `lem_invfun` uses only operator norms on fixed-radius balls |
| \(C_{\rm U},e_{\rm U}\) | polar/group/derivative errors through (1.5) | the products and derivatives at `tex:690-892` are fixed-length estimates |
| \(r_{\rm iso},e_{\rm iso}\) | uniqueness of the fixed points in the two \(r_{\rm iso}\)-balls | (1.4) is an operator-norm estimate; the quotient dimension does not enter |
| \(C_{\rm proj}\) | rectified projection defect (1.7) | expansion of four binary products, with no dimension-indexed sum |
| \(C_{\rm nv}\) | nonvanishing norm errors (1.9) | the fixed isolation radius and the two alternatives at `tex:926-929` |
| \(C_{\rm np},e_{\rm np}\) | (0.3)-(0.4) | projection conversion and transfer use a fixed number of terms |
| \(C_{\rm pair},e_{\rm pair}\) | all-level inclusion estimate (1.19) | four elementary tensors plus the isometry at `tex:1475`; no entrywise sum |
| \(C_{\rm old},e_{\rm old}\) | old-side estimate (1.21) | one restriction and one compression map, not \(m-1\) separate estimates |
| \(C_{\rm split},e_{\rm split}\) | common packet (0.2)-(0.7) | finite maximum/minimum of the preceding universal data |

The dimension enters the topology only to ensure
\(\dim\breve{\mathcal U}>0\) and hence two nonzero cohomology groups at
`tex:945-968`; it never enters an analytic coefficient. Amplification
levels enter only through \(I_n\otimes\cdot\) and the isometry
`tex:1475`. The split has exactly two summands. Reusing the packet at
another stage changes only the current value of \(\varepsilon_X\), not
any constant.

## 3. Corrected MAIN-CB reset chain

Starting from the symbols in `LEDGER-W74F-G-K.md`, replace (1.5)'s first
three definitions by
\[
\boxed{
\begin{aligned}
C_{\rm main}&:=\max\{C_{\rm co},C_{\rm split}\},\\
L&:=C_{\rm main}(1+c_0^{\rm cb}),\\
C_{\rm pre}&:=2L^2\max\{1,C_{\rm ext},C_{\rm merge}\}.
\end{aligned}}
\tag{3.1}
\]
Keep \(C_E=c_0^{\rm cb}\), and replace the MAIN radius by
\[
\boxed{
\varepsilon_E^{\rm corr}:=
\min\left\{
\frac{\delta_{\max}^{\rm cb}}{C_{\rm pre}},
\frac{e_H}{C_{\rm pre}},
\frac{e_{\rm ext}}{C_{\rm pre}},
\frac{e_{\rm sel}}{C_{\rm pre}},
\frac{e_{\rm split}}{C_{\rm pre}}
\right\}.}
\tag{3.2}
\]

The new bookkeeping symbols have no new data dependence:

| symbol | producing expression | independence |
|---|---|---|
| \(C_{\rm main}\) | finite maximum of the compression and split coefficients | neither input depends on dimension, blocks, amplification, or stage |
| \(L\) | \(C_{\rm main}(1+c_0^{\rm cb})\) | fixed product of universal coefficients |
| \(C_{\rm pre}\) | \(2L^2\max\{1,C_{\rm ext},C_{\rm merge}\}\) | fixed maximum; it does not count calls |
| \(\varepsilon_E^{\rm corr}\) | finite minimum in (3.2) | positive minimum of universal radii divided by \(C_{\rm pre}\) |

Here is the corrected full replacement for ledger (2.2)-(2.5).
The existing corner estimate becomes
\[
 \varepsilon_X
 \leq C_{\rm co}(1+c_0^{\rm cb})\varepsilon
 \leq L\varepsilon.
\tag{3.3}
\]
For every ordinary reset/restriction/compression packet,
\[
\delta_{\rm comp}
\leq C_{\rm co}(1+c_0^{\rm cb})\varepsilon_X
\leq L\varepsilon_X
\leq L^2\varepsilon.
\tag{3.4}
\]
For the fresh Stage-1 packet, (0.2)-(0.7) and (3.3) give
\[
\delta_{\rm split}
\leq C_{\rm split}\varepsilon_X
\leq C_{\rm main}\varepsilon_X
\leq L\varepsilon_X
\leq L^2\varepsilon.
\tag{3.5}
\]
The penultimate inequality is deliberately coarse and uses
\(1+c_0^{\rm cb}\geq1\).

Thus every pre-extension/merge raw packet, including both kinds of
Stage-1 input, satisfies the corrected (2.2)
\[
\boxed{\delta_{\rm raw}\leq L^2\varepsilon.}
\tag{3.6}
\]
Together with (3.3), the corrected (2.3) is
\[
\boxed{
e_{\rm raw}:=\delta_{\rm raw}+\varepsilon_X
\leq(L^2+L)\varepsilon
\leq2L^2\varepsilon
\leq C_{\rm pre}\varepsilon.}
\tag{3.7}
\]
The corrected (2.4) is unchanged in form:
\[
\boxed{
\begin{aligned}
\delta_{\rm ext,out}
 &\leq C_{\rm ext}e_{\rm raw}
 \leq C_{\rm pre}\varepsilon,\\
\delta_{\rm merge,out}
 &\leq C_{\rm merge}e_{\rm raw}
 \leq C_{\rm pre}\varepsilon.
\end{aligned}}
\tag{3.8}
\]
Finally, \(\varepsilon\leq\varepsilon_E^{\rm corr}\) gives the corrected
(2.5):
\[
\boxed{
C_{\rm pre}\varepsilon
\leq
\delta_{\max}^{\rm cb},\ e_H,\ e_{\rm ext},\ e_{\rm sel},\
e_{\rm split}.}
\tag{3.9}
\]
In particular,
\[
\varepsilon_X\leq L\varepsilon
\leq C_{\rm pre}\varepsilon
\leq e_{\rm split},
\tag{3.10}
\]
so invoking the new packet is noncircular. Stage 1 is a fixed
two-way split followed by a binary merge; Stage 2 has one compression,
one extension, and an immediate reset; every Stage-3 binary merge is
immediately reset. Equations (3.4)-(3.8) therefore acquire neither a
step-count nor a block-count factor.

## 4. Corrected \(\eta_K\) delta

The MAIN contribution becomes
\[
\frac{\varepsilon_E^{\rm corr}}{C_A}
=\min\left\{
\frac{\delta_{\max}^{\rm cb}}{C_{\rm pre}C_A},
\frac{e_H}{C_{\rm pre}C_A},
\frac{e_{\rm ext}}{C_{\rm pre}C_A},
\frac{e_{\rm sel}}{C_{\rm pre}C_A},
\boxed{\frac{e_{\rm split}}{C_{\rm pre}C_A}}
\right\}.
\tag{4.1}
\]
Accordingly, replace ledger (4.2) by
\[
\boxed{
\begin{aligned}
\eta_K^{\rm corr}:=\min\biggl\{&
\frac18,\ \eta_A,\
\frac{\delta_{\max}^{\rm cb}}{C_{\rm pre}C_A},\
\frac{e_H}{C_{\rm pre}C_A},\
\frac{e_{\rm ext}}{C_{\rm pre}C_A},\
\frac{e_{\rm sel}}{C_{\rm pre}C_A},\
\frac{e_{\rm split}}{C_{\rm pre}C_A},\\
&\frac1{4C_\theta},\
\frac1{4C_EC_A},\
\frac1{2(C_T+C_{\Delta'})},\
\frac1{4(1+C_2+C_3+C_{\Upsilon'})},\
\frac1{2(C_T+C_{\Upsilon'})},\\
&\frac1{24K},\ 1
\biggr\}.
\end{aligned}}
\tag{4.2}
\]
The new term implies
\[
C_{\rm pre}C_A\eta\leq e_{\rm split},
\tag{4.3}
\]
which is exactly (3.10) after
\(\varepsilon=\varepsilon_{\rm AI}(\eta)\leq C_A\eta\).
Every entry remains positive and dimension-free.

## 5. Unchanged \(K\) and finish

The Stage-1 repair changes only the admissible MAIN-CB radius. It does
not change a factor-map coefficient. Thus ledger (3.3) remains
\[
K=\max\left\{
1,\,
C_\theta+C_\Delta+2C_\Upsilon,\,
C_\Upsilon+2(C_2+C_\theta+C_\Delta),\,
C_\Upsilon+2C_\Delta
\right\}.
\tag{5.1}
\]
No recalculation of its three telescopes is made here; the preceding
hostile verdict marked them valid.

Likewise the finish is unchanged: with
\(\eta\leq\eta_K^{\rm corr}\), ledger (5.1)-(5.2) still yields
\[
\|Q-E\|_{\infty\to\infty}
\leq(K+4\sqrt{2K})\sqrt\eta.
\tag{5.2}
\]
Nothing in this artifact changes PRH or its threshold.

## 6. Hypothesis hygiene

1. The nontrivial-projection construction requires finite dimension
   and \(\dim\mathcal X>1\). Finite dimension is used for compactness,
   finite triangulation, and top-degree cohomology; it is not used in
   a coefficient.
2. Extended structure is not needed to find \(P'\) at level one. It is
   needed to interpret every \(I_n\otimes P'\) and (0.5) at all levels.
   Their bounds follow from `tex:1475` and the extended
   \(\varepsilon_X\)-\(C^*\) axioms, not from entrywise estimates.
3. Exact unitality is not assumed of the incoming corner. It is
   introduced by `prop_unit` and then transferred back by (1.1) and
   (1.10).
4. The old-side map (0.7) additionally assumes the preceding
   commutative inclusion has been reset. That is the MAIN-CB induction
   invariant, not a conclusion of `lem_nontriv_projection`.
5. The new guard is consumed before the Stage-1 construction:
   (3.10) proves \(\varepsilon_X\leq e_{\rm split}\). It is not inferred
   from the output of the construction.
6. The functional-calculus radius for the compression maps remains in
   COMP-CB/\(\delta_{\max}^{\rm cb}\). The genuinely new hidden radii
   are \(e_{\rm unit},e_{\rm Neu},e_{\rm IFT},e_{\rm U},e_{\rm iso}\),
   assembled into \(e_{\rm split}\).
7. The \(O(\varepsilon_X)\) coefficients are symbolic because the
   source does not print their numerical values. Their independence
   follows from the source convention at `tex:458`; no decimal value
   is inferred.

## 7. Required honesty sentences

The two closure sentences are, exactly:

> The factor-map and finish ledgers are closed relative to MAIN-CB, H-CB, and EXT-CB; MAIN-CB is closed relative to the Stage-1 packet supplied here only if that packet survives separate fresh hostile verification.

> No mathematical gap is knowingly left inside this relative ledger conditional on separate fresh hostile verification of the Stage-1 packet supplied here; external hostile verification of this artifact and eventual L0 closure remain.

## 8. LOUD DEFECT REGISTER

1. **UNVERIFIED AUTHOR OUTPUT.** This artifact is neither a verifier
   verdict nor an L0 certificate. It must not be called verified,
   validated, formalized, or rigorous.
2. **THE SOURCE CONSTANTS ARE NOT NUMERICAL.** The paper asserts
   concrete data-independent big-\(O\) functions at `tex:458`, but does
   not print \(C_{\rm unit},C_{\rm U},C_{\rm proj},C_{\rm nv}\), or
   their radii. This packet names finite maxima/minima; it does not
   manufacture values.
3. **THE UNIFORM ISOLATION SENTENCE IS LOAD-BEARING.** The step from
   `der_gr_inverse` to a dimension-free \(r_{\rm iso}\) is expanded in
   (1.3)-(1.4), but the printed paper compresses it into one sentence
   at `tex:943`. A hostile reader should attack the chart-radius
   uniformity and the passage to the quotient first.
4. **THE TOPOLOGICAL THEOREMS ARE USED AS PRINTED.** Lefschetz-Hopf,
   Hopf's structure theorem, orientability, and the finite-CW claim are
   not reconstructed from foundations here. The quantitative claim is
   only that they introduce no analytic coefficient.
5. **EXACT-UNIT TRANSFER IS LOAD-BEARING.** The projection is first
   produced for the rectified product and unit. Equations (1.1) and
   (1.10)-(1.11) are required to recover the original corner packet.
6. **THE OLD SIDE STILL DEPENDS ON COMP-CB.** SPLIT-C does not replace
   the compression packet; it identifies its single-map use and keeps
   it separate from the fresh SPLIT-B construction.
7. **NO AMPLIFICATION SUM IS PERMITTED.** The all-level proof rests on
   the four-term identity (1.14) and the isometry `tex:1475`. Replacing
   it by an entrywise matrix estimate would reintroduce an \(n\)-factor
   and invalidate the packet.
8. **ONLY THE LEDGER RADIUS CHANGES.** The corrected delta is
   \(C_{\rm co}\mapsto C_{\rm main}\) in \(L\), plus the
   \(e_{\rm split}\) guards in (3.2) and (4.2). The \(K\) formula,
   factor-map telescopes, PRH, H-CB, EXT-CB, and the finish are
   untouched.
9. **NO STATUS PROMOTION.** Even if a fresh hostile verifier accepts
   this artifact, the appropriate repository rung is
   `proved-mod-audit`, not `proved`/`af: validated`.
