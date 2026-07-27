# DESIGN — sixth repair of closed contracts for GAP-S1-POLAR-CONTRACT

Date: 2026-07-27  
Role: fresh independent repair designer  
Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND OR SEED before a fresh hostile audit and user ratification**

## 0. Verdict and exact delta from v5

**DESIGNED-CLOSABLE, as thirteen core analytic rows, seven parameterized
transport helpers, and six downstream repairs.** This is a design verdict,
not a proof or status promotion. I found no route-level mathematical gap and
no dimension-dependent coefficient, but every new row below remains subject
to a fresh hostile audit.

The binding choice is `AUDIT-S1-POLAR-v5.md` §6 option 1,
**finite-dimensional closure**. It is the smallest coherent repair because
every stated Route-F consumer is finite-dimensional and the Stage-1 quotient
rows explicitly assume finite dimension. Option 2, adding or widening
all-domain graph and polar producers, is declined: no downstream consumer
needs that stronger architecture.

Exactly three contract-domain changes and three audit-accounting updates are
made to v5; everything else is carried forward.

| v6 change | binding audit-v5 item forcing it |
|---|---|
| Restrict base producers 6 `lem-stage1-approximate-group-laws`, 7 `lem-stage1-polar-path-admissibility`, and 8 `lem-stage1-inversion-derivative-control` from every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra to every **finite-dimensional** exact-unit \(\varepsilon_r\)-\(C^*\)-algebra. No other contract text changes. | §0; §3; §6 option 1. Rows 2 and 4 now supply \(g_V\) and \((u_\delta,h_\delta)\) on exactly the consumed domain. |
| Make the identical finite-dimensional insertion in helpers 13e `lem-stage1-approximate-group-laws-transport`, 13f `lem-stage1-polar-path-transport`, and 13g `lem-stage1-inversion-derivative-transport`. Their definite descriptions are now backed by matching-domain base and graph/polar producers. | §§1, 3, 4, and §6 option 1. |
| Make the identical finite-dimensional insertion in row-13 clauses \((A_5),(A_6),(A_7)\). This restores the v4 domain text coherently because the base producers and helpers are restricted at the same time. The v4 audit refuted the insertion only while it mismatched wider-domain producers; that mismatch is eliminated here. | §§0, 2.5–2.7, and §6 option 1. |
| Retain the provenance cells of rows 6–8. TeX 857–912 presents the relevant maps in the source exact-unit discussion; restricting the contracts to finite-dimensional algebras is a weakening, so no provenance interface changes. | §3 and the sixth-repair brief item 4. |
| Re-project helpers 13e–13g as \(4/2\): after the domain insertion, each base producer and rows 2/4 introduce every map used on the helper's full domain. Retain row 13 at \(11/3\). | §§1 and 4. |
| Replace the disposition section by an exhaustive table for every v5-audit finding. Preserve every surface declared VALID: helpers 13a–13d, clauses \((A_1)\)–\((A_4)\) and \((R)\), monotonicity directions, scalar arithmetic, rows 1–5 and 9–12, all six downstream rows, the obligation ledger, definitions, dimension-freeness, sources, and serial order. | §§1–5. |

The downstream sweep is closed row by row:

| §5 downstream row | domain consumption |
|---|---|
| `lem-stage1-uniform-inversion-isolation` | Finite-dimensional exact-unit algebra. |
| `lem-stage1-quotient-manifold-package` | Finite-dimensional exact-unit algebra. |
| `lem-stage1-quotient-finite-cw` | Finite-dimensional exact-unit algebra. |
| `lem-stage1-quotient-left-inversion` | Finite-dimensional exact-unit algebra. |
| `lem-stage1-quotient-inversion-index-data` | Finite-dimensional exact-unit algebra. |
| `lem-finite-polyhedron-maximal-simplex-placement` | Algebra-independent; consumes none of rows 6–8. |

The §6 obligation-ledger lines consume only those five finite-dimensional
analytic interfaces, the algebra-independent maximal-simplex row, or their
topological consequences. No downstream contract or obligation-ledger line
consumed the wider v5 domain of rows 6–8. Consequently those protected
surfaces remain byte-stable.

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

The architecture has two endpoint rows and seven transport helpers:

1. `lem-stage1-polar-scalar-arithmetic` is universal over **every already
   selected tuple** satisfying only
   \(C_\bullet\ge1\),
   \(0<\kappa_\bullet\le\tfrac12\), and
   \(0<e_{\rm rect}\le1/C_{\rm rect}\). It proves scalar implications only and
   has no analytic dependency.
2. Seven parameterized transport helpers each obtain one producer's base
   witnesses and assert its full conclusion for every datum-only tuple \(W\)
   that moves the relevant coefficients upward and margins downward. Thus
   producer instantiation and monotonicity are discharged inside a small
   \(4/2\) row, while all seven helpers can later receive the same \(W\).
3. `lem-stage1-polar-constant-ledger` selects one tuple and states an
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

The unification proof chooses finite maxima of the helper base coefficients
and finite minima of their margins. Every affected producer is monotone in the
needed direction: a larger coefficient and smaller admissibility margin
strengthen its antecedent and weaken its norm-bound conclusion. No smooth row
has a quantitative witness, so smoothness introduces no extra radius.

The declared counting convention is: one direct dependency
instantiation/application is one atomic node; selecting finitely many scalar
witnesses and taking their fixed finite maxima/minima is one node; conjunction
assembly is one node. A producer instantiation and its monotonicity transport
are **not** fused in row 13. They are factored into the seven helper rows,
where the four nodes are root, producer-witness instantiation, parameterized
monotonicity, and assembly, at depth \(2\). Row 13 then has root, tuple
selection/range, seven helper applications, one arithmetic application, and
final conjunction assembly: \(11\) nodes at depth \(3\). Without the helpers,
the binding audit's conservative count is retained honestly as \(18/4\).

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
| 6 | `lem-stage1-approximate-group-laws` | lemma / `stated` candidate | Quantitative approximate group laws: there exist universal \(C_{\rm grp},C_{\rm pol}\ge1\), \(\kappa_{\rm pol}\in(0,\tfrac12]\) such that for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and \(\delta>0\) satisfying \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\) and \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), the inverse \(u_\delta\) of the polar map defines \(C^1\) maps \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\), \(\sigma(U)=u_\delta(U^\dagger)\) on all of \(\mathcal U\), with \(\mu(J,U)=\mu(U,J)=U\), \(\sigma(J)=J\), \(\|\mu(U,V)-U\boldsymbol\cdot V\|\le C_{\rm grp}\varepsilon_r\), \(\|\sigma(U)-U^\dagger\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\mu(U,V),W)-\mu(U,\mu(V,W))\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\sigma(U),U)-J\|\le C_{\rm grp}\varepsilon_r\), and \(\|\mu(U,\sigma(U))-J\|\le C_{\rm grp}\varepsilon_r\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality` | **Corrected:** the two closeness estimates derive from TeX 845–868 plus `lem-stage1-polar-retraction`; only the three group defects are literal at TeX 872–874; basepoint identities are at 876–878. | 10 / 3 |
| 7 | `lem-stage1-polar-path-admissibility` | lemma / `stated` candidate | Joint projected-straight-path admissibility: there exist universal \(C_{\rm path},C_{\rm pol}\ge1\), \(\kappa_{\rm pol}\in(0,\tfrac12]\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), and \(U_0,U_1\in\mathcal U\), if \(0\le q\le1\), \(\|U_1-U_0\|\le q\), \(C_{\rm path}q\le\tfrac14\), and \(C_{\rm path}(q+\varepsilon_rq+q^2)<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), then for \(Z_t=(1-t)U_0+tU_1\) every \(L_{Z_t}\) is invertible, every \(Z_t\in\overline{\mathcal U}_{C_{\rm path}(q+\varepsilon_rq+q^2)}\), and \(H(t,U_0,U_1)=u_\delta(Z_t)\) is jointly continuous in all displayed variables, joins \(U_0\) to \(U_1\), and obeys \(H(t,cU_0,cU_1)=cH(t,U_0,U_1)\) for \(c\in U(1)\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality` | TeX 895–912 plus derivation from 655–661, 699–725; exact identity \(Z_t^\dagger\boldsymbol\cdot Z_t-J=t(t-1)(U_1-U_0)^\dagger\boldsymbol\cdot(U_1-U_0)\). | 7 / 3 |
| 8 | `lem-stage1-inversion-derivative-control` | lemma / `stated` candidate | Typed inversion derivative with chart retention: there exist universal \(C_{\rm der},C_{\rm ch},C_{\rm pol},C_{\rm grp}\ge1\) and \(\kappa_{\rm der},\kappa_{\rm ch},\kappa_{\rm pol}\in(0,\tfrac12]\) such that for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, \(s\in\{\pm1\}\), and \(0<r\le\delta\) satisfying \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), \(C_{\rm der}(\varepsilon_r+r)\le\kappa_{\rm der}\), and \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta))r+C_{\rm grp}\varepsilon_r<2\delta\), the globally defined \(\sigma(U)=u_\delta(U^\dagger)\) maps \(\chi_s(B_r^{i\mathcal H}(0))\) into the same \(sJ\)-graph chart, where \(\chi_s(A)=sJ\boldsymbol\cdot(J+A+g_{sJ}(A))\), and \(F_s(A)=\phi_{sJ}^{\parallel}(\sigma(\chi_s(A)))\) satisfies \(\|D(F_s-\mathrm{id})(A)+2I_{i\mathcal H}\|\le C_{\rm der}(\varepsilon_r+r)\) for all \(A\in B_r^{i\mathcal H}(0)\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-unitary-graph-control`; `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality`; `lem-stage1-approximate-group-laws` | TeX 728–762, 857–892, 943; the group/adjoint-domain edge and chart-retention guard are explicit. | 10 / 3 |
| 9 | `lem-stage1-smooth-unitary-atlas` | lemma / `stated` candidate | Smooth graph-atlas upgrade: for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, if \(\mathcal U\) is covered by the unique \(C^1\) graph functions \(g_V\) of `lem-stage1-unitary-graph-control` and \(D_{A^\perp}f_V\) is invertible at every graph point, then those same \(g_V\) are \(C^\infty\), and the same graph charts make \(\mathcal U\) a smooth embedded manifold; no point or first derivative of a graph or chart is changed. | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-rectified-cstar-control`; `lem-stage1-unitary-graph-control` | Polynomiality from TeX 420–429, 692–793; Lee C.40 at txt:31330–31344, 31374–31385; overlap gluing is by graph uniqueness. | 3 / 2 |
| 10 | `lem-stage1-smooth-polar-inverse` | lemma / `stated` candidate | Smooth polar-inverse upgrade: for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\), if `lem-stage1-smooth-unitary-atlas` gives the smooth embedded atlas and \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to S_\delta\) is the bijective \(C^1\) local diffeomorphism of `lem-stage1-polar-retraction` onto an open set, then the same ambient-bilinear \(\Pi_\delta\) is a smooth diffeomorphism and its same set-theoretic inverse \((u_\delta,h_\delta)\) is smooth; no point or first derivative is changed. | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-smooth-unitary-atlas` | TeX 809–855; Lee C.34 at txt:31134–31137 and C.36 at txt:31286–31298, applied chartwise after the smooth-atlas row. | 4 / 3 |
| 11 | `lem-stage1-smooth-unitary-operations` | lemma / `stated` candidate | Smooth action/operations upgrade: under `lem-stage1-approximate-group-laws`, `lem-stage1-smooth-unitary-atlas`, and `lem-stage1-smooth-polar-inverse`, the scalar action \(U(1)\times\mathcal U\to\mathcal U\), \((c,U)\mapsto cU\), and the same maps \(\mu:\mathcal U\times\mathcal U\to\mathcal U\), \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\), and \(\sigma:\mathcal U\to\mathcal U\), \(\sigma(U)=u_\delta(U^\dagger)\), are smooth as maps into the embedded manifold \(\mathcal U\); they obey \(\mu(cU,dV)=cd\,\mu(U,V)\) and \(\sigma(cU)=\overline c\,\sigma(U)\), and no point or first derivative is changed. | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-coherence-naturality`; `lem-stage1-approximate-group-laws`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse` | TeX 857–868 for the domains; smoothness follows by restriction/corestriction of the ambient scalar, bilinear, and real-linear maps followed by the smooth polar inverse; scalar identities use polar coherence/naturality. | 4 / 2 |
| 12 | `lem-stage1-polar-scalar-arithmetic` | lemma / `stated` candidate | Universal Stage-1 polar arithmetic: for every \(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der}\ge1\), \(e_{\rm rect}\in(0,1/C_{\rm rect}]\), and \(\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der}\in(0,\tfrac12]\), setting \(\delta_*=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol})\}\), \(\varepsilon_*^r=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol}),\kappa_{\rm der}/(8C_{\rm der}),1/C_{\rm grp},\delta_*/(12C_{\rm path}C_{\rm grp})\}\), \(e_{\rm S1}=\min\{e_{\rm rect},\varepsilon_*^r/C_{\rm rect}\}\), \(r_{\rm iso}=\min\{\delta_*/4,\kappa_{\rm der}/(8C_{\rm der})\}\), \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), \(q=C_{\rm grp}\varepsilon_r\), \(r_-=\delta_*-C_{\rm pol}(\varepsilon_r\delta_*+\delta_*^2)\), and \(\eta=C_{\rm path}(q+\varepsilon_rq+q^2)\), every \(0\le\varepsilon_X\le e_{\rm S1}\) satisfies \(C_{\rm ch}(\varepsilon_r+\delta_*)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta_*)\le\kappa_{\rm pol}\), \(q<r_-\), \(C_{\rm path}q\le\tfrac14\), \(\eta<r_-\), \(C_{\rm der}(\varepsilon_r+r_{\rm iso})\le\kappa_{\rm der}\), and \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta_*))r_{\rm iso}+q<2\delta_*\); moreover \(r_-\ge3\delta_*/4\), \(\eta\le\delta_*/4\), and \(C_{\rm der}(r_{\rm iso}+\varepsilon_r)\le\kappa_{\rm der}/4<1\). | `def-stage1-polar-witness-data` | none | `AUDIT-S1-POLAR-v2.md` §3, which recomputes all eight guards exactly; pure scalar derivation. | 5 / 2 |
| 13a | `lem-stage1-rectified-cstar-transport` | lemma / `stated` candidate | Parameterized rectification transport: there exist \(C_{\rm rect}^0\ge1\) and \(e_{\rm rect}^0\in(0,1/C_{\rm rect}^0]\) such that, for every `def-stage1-polar-witness-data` tuple \(W\) with \(C_{\rm rect}\ge C_{\rm rect}^0\) and \(0<e_{\rm rect}\le\min\{e_{\rm rect}^0,1/C_{\rm rect}\}\), for every finite-dimensional \(\varepsilon_X\)-\(C^*\)-algebra \((\mathcal X,I_X,\cdot,\dagger)\) with \(0\le\varepsilon_X\le e_{\rm rect}\), there are on the same involutive normed space a bilinear product \(\boldsymbol\cdot\) and an element \(J=J^\dagger\) for which \((\mathcal X,J,\boldsymbol\cdot,\dagger)\) satisfies every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra axiom of `def-epsilon-cstar-algebra`, including \(\|J\|=1\), where \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), and for every \(x,y\in\mathcal X\), \(\|J-I_X\|\le C_{\rm rect}\varepsilon_X\) and \(\|x\boldsymbol\cdot y-xy\|\le C_{\rm rect}\varepsilon_X\|x\|\|y\|\). | `def-stage1-polar-witness-data`; `def-epsilon-cstar-algebra` | `lem-stage1-rectified-cstar-control` | TeX 407–440, 672–687; parameterized coefficient/radius monotonicity; `AUDIT-S1-POLAR-v4.md` §3. | 4 / 2 |
| 13b | `lem-stage1-unitary-graph-transport` | lemma / `stated` candidate | Parameterized unitary-graph transport: there exist \(C_{\rm ch}^0\ge1\) and \(\kappa_{\rm ch}^0\in(0,\tfrac12]\) such that, for every `def-stage1-polar-witness-data` tuple \(W\) with \(C_{\rm ch}\ge C_{\rm ch}^0\) and \(0<\kappa_{\rm ch}\le\kappa_{\rm ch}^0\), for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra \((\mathcal X,J,\boldsymbol\cdot,\dagger)\), every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), every \(V\in\overline{\mathcal U}_\delta\), and every \(A^\parallel\in B^{i\mathcal H}_{2\delta}(0)\), there is a unique \(g_V(A^\parallel)\in B^\mathcal H_{2\delta}(0)\) such that \(f_V(A^\parallel+g_V(A^\parallel))=0\), where \(f_V(A)=\tfrac12(((J+A^\dagger)\boldsymbol\cdot V^\dagger)\boldsymbol\cdot(V\boldsymbol\cdot(J+A))-J)\), the element \(V\boldsymbol\cdot(J+A^\parallel+g_V(A^\parallel))\) lies in \(\mathcal U\), \(\|g_V(A^\parallel)+\tfrac12(V^\dagger\boldsymbol\cdot V-J)\|\le C_{\rm ch}(\varepsilon_r\delta+\delta^2)\), \(\|Dg_V(A^\parallel)\|\le C_{\rm ch}(\varepsilon_r+\delta)\), and \(\|D_{A^\perp}f_V(A^\parallel+g_V(A^\parallel))-I_{\mathcal H}\|\le C_{\rm ch}(\varepsilon_r+\delta)<1\), and these \(C^1\) graph charts cover \(\mathcal U\). | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-unitary-graph-control` | TeX 692–793; parameterized coefficient/margin monotonicity; `AUDIT-S1-POLAR-v4.md` §3. | 4 / 2 |
| 13c | `lem-stage1-maurer-cartan-transport` | lemma / `stated` candidate | Parameterized Maurer–Cartan transport: there exist \(C_{\rm ch}^0\ge1\) and \(\kappa_{\rm ch}^0\in(0,\tfrac12]\) such that, for every `def-stage1-polar-witness-data` tuple \(W\) with \(C_{\rm ch}\ge C_{\rm ch}^0\) and \(0<\kappa_{\rm ch}\le\kappa_{\rm ch}^0\), for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), and every family \(g=(g_U)_{U\in\mathcal U}\) of \(C^1\) maps \(g_U:B^{i\mathcal H}_{2\delta}(0)\to B^\mathcal H_{2\delta}(0)\) such that, for every \(U\in\mathcal U\) and \(A^\parallel\in B^{i\mathcal H}_{2\delta}(0)\), \(g_U(A^\parallel)\) is the unique element of \(B^\mathcal H_{2\delta}(0)\) satisfying \(f_U(A^\parallel+g_U(A^\parallel))=0\), where \(f_U(A)=\tfrac12(((J+A^\dagger)\boldsymbol\cdot U^\dagger)\boldsymbol\cdot(U\boldsymbol\cdot(J+A))-J)\), every tangent space \(T_U\mathcal U\) is the image of \(L_U(I+Dg_U(0)):i\mathcal H\to\mathcal X\), and \(\omega_U(Z)=(L_U^{-1}Z)^\parallel:T_U\mathcal U\to i\mathcal H\) is a global \(C^1\) bundle trivialization with distortion at most \(1+C_{\rm ch}\varepsilon_r\), satisfying \(\omega_{cU}(cZ)=\omega_U(Z)\) and \(\omega_U(iU)=iJ\) for every \(U\in\mathcal U\), \(Z\in T_U\mathcal U\), and \(c\in U(1)\). | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-maurer-cartan-trivialization` | TeX 795–807; parameterized distortion/guard monotonicity; `AUDIT-S1-POLAR-v4.md` §§1.3, 3. | 4 / 2 |
| 13d | `lem-stage1-polar-retraction-transport` | lemma / `stated` candidate | Parameterized polar-retraction transport: there exist \(C_{\rm pol}^0\ge1\) and \(\kappa_{\rm pol}^0\in(0,\tfrac12]\) such that, for every `def-stage1-polar-witness-data` tuple \(W\) with \(C_{\rm pol}\ge C_{\rm pol}^0\) and \(0<\kappa_{\rm pol}\le\kappa_{\rm pol}^0\), for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), the map \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to\mathcal X\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), is a \(C^1\) diffeomorphism onto the open set \(S_\delta:=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), its inverse \((u_\delta,h_\delta):S_\delta\to\mathcal U\times B^\mathcal H_\delta(J)\) satisfies \(X=u_\delta(X)\boldsymbol\cdot h_\delta(X)\), \(u_\delta(U)=U\), and \(h_\delta(U)=J\) for every \(X\in S_\delta\) and \(U\in\mathcal U\), and \(\mathcal U_{\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\subseteq S_\delta\subseteq\mathcal U_{\delta+C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\). | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction` | TeX 809–855; parameterized loss/guard monotonicity; `AUDIT-S1-POLAR-v4.md` §3. | 4 / 2 |
| 13e | `lem-stage1-approximate-group-laws-transport` | lemma / `stated` candidate | Parameterized approximate-group transport: there exist \(C_{\rm grp}^0,C_{\rm pol}^0\ge1\) and \(\kappa_{\rm pol}^0\in(0,\tfrac12]\) such that, for every `def-stage1-polar-witness-data` tuple \(W\) with \(C_{\rm grp}\ge C_{\rm grp}^0\), \(C_{\rm pol}\ge C_{\rm pol}^0\), and \(0<\kappa_{\rm pol}\le\kappa_{\rm pol}^0\), for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) satisfying \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\) and \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), writing \((u_\delta,h_\delta)\) for the unique inverse of \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to S_\delta:=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), the formulas \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\) and \(\sigma(U)=u_\delta(U^\dagger)\) define \(C^1\) maps on all of \(\mathcal U\times\mathcal U\) and \(\mathcal U\), respectively, and for every \(U,V,Z\in\mathcal U\), \(\mu(J,U)=\mu(U,J)=U\), \(\sigma(J)=J\), \(\|\mu(U,V)-U\boldsymbol\cdot V\|\le C_{\rm grp}\varepsilon_r\), \(\|\sigma(U)-U^\dagger\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\mu(U,V),Z)-\mu(U,\mu(V,Z))\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\sigma(U),U)-J\|\le C_{\rm grp}\varepsilon_r\), and \(\|\mu(U,\sigma(U))-J\|\le C_{\rm grp}\varepsilon_r\). | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-approximate-group-laws` | TeX 845–878; parameterized estimate/guard monotonicity; `AUDIT-S1-POLAR-v4.md` §§1.5, 3. | 4 / 2 |
| 13f | `lem-stage1-polar-path-transport` | lemma / `stated` candidate | Parameterized polar-path transport: there exist \(C_{\rm path}^0,C_{\rm pol}^0\ge1\) and \(\kappa_{\rm pol}^0\in(0,\tfrac12]\) such that, for every `def-stage1-polar-witness-data` tuple \(W\) with \(C_{\rm path}\ge C_{\rm path}^0\), \(C_{\rm pol}\ge C_{\rm pol}^0\), and \(0<\kappa_{\rm pol}\le\kappa_{\rm pol}^0\), for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), every \(U_0,U_1\in\mathcal U\), and every \(q\in[0,1]\) satisfying \(\|U_1-U_0\|\le q\), \(C_{\rm path}q\le\tfrac14\), and \(C_{\rm path}(q+\varepsilon_rq+q^2)<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), every \(L_{Z_t}\) is invertible and every \(Z_t=(1-t)U_0+tU_1\) lies in \(\overline{\mathcal U}_{C_{\rm path}(q+\varepsilon_rq+q^2)}\) for \(t\in[0,1]\), and, writing \(u_\delta\) for the unique first component of the inverse of \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to S_\delta:=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), the map \(H(t,U_0,U_1)=u_\delta(Z_t)\) is jointly continuous in \((t,U_0,U_1)\), joins \(U_0\) to \(U_1\), and satisfies \(H(t,cU_0,cU_1)=cH(t,U_0,U_1)\) for every \(c\in U(1)\). | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-path-admissibility` | TeX 895–912; parameterized path/loss/guard monotonicity; `AUDIT-S1-POLAR-v4.md` §§1.6, 3. | 4 / 2 |
| 13g | `lem-stage1-inversion-derivative-transport` | lemma / `stated` candidate | Parameterized inversion-derivative transport: there exist \(C_{\rm der}^0,C_{\rm ch}^0,C_{\rm pol}^0,C_{\rm grp}^0\ge1\) and \(\kappa_{\rm der}^0,\kappa_{\rm ch}^0,\kappa_{\rm pol}^0\in(0,\tfrac12]\) such that, for every `def-stage1-polar-witness-data` tuple \(W\) with \(C_{\rm der}\ge C_{\rm der}^0\), \(C_{\rm ch}\ge C_{\rm ch}^0\), \(C_{\rm pol}\ge C_{\rm pol}^0\), \(C_{\rm grp}\ge C_{\rm grp}^0\), \(0<\kappa_{\rm der}\le\kappa_{\rm der}^0\), \(0<\kappa_{\rm ch}\le\kappa_{\rm ch}^0\), and \(0<\kappa_{\rm pol}\le\kappa_{\rm pol}^0\), for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\), every \(s\in\{\pm1\}\), and every \(0<r\le\delta\) satisfying \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), \(C_{\rm der}(\varepsilon_r+r)\le\kappa_{\rm der}\), and \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta))r+C_{\rm grp}\varepsilon_r<2\delta\), writing \(u_\delta\) for the unique first component of the inverse of \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to S_\delta:=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), and \(g_{sJ}:B_{2\delta}^{i\mathcal H}(0)\to B_{2\delta}^{\mathcal H}(0)\) for the unique \(C^1\) map such that, for every \(A\in B_{2\delta}^{i\mathcal H}(0)\), \(f_{sJ}(A+g_{sJ}(A))=0\), where \(f_{sJ}(B)=\tfrac12(((J+B^\dagger)\boldsymbol\cdot(sJ)^\dagger)\boldsymbol\cdot(sJ\boldsymbol\cdot(J+B))-J)\), define \(\chi_s(A)=sJ\boldsymbol\cdot(J+A+g_{sJ}(A))\) and the global \(C^1\) map \(\sigma(U)=u_\delta(U^\dagger)\); then \(\sigma\) maps \(\chi_s(B_r^{i\mathcal H}(0))\) into the same \(sJ\)-graph chart and, with \(F_s(A)=\phi_{sJ}^{\parallel}(\sigma(\chi_s(A)))\), one has \(\|D(F_s-\mathrm{id})(A)+2I_{i\mathcal H}\|\le C_{\rm der}(\varepsilon_r+r)\) for every \(A\in B_r^{i\mathcal H}(0)\). | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-inversion-derivative-control` | TeX 728–762, 857–892, 943; parameterized chart/derivative/guard monotonicity; `AUDIT-S1-POLAR-v4.md` §§1.7, 3. | 4 / 2 |
| 13 | `lem-stage1-polar-constant-ledger` | lemma / `stated` candidate | Compatible Stage-1 polar witnesses and range: there exists one universal `def-stage1-polar-witness-data` tuple \(W=(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der},e_{\rm rect},\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der},\delta_*,\varepsilon_*^r,e_{\rm S1},r_{\rm iso})\), with \(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der}\ge1\), \(0<e_{\rm rect}\le1/C_{\rm rect}\), and \(0<\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der}\le\tfrac12\), such that all of the following hold simultaneously: \((A_1)\) for every finite-dimensional \(\varepsilon_X\)-\(C^*\)-algebra \((\mathcal X,I_X,\cdot,\dagger)\) with \(0\le\varepsilon_X\le e_{\rm rect}\), there are on the same involutive normed space a bilinear product \(\boldsymbol\cdot\) and an element \(J=J^\dagger\) for which \((\mathcal X,J,\boldsymbol\cdot,\dagger)\) satisfies every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra axiom of `def-epsilon-cstar-algebra`, including \(\|J\|=1\), where \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), and for every \(x,y\in\mathcal X\), \(\|J-I_X\|\le C_{\rm rect}\varepsilon_X\) and \(\|x\boldsymbol\cdot y-xy\|\le C_{\rm rect}\varepsilon_X\|x\|\|y\|\); \((A_2)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra \((\mathcal X,J,\boldsymbol\cdot,\dagger)\), every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), every \(V\in\overline{\mathcal U}_\delta\), and every \(A^\parallel\in B^{i\mathcal H}_{2\delta}(0)\), there is a unique \(g_V(A^\parallel)\in B^\mathcal H_{2\delta}(0)\) such that \(f_V(A^\parallel+g_V(A^\parallel))=0\), where \(f_V(A)=\tfrac12(((J+A^\dagger)\boldsymbol\cdot V^\dagger)\boldsymbol\cdot(V\boldsymbol\cdot(J+A))-J)\), the element \(V\boldsymbol\cdot(J+A^\parallel+g_V(A^\parallel))\) lies in \(\mathcal U\), \(\|g_V(A^\parallel)+\tfrac12(V^\dagger\boldsymbol\cdot V-J)\|\le C_{\rm ch}(\varepsilon_r\delta+\delta^2)\), \(\|Dg_V(A^\parallel)\|\le C_{\rm ch}(\varepsilon_r+\delta)\), and \(\|D_{A^\perp}f_V(A^\parallel+g_V(A^\parallel))-I_{\mathcal H}\|\le C_{\rm ch}(\varepsilon_r+\delta)<1\), and these \(C^1\) graph charts cover \(\mathcal U\); \((A_3)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), and every family \(g=(g_U)_{U\in\mathcal U}\) of \(C^1\) maps \(g_U:B^{i\mathcal H}_{2\delta}(0)\to B^\mathcal H_{2\delta}(0)\) such that, for every \(U\in\mathcal U\) and \(A^\parallel\in B^{i\mathcal H}_{2\delta}(0)\), \(g_U(A^\parallel)\) is the unique element of \(B^\mathcal H_{2\delta}(0)\) satisfying \(f_U(A^\parallel+g_U(A^\parallel))=0\), where \(f_U(A)=\tfrac12(((J+A^\dagger)\boldsymbol\cdot U^\dagger)\boldsymbol\cdot(U\boldsymbol\cdot(J+A))-J)\), every tangent space \(T_U\mathcal U\) is the image of \(L_U(I+Dg_U(0)):i\mathcal H\to\mathcal X\), and \(\omega_U(Z)=(L_U^{-1}Z)^\parallel:T_U\mathcal U\to i\mathcal H\) is a global \(C^1\) bundle trivialization with distortion at most \(1+C_{\rm ch}\varepsilon_r\), satisfying \(\omega_{cU}(cZ)=\omega_U(Z)\) and \(\omega_U(iU)=iJ\) for every \(U\in\mathcal U\), \(Z\in T_U\mathcal U\), and \(c\in U(1)\); \((A_4)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), the map \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to\mathcal X\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), is a \(C^1\) diffeomorphism onto the open set \(S_\delta:=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), its inverse \((u_\delta,h_\delta):S_\delta\to\mathcal U\times B^\mathcal H_\delta(J)\) satisfies \(X=u_\delta(X)\boldsymbol\cdot h_\delta(X)\), \(u_\delta(U)=U\), and \(h_\delta(U)=J\) for every \(X\in S_\delta\) and \(U\in\mathcal U\), and \(\mathcal U_{\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\subseteq S_\delta\subseteq\mathcal U_{\delta+C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\); \((A_5)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) satisfying \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\) and \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), writing \((u_\delta,h_\delta)\) for the unique inverse of \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to S_\delta:=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), the formulas \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\) and \(\sigma(U)=u_\delta(U^\dagger)\) define \(C^1\) maps on all of \(\mathcal U\times\mathcal U\) and \(\mathcal U\), respectively, and for every \(U,V,Z\in\mathcal U\), \(\mu(J,U)=\mu(U,J)=U\), \(\sigma(J)=J\), \(\|\mu(U,V)-U\boldsymbol\cdot V\|\le C_{\rm grp}\varepsilon_r\), \(\|\sigma(U)-U^\dagger\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\mu(U,V),Z)-\mu(U,\mu(V,Z))\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\sigma(U),U)-J\|\le C_{\rm grp}\varepsilon_r\), and \(\|\mu(U,\sigma(U))-J\|\le C_{\rm grp}\varepsilon_r\); \((A_6)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), every \(U_0,U_1\in\mathcal U\), and every \(q\in[0,1]\) satisfying \(\|U_1-U_0\|\le q\), \(C_{\rm path}q\le\tfrac14\), and \(C_{\rm path}(q+\varepsilon_rq+q^2)<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), every \(L_{Z_t}\) is invertible and every \(Z_t=(1-t)U_0+tU_1\) lies in \(\overline{\mathcal U}_{C_{\rm path}(q+\varepsilon_rq+q^2)}\) for \(t\in[0,1]\), and, writing \(u_\delta\) for the unique first component of the inverse of \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to S_\delta:=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), the map \(H(t,U_0,U_1)=u_\delta(Z_t)\) is jointly continuous in \((t,U_0,U_1)\), joins \(U_0\) to \(U_1\), and satisfies \(H(t,cU_0,cU_1)=cH(t,U_0,U_1)\) for every \(c\in U(1)\); \((A_7)\) for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\), every \(s\in\{\pm1\}\), and every \(0<r\le\delta\) satisfying \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), \(C_{\rm der}(\varepsilon_r+r)\le\kappa_{\rm der}\), and \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta))r+C_{\rm grp}\varepsilon_r<2\delta\), writing \(u_\delta\) for the unique first component of the inverse of \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to S_\delta:=\Pi_\delta(\mathcal U\times B^\mathcal H_\delta(J))\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), and \(g_{sJ}:B_{2\delta}^{i\mathcal H}(0)\to B_{2\delta}^{\mathcal H}(0)\) for the unique \(C^1\) map such that, for every \(A\in B_{2\delta}^{i\mathcal H}(0)\), \(f_{sJ}(A+g_{sJ}(A))=0\), where \(f_{sJ}(B)=\tfrac12(((J+B^\dagger)\boldsymbol\cdot(sJ)^\dagger)\boldsymbol\cdot(sJ\boldsymbol\cdot(J+B))-J)\), define \(\chi_s(A)=sJ\boldsymbol\cdot(J+A+g_{sJ}(A))\) and the global \(C^1\) map \(\sigma(U)=u_\delta(U^\dagger)\); then \(\sigma\) maps \(\chi_s(B_r^{i\mathcal H}(0))\) into the same \(sJ\)-graph chart and, with \(F_s(A)=\phi_{sJ}^{\parallel}(\sigma(\chi_s(A)))\), one has \(\|D(F_s-\mathrm{id})(A)+2I_{i\mathcal H}\|\le C_{\rm der}(\varepsilon_r+r)\) for every \(A\in B_r^{i\mathcal H}(0)\); and \((R)\) \(\delta_*=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol})\}\), \(\varepsilon_*^r=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol}),\kappa_{\rm der}/(8C_{\rm der}),1/C_{\rm grp},\delta_*/(12C_{\rm path}C_{\rm grp})\}\), \(e_{\rm S1}=\min\{e_{\rm rect},\varepsilon_*^r/C_{\rm rect}\}\), \(r_{\rm iso}=\min\{\delta_*/4,\kappa_{\rm der}/(8C_{\rm der})\}\), and for every \(0\le\varepsilon_X\le e_{\rm S1}\), on setting \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), \(q=C_{\rm grp}\varepsilon_r\), \(r_-=\delta_*-C_{\rm pol}(\varepsilon_r\delta_*+\delta_*^2)\), and \(\eta=C_{\rm path}(q+\varepsilon_rq+q^2)\), one has \(C_{\rm ch}(\varepsilon_r+\delta_*)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta_*)\le\kappa_{\rm pol}\), \(q<r_-\), \(C_{\rm path}q\le\tfrac14\), \(\eta<r_-\), \(C_{\rm der}(\varepsilon_r+r_{\rm iso})\le\kappa_{\rm der}\), \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta_*))r_{\rm iso}+q<2\delta_*\), \(r_-\ge3\delta_*/4\), \(\eta\le\delta_*/4\), and \(C_{\rm der}(r_{\rm iso}+\varepsilon_r)\le\kappa_{\rm der}/4<1\). | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-rectified-cstar-transport`; `lem-stage1-unitary-graph-transport`; `lem-stage1-maurer-cartan-transport`; `lem-stage1-polar-retraction-transport`; `lem-stage1-approximate-group-laws-transport`; `lem-stage1-polar-path-transport`; `lem-stage1-inversion-derivative-transport`; `lem-stage1-polar-scalar-arithmetic` | TeX 458 plus finite maxima/minima of the seven helper base witnesses; object-level monotonicity is discharged in the helper rows; `AUDIT-S1-POLAR-v4.md` §§1.3, 1.5–1.7, 2.2, 3, 6. | 11 / 3 |

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
| `lem-stage1-rectified-cstar-transport` | **SUPPORTED-WITH-DERIVATION** | Instantiate the rectification producer once, retain its base witnesses, and use \(C_{\rm rect}\ge C_{\rm rect}^0\) and \(e_{\rm rect}\le e_{\rm rect}^0\) to obtain the displayed conclusion for every receiving \(W\). Count: root, producer instantiation, monotonicity, assembly \(=4/2\). |
| `lem-stage1-unitary-graph-transport` | **SUPPORTED-WITH-DERIVATION** | Instantiate the graph producer once; increasing \(C_{\rm ch}\) and decreasing \(\kappa_{\rm ch}\) strengthens its guard and weakens all three norm bounds for every receiving \(W\). Count \(4/2\). |
| `lem-stage1-maurer-cartan-transport` | **SUPPORTED-WITH-DERIVATION** | Instantiate the Maurer–Cartan producer once; increasing \(C_{\rm ch}\) and decreasing \(\kappa_{\rm ch}\) preserves the minimal graph-map dependency binder and weakens only the distortion bound. Count \(4/2\). |
| `lem-stage1-polar-retraction-transport` | **SUPPORTED-WITH-DERIVATION** | Instantiate the polar producer once; increasing \(C_{\rm pol}\) and decreasing \(\kappa_{\rm pol}\) strengthens the guard, shrinks the inner set, and enlarges the outer set for every receiving \(W\). Count \(4/2\). |
| `lem-stage1-approximate-group-laws-transport` | **SUPPORTED-WITH-DERIVATION** | Instantiate the group producer once; increasing \(C_{\rm grp},C_{\rm pol}\) and decreasing \(\kappa_{\rm pol}\) strengthens both domain guards and weakens the seven retained estimates/identities without conditionalizing the inverse or maps. Count \(4/2\). |
| `lem-stage1-polar-path-transport` | **SUPPORTED-WITH-DERIVATION** | Instantiate the path producer once; increasing \(C_{\rm path},C_{\rm pol}\) and decreasing \(\kappa_{\rm pol}\) strengthens all path/domain guards and enlarges the asserted approximate-unitary tolerance, while continuity and equivariance are unchanged. Count \(4/2\). |
| `lem-stage1-inversion-derivative-transport` | **SUPPORTED-WITH-DERIVATION** | Instantiate the derivative producer once; increasing the four coefficients and decreasing the three margins strengthens every guard and weakens the derivative bound while preserving the explicit inverse, graph, chart, and inversion binders. Count \(4/2\). |
| `lem-stage1-polar-constant-ledger` | **SUPPORTED-WITH-DERIVATION** | Obtain the seven helper base-witness packages, take finite maxima of their coefficients and finite minima of their margins, and choose the one receiving tuple \(W\). Apply each parameterized helper and the universal scalar-arithmetic result, then assemble the eight clauses. Under §2's declared convention the projected tree is root, tuple selection/range, seven helper applications, arithmetic application, and conjunction assembly: \(11/3\). The rejected unfactored projection is \(18/4\). |

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
14. Land `lem-stage1-rectified-cstar-transport`.
15. Land `lem-stage1-unitary-graph-transport`.
16. Land `lem-stage1-maurer-cartan-transport`.
17. Land `lem-stage1-polar-retraction-transport`.
18. Land `lem-stage1-approximate-group-laws-transport`.
19. Land `lem-stage1-polar-path-transport`.
20. Land `lem-stage1-inversion-derivative-transport`.
21. Land `lem-stage1-polar-constant-ledger`.
22. Land `lem-finite-polyhedron-maximal-simplex-placement` (independent).
23. Land `lem-stage1-uniform-inversion-isolation`.
24. Land `lem-stage1-quotient-manifold-package`.
25. Land `lem-stage1-quotient-finite-cw`.
26. Land `lem-stage1-quotient-left-inversion`.
27. Land `lem-stage1-quotient-inversion-index-data`, including the phase-lift.
28. Land the separately designed `lem-stage1-exterior-cohomology`,
    `lem-stage1-left-inversion-associated-graded`, and
    `lem-stage1-left-inversion-trace`, in that order, unless they are already
    present from their own audited campaign.
29. Land the corrected `lem-stage1-extra-fixed-class` with all ten
    dependencies in §6.

No row consumes a later row. The currently `stated/seeded`
`lem-topology-finite-triangulation` prevents its consumer from being promoted
beyond its honest dependency status.

## 10. Disposition of every `AUDIT-S1-POLAR-v5.md` finding

Every finding of the binding audit is accepted. `CLEARED-BY` means only that
this design performs the prescribed repair; `unchanged-VALID` means that the
audit's valid finding is carried forward without mathematical change. Neither
label is a proof, a registry status, or authorization to land.

### 10.1 Final disposition, helpers, and analytic clauses

| audit-v5 finding | disposition |
|---|---|
| §0 overall `REDESIGN`: the graph/polar inverse exists only in finite dimension while producers 6–8, helpers 13e–13g, and \((A_5)\)–\((A_7)\) used it on every exact-unit algebra | **CLEARED-BY** the finite-dimensional insertion in exactly those nine contract locations. Rows 2 and 4 now supply every definite-description map on the complete consumed domain. |
| §0 a definite description is not an existence theorem, and variables under \((A_4)\) do not scope into independent wider quantifiers | **CLEARED-BY** matching the independent quantifiers in \((A_5)\)–\((A_7)\) to \((A_2)\) and \((A_4)\); no cross-conjunct scoping is asserted. |
| §0 \(W\) is scalar/typing data and cannot supply \(u,h,\mu,\sigma\) | **unchanged-VALID**; \(W\) remains datum-only and the maps are supplied by result rows on the matched finite-dimensional domain. |
| §0 contract/domain defect, not a route-level obstruction | **unchanged-VALID**. |
| §1 helper 13a rectification transport | **unchanged-VALID**; its domain, receiving guards, axiom weakening, closeness bounds, and \(4/2\) projection are byte-stable. |
| §1 helper 13b graph transport, including the strict normal-derivative conclusion | **unchanged-VALID**; its matched finite-dimensional domain and monotonicity are byte-stable. |
| §1 helper 13c Maurer–Cartan transport and minimal unique-zero binder | **unchanged-VALID**. |
| §1 helper 13d polar transport and both sandwich monotonicity directions | **unchanged-VALID**. |
| §1 helper 13e had correct scalar monotonicity but an unsupported all-domain polar inverse | **CLEARED-BY** its finite-dimensional insertion and the identically restricted base row 6; row 4 now supplies the inverse on the helper's full domain. Its projection is \(4/2\). |
| §1 helper 13f had correct path monotonicity but used \(u_\delta\) outside the polar producer's domain | **CLEARED-BY** its finite-dimensional insertion and identically restricted base row 7; row 4 supplies \(u_\delta\). Its projection is \(4/2\). |
| §1 helper 13g had correct guard/estimate monotonicity but used both \(u_\delta\) and \(g_{sJ}\) outside their producer domains | **CLEARED-BY** its finite-dimensional insertion and identically restricted base row 8; rows 2 and 4 supply both maps. Its projection is \(4/2\). |
| §2.1 \((A_1)\) | **unchanged-VALID**; byte-stable from v5. |
| §2.2 \((A_2)\) | **unchanged-VALID**; byte-stable from v5. |
| §2.3 \((A_3)\) | **unchanged-VALID**; byte-stable from v5. |
| §2.4 \((A_4)\) | **unchanged-VALID**; byte-stable from v5. |
| §2.5 \((A_5)\) faithfully retained the seven group conclusions but referred to an unsupported all-domain inverse | **CLEARED-BY** the finite-dimensional insertion; its local definite description is now backed by \((A_4)\) and helper 13e on the same domain. |
| §2.6 \((A_6)\) retained the path guards/conclusions but referred to an unsupported all-domain inverse | **CLEARED-BY** the finite-dimensional insertion; \((A_4)\) and helper 13f now supply the inverse on the same domain. |
| §2.7 \((A_7)\) retained the corrected syntax but lacked all-domain graph and polar existence | **CLEARED-BY** the finite-dimensional insertion; \((A_2)\), \((A_4)\), and helper 13g now supply \(g_{sJ}\) and \(u_\delta\) on the same domain. |
| §2.8 \((R)\), including four finite minima and ten scalar consequences | **unchanged-VALID**; byte-stable from v5. |

### 10.2 Producer closure and budget

| audit-v5 finding | disposition |
|---|---|
| §3 row 6 consumed a wider polar domain than row 4 produced | **CLEARED-BY** restricting row 6 to finite-dimensional exact-unit algebras. |
| §3 row 7 consumed a wider polar domain than row 4 produced | **CLEARED-BY** restricting row 7 to finite-dimensional exact-unit algebras. |
| §3 row 8 consumed wider polar and graph domains than rows 4 and 2 produced | **CLEARED-BY** restricting row 8 to finite-dimensional exact-unit algebras. |
| §3 row 5 is conditional coherence/naturality, not a missing existence producer | **unchanged-VALID**; row 5 is byte-stable and is not used as an existence assertion. |
| §3 TeX 692 and 809–878 could support a future all-domain architecture but did not close v5's imports | **CLEARED-BY** choosing §6 option 1 instead. Rows 6–8 retain their provenance cells because finite-dimensional restriction is a weakening of the source discussion at TeX 857–912. |
| §4 helpers 13a–13d are \(4/2\) | **unchanged-VALID**. |
| §4 helpers 13e–13g lacked closed projections until domain repair | **CLEARED-BY** matching their finite-dimensional domains to base rows 6–8 and graph/polar rows 2/4; each is now credibly \(4/2\). |
| §4 row 13 may retain \(11/3\) after producer/domain repair | **CLEARED-BY** the repaired helper layer; row 13 remains \(11/3\), below the unchanged \(12/3\) cap. |

### 10.3 Carry-forward, downstream sweep, sources, and dimension-freeness

| audit-v5 finding | disposition |
|---|---|
| §5.1 carry-forward outside v5's declared surfaces | **unchanged-VALID**. In v6, rows 1–5 and 9–12, helpers 13a–13d, the six downstream rows, obligation ledger/ten-id list, dimension-freeness audit, definitions, local-source/hash section, and serial dependency order remain byte-stable. |
| §5.2 Kitaev SHA256 | **unchanged-VALID**: `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. |
| §5.2 Lee SHA256 | **unchanged-VALID**: `324b7d8b1f70d40eb7608919e3c9cef93628215fa9e9f0816cb4c9549f058b3c`. |
| §5.2 Munkres SHA256 | **unchanged-VALID**: `9fcbbac92a09926498c1caba8fafa61b1a3568033485b3977edc523cc0459e5d`. |
| §5.2 pinned Kitaev polar/group and Lee inverse/implicit-function loci; no **NOT IN LOCAL REFS** escalation | **unchanged-VALID**. |
| §5.2 helper maxima/minima and dimension-freeness | **unchanged-VALID**; the finite-dimensional restriction introduces no coefficient and no dimension-dependent norm conversion. |
| §5.3 serial topological order | **unchanged-VALID**; no new id or dependency is introduced. |
| Sixth-repair downstream sweep | **CLEARED-BY** the §0 row-by-row table: five analytic §5 consumers quantify over finite-dimensional exact-unit algebras, while the sixth, maximal-simplex placement, is algebra-independent and consumes none of rows 6–8. Every §6 obligation-ledger line consumes only those interfaces or their topological consequences. |

### 10.4 Exact correction choice from audit §6

| audit-v5 required correction / option | disposition |
|---|---|
| §6 option 1: restrict producers 6–8, helpers 13e–13g, and clauses \((A_5)\)–\((A_7)\) to finite-dimensional exact-unit algebras | **CLEARED-BY** the nine literal domain insertions in §3's corrected table. |
| §6 option 2: add or widen all-domain graph and polar producers | **CLEARED-BY** an explicit decline in §0: the stronger architecture is unnecessary for the entirely finite-dimensional downstream consumers. |
| Preserve valid monotonicity, scalar arithmetic, downstream material, and datum-only definitions | **unchanged-VALID**; all are byte-stable from v5. |
| Re-project changed producer/helper trees and retain the \(12/3\) cap | **CLEARED-BY** unchanged producer budgets, \(4/2\) for helpers 13e–13g after closure, and \(11/3\) for row 13. |
| Do not land or seed v5; repair then run a fresh hostile audit | **CLEARED-BY** this design-only v6 deliverable; a fresh hostile audit and user ratification remain mandatory. |

## 11. Final unblocking map

| formerly blocked interface | v6 disposition |
|---|---|
| `lem-stage1-inversion-derivative-control` | Formula-level, factored-dependency-closed, and tied to the common analytic tuple; still only a `stated` candidate. |
| `lem-stage1-quotient-manifold-package` | Transcribable in the corrected smooth form from the separate atlas, action, Maurer–Cartan, quotient, and common-range producers. |
| `lem-stage1-quotient-left-inversion` | Transcribable from scalar-equivariant smooth operations and joint path admissibility on the same tuple. |
| `lem-stage1-quotient-inversion-index-data` | Transcribable only with the explicit square-root phase-lift in its contract and proof. |
| `lem-stage1-extra-fixed-class` | Dependency-complete at design level only with the quotient-index and maximal-simplex rows added and the phase-lift consumed through the quotient-index row. |

The correct next action is a **fresh hostile audit of this v6 design**. Nothing
here lands a registry row, mutates a definition, promotes a status, or proves
Route F or `op-classical`.
