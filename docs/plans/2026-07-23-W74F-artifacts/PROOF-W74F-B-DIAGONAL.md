STATUS: UNVERIFIED PROVER OUTPUT

# W74F-B — exact whole-algebra diagonal repair and use-site recheck

## Scope and headline

The SHA256 I recomputed for
`refs/kitaev-2405.02434/approximate_algebras.tex` is

```text
e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb
```

which is the digest specified in the brief.

The identified flaw is **confirmed**.  The smallest example is
\(\mathcal B=\mathbb C\oplus\mathbb C\): the printed Cartesian product
formula is normalized, but it is not central.  Thus it is not a diagonal.

There is an exact finite repair.  Start with a finite unitary diagonal in
each matrix block and independently multiply the unitary in block \(r\)
by a sign \(\varepsilon_r\in\{\pm1\}\), averaging uniformly over all sign
vectors.  The exact moment
\[
  2^{-m}\sum_{\varepsilon\in\{\pm1\}^m}\varepsilon_r\varepsilon_k
  =\delta_{rk}
\]
deletes every cross-block tensor.  The resulting whole-algebra diagonal
is a finite convex combination of \(W^\dagger\otimes W\) with \(W\)
unitary.  Its projective norm, and the coefficient sum actually used
downstream, are exactly \(1\), independently of the number and sizes of
the blocks.

The repaired object is a diagonal of the **exact finite-dimensional
\(C^*\)-algebra \(\mathcal B\)**.  No diagonal of the approximate algebra
\(\mathcal A\) is constructed or assumed anywhere in this repair.

With this exact central diagonal, the CP-ization of \(\widetilde\Delta\)
works entrywise.  It uses preservation of the involution by
\(\widetilde\Delta\), but it does **not** use exact multiplicativity of
\(\widetilde\Delta\).  The repair uses no projection onto the CP cone and
causes no change in any downstream constant.

## 1. Byte-verbatim source record

The source defines a diagonal as follows:

> `tex:480`  
> `An associative algebra $\calA$ has trivial Hochschild cohomology if there is a \emph{diagonal}, i.e.\ an element $D=\sum_{j}A_j\otimes B_j\in\calA\otimes\calA$ satisfying the equations $\sum_{j}A_j\otimes B_jX=\sum_{j}XA_j\otimes B_j$ for all $X\in\calA$ and $\sum_{j}A_jB_j=I$. Indeed, in this case, an arbitrary cocycle $h$ is the coboundary of this $g$:`

The source identifies the relevant tensor norm:

> `tex:1228-1232`  
> `The proof involves the concept of a diagonal. Let us give its general definition for completeness, and then specialize to the finite-dimensional case. For arbitrary Banach algebras $\calA$ and $\calB$, the projective tensor product $\calA\hotimes\calB$ is also a Banach algebra. In more detail, $\calA\hotimes\calB$ is the completion of $\calA\otimes\calB$ endowed with the projective tensor norm,`  
> `\begin{equation}`  
> `\|C\|=\inf\biggl\{\sum_{j}\|A_j\|\ts\|B_j\|:\,`  
> `\sum_{j}A_j\otimes B_j=C\biggr\}\qquad (A_j\in\calA,\,\: B_j\in\calB),`

The exact identities are restated at:

> `tex:1233-1242`  
> `For arbitrary $\tilde{D}=\sum_{j}A_j\otimes B_j\in\calB\otimes\calB$ and $X\in\calB$, we write`  
> `\begin{equation}`  
> `X\tilde{D}=\sum_{j}XA_j\otimes B_j,\qquad`  
> `\tilde{D}X=\sum_{j}A_j\otimes B_jX,\qquad`  
> `\pi(\tilde{D})=\sum_{j}A_jB_j.`  
> `\end{equation}`  
> `These operations extend from $\calB\otimes\calB$ to $\calB\hotimes\calB$. An element $D\in\calB\hotimes\calB$ is called a \emph{diagonal} if`  
> `\begin{equation}`  
> `XD=DX\quad\text{for all }\, X\in\calB,\qquad \pi(D)=I_\calB.`

The source already gives the correct whole-unitary-group construction
and its finite norm-one representation:

> `tex:1245-1248`  
> `Every finite-dimensional $C^*$ algebra has a standard diagonal, $D=\int dU\, (U^\dag\otimes U)$, where the integral is taken with respect to the Haar measure on the unitary group. Note that $\|D\|=1$ because the integral can be approximated by finite sums, i.e.\ convex combinations of $U^\dag\otimes U$. Due to Caratheodory's theorem and the compactness of the unitary group, $D$ itself is representable as such a convex combination. Thus,`  
> `\begin{equation}\label{finite_diag}`  
> `D=\sum_jA_j\otimes B_j,\qquad \sum_j\|A_j\|\ts\|B_j\|=1.`

The first false direct-sum formula is printed verbatim at:

> `tex:1254`  
> `where $\braket{e_l}{S_{jk}e_m}$ are the matrix elements of $S_{jk}$ in some orthonormal basis $\{e_0,\dots,e_{d-1}\}$. The diagonal of $\bigoplus_{l=1}^{m}\Bo(\CC^{d_l})$ is obtained by combining the component diagonals $D_l=\sum_j p_{lj}\ts U_{lj}^\dag\otimes U_{lj}$ into a sum over $j=(j_1,\dots,j_m)$ with $p_{j_1,\dots,j_m}=p_{1j_1}\cdots p_{mj_m}$ and $U_{j_1,\dots,j_m}=U_{1j_1}\oplus\cdots\oplus U_{mj_m}$.`

It is repeated at the factorization use site:

> `tex:2771-2783`  
> `Since $\calB$ is a finite-dimensional $C^*$ algebra, $\calB=\bigoplus_{j=1}^{m}\Bo(\calL_j)$ (up to an isomorphism). Let us represent the diagonal of $\Bo(\calL_j)$ as a unitary $1$-design, i.e. $D_j=\sum_{s}p_{js}\ts U_{js}^\dag\otimes U_{js}\in\Bo(\calL_j)\otimes\Bo(\calL_j)$, where`  
> `\begin{gather}`  
> `\label{diag_j01}`  
> `p_{js}\ge 0,\quad\: \sum_{s}p_{js}=1,\qquad U_{js}^{\dag}U_{js}=1_{\calL_j},\\[2pt]`  
> `\label{diag_j2}`  
> `\sum_{s}p_{js}\ts XU_{js}^{\dag}\otimes U_{js}`  
> `=\sum_{s}p_{js}\ts U_{js}^{\dag}\otimes U_{js}X\quad\:`  
> `\text{for all }\, X\in\Bo(\calL_j).`  
> `\end{gather}`  
> `(See \eqref{Pauli_diag} for an explicit example.) The diagonal of the entire algebra $\calB$ is $D=\sum_{s}p_{s}\ts U_{s}^\dag\otimes U_{s}$, where $s=(s_1,\dots,s_m)$,`  
> `\begin{equation}`  
> `p_{s_1,\dots,s_m}=p_{1s_1}\cdots p_{ms_m},\qquad`  
> `U_{s_1,\dots,s_m}=U_{1s_1}\oplus\cdots\oplus U_{ms_m}.`

The CP-ization use site is:

> `tex:2786-2801`  
> `Now, we define a map $\Delta'\colon\calB\to\Bo(\calH)$ by the equation`  
> `\begin{equation}`  
> `\Delta'(X)=\sum_{s}p_{s}\ts\Phi\bigl(\wt{\Delta}(XU_{s}^{\dag})\ts\wt{\Delta}(U_{s})\bigr)`  
> `=\sum_{s}p_{s}\ts\Phi\bigl(\wt{\Delta}(U_{s}^{\dag})\ts\wt{\Delta}(U_{s}X)\bigr)\qquad (X\in\calB).`  
> `\end{equation}`  
> `It is evident that $\Delta'$ commutes with the involution. The complete positivity is shown as follows: if $X\in 1_{\Ma{n}}\otimes\calB$ is positive, it can be represented as $Y^{\dag}Y$, and`  
> `\[`  
> `\Delta'_n(Y^{\dag}Y)`  
> `=\sum_{s}p_{s}\ts\Phi_n\bigl(\wt{\Delta}_n(Y^{\dag}(I_n\otimes U_{s}^{\dag}))\,`  
> `\wt{\Delta}_n((I_n\otimes U_{s})Y)\bigr)\ge 0.`  
> `\]`  
> `Due to equation \eqref{tilde_Del2}, we have $\Delta'_n(X)=\wt{\Delta}_n(X)+O(\eta)\ts\|X\|$ for all $X\in 1_{\Ma{n}}\otimes\calB$, implying that $\|\Delta'-\wt{\Delta}\|_\cb\le O(\eta)$. And using \eqref{tilde_Del1}, we conclude that`  
> `\begin{equation}`  
> `\Delta\colon X\mapsto (\Delta'(I_\calB))^{-1/2}\ts\Delta'(X)\ts(\Delta'(I_\calB))^{-1/2}`  
> `\end{equation}`  
> `is a UCP map such that $\|\Delta-\wt{\Delta}\|_\cb\le O(\eta)$.`

The exact-algebra/approximate-algebra distinction is explicit in the
error-reduction discussion:

> `tex:490`  
> `The second problem is to control errors. We must make sure that $v$ is a $\delta_0$-inclusion for some fixed $\delta_0=O(\eps)$. Simply extending the current $v$ to a new, larger $\calB$ gives a $\delta$-inclusion for $\delta$ greater than $\delta_0$. Thus, we need the following \emph{error reduction} result (Corollary~\ref{cor_improvement}): if there exists a $\delta$-inclusion of a finite-dimensional $C^*$ algebra $\calB$ into an $\eps$-$C^*$ algebra $\calA$ for $\delta$ less than a certain constant, then there is also an $\delta_0$-inclusion, where $\delta_0=O(\eps)$ does not depend on $\delta$. This can be shown by cohomological methods because $\calB$ does have a diagonal. Similar results are found in the literature; they are concerned with the existence of a $C^*$ subalgebra near an approximate $C^*$ subalgebra~\cite{Chr80} and a homomorphism of $C^*$ algebras near an approximately multiplicative map~\cite{Joh88}. Our argument is similar to the proof of Theorem~3.1 in~\cite{Joh88} but actually simpler due to the finite dimensionality condition.`

Thus the diagonal there belongs to the exact domain \(\mathcal B\), not
to the approximate target \(\mathcal A\).

## 2. Smallest counterexample to the printed formula

Let
\[
 \mathcal B=\mathbb C\oplus\mathbb C,\qquad
 e_1=(1,0),\quad e_2=(0,1).
\]
Each block is \(\mathbb C\).  Choose in each block the one-point unitary
design with unitary \(1\) and weight \(1\).  The formula printed at
`tex:1254` and `tex:2780-2783` then has only the whole-algebra unitary
\[
 U=(1,1)=e_1+e_2
\]
and produces
\[
\begin{aligned}
 D_{\rm print}
  &=U^\dagger\otimes U\\
  &=e_1\otimes e_1+e_1\otimes e_2
    +e_2\otimes e_1+e_2\otimes e_2.
\end{aligned}
\]

Take \(Z=e_1\).  Multiplication on the first and second tensor factors
gives
\[
\begin{aligned}
 ZD_{\rm print}
   &=e_1\otimes e_1+e_1\otimes e_2,\\
 D_{\rm print}Z
   &=e_1\otimes e_1+e_2\otimes e_1.
\end{aligned}
\]
The tensors \(e_r\otimes e_k\) are the four coordinate basis elements of
\(\mathcal B\otimes\mathcal B\), so these two elements are unequal.
Centrality fails.

Normalization does hold:
\[
 \pi(D_{\rm print})=U^\dagger U=(1,1)=I_{\mathcal B}.
\]
In fact, normalization holds for every instance of the printed formula,
because every joint \(U_s\) is unitary and the weights sum to \(1\).
The defect is specifically the survival of cross-block terms and hence
the loss of centrality.

This is the smallest possible algebraic example: the only
one-dimensional unital finite-dimensional \(C^*\)-algebra is
\(\mathbb C\), which has one block and hence no cross-block term.

## 3. Standalone finite repair lemma

### Lemma (finite phase-balanced whole-algebra diagonal)

Let
\[
 \mathcal B=\bigoplus_{r=1}^{m}M_{d_r}.
\]
There are finitely many unitaries \(W_t\in\mathcal B\) and weights
\(q_t\ge0\), \(\sum_tq_t=1\), such that
\[
 D_{\mathcal B}:=\sum_tq_t\,W_t^\dagger\otimes W_t
\]
satisfies exactly
\[
 ZD_{\mathcal B}=D_{\mathcal B}Z\quad(Z\in\mathcal B),
 \qquad
 \pi(D_{\mathcal B})=I_{\mathcal B}.
\]
Moreover, for the projective tensor norm,
\[
 \|D_{\mathcal B}\|_\pi=1,
 \qquad
 \sum_tq_t\|W_t^\dagger\|\,\|W_t\|=1.
\]
These bounds are independent of \(m\), all \(d_r\), and
\(\dim\mathcal B\).

### Proof

For each block \(M_{d_r}\), first form its Haar diagonal
\[
 D_r=\int_{\mathcal U(d_r)}U^\dagger\otimes U\,d\mu_r(U).
\]
For a unitary \(V\in M_{d_r}\), right invariance of Haar measure and the
substitution \(W=UV^\dagger\) give
\[
\begin{aligned}
 VD_r
 &=\int VU^\dagger\otimes U\,d\mu_r(U)\\
 &=\int W^\dagger\otimes WV\,d\mu_r(W)
 =D_rV.
\end{aligned}
\]
Every matrix is a linear combination of unitaries, so this proves
centrality for every \(V\in M_{d_r}\).  For completeness, if \(H=H^\dagger\)
and \(\|H\|\le1\), then
\[
 H=\frac12\left(H+i(I-H^2)^{1/2}\right)
   +\frac12\left(H-i(I-H^2)^{1/2}\right)
\]
is the average of two unitaries; decompose a general matrix into real
and imaginary self-adjoint parts and rescale.  Also,
\[
 \pi(D_r)=\int U^\dagger U\,d\mu_r(U)=I_{d_r}.
\]

The compact orbit
\(\{U^\dagger\otimes U:U\in\mathcal U(d_r)\}\) lies in a
finite-dimensional real vector space.  Its Haar barycenter therefore
belongs to its convex hull, and Carathéodory gives an exact finite
representation
\[
 D_r=\sum_{\alpha\in S_r}p_{r\alpha}\,
       U_{r\alpha}^\dagger\otimes U_{r\alpha},
 \qquad
 p_{r\alpha}\ge0,\quad\sum_{\alpha\in S_r}p_{r\alpha}=1.
\]

Now take
\[
 \alpha=(\alpha_1,\ldots,\alpha_m)\in\prod_rS_r,\qquad
 \varepsilon=(\varepsilon_1,\ldots,\varepsilon_m)\in\{\pm1\}^m
\]
and set
\[
\begin{aligned}
 W_{\alpha,\varepsilon}
   &:=\bigoplus_{r=1}^m\varepsilon_rU_{r\alpha_r},\\
 q_{\alpha,\varepsilon}
   &:=2^{-m}\prod_{r=1}^mp_{r\alpha_r}.
\end{aligned}
\]
Every \(W_{\alpha,\varepsilon}\) is a unitary of \(\mathcal B\), the
family is finite, the weights are nonnegative, and
\(\sum_{\alpha,\varepsilon}q_{\alpha,\varepsilon}=1\).

Let \(\iota_r:M_{d_r}\to\mathcal B\) be the block inclusion.  Expanding
the tensor gives
\[
\begin{aligned}
 D_{\mathcal B}
 &=\sum_{\alpha,\varepsilon}q_{\alpha,\varepsilon}
   \sum_{r,k}\varepsilon_r\varepsilon_k\,
   \iota_r(U_{r\alpha_r}^\dagger)
      \otimes\iota_k(U_{k\alpha_k})\\
 &=\sum_{r,k}
   \left(2^{-m}\sum_{\varepsilon}\varepsilon_r\varepsilon_k\right)
   \sum_\alpha\left(\prod_\ell p_{\ell\alpha_\ell}\right)
   \iota_r(U_{r\alpha_r}^\dagger)
      \otimes\iota_k(U_{k\alpha_k})\\
 &=\sum_{r=1}^m(\iota_r\otimes\iota_r)(D_r).
\end{aligned}
\]
The last equality is exactly the sign moment
\[
 2^{-m}\sum_\varepsilon\varepsilon_r\varepsilon_k
 =\begin{cases}1,&r=k,\\0,&r\ne k.\end{cases}
\]
Thus every cross-block term in the printed Cartesian product has been
deleted.

If \(Z=\bigoplus_rZ_r\), then blockwise centrality gives
\[
\begin{aligned}
 ZD_{\mathcal B}
 &=\sum_r(\iota_r\otimes\iota_r)(Z_rD_r)\\
 &=\sum_r(\iota_r\otimes\iota_r)(D_rZ_r)
 =D_{\mathcal B}Z.
\end{aligned}
\]
Similarly,
\[
 \pi(D_{\mathcal B})
 =\bigoplus_r\pi(D_r)
 =\bigoplus_rI_{d_r}
 =I_{\mathcal B}.
\]

Finally, the displayed finite unitary representation gives
\[
\|D_{\mathcal B}\|_\pi
\le\sum_{\alpha,\varepsilon}q_{\alpha,\varepsilon}
  \|W_{\alpha,\varepsilon}^\dagger\|
  \|W_{\alpha,\varepsilon}\|
=1.
\]
The multiplication map
\(\pi:\mathcal B\widehat\otimes_\pi\mathcal B\to\mathcal B\) is
contractive, because
\(\|AB\|\le\|A\|\|B\|\).  Hence
\[
 1=\|I_{\mathcal B}\|
  =\|\pi(D_{\mathcal B})\|
  \le\|D_{\mathcal B}\|_\pi.
\]
Therefore \(\|D_{\mathcal B}\|_\pi=1\), as claimed. \(\square\)

### What is and is not dimension-free

The number of terms in this finite representation can grow with the
block data.  No downstream estimate counts terms: every estimate uses
the probability weights, equivalently the coefficient sum
\(\sum_tq_t\|W_t^\dagger\|\|W_t\|=1\).  Thus the quantity actually used
downstream is exactly dimension-free.

The construction is performed only for the exact algebra
\(\mathcal B=\bigoplus_rM_{d_r}\).  The source warns about trying to
construct a diagonal in an approximate algebra:

> `tex:484`  
> `For finite-dimensional $C^*$ algebras, a diagonal can be obtain as $D=\int dU\, (U^\dag\otimes U)$, where the integral is taken with respect to the Haar measure on the unitary group. Unfortunately, naive constructions of the Haar measure (or just the diagonal) in the $\eps$-associative setting have error bounds proportional to $n=\dim\calA$. So the outlined procedure of fixing the multiplication works only if $\eps<cn^{-1}$ for some constant $c$.`

This repair does not enter that approximate-algebra construction.

## 4. CP-ization re-proved from the repaired diagonal

### 4.1 Exact positivity; no multiplicativity is used

Write the repaired diagonal as
\[
 D_{\mathcal B}=\sum_tq_tW_t^\dagger\otimes W_t.
\]
Define
\[
 \Delta'(X)
 =\sum_tq_t\,
   \Phi\!\left(
     \widetilde\Delta(XW_t^\dagger)\widetilde\Delta(W_t)
   \right).
\]
Centrality, followed by the bilinear map
\[
 a\otimes b\longmapsto
 \Phi\!\left(\widetilde\Delta(a)\widetilde\Delta(b)\right),
\]
also gives
\[
 \Delta'(X)
 =\sum_tq_t\,
   \Phi\!\left(
     \widetilde\Delta(W_t^\dagger)\widetilde\Delta(W_tX)
   \right).
\]
This proves the equality between the two expressions printed at
`tex:2788-2789`.

For complete positivity, fix \(n\) and
\(Y=(Y_{bc})\in M_n\otimes\mathcal B\).  The \((a,c)\)-entry obtained
from the first definition is
\[
 \sum_{b,t}q_t\,
 \Phi\!\left(
 \widetilde\Delta(Y_{ba}^\dagger Y_{bc}W_t^\dagger)
 \widetilde\Delta(W_t)\right).
\]
For each \(b,a,c\), exact centrality applied to \(Z=Y_{bc}\), followed
by left multiplication by \(Y_{ba}^\dagger\) in the first tensor
factor, says
\[
\sum_tq_t\,
Y_{ba}^\dagger Y_{bc}W_t^\dagger\otimes W_t
=
\sum_tq_t\,
Y_{ba}^\dagger W_t^\dagger\otimes W_tY_{bc}.
\]
Applying the displayed bilinear map transforms the \((a,c)\)-entry
into
\[
 \sum_{b,t}q_t\,
 \Phi\!\left(
 \widetilde\Delta(Y_{ba}^\dagger W_t^\dagger)
 \widetilde\Delta(W_tY_{bc})\right).
\]
Because \(\widetilde\Delta\) commutes with the involution,
\[
 \widetilde\Delta(Y_{ba}^\dagger W_t^\dagger)
 =\widetilde\Delta(W_tY_{ba})^\dagger.
\]
Consequently, with
\[
 Z_t:=\widetilde\Delta_n((I_n\otimes W_t)Y),
\]
the entrywise calculation assembles to the exact matrix identity
\[
 \Delta'_n(Y^\dagger Y)
 =\sum_tq_t\,\Phi_n(Z_t^\dagger Z_t)\ge0.
\]
Since this holds for every \(n\), \(\Delta'\) is completely positive.

No equation
\(\widetilde\Delta(AB)=\widetilde\Delta(A)\widetilde\Delta(B)\) occurred
in this derivation.  The only properties of
\(\widetilde\Delta\) used for positivity were linearity and preservation
of the involution; the essential algebraic input was exact centrality
of \(D_{\mathcal B}\).

### 4.2 Explicit universal error and unitalization ledger

The source supplies the following inputs before CP-ization:

> `tex:2742-2743`  
> `\begin{proof}[Discussion and an outline of the proof.]`  
> `Let us consider the idempotent map $\wt{\Phi}=\theta(2\Phi-1)$ such that $\|\wt{\Phi}-\Phi\|_\cb\le O(\eta)$. By Theorem~\ref{th_almost_idemp}, the subspace $\calA=\Img\wt{\Phi}$ equipped with the Choi-Effros product $Z\star W=\wt{\Phi}(ZW)$ is an extended $O(\eta)$-$C^*$ algebra.`

> `tex:2749-2761`  
> `Theorem~\ref{th_factorization} is proved by reversing those arguments. By Theorem~\ref{th_main_ext}, there exist a finite-dimensional $C^*$ algebra $\calB$ and an extended $O(\eta)$-isomorphism $v\colon\calB\to\calA$. Let $\wt{\Delta}$ be $v$ followed by the inclusion $\calA\to\Bo(\calH)$, and let $\wt{\Upsilon}$ be $\wt{\Phi}$ with the target space $\calA$, followed by $v^{-1}$. These maps are not UCP but meet the other requirements. Indeed, it is immediate that`  
> `\begin{equation}\label{tilde_DelUps}`  
> `\wt{\Delta}\wt{\Upsilon}=\wt{\Phi},\qquad \wt{\Upsilon}\wt{\Delta}=1_\calB,\qquad`  
> `\|\wt{\Delta}\|_\cb\le 1+O(\eta),\qquad \|\wt{\Upsilon}\|_\cb\le 1+O(\eta).`  
> `\end{equation}`  
> `Since $v$ maps $I_\calB$ to $1_\calH$ and carries the $\calB$ product to the Choi-Effros product with $O(\eta)$ accuracy (including tensor extensions), these bounds hold:`  
> `\begin{gather}`  
> `\label{tilde_Del1}`  
> `\|\wt{\Delta}(I_\calB)-1_\calH\|\le O(\eta),\\[2pt]`  
> `\label{tilde_Del2}`  
> `\bigl\|\wt{\Phi}_n\bigl(\wt{\Delta}_n(X)\wt{\Delta}_n(Y)\bigr)`  
> `-\wt{\Delta}_n(XY)\bigr\|`  
> `\le O(\eta)\ts\|X\|\ts\|Y\|\quad\: (X,Y\in\Ma{n}\otimes\calB).`

The involution hypothesis used below is also stated explicitly:

> `tex:2763`  
> `Equations \eqref{tilde_DelUps}--\eqref{tilde_Del2}, as well as the commutation with the involution, fully characterize $\wt{\Delta}$ and $\wt{\Upsilon}$ for our purposes. In particular, these properties imply that`

Make the implicit constants symbolic.  Assume, uniformly in \(n\),
\[
\begin{aligned}
 \|\widetilde\Delta\|_{\rm cb}&\le A,\\
 \|\Phi-\widetilde\Phi\|_{\rm cb}&\le c_\Phi\eta,\\
 \|\widetilde\Delta(I)-I\|&\le c_1\eta,\\
 \|\widetilde\Phi_n(
   \widetilde\Delta_n(X)\widetilde\Delta_n(Y))
   -\widetilde\Delta_n(XY)\|
   &\le c_2\eta\|X\|\|Y\|.
\end{aligned}
\]
For sufficiently small universal \(\eta\), the source's
\(1+O(\eta)\) bound allows a fixed universal \(A\), for example \(A=2\).

For each unitary \(W_t\),
\[
\begin{aligned}
 &\|\Phi_n(
   \widetilde\Delta_n(X(I_n\otimes W_t^\dagger))
   \widetilde\Delta_n(I_n\otimes W_t))
   -\widetilde\Delta_n(X)\|\\
 &\qquad\le
 \bigl(c_2+c_\Phi A^2\bigr)\eta\|X\|.
\end{aligned}
\]
Averaging costs no factor because \(\sum_tq_t=1\).  Set
\[
 K_0:=c_2+c_\Phi A^2.
\]
Then the explicit repaired estimate is
\[
 \boxed{\ \|\Delta'-\widetilde\Delta\|_{\rm cb}
       \le K_0\eta.\ }
\]
No block count, block dimension, or number of design points occurs.

Let
\[
 H:=\Delta'(I_{\mathcal B}),\qquad
 e:=(c_1+K_0)\eta.
\]
Then \(H\ge0\) and \(\|H-I\|\le e\).  If \(e\le1/2\), \(H\) is
invertible and
\[
 S:=H^{-1/2},\qquad
 \|S\|\le(1-e)^{-1/2},\qquad
 \|S-I\|\le(1-e)^{-1/2}-1\le\sqrt2\,e.
\]
The map
\[
 \Delta(X):=S\Delta'(X)S
\]
is CP and exactly unital.  Since a CP map has cb norm equal to the norm
of its value at the identity,
\(\|\Delta'\|_{\rm cb}=\|H\|\le1+e\).  Therefore
\[
\begin{aligned}
 \|\Delta-\Delta'\|_{\rm cb}
 &\le \|S-I\|\,\|\Delta'\|_{\rm cb}(\|S\|+1)\\
 &\le 6e
\end{aligned}
\]
when \(e\le1/2\).  Thus
\[
 \boxed{\ \|\Delta-\widetilde\Delta\|_{\rm cb}
 \le R\eta,\qquad
 R:=6c_1+7K_0.\ }
\]
This is the unitalization cost.  It is universal whenever the input
constants are universal.

For completeness, the degree-two estimate survives with an explicit
symbolic constant.  Using that \(\Phi\) and \(\Delta\) are contractions,
\[
\begin{aligned}
 &\|\Phi_n(\Delta_n(X)\Delta_n(Y))-\Delta_n(XY)\|\\
 &\quad\le
 \left[c_2+c_\Phi A^2+R(A+2)\right]
 \eta\|X\|\|Y\|.
\end{aligned}
\]
Also, the exact identities
\(\widetilde\Delta\widetilde\Upsilon=\widetilde\Phi\) and
\(\widetilde\Upsilon\widetilde\Delta=1_{\mathcal B}\) imply
\(\widetilde\Phi\widetilde\Delta=\widetilde\Delta\), so
\[
 \|\Phi\Delta-\Delta\|_{\rm cb}
 \le(2R+c_\Phi A)\eta.
\]
If \(c_{\rm assoc}\eta\) is the universal constant in the approximate
associativity identity used by the source, then the five-step
calculation at `tex:2820-2828` gives the degree-three constant
\[
 c_3=c_{\rm assoc}
   +6(2R+c_\Phi A)
   +2\left[c_2+c_\Phi A^2+R(A+2)\right].
\]
Again, no dimension enters.

The source records that approximate associativity input as:

> `tex:2196-2205`  
> `The nontrivial part of the proof is concerned with the following equations,`  
> `\begin{align}`  
> `\label{Phi_assoc1}`  
> `\Phi\Bigl(\Phi\bigl(\Phi(X)\,\Phi(Y)\bigr)\,\Phi(Z)\Bigr)`  
> `&=\Phi\bigl(\Phi(X)\,\Phi(Y)\,\Phi(Z)\bigr)+O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|,`  
> `\\[2pt]`  
> `\label{Phi_assoc2}`  
> `\Phi\Bigl(\Phi(X)\,\Phi\bigl(\Phi(Y)\,\Phi(Z)\bigr)\Bigr)`  
> `&=\Phi\bigl(\Phi(X)\,\Phi(Y)\,\Phi(Z)\bigr)+O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|,`  
> `\end{align}`

It states that the same input is used at every amplification:

> `tex:2208-2209`  
> `\begin{proof}[Proof of Theorem~\ref{th_almost_idemp} using equations \eqref{Phi_assoc1} and \eqref{Phi_assoc2}.]`  
> `We assume that these equations are true for all $\eta$-idempotent UCP maps, and in particular, for $1_{\Ma{n}}\otimes\Phi$. So the subsequent arguments are applicable not only to the algebra $\calA$ but also to $\Ma{n}\otimes\calA$.`

The five-step degree-three chain is:

> `tex:2817-2828`  
> `The first three of these follow from \eqref{tilde_DelUps} and \eqref{tilde_Del2}. To prove the last property, we do the following calculation with $O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|$ accuracy, where the second step is the application of equation \eqref{Phi_assoc1} to the UCP map $\Phi_n$:`  
> `\[`  
> `\begin{aligned}`  
> `\Phi_n\bigl(\Delta_n(X)\ts\Delta_n(Y)\ts\Delta_n(Z)\bigr)`  
> `&\approx\Phi_n\bigl(\Phi_n(\Delta_n(X))\,\Phi_n(\Delta_n(Y))\,`  
> `\Phi_n(\Delta_n(Z))\bigr)\\`  
> `&\approx\Phi_n\Bigl(\Phi_n\bigl(\Phi_n(\Delta_n(X))\,\Phi_n(\Delta_n(Y))\bigr)\,`  
> `\Phi_n(\Delta_n(Z))\Bigr)\\`  
> `&\approx\Phi_n\bigl(\Phi_n\bigl(\Delta_n(X)\ts\Delta_n(Y)\bigr)\ts`  
> `\Delta_n(Z)\bigr)`  
> `\approx\Phi_n\bigl(\Delta_n(XY)\ts\Delta_n(Z)\bigr)`  
> `\approx\Delta_n(XYZ).`

The source's resulting degree-two and degree-three target estimates are:

> `tex:2808-2815`  
> `\label{PhiDelta1}`  
> `\|\Phi\Delta-\Delta\|_\cb&\le O(\eta),\qquad& &\\[2pt]`  
> `\label{PhiDelta2}`  
> `\bigl\|\Phi_n\bigl(\Delta_n(X)\Delta_n(Y)\bigr)-\Delta_n(XY)\bigr\|`  
> `&\le O(\eta)\ts\|X\|\ts\|Y\|\qquad& &(X,Y\in\Ma{n}\otimes\calB),\\[2pt]`  
> `\label{PhiDelta3}`  
> `\bigl\|\Phi_n\bigl(\Delta_n(X)\Delta_n(Y)\Delta_n(Z)\bigr)-\Delta_n(XYZ)\bigr\|`  
> `&\le O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|\qquad& &(X,Y,Z\in\Ma{n}\otimes\calB).`

The repaired diagonal therefore changes none of the asymptotic orders
and introduces only coefficient \(1\) at the averaging step.

## 5. Complete use-site recheck ledger

The grep keys used were `diagonal`, `finite_diag`, `diag_j01`,
`diag_j2`, `cor_improvement`, `p_{js}`, `p_s`, and the whole-diagonal
unitary symbols.  The topology use of the word “diagonal” at
`tex:986` is unrelated.  The algebraic consumers are listed below.

| tex locus | algebra whose diagonal is used | what the site uses | repaired diagonal supplies it? | constant change |
|---|---|---|---|---|
| `480-484` | Exact associative algebra in the general discussion; exact finite-dimensional \(C^*\)-algebra for Haar | Definition: centrality and normalization; Haar construction | Yes for exact \(\mathcal B\). No claim is made for approximate \(\mathcal A\). | None |
| `490` | Exact domain \(\mathcal B\), mapped into approximate \(\mathcal A\) | Existence of a diagonal for error reduction | Yes: the lemma above constructs it in \(\mathcal B\). | None |
| `1228-1248` | Exact finite-dimensional \(C^*\)-algebra \(\mathcal B\) | Projective norm, exact centrality, exact normalization, finite norm-one representation | Yes; \(\|D_{\mathcal B}\|_\pi=1\) and the displayed coefficient sum is \(1\). | None |
| `1254` | Exact direct sum \(\mathcal B=\bigoplus_rM_{d_r}\) | Purports to construct the whole-algebra diagonal from per-block designs | **No as printed.** Replace the printed product by the phase-balanced family \(W_{\alpha,\varepsilon}\). | None; term count grows but is never used |
| `1277-1313` (`lem_approx`) | Exact domain \(\mathcal B\); target \(\mathcal A\) is approximate | Finiteness; coefficient sum \(1\) at `1281`; centrality at `1281`, `1294-1296`; normalization at `1302-1303` | Yes, exactly. | None |
| `1317-1319` (`cor_improvement`) | Exact \(\mathcal B\) | Indirectly consumes `lem_approx`, hence all three diagonal properties and norm one | Yes. | None |
| `1415`, `1426`, `1441`, `1443` | The successive exact \(C^*\)-algebras built in the main-theorem argument | Repeated indirect calls to `cor_improvement` | Yes at the diagonal interface. | None |
| `1508-1535` (`lem_approx_ext`) | Exact domain \(\mathcal B\); amplified approximate target \(M_n\otimes\mathcal A\) | Same finite norm-one representation; exact centrality is used entrywise at `1535`; normalization is inherited from the unamplified proof | Yes. The same \(D_{\mathcal B}\) is used for every \(n\), so the coefficient bound stays \(1\). | None |
| `1557` | Exact domain \(\mathcal B\) in the proposed extended error-reduction adaptation | Indirect use of `lem_approx_ext` | The diagonal input is supplied, but the source's broader amplified adaptation remains a separate proof gap; see the defect register. | None from the diagonal |
| `2771-2783` | Exact \(C^*\)-algebra \(\mathcal B=\bigoplus_j\mathcal B(\mathcal L_j)\) | Per-block designs plus a finite norm-one whole-algebra diagonal | Per-block formulas `diag_j01`/`diag_j2` are retained. Replace only the false whole-block product by the phase-balanced product. | None |
| `2786-2796` | Exact \(\mathcal B\) | Whole-diagonal centrality for equality `2788-2789` and entrywise CP; positive weights and finiteness for a finite CP sum | Yes, as re-proved in §4.1. | None |
| `2797-2801` | Exact \(\mathcal B\) | Whole unitaries of norm \(1\), weights summing to \(1\), and approximate unitality | Yes. The averaging coefficient remains exactly \(1\); explicit cost is \(K_0\eta\), followed by at most \(6(c_1+K_0)\eta\) for unitalization under the ledger above. | None relative to a correct norm-one diagonal |
| `2803-2829` | No new diagonal; consumes the repaired UCP \(\Delta\) | cb closeness, approximate invariance, and degree-two/three estimates | Yes conditionally on the pre-existing universal input constants; §4.2 gives the telescoping ledger. | No dimension-dependent change |
| `2840-2856` (`lem_RC`) | Each exact single block \(\mathcal B(\mathcal L_j)\), not the whole direct sum | Per-block centrality `diag_j2`, normalization/unitarity, probability weights | Yes, but no repair is needed here: the per-block \(D_j\) is valid. | None |
| `2859-2899` | Each exact single block for \(R_j,L_j\); then the already repaired UCP \(\Delta\) | Per-block finite convex averages, \(\sum_sp_{js}=1\), and the estimates `PhiDelta1`/`PhiDelta3` | Yes. The independent block signs used only in the earlier whole-algebra diagonal do not alter these valid per-block designs. | None |

The direct error-reduction uses can be seen verbatim here:

> `tex:1277-1281`  
> `First, let us try this version of $w$, which uses a diagonal of the form \eqref{finite_diag}:`  
> `\begin{equation}`  
> `w'(X) = \sum_{j}v(A_j)g(B_j,X).`  
> `\end{equation}`  
> `We have $\|w'(X)\|\le O(\delta)\ts\|X\|$ since $v$ is a $\delta$-homomorphism and $\sum_{j}\|A_j\|\ts\|B_j\|=1$. In the calculation of $F_{w'}$, we will also use a corollary of the equation $\sum_{j}XA_j\otimes B_j=\sum_{j}A_j\otimes B_jX$, namely, $\sum_{j}v(XA_j)g(B_j,Y) =\sum_{j}v(A_j)g(B_jX,Y)$:`

> `tex:1293-1303`  
> `&= \begin{aligned}[t]`  
> `&\sum\nolimits_{j}v(A_j)\bigl(g(B_jX,Y)-g(B_j,XY)+g(B_j,X)v(Y)\bigr)`  
> `+O(\delta\eps+\delta^2)\ts\|X\|\ts\|Y\|\\`  
> `&\textstyle (\text{because } \sum_{j}v(XA_j)g(B_j,Y)=\sum_{j}v(A_j)g(B_jX,Y))`  
> `\end{aligned}`  
> `\nonumber\\[2pt]`  
> `&= \sum\nolimits_{j}v(A_j)\bigl(v(B_j)g(X,Y)\bigr)+O(\delta^2+\eps)\ts\|X\|\ts\|Y\|\quad\:`  
> `(\text{due to the 2-cocycle equation})`  
> `\nonumber\\[2pt]`  
> `&=g(X,Y)+O(\delta^2+\eps)\ts\|X\|\ts\|Y\|\quad\:`  
> `{\textstyle (\text{because } \sum\nolimits_jA_jB_j=I_\calB)}.`

The error-reduction corollary itself is:

> `tex:1317-1319`  
> `\begin{Corollary}[Error reduction]\label{cor_improvement}`  
> `There exist some positive constants $\eps_{\max}$, $\delta_{\max}$, and $c_0$ such that for all $\eps<\eps_{\max}$, if a finite-dimensional $C^*$ algebra $\calB$ is $\delta_{\max}$-included into an $\eps$-$C^*$ algebra $\calA$, there is also a $c_0\eps$-inclusion. If the original inclusion is bijective, then so is the new inclusion.`  
> `\end{Corollary}`

Its repeated consumers in the construction say:

> `tex:1415`  
> `Let $c_0$ be the constant from Corollary~\ref{cor_improvement}. We will construct a $c_0\eps$-isomorphism $v$ from some $C^*$ algebra $\calB$ to the $\eps$-$C^*$ algebra $\calA$ in three stages. The first stage yields a $c_0\eps$-inclusion $v_\comm\colon\calB_\comm\to\calA$, where $\calB_\comm$ is a commutative $C^*$ algebra. The second stage involves the parallel construction of $c_0\eps'$-isomorphisms from some matrix algebras to approximate direct summands of $\calA$. At the third stage, those algebras and isomorphisms are merged.\medskip`

> `tex:1426`  
> `Merging $v_\comm^{(1)}$ and $v_\comm^{(2)}$ using Corollary~\ref{cor_merge_sum}, we obtain an $O(\eps)$-inclusion $v_\comm^+\colon\calB_\comm^+\to\calA$, where $\calB_\comm^+=\calB_\comm^{(1)}\oplus\calB_\comm^{(2)}$. Due to Corollary~\ref{cor_improvement}, there also exists a $c_0\eps$-inclusion of $\calB_\comm^+$ into $\calA$. But this contradicts the maximum dimensionality assumption.\medskip`

> `tex:1441`  
> `Then we extend the $O(\eps)$-isomorphism $v_{r-1}'\colon \Ma{r-1}\to\calA_{r-1}'$ to an $O(\eps)$-isomorphism $v_{r-1}^+\colon \Ma{r}\to\calA_{r}$ using Lemma~\ref{lem_extension}. Finally, we use Corollary~\ref{cor_improvement} to replace $v_{r-1}^+$ with a $c_0\eps'$-isomorphism $v_r$.\medskip`

> `tex:1443`  
> `\noindent\textbf{Stage 3.} At this point, we have constructed $c_0\eps'$-isomorphisms $v_C\colon\Ma{|C|}\to\calS_{P_C}$ for all equivalence classes $C$. Note that by Lemma~\ref{lem_add_dim}, $\calS_{P_C,P_D}=0$ if the classes $C$ and $D$ are distinct. This allows us to successively merge the isomorphisms $v_C$ for different $C$. Each step includes the application of Corollary~\ref{cor_merge_sum} followed by the use of Corollary~\ref{cor_improvement} to reduce the errors.`

The amplified construction and centrality use are verbatim:

> `tex:1517-1521`  
> `It satisfies the approximate 2-cocycle equation because $\Ma{n}\otimes\calA$ is an $\eps$-$C^*$ algebra. Using the diagonal $D=\sum_{j}A_j\otimes B_j \in\calB\otimes\calB$, we define the map $w_n'\colon \Ma{n}\otimes\calB \to\Ma{n}\otimes\calA$ as follows:`  
> `\begin{equation}`  
> `w_n'(X) = \sum_{j}v_n(I_n\otimes A_j)\, g_n(I_n\otimes B_j,X).`  
> `\end{equation}`

> `tex:1535`  
> `Here we have used the property of the diagonal $\sum_{j}ZA_j\otimes B_j=\sum_{j}A_j\otimes B_jZ$ for $Z=[X]_{kp}$. The rest of the proof is the same as for Lemma~\ref{lem_approx}.`

The per-block use after CP-ization is distinct from the false whole
direct-sum formula:

> `tex:2843-2854`  
> `R_j =\sum_{s}p_{js}(U_{js}^{\dag}\otimes 1_{\calE_j})`  
> `W_jW_j^{\dag}(U_{js}\otimes 1_{\calE_j})`  
> `\end{equation}`  
> `has the form $1_{\calL_j}\otimes C_j$ for some $C_j\in\Bo(\calE_j)$. Furthermore, $1-O(\eta)\le\|C_j\|\le 1$.`  
> `\end{Lemma}`  
> `\begin{proof}`  
> `Due to the property \eqref{diag_j2} of the diagonal, $R_j$ commutes with $X\otimes 1_{\calE_j}$ for all $X\in\Bo(\calL_j)$. Hence, $R_j=1_{\calL_j}\otimes C_j$ for some $C_j$. The upper bound $\|C_j\|=\|R_j\|\le 1$ follows from the fact that $\|W_j\|\le 1$. To prove the lower bound, we note that $\|\Phi(W_j^{\dag}R_jW_j)\|\le\|C_j\|$. The left-hand side can be estimated using \eqref{Choi_Delta} (with a single nonzero $X_j$) and \eqref{PhiDelta2}:`  
> `\[`  
> `\Phi(W_j^{\dag}R_jW_j)`  
> `=\sum_{s}p_{js}\ts\Phi\bigl(\Delta(U_{js}^{\dag})\ts\Delta(U_{js})\bigr)`  
> `=\sum_{s}p_{js}\ts\Delta(U_{js}^{\dag}U_{js})+O(\eta)`  
> `=\Delta(1_{\calL_j})+O(\eta).`

The later per-block averaging and unitalization are:

> `tex:2859-2871`  
> `Let $\xi_j\in\calE_j$ be a unit vector such that $\bigl|\|C_j\xi_j\|-1\bigr|\le O(\eta)$. Let us also consider the Choi representation $\Phi(X)=V^\dag(X\otimes 1_\calF)V$ with $V\colon\calH\to\calH\otimes\calF$ and derive new linear maps from $V$:`  
> `\begin{equation}`  
> `L_j\colon\calL_j\to\calH\otimes\calF,\qquad`  
> `L_j=\sum_{s}p_{js}\ts\bigl(\Delta(U_{js}^\dag)\otimes 1_\calF\bigr)`  
> `V W_j^\dag(U_{js}\otimes\xi_j).`  
> `\end{equation}`  
> `We now construct a manifestly completely positive map $\Upsilon'\colon\Bo(\calH)\to\calB$ by components,`  
> `\begin{equation}`  
> `\Upsilon'=(\Upsilon'_1,\dots,\Upsilon'_m),\qquad \text{where}\quad`  
> `\Upsilon'_j\colon\Bo(\calH)\to\Bo(\calL_j),\quad\:`  
> `\Upsilon_j'(X)=L_j^\dag\bigl(\Phi(X)\otimes 1_\calF\bigr)L_j.`  
> `\end{equation}`  
> `Because $\Phi$ is $\eta$-idempotent, $\|\Upsilon'\Phi-\Upsilon'\|_\cb\le O(\eta)$. Let us prove that $\|\Upsilon'\Delta-1_\calB\|_\cb\le O(\eta)$, meaning that if $Y=(Y_1,\dots,Y_m)\in\Ma{n}\otimes\calB$, then $\|(\Upsilon'_j)_n(\Delta_n(Y))-Y_j\|\le O(\eta)\ts\|Y\|$, where $\|Y\|=\max_k\|Y_k\|$. We calculate $(\Upsilon'_j)_n(\Delta_n(Y))$ with $O(\eta)\ts\|Y\|$ accuracy, omitting the subscript $n$:`

> `tex:2895-2899`  
> `Thus, $\Upsilon'\approx \Upsilon'\Phi\approx \Upsilon'\wt{\Phi}= \Upsilon'\wt{\Delta}\wt{\Upsilon}\approx \Upsilon'\Delta\wt{\Upsilon}\approx \wt{\Upsilon}$ with $O(\eta)$ accuracy. Finally, we define the UCP map`  
> `\begin{equation}`  
> `\Upsilon\colon X\mapsto (\Upsilon'(1_\calH))^{-1/2}\ts\Upsilon'(X)\ts(\Upsilon'(1_\calH))^{-1/2},`  
> `\end{equation}`  
> `which also has the property $\|\Upsilon-\wt{\Upsilon}\|_\cb\le O(\eta)$.`

## 6. No cone-projection shortcut

This repair uses no nearest-CP-map theorem and no projection of a Choi
matrix onto the positive cone.  Complete positivity follows exactly
from centrality through
\[
 \Delta'_n(Y^\dagger Y)
 =\sum_tq_t\Phi_n(Z_t^\dagger Z_t)\ge0.
\]
The only later correction is the explicit conjugation by
\(\Delta'(I)^{-1/2}\), which preserves CP and makes the map exactly
unital.

If one discarded the exact-diagonal repair and instead tried to repair a
non-CP map by cone projection, the missing input would have to be a
theorem of the following form:

* a universal \(K\), independent of all domain, codomain, and ancillary
  dimensions, bounding cb distance to the CP cone by
  \(\operatorname{dist}_{\rm cb}(T,\mathrm{CP})\le K\eta\) under the
  available hypotheses;
* a dimension-free unitalization bound for the selected CP map; and
* dimension-free preservation, after selection and unitalization, of
  the degree-two and degree-three estimates used at
  `tex:2808-2815`.

No such theorem is proved or invoked here.  It is unnecessary for the
exact central-diagonal route.

## 7. Defect and edit register

| item | status after this prover pass |
|---|---|
| Printed formula at `tex:1254` | False. It must be replaced by the phase-balanced formula of §3, or by a finite convex representation of the full whole-algebra Haar diagonal. |
| Printed formula at `tex:2780-2783` | Same false formula. It needs the same replacement. |
| Equality at `tex:2788-2789` | Becomes exact after that replacement, by whole-algebra centrality. It is not justified by the printed noncentral object. |
| Positivity display at `tex:2793-2796` | Correct after replacement, but the proof should be written entrywise as in §4.1. Treating \(Y\) as though it occupied both factors of a scalar tensor identity would be invalid. |
| Projective-norm/convex-sum constants | Closed at the diagonal interface: both equal exactly \(1\); no downstream constant changes. |
| Finiteness | Closed: the sign-balanced construction is a finite sum. The number of terms may depend on the block data, but no use site counts terms. |
| Exact \(\mathcal B\) versus approximate \(\mathcal A\) | Closed at all diagonal use sites: every repaired use is a diagonal of exact \(\mathcal B\). No approximate-\(\mathcal A\) diagonal is assumed. |
| Cone projection | Not used. A dimension-free cb nearest-CP theorem would remain an open blocker if this exact repair were rejected. |
| Numerical values of the paper's \(O(\eta)\) constants | Not supplied by this local repair. §4.2 gives an explicit symbolic propagation ledger and shows the diagonal contributes factor \(1\), but numerical evaluation requires numerical values for the source's input constants. |
| Extended main theorem / error-reduction adaptation | Not closed by a diagonal repair. The correct norm-one diagonal supplies the diagonal input to `lem_approx_ext`, but it does not fill other omitted amplified arguments. |
| Other components of `th_almost_idemp` and the full Route-F proof | Outside this diagonal task and not re-proved here. No conclusion about the whole theorem follows from this local repair alone. |

The remaining extended-proof gap is visible verbatim in the source:

> `tex:1538-1539`  
> `\begin{Theorem}\label{th_main_ext}`  
> `For any finite-dimensional extended $\eps$-$C^*$ algebra $\calA$, there exist a $C^*$ algebra $\calB$ and an extended $O(\eps)$-isomorphism $v\colon\calB\to\calA$. (The implicit constant in $O(\eps)$ does not depend on $\calA$ or its dimensionality.)`

> `tex:1557`  
> `Corollary~\ref{cor_improvement} (error reduction) should be adapted to extended inclusions using Lemma~\ref{lem_approx_ext} and Proposition~\ref{prop_inc_ext}. The arguments in Section~\ref{sec_proof_main} require only trivial modifications, namely, one should use the norms $\|\cdot\|_n$ in certain places.`

Accordingly, the result of this prover pass is local and conditional:
the exact whole-algebra diagonal defect has a finite norm-one repair,
and every diagonal-dependent use survives that repair without a
dimension-dependent loss; this does not by itself discharge the
separate amplified-proof gaps.
