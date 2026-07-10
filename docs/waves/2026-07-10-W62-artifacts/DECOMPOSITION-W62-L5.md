# W62 decomposition strategy — L5-GAP-1, the dual-face mass minimax

This is a strategy artifact only. Every new node below has proposed status
`conjecture`; no statement is promoted and no proof of L5-GAP-1 is claimed.
All nodes stay in the exact **signed** picture, with
\(\delta=\delta(P)>0\) and \(\tau=\sqrt\delta\). There is no stochastic
crossing. The case \(\delta=0\) is vacuous under the target's tall hidden-top
hypothesis by `lem-delta-zero-endpoint` (then \(H=0\)).
Throughout, \(c_m\in(0,1)\) is fixed first as the universal W54 branch
threshold, exactly as in `context/l5-answer.md`.

## 0. Binding-gap verdict

**The binding gap is an engine-payer mass-transport dual, not a finite cover of
\(Y_v\).** The conditional cover lemma in `context/l5-answer.md` is correct,
but a universal cover is a stronger sufficient statement, not an equivalent
form of the direct minimax. It also retains the wrong combinatorial object:
the number of pointwise serving directions. If the \(A\)-mass is first
aggregated on full row-point fibers and normalized, exact affinity gives one
synthetic row-hull point
\[
 q_A=\frac1{S_A}\sum_Q m_Qp_Q,
 \qquad
 \frac1{S_A}L_A(y)=y\cdot(p_v-q_A).
\]
Thus L5 asks for one top-dual direction separating one **owned barycenter**.
The W54 simplex obstruction says precisely that this barycenter can re-enter
the convex summit cylinder even though every atom is pointwise visible; it
does not say that a growing cover is the intrinsic object.

Two proposed, near-mechanical reductions make the remaining obstruction
smaller. First, R1 proposes the following constant-complexity primal ray
certificate for the support value at \(q_A\):
\[
 Z_v(q_A)=\min_{\Lambda\ge0,\ c\in C_W}
 \bigl(\|p_v-q_A+\Lambda(p_v-c)\|_1-\Lambda H\bigr).
\]
Second, R2--R3 propose an allocation of the W61 exterior-financing engine to
the correct carrier. Applying `lem-hx-forced-exterior-coupling` to every pair
\((v,Q)\) charged by the \(P_v^+\)-submeasure and then using \(P^2=P\) once
would force **row \(v\) itself** to put \(\Omega(\tau S_A)\) positive mass
outside every half-ball. This is stronger than a collection of unrelated
pairwise demands and is exactly where the new engine bank changes the proposed
surface.

The true creative fork is therefore where this forced payer lives. Either a
local half-ball has an exterior payer below the \((H-8\tau)\)-depth band (the
**shallow-counterweight horn**), or every local half-ball has an exterior
\(P_v^+\)-payer in the far co-top web (the **uniform co-top-web horn**). The
first must beat the W54 constants fight; the second must rule out a globally
completed, internally reproducing dual-simplex plateau. Tallness is the only
known resource capable of doing either: both W61 refuter families bought the
local financing ledgers but failed exactly at \(H>16\tau\). A one-functional
construction through the ray certificate plus this payer fork is therefore
the recommended route. To avoid leaving the whole simplex obstruction in one
leaf, the co-top horn is split once more: scalar drift or scalar width produces
an explicit weighted chord (C), while simultaneous low drift and low width is
the isolated isotropic completion problem (I). A finite cover should be
retained only as a fallback if it emerges from one of these horns, not made the
main target.

## 1. The tree

### Shared clone-quotient notation

Call \((P,v,A)\) an **L5 datum** when \(P\) is an exact signed idempotent
with \(0<\delta\), \(W(P)\ne\varnothing\), \(v\) is a hidden top vertex with
\(H>16\tau\), and every \(j\in A\) satisfies the target's two inequalities
\(\|p_j-p_v\|_1\ge4\tau\) and \(d_j>H-8\tau\); mass lower bounds are stated
separately in the nodes that need them.

Let \(\mathcal Q(P)\) be the finite set of full equal-row fibers and write
\(p_Q\) for their common row point. For a fiber set \(F\), put
\[
 P_Q^+(F):=\sum_{R\in F}\sum_{k\in R}(P_{Qk})_+,
 \qquad
 P_v^+(F):=\sum_{R\in F}\sum_{k\in R}(P_{vk})_+.
\]
For the arbitrary target set \(A\), do **not** take a positive part after
fiber aggregation. Instead define the quotient submeasure
\[
 m_Q:=\sum_{j\in A\cap Q}(P_{vj})_+,
 \qquad S:=\sum_Qm_Q=S_A,
 \qquad \mu_Q:=m_Q/S,
 \qquad q:=q_A:=\sum_Q\mu_Qp_Q\in K(P).
\]
This preserves an arbitrary partially selected fiber while forgetting all
clone multiplicity. Under a compatible lift of the selected submeasure,
\(m_Q\), \(S\), \(\mu\), and \(q\) are unchanged; universal quantification
over quotient submeasures is what supplies clone safety for arbitrary \(A\).

Let
\[
 d_Q:=d_1(p_Q,C_W),
 \qquad z_y(Q):=y\cdot(p_v-p_Q),
 \qquad z_y(j):=y\cdot(p_v-p_j),
 \qquad
 Z_v(q):=\sup_{y\in Y_v}y\cdot(p_v-q),
 \qquad D_0:=2+4\delta.
\]
Also define
\[
 \begin{aligned}
 G_v&:=\{Q:\|p_Q-p_v\|_1\ge4\tau,\ d_Q>H-8\tau\},\\
 \mathrm{Sh}_v&:=\{Q:d_Q\le H-8\tau\},\\
 E_c&:=\{Q:\|p_Q-c\|_1>1/2\},\\
 K_v^{\mathrm{loc}}&:=\{c\in K(P):\|c-p_v\|_1\le1/4\}.
 \end{aligned}
\]
The target hypothesis says \(\operatorname{supp}\mu\subseteq G_v\). The
strict/non-strict conventions are deliberate: \(G_v\) owns the strict depth
band, while \(\mathrm{Sh}_v\) owns equality.

For any nonzero positive full-fiber measure \(\omega\), write
\[
 M_\omega:=\sum_Q\omega_Q,
 \qquad \bar\omega_Q:=\omega_Q/M_\omega,
 \qquad r_\omega:=\sum_Q\bar\omega_Qp_Q,
\]
and define its clone-invariant scalar width
\[
 \Omega(\omega):=
 \sup_{\substack{\ell\ \mathrm{affine}\\
                   \operatorname{Lip}_{\ell^1}(\ell)\le1}}
 \sum_Q\bar\omega_Q\,|\ell(p_Q)-\ell(r_\omega)|.
\]
Affine constants cancel, so the supremum is over a compact
\(\ell^\infty\)-ball of linear parts and is attained. This is a scalar
diagnostic, not a selected coordinate frame.

```mermaid
flowchart TD
    L5[L5 datum P,v,A]
    R0[R0 mass barycenter]
    R1[R1 dual ray certificate]
    R2[R2 one-step foldback]
    R3[R3 universal exterior payer]
    S[S shallow-payer exclusion]
    C[C scalarizable co-top web]
    I[I isotropic co-top web]
    Z[normalized Z_v(q) lower bound]
    Y[one y in Y_v]

    L5 --> R0
    L5 --> R1
    R2 --> R3
    L5 --> R3
    R3 -->|some local center has shallow payer| S
    R3 -->|no shallow payer; drift or width| C
    R3 -->|no shallow payer; low drift and width| I
    R0 --> Y
    S --> Z
    C --> Z
    I --> Z
    Z --> Y
    R1 --> S
    R1 --> C
    R1 --> I
    R2 --> S
    R2 --> C
    R2 --> I
```

The intended dependency order is \(\mathrm{R0},\mathrm{R1},\mathrm{R2}\)
first, then R3, then S/C/I. S, C, or I supplies the normalized \(Z_v(q)\)
bound; only R0 converts that bound to the requested mass objective and hence
to one \(y\). There is no back-edge and no node consumes its own assembly
consequence.

### R0 — `conj-w62-mass-barycenter-dualization`

**(a) Pinned contract.** Proposed metadata: `status: conjecture`;
`picture: signed delta`; intended deps: `lem-top-support-dual-face`,
`lem-affine-barycenter-identity`.

> For every L5 datum \((P,v,A)\) with \(S>0\), the quotient barycenter \(q\)
> above satisfies
> \[
>   \sup_{y\in Y_v}\sum_{j\in A}(P_{vj})_+z_y(j)=S Z_v(q).
> \]

**(b) Mechanism sketch.** The first identity is finite affine integration:
\(S^{-1}L_A(y)=y\cdot(p_v-q)\), followed by the supremum over the same compact
face \(Y_v\). A useful body corollary follows because every \(y\in Y_v\) obeys
\[
 y\cdot q-h_C(y)\le d_1(q,C_W),
 \quad
 y\cdot(p_v-q)=H-(y\cdot q-h_C(y)).
\]
In particular, failure at level \(\gamma\tau\) puts the single synthetic
point \(q\) in the co-top cylinder:
\(Z_v(q)<\gamma\tau\Rightarrow d_1(q,C_W)>H-\gamma\tau\).
`lem-top-deficit-price` supplies \(z_y(Q)\ge0\), which later permits discarding
unselected fibers without a sign loss.

**(c) Honest price.** Difficulty: **routine**. The likeliest death is only a
contract wording error around a partially selected clone fiber; the definition
of \(m_Q\) above removes it. Evidence for the identity is the already proved
dual-face reduction in `context/l5-answer.md`. Adverse evidence is not against
R0 but against overreading it: the W54 simplex witness shows that \(q\) may be
blind even when every atom is visible.

**(d) Interface check.** \(A\) and its full-fiber submeasure are fixed before
\(q\); \(y\) is chosen only after \(q\). There is no rowwise \(y_Q\), no
averaging of support functionals, no support-size bound, and no Jensen step.
All quantities are row points, affine values, and full-fiber masses. The
statement is frame-free.

**(e) Fallback.** If partial-fiber notation is awkward, state the same equality
for an arbitrary nonzero full-fiber submeasure \(m\le P_v^+\); the target's
\(A\)-measure is then a literal instantiation.

### R1 — `conj-w62-top-face-primal-ray-formula`

**(a) Pinned contract.** Proposed metadata: `status: conjecture`;
`picture: signed delta`; intended dep: `lem-top-support-dual-face`.

> For every exact signed idempotent \(P\) with \(\delta(P)>0\), nonempty
> visible set, and hidden top vertex \(v\) of height \(H\), and every
> \(q\in K(P)\),
> \[
>  Z_v(q)=\min_{\Lambda\ge0,\ c\in C_W}
>  \left\{\|p_v-q+\Lambda(p_v-c)\|_1-\Lambda H\right\},
> \]
> where \(c\) is omitted when \(\Lambda=0\).

**(b) Mechanism sketch.** By `lem-top-support-dual-face`,
\[
 Y_v=\{y:\|y\|_\infty\le1, y\cdot(p_v-p_w)\ge H\ \forall w\in W\}.
\]
Finite LP duality introduces multipliers \(\lambda_w\ge0\). Writing
\(\Lambda=\sum_w\lambda_w\) and
\(c=\Lambda^{-1}\sum_w\lambda_wp_w\) collapses the entire dual multiplier
family to the displayed pair \((\Lambda,c)\). Thus minimax failure has one
constant-complexity **outward visible-ray certificate**, not a large family of
extreme points of \(Y_v\).

**(c) Honest price.** Difficulty: **routine** (a valuable algebra audit). The
likeliest death is a sign error in the LP dual or an omitted \(\Lambda=0\)
edge, not a geometric counterexample. The formula passes the one-dimensional
test \(C_W=\{0\},p_v=1\). Finite primal feasibility, compactness, and ordinary
finite LP strong duality are evidence for attainment.

**(d) Interface check.** The minimizer is existential after \(q\); no
canonical choice, tie property, or exact-max-volume selector is asserted.
Aggregating \(\lambda_w\) into \((\Lambda,c)\) is an affine identity on the
visible hull. No coefficient cleanup, coordinate chart, or frame-specific
simplex model is used. S, C, and I must consume the actual certificate they
get; they may not assume a favorable minimizer.

**(e) Fallback.** Keep the finite nonnegative multipliers aggregated on full
visible row-point fibers in the formula. That is clone-safe and exactly
equivalent; it is less compact but avoids any concern at \(\Lambda=0\).

### R2 — `conj-w62-positive-flow-foldback`

**(a) Pinned contract.** Proposed metadata: `status: conjecture`;
`picture: signed delta`; intended dep: `lem-mass-split`.

> For every finite exact signed idempotent \(P\), row \(v\), nonnegative
> full-fiber submeasure \(m_Q\le\sum_{j\in Q}(P_{vj})_+\), and function
> \(g:\mathcal Q(P)\to[0,M]\),
> \[
>  \sum_Qm_Q\sum_R\sum_{k\in R}(P_{Qk})_+g_R
>  \le
>  \sum_R\sum_{k\in R}(P_{vk})_+g_R+2\delta(1+\delta)M.
> \]

**(b) Mechanism sketch.** Expand row \(v\) of \(P^2=P\), split its positive
coefficients into \(m\) plus the positive remainder, and split its negative
coefficients once. Every row has negative mass at most \(\delta\), positive
mass at most \(1+\delta\), and the \(m\)-mass lost to a negative receiver
term cancels algebraically with the same \(m\)-mass removed from the positive
remainder bound. The surviving error is at most \(2\delta(1+\delta)M\).
For \(g=1_F\), this says the selected actors' aggregate positive one-step
outflow into \(F\) cannot substantially exceed \(P_v^+(F)\). For
\(g=z_y\), \(0\le z_y\le D_0\) and `lem-top-deficit-price` additionally cap
the whole folded dual moment by \(O(\delta D_0)\).

**(c) Honest price.** Difficulty: **routine**. The likeliest death is a loose
constant or a missed internal-fiber sign cancellation. The exact identity
\(P_v=P_vP\), `lem-mass-split`, and the same subset-budget pattern later
formalized by `lem-hx-signed-variation-ledger` are strong evidence; the ledger
is corroborative rather than a claimed formal dependency here.

**(d) Interface check.** This is one aggregate one-step flow, not a raw-index
path-product floor and not a claim that \(P\) is stochastic. The positive part
is taken before receiver-fiber aggregation, exactly as in the signed ledger.
The contract is universal in \(g\), so R3 may use the indicator of its actual
half-ball complement and S/C/I may use their actual single dual deficit. No
carrier is selected independently.

**(e) Fallback.** Replace the sharp error by \(4\delta M\) for
\(\delta\le1/4\). If a hostile algebra pass finds asymmetric errors, split the
set-indicator form (needed by R3) from the deficit-moment form rather than
hiding the issue in a compound estimate.

### R3 — `conj-w62-universal-exterior-payer`

**(a) Pinned contract.** Proposed metadata: `status: conjecture`;
`picture: signed delta`; intended deps:
`lem-hx-forced-exterior-coupling`, R2.

> There is \(\delta_E>0\) such that for every finite exact signed idempotent
> \(P\) with \(0<\delta(P)=\delta\le\delta_E\), every row \(v\) of \(P\),
> and every nonnegative full-fiber submeasure \(m\le P_v^+\) of mass
> \(S\ge c_m\) supported on
> \(\{Q:\|p_Q-p_v\|_1\ge4\tau\}\), one has
> \[
>   \forall c\in K(P),\qquad P_v^+(E_c)\ge\frac18\,\tau S.
> \]

**(b) Mechanism sketch.** For every charged fiber \(Q\), choose any row-index
representative \(s\in Q\); equal rows make all displayed fiber totals
representative-independent. For every fixed \(c\in K(P)\),
`lem-hx-forced-exterior-coupling` applied to \((v,s)\) gives
\[
 P_v^+(E_c)+P_Q^+(E_c)
 \ge \frac{\tau}{1+2\delta}-2\delta,
\]
because \(\|p_Q-p_v\|_1\ge4\tau\). Multiply by \(m_Q\), sum over full
fibers, and use R2 with \(g=1_{E_c}\). If \(V=P_v^+(E_c)\), the exact
intermediate inequality is
\[
 (1+S)V\ge
 S\left(\frac{\tau}{1+2\delta}-2\delta\right)
 -2\delta(1+\delta).
\]
Since \(S\le1+\delta\), the displayed \(1/8\) follows, for example, after
shrinking below a ceiling of the shape
\(\delta_E\le\min\{1/16,(c_m/32)^2\}\). This is the exact
engine-demand pairing missing in W54: actor financing cannot be repeatedly
charged without being folded back to the top row.

**(c) Honest price.** Difficulty: **routine-hard / near-mechanical**. The
likeliest death is only a boundary or constant correction.
`lem-hx-forced-exterior-coupling` explicitly did not allocate which endpoint
pays; R2 is the new allocation step. Evidence against a hidden class-count loss is that the
whole argument is one normalized full-fiber sum. The W61 dyadic leak-financer
is useful hostile calibration: it may pay a local engine demand, but it must
also pass this foldback inequality.

**(d) Interface check.** The order is
the fixed \(c_m\) first, then \(\delta_E\), then \((P,v,m)\), and finally
**every** \(c\in K(P)\). The strict \(>1/2\) set is exactly the banked E5
boundary. No center selector, path count, dimension, or number of fibers
appears. R3 does not yet assert a top-dual deficit; S, C, and I own that
conversion.

**(e) Fallback.** Retain the exact intermediate inequality above, or use
`lem-hx-financing-floor` directly at a fixed radius \(R\in(0,1)\) and keep an
explicit \(b_E(R)\). If foldback fails, the honest fallback object is the
two-payer package
\[
 S P_v^+(E_c)+\sum_Qm_QP_Q^+(E_c)
 \ge S\left(\frac{\tau}{1+2\delta}-2\delta\right),
\]
not an illegal unquantified sum of independent pairwise floors.

### S — `conj-w62-shallow-exterior-payer-exclusion`

**(a) Pinned contract.** Proposed metadata: `status: conjecture`;
`picture: signed delta`; intended deps: R1, R2,
`lem-hx-financing-floor`, `lem-hx-transverse-moment-identity`,
`lem-negpart-subadditive`, `lem-top-deficit-price`,
`obs-height-collapse`, `lem-halo-collapse`.

> There are universal \(\gamma_S>0\) and \(\delta_S\in(0,1/4]\) such that every L5
> datum \((P,v,A)\) with \(0<\delta\le\delta_S\), \(S\ge c_m\), and
> \[
>  \exists c\in K_v^{\mathrm{loc}}:\quad
>  P_v^+(E_c\cap\mathrm{Sh}_v)\ge\frac1{16}\tau S
> \]
> satisfies \(Z_v(q_A)\ge\gamma_S\tau\).

**(b) Mechanism sketch.** Argue from a failed conclusion. R1 replaces the
whole dual face by one outward-ray certificate \((\Lambda,c_0)\) for \(q_A\).
Every shallow payer \(R\in\mathrm{Sh}_v\) has
\[
 z_y(R)\ge H-d_R\ge8\tau\qquad\text{for every }y\in Y_v,
\]
so the payer cannot be hidden by changing the top functional. Normalize the
actual shallow payer into its synthetic row-hull barycenter \(q_{\rm sh}\).
Exact affine integration gives
\(y\cdot(p_v-q_{\rm sh})\ge8\tau\) for every \(y\in Y_v\), so
\(q_{\rm sh}\ne p_v\) without a point selector or a convexity/Jensen step.
Put \(L_{\rm sh}:=\|p_v-q_{\rm sh}\|_1\ge8\tau\), choose an
\(\ell^1\)-norming sign vector \(s\), and construct
\[
 \chi(x):=\frac{s\cdot(x-q_{\rm sh})}{L_{\rm sh}},
 \qquad \chi(p_v)-\chi(q_{\rm sh})=1.
\]
For the ordered pair \((a,b)=(p_v,q_{\rm sh})\), let
\[
 \ell_{\rm fib}:=
 \sum_R\left|\sum_{k\in R}(a_k-b_k)\right|.
\]
`lem-hx-transverse-moment-identity` gives \(\ell_{\rm fib}>0\). Set
\[
 A_{\rm lev}:=(2\ell_{\rm fib})^{-1}>0,
 \quad \Lambda_{\rm lev}:=D_0/L_{\rm sh},
 \quad N:=\{R:|\chi(p_R)|\le A_{\rm lev}\},
 \quad F:=N^c.
\]
Then \(|\chi(p_R)|\le\Lambda_{\rm lev}\) globally and
\(1-A_{\rm lev}\ell_{\rm fib}=1/2\), so the corrected
`lem-hx-financing-floor` has all inputs constructed and yields
\[
 p_v^+(F)+q_{\rm sh}^+(F)
 \ge \frac{L_{\rm sh}}{2D_0}-2\delta.
\]
Here \(\nu(q_{\rm sh})\le\delta\) follows from
`lem-negpart-subadditive`, nonnegative homogeneity, and the fact that
\(q_{\rm sh}\) is a convex average of rows; this is the legal replacement of
the financing floor's exact term \(-\nu(p_v)-\nu(q_{\rm sh})\) by
\(-2\delta\).
The antecedent center \(c\), R1's visible-ray point \(c_0\), and this norming
construction are independent objects; the creative content of S is to align
the last engine demand with the **actual** R1 ray certificate using the common
\(P_v^+\)-ownership and R2, not to identify the centers.

The exact tallness budgets available for that alignment are
\[
 H(1-\sigma_v)\le\nu_vD_0,
 \qquad
 H(1-\sigma_g)\le(\sigma_v-\sigma_g)\frac\tau4+\nu_vD_0
\]
from `obs-height-collapse` and `lem-halo-collapse`. Neither inequality alone
excludes the shallow counterweight; S must show that the constructed
high-lever compensation contributes quantitatively to one of their left-hand
deficits. If it does, \(H>16\tau\) makes the \(O(\tau)\) demand incompatible
with the \(O(\delta)\) negative budget. The output is one \(y\in Y_v\), never
an average of rowwise supports.

**(c) Honest price.** Difficulty: **creative-hard**. The likeliest death is the
constants fight: mass \(O(\tau S)\) at guaranteed deficit \(8\tau\) pays only
\(O(S\delta)\), and the W54 shallow counterweight of mass
\(\asymp4\tau/(2+4\delta)\) passes all presently scalar caps. Evidence the
node may nevertheless be true is exactly the missing global condition: no such
counterweight has been completed with all-row negativity \(\le\tau^2\), the
owned barycenter, and \(H>16\tau\); both W61 local financer searches failed at
tallness.

**(d) Interface check.** The package center \(c\) is an antecedent witness,
chosen before the one output \(y\). No favorable minimizer of R1 may be
assumed: the proof must work with an attained certificate. The constants do
not divide by \(t^*(v)\), and no hiddenness witness is averaged. The shallow
set is defined by row-point depth, not an index label or coordinate slab. The
predicate is a proper quantitative subclass and its \(\ge\) boundary is owned
here. The constructed pair \((p_v,q_{\rm sh})\) is distinct, so every use of
the corrected `lem-hx-financing-floor` can and must state an explicit
parameter \(A>0\).

**(e) Fallback.** Split the payer into
\(d_R\le\tau/4\) (a halo-collapse-shaped subleaf) and
\(\tau/4<d_R\le H-8\tau\). The latter is the exact interface to
`conj-shallow-counterweight-exclusion` (SL1b); keep it as a named shallow-payer
cell rather than replacing S by coefficient-only LP cleanup.

### C — `conj-w62-scalarizable-cotop-web-exclusion`

**(a) Pinned contract.** Proposed metadata: `status: conjecture`;
`picture: signed delta`; intended deps: R1, R2,
`lem-hx-financing-floor`, `lem-hx-transverse-moment-identity`,
`lem-hx-signed-variation-ledger`, `lem-negpart-subadditive`,
`lem-top-deficit-price`,
`obs-height-collapse`, `lem-halo-collapse`.

> There are universal \(\gamma_C>0\) and \(\delta_C\in(0,1/4]\) with the following
> property. Let \((P,v,A)\) be an L5 datum with
> \(0<\delta\le\delta_C\) and \(S\ge c_m\), satisfying for every
> \(c\in K_v^{\mathrm{loc}}\),
> \[
>  P_v^+(E_c\cap\mathrm{Sh}_v)<\frac1{16}\tau S,
>  \qquad
>  P_v^+(E_c\cap G_v)\ge\frac1{16}\tau S.
> \]
> Define \(\omega_Q:=P_v^+(\{Q\})1_{G_v}(Q)\). If
> \[
>  \|r_\omega-p_v\|_1\ge\frac18
>  \quad\text{or}\quad
>  \Omega(\omega)\ge\frac1{16},
> \]
> then \(Z_v(q_A)\ge\gamma_C\tau\).

**(b) Mechanism sketch.** Failure of the conclusion first gives R1's actual
ray certificate for \(q_A\). The displayed alternatives then construct a
legal engine pair without a row selector. Since the target submeasure is
supported in \(G_v\), \(M_\omega\ge S\ge c_m\), so every normalization below
is legal and retains quantitative top ownership.

In the drift horn take \((a,b)=(r_\omega,p_v)\), whose separation
\(L\ge1/8\). In the width horn, choose an affine \(1\)-Lipschitz
\(\ell\) attaining \(\Omega(\omega)\), split \(\bar\omega\) at
\(\ell(r_\omega)\), and let \(s_\pm,q_\pm\) be the two conditional masses and
barycenters. Exact affine centering gives
\[
 s_+s_-\,\|q_+-q_-\|_1
 \ge s_+s_-\bigl(\ell(q_+)-\ell(q_-)\bigr)
 =\frac12\Omega(\omega)\ge\frac1{32}.
\]
Thus \((a,b)=(q_+,q_-)\) is quantitatively separated, even though no atom has
a mass floor.

For either constructed pair, put \(L:=\|a-b\|_1>0\), choose a norming sign
vector, and set
\[
 \chi(x):=\frac{s\cdot(x-b)}L,
 \quad
 \ell_{\rm fib}:=\sum_R\left|\sum_{k\in R}(a_k-b_k)\right|,
 \quad
 A_{\rm lev}:=(2\ell_{\rm fib})^{-1},
\]
\[
 \Lambda_{\rm lev}:=D_0/L,
 \qquad N:=\{R:|\chi(p_R)|\le A_{\rm lev}\},
 \qquad F:=N^c.
\]
The transverse moment makes \(\ell_{\rm fib}>0\), so \(A_{\rm lev}>0\),
and \(|\chi(p_R)|\le\|p_R-b\|_1/L\le D_0/L=\Lambda_{\rm lev}\)
globally. Since `lem-negpart-subadditive` gives \(\nu(a),\nu(b)\le\delta\),
`lem-hx-financing-floor` yields
\[
 a^+(F)+b^+(F)\ge\frac{L}{2D_0}-2\delta.
\]
Define the actual selected actor flow
\(T_\omega(F):=\sum_Q\omega_QP_Q^+(F)\). Because \(r_\omega\) and
\(q_\pm\) are barycenters of the **same** top-owned
measure \(\omega\), positive-part subadditivity (the sign-reversed form of
`lem-negpart-subadditive`) places their weighted demands below the actual
selected actor flow. In the drift horn, if
\(B:=L/(2D_0)-2\delta\), then
\[
 T_\omega(F)+M_\omega P_v^+(F)\ge M_\omega B,
 \qquad
 T_\omega(F)\le P_v^+(F)+2\delta(1+\delta)
\]
by R2, hence
\((1+M_\omega)P_v^+(F)\ge M_\omega B-2\delta(1+\delta)\).
In the width horn multiply by \(M_\omega s_+s_-\) and use
\[
 s_+s_-\bigl(q_+^+(F)+q_-^+(F)\bigr)
 \le \sum_Q\bar\omega_QP_Q^+(F).
\]
The weighted chord gives the explicit pre-foldback floor
\[
 T_\omega(F)
 \ge M_\omega s_+s_-\left(\frac{L}{2D_0}-2\delta\right)
 \ge \frac{M_\omega}{64D_0}-2M_\omega\delta.
\]
R2 then folds this actual flow back to row \(v\), and the signed-variation
ledger pays each sign union once. The creative remaining
step is to couple that explicit chord demand to R1's ray certificate. The only
tallness budgets allowed in doing so are the exact inequalities
\[
 H(1-\sigma_v)\le\nu_vD_0,
 \qquad
 H(1-\sigma_g)\le(\sigma_v-\sigma_g)\frac\tau4+\nu_vD_0.
\]
The proof must show which chord tail contributes to a left-hand deficit; the
height lemmas do not supply that alignment by themselves.

**(c) Honest price.** Difficulty: **creative-hard**. The likeliest death is a
two-prong co-top crown whose two conditional rows finance each other while the
owned barycenter remains ray-blind—the W55 same-carrier/completion wall in
scalar form. Evidence for C is that W61 now supplies a genuine lower demand,
the pair is constructed on the correct \(P_v^+\)-carrier, and no tall
two-prong completion is known. The drift horn is materially easier and should
be proved or refuted separately inside the same dispatch.

**(d) Interface check.** The scalar-width optimizer is selected only for its
attained value; no coordinate, max-volume tie, or individual atom is chosen.
The exact sign split constructs both endpoints and their ownership before any
engine call. The corrected engine parameters satisfy \(A_{\rm lev}>0\) and
\(1-A_{\rm lev}\ell_{\rm fib}=1/2\). R1's visible point, the local centers,
and the chord center are not identified. The branch is the proper
drift-or-width subclass of the uniform co-top horn.

**(e) Fallback.** Split C into the exact predicates
\(\|r_\omega-p_v\|_1\ge1/8\) and
\(\|r_\omega-p_v\|_1<1/8,\ \Omega(\omega)\ge1/16\). If the latter dies,
retain its explicit weighted-chord package
\(s_+s_-\|q_+-q_-\|_1\ge1/32\); do not replace it by a pointwise selector.

### I — `conj-w62-isotropic-cotop-web-exclusion`

**(a) Pinned contract.** Proposed metadata: `status: conjecture`;
`picture: signed delta`; intended deps: R1, R2,
`lem-hx-transverse-moment-identity`, `lem-hx-signed-variation-ledger`,
`lem-hiddenness-dual-witness`, `lem-always-tight-dual-support`,
`lem-positive-exposedness-margin`, `lem-optimal-face-conic-reduction`,
`lem-cotop-witness-pinning`, `lem-top-deficit-price`,
`obs-height-collapse`, `lem-halo-collapse`.

> There are universal \(\gamma_I>0\) and \(\delta_I\in(0,1/4]\) with the following
> property. Let \((P,v,A)\) be an L5 datum with
> \(0<\delta\le\delta_I\) and \(S\ge c_m\), put
> \(\omega_Q:=P_v^+(\{Q\})1_{G_v}(Q)\), and suppose that for every
> \(c\in K_v^{\mathrm{loc}}\),
> \[
>  P_v^+(E_c\cap\mathrm{Sh}_v)<\frac1{16}\tau S,
>  \qquad
>  P_v^+(E_c\cap G_v)\ge\frac1{16}\tau S,
> \]
> while
> \[
>  \|r_\omega-p_v\|_1<\frac18,
>  \qquad \Omega(\omega)<\frac1{16}.
> \]
> Then \(Z_v(q_A)\ge\gamma_I\tau\).

**(b) Mechanism sketch.** This is the deliberately isolated dual-simplex
package: the top-owned co-top measure escapes every local half-ball, but its
mean does not drift and no affine scalar has enough first absolute moment to
produce C's weighted chord. Again \(M_\omega\ge S\ge c_m\). Suppose the
conclusion fails. R1 supplies one
outward-ray certificate for \(q_A\), while `lem-top-deficit-price` gives the
simultaneous moment cap
\[
 \int z_y\,d\omega\le\delta D_0\qquad\text{for every }y\in Y_v.
\]
Because \(S>0\) supplies a nonempty \(4\tau\)-far set,
`lem-positive-exposedness-margin` gives \(t^*(v)>0\). Hence an optimal reduced
display exists and `lem-cotop-witness-pinning` supplies the second,
dual-required co-top measure (more than \(13/16\) of its \(\lambda\)-mass in
\(G_v\)). This witness is used only as geography.

The proposed proof is a whole-measure transport dual: combine the unit
transverse moments for the explicit distinct pairs
\((p_v,p_Q)\), \(Q\in\operatorname{supp}\omega\), integrate them against the
quotient measure \(\bar\omega\), combine the resulting sign unions with
`lem-hx-signed-variation-ledger`, R2's top-owned flow, and
the two exact tallness inequalities
\[
 H(1-\sigma_v)\le\nu_vD_0,
 \qquad
 H(1-\sigma_g)\le(\sigma_v-\sigma_g)\frac\tau4+\nu_vD_0
\]
to show that the ray certificate and uniform exterior floor cannot coexist.
Unlike C, I must **not** invoke `lem-hx-financing-floor` on
\((p_v,r_\omega)\) after letting the separation vanish. Its missing theorem is
precisely that an isotropic, internally reproducing co-top web cannot globally
complete in the tall regime; the output must be one dual solution \(y\), not
a feasible circuit run backward into exposure.

**(c) Honest price.** Difficulty: **creative-hard, highest-information**. The
likeliest death is an exact high-dimensional sign-cube/dual-simplex plateau
whose common mean is near \(p_v\), scalar width stays below \(1/16\), and the
same web pays every exterior demand. The W55 \(A_0=5,g=5\tau\) gadget is
adverse local evidence but has no tall global completion. Positive evidence is
the repeated W61 signal: both local refuters met their ledgers only after
losing \(H>16\tau\).

**(d) Interface check.** I owns strict low drift and strict low width; C owns
both equality boundaries. The for-all-centers hypothesis precedes the one
existential output \(y\), so no \(y_c\) is selected or averaged. The reduced
witness is small-beta, is never identified with \(P_v^+\), and no constant
uses \(1/t^*(v)\). The node explicitly refuses the illegal equal-endpoint
financing call and never reverses the W37 dual inequality. It is a proper,
quantified isotropic subclass, not a finite-cover claim.

**(e) Fallback.** Split I, conditional on the still-conjectural sibling tools,
by always-tight hull intersection versus disjointness. The disjoint
specialization is a top-owned companion to `conj-cotop-web-coupling` and would
pay toward L6.5; the intersecting specialization must use the whole-measure
engine ledger, not W54's dead witness averaging. A separate conditional
fallback may invoke `conj-summit-cylinder-exclusion` only after adding the
explicit concentration predicate
\(\sup_Q\bar\omega(B_1(p_Q,c_3\tau/2))\ge1/4\); the same one-row support then
serves that one cell by Lipschitzness.

## 2. The assembly implication

Assume R0--R3, S, C, and I with exactly the quantifiers above, with the branch
constant \(c_m\) already fixed. Let R3 supply \(\delta_E\), and let S, C,
and I supply \(\gamma_S,\gamma_C,\gamma_I\) and ceilings
\(\delta_S,\delta_C,\delta_I\). Set
\[
 \gamma:=\min\{\gamma_S,\gamma_C,\gamma_I\}>0,
 \qquad c_5:=\gamma,
\]
and
\[
 \delta_0:=\min\left\{
   \delta_E,\delta_S,\delta_C,\delta_I,2^{-8}
 \right\}>0.
\]
Since \(c_m\) is the already fixed universal W54 branch threshold, this is a
universal ceiling for L5\((c_m)\); the output constant \(c_5\) is independent
of \(c_m\).

Take an arbitrary exact signed idempotent \(P\) with
\(0<\delta\le\delta_0\), nonempty visible set, and hidden top vertex \(v\)
with \(H>16\tau\), and take arbitrary \(A\) satisfying the L5 hypotheses.
Form the full-fiber
submeasure \(m\), its mass \(S\ge c_m\), and \(q_A\). R3 applies because
\(m\le P_v^+\) and its support is \(4\tau\)-far. Hence for every
\(c\in K_v^{\mathrm{loc}}\),
\[
 P_v^+(E_c)\ge\frac18\tau S.
\]
Our ceiling gives \(\tau\le1/16\). If
\(c\in K_v^{\mathrm{loc}}\) and \(Q\in E_c\), then
\[
 \|p_Q-p_v\|_1>\frac12-\frac14=\frac14\ge4\tau.
\]
Thus, on every such \(E_c\), the two fiber sets
\(E_c\cap\mathrm{Sh}_v\) and \(E_c\cap G_v\) are disjoint and exhaustive.

There are now exactly three branches.

1. If some \(c\in K_v^{\mathrm{loc}}\) satisfies
   \(P_v^+(E_c\cap\mathrm{Sh}_v)\ge\frac1{16}\tau S\), S owns the
   equality boundary and gives \(Z_v(q_A)\ge\gamma_S\tau\).
2. Otherwise the shallow mass is strictly less than
   \(\frac1{16}\tau S\) for every local center. Subtracting it from R3's
   \(\frac18\tau S\) floor gives
   \[
    \forall c\in K_v^{\mathrm{loc}},\qquad
    P_v^+(E_c\cap G_v)>\frac1{16}\tau S.
   \]
   Define the nonzero measure \(\omega=P_v^+|_{G_v}\). If
   \(\|r_\omega-p_v\|_1\ge1/8\) or \(\Omega(\omega)\ge1/16\), C owns both
   equality boundaries and gives \(Z_v(q_A)\ge\gamma_C\tau\).
3. In the remaining subcase
   \(\|r_\omega-p_v\|_1<1/8\) and \(\Omega(\omega)<1/16\). I owns exactly
   these two strict inequalities and gives \(Z_v(q_A)\ge\gamma_I\tau\).

In either branch R0 yields
\[
 \sup_{y\in Y_v}\sum_{j\in A}(P_{vj})_+z_y(j)
 =S Z_v(q_A)
 \ge\gamma\tau S
 \ge c_5\tau c_m.
\]
Choose a maximizing \(y\in Y_v\) (compactness), and let
\(\phi_y(x)=y\cdot x-h_C(y)\). By `lem-top-support-dual-face`, this is one
top support functional and
\(z_y(j)=H-\phi_y(p_j)\). This is exactly L5-GAP-1.

The statement-level chain is therefore
\[
 \boxed{\mathrm{R0+R1+R2+R3+S+C+I}\Longrightarrow\mathrm{L5\text{-}GAP\text{-}1}.}
\]
R0 owns the mass-to-one-point conversion; R1 owns the finite ray certificate
for minimax failure; R2 owns same-carrier positive-flow allocation; R3 owns the
dimension-free exterior lower bound; S owns the existential shallow-payer
horn; C owns scalarizable drift/chord in the co-top complement; I owns strict
low-drift, low-width isotropic cancellation. The conditional finite-cover
lemma from `context/l5-answer.md` is not used and is not claimed equivalent.

As a downstream check, combining the resulting L5 bound with
`lem-top-deficit-price` makes the L5 antecedent empty once
\(3\tau<c_5c_m\). Conditional on the still-conjectural
`conj-cotop-web-coupling`, the disjoint/heavy W54 branch supplies a far-deep
mass threshold (the recorded assembly uses a safe value such as
\(c_m=c_*/2\)). L5 would then supply one currently missing premise of the
huddle assembly. This is **not** a consumable downstream DAG edge:
`lem-huddle-charge-assembly` has status `stated` and carries a hostile
`INVALID AS STATED / DO NOT CONSUME` verdict until its other assembly gaps are
repaired.

## 3. Kill-list check

### Node-by-node audit

| Node | Verdict | Audit |
|---|---|---|
| R0 | **PASS** | Uses the exact full-fiber submeasure and one affine barycenter. It explicitly accepts that the barycenter can re-enter the summit cylinder; no pointwise averaging or Jensen inference is made. |
| R1 | **PASS** | Dualizes the actual finite LP over \(Y_v\) and outputs one attained ray certificate. It is neither an exact-max-volume selector nor coefficient-only support cleanup, and no tie property is consumed. |
| R2 | **PASS** | Uses one aggregate application of \(P^2=P\) and sign-union budgets. It is not a raw-index path product, does not call signed coefficients probabilities, and is invariant under clone splitting. |
| R3 | **PASS** | Averages the banked engine only after full-fiber aggregation and uses R2 to prevent a reusable actor payer from being charged repeatedly. There is no dimension, class count, or row selector. |
| S | **PASS (priced)** | Retains the proper shallow-payer package and must construct one common \(y\) through R1. It neither uses the W53 upper charge as a lower bound nor divides by \(t^*\); its constants weakness is stated rather than hidden. |
| C | **PASS (priced)** | Owns the proper drift-or-width subclass and constructs an explicit separated synthetic pair with all corrected financing-floor inputs. No atom mass floor or frame selector is used. |
| I | **PASS (highest risk)** | Owns the strict uniform-web + low-drift + low-width subclass. It explicitly isolates, rather than silently scalarizes, equal-barycenter cancellation; the small-beta witness pins geography only and no W37 reversal or \(1/t^*\) appears. |

### Named walls

- **Raw-index paths / cloning — PASS.** Every measure is a full-row-point-fiber
  aggregate. No floor depends on the number of indices, atoms, vertices, or
  dimensions.
- **Simplex averaging — PASS.** The simplex fan is routed to I as an adverse
  completion shape. R0 asks directly whether its barycenter is visible; no
  sum of pointwise suprema is substituted for a supremum of the mass sum.
- **W53 affine-pairing blind spot — PASS.** `lem-top-deficit-price` is used only
  as an upper budget. The proposed lower input is R3's W61 engine demand plus
  the S/C/I structural predicates.
- **W54 witness averaging — PASS.** No \(y_Q\), no convex average of top
  functionals, and no average of hiddenness witnesses occurs.
- **W54 \(t^*\)-free discipline — PASS.** S and C do not use \(t^*\); I uses
  positive margin only to legalize the small-beta geography and takes no
  reciprocal or quantitative lower bound for \(t^*\).
- **W37 dual-direction wall — PASS.** R1 dualizes the desired primal support
  problem directly. Neither creative node turns an upper bound on exposedness
  into a lower one.
- **Exact-max-volume selectors — PASS.** The only optimization is the actual
  compact/finite LP defining \(Z_v\); an arbitrary attained minimizer must
  work, and no tie is resolved canonically.
- **Jensen — PASS.** R0 is an equality for affine integration. No separation
  of atoms is inferred to survive their barycenter. C's endpoints come from
  an exact affine sign split and a displayed weighted-chord identity.
- **Coefficient-only LP cleanup — PASS.** R1 is only an exact geometric
  representation. S/C/I must additionally consume exact idempotence, signed
  variation, the W61 financing floor, row geometry, and tallness.
- **W56 one-hard-leaf wall — PASS.** R3 first separates the witnessed shallow
  payer S from a uniform co-top web; the latter is then split by the consumed
  quantitative statistics \(\|r_\omega-p_v\|_1\) and \(\Omega(\omega)\).
  C constructs a constant weighted chord, while I retains the strict
  low-drift/low-width isotropic subclass. No creative leaf retains the full
  L5 class after selector bookkeeping.

### Variants killed before entering the tree

1. **FAIL — universal finite cover as the main node.** It is stronger than the
   direct minimax and is vulnerable to a coherent core plus arbitrarily many
   tiny orthogonal fibers. Nothing downstream needs its cover number.
2. **FAIL — `conj-summit-cylinder-exclusion` plus averaging.** The verified
   **abstract simplex obstruction** has pointwise value one and uniform mass
   value \(1/m\); no in-class exact signed-idempotent realization is claimed.
   Averaging the \(y_Q\)'s or pigeonholing without a universal cover re-walks
   W54 exactly.
3. **FAIL — summing E5 pairwise demands without R2.** The same \(P_v^+\)-payer
   or disjoint actor-row leaks may pay every pair. R2 is mandatory before any
   aggregate lower bound is read.
4. **FAIL — identify the hiddenness witness with \(P_v^+\).** Common co-top
   localization does not give coefficient overlap, and \(\lambda P\ne p_v\).
5. **FAIL — choose a favorable ray minimizer.** R1 supplies existence but no
   tie structure. Any S/C/I proof depending on a selected exact-max-volume or
   minimal-support certificate is killed.
6. **FAIL — lexicographic minimal counterexample, transient-row censoring, or
   second-web recursion.** None consumes the S/C/I predicates, and all three
   are covered by W56's death certificates.

## 4. Recommended dispatch order

1. **Routine batch first: R0, R1, R2, then R3.** These are af-elevation-shaped
   single contracts. R0 and R1 need a short finite-LP hostile pass; R2 needs a
   symbolic sign audit on arbitrary full fibers; R3 should then be checked at
   the exact intermediate inequality before the clean \(1/8\) corollary is
   attempted. Clone-split every algebra fixture.

2. **Cheap L3 deciders before creative spend.** Every genuine refuter family
   must have exact \(P^2=P\), all row sums one, \(\delta_k\to0\), nonempty
   \(W(P_k)\), and \(H_k>16\tau_k\); a short local gadget is evidence only.

   - **Heavy summit-axis spike:** one far-deep fiber with
     \(P_v^+\)-mass at least \(c_m\) and
     \(Z_v(p_Q)/\tau\to0\). This is the cheapest one-actor attack on both
     creative horns.
   - **Shallow-counterweight completion (S):** attach the W54 shallow payer to
     the W61 dyadic leak-financer in factorized coordinates \(P=LB,BL=I\),
     force its receiver into \(E_c\cap\mathrm{Sh}_v\), and sweep
     \(H/\tau\downarrow16\).
   - **Two-prong engine-financing bouquet (C):** make opposing co-top actors
     share one reusable exterior payer while keeping \(q_A\) on the summit
     axis; this attacks the same-carrier step after R3.
   - **Growing low-width dual-simplex fan (I):** use
     \(m=3,4,8,\ldots\) far-deep fibers
     of mass \(\asymp c_m/m\), require the true normalized LP value
     \(Z_v(q_A)/\tau\to0\), enforce the for-all-local-centers co-top floor,
     and check both \(\|r_\omega-p_v\|_1<1/8\) and
     \(\Omega(\omega)<1/16\).
   - **Tall completions of the known seeds:** separately try the W61 thin
     transient graft, its dyadic leak-financer, and the W55
     \(A_0=5,g=5\tau\) plateau. A completion that preserves all-row
     negativity and tallness kills or sharply restates I; failure again at
     tallness is positive but non-rigorous evidence.

3. **Creative nodes last: dispatch I, then C, then S.** I has the highest
   information value: a refuter is a direct exact realization of the
   low-width dual-simplex threat and informs
   `conj-cotop-web-coupling`/L6.5. C is next because its drift horn and explicit
   weighted chord give fast prove-or-refute lanes. Dispatch S with the actual
   constants certified by R3. If S's scalar constants fail, split halo versus
   intermediate depth immediately and hand the latter to the registered SL1b
   surface.
