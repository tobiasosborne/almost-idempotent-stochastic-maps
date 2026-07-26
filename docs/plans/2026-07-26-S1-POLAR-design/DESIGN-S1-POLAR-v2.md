# DESIGN — repaired closed contracts for GAP-S1-POLAR-CONTRACT

Date: 2026-07-26  
Role: fresh independent repair designer  
Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND OR SEED before a fresh hostile audit**

## 0. Executive verdict

**DESIGNED-CLOSABLE, with nine analytic rows and six explicit downstream
contract repairs.** Every finding in `AUDIT-S1-POLAR.md` is accepted. None is
refuted.
The decisive smoothness repair is stronger than approximation: the same
unitary charts, polar inverse, multiplication, and inversion are smooth because
their defining maps are smooth finite-dimensional maps and the smooth
implicit/inverse function theorems apply. Thus no fixed point, derivative,
homotopy, or index datum is changed.

The local Munkres source was checked first. It contains both compatible
structure and approximation results, but the direct exact-map upgrade below
is smaller and avoids proving that a smoothed approximation preserves the
distinguished fixed point and the left-inversion data.

No numerical coefficient is invented. All analytic coefficients remain
existential universal witnesses justified by the source convention at
`approximate_algebras.tex:458`; every radius built from them is displayed as
a closed finite formula. There is **NO ROUTE-LEVEL DIMENSION-FREENESS ALARM**.

## 1. Local smoothing-source check

Payload SHA256 values checked in this design:

- Munkres txt:
  `9fcbbac92a09926498c1caba8fafa61b1a3568033485b3977edc523cc0459e5d`;
- Lee txt:
  `324b7d8b1f70d40eb7608919e3c9cef93628215fa9e9f0816cb4c9549f058b3c`;
- Hatcher txt:
  `9f69088c02fbe1354fdc342c495ac04a59c9a8d16e4517ce2d6b7d989cf1cf06`.

| local source | exact result and locus | consequence for this repair |
|---|---|---|
| Munkres | Corollary 4.9, p.46, txt:2055-2056: a \(C^1\) structure on a manifold without boundary contains a \(C^\infty\) structure. Theorem 5.11, pp.57-58, txt:2533-2551 gives the boundary case. | A compatible smooth structure is **IN LOCAL REFS**. The Stage-1 quotient is without boundary, so Cor. 4.9 is the exact case needed. |
| Munkres | Theorem 4.2, pp.41-43, txt:1833-1905: a \(C^r\) map between \(C^p\) manifolds, \(1\le r<p\le\infty\), has an arbitrarily fine strong-\(C^1\) \(C^p\) approximation and a \(C^r\) differentiable homotopy. The relative strengthening is Exercise 4.2(a), txt:1888-1896. | A \(C^1\)-to-smooth map approximation is **IN LOCAL REFS**. It is a fallback, not the selected route. |
| Munkres | Theorem 3.10, pp.33-35, txt:1509-1637 preserves immersions, embeddings, and (with the boundary condition) diffeomorphisms under sufficiently fine strong-\(C^1\) approximation; Corollaries 4.3-4.5, pp.43-44, txt:1907-1928 and Theorem 5.13, pp.59-60, txt:2622-2648 give the smoothing consequences. | These results support structural stability of smooth approximation, but do not by themselves make an arbitrary compatible smoothing \(U(1)\)-equivariant or preserve the exact fixed map. |
| Lee | Smooth inverse function theorem C.34, pp.657-660, txt:31134-31299; smooth implicit function theorem C.40, pp.661-662, txt:31330-31380. | These close the selected **exact-map** upgrade: the polynomial graph equation has the same unique smooth solution, and the bijective smooth polar local diffeomorphism has the same smooth inverse. |
| Lee | Quotient Manifold Theorem 21.10, pp.544-545, txt:25748-25754; landed verbatim as `lem-topology-quotient-manifold`. | Once the exact unitary manifold and scalar action are smooth, the landed quotient consumer applies without changing its contract. |
| Hatcher | No \(C^1\)-to-smooth compatible-structure or smooth-approximation theorem was located in `AT.txt`; its relevant local role is algebraic topology, not smoothing. | **NOT IN LOCAL HATCHER**, but no source acquisition is needed because Munkres and Lee supply the needed results. |

### Selected route and rejected fallback

For fixed \(V\), Kitaev's map
\[
 f_V(A)
 =\tfrac12\Bigl(
   \bigl((J+A^\dagger)\boldsymbol\cdot V^\dagger\bigr)
   \boldsymbol\cdot\bigl(V\boldsymbol\cdot(J+A)\bigr)-J
 \Bigr)
\]
is a polynomial map of finite-dimensional real vector spaces: the product is
bilinear and the involution is real-linear. The quantitative row supplies
invertibility of the \(A^\perp\)-derivative and uniqueness of the graph.
Lee C.40 therefore makes the **same** graph \(g_V\) smooth. The polar map is a
smooth bilinear map; its already-proved injectivity and invertible derivative,
together with Lee C.34, make its **same** inverse \((u,h)\) smooth. Hence the
same \(\mu\), \(\sigma\), and scalar action are smooth.

This exact-map route is selected. The Munkres fallback would require a
compatible smooth structure, a relative strong-\(C^1\) approximation of
\(\breve\sigma\), an equivariant-action repair, and a proof that the
approximation has exactly the required fixed-point/index data. None of that is
needed when the original maps themselves are smooth.

## 2. Witness and formula discipline

Every contract below quantifies all constants it uses. The following formulas
are repeated in the relevant `contract:` cells as `where` clauses; this section
is explanatory only and is not relied on for registry closure:
\[
\begin{aligned}
r_\pm(\varepsilon_r,\delta)
  &=\delta\pm C_{\rm pol}
       (\varepsilon_r\delta+\delta^2),\\
\eta_{\rm path}(\varepsilon_r,q)
  &=C_{\rm path}(q+\varepsilon_rq+q^2).
\end{aligned}
\]

The proposed theorem-free datum shard `def-stage1-polar-witness-data` contains
only fields for the six selected constants, four smallness margins, and four
derived scales. It asserts no existence, inequality, admissibility, map, or
topology. The final ledger row existentially selects one compatible tuple;
all post-rectification analytic rows are universal over the fixed rectified
algebra and their maps are uniquely determined on the displayed domains, so
no dependency is treated as installing a global existential witness.

## 3. Repaired formula-level proposal table

| proposed id | kind / status | one-line `contract:` value | defs | deps | provenance | projected af |
|---|---|---|---|---|---|---|
| `lem-stage1-rectified-cstar-control` | lemma / `stated` candidate | Controlled exact-unit \(C^*\)-rectification: there are universal \(C_{\rm rect}\ge1\) and \(e_{\rm rect}\in(0,1/C_{\rm rect}]\) such that every finite-dimensional \(\varepsilon_X\)-\(C^*\)-algebra with \(0\le\varepsilon_X\le e_{\rm rect}\) admits, on the same involutive normed space, a bilinear product \(\boldsymbol\cdot\) and \(J=J^\dagger\) for which \((\mathcal X,J,\boldsymbol\cdot,\dagger)\) satisfies **every** exact-unit \(\varepsilon_r\)-\(C^*\)-algebra axiom of `def-epsilon-cstar-algebra`, including \(\|J\|=1\), where \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), and \(\|J-I_X\|\le C_{\rm rect}\varepsilon_X\), \(\|x\boldsymbol\cdot y-xy\|\le C_{\rm rect}\varepsilon_X\|x\|\|y\|\). | `def-epsilon-cstar-algebra` | `lem-stage1-exact-unit-rectification`; `lem-stage1-quantitative-inverse-function` | TeX 407-440,663-687; proof repair: normalize the provisional unit \(J_0\) by \(J=J_0/\|J_0\|\) and the provisional product by \(x\boldsymbol\cdot y=\|J_0\|(x\cdot_0y)\), then expand every axiom | 10 / 3 |
| `lem-stage1-unitary-chart-control` | lemma / `stated` candidate | Uniform unitary graph and tangent control: there are universal \(C_{\rm ch}\ge1\), \(\kappa_{\rm ch}\in(0,\tfrac12]\) such that for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), every \(V\in\overline{\mathcal U}_\delta\), and every \(A^\parallel\in B^{i\mathcal H}_{2\delta}(0)\), there is a unique \(g_V(A^\parallel)\in B^{\mathcal H}_{2\delta}(0)\) with \(f_V(A^\parallel+g_V(A^\parallel))=0\), and the corresponding \(V\boldsymbol\cdot(J+A^\parallel+g_V(A^\parallel))\) lies in \(\mathcal U\), where \(f_V(A)=\tfrac12(((J+A^\dagger)\boldsymbol\cdot V^\dagger)\boldsymbol\cdot(V\boldsymbol\cdot(J+A))-J)\); moreover \(\|g_V(A^\parallel)+\tfrac12(V^\dagger\boldsymbol\cdot V-J)\|\le C_{\rm ch}(\varepsilon_r\delta+\delta^2)\), \(\|Dg_V(A^\parallel)\|\le C_{\rm ch}(\varepsilon_r+\delta)\), and \(\|D_{A^\perp}f_V(A^\parallel+g_V(A^\parallel))-I_{\mathcal H}\|\le C_{\rm ch}(\varepsilon_r+\delta)<1\); the resulting \(C^1\) graph charts cover \(\mathcal U\), and \(\omega_U(Z)=(L_U^{-1}Z)^\parallel:T_U\mathcal U\to i\mathcal H\) is an isomorphism with distortion at most \(1+C_{\rm ch}\varepsilon_r\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-quantitative-inverse-function`; `lem-stage1-rectified-cstar-control` | TeX 692-807, especially 758-807 | 10 / 3; split graph/MC before seeding if measured \(>12\) |
| `lem-stage1-polar-retraction` | lemma / `stated` candidate | Closed \(C^1\) polar retraction: there are universal \(C_{\rm pol}\ge1\), \(\kappa_{\rm pol}\in(0,\tfrac12]\) such that for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\) is a \(C^1\) diffeomorphism from \(\mathcal U\times B^\mathcal H_\delta(J)\) onto an open \(S_\delta\), its inverse \((u_\delta,h_\delta)\) obeys \(X=u_\delta(X)\boldsymbol\cdot h_\delta(X)\), \(u_\delta(U)=U\), \(h_\delta(U)=J\), and \(\mathcal U_{\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\subseteq S_\delta\subseteq\mathcal U_{\delta+C_{\rm pol}(\varepsilon_r\delta+\delta^2)}\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-unitary-chart-control` | TeX 809-855; the two radii are inlined and repair the line-845 mismatch | 12 / 3 |
| `lem-stage1-polar-coherence-naturality` | lemma / `stated` candidate | Polar coherence and scalar naturality: for every exact-unit algebra and every two polar data \((\delta_j,S_j,u_j,h_j)\), \(j=1,2\), for which \(\Pi_{\delta_j}:\mathcal U\times B^\mathcal H_{\delta_j}(J)\to S_j\), \((U,H)\mapsto U\boldsymbol\cdot H\), is bijective with inverse \((u_j,h_j)\), one has \((u_1,h_1)=(u_2,h_2)\) on \(S_1\cap S_2\); moreover, for \(c\in U(1)\) and \(X,cX\in S_j\), \(u_j(cX)=c\,u_j(X)\) and \(h_j(cX)=h_j(X)\). | `def-approximate-unitary-space` | `lem-stage1-polar-retraction` | TeX 809-845,945; uniqueness derivation | 3 / 2 |
| `lem-stage1-approximate-group-laws` | lemma / `stated` candidate | Quantitative approximate group laws: there exist universal \(C_{\rm grp},C_{\rm pol}\ge1\), \(\kappa_{\rm pol}\in(0,\tfrac12]\) such that for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and \(\delta>0\) satisfying \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\) and \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), the inverse \(u_\delta\) of the polar map defines \(C^1\) maps \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\), \(\sigma(U)=u_\delta(U^\dagger)\) on all of \(\mathcal U\), with \(\mu(J,U)=\mu(U,J)=U\), \(\sigma(J)=J\), \(\|\mu(U,V)-U\boldsymbol\cdot V\|\le C_{\rm grp}\varepsilon_r\), \(\|\sigma(U)-U^\dagger\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\mu(U,V),W)-\mu(U,\mu(V,W))\|\le C_{\rm grp}\varepsilon_r\), \(\|\mu(\sigma(U),U)-J\|\le C_{\rm grp}\varepsilon_r\), and \(\|\mu(U,\sigma(U))-J\|\le C_{\rm grp}\varepsilon_r\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality` | TeX 857-893; all three formerly free “defects in TeX” are literal | 10 / 3 |
| `lem-stage1-polar-path-admissibility` | lemma / `stated` candidate | Joint projected-straight-path admissibility: there exist universal \(C_{\rm path},C_{\rm pol}\ge1\), \(\kappa_{\rm pol}\in(0,\tfrac12]\) such that, for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), and \(U_0,U_1\in\mathcal U\), if \(0\le q\le1\), \(\|U_1-U_0\|\le q\), \(C_{\rm path}q\le\tfrac14\), and \(C_{\rm path}(q+\varepsilon_rq+q^2)<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), then for \(Z_t=(1-t)U_0+tU_1\) every \(L_{Z_t}\) is invertible, every \(Z_t\in\overline{\mathcal U}_{C_{\rm path}(q+\varepsilon_rq+q^2)}\), and \(H(t,U_0,U_1)=u_\delta(Z_t)\) is jointly continuous in all displayed variables, joins \(U_0\) to \(U_1\), and obeys \(H(t,cU_0,cU_1)=cH(t,U_0,U_1)\) for \(c\in U(1)\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality` | TeX 895-912 plus derivation from 655-661,699-725; exact identity \(Z_t^\dagger\boldsymbol\cdot Z_t-J=t(t-1)(U_1-U_0)^\dagger\boldsymbol\cdot(U_1-U_0)\) | 7 / 3 |
| `lem-stage1-inversion-derivative-control` | lemma / `stated` candidate | Typed inversion derivative with chart retention: there exist universal \(C_{\rm der},C_{\rm ch},C_{\rm pol},C_{\rm grp}\ge1\) and \(\kappa_{\rm der},\kappa_{\rm ch},\kappa_{\rm pol}\in(0,\tfrac12]\) such that for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, \(s\in\{\pm1\}\), and \(0<r\le\delta\) satisfying \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), \(C_{\rm grp}\varepsilon_r<\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), \(C_{\rm der}(\varepsilon_r+r)\le\kappa_{\rm der}\), and \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta))r+C_{\rm grp}\varepsilon_r<2\delta\), the globally defined \(\sigma(U)=u_\delta(U^\dagger)\) maps \(\chi_s(B_r^{i\mathcal H}(0))\) into the same \(sJ\)-graph chart, where \(\chi_s(A)=sJ\boldsymbol\cdot(J+A+g_{sJ}(A))\), and \(F_s(A)=\phi_{sJ}^{\parallel}(\sigma(\chi_s(A)))\) satisfies \(\|D(F_s-\mathrm{id})(A)+2I_{i\mathcal H}\|\le C_{\rm der}(\varepsilon_r+r)\) for all \(A\in B_r^{i\mathcal H}(0)\). | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-unitary-chart-control`; `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality`; **`lem-stage1-approximate-group-laws`** | TeX 728-762,857-892,943; missing group/adjoint-domain edge added | 10 / 3 |
| `lem-stage1-smooth-unitary-polar-package` | lemma / `stated` candidate | Exact-map smooth upgrade: for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\), if \(\mathcal U\) is covered by unique \(C^1\) graph functions \(g_V\) solving smooth finite-dimensional equations \(f_V(A^\parallel+g_V(A^\parallel))=0\) whose \(A^\perp\)-derivatives at those solutions are invertible, if \(\Pi_\delta:\mathcal U\times B^\mathcal H_\delta(J)\to S_\delta\) is a bijective \(C^1\) local diffeomorphism onto an open set, and if \(U\boldsymbol\cdot V,U^\dagger\in S_\delta\) for all \(U,V\in\mathcal U\), then those same \(g_V\) are \(C^\infty\), the same graph atlas makes \(\mathcal U\) a smooth embedded manifold, the same \(\Pi_\delta\) is a smooth diffeomorphism with the same smooth inverse \((u_\delta,h_\delta)\), the scalar \(U(1)\)-action is smooth, and the same globally defined \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\) and \(\sigma(U)=u_\delta(U^\dagger)\) are smooth; no point or first derivative of any map is changed. | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-unitary-chart-control`; `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality`; `lem-stage1-approximate-group-laws` | Lee C.34 txt:31134-31299 and C.40 txt:31330-31380; polynomiality from TeX 728-855; Munkres 4.9/5.11 and 4.2 are checked fallback only | 6 / 3 |
| `lem-stage1-polar-constant-ledger` | lemma / `stated` candidate | Compatible Stage-1 polar range: there is one simultaneously selectable universal tuple \(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der}\ge1\), \(e_{\rm rect}\in(0,1/C_{\rm rect}]\), \(\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der}\in(0,\tfrac12]\) for which, setting \(\delta_*=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol})\}\), \(\varepsilon_*^r=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol}),\kappa_{\rm der}/(8C_{\rm der}),1/C_{\rm grp},\delta_*/(12C_{\rm path}C_{\rm grp})\}\), \(e_{\rm S1}=\min\{e_{\rm rect},\varepsilon_*^r/C_{\rm rect}\}\), \(r_{\rm iso}=\min\{\delta_*/4,\kappa_{\rm der}/(8C_{\rm der})\}\), \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), \(q=C_{\rm grp}\varepsilon_r\), \(r_-=\delta_*-C_{\rm pol}(\varepsilon_r\delta_*+\delta_*^2)\), and \(\eta=C_{\rm path}(q+\varepsilon_rq+q^2)\), every \(0\le\varepsilon_X\le e_{\rm S1}\) satisfies \(C_{\rm ch}(\varepsilon_r+\delta_*)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta_*)\le\kappa_{\rm pol}\), \(q<r_-\), \(C_{\rm path}q\le\tfrac14\), \(\eta<r_-\), \(C_{\rm der}(\varepsilon_r+r_{\rm iso})\le\kappa_{\rm der}\), and \((1+\varepsilon_r)(1+C_{\rm ch}(\varepsilon_r+\delta_*))r_{\rm iso}+q<2\delta_*\); moreover \(r_-\ge3\delta_*/4\), \(\eta\le\delta_*/4\), and \(C_{\rm der}(r_{\rm iso}+\varepsilon_r)\le\kappa_{\rm der}/4<1\). | `def-stage1-polar-witness-data` | all preceding eight rows | Audit §2 arithmetic, with every witness quantified and both auxiliary formulas inlined | 10 / 2 |

No contract relies on the notation in §2. Rows 3, 5, 6, and 9 inline
\(r_\pm\) or \(\eta_{\rm path}\); rows 4 and 8 universally quantify their
input maps. The ledger is the only simultaneous-witness join.

## 4. Per-row feasibility verdicts

| proposed id | verdict | exact hostile derivation obligation |
|---|---|---|
| `lem-stage1-rectified-cstar-control` | **SUPPORTED-WITH-DERIVATION** | TeX 672-687 does not display all axioms. Start with its \(J_0,\cdot_0\); prove product norm, associator, involution-product compatibility, and the \(C^*\)-lower bound by fixed-term perturbation. The exact norm defect is repaired, not ignored: put \(a=\|J_0\|=1+O(\varepsilon_X)\), \(J=J_0/a\), and \(x\boldsymbol\cdot y=a(x\cdot_0y)\). Then \(J\) is a two-sided unit and \(\|J\|=1\), and the rescaling changes every defect by only a universal \(O(\varepsilon_X)\). |
| `lem-stage1-unitary-chart-control` | **SUPPORTED-WITH-DERIVATION** | Replace each \(O(\varepsilon_r+\delta)\) and \(O(\varepsilon_r\delta+\delta^2)\) in TeX 758-807 by one finite maximum. The graph and Maurer--Cartan interfaces remain one row because the projection is \(10\) nodes; split them before seeding if measurement exceeds \(12\). |
| `lem-stage1-polar-retraction` | **SUPPORTED-WITH-DERIVATION** | TeX 809-843 supplies injectivity and the two losses. The contract uses the smaller inner domain and never repeats the unsupported line-845 domain. |
| `lem-stage1-polar-coherence-naturality` | **SUPPORTED-WITH-DERIVATION** | Apply injectivity on the common decomposition; bilinearity gives \((cU)\boldsymbol\cdot H=c(U\boldsymbol\cdot H)\). The universal antecedent removes all free witnesses. |
| `lem-stage1-approximate-group-laws` | **SUPPORTED-WITH-DERIVATION** | Prove \(U\boldsymbol\cdot V,U^\dagger\) lie in the inlined polar domain, including right-invertibility, then telescope a fixed number of associators. All three norm defects are explicit. |
| `lem-stage1-polar-path-admissibility` | **SUPPORTED-WITH-DERIVATION** | Use the exact quadratic identity displayed in the provenance column and one Neumann comparison \(L_{Z_t}=L_{U_0}+tL_{U_1-U_0}\). Continuity is joint because the affine path and \(u_\delta\) are jointly continuous on one open domain. |
| `lem-stage1-inversion-derivative-control` | **SUPPORTED-WITH-DERIVATION** | The group row is now a dependency. The extra closed guard ensures that \(\sigma(\chi_s(A))\) remains in the same graph chart, so equality of parallel coordinates really implies equality of unitary points. |
| `lem-stage1-smooth-unitary-polar-package` | **SUPPORTED-WITH-DERIVATION** | The maps are unchanged. Apply Lee C.40 locally to the smooth polynomial graph equation and use graph uniqueness to glue; apply Lee C.34 to the smooth polar local diffeomorphism and use global injectivity to glue its inverse. Smoothness of the action, \(\mu\), and \(\sigma\) follows by composition. |
| `lem-stage1-polar-constant-ledger` | **SUPPORTED-WITH-DERIVATION** | Select one tuple by finite maxima/minima before defining the displayed scales. Audit §2 already verifies the three principal inequalities. The same bounds give \(C_{\rm path}C_{\rm grp}\varepsilon_r\le\delta_*/12\) and the chart-retention guard; smoothness consumes no new radius. |

## 5. Corrected downstream rows

These are not additional hidden polar facts. They are the minimal consumer
repairs required by the audit.

| proposed/corrected id | closed replacement contract | repaired deps | projected af |
|---|---|---|---|
| `lem-stage1-uniform-inversion-isolation` | There are universal \(e_{\rm iso}^r>0,r_{\rm iso}>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_{\rm iso}^r\), \(J\) and \(-J\) are the only fixed points of the smooth \(\sigma\) in their respective ambient \(r_{\rm iso}\)-balls. | `lem-stage1-quantitative-inverse-function`; `lem-stage1-inversion-derivative-control`; `lem-stage1-smooth-unitary-polar-package`; `lem-stage1-polar-constant-ledger` | 6 / 3 |
| `lem-stage1-quotient-manifold-package` | There is a universal \(e_{\rm quot}^r>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_{\rm quot}^r\) and \(1<N=\dim_\mathbb C\mathcal X<\infty\), \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a connected compact orientable **smooth** manifold without boundary of real dimension \(N-1\). | `lem-stage1-smooth-unitary-polar-package`; `lem-stage1-polar-constant-ledger`; `lem-topology-quotient-manifold` | 8 / 3 |
| `lem-stage1-quotient-finite-cw` | For every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, if \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a compact smooth manifold without boundary, then \(\breve{\mathcal U}\) is homeomorphic to a finite simplicial complex and hence has finite CW type. | `lem-stage1-quotient-manifold-package`; `lem-topology-finite-triangulation` | 3 / 2 |
| `lem-stage1-quotient-left-inversion` | There is a universal \(e_H^r>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_H^r\), the scalar-equivariant \(\mu,\sigma\) and the jointly continuous projected straight paths descend to \(\breve{\mathcal U}\); the descended multiplication makes it a connected H-space, and the descended **smooth** map \(\breve\sigma\) is a left inversion. | `lem-stage1-approximate-group-laws`; `lem-stage1-polar-path-admissibility`; `lem-stage1-polar-coherence-naturality`; `lem-stage1-smooth-unitary-polar-package`; `lem-stage1-quotient-manifold-package`; `lem-stage1-polar-constant-ledger` | 8 / 3 |
| `lem-stage1-quotient-inversion-index-data` | There is a universal \(e_{\rm idx}^r>0\) such that, for every finite-dimensional exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(0\le\varepsilon_r\le e_{\rm idx}^r\) and \(1<N=\dim_\mathbb C\mathcal X<\infty\), the scalar class \(\breve e=[J]\) is an isolated fixed point of the smooth \(\breve\sigma\), the vertical line \(i\mathbb RJ\) is \(D\sigma_J\)-invariant, \(\|D\breve\sigma_{\breve e}+I\|<1\) in the quotient norm, and \(\det(I-D\breve\sigma_{\breve e})>0\), so its local index is \(+1\). | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-inversion-derivative-control`; `lem-stage1-polar-constant-ledger`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-left-inversion`; `lem-topology-local-index-sign` | 7 / 3 |
| `lem-finite-polyhedron-maximal-simplex-placement` | Every point of a finite polyhedron lies in a maximal simplex of its defining finite simplicial complex; therefore every finite fixed set does. | — (finite-poset derivation) | 2 / 1 |

The downstream rows are universal over one **fixed** rectified algebra, so they
do not choose incompatible rectifications. At the Route-F assembly, first
choose one rectification from row 1 and then impose the single original-scale
threshold
\[
 e_F=\min\left\{e_{\rm S1},
 \frac{e_{\rm iso}^r}{C_{\rm rect}},
 \frac{e_{\rm quot}^r}{C_{\rm rect}},
 \frac{e_H^r}{C_{\rm rect}},
 \frac{e_{\rm idx}^r}{C_{\rm rect}}\right\}.
\]
Thus \(\varepsilon_r=C_{\rm rect}\varepsilon_X\) meets every downstream
threshold on the same structure; no existential dependency is treated as a
global choice.

For the quotient package, closedness must be proved as the audit prescribes:
\(L_{U^\dagger}L_U=I+O(\varepsilon_r)\) is injective by Neumann; finite
dimension makes \(L_U\) surjective and supplies the required right inverse.
Orientability must be proved from
\[
 \omega_{cU}(cZ)=\omega_U(Z),\qquad \omega_U(iU)=iJ,
\]
which trivializes the quotient tangent bundle by
\(i\mathcal H/i\mathbb RJ\).

For the index row, write \(D\breve\sigma=-I+E\), \(\|E\|<1\). Then
\(I-D\breve\sigma=2I-E\) stays invertible along \(2I-tE\),
\(0\le t\le1\), so its determinant has the positive sign of \(2I\).

## 6. Obligation ledger for `lem-stage1-extra-fixed-class`

| landed consumer obligation | exact input needed at the application site | row that discharges it |
|---|---|---|
| `lem-stage1-uniform-inversion-isolation` | Dimension-free isolation at the scalar lifts and a valid same-chart derivative argument. | corrected isolation row from derivative-control + polar-ledger. |
| `lem-stage1-quotient-manifold-package` | Connected, compact, orientable, positive-dimensional smooth manifold without boundary. | corrected smooth quotient package; exact-map smooth upgrade; Lee quotient theorem. |
| `lem-stage1-quotient-finite-cw` | Compact **smooth** manifold before invoking the landed triangulation row. | corrected quotient-finite-CW row. |
| `lem-stage1-quotient-left-inversion` | Continuous H-space multiplication, basepoint laws, left-inversion homotopy, and a smooth descended \(\breve\sigma\). | corrected quotient-left-inversion row; joint path row supplies the homotopy. |
| `lem-stage1-left-inversion-trace` | Connected finite-CW H-space with left inversion. | quotient-finite-CW + quotient-left-inversion; no new polar obligation. |
| `lem-topology-lefschetz-hopf` | Under the contradiction assumption \(\operatorname{Fix}(\breve\sigma)=\{\breve e\}\), the fixed set is finite and every fixed point lies in a maximal simplex of the selected finite triangulation. | `lem-finite-polyhedron-maximal-simplex-placement`; this is now an explicit dependency/body step. |
| `lem-topology-local-index-sign` | Smooth self-map of a compact orientable manifold and \(\det(I-D\breve\sigma_{\breve e})\ne0\). | `lem-stage1-quotient-inversion-index-data`; index \(+1\). |
| `lem-topology-orientable-top-cohomology` | Connected compact orientable positive-dimensional manifold without boundary. | corrected smooth quotient package. |
| Lefschetz-number comparison | \(\Lambda(\breve\sigma)=\sum_k\dim H^k\ge2\), while the only-fixed-point assumption would give index sum \(1\). | left-inversion-trace + top cohomology + Lefschetz-Hopf + quotient-index-data. |

Accordingly, the corrected `lem-stage1-extra-fixed-class` dependency list must
add `lem-stage1-quotient-inversion-index-data` and
`lem-finite-polyhedron-maximal-simplex-placement`; it must not claim that the
maximal-simplex or smoothness obligations are automatic from the old design.

## 7. Dimension-freeness audit

| constant / step | dimension-freeness check |
|---|---|
| \(C_{\rm rect},e_{\rm rect}\) | Fixed-term perturbations, operator-norm Neumann inversion, and one scalar normalization \(a=\|J_0\|\); no basis sum. |
| \(C_{\rm ch},\kappa_{\rm ch}\) | Quantitative IFT in Banach/operator norms. The tangent/normal split has exactly two factors. Vector max/sum norms cost at most \(2\); passing to induced operator norms can cost another fixed factor, never \(\dim\mathcal X\). |
| \(C_{\rm pol},\kappa_{\rm pol}\) | One two-block derivative and a fixed Neumann margin; the blocks are tangent/normal, not matrix-amplification blocks. |
| \(C_{\rm grp}\) | A fixed number of products, associators, and polar retractions. |
| \(C_{\rm path}\) | One exact quadratic identity and one Neumann comparison. |
| \(C_{\rm der},\kappa_{\rm der}\) | Operator-norm multiplier formula; quotienting cannot enlarge the induced error once the vertical line is invariant. |
| Smooth upgrade | Qualitative smooth IFT applied to the same finite-dimensional polynomial maps. It introduces no modulus or radius and therefore no dimension dependence. |
| Compactness/closedness | Finite dimension is used qualitatively for bounded-closed compactness and injective \(\Rightarrow\) surjective, never to select a coefficient. |
| Quotient/orientation/index | Compact \(U(1)\), a fixed one-dimensional vertical line, and a quotient norm. Determinant dimension affects only the sign of \(2I\), not an analytic constant. |
| Amplification/block/stage | No entrywise estimate, block sum, number of calls, or stage index appears. If an amplification satisfies the same exact-unit \(\varepsilon_r\)-\(C^*\) axioms, the analytic estimates are verbatim level-free. |

**ROUTE-LEVEL ALARM TEST: PASS, conditional on the listed derivations.** Any
future proof using an unquantified compactness modulus, Euclidean norm
equivalence, or entrywise sum must be challenged.

## 8. Definition provisioning

| proposed def id | kind/status | exact theorem-free content | provenance/rationale |
|---|---|---|---|
| `def-approximate-unitary-space` | `consensus` / `draft` pending sign-off | For an exact-unit \(\varepsilon\)-\(C^*\)-algebra define \(\mathcal H=\{X:X^\dagger=X\}\), \(i\mathcal H=\{X:X^\dagger=-X\}\), \(\mathcal U\), \(\overline{\mathcal U}_\delta\), \(\mathcal U_\delta\), and \(\mathcal U_e\). For a \(V\) for which \(L_V\) is invertible, reserve \(\phi_V(X)=L_V^{-1}(X-V)\) and its \(\parallel,\perp\) components as **coordinate notation only**. Reserve \(u,h,\mu,\sigma\) only as partial notation on domains supplied by result rows. Assert no chart, inverse, estimate, smoothness, compactness, orientation, or isolation theorem. | TeX 692-750,845-859; audit §6 wording adopted exactly. |
| `def-stage1-polar-witness-data` | `original` / `draft` pending sign-off | A tuple of named scalar fields \(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der},e_{\rm rect},\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der},\delta_*,\varepsilon_*^r,e_{\rm S1},r_{\rm iso}\). It is data and typing only: it contains no positivity, inequality, existence, uniqueness, estimate, map, regularity, admissibility, or topological assertion. | Required solely to pass one selected scalar witness tuple through the ledger without turning existential dependencies into global constants; R35. |

No definition contains \(r_\pm\), \(\eta_{\rm path}\), a “polar-admissible”
predicate, or any conclusion from §3. Those formulas remain in result
contracts.

## 9. Disposition of every audit finding

### 9.1 Blockers, source loci, and per-row findings

| audit finding | disposition |
|---|---|
| §0.1 / §9.1 \(C^1\)-versus-smooth blocker | **CLEARED-BY** `lem-stage1-smooth-unitary-polar-package` and the corrected smooth quotient rows. Exact maps are upgraded using Lee C.34/C.40; Munkres 4.9/5.11 and 4.2 are locally pinned fallback results. |
| §0.2 / §3.3-3.8 / §9.2 free witnesses and naked \(r_\pm,\eta_{\rm path}\) | **CLEARED-BY** quantifiers and literal `where` formulas in every affected contract, plus one explicit simultaneous-witness ledger. |
| §0.3 / §3.7 / §4.1 / §9.3 missing group \(\to\) derivative edge | **CLEARED-BY** the bold dependency on `lem-stage1-approximate-group-laws` in the derivative row. |
| §1 TeX 458, no numerical constants | **CLEARED-BY** named universal witnesses only; no decimal radius appears. |
| §1 TeX 560, two-factor norm statement too terse | **CLEARED-BY** §7: vector norms cost at most \(2\), and induced operator comparisons may cost a second fixed factor. |
| §1 TeX 655-661, no automatic straight-path inverse | **CLEARED-BY** the explicit Neumann guard \(C_{\rm path}q\le1/4\) and proof obligation. |
| §1 / §3.1 / §7 rectification lacks the full \(C^*\) package and \(\|J\|=1\) | **CLEARED-BY** the stronger rectification contract and the explicit scalar normalization \(J=J_0/\|J_0\|\), \(x\boldsymbol\cdot y=\|J_0\|(x\cdot_0y)\), followed by every-axiom expansion. |
| §1 TeX 692-725 | **CLEARED-BY** retaining the right-inverse clause and importing the multiplier/Neumann estimates into chart, group, and path rows. |
| §1 / §3.2 TeX 728-807 proves only \(C^1\) | **CLEARED-BY** Lee C.40 applied to the same polynomial graph equation; chart+MC stays one row only while projected at \(10\) nodes, with a mandatory split if measurement exceeds \(12\). |
| §1 / §3.3 TeX 809-843 requires derivation and inline radii | **CLEARED-BY** the literal inner/outer formulas in the polar contract. |
| §1 TeX 845-855 source-radius mismatch and typo | **CLEARED-BY** using only the shrunken inner set; no conclusion uses the “derivatives of \(v\)” typo. |
| §1 / §3.5 TeX 857-880 all-\(\mathcal U\) domain and literal defects | **CLEARED-BY** the group-domain guard, right-inverse derivation, and five literal norm inequalities. |
| §1 / §7 TeX 881-893 repeated second-variable denominator | **CLEARED-BY** non-use: no contract asserts the missing second-variable formula; first-variable inversion derivative is typed explicitly. |
| §1 / §3.6 / §7 TeX 895-912 straight-path omission and H-space type typo | **CLEARED-BY** the path row's exact quadratic identity, Neumann proof, joint continuity, and the already-correct locked definition \(\mu:M\times M\to M\). |
| §1 TeX 943-955 insufficient for consumer closure | **CLEARED-BY** independent smooth, quotient, orientation, index, finite-CW, and maximal-simplex producers. TeX 943-955 is not treated as sufficient provenance. |
| §3.4 coherence row captures free polar witnesses | **CLEARED-BY** universal quantification over two complete polar data in the antecedent. |
| §3.7 derivative does not ensure the target stays in the same graph chart | **CLEARED-BY** the explicit chart-retention inequality and conclusion in the derivative contract. |
| §3.8 ledger conditional arithmetic valid but logical closure false | **CLEARED-BY** one existential compatible tuple and inlined formulas; the audit's arithmetic is preserved. |

### 9.2 Dependency, consumer, definition, and dimension findings

| audit finding | disposition |
|---|---|
| §4.2 / §9.1 explicit smooth producer required | **CLEARED-BY** `lem-stage1-smooth-unitary-polar-package`. |
| §4.3 witness threading required | **CLEARED-BY** theorem-free witness data plus the simultaneous ledger; no dependency exports a global constant. |
| §4.4 chart row may exceed the cap | **CLEARED-BY** projected \(10/3\) and an explicit “split before seeding if measured \(>12\)” gate. |
| §5.1 derivative descent, same-chart use, and determinant sign | **CLEARED-BY** derivative chart retention and `lem-stage1-quotient-inversion-index-data`. |
| §5.2 quotient regularity, closedness, and orientation | **CLEARED-BY** exact smooth upgrade, the finite-dimensional closedness argument, and the two displayed Maurer--Cartan identities. |
| §5.3 left inversion needs joint paths and smooth \(\breve\sigma\) | **CLEARED-BY** joint path-admissibility and the corrected quotient-left-inversion contract. |
| §5.4 smooth manifold / finite triangulation / local index obligations | **CLEARED-BY** the itemized §6 obligation ledger. |
| §5.4 Lefschetz maximal-simplex obligation | **CLEARED-BY** `lem-finite-polyhedron-maximal-simplex-placement`, explicitly added to the fixed-class assembly. |
| §6 definition calls \(\phi_V\) an unconditional chart | **CLEARED-BY** conditioning the notation on invertibility of \(L_V\) and asserting no chart theorem. |
| §7 controlled rectification gap | **CLEARED-BY** the first row; status remains `stated` until proved and reviewed. |
| §7 straight-path gap | **CLEARED-BY** the sixth row; it remains derivational, not a source transcription. |
| §7 source-radius mismatch | **CLEARED-BY** the inlined \(r_-\) domain. |
| §7 derivative typing gap | **CLEARED-BY** \(F_s=\phi_{sJ}^{\parallel}\circ\sigma\circ\chi_s\). |
| §7 no numerical polar constants | **CLEARED-BY** named witnesses and finite formulas only. |
| §7 additional smoothness, free-witness, and missing-dep defects | **CLEARED-BY** the smooth row, quantified contracts/ledger, and added group edge respectively. |
| §8 direct-sum/operator-norm correction | **CLEARED-BY** the explicit fixed-factor accounting in §7. |
| §8 smooth upgrade must remain qualitative/operator-norm based | **CLEARED-BY** Lee's qualitative smooth IFT on the same maps; it adds no compactness modulus or norm conversion. |
| §9.4 expand every rectified axiom | **CLEARED-BY** the row contract and feasibility obligation enumerating all axioms. |
| §9.5 qualify \(\phi_V\) | **CLEARED-BY** §8 definition text. |
| §9.6 complete fixed-class consumer plan | **CLEARED-BY** §6, including smoothness, quotient derivative, determinant sign, triangulation, and maximal simplex. |
| §9.7 preserve finite-minimum arithmetic | **CLEARED-BY** the ledger's unchanged principal minima and inequalities; smoothness adds no radius. |

No audit finding is marked REFUTED. No source-acquisition escalation remains:
the required smoothing and smooth-IFT statements are present locally. The
correct next disposition is nevertheless **FRESH HOSTILE AUDIT; DO NOT LAND OR
SEED**, because every new analytic and assembly statement here is only a
design.

## 10. Final unblocking map

| formerly blocked row | v2 disposition |
|---|---|
| `lem-stage1-inversion-derivative-control` | Formula-level and dependency-closed after rows 1-7; still `stated` candidate. |
| `lem-stage1-quotient-manifold-package` | Transcribable only in the corrected **smooth** form after rows 8-9; the old \(C^1\) contract must not be used with the landed smooth quotient theorem. |
| `lem-stage1-quotient-left-inversion` | Transcribable only with joint path continuity and smooth descended inversion. |
| `lem-stage1-extra-fixed-class` | Dependency-complete only after the quotient-index and maximal-simplex rows are added exactly as in §6. |

The old claim that eight rows alone make all three consumers transcribable is
withdrawn. The repaired closure is nine analytic rows plus the six downstream
contract repairs displayed in §5 (two new ids and four corrected existing
interfaces). Nothing in this document promotes a status or proves the Route-F
theorem.
