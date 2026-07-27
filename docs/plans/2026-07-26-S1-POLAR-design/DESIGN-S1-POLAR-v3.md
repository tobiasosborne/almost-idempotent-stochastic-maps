# DESIGN — third repair of closed contracts for GAP-S1-POLAR-CONTRACT

Date: 2026-07-27  
Role: fresh independent repair designer  
Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND OR SEED before a fresh hostile audit and user ratification**

## 0. Verdict and exact delta from v2

**DESIGNED-CLOSABLE, now as thirteen factored analytic rows and six
downstream repairs.** This is a design verdict, not a proof or status
promotion. I found no route-level mathematical gap and no dimension-dependent
coefficient, but every new row below remains subject to a fresh hostile audit.

The direct-smoothness route is retained unchanged: the graph equation is a
degree-two polynomial of finite-dimensional real vector spaces; Lee C.40 makes
the already unique local graphs smooth and uniqueness glues them; the polar
map is then smooth, and Lee C.34/C.36 makes its already existing inverse smooth.
Munkres remains a checked fallback only. No approximation, new source, changed
map, changed fixed point, or changed first derivative is introduced.

Exactly the following changes are made to v2.

| v3 change | binding audit item forcing it |
|---|---|
| Replace compound `lem-stage1-unitary-chart-control` by `lem-stage1-unitary-graph-control` and `lem-stage1-maurer-cartan-trivialization`. | `AUDIT-S1-POLAR-v2.md` §§0.2, 4 (row 2), 10.1. |
| Replace compound `lem-stage1-smooth-unitary-polar-package` by `lem-stage1-smooth-unitary-atlas`, `lem-stage1-smooth-polar-inverse`, and `lem-stage1-smooth-unitary-operations`. | Audit §§0.2, 2.3, 4 (row 8), 10.1. |
| Replace v2's logically unthreaded ledger by a universal scalar-arithmetic row and a separate common-witness row whose conclusion explicitly says that the exact same tuple witnesses every parameterized analytic producer. | Audit §§0.1, 3, 4 (row 9), 7, 9.1, 9.2, 10.2. |
| Add an explicit quotient fixed-class phase-lift to `lem-stage1-quotient-inversion-index-data` and to the `lem-stage1-extra-fixed-class` obligation ledger. | Audit §§0.3, 5 (quotient-index row), 6, 9.1, 9.2, 10.3. |
| Correct group-law provenance: the two closeness estimates are derived from TeX 845–868 plus the polar retraction; only the three group defects are literal at TeX 872–874. | Audit §§0.4, 1 (TeX 857–893), 4 (group row), 9.1, 10.4. |
| State that `lem-stage1-rectified-cstar-control` reconstructs TeX 672–687 inside its own proof, including exact dagger compatibility, every \(C^*\)-axiom, and \(\lVert J\rVert=1\); it does not import unadvertised content from the weaker landed rectification contract. | Audit §§1 (TeX 655–687 and landed interfaces), 4 (rectification row), 9.1, 9.2, 10.4. |
| Replace all six downstream dependencies on the compound smooth row or unthreaded ledger by dependencies on the relevant factored producers and the genuine common-witness row. | Audit §§5–6 and brief carry-forward instruction. |

The contracts of v2 rows 3, 4, 6, and 7 are retained verbatim. The contracts
of the rectification and group-law rows are also retained verbatim; only their
named provenance/proof obligations change. The v2 scalar formulas and all
eight guards are retained verbatim in the new universal arithmetic row. The
contents of both proposed definition shards are retained verbatim.

## 1. Local-source and hash discipline

The relevant local payloads have the following SHA256 values:

- Kitaev TeX:
  `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`;
- Lee text:
  `324b7d8b1f70d40eb7608919e3c9cef93628215fa9e9f0816cb4c9549f058b3c`;
- Munkres text:
  `9fcbbac92a09926498c1caba8fafa61b1a3568033485b3977edc523cc0459e5d`.

The selected source interfaces are:

| local source | exact locus | use |
|---|---|---|
| Kitaev | `approximate_algebras.tex:407-440` | Complete \(\varepsilon\)-\(C^*\)-algebra and exact-unit axiom list. |
| Kitaev | `approximate_algebras.tex:458` | Each big-\(O\) is a concrete data-independent function; this permits named universal witnesses, not guessed numerical coefficients. |
| Kitaev | `approximate_algebras.tex:554-560` | A fixed two-factor direct-sum norm lies between max and sum; vector comparison costs at most \(2\), and source/target induced-operator comparisons may cost a second fixed factor. |
| Kitaev | `approximate_algebras.tex:655-687` | Multiplier/Neumann interfaces and the terse exact-unit rectification to be reconstructed, not silently strengthened. |
| Kitaev | `approximate_algebras.tex:692-807` | Approximate-unitary sets, right-inverse condition, graph estimates, normal derivative, tangent spaces, and Maurer–Cartan formula. |
| Kitaev | `approximate_algebras.tex:809-855` | \(C^1\) polar retraction, inverse identities, and inner/outer losses. |
| Kitaev | `approximate_algebras.tex:857-893` | Operations, adjoint/product polar domains, three literal group defects, and the typed inversion derivative; the printed second-variable derivative is not consumed. |
| Kitaev | `approximate_algebras.tex:895-912` | H-space/left-inversion prose; the projected straight-path right-inverse and domain steps must be derived. |
| Kitaev | `approximate_algebras.tex:943-955` | Isolation and quotient claims as prose only; the phase-lift is visible at 945 but is not a sufficient proof of quotient isolation. |
| Lee | `lee-smooth-manifolds-2ed.txt:31134-31137,31286-31298` | Smooth inverse function theorem and injective-everywhere gluing of the inverse. |
| Lee | `lee-smooth-manifolds-2ed.txt:31330-31344,31374-31385` | Local smooth implicit graph; uniqueness must identify the local graphs on overlaps. |
| Munkres | `munkres-elementary-differential-topology.txt:2055-2056,2533-2558` | Compatible smooth structures; checked fallback only. |
| Munkres | `munkres-elementary-differential-topology.txt:1833-1840,1888-1901` | \(C^r\)-to-\(C^p\) approximation; the relative statement is an exercise, and the route is not used. |
| Munkres | `munkres-elementary-differential-topology.txt:1509-1514,1596-1637` | Fine-\(C^1\) stability of immersions/embeddings and the boundary-qualified diffeomorphism result; checked fallback only. |

All needed direct-smoothness facts are in local refs; there is no
**NOT IN LOCAL REFS** escalation. The fallback does not supply equivariance or
fixed-point preservation and is therefore not used.

## 2. Witness-unification architecture

This design takes audit option **(a)**. Multiple downstream consumers need the
same rectification, graph, polar, group, path, and derivative ranges. Selecting
those witnesses once in the result DAG is smaller and safer than repeating the
selection and arithmetic independently at each analytic application.

The architecture has two distinct result rows:

1. `lem-stage1-polar-scalar-arithmetic` is universal over **every already
   selected tuple** satisfying only
   \(C_\bullet\ge1\),
   \(0<\kappa_\bullet\le\tfrac12\), and
   \(0<e_{\rm rect}\le1/C_{\rm rect}\). It proves scalar implications only and
   has no analytic dependency.
2. `lem-stage1-polar-constant-ledger` selects one tuple and says in its formal
   conclusion that, after replacing the leading existential constants in each
   named producer contract by the tuple's exact fields, the entire remaining
   universally quantified conclusion of every producer is simultaneously
   true. It then applies the universal arithmetic row to that same tuple.

Thus the consumer receives
\[
\exists W\,
  \bigl(\operatorname{AnalyticWitnesses}(W)
        \mathbin{\wedge}\operatorname{Arithmetic}(W)\bigr),
\]
not the invalid v2 pair consisting of
\(\exists W\,\operatorname{Arithmetic}(W)\) and unrelated existential
analytic theorems. The displayed phrase
“after replacing the leading existential constants” is included literally in
the common-witness contract below; it is not hidden in proof prose or in a
definition.

The unification proof chooses finite maxima of the producer coefficients and
finite minima of their margins. Every affected producer is monotone in the
needed direction: a larger coefficient and smaller admissibility margin
strengthen its antecedent and weaken its norm-bound conclusion. No smooth row
has a quantitative witness, so smoothness introduces no extra radius.

## 3. Factored formula-level proposal table

Every proposed row is at most a `stated` candidate. Dependencies are existing
registry ids or earlier rows in this table. Projected budgets are for the
already factored contracts, not promises to split a compound row later.

| # | proposed id | kind / status | one-line `contract:` value | defs | exact deps | provenance | projected af |
|---|---|---|---|---|---|---|---|
| 1 | `lem-stage1-rectified-cstar-control` | lemma / `stated` candidate | Controlled exact-unit \(C^*\)-rectification: there are universal \(C_{\rm rect}\ge1\) and \(e_{\rm rect}\in(0,1/C_{\rm rect}]\) such that every finite-dimensional \(\varepsilon_X\)-\(C^*\)-algebra with \(0\le\varepsilon_X\le e_{\rm rect}\) admits, on the same involutive normed space, a bilinear product \(\boldsymbol\cdot\) and \(J=J^\dagger\) for which \((\mathcal X,J,\boldsymbol\cdot,\dagger)\) satisfies **every** exact-unit \(\varepsilon_r\)-\(C^*\)-algebra axiom of `def-epsilon-cstar-algebra`, including \(\|J\|=1\), where \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), and \(\|J-I_X\|\le C_{\rm rect}\varepsilon_X\), \(\|x\boldsymbol\cdot y-xy\|\le C_{\rm rect}\varepsilon_X\|x\|\|y\|\). | `def-epsilon-cstar-algebra` | `lem-stage1-exact-unit-rectification`; `lem-stage1-quantitative-inverse-function` | TeX 407–440, 672–687. This row reconstructs the terse source proof internally; the weaker landed rectification contract supplies no hidden axiom. | 10 / 3 |
| 2 | `lem-stage1-unitary-graph-control` | lemma / `stated` candidate | Uniform unitary graph control: there are universal \(C_{\rm ch}\ge1\), \(\kappa_{\rm ch}\in(0,\tfrac12]\) such that for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), every \(V\in\overline{\mathcal U}_\delta\), and every \(A^\parallel\in B^{i\mathcal H}_{2\delta}(0)\), there is a unique \(g_V(A^\parallel)\in B^{\mathcal H}_{2\delta}(0)\) with \(f_V(A^\parallel+g_V(A^\parallel))=0\), and the corresponding \(V\boldsymbol\cdot(J+A^\parallel+g_V(A^\parallel))\) lies in \(\mathcal U\), where \(f_V(A)=\tfrac12(((J+A^\dagger)\boldsymbol\cdot V^\dagger)\boldsymbol\cdot(V\boldsymbol\cdot(J+A))-J)\); moreover \(\|g_V(A^\parallel)+\tfrac12(V^\dagger\boldsymbol\cdot V-J)\|\le C_{\rm ch}(\varepsilon_r\delta+\delta^2)\), \(\|Dg_V(A^\parallel)\|\le C_{\rm ch}(\varepsilon_r+\delta)\), and \(\|D_{A^\perp}f_V(A^\parallel+g_V(A^\parallel))-I_{\mathcal H}\|\le C_{\rm ch}(\varepsilon_r+\delta)<1\); the resulting \(C^1\) graph charts cover \(\mathcal U\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-quantitative-inverse-function`; `lem-stage1-rectified-cstar-control` | TeX 692–793, especially 728–793. | 8 / 3 |
| 3 | `lem-stage1-maurer-cartan-trivialization` | lemma / `stated` candidate | Uniform global tangent/Maurer–Cartan control: there are universal \(C_{\rm ch}\ge1\), \(\kappa_{\rm ch}\in(0,\tfrac12]\) such that for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), the graph maps supplied by `lem-stage1-unitary-graph-control` satisfy: every tangent space \(T_U\mathcal U\) is the image of \(L_U(I+Dg_U(0)):i\mathcal H\to\mathcal X\), and \(\omega_U(Z)=(L_U^{-1}Z)^\parallel:T_U\mathcal U\to i\mathcal H\) is a global \(C^1\) bundle trivialization with distortion at most \(1+C_{\rm ch}\varepsilon_r\), satisfying \(\omega_{cU}(cZ)=\omega_U(Z)\) and \(\omega_U(iU)=iJ\) for every \(c\in U(1)\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-unitary-graph-control` | TeX 795–807; the two equivariance identities are direct from the displayed formula and scalar bilinearity. | 4 / 2 |
| 4 | `lem-stage1-polar-retraction` | lemma / `stated` candidate | Closed \(C^1\) polar retraction: there are universal \(C_{\rm pol}\ge1\), \(\kappa_{\rm pol}\in(0,\tfrac12]\) such that for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\) is a \(C^1\) diffeomorphism from \(\mathcal U\times B^\mathcal H_\delta(J)\) onto an open \(S_\delta\), its inverse \((u_\delta,h_\delta)\) obeys \(X=u_\delta(X)\boldsymbol\cdot h_\delta(X)\), \(u_\delta(U)=U\), \(h_\delta(U)=J\), and \(\mathcal U_{\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\subseteq S_\delta\subseteq\mathcal U_{\delta+C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-unitary-graph-control` | TeX 809–855; the two radii are inlined and only the supported shrunken inner domain is used. | 12 / 3 |
| 5 | `lem-stage1-polar-coherence-naturality` | lemma / `stated` candidate | Polar coherence and scalar naturality: for every exact-unit algebra and every two polar data \((\delta_j,S_j,u_j,h_j)\), \(j=1,2\), for which \(\Pi_{\delta_j}:\mathcal U\times B^\mathcal H_{\delta_j}(J)\to S_j\), \((U,H)\mapsto U\boldsymbol\cdot H\), is bijective with inverse \((u_j,h_j)\), one has \((u_1,h_1)=(u_2,h_2)\) on \(S_1\cap S_2\); moreover, for \(c\in U(1)\) and \(X,cX\in S_j\), \(u_j(cX)=c\,u_j(X)\) and \(h_j(cX)=h_j(X)\). | `def-approximate-unitary-space` | `lem-stage1-polar-retraction` | TeX 809–845, 945; uniqueness and bilinearity derivation. | 3 / 2 |
| 6 | `lem-stage1-approximate-group-laws` | lemma / `stated` candidate | Quantitative approximate group laws: there exist universal \(C_{\rm grp},C_{\rm pol}\ge1\), \(\kappa_{\rm pol}\in(0,\tfrac12]\) such that for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and \(\delta>0\) satisfying \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\) and \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), the inverse \(u_\delta\) of the polar map defines \(C^1\) maps \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\), \(\sigma(U)=u_\delta(U^\dagger)\) on all of \(\mathcal U\), with \(\mu(J,U)=\mu(U,J)=U\), \(\sigma(J)=J\), \(\|\mu(U,V)-U\boldsymbol\cdot V\|\le C_{\rm grp}\varepsilon_r\), \(\|\sigma(U)-U^\dagger\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\mu(U,V),W)-\mu(U,\mu(V,W))\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\sigma(U),U)-J\|\le C_{\rm grp}\varepsilon_r\), and \(\|\mu(U,\sigma(U))-J\|\le C_{\rm grp}\varepsilon_r\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality` | **Corrected:** the two closeness estimates derive from TeX 845–868 plus `lem-stage1-polar-retraction`; only the three group defects are literal at TeX 872–874; basepoint identities are at 876–878. | 10 / 3 |
| 7 | `lem-stage1-polar-path-admissibility` | lemma / `stated` candidate | Joint projected-straight-path admissibility: there exist universal \(C_{\rm path},C_{\rm pol}\ge1\), \(\kappa_{\rm pol}\in(0,\tfrac12]\) such that, for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), and \(U_0,U_1\in\mathcal U\), if \(0\le q\le1\), \(\|U_1-U_0\|\le q\), \(C_{\rm path}q\le\tfrac14\), and \(C_{\rm path}(q+\varepsilon_rq+q^2)<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), then for \(Z_t=(1-t)U_0+tU_1\) every \(L_{Z_t}\) is invertible, every \(Z_t\in\overline{\mathcal U}_{C_{\rm path}(q+\varepsilon_rq+q^2)}\), and \(H(t,U_0,U_1)=u_\delta(Z_t)\) is jointly continuous in all displayed variables, joins \(U_0\) to \(U_1\), and obeys \(H(t,cU_0,cU_1)=cH(t,U_0,U_1)\) for \(c\in U(1)\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality` | TeX 895–912 plus derivation from 655–661, 699–725; exact identity \(Z_t^\dagger\boldsymbol\cdot Z_t-J=t(t-1)(U_1-U_0)^\dagger\boldsymbol\cdot(U_1-U_0)\). | 7 / 3 |
| 8 | `lem-stage1-inversion-derivative-control` | lemma / `stated` candidate | Typed inversion derivative with chart retention: there exist universal \(C_{\rm der},C_{\rm ch},C_{\rm pol},C_{\rm grp}\ge1\) and \(\kappa_{\rm der},\kappa_{\rm ch},\kappa_{\rm pol}\in(0,\tfrac12]\) such that for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, \(s\in\{\pm1\}\), and \(0<r\le\delta\) satisfying \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), \(C_{\rm der}(\varepsilon_r+r)\le\kappa_{\rm der}\), and \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta))r+C_{\rm grp}\varepsilon_r<2\delta\), the globally defined \(\sigma(U)=u_\delta(U^\dagger)\) maps \(\chi_s(B_r^{i\mathcal H}(0))\) into the same \(sJ\)-graph chart, where \(\chi_s(A)=sJ\boldsymbol\cdot(J+A+g_{sJ}(A))\), and \(F_s(A)=\phi_{sJ}^{\parallel}(\sigma(\chi_s(A)))\) satisfies \(\|D(F_s-\mathrm{id})(A)+2I_{i\mathcal H}\|\le C_{\rm der}(\varepsilon_r+r)\) for all \(A\in B_r^{i\mathcal H}(0)\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-unitary-graph-control`; `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality`; `lem-stage1-approximate-group-laws` | TeX 728–762, 857–892, 943; the group/adjoint-domain edge and chart-retention guard are explicit. | 10 / 3 |
| 9 | `lem-stage1-smooth-unitary-atlas` | lemma / `stated` candidate | Smooth graph-atlas upgrade: for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, if \(\mathcal U\) is covered by the unique \(C^1\) graph functions \(g_V\) of `lem-stage1-unitary-graph-control` and \(D_{A^\perp}f_V\) is invertible at every graph point, then those same \(g_V\) are \(C^\infty\), and the same graph charts make \(\mathcal U\) a smooth embedded manifold; no point or first derivative of a graph or chart is changed. | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-rectified-cstar-control`; `lem-stage1-unitary-graph-control` | Polynomiality from TeX 420–429, 692–793; Lee C.40 at txt:31330–31344, 31374–31385; overlap gluing is by graph uniqueness. | 3 / 2 |
| 10 | `lem-stage1-smooth-polar-inverse` | lemma / `stated` candidate | Smooth polar-inverse upgrade: for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\), if `lem-stage1-smooth-unitary-atlas` gives the smooth embedded atlas and \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to S_\delta\) is the bijective \(C^1\) local diffeomorphism of `lem-stage1-polar-retraction` onto an open set, then the same ambient-bilinear \(\Pi_\delta\) is a smooth diffeomorphism and its same set-theoretic inverse \((u_\delta,h_\delta)\) is smooth; no point or first derivative is changed. | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-smooth-unitary-atlas` | TeX 809–855; Lee C.34 at txt:31134–31137 and C.36 at txt:31286–31298, applied chartwise after the smooth-atlas row. | 4 / 3 |
| 11 | `lem-stage1-smooth-unitary-operations` | lemma / `stated` candidate | Smooth action/operations upgrade: under `lem-stage1-approximate-group-laws`, `lem-stage1-smooth-unitary-atlas`, and `lem-stage1-smooth-polar-inverse`, the scalar action \(U(1)\times\mathcal U\to\mathcal U\), \((c,U)\mapsto cU\), and the same maps \(\mu:\mathcal U\times\mathcal U\to\mathcal U\), \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\), and \(\sigma:\mathcal U\to\mathcal U\), \(\sigma(U)=u_\delta(U^\dagger)\), are smooth as maps into the embedded manifold \(\mathcal U\); they obey \(\mu(cU,dV)=cd\,\mu(U,V)\) and \(\sigma(cU)=\overline c\,\sigma(U)\), and no point or first derivative is changed. | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-coherence-naturality`; `lem-stage1-approximate-group-laws`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse` | TeX 857–868 for the domains; smoothness follows by restriction/corestriction of the ambient scalar, bilinear, and real-linear maps followed by the smooth polar inverse; scalar identities use polar coherence/naturality. | 4 / 2 |
| 12 | `lem-stage1-polar-scalar-arithmetic` | lemma / `stated` candidate | Universal Stage-1 polar arithmetic: for every \(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der}\ge1\), \(e_{\rm rect}\in(0,1/C_{\rm rect}]\), and \(\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der}\in(0,\tfrac12]\), setting \(\delta_*=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol})\}\), \(\varepsilon_*^r=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol}),\kappa_{\rm der}/(8C_{\rm der}),1/C_{\rm grp},\delta_*/(12C_{\rm path}C_{\rm grp})\}\), \(e_{\rm S1}=\min\{e_{\rm rect},\varepsilon_*^r/C_{\rm rect}\}\), \(r_{\rm iso}=\min\{\delta_*/4,\kappa_{\rm der}/(8C_{\rm der})\}\), \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), \(q=C_{\rm grp}\varepsilon_r\), \(r_-=\delta_*-C_{\rm pol}(\varepsilon_r\delta_*+\delta_*^2)\), and \(\eta=C_{\rm path}(q+\varepsilon_rq+q^2)\), every \(0\le\varepsilon_X\le e_{\rm S1}\) satisfies \(C_{\rm ch}(\varepsilon_r+\delta_*)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta_*)\le\kappa_{\rm pol}\), \(q<r_-\), \(C_{\rm path}q\le\tfrac14\), \(\eta<r_-\), \(C_{\rm der}(\varepsilon_r+r_{\rm iso})\le\kappa_{\rm der}\), and \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta_*))r_{\rm iso}+q<2\delta_*\); moreover \(r_-\ge3\delta_*/4\), \(\eta\le\delta_*/4\), and \(C_{\rm der}(r_{\rm iso}+\varepsilon_r)\le\kappa_{\rm der}/4<1\). | `def-stage1-polar-witness-data` | none | `AUDIT-S1-POLAR-v2.md` §3, which recomputes all eight guards exactly; pure scalar derivation. | 5 / 2 |
| 13 | `lem-stage1-polar-constant-ledger` | lemma / `stated` candidate | Compatible Stage-1 polar witnesses and range: there exists one universal `def-stage1-polar-witness-data` tuple \(W=(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der},e_{\rm rect},\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der},\delta_*,\varepsilon_*^r,e_{\rm S1},r_{\rm iso})\) such that, **after replacing the leading existential constants in the contracts of `lem-stage1-rectified-cstar-control`, `lem-stage1-unitary-graph-control`, `lem-stage1-maurer-cartan-trivialization`, `lem-stage1-polar-retraction`, `lem-stage1-approximate-group-laws`, `lem-stage1-polar-path-admissibility`, and `lem-stage1-inversion-derivative-control` by these exact corresponding fields, the entire remaining universally quantified conclusion of every one of those seven contracts is true simultaneously**; the four derived fields are exactly the finite-minimum values specified by `lem-stage1-polar-scalar-arithmetic`, and for this same \(W\) every \(0\le\varepsilon_X\le e_{\rm S1}\), with \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), \(q=C_{\rm grp}\varepsilon_r\), \(r_-=\delta_*-C_{\rm pol}(\varepsilon_r\delta_*+\delta_*^2)\), and \(\eta=C_{\rm path}(q+\varepsilon_rq+q^2)\), satisfies the full conclusion of `lem-stage1-polar-scalar-arithmetic`. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-rectified-cstar-control`; `lem-stage1-unitary-graph-control`; `lem-stage1-maurer-cartan-trivialization`; `lem-stage1-polar-retraction`; `lem-stage1-approximate-group-laws`; `lem-stage1-polar-path-admissibility`; `lem-stage1-inversion-derivative-control`; `lem-stage1-polar-scalar-arithmetic` | TeX 458 plus finite maxima/minima of the seven producer witnesses; monotonicity check in this section; audit §§3, 4, 7. | 10 / 3 |

Rows 9–11 are qualitative and introduce no smoothness threshold. Row 13 does
not depend on them and therefore stays below the brittleness cap; each
downstream consumer imports the particular smooth row it actually needs.

## 4. Per-row feasibility and proof obligations

| proposed id | verdict | exact derivation obligation |
|---|---|---|
| `lem-stage1-rectified-cstar-control` | **SUPPORTED-WITH-DERIVATION** | Reconstruct TeX 672–687 inside this row. Starting from its \(J_0,\boldsymbol\cdot_0\), prove bilinearity, product norm, associator bound, conjugate-linear isometric involution, exact \((x\boldsymbol\cdot_0y)^\dagger=y^\dagger\boldsymbol\cdot_0x^\dagger\), the lower \(C^*\)-bound, both exact unit laws, \(J_0^\dagger=J_0\), and unit closeness. For \(a=\lVert J_0\rVert>0\), set \(J=J_0/a\) and \(x\boldsymbol\cdot y=a(x\boldsymbol\cdot_0y)\); recheck every axiom and obtain \(\lVert J\rVert=1\). The landed `lem-stage1-exact-unit-rectification` contract supplies only its advertised exact-unit/product-closeness interface. |
| `lem-stage1-unitary-graph-control` | **SUPPORTED-WITH-DERIVATION** | Replace the fixed finite list of \(O(\varepsilon_r+\delta)\) and \(O(\varepsilon_r\delta+\delta^2)\) terms at TeX 758–793 by one coefficient/margin pair. The right-inverse and normal-derivative Neumann steps use TeX 699–725. |
| `lem-stage1-maurer-cartan-trivialization` | **SUPPORTED-WITH-DERIVATION** | Invert the graph tangent map from `lem-stage1-unitary-graph-control` to obtain TeX 795–807 globally. Derive \(\omega_{cU}(cZ)=\omega_U(Z)\) and \(\omega_U(iU)=iJ\) directly; no graph-existence work is repeated. |
| `lem-stage1-polar-retraction` | **SUPPORTED-WITH-DERIVATION** | TeX 809–843 supplies the \(C^1\) bijection and losses. Use the smaller inner set and never claim the unsupported larger line-845 source. |
| `lem-stage1-polar-coherence-naturality` | **SUPPORTED-WITH-DERIVATION** | Use injectivity on common decompositions; bilinearity gives the scalar identities. Its universal antecedent has no free polar witness. |
| `lem-stage1-approximate-group-laws` | **SUPPORTED-WITH-DERIVATION** | Prove \(U\boldsymbol\cdot V,U^\dagger\in S_\delta\), including right-invertibility, from TeX 845–868 and `lem-stage1-polar-retraction`. Derive the two closeness estimates there; telescope a fixed number of associators for the three defects literally printed at 872–874. |
| `lem-stage1-polar-path-admissibility` | **SUPPORTED-WITH-DERIVATION** | Use the exact quadratic identity and \(L_{Z_t}=L_{U_0}+tL_{U_1-U_0}\) with one Neumann comparison. Joint continuity and scalar equivariance use one open polar domain. |
| `lem-stage1-inversion-derivative-control` | **SUPPORTED-WITH-DERIVATION** | `lem-stage1-approximate-group-laws` supplies the all-\(\mathcal U\) adjoint domain. The explicit retention guard keeps \(\sigma(\chi_s(A))\) in the same chart, so coordinate equality is legitimate. The bad second-variable display at TeX 883–888 is unused. |
| `lem-stage1-smooth-unitary-atlas` | **SUPPORTED-WITH-DERIVATION** | The graph equation is a degree-two polynomial of real finite-dimensional spaces. Apply Lee C.40 pointwise and use `lem-stage1-unitary-graph-control` uniqueness on overlaps. |
| `lem-stage1-smooth-polar-inverse` | **SUPPORTED-WITH-DERIVATION** | The polar map is a smooth ambient-bilinear map after `lem-stage1-smooth-unitary-atlas`. The \(C^1\)-diffeomorphism property of `lem-stage1-polar-retraction` gives derivative invertibility. Apply Lee C.34/C.36 chartwise; global injectivity glues the inverse. |
| `lem-stage1-smooth-unitary-operations` | **SUPPORTED-WITH-DERIVATION** | The scalar action is a smooth ambient restriction/corestriction. `lem-stage1-approximate-group-laws` puts product and adjoint inputs in the polar domain; compose those smooth ambient maps with `lem-stage1-smooth-polar-inverse` and corestrict to the embedded manifold. |
| `lem-stage1-polar-scalar-arithmetic` | **SUPPORTED** | Audit §3 proves all displayed inequalities for every tuple with the stated sign/range hypotheses. No analytic selection occurs here. |
| `lem-stage1-polar-constant-ledger` | **SUPPORTED-WITH-DERIVATION** | Select witnesses from the seven analytic ids named in its contract; take finite maxima of coefficients and finite minima of margins. Check monotonicity contract by contract, state the exact simultaneous-substitution relation in the conclusion, and apply `lem-stage1-polar-scalar-arithmetic` to that same tuple. |

## 5. Corrected six downstream rows

All six rows are `stated` candidates. The contracts not named by the audit are
retained verbatim. Dependencies now use the factored smooth interfaces and
row 13's genuinely compatible tuple.

| proposed/corrected id | closed replacement contract | corrected exact deps | projected af |
|---|---|---|---|
| `lem-stage1-uniform-inversion-isolation` | There are universal \(e_{\rm iso}^r>0,r_{\rm iso}>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_{\rm iso}^r\), \(J\) and \(-J\) are the only fixed points of the smooth \(\sigma\) in their respective ambient \(r_{\rm iso}\)-balls. | `lem-stage1-quantitative-inverse-function`; `lem-stage1-inversion-derivative-control`; `lem-stage1-smooth-unitary-operations`; `lem-stage1-polar-constant-ledger` | 6 / 3 |
| `lem-stage1-quotient-manifold-package` | There is a universal \(e_{\rm quot}^r>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_{\rm quot}^r\) and \(1<N=\dim_\mathbb C\mathcal X<\infty\), \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a connected compact orientable **smooth** manifold without boundary of real dimension \(N-1\). | `lem-stage1-maurer-cartan-trivialization`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-unitary-operations`; `lem-stage1-polar-constant-ledger`; `lem-topology-quotient-manifold` | 8 / 3 |
| `lem-stage1-quotient-finite-cw` | For every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, if \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a compact smooth manifold without boundary, then \(\breve{\mathcal U}\) is homeomorphic to a finite simplicial complex and hence has finite CW type. | `lem-stage1-quotient-manifold-package`; `lem-topology-finite-triangulation` | 3 / 2 |
| `lem-stage1-quotient-left-inversion` | There is a universal \(e_H^r>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_H^r\), the scalar-equivariant \(\mu,\sigma\) and the jointly continuous projected straight paths descend to \(\breve{\mathcal U}\); the descended multiplication makes it a connected H-space, and the descended **smooth** map \(\breve\sigma\) is a left inversion. | `lem-stage1-polar-coherence-naturality`; `lem-stage1-approximate-group-laws`; `lem-stage1-polar-path-admissibility`; `lem-stage1-smooth-unitary-operations`; `lem-stage1-polar-constant-ledger`; `lem-stage1-quotient-manifold-package` | 8 / 3 |
| `lem-stage1-quotient-inversion-index-data` | There is a universal \(e_{\rm idx}^r>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_{\rm idx}^r\) and \(1<N=\dim_\mathbb C\mathcal X<\infty\), the scalar class \(\breve e=[J]\) is an isolated fixed point of the smooth \(\breve\sigma\), the vertical line \(i\mathbb RJ\) is \(D\sigma_J\)-invariant, \(\|D\breve\sigma_{\breve e}+I\|<1\) in the quotient norm, and \(\det(I-D\breve\sigma_{\breve e})>0\), so its local index is \(+1\); **more precisely, there is a quotient neighborhood \(\mathcal N\) of \([J]\) such that if \([U]\in\mathcal N\) is fixed, choose a representative \(U_0\) close to \(J\) and \(c\in U(1)\) with \(\sigma(U_0)=cU_0\), choose \(a\in U(1)\) with \(a^2=c\), and use \(\sigma(aU_0)=\overline a\,\sigma(U_0)=aU_0\): the two actual fixed lifts \(\pm aU_0\) lie in the \(J\)- and \(-J\)-isolation balls, hence equal \(J\) and \(-J\), so \([U]=[J]\)**. | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-polar-coherence-naturality`; `lem-stage1-inversion-derivative-control`; `lem-stage1-smooth-unitary-operations`; `lem-stage1-polar-constant-ledger`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-left-inversion`; `lem-topology-local-index-sign` | 9 / 3 |
| `lem-finite-polyhedron-maximal-simplex-placement` | Every point of a finite polyhedron lies in a maximal simplex of its defining finite simplicial complex; therefore every finite fixed set does. | none (finite-poset derivation) | 2 / 1 |

The phase-lift proof must include the neighborhood estimate suppressed by the
one-line contract: quotient closeness selects \(U_0\) close to \(J\);
continuity and \(\sigma(J)=J\) make the quotient phase \(c\) close to \(1\);
its two square roots can be labelled so that \(aU_0\) is in the \(J\)-ball
and \(-aU_0\) is in the \(-J\)-ball. This is a qualitative neighborhood
shrink inside the already fixed isolation radius, not a new analytic
coefficient. The contract records the lift because actual isolation alone
does not imply quotient isolation.

At Route-F assembly, first select the one rectification and row-13 tuple, then
use the same original-scale threshold retained from v2:
\[
 e_F=\min\left\{e_{\rm S1},
 \frac{e_{\rm iso}^r}{C_{\rm rect}},
 \frac{e_{\rm quot}^r}{C_{\rm rect}},
 \frac{e_H^r}{C_{\rm rect}},
 \frac{e_{\rm idx}^r}{C_{\rm rect}}\right\}.
\]
Thus every consumer uses one fixed rectified algebra and one fixed analytic
tuple.

## 6. Corrected obligation ledger for `lem-stage1-extra-fixed-class`

| landed/proposed consumer obligation | exact input needed | discharge |
|---|---|---|
| Actual inversion isolation near \(J,-J\) | Dimension-free actual isolation in the two ambient balls. | `lem-stage1-uniform-inversion-isolation`. |
| Quotient isolation of \([J]\) | A quotient-fixed class near \([J]\) must be phase-lifted to actual fixed points before ambient isolation is used. | The explicit square-root/scalar-naturality clause inside `lem-stage1-quotient-inversion-index-data`; isolation alone is not cited. |
| Connected compact orientable positive-dimensional smooth quotient | Smooth embedded atlas/action, free proper scalar action, quotient dimension, closedness, and Maurer–Cartan orientation. | `lem-stage1-quotient-manifold-package` from rows 3, 9, 11 and `lem-topology-quotient-manifold`. |
| Finite polyhedron / finite CW | A compact smooth boundaryless manifold before triangulation. | `lem-stage1-quotient-finite-cw`; its status cannot outrun the currently `stated/seeded` triangulation dependency. |
| Continuous H-space and left inversion; smooth \(\breve\sigma\) | Scalar-equivariant operations and joint projected paths. | `lem-stage1-quotient-left-inversion` from rows 5–7 and 11. |
| Left-inversion trace | Connected finite-CW H-space with left inversion. | `lem-stage1-quotient-finite-cw`; `lem-stage1-quotient-left-inversion`; the separately designed `lem-stage1-left-inversion-trace`. |
| Lefschetz-Hopf maximal-simplex placement | Under the only-fixed-class contradiction, the fixed set is finite and lies in maximal simplices of the chosen finite triangulation. | `lem-finite-polyhedron-maximal-simplex-placement` plus `lem-topology-lefschetz-hopf`. |
| Local index \(+1\) | Smooth quotient self-map, genuine quotient isolation, and positive \(\det(I-D\breve\sigma)\). | `lem-stage1-quotient-inversion-index-data`; `lem-topology-local-index-sign`. |
| Nonzero top cohomology and \(\Lambda(\breve\sigma)\ge2\) | Connected compact orientable positive-dimensional boundaryless quotient; degree-zero and top-degree cohomology; trace formula. | `lem-stage1-quotient-manifold-package`; `lem-topology-orientable-top-cohomology`; `lem-stage1-left-inversion-trace`. |

The corrected dependency list for `lem-stage1-extra-fixed-class` is therefore:

1. `lem-stage1-uniform-inversion-isolation`;
2. `lem-stage1-quotient-manifold-package`;
3. `lem-stage1-quotient-finite-cw`;
4. `lem-stage1-quotient-left-inversion`;
5. `lem-stage1-left-inversion-trace`;
6. `lem-topology-lefschetz-hopf`;
7. `lem-topology-local-index-sign`;
8. `lem-topology-orientable-top-cohomology`;
9. **`lem-stage1-quotient-inversion-index-data`**;
10. **`lem-finite-polyhedron-maximal-simplex-placement`**.

Items 9–10 are the additions required by the audits. The phase-lift is a
proof obligation and contract clause of item 9, not an unstated inference in
`lem-stage1-extra-fixed-class`.

## 7. Dimension-freeness audit

Factoring changes no quantitative conclusion. It only assigns already
existing interfaces to separate rows.

| constant / step | dimension-freeness check |
|---|---|
| \(C_{\rm rect},e_{\rm rect}\) | Fixed-term product comparisons, operator-norm Neumann inversion, and one scalar normalization \(a=\lVert J_0\rVert\); no basis sum. Reconstructing all axioms adds only a fixed list of terms. |
| \(C_{\rm ch},\kappa_{\rm ch}\) | Quantitative IFT in Banach/operator norms. The tangent/normal split has exactly two factors. Vector max/sum conversion costs at most \(2\); induced-operator comparison on source and target may cost one further fixed factor. Splitting graph and Maurer–Cartan rows adds no estimate. |
| \(C_{\rm pol},\kappa_{\rm pol}\) | One two-block derivative and a fixed Neumann margin; the blocks are tangent/normal, not amplification blocks. |
| \(C_{\rm grp}\) | A fixed number of products, associators, and polar retractions. Correcting provenance changes no term count. |
| \(C_{\rm path}\) | One exact quadratic identity and one Neumann comparison. |
| \(C_{\rm der},\kappa_{\rm der}\) | Operator-norm multiplier formula; quotienting cannot enlarge the induced error once the vertical line is invariant. |
| Smooth atlas | Lee C.40 is qualitative. Euclidean coordinates are used only to infer smoothness; no smoothness radius or norm modulus is exported. |
| Smooth polar inverse | Lee C.34/C.36 is qualitative and is applied to the already controlled map. No coordinate norm-equivalence constant enters a quantitative conclusion. |
| Smooth action/operations | Restriction/corestriction and composition of a fixed scalar, bilinear, real-linear, and smooth-polar map; no new coefficient. |
| Witness unification | Finite maxima/minima over seven fixed producer packages; the number seven is absolute. |
| Compactness/closedness | Finite dimension is used qualitatively for bounded-closed compactness and injective \(\Rightarrow\) surjective, never to select a coefficient. |
| Quotient/orientation/index/phase-lift | \(U(1)\) and the vertical line are fixed-dimensional. The quotient norm does not enlarge the derivative error. The determinant homotopy \(2I-tE\) and the phase square root are qualitative and dimension-free. |
| Amplification/block/stage | No entrywise sum, block count, number of stages, or amplification level occurs. The estimates apply verbatim whenever an amplified algebra satisfies the same axioms. |

**DIMENSION-FREENESS VERDICT: PASS AT DESIGN LEVEL; NO ROUTE-LEVEL ALARM.**
Any proof that introduces an unquantified compactness modulus, a
dimension-dependent Euclidean norm conversion, or a basis/entrywise sum must
be challenged.

## 8. Definition provisioning (unchanged from v2)

| proposed def id | kind/status | exact theorem-free content | provenance/rationale |
|---|---|---|---|
| `def-approximate-unitary-space` | `consensus` / `draft` pending sign-off | For an exact-unit \(\varepsilon\)-\(C^*\)-algebra define \(\mathcal H=\{X:X^\dagger=X\}\), \(i\mathcal H=\{X:X^\dagger=-X\}\), \(\mathcal U\), \(\overline{\mathcal U}_\delta\), \(\mathcal U_\delta\), and \(\mathcal U_e\). For a \(V\) for which \(L_V\) is invertible, reserve \(\phi_V(X)=L_V^{-1}(X-V)\) and its \(\parallel,\perp\) components as **coordinate notation only**. Reserve \(u,h,\mu,\sigma\) only as partial notation on domains supplied by result rows. Assert no chart, inverse, estimate, smoothness, compactness, orientation, or isolation theorem. | TeX 692–750, 845–859; first audit §6 and re-audit §7. |
| `def-stage1-polar-witness-data` | `original` / `draft` pending sign-off | A tuple of named scalar fields \(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der},e_{\rm rect},\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der},\delta_*,\varepsilon_*^r,e_{\rm S1},r_{\rm iso}\). It is data and typing only: it contains no positivity, inequality, existence, uniqueness, estimate, map, regularity, admissibility, or topological assertion. | R35; the analytic-witness relation is exported only by row 13. |

No definition contains \(r_\pm\), \(\eta_{\rm path}\), a validity predicate, or
any theorem conclusion. The two definition contents are unchanged because the
re-audit found them valid as data.

## 9. Genuine serial landing order

This is a topological sort, not authorization to land. Every item remains
gated by fresh hostile re-audit and user ratification.

1. Ratify and land the unchanged datum-only
   `def-approximate-unitary-space` and
   `def-stage1-polar-witness-data`.
2. Land `lem-stage1-rectified-cstar-control`.
3. Land `lem-stage1-unitary-graph-control`.
4. Land `lem-stage1-maurer-cartan-trivialization`.
5. Land `lem-stage1-polar-retraction`.
6. Land `lem-stage1-polar-coherence-naturality`.
7. Land `lem-stage1-approximate-group-laws`.
8. Land `lem-stage1-polar-path-admissibility`.
9. Land `lem-stage1-inversion-derivative-control`.
10. Land `lem-stage1-smooth-unitary-atlas`.
11. Land `lem-stage1-smooth-polar-inverse`.
12. Land `lem-stage1-smooth-unitary-operations`.
13. Land `lem-stage1-polar-scalar-arithmetic`.
14. Land `lem-stage1-polar-constant-ledger`.
15. Land `lem-finite-polyhedron-maximal-simplex-placement` (independent).
16. Land `lem-stage1-uniform-inversion-isolation`.
17. Land `lem-stage1-quotient-manifold-package`.
18. Land `lem-stage1-quotient-finite-cw`.
19. Land `lem-stage1-quotient-left-inversion`.
20. Land `lem-stage1-quotient-inversion-index-data`, including the phase-lift.
21. Land the separately designed `lem-stage1-exterior-cohomology`,
    `lem-stage1-left-inversion-associated-graded`, and
    `lem-stage1-left-inversion-trace`, in that order, unless they are already
    present from their own audited campaign.
22. Land the corrected `lem-stage1-extra-fixed-class` with all ten
    dependencies in §6.

No row consumes a later row. The currently `stated/seeded`
`lem-topology-finite-triangulation` prevents its consumer from being promoted
beyond its honest dependency status.

## 10. Disposition of every `AUDIT-S1-POLAR-v2.md` finding

Every audit finding is accepted. None is refuted, and no new gap is escalated.
The allowed disposition vocabulary below is therefore `CLEARED-BY`
throughout; that means “addressed in this design,” not “proved.”

### 10.1 Final-disposition and local-source findings

| audit finding | disposition |
|---|---|
| §0.1 ledger does not thread compatible witnesses | **CLEARED-BY** §2 and rows 12–13: pure universal arithmetic is separate, and row 13 explicitly substitutes one exact tuple into all seven producer conclusions. |
| §0.2 rows 2 and 8 are compound | **CLEARED-BY** rows 2–3 and 9–11; the splits are made now. |
| §0.3 quotient isolation omits the phase-lift | **CLEARED-BY** the expanded quotient-index contract in §5 and the separate obligation in §6. |
| §0.4 group provenance is false as written | **CLEARED-BY** row 6's corrected provenance and the matching disposition below. |
| §1 hashes / locked definition prefix | **CLEARED-BY** §1's recomputed hashes and `def-epsilon-cstar-algebra` locus. |
| §1 TeX 407–440 complete axiom list | **CLEARED-BY** row 1 and its feasibility plan, which enumerates and reconstructs every axiom. |
| §1 TeX 458 named witnesses only | **CLEARED-BY** rows 12–13; no numerical coefficient is guessed. |
| §1 TeX 560 direct-sum/operator comparison | **CLEARED-BY** §7's two-stage fixed-factor accounting. |
| §1 TeX 655–687 terse rectification | **CLEARED-BY** row 1's explicit in-tree reconstruction and non-use of hidden proof-export content. |
| §1 TeX 692–725 right-inverse and Neumann interface | **CLEARED-BY** rows 2, 6, and 7 feasibility obligations. |
| §1 TeX 728–807 is \(C^1\) and row 2 compound | **CLEARED-BY** rows 2–3 and the separate smooth row 9. |
| §1 TeX 809–855 polar losses / smaller domain | **CLEARED-BY** retained row 4, verbatim contract. |
| §1 TeX 857–893 domains, defects, provenance, erratum | **CLEARED-BY** row 6's corrected split provenance and row 8's non-use of the bad second-variable display. |
| §1 TeX 895–912 straight-path omissions / type typo | **CLEARED-BY** retained row 7 and reuse of locked `def-h-space-left-inversion`. |
| §1 TeX 943–955 insufficient provenance | **CLEARED-BY** independent rows 9–11, the downstream quotient/index rows, and the explicit phase-lift. |
| §1 Lee C.34/C.36 | **CLEARED-BY** row 10 with exact txt loci. |
| §1 Lee C.40 local graph only | **CLEARED-BY** row 9, whose proof obligation uses row-2 uniqueness to glue. |
| §1 Munkres 4.9/5.11 fallback only | **CLEARED-BY** §1: pinned but not consumed. |
| §1 Munkres 4.2 relative form is an exercise | **CLEARED-BY** §1's scope callout; not consumed. |
| §1 Munkres 3.10 boundary qualification | **CLEARED-BY** §1's exact qualification; not consumed. |
| §1 landed quantitative IFT is not smooth IFT | **CLEARED-BY** rows 9–10 depend on Lee, not on an unadvertised landed interface. |
| §1 landed rectification contract is weak | **CLEARED-BY** row 1 reconstructs the stronger package in its own tree. |
| §1 landed quotient theorem requires smooth data | **CLEARED-BY** downstream quotient deps on rows 9 and 11. |
| §1.1 deliverable scope not narrowed | **CLEARED-BY** thirteen analytic rows, six downstream rows, definitions, dimension audit, and unblocking order in §§3–9. |

### 10.2 Direct-smoothness and arithmetic findings

| audit finding | disposition |
|---|---|
| §2.1 graph equation is smooth polynomial; local graphs glue by uniqueness | **CLEARED-BY** rows 2 and 9 with TeX 420–429, 742–793 and Lee C.40. |
| §2.2 polar inverse is smooth after atlas upgrade | **CLEARED-BY** row 10 with Lee C.34/C.36. |
| §2.3 scalar action and \(\mu,\sigma\) are smooth into the embedded manifold | **CLEARED-BY** row 11, separated from rows 9–10. |
| §2.3 unchanged first derivatives | **CLEARED-BY** explicit “no point or first derivative is changed” clauses in rows 9–11. |
| §3 all eight scalar guards recompute exactly | **CLEARED-BY** row 12, copied without numerical change. |
| §3 arithmetic was logically disconnected from analytic witnesses | **CLEARED-BY** row 13's exact simultaneous-substitution relation. |

### 10.3 Verdict per v2 analytic row

| v2 row finding | disposition |
|---|---|
| Rectified control valid with reconstruction correction | **CLEARED-BY** row 1 and §4's every-axiom reconstruction. |
| Unitary chart row refuted as atomic | **CLEARED-BY** rows 2–3. |
| Polar retraction valid | **CLEARED-BY** retained row 4 verbatim. |
| Coherence/naturality valid | **CLEARED-BY** retained row 5 verbatim. |
| Group laws valid with corrected provenance | **CLEARED-BY** retained contract and corrected row-6 provenance. |
| Path admissibility valid | **CLEARED-BY** retained row 7 verbatim. |
| Inversion derivative valid | **CLEARED-BY** retained row 8 verbatim with factored graph dep. |
| Smooth package refuted as atomic; direct route valid | **CLEARED-BY** rows 9–11. |
| Constant ledger refuted compositionally; arithmetic valid | **CLEARED-BY** rows 12–13. |
| §4 dependency order otherwise acyclic | **CLEARED-BY** tables in §§3, 5 and topological sort §9. |
| §4 projected counts cannot excuse compound rows | **CLEARED-BY** mandatory factoring before projection; every row is at most 12/depth 3. |

### 10.4 Verdict per downstream row and fixed-class obligation

| audit finding | disposition |
|---|---|
| Isolation needs factored smooth rows and compatible range | **CLEARED-BY** corrected deps on rows 8, 11, 13. |
| Quotient manifold needs factored atlas/action and Maurer–Cartan rows | **CLEARED-BY** corrected deps on rows 3, 9, 11, 13. |
| Quotient finite-CW contract is valid but dependency remains non-rigorous | **CLEARED-BY** retained contract and explicit status warning in §§5, 9. |
| Quotient left inversion needs factored operations and corrected range | **CLEARED-BY** corrected deps on rows 5–7, 11, 13. |
| Quotient index needs phase-lift | **CLEARED-BY** expanded contract and proof obligation in §5. |
| Maximal-simplex placement valid | **CLEARED-BY** retained sixth downstream contract. |
| Actual isolation obligation | **CLEARED-BY** first row of §6. |
| Quotient isolation additionally needs phase-lift | **CLEARED-BY** second row of §6. |
| Smooth quotient obligation | **CLEARED-BY** third row of §6. |
| Finite-CW obligation | **CLEARED-BY** fourth row of §6. |
| H-space/left-inversion and smooth \(\breve\sigma\) obligation | **CLEARED-BY** fifth row of §6. |
| Left-inversion trace obligation | **CLEARED-BY** sixth row of §6 with no new polar claim. |
| Lefschetz maximal-simplex obligation | **CLEARED-BY** seventh row of §6. |
| Local index \(+1\) subject to quotient isolation | **CLEARED-BY** eighth row of §6 and phase-lifted index row. |
| Top cohomology and Lefschetz-number comparison | **CLEARED-BY** ninth row of §6. |
| Extra-fixed dependency list must add quotient-index and maximal-simplex rows | **CLEARED-BY** explicit ten-id list in §6. |

### 10.5 Definition and dimension findings

| audit finding | disposition |
|---|---|
| `def-approximate-unitary-space` valid | **CLEARED-BY** unchanged first definition row in §8. |
| `def-stage1-polar-witness-data` valid as data, invalid as threading theorem | **CLEARED-BY** unchanged data row plus result-level relation in row 13. |
| No guessed numerical constant needed | **CLEARED-BY** TeX 458 discipline and rows 12–13. |
| Rectification dimension-free | **CLEARED-BY** §7 rectification row. |
| Charts/polar dimension-free | **CLEARED-BY** §7 chart/polar rows. |
| Group/path/derivative dimension-free | **CLEARED-BY** §7 corresponding rows. |
| Smooth upgrade qualitative and dimension-free | **CLEARED-BY** three separate smooth rows in §7. |
| Compactness/closedness qualitative | **CLEARED-BY** §7 compactness row. |
| Quotient/orientation/index dimension-free | **CLEARED-BY** §7 quotient row, including phase-lift. |
| Amplification/block/stage independence | **CLEARED-BY** final row of §7. |
| §8 overall no route-level alarm | **CLEARED-BY** explicit design-level verdict in §7. |

### 10.6 Every v2 §9 disposition claim re-audited in the binding audit

| binding re-audit finding | disposition |
|---|---|
| §9.1 \(C^1\)-versus-smooth blocker valid with factoring correction | **CLEARED-BY** rows 9–11. |
| §9.1 free witnesses/naked formulas refuted | **CLEARED-BY** rows 12–13; formulas are inlined. |
| §9.1 missing group-to-derivative edge valid | **CLEARED-BY** row 8 dep on row 6. |
| §9.1 TeX 458 use valid | **CLEARED-BY** §2 and rows 12–13. |
| §9.1 TeX 560 clarification valid | **CLEARED-BY** §7. |
| §9.1 straight-path inverse guard valid | **CLEARED-BY** row 7. |
| §9.1 full rectification valid with weak-contract correction | **CLEARED-BY** row 1 proof plan. |
| §9.1 TeX 692–725 requires actual Neumann/right-inverse step | **CLEARED-BY** §4 graph/group/path obligations. |
| §9.1 TeX 728–807 smooth repair valid but factoring required | **CLEARED-BY** rows 2–3 and 9. |
| §9.1 TeX 809–843 inline radii valid | **CLEARED-BY** row 4. |
| §9.1 TeX 845–855 mismatch/typo handling valid | **CLEARED-BY** row 4 and non-use callout. |
| §9.1 TeX 857–880 provenance needs correction | **CLEARED-BY** row 6 corrected provenance. |
| §9.1 TeX 881–893 repeated denominator non-use valid | **CLEARED-BY** row 8 feasibility note. |
| §9.1 TeX 895–912 omission/type repair valid | **CLEARED-BY** row 7 and locked definition. |
| §9.1 TeX 943–955 closure needs factoring/witness/phase repairs | **CLEARED-BY** §§3, 5, 6. |
| §9.1 coherence row has no free polar witness | **CLEARED-BY** retained row 5. |
| §9.1 derivative target chart retention valid | **CLEARED-BY** retained row 8. |
| §9.1 ledger logical closure refuted | **CLEARED-BY** row 13's formal analytic-witness relation. |
| §9.2 explicit smooth producer needs factoring | **CLEARED-BY** rows 9–11. |
| §9.2 witness threading refuted | **CLEARED-BY** §2 and row 13. |
| §9.2 chart row cap/compoundness refuted | **CLEARED-BY** rows 2–3 with separate budgets. |
| §9.2 derivative descent/same-chart/determinant needs phase-lift | **CLEARED-BY** row 8 plus phase-lifted quotient-index row. |
| §9.2 quotient regularity/closedness/orientation needs factored deps | **CLEARED-BY** corrected quotient-manifold deps. |
| §9.2 left inversion needs factored operations/witnesses | **CLEARED-BY** corrected quotient-left-inversion deps. |
| §9.2 smooth manifold/triangulation/local index needs phase-lift | **CLEARED-BY** §§5–6. |
| §9.2 maximal-simplex placement valid | **CLEARED-BY** sixth downstream row. |
| §9.2 qualified \(\phi_V\) valid | **CLEARED-BY** unchanged §8 definition. |
| §9.2 controlled rectification needs honest reconstruction | **CLEARED-BY** row 1. |
| §9.2 straight-path gap valid | **CLEARED-BY** row 7. |
| §9.2 source-radius mismatch valid | **CLEARED-BY** row 4. |
| §9.2 derivative typing valid | **CLEARED-BY** row 8. |
| §9.2 no numerical polar constants valid | **CLEARED-BY** rows 12–13. |
| §9.2 bundled smoothness/free-witness/missing-dep claim refuted as bundle | **CLEARED-BY** separate repairs: rows 9–11, row 13, and row-8 dep on row 6. |
| §9.2 direct-sum/operator-norm correction valid | **CLEARED-BY** §7. |
| §9.2 qualitative smooth upgrade valid | **CLEARED-BY** rows 9–10. |
| §9.2 expand every rectified axiom | **CLEARED-BY** row 1 feasibility obligation. |
| §9.2 qualify \(\phi_V\) | **CLEARED-BY** unchanged §8 definition. |
| §9.2 complete fixed-class plan needs phase-lift | **CLEARED-BY** §6. |
| §9.2 finite-minimum arithmetic valid only arithmetically | **CLEARED-BY** separation into rows 12 and 13. |
| §10.1 factor graph/MC and three smooth interfaces | **CLEARED-BY** five rows 2–3 and 9–11. |
| §10.2 export actual common-witness relation | **CLEARED-BY** option (a), rows 12–13. |
| §10.3 add quotient phase-lift | **CLEARED-BY** §5 index contract and §6 ledger. |
| §10.4 correct group and rectification provenance | **CLEARED-BY** rows 1 and 6 plus §4. |
| §10 final decision: do not land v2; redesign then re-audit | **CLEARED-BY** this v3 design's status ceiling and mandatory fresh-audit gate. |

## 11. Final unblocking map

| formerly blocked interface | v3 disposition |
|---|---|
| `lem-stage1-inversion-derivative-control` | Formula-level, factored-dependency-closed, and tied to the common analytic tuple; still only a `stated` candidate. |
| `lem-stage1-quotient-manifold-package` | Transcribable in the corrected smooth form from the separate atlas, action, Maurer–Cartan, quotient, and common-range producers. |
| `lem-stage1-quotient-left-inversion` | Transcribable from scalar-equivariant smooth operations and joint path admissibility on the same tuple. |
| `lem-stage1-quotient-inversion-index-data` | Transcribable only with the explicit square-root phase-lift in its contract and proof. |
| `lem-stage1-extra-fixed-class` | Dependency-complete at design level only with the quotient-index and maximal-simplex rows added and the phase-lift consumed through the quotient-index row. |

The correct next action is a **fresh hostile audit of this v3 design**. Nothing
here lands a registry row, mutates a definition, promotes a status, or proves
Route F or `op-classical`.
