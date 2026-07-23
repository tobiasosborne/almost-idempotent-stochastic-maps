# W73b hostile audit of Route F, steps F0--F3

Date: 2026-07-23  
Auditor posture: fresh, hostile, source-first  
Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`, SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`

## Executive verdicts

Q1: VALID

Q2: VALID-WITH-CORRECTIONS (the paper unmistakably claims universal constants, but it does not extract them; the proof route contains an incorrect printed direct-sum diagonal formula and an outline-level tensor-extension argument whose uniform constants are not actually closed)

Q3: INVALID (as written, the proof uses a false direct-sum diagonal construction and invokes `th_main_ext`, whose amplified proof is only sketched; the proposed generic nearest-CP/cone-projection repair is not shown to be dimension-free in cb norm, although an exact Haar/phase-balanced diagonal repairs the local CP step)

Q4: VALID

Q5: VALID

The decisive distinction is this:

- The literal statement of `th_factorization` is exactly the engine Route F wants.
- F0 and F2--F3 are correct, with the constants claimed by Strategist C, conditional on
  that engine.
- The supplied TeX does not establish `th_factorization` to a standard suitable for a
  rigorous import without repairing and completing its proof. Route F therefore remains
  conditional on a substantial literature-proof closure, not merely on extracting a
  numerical value of \(K\).

## Q1. Literal statement shape

### Verdict

Q1: VALID

At `tex:2730-2740`, the theorem says:

1. \(\mathcal H\) is nonzero and finite-dimensional.
2. \(\Phi:\mathcal B(\mathcal H)\to\mathcal B(\mathcal H)\) is UCP and
   \(\|\Phi^2-\Phi\|_{\rm cb}\le\eta\).
3. There are a finite-dimensional \(C^*\)-algebra \(\mathcal B\) and UCP maps in the
   orientations
   \[
   \Delta:\mathcal B\longrightarrow\mathcal B(\mathcal H),\qquad
   \Upsilon:\mathcal B(\mathcal H)\longrightarrow\mathcal B.
   \]
4. The first conclusion is literally
   \[
   \|\Delta\Upsilon-\Phi\|_{\rm cb}\le O(\eta)
   \]
   at `tex:2733-2734`.
5. The second conclusion is literally
   \[
   \bigl\|\Upsilon_n(\Delta_n(X)\Delta_n(Y))-XY\bigr\|
   \le O(\eta)\|X\|\|Y\|,
   \qquad X,Y\in M_n\otimes\mathcal B
   \]
   at `tex:2735-2737`.
6. The parenthetical consequence
   \[
   \|\Upsilon\Delta-1_{\mathcal B}\|_{\rm cb}\le O(\eta)
   \]
   is printed at `tex:2739`.

The quantifier “for every \(n\ge1\)” is not typeset beside (12.23), but it is the only
consistent reading: `tex:2728` declares the tensor-extension notation, \(n\) is arbitrary
in (12.23), and the asserted consequence is a cb-norm bound. Taking
\(Y=I_n\otimes1_{\mathcal B}\) is legitimate because \(\Delta\) is unital and gives
\[
\|\Upsilon_n\Delta_n(X)-X\|\le O(\eta)\|X\|.
\]

Thus Strategist C `lines 137-153` has the maps, orientations, and consequence in the
right direction. Its displayed (5.3) records only the \(n=1\) specialization, which is
all that its commutator calculation needs.

## Q2. Universality and the proof-chain constant audit

### Verdict

Q2: VALID-WITH-CORRECTIONS (the universality claim is explicit; its proof and numerical
constant extraction are not complete in the source)

### What big-\(O\) means in this paper

The convention is unusually explicit. At `tex:458`:

> each instance of big-\(O\) or similar notation stands for a concrete function, not
> depending on any additional data.

The main theorem then adds at `tex:460-462` that the implicit constant does not depend on
\(\mathcal A\) or its dimension. The extended theorem repeats the same statement at
`tex:1538-1540`. The introduction says at `tex:398-400` that the extended estimates are
uniform in the amplification level \(n\), and it advertises both factorization
orientations in cb norm.

Accordingly, the \(O(\eta)\)'s in `th_factorization` are claimed to be independent of:

- \(\dim\mathcal H\);
- \(\dim\mathcal B\);
- the number \(m\) of simple summands of \(\mathcal B\);
- all block dimensions \(\dim\mathcal L_j\);
- the amplification level \(n\).

Because only finitely many estimates are used, one may existentially replace their
constants by one common \(K\), and replace their smallness requirements by one common
\(\eta_{\rm K}>0\). What cannot be done from this TeX is to give a numerical \(K\) or
numerical \(\eta_{\rm K}\): most intermediate constants are left inside \(O(\cdot)\), and
the Newton/error-reduction constants in particular are not multiplied out.

### Constant-risk trace

#### 1. Functional calculus and `th_almost_idemp`

At `tex:2171-2179`, \(\widetilde\Phi=\theta(2\Phi-1)\) is constructed in the Banach
algebra of completely bounded maps. The Taylor series is used only for
\(\eta<1/4\). This step is dimension-free: it depends on a scalar power series and the cb
norm, not on a matrix-coordinate expansion.

At `tex:2198-2235` and `tex:2239-2723`, the approximate associativity estimates are
obtained from Stinespring isometries, \(C^*\)-homomorphisms, contractions, and a fixed
number of triangle/Cauchy--Schwarz steps. The same proof is applied to
\(1_{M_n}\otimes\Phi\) at `tex:2208-2209`. No sum over a basis, block set, or dimension
appears. This is structurally consistent with a universal constant, although the
diagrammatic proof does not expose its numerical value.

#### 2. Banach-analytic apparatus in Sections 5--7

The inverse-function, exact-unit, approximate-unitary, and polar-decomposition estimates
at `tex:493-914` are written in operator norms on Banach spaces. Their stated radii and
errors are scalar functions of \(\epsilon,\delta\). There is no overt dimension factor.
However, many thresholds are only called “suitable positive constants”; the paper does
not provide a complete numerical ledger.

#### 3. The nontrivial projection at `tex:931-969`

`lem_nontriv_projection` is nonconstructive: it uses Lefschetz--Hopf theory to obtain a
nontrivial fixed point. This is not itself a dimension dependence. The asserted
constant-distance exclusion near \(\pm I\) at `tex:943` is based on a uniform local
derivative estimate, not on a spectral search over \(\dim\mathcal A\).

The sibling D1 concern is therefore correctly described as a constructive/constant-
extraction concern, not a refutation of the theorem's universality claim. Nevertheless,
the TeX does not spell out the uniform neighborhood or its numerical radius.

#### 4. Projection-subspace decomposition

`lem_alpha` contains an explicit \(pq\) loss at `tex:1091-1118`. This is a potential
dimension leak if applied to a large partition all at once. The paper explicitly says at
`tex:1084` that it will use the lemma only for \(p,q\le2\), and the main construction
performs binary merges. Thus this factor is harmless only under that intended binary
use.

There is a typographical error at `tex:1109`: the displayed definition of
\(\beta_{jk}\) uses \(\operatorname{Co}_{P_j,Q_j}\); its codomain and all subsequent
indices require
\[
\beta_{jk}=\operatorname{Co}_{P_j,Q_k}.
\]

#### 5. Approximate homomorphism improvement

The dimension-free mechanism in `lem_approx` is the norm-one diagonal at
`tex:1245-1248`. Haar averaging gives
\[
D=\int U^\dagger\otimes U\,dU,\qquad \|D\|_\pi=1.
\]
This is exactly what prevents a block-count or matrix-size factor in
`tex:1277-1313`.

The explicit direct-sum formula at `tex:1254` is false for arbitrary choices of the
per-block designs appearing there. For the smallest counterexample,
\(\mathcal B=\mathbb C\oplus\mathbb C\), each one-dimensional block design consists only
of \(1\). The printed product construction gives
\[
D=1_{\mathcal B}\otimes1_{\mathcal B},
\]
but with \(e_1=(1,0)\),
\[
e_1D=e_1\otimes1_{\mathcal B}\ne1_{\mathcal B}\otimes e_1=De_1.
\]
So it is not a diagonal.

This does not invalidate the preceding Haar existence argument. Haar averaging over
\(\prod_jU(\mathcal L_j)\), or a finite phase-balanced version of it, kills all
cross-summand first moments and retains a norm-one convex combination of joint
unitaries. What would be dangerous is replacing it by the obvious cross-term-free
embedded block sum: that representation has a visible \(m\)-sized projective-norm
bound. The proof must retain the Haar/phase-balanced norm-one representation.

`tex:1313-1318` asserts the Newton/error-reduction constants
\(\epsilon_{\max},\delta_{\max},c_0\), but does not calculate them. This confirms the
sibling D2 observation about extraction, while not changing the literal claim that the
constants are universal.

#### 6. Iterated merging and extension

At `tex:1414-1444`, every binary extension or merge is followed by error reduction back
to \(c_0\epsilon\). If `cor_improvement` has a genuinely universal \(c_0\), the final
error does not accumulate with the number of blocks or extension steps. This is the
intended and internally consistent answer to the dimension-growth threat.

The source still suppresses the intermediate constants needed to verify that every
pre-improvement map remains below the same universal \(\delta_{\max}\). That bookkeeping
is plausible from the stated lemmas, but it is not carried out numerically.

#### 7. Tensor extension and `th_main_ext`

`prop_inc_ext`, `tex:1483-1506`, gives a uniform lower norm at every amplification. The
doubling loss \(a_{2n}\ge a_n/2\) is repaired by the base-level
`prop_delta_hominc`, yielding \(a_n\ge1-O(\delta+\epsilon)\) independent of \(n\).
`lem_approx_ext`, `tex:1508-1536`, uses the same norm-one diagonal and is also designed
to be uniform.

The proof of `th_main_ext` itself is not closed. At `tex:1542-1557` it says the arguments
are “straightforward,” “generalized in a straightforward way,” “should be adapted,” and
need “only trivial modifications.” In particular it does not prove in detail that the
single map \(v\) constructed at level one has every required amplified
multiplicativity, norm, and inverse bound with one common constant.

There is also a dimensional typo at `tex:1551-1555`. The printed inequality compares
\(\langle X,X\rangle\) to \(\|X\|_{n,1}\), then concludes that
\(\sqrt{\langle X,X\rangle}\) is comparable to \(\|X\|_{n,1}\). The required statement,
matching `tex:1129-1131`, is
\[
\left|\langle X,X\rangle-\|X\|_{n,1}^{\,2}\right|
\le O(\delta+\epsilon)\|X\|_{n,1}^{\,2}.
\]

This amplified-outline gap is the largest unresolved universality risk in the source.

#### 8. UCP replacement and block count

At `tex:2771-2801`, the same erroneous direct-sum diagonal formula reappears. With a
genuine norm-one Haar/phase-balanced diagonal, the averaging has total weight one and
introduces no \(m\) or block-dimension factor.

At `tex:2840-2899`, `lem_RC` is per block, the norm on
\(\bigoplus_j\mathcal B(\mathcal L_j)\) is a maximum, and the components of
\(\Upsilon'\) are estimated uniformly. No sum over \(j\) is taken in the output norm.
There is no hidden \(m\)-loss in this part.

### Universality conclusion

The claim of universality is clear and consistently advertised. The architecture also
contains recognizable devices intended to enforce it: cb norms, norm-one diagonals,
binary merging followed by error reduction, and maximum rather than sum norms over
blocks.

But “the paper claims a universal \(K\)” is stronger than “this TeX supplies a
fully checkable proof of one.” It does not. Strategist C `lines 155 and 286-300` may use
an existential common \(K\) only conditionally on closing the proof gaps above. It may
not describe \(K\) as already extracted.

## Q3. Soundness of `th_factorization`

### Verdict

Q3: INVALID (as a proof in the supplied source)

### Q3(a). The \(\Delta'\) CP argument

#### What is actually wrong

The sibling C14 diagnosis identifies a genuine failure in the printed construction but
misidentifies its logical cause. Exact multiplicativity of \(\widetilde\Delta\) is not
needed.

Let
\[
D=\sum_s p_sU_s^\dagger\otimes U_s
\]
be an exact diagonal of \(\mathcal B\). For
\(Y=(Y_{bc})\in M_n\otimes\mathcal B\), work entrywise (the naive tensor
identity with \(Y\) in both matrix factors would be false). The
\((a,c)\)-entry of the first expression defining
\(\Delta'_n(Y^\dagger Y)\) is
\[
\sum_{b,s}p_s\,
\Phi\!\left(
\widetilde\Delta(Y_{ba}^\dagger Y_{bc}U_s^\dagger)
\widetilde\Delta(U_s)\right).
\]
For each fixed \(b,a,c\), exact centrality of \(D\), applied to
\(Y_{bc}\) and then left-multiplied in the first tensor factor by
\(Y_{ba}^\dagger\), gives
\[
\sum_s p_s\,Y_{ba}^\dagger Y_{bc}U_s^\dagger\otimes U_s
=
\sum_s p_s\,Y_{ba}^\dagger U_s^\dagger\otimes U_sY_{bc}.
\]
Apply the bilinear operation
\[
a\otimes b\longmapsto
\Phi\!\left(\widetilde\Delta(a)\widetilde\Delta(b)\right)
\]
and then sum over \(b\). Because \(\widetilde\Delta\) commutes with the
involution, the resulting block matrix is
\[
\sum_s p_s\,
\Phi_n\!\left(Z_s^\dagger Z_s\right)\ge0,\qquad
Z_s=\widetilde\Delta_n((I_n\otimes U_s)Y).
\]
This is the displayed positivity at `tex:2791-2796`, and it is exact. No homomorphism
identity for \(\widetilde\Delta\) was used.

The failure is instead at `tex:2780-2783`: the printed Cartesian product of arbitrary
per-block designs need not be a diagonal of a direct sum. The
\(\mathbb C\oplus\mathbb C\) counterexample from Q2 already breaks the equality in
`tex:2788-2789`, hence also the displayed positivity derivation.

#### Exact local repair

Use the Haar diagonal over the full unitary group of \(\mathcal B\), whose existence and
norm-one property the paper already proves at `tex:1245-1248`.

A finite repair is also immediate: independently multiply every per-block design
unitary by a random sign \(\varepsilon_j\in\{\pm1\}\), and average over all signs. The
within-block terms \(U_j^\dagger\otimes U_j\) are unchanged, while every cross-block
term contains \(\mathbb E(\varepsilon_j\varepsilon_k)=0\) for \(j\ne k\). The resulting
joint unitaries form a norm-one convex representation of the true diagonal. With this
replacement, \(\Delta'\) is exactly CP and `tex:2797-2801` is locally valid.

#### Why generic cone projection is not yet a valid repair

Projecting a Choi matrix onto the positive cone controls the chosen Choi-matrix norm. It
does not automatically give
\[
\|\Delta_{\rm CP}-\Delta'\|_{\rm cb}\le C\eta
\]
with \(C\) independent of the domain and codomain dimensions. Standard conversions
between Choi norms and cb/diamond norms can carry dimension factors. A measured
\(O(\eta^2)\) negative eigenvalue on selected fixtures does not establish a universal
cb-distance-to-CP theorem.

If a dimension-free cb-close CP map were supplied, then the remaining estimates would
survive: after an \(O(\eta)\) unitalization, all degree-two and degree-three expressions
at `tex:2803-2829` change by \(O(\eta)\) through fixed-length telescoping estimates.
The missing premise is precisely the dimension-free cb closeness. The exact-diagonal
repair avoids this issue entirely.

### Q3(b). `lem_RC` and the construction of \(\Upsilon'\)

Conditional on a UCP \(\Delta\) satisfying `tex:2805-2815`, this portion survives hostile
checking.

1. At `tex:2843-2849`, the per-block unitary twirl makes
   \(R_j=1_{\mathcal L_j}\otimes C_j\) exactly. Since
   \(W_j^\dagger W_j\le I\), \(\|W_j\|\le1\) and
   \(\|C_j\|=\|R_j\|\le1\).
2. At `tex:2851-2856`,
   \[
   \Phi(W_j^\dagger R_jW_j)
   =\Delta(1_{\mathcal L_j})+O(\eta).
   \]
   Contractivity gives
   \(\|\Phi(W_j^\dagger R_jW_j)\|\le\|C_j\|\), while
   `Delta_norm` gives
   \(\|\Delta(1_{\mathcal L_j})\|\ge1-O(\eta)\). Hence
   \(1-O(\eta)\le\|C_j\|\le1\).
3. A unit vector \(\xi_j\) with
   \(\|C_j\xi_j\|=\|C_j\|\) exists in finite dimension. In fact \(C_j\) is positive,
   because it is the partial-trace coefficient of a positive twirl.
4. Every summand defining \(L_j\) at `tex:2860-2864` is a contraction, so
   \(\|L_j\|\le1\). Therefore \(\Upsilon'\) is CP,
   \(\|\Upsilon'\|_{\rm cb}\le1\), and
   \[
   \|\Upsilon'\Phi-\Upsilon'\|_{\rm cb}
   \le\|\Phi^2-\Phi\|_{\rm cb}.
   \]
5. The calculation at `tex:2873-2892` is correctly ordered. The first approximation
   uses `PhiDelta1` and `PhiDelta3`; the Choi expansion then leaves only the \(j\)-block;
   the two averages factor as \(R_j^\dagger(Y_j\otimes I)R_j\); and the last scalar is
   \(\|C_j\xi_j\|^2=1-O(\eta)\). Thus
   \[
   \|\Upsilon'\Delta-1_{\mathcal B}\|_{\rm cb}\le O(\eta)
   \]
   with no sum over \(j\).
6. The ancilla order at `tex:2859-2869` is consistent with the paper's convention
   \(V:\mathcal H\to\mathcal H\otimes\mathcal F\). The sibling C13 issue concerns an
   implementation using the opposite tensor-factor convention; it is not a defect in
   the TeX.
7. In the chain at `tex:2895`,
   \(\Upsilon'\Phi\approx\Upsilon'\) uses \(\|L_j\|\le1\);
   \(\Phi\approx\widetilde\Phi\) is a cb estimate;
   \(\widetilde\Phi=\widetilde\Delta\widetilde\Upsilon\) is exact;
   \(\widetilde\Delta\approx\Delta\) is cb;
   and \(\Upsilon'\Delta\approx1\) is the bound just proved.
   Hence \(\Upsilon'\approx\widetilde\Upsilon\).
8. Consequently \(\Upsilon'(I)=I_{\mathcal B}+O(\eta)\). For small universal \(\eta\)
   it is positive and invertible, so `tex:2896-2899` gives a UCP \(\Upsilon\) still
   cb-close to \(\widetilde\Upsilon\).

Thus C13 does not produce a mathematical obstruction. The local F3 construction is
sound once the input \(\Delta\) is genuinely UCP with the listed estimates.

### Q3(c). What `th_main_ext` must deliver

The factorization proof needs one finite-dimensional \(C^*\)-algebra \(\mathcal B\) and
one bijection \(v:\mathcal B\to\mathcal A\) such that, uniformly for every \(n\),

- \(v_n\) and \(v_n^{-1}\) have norm \(1+O(\eta)\);
- \(v(I_{\mathcal B})=I_{\mathcal A}+O(\eta)\);
- \(v_n(XY)=v_n(X)\star v_n(Y)+O(\eta)\|X\|\|Y\|\);
- \(v\) commutes with the involution;
- all constants and the smallness threshold are independent of all dimensions and of
  \(n\).

These properties give
\[
\widetilde\Delta=v:\mathcal B\to\mathcal A\subseteq\mathcal B(\mathcal H),\qquad
\widetilde\Upsilon=v^{-1}\widetilde\Phi,
\]
and therefore the exact identities at `tex:2750-2752` plus the amplified product
estimate at `tex:2758-2766`.

`th_main_ext` states exactly this strength through the definition at
`tex:1477-1484`. It is not proved at that strength in a fully checkable way:
`tex:1542-1557` supplies an adaptation outline, contains the squared-norm typo noted
above, and omits the uniform amplified versions of the Hilbert-space and merging
arguments. This is not a cosmetic missing constant. It is the load-bearing bridge from
an ordinary approximate algebra isomorphism to the cb estimates required by
`th_factorization`.

Accordingly, the source supports “stated theorem with a plausible dimension-free proof
architecture,” not “audited rigorous engine.”

## Q4. The classical lift F0

### Verdict

Q4: VALID

Let \(D:M_n\to\ell_\infty^n\) take the diagonal and
\(J:\ell_\infty^n\to M_n\) be diagonal inclusion.

### Q4(a). Complete positivity

A row-stochastic \(Q\) is a positive unital map on \(\ell_\infty^n\). Positive maps with
commutative domain are completely positive. Both \(D\) and \(J\) are UCP. Therefore
\[
\Phi=JQD
\]
is UCP.

### Q4(b). Squaring

Since \(DJ=1_{\ell_\infty^n}\),
\[
\Phi^2=JQD\,JQD=JQ^2D,
\qquad
\Phi^2-\Phi=J(Q^2-Q)D.
\]

### Q4(c). Exact cb-norm identity

For any scalar matrix \(L=(l_{ij}):\ell_\infty^n\to\ell_\infty^m\), identify
\[
M_r(\ell_\infty^n)\cong\bigoplus_{j=1}^nM_r,\qquad
\|(X_j)_j\|=\max_j\|X_j\|.
\]
Then
\[
L_r((X_j)_j)=\left(\sum_jl_{ij}X_j\right)_i,
\]
so
\[
\|L_r\|\le\max_i\sum_j|l_{ij}|.
\]
Choose a maximizing row \(i_0\) and
\[
X_j=e^{-i\arg l_{i_0j}}I_r
\]
(maximizing signs suffice for real \(L\)). The input has norm one and the \(i_0\)-th
output is
\[
\left(\sum_j|l_{i_0j}|\right)I_r.
\]
Hence, for every \(r\),
\[
\|L_r\|=\max_i\sum_j|l_{ij}|=\|L\|_{\infty\to\infty}.
\]

Now \(D_r\) is contractive, \(J_r\) is isometric, and
\[
\|(JLD)_r\|\le\|L_r\|.
\]
For the reverse inequality, take the attaining input in the range of \(J_r\), so that
\(D_rJ_r=1\). Therefore
\[
\|JLD\|_{\rm cb}=\|L\|_{\infty\to\infty}.
\]
With \(L=Q^2-Q\), Strategist C `lines 126-133` is correct in both directions:
\[
\|\Phi^2-\Phi\|_{\rm cb}
=\|Q^2-Q\|_{\infty\to\infty}.
\]

## Q5. Commutativity forcing and compression F2--F3

### Verdict

Q5: VALID

Assume one common \(K\) gives
\[
\|\Delta\Upsilon-\Phi\|_{\rm cb}\le K\eta,\qquad
\|\Upsilon\Delta-1_{\mathcal B}\|_{\rm cb}\le K\eta,
\]
and the multiplicativity estimate from Q1. All calculations below are also valid at
amplification level, though level one suffices for commutativity.

### Q5(a). Approximate invariance of \(\Delta\)

Because \(\Delta\) is UCP, \(\|\Delta\|_{\rm cb}=1\). Thus
\[
\begin{aligned}
\|\Phi\Delta-\Delta\|_{\rm cb}
&\le\|(\Phi-\Delta\Upsilon)\Delta\|_{\rm cb}
 +\|\Delta(\Upsilon\Delta-1_{\mathcal B})\|_{\rm cb}\\
&\le2K\eta.
\end{aligned}
\]
Strategist C `lines 159-165` is exact.

### Q5(b). The constants \(8\) and \(10\)

For contractions \(x,y\in\mathcal B\), put
\[
a=\Delta x,\quad b=\Delta y,\quad
a_0=\Phi\Delta x,\quad b_0=\Phi\Delta y.
\]
Both \(a_0,b_0\) are diagonal, hence commute. All four elements are contractions, and
\[
\|a-a_0\|,\ \|b-b_0\|\le2K\eta.
\]
Therefore
\[
\begin{aligned}
\|[\Delta x,\Delta y]\|
&=\|[a-a_0,b]+[a_0,b-b_0]\|\\
&\le2\|a-a_0\|\|b\|+2\|a_0\|\|b-b_0\|\\
&\le8K\eta.
\end{aligned}
\]
Using the multiplicativity estimate in the two orders,
\[
\begin{aligned}
\|[x,y]\|
&\le
\|xy-\Upsilon(\Delta x\Delta y)\|
+\|\Upsilon([\Delta x,\Delta y])\|\\
&\qquad
+\|\Upsilon(\Delta y\Delta x)-yx\|\\
&\le K\eta+8K\eta+K\eta
=10K\eta.
\end{aligned}
\]
The argument does need \(\|\Delta\|_{\rm cb}=\|\Upsilon\|_{\rm cb}=1\), and UCP supplies
exactly that.

### Q5(c). Exact commutator gap in a noncommutative block

In \(M_2\), take the Pauli contractions
\[
x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
y=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
They are unitaries and
\[
[x,y]=\begin{pmatrix}0&-2\\2&0\end{pmatrix},
\qquad \|[x,y]\|=2.
\]
Embed this \(2\times2\) corner into any \(M_d\), \(d\ge2\), and put zero in all other
summands. Hence every noncommutative finite-dimensional \(C^*\)-algebra contains two
contractions with commutator norm exactly \(2\).

It follows that \(10K\eta<2\) forces
\(\mathcal B\cong\ell_\infty^k\). Strategist C `lines 166-178` is correct. This is also
why Strategist A's `lines 82-84` “commutative inheritance” need not be obtained by
inspecting Kitaev's block-building algorithm: the quantitative commutator argument
forces it after the factorization is built.

### Q5(d). Lower bound for \(A=D\Delta\)

The approximate left inverse gives, for every \(x\in\ell_\infty^k\),
\[
\|x\|
\le\|\Upsilon\Delta x\|+K\eta\|x\|
\le\|\Delta x\|+K\eta\|x\|,
\]
so
\[
\|\Delta x\|\ge(1-K\eta)\|x\|.
\]

The exact identity is not \(\Phi\Delta=JA\). It is
\[
\Phi\Delta=JQD\Delta=JQA.
\]
Using Q5(a), the isometry of \(J\), and the contractivity of the stochastic map \(Q\),
\[
\begin{aligned}
\|\Delta x\|
&\le\|\Phi\Delta x\|+2K\eta\|x\|\\
&=\|JQAx\|+2K\eta\|x\|\\
&\le\|Ax\|+2K\eta\|x\|.
\end{aligned}
\]
Combining the two inequalities yields
\[
\|Ax\|\ge(1-3K\eta)\|x\|.
\]

Strategist C `lines 197-203` writes the correct identity
\(\Phi\Delta x=JQAx\); the contraction by \(Q\) is implicit there and should be made
explicit in any formal proof.

### Q5(e). The \(MA-I_k\) bound

Let
\[
A=D\Delta,\qquad M=\Upsilon J,\qquad F=AM.
\]
Then composition is exactly as written:
\[
D\Delta\Upsilon J=(D\Delta)(\Upsilon J)=AM.
\]
Compressing the first factorization estimate gives
\[
\begin{aligned}
D(\Delta\Upsilon-\Phi)J
&=D\Delta\Upsilon J-DJQDJ\\
&=AM-Q,
\end{aligned}
\]
and therefore
\[
\|AM-Q\|\le K\eta.
\]
Similarly,
\[
D(\Phi\Delta-\Delta)=QA-A,
\qquad
\|QA-A\|\le2K\eta.
\]

Since \(A\) is positive unital, \(\|A\|=1\). Thus
\[
\begin{aligned}
\|A(MA-I)x\|
&=\|AMAx-Ax\|\\
&\le\|(AM-Q)Ax\|+\|(QA-A)x\|\\
&\le3K\eta\|x\|.
\end{aligned}
\]
Apply the lower bound for \(A\) to \((MA-I)x\):
\[
(1-3K\eta)\|(MA-I)x\|
\le3K\eta\|x\|.
\]
For \(3K\eta<1\),
\[
\|MA-I_k\|
\le\frac{3K\eta}{1-3K\eta}.
\]
Strategist C `lines 182-216` is correct.

### Root 5 constants

Conditional on a valid universal factorization constant \(K\), enlarge it to \(K\ge1\)
if necessary and take
\[
\eta_0\le\min\{\eta_{\rm K},1,(24K)^{-1}\}.
\]
Then \(10K\eta<2\), \(3K\eta\le1/8\), and
\[
\varepsilon=\frac{3K\eta}{1-3K\eta}\le4K\eta<\frac12.
\]
The estimates at Strategist C `lines 284-300` follow. No additional dimension
dependence is introduced in F2--F3.

## Correction ledger

| Locus | Flaw | Corrected statement |
|---|---|---|
| `tex:1254` | Cartesian products of arbitrary per-block unitary designs need not give a diagonal of a direct sum. | Use the full Haar diagonal, or add independent block phases/signs so all cross-block first moments vanish. |
| `tex:1109` | \(\beta_{jk}\) is printed with \(Q_j\), inconsistent with its codomain and subsequent use. | \(\beta_{jk}=\operatorname{Co}_{P_j,Q_k}\). |
| `tex:1551-1555` | The extended inner-product estimate omits squares and does not imply the following norm comparison. | \(\left|\langle X,X\rangle-\|X\|_{n,1}^2\right|\le O(\delta+\epsilon)\|X\|_{n,1}^2\). |
| `tex:1542-1557` | `th_main_ext` is concluded by “straightforward”/“should be adapted” assertions, without proving one map has all uniform amplified bounds. | Supply the amplified compression, Hilbert-space, extension, merging, and error-reduction lemmas with a single dimension-free constant ledger. |
| `tex:2780-2783` | Repeats the false direct-sum diagonal formula. | Use the norm-one Haar/phase-balanced whole-algebra diagonal. |
| `tex:2788-2796` | Positivity is not justified for the printed, possibly noncentral \(D\). | With an exact diagonal, centrality—not exact multiplicativity of \(\widetilde\Delta\)—gives the displayed sum of \(\Phi_n(Z_s^\dagger Z_s)\). |
| sibling FINDINGS C14, `lines 670-704` | Attributes the CP failure to \(\widetilde\Delta\) being only approximately multiplicative and treats cone projection as automatically harmless. | The local cause is loss of exact diagonal centrality. A cone projection is sufficient only after proving dimension-free cb closeness and unitalization bounds; the exact-diagonal repair is preferable. |
| Strategist C `lines 137-155` | Labels the imported engine as known literature and speaks of extracting one \(K\), without exposing the proof-level gaps. | Treat `th_factorization` as stated/conditional until the direct-sum diagonal and `th_main_ext` closures are independently proved. |
| Strategist C `lines 197-203` | No wrong formula is printed, but the contractive step is compressed. | Record explicitly \(\Phi\Delta=JQA\) and \(\|QAx\|\le\|Ax\|\); never replace this by \(\Phi\Delta=JA\). |

## Residual risk register

Even under the most optimistic reading of the local repairs, the following stand between
Route F and a rigorous proof of `op-classical`.

1. **A complete proof of `th_main_ext`.** The source states the required uniform theorem
   but does not prove the amplified construction in full. This is the principal blocker.
2. **A universal constant ledger.** One must derive a common finite \(K\) and a common
   positive \(\eta_{\rm K}\) from the functional-calculus, approximate-algebra,
   error-reduction, tensor-extension, CP, and normalization steps. A numerical value is
   not mathematically necessary for `op-classical`, but universality is.
3. **The exact whole-algebra diagonal repair.** The corrected Haar or phase-balanced
   finite diagonal must be inserted at both `tex:1254` and `tex:2780-2783`, and all uses
   of its centrality and norm-one representation must be rechecked.
4. **No unproved cone-projection shortcut.** If cone projection is retained instead,
   it needs a theorem controlling distance to the CP cone in cb norm with a universal
   constant, plus preservation of unitality and the degree-two/three estimates. Choi
   eigenvalue measurements are not such a theorem.
5. **Full audit of `th_almost_idemp`.** This audit traced its dimension-free mechanism
   and checked the interfaces used here, but did not independently re-prove every
   diagrammatic equality in `tex:2239-2723` with explicit constants.
6. **The positive-retract hardening (PRH) lemma.** Root 4, Strategist C
   `lines 223-280`, was outside Q1--Q5. Its simultaneous thresholding, conditioning,
   norm estimates, and \(\varepsilon=0\) endpoint still require a standalone hostile
   proof/review before they can close the route.
7. **Rigour-status and provenance closure.** Until items 1--6 are discharged under the
   repository's reviewer/proof protocol, Route F is a promising conditional reduction,
   not a rigorous proof of `op-classical`.

The hostile bottom line is therefore:
\[
\boxed{\text{F0--F3 are sound conditional on Theorem 12.3, but Theorem 12.3 is not
rigorously established by the supplied TeX as written.}}
\]
