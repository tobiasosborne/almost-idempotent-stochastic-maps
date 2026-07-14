conj-w67-aesc-synthetic-finance-tail-amplification: VALID

conj-w67-aesc-synthetic-finance-tail-amplification-fixed-K: VALID

conj-w67-aesc-guarded-hull-split: VALID

conj-w67-aesc-common-tail-union: VALID

conj-w67-aesc-hull-exterior-separation-geography: VALID-WITH-CORRECTION

## SF — `conj-w67-aesc-synthetic-finance-tail-amplification`

The proof does not consume the conclusion of
`lem-hx-robust-scalar-starvation`. It consumes
`lem-dcap-five-way-completion-split` only for the normalized-carrier facts

\[
 \widetilde q_u\in K(P),\qquad
 D_u=\widetilde q_u-p_u,\qquad
 \tau/2\le\|D_u\|_1\le2\tau,\qquad a_u\ge4,
\]

and \(a_uD_u=k_{O,u}-k_{T,u}\). The numerical window (1.4) by itself would
not be enough: hull membership of \(\widetilde q_u\) is essential. That missing
piece is, however, a literal conclusion of the consumed D-cap shard and is
explicitly audited in the appendix.

The complete hypothesis block of `lem-hx-transverse-moment-identity` is met:
\(P\) is a finite exact signed idempotent; \(q_0=p_u\) and
\(q_1=\widetilde q_u\) lie in \(K(P)\); they are distinct because
\(\|D_u\|_1\ge\tau/2>0\); and the affine sign normer satisfies

\[
 \chi_u(p_u)=0,\qquad
 \chi_u(\widetilde q_u)
 =\frac{\operatorname{sgn}(D_u)\cdot D_u}{\|D_u\|_1}=1.
\]

That shard requires no actual finance row, Lipschitz condition, rank, slab, or
I-cap hypothesis. Its fiber difference is exactly \(d_{u,Q}\), so (A.9) is a
legal fresh use of its conclusion. Convexity of negative mass also gives
\(\nu(\widetilde q_u)\le\delta\), the budget used on the negative tail.

For an arbitrary nearest point \(r\in K(P)\), exact idempotence and convexity
give \(rP=r\), \(r\mathbf1=1\), and \(\nu(r)\le\delta\). With
\(e_u=r-(p_u-a_uD_u)=r-p_u+a_uD_u\), one has
\(\|e_u\|_1\le3\delta\) and the correctly signed fiber identity

\[
 r_Q-c_{u,Q}+a_ud_{u,Q}=e_{u,Q}.
\]

No representation coefficient of \(r\) is used as transition mass, no
nearest-point tie is resolved favorably, and no actual-row property beyond
the three synthetic invariants and the displayed identity enters the estimate.

The constant chain is correct:

- Core: \(\sum_{|\chi_u|\le1}|d_{u,Q}|\le\|D_u\|_1\le2\tau\).

- Lever:
  \[
   \frac{D_0}{\tau/2}=\frac{4+8\delta}{\tau}\le\frac6\tau
  \]
  holds exactly when \(\delta\le1/4\). The pinned
  \(\delta\le\delta_{\rm rt}\le2^{-16}\) is more than sufficient.

- Negative tail: the coefficient is at most \(C_u+\delta\), using
  \((-d_{u,Q})_+\le(c_{u,Q})_++(-\widetilde q_{u,Q})_+\).

- Positive tail:
  \[
   \sum_{\chi_u>1}(d_{u,Q})_+
   \le\frac{C_u+\delta+3\delta}{a_u}
   \le\frac{C_u}{4}+\delta.
  \]

Thus

\[
 1\le2\tau+\frac6\tau\left(\frac54C_u+2\delta\right)
   =14\tau+\frac{15}{2\tau}C_u,
\]

because \(12\delta/\tau=12\tau\). Consequently

\[
 C_u\ge\frac{2\tau}{15}(1-14\tau)
 \ge\frac{2\tau}{15}\frac{242}{256}
 =\frac{121}{960}\tau
 >\frac{120}{960}\tau=\frac\tau8.
\]

The signs \(x_u=p_u-a_uD_u\),
\(p_f-x_u=p_f-p_u+a_uD_u\), and \(e_u=r-p_u+a_uD_u\) are consistent
throughout.

## SF-K — `conj-w67-aesc-synthetic-finance-tail-amplification-fixed-K`

The same shard audit applies. Replacing \(\|e_u\|_1\le3\delta\) by
\(\|e_u\|_1\le K\delta\) changes only the positive-tail estimate:

\[
 \sum_{\chi_u>1}(d_{u,Q})_+
 \le\frac{C_u+(K+1)\delta}{a_u}
 \le\frac{C_u}{4}+\frac{K+1}{4}\delta.
\]

Adding the negative-tail \(C_u+\delta\), applying the \(6/\tau\) lever, and
adding the \(2\tau\) core gives exactly

\[
 1\le\frac{3K+19}{2}\tau+\frac{15}{2\tau}C_u,
\]

so

\[
 C_u\ge\frac{2\tau}{15}
       \left(1-\frac{3K+19}{2}\tau\right).
\]

At \(\tau\le1/(3K+19)\), the parenthesis is at least \(1/2\), including
equality at the ceiling, and hence \(C_u\ge\tau/15\). The equivalent added
defect ceiling is \(\delta\le(3K+19)^{-2}\). The estimate is uniform over all
nearest points.

## HS — `conj-w67-aesc-guarded-hull-split`

The fixed display field determines \(D_u,a_u,x_u\) before \(h_u\) is
measured. The predicates

\[
 h_u>3\delta,\qquad h_u\le3\delta
\]

are a disjoint exhaustive partition of \(\mathsf A_{\rm esc}\), with
\(h_u=3\delta\) owned by \(\mathsf D_{\rm tail}\). Therefore

\[
 \eta_D^*(\mathsf D_{\rm tail})
 \ge\frac1{80}-\eta_D^*(\mathsf H_{\rm out})
 >\frac1{160}
\]

under the strict failure guard. If
\(\eta_D^*(\mathsf H_{\rm out})=1/160\), the guard does not fire, so mass
equality is owned by HES exactly as declared. No shard is consumed.

## TU — `conj-w67-aesc-common-tail-union`

The aggregation direction is correct. For every fiber \(R\),

\[
 (c_{u,R})_+=\left(\sum_{j\in R}P_{uj}\right)_+
 \le\sum_{j\in R}(P_{uj})_+.
\]

Every tail fiber with positive aggregate belongs to \(\mathcal U_B\), so the
safe consequence is

\[
 \operatorname{Tail}_1(u)\le P_u^+(\mathcal U_B),
\]

not the reverse. This is the direction used in (A.24)--(A.25).

The source \(m=\eta_D^*|_B\) is a nonnegative full-fiber measure because
\(B\) is a union of carrier fibers, and `lem-dcap-root-closure` gives the
literal pointwise domination

\[
 0\le m_Q\le\eta_D^*(Q)\le P_{f^*}^+(Q).
\]

Thus `lem-l5-positive-flow-foldback` applies exactly once, with the one common
test \(g=\mathbf1_{\mathcal U_B}\in[0,1]\). There is no family of
carrier-dependent tests and no summed pairwise error. Its left side is the
\(\eta_D^*|_B\)-weighted positive outflow to the same common receiver set.
Since the source space is finite, the pointwise strict SF bound and
\(\eta_D^*(B)>1/160\) yield

\[
 \int_B P_u^+(\mathcal U_B)\,d\eta_D^*(u)>\frac\tau{1280}.
\]

The ceiling arithmetic is also correct. At \(c_m=1/4\) and \(b=1/512\),

\[
 \frac{c_mb}{120}=\frac1{245760}
 =\frac{c_m^2}{15360}.
\]

This is the smallest square-root component of \(\delta_{\rm rt}\), so
\(\tau\le1/245760\). In particular

\[
 \frac{e_\delta}{\tau}=2\tau(1+\tau^2)<4\tau
 \le\frac1{61440}<\frac1{2560},
\]

and hence \(e_\delta<\tau/2560\). Therefore

\[
 P_{f^*}^+(\mathcal U_B)
 >\frac\tau{1280}-e_\delta>\frac\tau{2560}.
\]

The strategist's original formula
\(\tau\le c_m^2/15360<1/15360\) is not wrong: at \(c_m=1/4\) its first
quantity is exactly \(1/245760\). Nothing in the strategy depends on replacing
that sharper value by \(1/15360\).

## SEP — `conj-w67-aesc-hull-exterior-separation-geography`

The proof validates the following corrected statement:

> For every \(u\in\mathsf H_{\rm out}\), there exists an affine functional
> \(\psi_u\), with linear part \(\overline\psi_u\) satisfying
> \(\|\overline\psi_u\|_\infty\le1\), such that
> \[
>  \psi_u(x_u)-\sup_{r\in K(P)}\psi_u(r)=h_u,\qquad
>  -a_u\overline\psi_u(D_u)\ge h_u>3\delta.
> \]

The exact failing line of the original strategy is `AESC-ATTACK.md` (1.20):

> \[
>  -a_u\,\psi_u(D_u)\ge h_u>3\delta.
> \]

There \(\psi_u\) was declared affine. Applying an affine functional itself to
a displacement is not invariant under adding an affine constant: the gap in
(1.19) is unchanged, while the literal value \(\psi_u(D_u)\) changes. The
appendix silently changes this to the action of the linear part. That change is
necessary, so the literal original is not VALID without correction.

With the correction, the proof is sound. Weak separation of \(K(P)\) from the
open \(\ell^1\)-ball of radius \(h_u\) about \(x_u\), followed by dual-norm
normalization, gives a linear \(L\) with \(\|L\|_\infty=1\) and gap at least
\(h_u\). Hölder's inequality bounds that gap above by the distance \(h_u\), so
equality holds. Since \(p_u\in K(P)\) and \(x_u-p_u=-a_uD_u\),

\[
 h_u\le L(x_u-p_u)=-a_uL(D_u).
\]

The separator is chosen only after \(u\) is fixed and is neither averaged nor
summed across carriers.

## CROSS-CUTTING

### Shard and hypothesis discipline

The seven registered D-cap shards are
`lem-dcap-root-closure`, `lem-dcap-score-bulk-transfer`,
`lem-dcap-kernel-bulk-census`, `lem-dcap-common-ownership`,
`lem-dcap-tall-same-center-packet`, `lem-dcap-closed-overlay`, and
`lem-dcap-five-way-completion-split`. Their common D-cap hypothesis block is
the pinned antecedent: the finite exact signed idempotent and I-base data, the
two all-center local clauses, the strict coarse drift/width bounds, the
\(\delta_{\rm rt}\) ultra/rim block, the same exhibited certificate with
\(M_X\le1/8\), \(M_I<1/16\), \(M_D>1/16\), and the prescribed
kernel/display quantifier order. Of these, the routine proofs directly use only
`lem-dcap-five-way-completion-split` for normalized-carrier clauses and
`lem-dcap-root-closure` for full-fiber domination. The other five outputs are
retained background data but no conclusion from them is used in SF, SF-K, HS,
TU, or SEP. No `lem-icap-*` shard is consumed.

The synthetic-finance proofs do not cite the actual-finance-row starvation
conclusion, even indirectly as an estimate. They reconstruct the unit moment
from `lem-hx-transverse-moment-identity` and then perform the complete sign
split with the synthetic nearest point. TU makes one new foldback call; the
registered proof history of R0 is not duplicated as a second call in TU.

### Quantifiers, ownership, signs, and boundaries

The certificate, legal kernel, and arbitrary reduced-display field remain
fixed in the inherited order. In particular the display field is fixed before
\(h_u\), \(\operatorname{Tail}_1(u)\), \(B\), or \(\mathcal U_B\) is
measured. Nearest hull points are arbitrary. The HES mass boundary \(1/160\)
belongs to HES, while \(h_u=3\delta\) belongs to the hull-near/D-tail class.
The separator may depend on \(u\), but no proof commonizes it.

All target signs agree with

\[
 a_uD_u=k_{O,u}-k_{T,u},\qquad
 x_u=p_u-a_uD_u=p_u+k_{T,u}-k_{O,u}.
\]

Thus the A-esc residual is \(p_f-x_u=p_f-p_u+a_uD_u\), the synthetic error is
\(r-x_u=r-p_u+a_uD_u\), and the separation displacement is
\(x_u-p_u=-a_uD_u\). No SF or SEP line reverses these signs.

### Clone invariance and walls

Under compatible row cloning, the full-fiber lift preserves row-point
\(\ell^1\) geometry and the row hull, hence \(h_u\). It preserves the sign
normer's scalar values, while \(\operatorname{Tail}_1(u)\) uses the positive
part only after the clone coordinates have been recombined into full-fiber
aggregates. The definition of \(\mathcal U_B\) uses only those aggregates,
row-point values, and a full-fiber existential quantifier. The thresholds
\(3\delta\), \(\tau/8\), \(\tau/15\), and \(\tau/2560\) depend only on
clone-invariant \(\delta\) and fixed universal constants. Every public
quantity in the batch is therefore clone-invariant.

No proof uses a raw-index floor, stochastic reading of signed coefficients,
favorable selection, conic recurrence, witness averaging, finite directional
cover, coefficient-only cleanup, spectral import, failed-census emptiness,
second web, or B5/R0 carrier identification. SEP proves only the standard
per-carrier distance-duality geography; it does not resurrect the dead
"literal psi-gap" route by turning those rotating normals into a common test or
an EC bound. Thus the FINDINGS walls and K1--K12 are respected.

Finally, SEP is only the geography (1.19)--(1.20). It does not prove the
creative HES synchronization contract
`conj-w67-aesc-hull-exterior-separator-synchronization`; no such promotion is
made here.
