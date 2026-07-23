STATUS: UNVERIFIED AUDITOR OUTPUT

# W74F-D hostile audit of `th_almost_idemp`

Date: 2026-07-23  
Auditor posture: fresh, hostile, source-first  
Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`  
Verified SHA256: `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`

## Executive verdict

**VALID-WITH-CORRECTIONS.**

I did not find a mathematical counterexample, a hidden dimension factor, an
amplification-level loss, or an uncharged use of approximate idempotence in
`tex:2239-2723`. The diagrammatic argument can be rewritten entirely as
composition of isometries, orthogonal projections, contractive
\(*\)-homomorphisms, and a fixed number of \(C^*\)-norm estimates. An explicit
ledger is:

\[
\begin{array}{c|c}
\text{printed big-O assertion} & \text{valid explicit bound}\\ \hline
\text{one-rectangle operator at `tex:2295-2296`}
  & \sqrt{3\eta}\,\|X\|\\
\text{its positive square at `tex:2378-2380`}
  & 3\eta\,\|X\|^2\\
W\text{ at `tex:2384-2423` or `tex:2669-2673`}
  & 3\eta\,\|X\|\,\|Y\|\,\|Z\|\\
\text{finite-dimensional reduction remainder at `tex:2580-2582`}
  & 7\eta\,\|X\|\,\|Y\|\,\|Z\|\\
Q\text{ reduction remainder at `tex:2717-2719`}
  & 5\eta\,\|X\|\,\|Y\|\,\|Z\|\\
W\text{ reduction remainder at `tex:2721-2723`}
  & 7\eta\,\|X\|\,\|Y\|\,\|Z\|\\
\text{each of \eqref{Phi_assoc1}, \eqref{Phi_assoc2}}
  & 10\eta\,\|X\|\,\|Y\|\,\|Z\|
\end{array}
\]

The corrections are real but local:

1. At `tex:2603`, `tex:2608`, `tex:2620`, and `tex:2624`, the displayed
   membership conditions say \(X\in\mathcal H_n\) or \(Y\in\mathcal H_m\);
   these variables are operators and must lie in
   \(\mathcal B(\mathcal H_n)\) or \(\mathcal B(\mathcal H_m)\).
2. At `tex:2665`, the final \(V_1\) must be \(V_{1+k}\). As printed, the
   product is not even type-correct when \(k>0\).
3. The sentence asserting that the second associativity equation is obtained
   “similarly” supplies no derivation. It is nevertheless an exact consequence
   of the first equation by taking adjoints and substituting
   \((Z^\dagger,Y^\dagger,X^\dagger)\), with the same constant \(10\).

The theorem therefore survives this audit, but the literal TeX needs those
corrections before it is a clean proof.

## Byte-verbatim source anchors

The source fixes the meaning of its asymptotic notation at `tex:458`:

> `Note that the inverse of a $\delta$-isomorphism is a ($\delta+O(\delta^2)$)-isomorphism. Here and in general, each instance of big-$O$ or similar notation stands for a concrete function, not depending on any additional data.`

The hypotheses are printed at `tex:2166-2169`:

> `Let $\calH$ be an arbitrary nonzero Hilbert space, and let us consider a UCP map $\Phi\colon\Bo(\calH)\to\Bo(\calH)$ such that`
>
> `\|\Phi^2-\Phi\|_\cb\le\eta,`
>
> `where $\eta$ is a sufficiently small nonnegative number.`

The target theorem is printed at `tex:2192-2194`:

> `\begin{Theorem}\label{th_almost_idemp}`
>
> `The space $\calA$ with the norm, involution, and unit inherited from $\Bo(\calH)$ and the multiplication $(X,Y)\mapsto X\star Y$ is an extended $O(\eta)$-$C^*$ algebra.`
>
> `\end{Theorem}`

The amplified scope is explicit at `tex:2208-2209`:

> `\begin{proof}[Proof of Theorem~\ref{th_almost_idemp} using equations \eqref{Phi_assoc1} and \eqref{Phi_assoc2}.]`
>
> `We assume that these equations are true for all $\eta$-idempotent UCP maps, and in particular, for $1_{\Ma{n}}\otimes\Phi$. So the subsequent arguments are applicable not only to the algebra $\calA$ but also to $\Ma{n}\otimes\calA$.`

The finite-dimensional proof begins at `tex:2239-2242`:

> `\begin{proof}[Proof of \eqref{Phi_assoc1} and \eqref{Phi_assoc2} in the finite-dimensional case.]`
>
> `Let $(\calF,V)$ be the Choi representation of $\Phi$, and let us introduce the notation`
>
> `\Pi=VV^\dag=`

The one-rectangle claim is printed at `tex:2273-2297`:

> `First, we show that`
>
> `\begin{equation}\label{1-Pi_X}`
>
> `=O\bigl(\sqrt{\eta}\bigr)\|X\|.`
>
> `\end{equation}`

Its square is identified at `tex:2378-2380`:

> `&= \Phi^2\bigl(\Phi(X^\dag)\,\Phi(X)\bigr)`
>
> `-\Phi\bigl(\Phi^2(X^\dag)\,\Phi^2(X)\bigr)`
>
> `=O(\eta)\|X\|^2.`

The two-rectangle estimate is printed at `tex:2384-2423`:

> `Now, consider a diagram that has two parts similar to the left-hand side of \eqref{1-Pi_X}, one containing $X$ and the other containing $Z$:`
>
> `\begin{equation}\label{WXYZOeta}`
>
> `W=`
>
> `=O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|.`
>
> `\end{equation}`

The finite-dimensional four-term translation and reduction are printed at
`tex:2572-2584`:

> `&=\begin{aligned}[t]`
>
> `&\phantom{\hbox{}+\hbox{}}`
>
> `\Phi^2\Bigl(\Phi\bigl(\Phi(X)\,\Phi(Y)\bigr)\,\Phi(Z)\Bigr)`
>
> `-\Phi\Bigl(\Phi^2\bigl(\Phi(X)\,\Phi(Y)\bigr)\,\Phi^2(Z)\Bigr)\\`
>
> `&-\Phi^2\bigl(\Phi^2(X)\,\Phi^2(Y)\,\Phi(Z)\bigr)`
>
> `+\Phi\Bigl(\Phi\bigl(\Phi^2(X)\,\Phi^2(Y)\bigr)\,\Phi^2(Z)\Bigr)`
>
> `\end{aligned}`
>
> `&=\Phi\Bigl(\Phi\bigl(\Phi(X)\,\Phi(Y)\bigr)\,\Phi(Z)\Bigr)`
>
> `-\Phi\bigl(\Phi(X)\,\Phi(Y)\,\Phi(Z)\bigr)`
>
> `+O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|.`
>
> `The combination of this result and equation \eqref{WXYZOeta} gives \eqref{Phi_assoc1}. Equation \eqref{Phi_assoc2} is obtained similarly.`

The general proof’s one-rectangle replacement is printed at `tex:2639-2660`:

> `\begin{proof}[General proof of equations \eqref{Phi_assoc1} and \eqref{Phi_assoc2}.]`
>
> `First, we construct an analogue of the left-hand side of \eqref{1-Pi_X} covered by $k$ additional layers:`
>
> `R_k(X)=u_{2+k,1}\mkern-1mu\Bigl(`
>
> `(I_1-V_1V_1^\dag)\,u_1(\Phi(X))`
>
> `\Bigr)\,V_{2+k}V_{1+k},`
>
> `where $I_n=1_{\calH_n}$. The norm of $R_k(X)$ is estimated as follows,`
>
> `R_k(X)^\dag\,R_k(X)`
>
> `&= u_{k,0}\Bigl(\Phi^2\bigl(\Phi(X^\dag)\,\Phi(X)\bigr)`
>
> `-\Phi\bigl(\Phi^2(X^\dag)\,\Phi^2(X)\bigr)\Bigr)`
>
> `=O(\eta)\|X\|^2,`

The general two-rectangle estimate is printed at `tex:2669-2673`:

> `By analogy with equation \eqref{WXYZOeta}, we have`
>
> `\begin{equation}\label{WXYZOeta-1}`
>
> `W=V_1^\dag\,R_1(X^\dag)^\dag\,u_{3,0}(\Phi(Y))\,V_3\,R_0(Z)`
>
> `=O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|.`
>
> `\end{equation}`

The final general reduction is printed at `tex:2717-2723`:

> `&=\Phi\bigl(\Phi\bigl(\Phi(X)\,\Phi(Y)\bigr)\,\Phi(Z)\bigr)`
>
> `-\Phi\bigl(\Phi(X)\,\Phi(Y)\,\Phi(Z)\bigr)`
>
> `+O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|.`
>
> `Thus, $W=\Phi\bigl(\Phi\bigl(\Phi(X)\,\Phi(Y)\bigr)\,\Phi(Z)\bigr)`
>
> `-\Phi\bigl(\Phi(X)\,\Phi(Y)\,\Phi(Z)\bigr)`
>
> `+O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|$. This equation together with \eqref{WXYZOeta-1} implies \eqref{Phi_assoc1}. Equation \eqref{Phi_assoc2} is obtained in the same way.`

## Explicit estimate engine

Put \(T=\Phi\) and \(D=T^2-T\). At every amplification level under
consideration,
\[
\|T\|\le 1,\qquad \|D\|\le\eta .
\]
The first inequality is the UCP contraction property; the second is the
hypothesis in cb norm. Consequently, for all \(A,B\),
\[
\|T^2(A)-T(A)\|\le\eta\|A\|,
\tag{E1}
\]
and
\[
\|T^2(A)T^2(B)-T(A)T(B)\|
\le 2\eta\|A\|\|B\|.
\tag{E2}
\]
For (E2), insert and subtract \(T(A)T^2(B)\). There is no sum over
coordinates, Kraus operators, blocks, or an ancillary basis.

For the positive operator represented by the squared one-rectangle diagram,
write
\[
S_X^\dagger S_X
=T^2\!\left(T(X^\dagger)T(X)\right)
-T\!\left(T^2(X^\dagger)T^2(X)\right).
\]
Insert \(T(T(X^\dagger)T(X))\). By (E1), the first difference costs
\(\eta\|X\|^2\); by (E2) and contractivity of \(T\), the second costs
\(2\eta\|X\|^2\). Hence
\[
\|S_X^\dagger S_X\|\le3\eta\|X\|^2,\qquad
\|S_X\|\le\sqrt{3\eta}\|X\|.
\tag{E3}
\]

The two-rectangle diagram has one such factor on each side of a contraction
of norm at most \(\|Y\|\). Thus
\[
\|W\|\le
\|S_X\|\,\|Y\|\,\|S_Z\|
\le3\eta\|X\|\|Y\|\|Z\|.
\tag{E4}
\]

To reduce the expanded finite-dimensional \(W\), abbreviate
\[
A=T(X),\quad B=T(Y),\quad C=T(Z),\qquad
A'=T^2(X),\quad B'=T^2(Y),\quad C'=T^2(Z).
\]
The four terms at `tex:2574-2577` are
\[
\begin{aligned}
W={}&T^2(T(AB)C)-T(T^2(AB)C')\\
&-T^2(A'B'C)+T(T(A'B')C').
\end{aligned}
\tag{E5}
\]
The first term differs from \(T(T(AB)C)\) by at most \(\eta\|X\|\|Y\|\|Z\|\).
The second and fourth terms combine, and
\[
\|T(A'B')-T^2(AB)\|
\le\underbrace{\|A'B'-AB\|}_{\le2\eta\|X\|\|Y\|}
 \eta\|A\|\|B\|
\le3\eta\|X\|\|Y\|.
\]
Finally,
\[
\|T^2(A'B'C)-T(ABC)\|
\le3\eta\|X\|\|Y\|\|Z\|.
\]
Therefore
\[
\left\|W-\left[T(T(AB)C)-T(ABC)\right]\right\|
\le7\eta\|X\|\|Y\|\|Z\|.
\tag{E6}
\]
Combining (E4) and (E6) gives the constant \(10\) in
\(\eqref{Phi_assoc1}\).

For \(\eqref{Phi_assoc2}\), apply \(\eqref{Phi_assoc1}\) to
\((Z^\dagger,Y^\dagger,X^\dagger)\), take adjoints, and use the exact
identity \(T(U^\dagger)=T(U)^\dagger\). This gives the same constant \(10\);
no second diagram expansion is needed.

In the general proof, the expansion of \(Q\) at `tex:2697-2715` gives
\[
\begin{aligned}
Q={}&T(T(AB)C)-T^2(AB)C'\\
&-T(A'B'C)+T(A'B')C'.
\end{aligned}
\tag{E7}
\]
The second and fourth terms cost \(3\eta\|X\|\|Y\|\|Z\|\) together, and the
third differs from \(-T(ABC)\) by at most
\(2\eta\|X\|\|Y\|\|Z\|\). Thus the \(Q\)-remainder is \(5\eta\).
Since \(W=T(Q)\), applying \(T\) to the two already-\(T\)-valued target
terms costs at most another \(2\eta\), giving the printed \(W\)-remainder
\(7\eta\), and again the final constant is \(7+3=10\).

## Per-block verdict ledger

| tex-locus | what is claimed | verdict | explicit constant | what it depends on / brief argument |
|---|---|---|---|---|
| `tex:2239-2272` | “`Let $(\calF,V)$ be the Choi representation of $\Phi$`” and “`\Pi=VV^\dag`”; the second rectangle is “`=1-\Pi`”. | VALID | \(0\) (exact) | Finite-dimensional UCP gives an isometry \(V\), so \(V^\dagger V=I\), \(VV^\dagger\) is an orthogonal projection, and \(I-VV^\dagger\) is an orthogonal projection. No dimension enters its norm. |
| `tex:2273-2380` | “`=O\bigl(\sqrt{\eta}\bigr)\|X\|`” and, after squaring, “`=O(\eta)\|X\|^2`”. | VALID | \(\sqrt{3\eta}\|X\|\); square \(\le3\eta\|X\|^2\) | Exact diagram multiplication gives \(S_X^\dagger S_X\) as printed at `tex:2378-2379`. Apply (E1) once and (E2) once, as in (E3). UCP supplies the isometry, \(*\)-preservation, and contractions; approximate idempotence supplies exactly three \(\eta\)-charges. |
| `tex:2384-2423` | “`a diagram that has two parts similar to the left-hand side of \eqref{1-Pi_X}`” satisfies “`=O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|`”. | VALID | \(3\eta\|X\|\|Y\|\|Z\|\) | Factor the diagram through the two one-rectangle operators. Every intervening \(V\), \(V^\dagger\), \(I-\Pi\), and tensor identity is contractive; the \(Y\)-box has norm \(\|Y\|\). Apply (E3) twice. |
| `tex:2424-2578` | “`Expanding both rectangles as $1-VV^\dag$, we get`” the four diagrams and then the four \(\Phi\)-terms at `tex:2574-2577`. | VALID | \(0\) (exact) | The signs are \(+,-,-,+\). Translating each inserted \(VV^\dagger\) through \(V^\dagger(A\otimes I)V=T(A)\) gives exactly (E5). This is multiplication/composition only; no approximate identity is used in this block. |
| `tex:2580-2584` | The four terms equal the desired first associativity defect “`+O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|`”, and “`Equation \eqref{Phi_assoc2} is obtained similarly.`” | VALID | reduction remainder \(7\eta\); each final identity \(10\eta\) | The \(7\eta\) calculation is (E6); add the \(3\eta\) norm of \(W\). The second identity follows by the exact adjoint argument, with the same \(10\). The source omits that argument but the assertion is correct. |
| `tex:2587-2609` | A canonical Stinespring stack is constructed and “`u_n(V_n^\dag XV_n)=\Phi_n(X)=V_{n+1}^\dag\, u_{n+1}(X)\, V_{n+1}`”; the second commuting identity is also displayed. | VALID-WITH-CORRECTIONS | \(0\) (exact) | The identities follow from the two commuting diagrams of the canonical Stinespring representation. At `tex:2603`, “`(X\in\calH_n)`” must be \(X\in\mathcal B(\mathcal H_n)\); at `tex:2608`, “`(Y\in\calH_{n-1})`” must be \(Y\in\mathcal B(\mathcal H_{n-1})\). These are type errors, not estimate errors. |
| `tex:2610-2626` | “`Equations \eqref{uVdV} and \eqref{uVVd} can be applied iteratively`” to give the two multi-layer identities. | VALID-WITH-CORRECTIONS | \(0\) (exact) | Induction on \(k\) gives both identities. At `tex:2620`, “`(X\in\calH_n)`” must be \(X\in\mathcal B(\mathcal H_n)\); at `tex:2624`, “`(Y\in\calH_m)`” must be \(Y\in\mathcal B(\mathcal H_m)\). Only the first identity is subsequently used, exactly as “`We will use only \eqref{uVdV}, \eqref{uVdV-multi}`” says at `tex:2626`. |
| `tex:2639-2667` | The general one-rectangle operator \(R_k(X)\) has square ending in “`=O(\eta)\|X\|^2`”; the auxiliary compression identity is printed at `tex:2664-2666`. | VALID-WITH-CORRECTIONS | \(\|R_k(X)^\dagger R_k(X)\|\le3\eta\|X\|^2\), so \(\|R_k(X)\|\le\sqrt{3\eta}\|X\|\), uniformly in \(k\) | The outer \(u_{k,0}\) is a contractive \(*\)-homomorphism, so (E3) applies unchanged. However, the printed `tex:2665` reads “`=V_{1+k}^\dag\,\ts u_{1+k,0}(V_1^\dag ZV_1)\,V_1`”. The final \(V_1\) must be \(V_{1+k}\); otherwise the product is ill-typed for \(k>0\). With that correction, the next equality follows by the multi-layer identity. |
| `tex:2669-2673` | “`W=V_1^\dag\,R_1(X^\dag)^\dag\,u_{3,0}(\Phi(Y))\,V_3\,R_0(Z)`” is “`=O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|`”. | VALID | \(3\eta\|X\|\|Y\|\|Z\|\) | Use the corrected \(R_k\) bound twice. \(V_1^\dagger,V_3\) are contractions; \(u_{3,0}\) is contractive; \(\|\Phi(Y)\|\le\|Y\|\). No layer count occurs. |
| `tex:2674-2689` | “`The expression for $W$ is transformed as follows`” through three lines and ends with “`=\Phi(Q)`”. | VALID | \(0\) (exact) | Successive uses of the one-step compression identity move \(V_3^\dagger(\cdot)V_3\), then \(V_2^\dagger(\cdot)V_2\), inward. Multiplicativity of \(u_2,u_3\) combines adjacent factors. The final \(V_1^\dagger u_1(Q)V_1\) is exactly \(\Phi(Q)\). |
| `tex:2690-2720` | The four-term expansion of \(Q\) ends in the desired first defect “`+O(\eta)\ts\|X\|\ts\|Y\|\ts\|Z\|`”. | VALID | \(5\eta\|X\|\|Y\|\|Z\|\) | The exact expansion is (E7). The pair containing \(C'\) costs \(3\eta\); replacing \(A'B'\) by \(AB\) in the remaining term costs \(2\eta\). No outer-\(T\) defect is charged yet. |
| `tex:2721-2723` | “`Thus, $W=`” the first associativity defect plus \(O(\eta)\), which with `\eqref{WXYZOeta-1}` implies the first equation; “`Equation \eqref{Phi_assoc2} is obtained in the same way.`” | VALID | \(W\)-reduction remainder \(7\eta\); each final identity \(10\eta\) | Applying the outer \(T\) to the \(5\eta\) remainder does not enlarge it; restoring the two \(T\)-valued target terms costs \(2\eta\). Add the independent \(3\eta\) bound on \(W\). The exact adjoint reduction gives the second equation with the same constant. |

## Literal correction register

### 1. Operator-domain corrections

At `tex:2602-2604`, the source prints:

> `u_n(V_n^\dag XV_n)=\Phi_n(X)=V_{n+1}^\dag\, u_{n+1}(X)\, V_{n+1}\qquad`
>
> `(X\in\calH_n).`

The corrected final condition is
\[
X\in\mathcal B(\mathcal H_n).
\]

At `tex:2607-2609`, the source prints:

> `u_{n+1}(V_n YV_n^\dag)=V_{n+1}\, u_n(Y)\, V_{n+1}^\dag\qquad`
>
> `(Y\in\calH_{n-1}).`

The corrected final condition is
\[
Y\in\mathcal B(\mathcal H_{n-1}).
\]

The same correction is required in the multi-layer equations. At
`tex:2619-2624`, the source prints:

> `u_{m+k,m}(V_{n,m}^\dag XV_{n,m})`
>
> `&=V_{n+k,m+k}^\dag\,\ts u_{n+k,n}(X)\,V_{n+k,m+k}\qquad && (X\in\calH_n),`
>
> `u_{n+k,n}(V_{n,m}YV_{n,m}^\dag)`
>
> `&=V_{n+k,m+k}\,\ts u_{m+k,m}(Y)\,V_{n+k,m+k}^\dag\qquad && (Y\in\calH_m).`

The corrected conditions are \(X\in\mathcal B(\mathcal H_n)\) and
\(Y\in\mathcal B(\mathcal H_m)\).

### 2. Wrong isometry index at `tex:2665`

At `tex:2664-2666`, the source prints:

> `V_{1+k}^\dag V_{2+k}^\dag\,\ts u_{2+k,1}(Z)\, V_{2+k}V_{1+k}`
>
> `=V_{1+k}^\dag\,\ts u_{1+k,0}(V_1^\dag ZV_1)\,V_1`
>
> `= u_{k,0}\mkern-1mu\bigl(V_1^\dag\,u_1(V_1^\dag ZV_1)\,V_1\bigr).`

The middle line must be
\[
V_{1+k}^\dagger\,
u_{1+k,0}(V_1^\dagger ZV_1)\,
V_{1+k}.
\]
This is forced by domains:
\(u_{1+k,0}(V_1^\dagger ZV_1)\in\mathcal B(\mathcal H_{1+k})\), while
\(V_{1+k}:\mathcal H_k\to\mathcal H_{1+k}\). The printed \(V_1\) has
domain \(\mathcal H_0\) and codomain \(\mathcal H_1\), so it cannot be
multiplied there for general \(k\).

## Dimension-freedom attack

### Finite-dimensional Choi diagrams

The source defines the Choi representation at `tex:1568-1574`:

> `If $\calK$ and $\calH$ are finite-dimensional Hilbert spaces, then any UCP map $\Phi\colon\Bo(\calK)\to\Bo(\calH)$ admits a \emph{Choi representation}`
>
> `\Phi(X)=V^\dag(X\otimes 1_\calF)V,\qquad`
>
> `V^{\dag}V=1_{\calH},\qquad`
>
> `\text{where}\quad`
>
> `V\colon\calH\to\calK\otimes\calF.`

The ancillary space \(\mathcal F\) may grow with \(\dim\mathcal H\), but
none of `tex:2239-2584` takes a trace over \(\mathcal F\), sums over a basis
of \(\mathcal F\), or uses a Hilbert--Schmidt norm. Every occurrence of an
\(\mathcal F\)-wire means tensoring with an identity, whose operator norm is
one. Every black dot is \(V\) or \(V^\dagger\), also norm one. Both
\(\Pi=VV^\dagger\) and \(I-\Pi\) are orthogonal projections, norm at most
one. Therefore no factor \(\dim\mathcal F\), \(\dim\mathcal H\), or number
of Kraus operators is present.

### General Stinespring stack

The source introduces the stack at `tex:2587-2600`:

> `To prove the result in full generality (in finite and infinite dimensions), we need to replace the Choi representation with the Stinespring representation and find suitable generalizations of the Hilbert spaces $\calH_n=\calH\otimes\calF^{\otimes n}$, isometries $V_n=V\otimes 1_\calF^{\otimes(n-1)}\colon\calH_{n-1}\to\calH_{n}$, and \hbox{$*$-homomorphisms} $u_n\colon X\mapsto X\otimes1_\calF\colon \Bo(\calH_{n-1})\to\Bo(\calH_{n})$.`
>
> `Such a ``Stinespring stack''`
>
> `is constructed inductively, starting from $\calH_0=\calH$ and $\Phi_0=\Phi$.`

After the index correction above, the proof uses only:

- isometries \(V_j\), norm one;
- orthogonal projections \(I_j-V_jV_j^\dagger\), norm at most one;
- \(*\)-homomorphisms \(u_{n,m}\), contractive;
- the fixed defect bound \(\|T^2-T\|\le\eta\);
- a fixed number of products and triangle inequalities.

The number of stack layers appearing in \(R_k\) does not affect the constant:
all extra layers are absorbed into one contractive \(*\)-homomorphism
\(u_{k,0}\). There is no direct sum of simple blocks anywhere in this
proof, so neither the number of summands nor a block dimension can enter.

### Amplification level

The source’s extended definition is at `tex:1477-1479`:

> `An \emph{extended $\eps$-$C^*$ algebra} is a complete self-adjoint operator space $\calA$ with a multiplication and a unit that make each space $\Ma{n}\otimes\calA$ into an $\eps$-$C^*$ algebra. An \emph{extended $\delta$-homomorphism} is a linear map $v\colon\calA'\to\calA''$ such that for each $n$, the map $1_{\Ma{n}}\otimes v\colon \Ma{n}\otimes\calA'\to\Ma{n}\otimes\calA''$ is a $\delta$-homomorphism.`

For \(T_n=1_{M_n}\otimes T\), UCP is preserved and
\[
\|T_n^2-T_n\|\le\|T^2-T\|_{\rm cb}\le\eta.
\]
The preceding estimates therefore apply verbatim to \(T_n\), with constants
\(\sqrt3,3,5,7,10\) independent of \(n\). No normalization by \(n\), trace
on \(M_n\), or sum of \(n\) terms occurs. I found no amplification leak.

## Hypothesis tracking

| hypothesis/property | where it is used | hostile conclusion |
|---|---|---|
| UCP | Choi/Stinespring representations; \(V_j\) isometric; \(\Phi\) contractive and \(*\)-preserving; Schwarz inequality in the earlier \(C^*\)-axiom step | Essential and explicitly assumed. Complete positivity is not silently weakened to positivity. |
| Unitality | Makes each Stinespring \(V_j\) an isometry, hence \(V_jV_j^\dagger\) an exact projection; gives the exact unit in \(\mathcal A\) | Essential. The diagrams would fail for a merely CP nonunital map. |
| \(\|\Phi^2-\Phi\|_{\rm cb}\le\eta\) | (E1), (E2), and uniform repetition at all matrix levels | Every replacement of \(\Phi^2\) by \(\Phi\) is charged. I found no approximate identity used as exact. |
| finite-dimensionality | Only `tex:2239-2585`, to use the concrete Choi tensor-power picture | Not used in the general Stinespring proof `tex:2587-2724`. |
| \(\eta<1/4\) | Functional calculus defining \(\widetilde\Phi\), before the audited diagrams | Not used in either proof of \(\eqref{Phi_assoc1}\), \(\eqref{Phi_assoc2}\). The diagram bounds hold whenever the stated defect bound holds. |
| smallness beyond \(\eta<1/4\) | Needed only to package the later lower \(C^*\)-norm estimate with a common \(\epsilon<1\) | No hidden smallness threshold occurs in constants \(3,5,7,10\). |

The source states the functional-calculus threshold at `tex:2171-2179`:

> `\wt{\Phi}=\theta(2\Phi-1)`
>
> `=\frac{1}{2}\Bigl(1+\sgn(2\Phi-1)\Bigr)`
>
> `=\frac{1}{2}\Bigl(1+(2\Phi-1)\bigl(1-4(\Phi-\Phi^2)\bigr)^{-1/2}\Bigr).`
>
> `The right-hand side involves a Taylor expansion in $4(\Phi-\Phi^2)$, which converges if $\eta<1/4$. The map $\wt{\Phi}$ has the properties`
>
> `\wt{\Phi}^2=\wt{\Phi},\qquad`
>
> `\|\wt{\Phi}-\Phi\|_\cb\le O(\eta),`

An explicit bound sufficient for the interface is
\[
r(\eta):=\|\widetilde\Phi-\Phi\|_{\rm cb}
\le \frac32\left((1-4\eta)^{-1/2}-1\right),
\qquad 0\le\eta<\frac14.
\tag{E8}
\]
Indeed, \(\|2\Phi-I\|_{\rm cb}\le3\), and the inverse-square-root series has
nonnegative scalar coefficients. This is dimension-free and
\(r(\eta)=O(\eta)\).

## Interface to `th_factorization`

The algebra is defined at `tex:2183-2189`:

> `which allow for the definition of $\calA$:`
>
> `\calA=\Img\wt{\Phi}=\Ker(1-\wt{\Phi})\subseteq\Bo(\calH).`
>
> `As such, $\calA$ is a closed subspace of $\Bo(\calH)$; it contains the unit operator $I=1_\calH$ and is invariant under the involution $X\mapsto X^\dag$. We define the multiplication (approximate Choi-Effros product) on $\calA$ by the equation`
>
> `X\star Y=\wt{\Phi}(XY)\qquad (X,Y\in\calA).`

With \(r=r(\eta)\) from (E8), put \(M=1+r\). The audited constants give one
fully explicit common extended-\(C^*\) error, for sufficiently small
\(\eta\),
\[
\epsilon_{\rm AI}(\eta)=
\max\left\{
r,\;
20\eta+2(M^5-1),\;
3r-r^2
\right\}.
\tag{E9}
\]
Here:

- submultiplicativity costs \(r\), since
  \(\|\widetilde\Phi(XY)\|\le(1+r)\|X\|\|Y\|\);
- the two \(T\)-associativity defects cost \(20\eta\), and replacing the
  five occurrences of \(T\) in each nested expression by
  \(\widetilde\Phi\) costs at most \(M^5-1\) per side;
- Schwarz for \(T\), followed by
  \(\|T(X)\|\ge(1-r)\|X\|\) for
  \(X\in\operatorname{Img}\widetilde\Phi\), gives
  \[
  \|\widetilde\Phi(X^\dagger X)\|
  \ge(1-3r+r^2)\|X\|^2.
  \]

The unit and involution axioms are exact. Formula (E9) is \(O(\eta)\), is
independent of \(\dim\mathcal H\), and applies at every matrix amplification.
Thus the audited proof really delivers
\[
\mathcal A=\operatorname{Img}\widetilde\Phi,\qquad
Z\star W=\widetilde\Phi(ZW),
\]
as an **extended** \(\epsilon_{\rm AI}(\eta)\)-\(C^*\)-algebra, not merely
an unamplified approximate algebra.

The downstream source use is explicit at `tex:2742-2749`:

> `\begin{proof}[Discussion and an outline of the proof.]`
>
> `Let us consider the idempotent map $\wt{\Phi}=\theta(2\Phi-1)$ such that $\|\wt{\Phi}-\Phi\|_\cb\le O(\eta)$. By Theorem~\ref{th_almost_idemp}, the subspace $\calA=\Img\wt{\Phi}$ equipped with the Choi-Effros product $Z\star W=\wt{\Phi}(ZW)$ is an extended $O(\eta)$-$C^*$ algebra.`
>
> `Theorem~\ref{th_factorization} is proved by reversing those arguments. By Theorem~\ref{th_main_ext}, there exist a finite-dimensional $C^*$ algebra $\calB$ and an extended $O(\eta)$-isomorphism $v\colon\calB\to\calA$.`

There is no extended/unextended interface mismatch in
`th_almost_idemp`: the amplified statement needed by `th_main_ext` is
exactly what the proof establishes. This conclusion does not audit or cure
any separate gap in `th_main_ext`.

## Counterexample attempts

### Attempt 1: qubit dephasing mixture

For \(0<\lambda<1\), consider the UCP Schur multiplier
\[
\Phi_\lambda
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=
\begin{pmatrix}a&\lambda b\\\lambda c&d\end{pmatrix}.
\]
It is the convex combination of the identity channel and diagonal
conditional expectation. Its cb idempotence defect is exactly
\[
\eta=\lambda(1-\lambda).
\]
For \(X=E_{12}\), the positive one-rectangle square is
\[
\lambda^2(1-\lambda^2)E_{22},
\]
so
\[
\frac{\|S_X^\dagger S_X\|}{\eta\|X\|^2}
=\lambda(1+\lambda)\longrightarrow2
\qquad(\lambda\to1).
\]
This attack disproves any universal square bound with constant \(1\), and
shows that the suppressed constant is not cosmetic. It does not break the
audited constant \(3\).

For the first associativity equation, take
\[
X=E_{11},\qquad Y=E_{12},\qquad Z=E_{22}.
\]
For the second, take
\[
X=E_{11},\qquad Y=E_{11},\qquad Z=E_{12}.
\]
In both cases the norm of the defect is
\[
(1-\lambda)\lambda^2=\lambda\eta.
\]
Thus each associativity constant must be at least \(1\) asymptotically.
The examples do not break \(10\).

Applying \(1_{M_2}\otimes\Phi_\lambda\) leaves these ratios unchanged by
using \(E_{11}\) in the new matrix leg. This failed to produce an
amplification factor.

### Attempt 2: the commutative algebra \(\mathbb C\oplus\mathbb C\)

Let \(e=(1,1)\), \(h=(1,-1)\), and
\[
\Phi_\lambda(ae+bh)=ae+\lambda bh.
\]
This is a unital positive map on a commutative \(C^*\)-algebra and hence
UCP. Again \(\|\Phi_\lambda^2-\Phi_\lambda\|=\lambda(1-\lambda)=\eta\).
With \((X,Y,Z)=(e,h,h)\), the first associativity defect is
\[
-\lambda^2(1-\lambda)e,
\]
of norm \(\lambda\eta\). With \((X,Y,Z)=(h,h,e)\), the second defect has
the same norm. This attacks the possibility that the matrix-unit example
worked only because of noncommutativity; it does not.

### Attempt 3: remove unitality

On \(\mathbb C\), the CP map \(\Psi_\lambda(z)=\lambda z\) has small
idempotence defect \(\lambda(1-\lambda)\), but it is not unital. Its
Stinespring operator is a contraction with
\(VV^\dagger=\lambda\), not a projection. Therefore the replacement of a
rectangle by \(I-VV^\dagger\) no longer has the projection interpretation
used at `tex:2242-2271`. This is not a counterexample to the theorem because
UCP includes unitality; it confirms that unitality is an essential, visible
hypothesis rather than harmless decoration.

## Residual register

1. **Constant optimality remains unchecked.** Constants
   \(\sqrt3,3,5,7,10\) are explicit valid upper bounds, not claimed best
   constants. The qubit family only forces lower constants
   \(\sqrt2\) for the one-rectangle operator and \(1\) for associativity.
2. **The earlier functional-calculus theorem was not re-proved in full.**
   Bound (E8) checks the dimension-free size of
   \(\widetilde\Phi-\Phi\), but exact idempotence of the spectral projector
   still rests on the source’s earlier functional-calculus construction.
   A full independent audit would start before `tex:2171`.
3. **The canonical Stinespring commuting proposition is a dependency.**
   This pass checked the types and every use of its two identities in
   `tex:2587-2723`, but did not independently reconstruct the canonical
   Stinespring representation from first principles. Such a check would
   audit `tex:1621-1687`.
4. **The literal source must be emended.** Without changing the four
   operator-domain annotations and the \(V_1\) at `tex:2665`, the general
   proof contains ill-typed formulas. The intended corrected formulas are
   clear and make the argument valid; leaving the printed formulas
   untouched is not acceptable for a formal import.
5. **No conclusion about `th_main_ext`.** This audit confirms that
   `th_almost_idemp` supplies the extended object consumed downstream. It
   does not establish that the separate theorem `th_main_ext` has a
   complete proof or a closed constant ledger.

## Hostile bottom line

\[
\boxed{
\begin{minipage}{0.88\linewidth}
The diagrammatic core of `th_almost_idemp` survives: after local type/index
corrections, both associativity identities hold at every amplification with
the dimension-free explicit constant \(10\eta\). No trace, basis sum,
ancilla dimension, block count, or amplification level enters. The printed
proof is not literally clean because `tex:2665` is ill-typed and four
operator variables are declared as vectors, but these are repairable
notation/index defects rather than a counterexample or a missing
dimension-free estimate.
\end{minipage}}
\]
