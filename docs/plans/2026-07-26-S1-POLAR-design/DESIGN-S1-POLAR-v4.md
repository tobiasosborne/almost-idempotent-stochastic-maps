# DESIGN — fourth repair of closed contracts for GAP-S1-POLAR-CONTRACT

Date: 2026-07-27  
Role: fresh independent repair designer  
Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND OR SEED before a fresh hostile audit and user ratification**

## 0. Verdict and exact delta from v3

**DESIGNED-CLOSABLE, still as thirteen factored analytic rows and six
downstream repairs.** This is a design verdict, not a proof or status
promotion. I found no route-level mathematical gap and no dimension-dependent
coefficient, but every new row below remains subject to a fresh hostile audit.

Exactly two changes are made to v3; everything else is carried forward.

| v4 change | binding audit item forcing it |
|---|---|
| Replace the meta-level row-13 contract by one object-level existential tuple whose seven analytic clauses restate the parameterized conclusions for rectification, graph control, Maurer–Cartan control, polar retraction, group laws, path admissibility, and inversion derivative control, and whose arithmetic clause states the four exact finite-minimum equations and every scalar conclusion. Re-project the resulting root as \(11/3\), within the \(12\)-node/depth-\(3\) cap. | `AUDIT-S1-POLAR-v3.md` §§0.1, 2, 4 (row 13), 7.3, 8, 9.1–9.2. |
| Add the six downstream rows' exact `defs` metadata, including an explicit `none` for maximal-simplex placement; no downstream contract or dependency changes. | `AUDIT-S1-POLAR-v3.md` §§0.2, 5, 9.4. |

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

This design retains audit option **(a)**. Multiple downstream consumers need the
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
2. `lem-stage1-polar-constant-ledger` selects one tuple and states an
   object-level conjunction. Seven clauses quantify directly over the
   algebras, graph maps \(g_V\), polar inverse \((u_\delta,h_\delta)\), group
   maps \(\mu,\sigma\), scales, and estimates appearing in the analytic
   conclusions. The eighth clause gives the four finite-minimum equations and
   every scalar consequence for that same tuple.

Thus the consumer receives the literal mathematical assertion
\[
\exists W\,
  \bigl(\operatorname{AnalyticWitnesses}(W)
        \mathbin{\wedge}\operatorname{Arithmetic}(W)\bigr),
\]
not the invalid v2 pair consisting of
\(\exists W\,\operatorname{Arithmetic}(W)\) and unrelated existential
analytic theorems. Both predicates are expanded in the contract itself; they
are not textual operations or definition-level validity predicates.

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
| 13 | `lem-stage1-polar-constant-ledger` | lemma / `stated` candidate | Compatible Stage-1 polar witnesses and range: there exists one universal `def-stage1-polar-witness-data` tuple \(W=(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der},e_{\rm rect},\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der},\delta_*,\varepsilon_*^r,e_{\rm S1},r_{\rm iso})\), with \(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der}\ge1\), \(0<e_{\rm rect}\le1/C_{\rm rect}\), and \(0<\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der}\le\tfrac12\), such that all of the following hold simultaneously: \((A_1)\) for every finite-dimensional \(\varepsilon_X\)-\(C^*\)-algebra \((\mathcal X,I_X,\cdot,\dagger)\) with \(0\le\varepsilon_X\le e_{\rm rect}\), there are on the same involutive normed space a bilinear product \(\boldsymbol\cdot\) and an element \(J=J^\dagger\) for which \((\mathcal X,J,\boldsymbol\cdot,\dagger)\) satisfies every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra axiom of `def-epsilon-cstar-algebra`, including \(\|J\|=1\), where \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), and for every \(x,y\in\mathcal X\), \(\|J-I_X\|\le C_{\rm rect}\varepsilon_X\) and \(\|x\boldsymbol\cdot y-xy\|\le C_{\rm rect}\varepsilon_X\|x\|\|y\|\); \((A_2)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra \((\mathcal X,J,\boldsymbol\cdot,\dagger)\), every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), every \(V\in\overline{\mathcal U}_\delta\), and every \(A^\parallel\in B^{i\mathcal H}_{2\delta}(0)\), there is a unique \(g_V(A^\parallel)\in B^\mathcal H_{2\delta}(0)\) such that \(f_V(A^\parallel+g_V(A^\parallel))=0\), where \(f_V(A)=\tfrac12(((J+A^\dagger)\boldsymbol\cdot V^\dagger)\boldsymbol\cdot(V\boldsymbol\cdot(J+A))-J)\), the element \(V\boldsymbol\cdot(J+A^\parallel+g_V(A^\parallel))\) lies in \(\mathcal U\), \(\|g_V(A^\parallel)+\tfrac12(V^\dagger\boldsymbol\cdot V-J)\|\le C_{\rm ch}(\varepsilon_r\delta+\delta^2)\), \(\|Dg_V(A^\parallel)\|\le C_{\rm ch}(\varepsilon_r+\delta)\), and \(\|D_{A^\perp}f_V(A^\parallel+g_V(A^\parallel))-I_{\mathcal H}\|\le C_{\rm ch}(\varepsilon_r+\delta)<1\), and these \(C^1\) graph charts cover \(\mathcal U\); \((A_3)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), and the family of unique graph maps \(g_U:B^{i\mathcal H}_{2\delta}(0)\to B^\mathcal H_{2\delta}(0)\) characterized for every \(U\in\mathcal U\) and \(A^\parallel\in B^{i\mathcal H}_{2\delta}(0)\) by \(f_U(A^\parallel+g_U(A^\parallel))=0\), \(f_U(A)=\tfrac12(((J+A^\dagger)\boldsymbol\cdot U^\dagger)\boldsymbol\cdot(U\boldsymbol\cdot(J+A))-J)\), \(U\boldsymbol\cdot(J+A^\parallel+g_U(A^\parallel))\in\mathcal U\), \(\|g_U(A^\parallel)+\tfrac12(U^\dagger\boldsymbol\cdot U-J)\|\le C_{\rm ch}(\varepsilon_r\delta+\delta^2)\), \(\|Dg_U(A^\parallel)\|\le C_{\rm ch}(\varepsilon_r+\delta)\), and \(\|D_{A^\perp}f_U(A^\parallel+g_U(A^\parallel))-I_{\mathcal H}\|\le C_{\rm ch}(\varepsilon_r+\delta)<1\), every tangent space \(T_U\mathcal U\) is the image of \(L_U(I+Dg_U(0)):i\mathcal H\to\mathcal X\), and \(\omega_U(Z)=(L_U^{-1}Z)^\parallel:T_U\mathcal U\to i\mathcal H\) is a global \(C^1\) bundle trivialization with distortion at most \(1+C_{\rm ch}\varepsilon_r\), satisfying \(\omega_{cU}(cZ)=\omega_U(Z)\) and \(\omega_U(iU)=iJ\) for every \(U\in\mathcal U\), \(Z\in T_U\mathcal U\), and \(c\in U(1)\); \((A_4)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), the map \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to\mathcal X\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), is a \(C^1\) diffeomorphism onto the open set \(S_\delta:=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), its inverse \((u_\delta,h_\delta):S_\delta\to\mathcal U\times B^\mathcal H_\delta(J)\) satisfies \(X=u_\delta(X)\boldsymbol\cdot h_\delta(X)\), \(u_\delta(U)=U\), and \(h_\delta(U)=J\) for every \(X\in S_\delta\) and \(U\in\mathcal U\), and \(\mathcal U_{\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\subseteq S_\delta\subseteq\mathcal U_{\delta+C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\); \((A_6)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) satisfying \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\) and \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), if \((u_\delta,h_\delta)\) is the inverse of \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\) on \(S_\delta=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), then \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\) and \(\sigma(U)=u_\delta(U^\dagger)\) are \(C^1\) maps on all of \(\mathcal U\times\mathcal U\) and \(\mathcal U\), respectively, and for every \(U,V,Z\in\mathcal U\), \(\mu(J,U)=\mu(U,J)=U\), \(\sigma(J)=J\), \(\|\mu(U,V)-U\boldsymbol\cdot V\|\le C_{\rm grp}\varepsilon_r\), \(\|\sigma(U)-U^\dagger\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\mu(U,V),Z)-\mu(U,\mu(V,Z))\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\sigma(U),U)-J\|\le C_{\rm grp}\varepsilon_r\), and \(\|\mu(U,\sigma(U))-J\|\le C_{\rm grp}\varepsilon_r\); \((A_7)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), every \(U_0,U_1\in\mathcal U\), and every \(q\in[0,1]\) satisfying \(\|U_1-U_0\|\le q\), \(C_{\rm path}q\le\tfrac14\), and \(C_{\rm path}(q+\varepsilon_rq+q^2)<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), every \(L_{Z_t}\) is invertible and every \(Z_t=(1-t)U_0+tU_1\) lies in \(\overline{\mathcal U}_{C_{\rm path}(q+\varepsilon_rq+q^2)}\) for \(t\in[0,1]\), and, with \(u_\delta\) the first component of the inverse of \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), the map \(H(t,U_0,U_1)=u_\delta(Z_t)\) is jointly continuous in \((t,U_0,U_1)\), joins \(U_0\) to \(U_1\), and satisfies \(H(t,cU_0,cU_1)=cH(t,U_0,U_1)\) for every \(c\in U(1)\); \((A_8)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\), every \(s\in\{\pm1\}\), and every \(0<r\le\delta\) satisfying \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), \(C_{\rm der}(\varepsilon_r+r)\le\kappa_{\rm der}\), and \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta))r+C_{\rm grp}\varepsilon_r<2\delta\), if \(u_\delta\) is the first component of the inverse of \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), \(g_{sJ}:B_{2\delta}^{i\mathcal H}(0)\to B_{2\delta}^{\mathcal H}(0)\) is the unique graph map such that, for every \(A\in B_{2\delta}^{i\mathcal H}(0)\), \(f_{sJ}(A+g_{sJ}(A))=0\), \(f_{sJ}(B)=\tfrac12(((J+B^\dagger)\boldsymbol\cdot(sJ)^\dagger)\boldsymbol\cdot(sJ\boldsymbol\cdot(J+B))-J)\), \(sJ\boldsymbol\cdot(J+A+g_{sJ}(A))\in\mathcal U\), \(\|g_{sJ}(A)+\tfrac12((sJ)^\dagger\boldsymbol\cdot(sJ)-J)\|\le C_{\rm ch}(\varepsilon_r\delta+\delta^2)\), \(\|Dg_{sJ}(A)\|\le C_{\rm ch}(\varepsilon_r+\delta)\), and \(\|D_{A^\perp}f_{sJ}(A+g_{sJ}(A))-I_{\mathcal H}\|\le C_{\rm ch}(\varepsilon_r+\delta)<1\), and if \(\chi_s(A)=sJ\boldsymbol\cdot(J+A+g_{sJ}(A))\), then the globally defined \(\sigma(U)=u_\delta(U^\dagger)\) maps \(\chi_s(B_r^{i\mathcal H}(0))\) into the same \(sJ\)-graph chart and, with \(F_s(A)=\phi_{sJ}^{\parallel}(\sigma(\chi_s(A)))\), one has \(\|D(F_s-\mathrm{id})(A)+2I_{i\mathcal H}\|\le C_{\rm der}(\varepsilon_r+r)\) for every \(A\in B_r^{i\mathcal H}(0)\); and \((R)\) \(\delta_*=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol})\}\), \(\varepsilon_*^r=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol}),\kappa_{\rm der}/(8C_{\rm der}),1/C_{\rm grp},\delta_*/(12C_{\rm path}C_{\rm grp})\}\), \(e_{\rm S1}=\min\{e_{\rm rect},\varepsilon_*^r/C_{\rm rect}\}\), \(r_{\rm iso}=\min\{\delta_*/4,\kappa_{\rm der}/(8C_{\rm der})\}\), and for every \(0\le\varepsilon_X\le e_{\rm S1}\), on setting \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), \(q=C_{\rm grp}\varepsilon_r\), \(r_-=\delta_*-C_{\rm pol}(\varepsilon_r\delta_*+\delta_*^2)\), and \(\eta=C_{\rm path}(q+\varepsilon_rq+q^2)\), one has \(C_{\rm ch}(\varepsilon_r+\delta_*)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta_*)\le\kappa_{\rm pol}\), \(q<r_-\), \(C_{\rm path}q\le\tfrac14\), \(\eta<r_-\), \(C_{\rm der}(\varepsilon_r+r_{\rm iso})\le\kappa_{\rm der}\), \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta_*))r_{\rm iso}+q<2\delta_*\), \(r_-\ge3\delta_*/4\), \(\eta\le\delta_*/4\), and \(C_{\rm der}(r_{\rm iso}+\varepsilon_r)\le\kappa_{\rm der}/4<1\). | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-rectified-cstar-control`; `lem-stage1-unitary-graph-control`; `lem-stage1-maurer-cartan-trivialization`; `lem-stage1-polar-retraction`; `lem-stage1-approximate-group-laws`; `lem-stage1-polar-path-admissibility`; `lem-stage1-inversion-derivative-control`; `lem-stage1-polar-scalar-arithmetic` | TeX 458 plus finite maxima/minima of the seven producer witnesses; monotonicity check in this section; `AUDIT-S1-POLAR-v3.md` §§0.1, 2, 4, 7.3. | 11 / 3 |

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
| `lem-stage1-polar-constant-ledger` | **SUPPORTED-WITH-DERIVATION** | Select the seven analytic witness packages, take the displayed finite maxima of coefficients and finite minima of margins, and transport each producer conclusion by its object-level monotonicity. Assemble the seven inline analytic clauses with the universal scalar-arithmetic conclusion for the same tuple. The projected \(11/3\) tree consists of the root, tuple selection, seven transports, the arithmetic application, and final assembly. |

## 5. Corrected six downstream rows

All six rows are `stated` candidates. The contracts not named by the audit are
retained verbatim. Dependencies now use the factored smooth interfaces and
row 13's genuinely compatible tuple.

| proposed/corrected id | closed replacement contract | defs | corrected exact deps | projected af |
|---|---|---|---|---|
| `lem-stage1-uniform-inversion-isolation` | There are universal \(e_{\rm iso}^r>0,r_{\rm iso}>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_{\rm iso}^r\), \(J\) and \(-J\) are the only fixed points of the smooth \(\sigma\) in their respective ambient \(r_{\rm iso}\)-balls. | `def-epsilon-cstar-algebra`; `def-approximate-unitary-space` | `lem-stage1-quantitative-inverse-function`; `lem-stage1-inversion-derivative-control`; `lem-stage1-smooth-unitary-operations`; `lem-stage1-polar-constant-ledger` | 6 / 3 |
| `lem-stage1-quotient-manifold-package` | There is a universal \(e_{\rm quot}^r>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_{\rm quot}^r\) and \(1<N=\dim_\mathbb C\mathcal X<\infty\), \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a connected compact orientable **smooth** manifold without boundary of real dimension \(N-1\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-maurer-cartan-trivialization`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-unitary-operations`; `lem-stage1-polar-constant-ledger`; `lem-topology-quotient-manifold` | 8 / 3 |
| `lem-stage1-quotient-finite-cw` | For every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, if \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a compact smooth manifold without boundary, then \(\breve{\mathcal U}\) is homeomorphic to a finite simplicial complex and hence has finite CW type. | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-quotient-manifold-package`; `lem-topology-finite-triangulation` | 3 / 2 |
| `lem-stage1-quotient-left-inversion` | There is a universal \(e_H^r>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_H^r\), the scalar-equivariant \(\mu,\sigma\) and the jointly continuous projected straight paths descend to \(\breve{\mathcal U}\); the descended multiplication makes it a connected H-space, and the descended **smooth** map \(\breve\sigma\) is a left inversion. | `def-approximate-unitary-space`; `def-h-space-left-inversion`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-coherence-naturality`; `lem-stage1-approximate-group-laws`; `lem-stage1-polar-path-admissibility`; `lem-stage1-smooth-unitary-operations`; `lem-stage1-polar-constant-ledger`; `lem-stage1-quotient-manifold-package` | 8 / 3 |
| `lem-stage1-quotient-inversion-index-data` | There is a universal \(e_{\rm idx}^r>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_{\rm idx}^r\) and \(1<N=\dim_\mathbb C\mathcal X<\infty\), the scalar class \(\breve e=[J]\) is an isolated fixed point of the smooth \(\breve\sigma\), the vertical line \(i\mathbb RJ\) is \(D\sigma_J\)-invariant, \(\|D\breve\sigma_{\breve e}+I\|<1\) in the quotient norm, and \(\det(I-D\breve\sigma_{\breve e})>0\), so its local index is \(+1\); **more precisely, there is a quotient neighborhood \(\mathcal N\) of \([J]\) such that if \([U]\in\mathcal N\) is fixed, choose a representative \(U_0\) close to \(J\) and \(c\in U(1)\) with \(\sigma(U_0)=cU_0\), choose \(a\in U(1)\) with \(a^2=c\), and use \(\sigma(aU_0)=\overline a\,\sigma(U_0)=aU_0\): the two actual fixed lifts \(\pm aU_0\) lie in the \(J\)- and \(-J\)-isolation balls, hence equal \(J\) and \(-J\), so \([U]=[J]\)**. | `def-approximate-unitary-space`; `def-lefschetz-fixed-point-data`; `def-epsilon-cstar-algebra` | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-polar-coherence-naturality`; `lem-stage1-inversion-derivative-control`; `lem-stage1-smooth-unitary-operations`; `lem-stage1-polar-constant-ledger`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-left-inversion`; `lem-topology-local-index-sign` | 9 / 3 |
| `lem-finite-polyhedron-maximal-simplex-placement` | Every point of a finite polyhedron lies in a maximal simplex of its defining finite simplicial complex; therefore every finite fixed set does. | none | none (finite-poset derivation) | 2 / 1 |

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

## 10. Disposition of every `AUDIT-S1-POLAR-v3.md` finding

Every finding of the binding audit is accepted. `CLEARED-BY` means only that
this design performs the prescribed repair; `unchanged-VALID` means that the
audit's valid finding is carried forward without mathematical change. Neither
label is a proof, a registry status, or authorization to land.

### 10.1 Final disposition, sources, witnesses, and arithmetic

| audit-v3 finding | disposition |
|---|---|
| §0 overall `REDESIGN` | **CLEARED-BY** the two and only two v4 changes in §0: the object-level row-13 root and the six downstream `defs` fields. |
| §0.1 row 13 quantifies over text and is not a registry/af proposition | **CLEARED-BY** §2 and row 13: \(W\), the seven analytic predicates, the four finite-minimum equations, and every scalar conclusion are now object-level and inline. |
| §0.1 preferred repair option 1 | **CLEARED-BY** row 12 is unchanged and row 13 is the prescribed \(\exists W[A_1\wedge A_2\wedge A_3\wedge A_4\wedge A_6\wedge A_7\wedge A_8\wedge R]\) architecture. |
| §0.1 old \(10/3\) projection was not attached to a well-formed root | **CLEARED-BY** the actual root is re-projected as \(11/3\): root, tuple selection, seven monotonicity transports, arithmetic application, and final assembly. The split trigger is not reached. |
| §0.2 six downstream rows omit `defs` | **CLEARED-BY** §5's explicit `defs` column, including `none` for maximal-simplex placement. |
| §1 three local hashes | **unchanged-VALID**; §1 is copied verbatim. |
| §1 Kitaev loci 407–440, 458, 554–560, 655–687, 692–807, 809–855, 845–878, 881–893, 895–912, and 943–955 | **unchanged-VALID**, including every audit correction and non-use warning. |
| §1 Lee C.34/C.36 and C.40 | **unchanged-VALID**; the direct-smoothness factoring is untouched. |
| §1 Munkres 4.9/5.11, 4.2, and 3.10 | **unchanged-VALID** as fallback/non-consumed material only. |
| §1 landed quantitative IFT, rectification, quotient, local-index, triangulation, Lefschetz, and top-cohomology interfaces | **unchanged-VALID**; no landed interface is strengthened. |
| §1.1 retained contracts and definition contents | **unchanged-VALID**; rows 1–12 and both definition-content cells are copied verbatim. |
| §2.1 monotonicity for rectification, graph, Maurer–Cartan, polar, group, path, and derivative packages | **unchanged-VALID**; the same finite max/min selection is used. |
| §2.1 coherence of the common graph and polar maps | **unchanged-VALID**; the inline predicates use the unique graph maps and the unique polar inverse. |
| §2.2 consumers lacked an object-level common tuple | **CLEARED-BY** the same row-13 id now exports the explicit common tuple, so the existing consumer edges become meaningful without rewiring to a new id. |
| §3 independent recomputation of row 12 | **unchanged-VALID**; row 12 is byte-for-byte unchanged. |

### 10.2 Analytic rows, downstream rows, and fixed-class obligations

| audit-v3 finding | disposition |
|---|---|
| §4 rows 1–12 | **unchanged-VALID** individually: rectified control; graph control; Maurer–Cartan; polar retraction; coherence/naturality; group laws; path admissibility; inversion derivative; smooth atlas; smooth polar inverse; smooth operations; scalar arithmetic. |
| §4 row 13 is meta-level | **CLEARED-BY** the fully quantified mathematical sentence-complex in row 13. |
| §4 rows 2–3 and 9–11 are genuinely factored | **unchanged-VALID**. |
| §5 uniform inversion isolation | **CLEARED-BY** the object-level common tuple and the prescribed two definition imports; its contract and deps are unchanged. |
| §5 quotient manifold package | **CLEARED-BY** the object-level common tuple and the prescribed algebra/unitary definition imports; its contract and deps are unchanged. |
| §5 quotient finite-CW | **CLEARED-BY** the prescribed algebra/unitary definition imports; its contract, deps, and honest status ceiling are unchanged. |
| §5 quotient left inversion | **CLEARED-BY** the object-level common tuple and the prescribed algebra/unitary/H-space definition imports; its contract and deps are unchanged. |
| §5 quotient inversion/index data | **CLEARED-BY** the object-level common tuple and the prescribed algebra/unitary/fixed-index definition imports; its contract and deps are unchanged. |
| §5 maximal-simplex placement | **unchanged-VALID** mathematically; §5 now records `defs: none` exactly. |
| §5.1 square-root phase lift | **unchanged-VALID**; no phase, map, fixed point, or neighborhood argument changes. |
| §6 actual inversion isolation obligation | **CLEARED-BY** the repaired common-tuple export. |
| §6 quotient isolation obligation | **CLEARED-BY** the repaired common-tuple export upstream; the phase lift itself is **unchanged-VALID**. |
| §6 connected compact orientable smooth quotient obligation | **CLEARED-BY** the repaired common-tuple export and complete definition metadata. |
| §6 finite-polyhedron / finite-CW obligation | **CLEARED-BY** complete definition metadata; the triangulation status warning is **unchanged-VALID**. |
| §6 H-space, left inversion, and smooth \(\breve\sigma\) obligation | **CLEARED-BY** the repaired common-tuple export and complete definition metadata. |
| §6 left-inversion trace obligation | **unchanged-VALID**. |
| §6 Lefschetz-Hopf maximal-simplex obligation | **unchanged-VALID**. |
| §6 local-index \(+1\) obligation | **CLEARED-BY** the repaired common-tuple export; derivative, determinant, isolation, and phase data are unchanged. |
| §6 top cohomology and Lefschetz comparison | **unchanged-VALID**. |
| §6 ten-id extra-fixed dependency list | **unchanged-VALID**. |

### 10.3 Definitions, dimension-freeness, DAG, and serial order

| audit-v3 finding | disposition |
|---|---|
| §7.1 `def-approximate-unitary-space` | **unchanged-VALID** theorem-free content. |
| §7.1 `def-stage1-polar-witness-data` | **unchanged-VALID** datum-only content; the result-level relation is now genuinely object-level in row 13. |
| §7.2 rectification, chart, polar, group, path, derivative, smoothness, compactness, quotient, phase, amplification, block, and stage dimension-freeness | **unchanged-VALID** in every listed component. |
| §7.2 no route alarm | **unchanged-VALID**. |
| §7.3 declared dependency edges are acyclic | **unchanged-VALID**. |
| §7.3 row-13 budget was unmeasured | **CLEARED-BY** the actual \(11/3\) projection in §§0, 3, and 4. |
| §7.3 serial order is topological but stopped at item 14 | **CLEARED-BY** the same order with an executable object-level item 14; no order change is needed. |
| §7.3 triangulation status warning | **unchanged-VALID**. |

### 10.4 Exhaustive disposition of audit §8's re-audit of v3 §10

The following table covers every row of audit-v3 §8. A semicolon separates
the rows that required v4 work from the rows whose audit verdict was retained.

| audit-v3 subsection | disposition of every row in that subsection |
|---|---|
| §8.1 | **CLEARED-BY** object-level row 13: ledger incompatibility, TeX-458 object relation, TeX-943–955 common-range closure, and the landed quotient's common-range consumption. **unchanged-VALID**: compound-row factoring; phase lift; group provenance; hashes; complete axiom list; norm comparison; rectification; right-inverse/Neumann work; \(C^1\) factoring; polar losses; derivative erratum non-use; path repair; all Lee/Munkres scope checks; landed quantitative-IFT and rectification interfaces; deliverable scope. |
| §8.2 | **CLEARED-BY** object-level row 13: arithmetic-to-analytic witness connection. **unchanged-VALID**: polynomial graph and uniqueness gluing; smooth polar inverse; smooth scalar/group/inversion maps; unchanged derivatives; all eight scalar guards. |
| §8.3 | **CLEARED-BY** object-level row 13 and its \(11/3\) projection: constant ledger, executable acyclic dependency step, and cap compliance. **unchanged-VALID**: rectified control; graph/MC factoring; polar retraction; coherence; group provenance; path; derivative; smooth-package factoring. |
| §8.4 | **CLEARED-BY** row 13 and §5 metadata: isolation, quotient, left-inversion, actual-isolation, smooth-quotient, finite-CW, H-space/smooth-inversion, and local-index common-range/metadata corrections. **unchanged-VALID**: phase lift; maximal-simplex placement; quotient-isolation argument; left-inversion trace; Lefschetz placement; top-cohomology comparison; ten-id list. |
| §8.5 | **CLEARED-BY** object-level row 13: witness datum plus result-level relation. **unchanged-VALID**: approximate-unitary definition; no guessed constants; every dimension-freeness row; no route alarm. |
| §8.6 | **CLEARED-BY** object-level row 13: free witnesses/naked formulas; ledger logical closure; witness threading; TeX-943–955 common-range closure; quotient/H-space/smooth-manifold common-range corrections; bundled smoothness/witness/edge repair; complete fixed-class plan; scalar-arithmetic/witness join; exported common-witness relation; bundled final repair. **CLEARED-BY** §5 metadata: quotient regularity, left inversion, triangulation/local-index consumers, and complete fixed-class imports. **unchanged-VALID**: every remaining §8.6 row—direct smoothness; group-to-derivative edge; TeX 458/560; path inverse guard; rectification reconstruction; all source-radius, derivative-typing, polar-radius, provenance, erratum, and norm checks; coherence; derivative chart retention; explicit smooth producers; graph/MC factoring; phase lift; maximal-simplex placement; qualified \(\phi_V\); no numerical constants; qualitative smoothness; definition contents; group/rectification provenance; design-only landing gate. |

### 10.5 Audit §9 required redesign

| required redesign item | disposition |
|---|---|
| Replace row 13 by an explicit object-level conjunction | **CLEARED-BY** row 13. |
| Re-project and split if over cap | **CLEARED-BY** the \(11/3\) projection; no split is triggered. |
| Rewire the four row-13-dependent interfaces | **CLEARED-BY** without an id change: all four already depend on `lem-stage1-polar-constant-ledger`, whose replacement contract is now object-level. |
| Add all downstream `defs` metadata | **CLEARED-BY** §5. |
| Do not alter scalar arithmetic, direct smoothness, retained contracts, definition contents, group provenance, or phase lift | **unchanged-VALID**; each is copied forward verbatim. |
| No `NOT IN LOCAL REFS` escalation and no `ROUTE-ALARM` | **unchanged-VALID**. |
| Do not land or seed v3; redesign and re-audit | **CLEARED-BY** this design-only v4 deliverable; a fresh hostile audit and user ratification remain mandatory. |

## 11. Final unblocking map

| formerly blocked interface | v4 disposition |
|---|---|
| `lem-stage1-inversion-derivative-control` | Formula-level, factored-dependency-closed, and tied to the common analytic tuple; still only a `stated` candidate. |
| `lem-stage1-quotient-manifold-package` | Transcribable in the corrected smooth form from the separate atlas, action, Maurer–Cartan, quotient, and common-range producers. |
| `lem-stage1-quotient-left-inversion` | Transcribable from scalar-equivariant smooth operations and joint path admissibility on the same tuple. |
| `lem-stage1-quotient-inversion-index-data` | Transcribable only with the explicit square-root phase-lift in its contract and proof. |
| `lem-stage1-extra-fixed-class` | Dependency-complete at design level only with the quotient-index and maximal-simplex rows added and the phase-lift consumed through the quotient-index row. |

The correct next action is a **fresh hostile audit of this v4 design**. Nothing
here lands a registry row, mutates a definition, promotes a status, or proves
Route F or `op-classical`.
