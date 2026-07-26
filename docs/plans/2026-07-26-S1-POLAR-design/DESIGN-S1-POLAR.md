# DESIGN — closed contracts for GAP-S1-POLAR-CONTRACT

Date: 2026-07-26
Role: fresh hostile design mathematician
Status: **DESIGN ONLY; NON-RIGOROUS; no row below is authorized for status
promotion or seeding before a separate hostile review**

## 0. Executive verdict

**CLOSABLE, BUT NOT BY TRANSCRIBING THE CURRENT THREE prose rows.**  The local
TeX supports a formula-level polar sub-DAG after eight atomic rows are
introduced.  Every analytic coefficient remains an existentially named
universal constant: the source explicitly says that every big-\(O\) instance
is a concrete function independent of additional data
(`approximate_algebras.tex:458`), but it does not print numerical coefficients.
Consequently, a contract demanding literal numerical values for the polar
radius is **GAP / NOT IN LOCAL REFS**.  The contracts below demand only named
universal coefficients and give every resulting radius and threshold by a
closed formula.

Two omissions in the present architecture are load-bearing:

1. `lem-stage1-exact-unit-rectification` does not assert in its current
   contract that the modified product still satisfies a controlled
   \(C^*\)-inequality.  That fact is needed before the polar machinery can be
   applied.  A new atomic producer is required; silently reading the stronger
   prose into the validated contract would be contract drift.
2. The \(O(\varepsilon)\) group-law errors do not alone produce the
   homotopies at TeX 895--912.  One must prove that every straight segment has
   a right inverse and remains inside the explicit polar domain.  This is a
   separate path-admissibility row.

No dimension-dependent analytic constant was found.  Subject to the
derivations stated below, there is **NO ROUTE-LEVEL DIMENSION-FREENESS ALARM**.

## 1. Notation and closed-constant convention

After rectification, write
\[
  \varepsilon_r:=C_{\rm rect}\varepsilon_X
\]
for a declared upper envelope on the defect of the exact-unit product, whose
unit is \(J\).  For a polar scale \(\delta>0\), define
\[
  r_\pm(\varepsilon_r,\delta)
  :=\delta\pm C_{\rm pol}(\varepsilon_r\delta+\delta^2).
\tag{1.1}
\]
For two unitary endpoints at distance at most \(q\), define
\[
  \eta_{\rm path}(\varepsilon_r,q)
  :=C_{\rm path}(q+\varepsilon_r q+q^2).
\tag{1.2}
\]
These are formulas, not definitions to be sharded.  The constants
\(C_{\rm rect},C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der}\)
and margins
\(\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der}\) are witnesses produced
by the rows below.  Their proof bodies must pin each witness to a finite
maximum or minimum of the concrete source estimates; no proof may merely
repeat \(O(\cdot)\).

## 2. Formula-level proposal table

| proposed id | kind / status | one-line `contract:` value | defs | deps | provenance | projected af |
|---|---|---|---|---|---|---|
| `lem-stage1-rectified-cstar-control` | lemma / `stated` candidate | Controlled exact-unit \(C^*\)-rectification: there are universal \(C_{\rm rect}\ge1\) and \(e_{\rm rect}\in(0,1]\) such that every finite-dimensional \(\varepsilon_X\)-\(C^*\)-algebra with \(0\le\varepsilon_X\le e_{\rm rect}\) admits on the same involutive normed space a unit \(J\) and product \(\boldsymbol\cdot\) for which \((\mathcal X,J,\boldsymbol\cdot,\dagger)\) is an exact-unit \(\varepsilon_r\)-\(C^*\)-algebra with \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), \(\|J-I_X\|\le C_{\rm rect}\varepsilon_X\), and \(\|x\boldsymbol\cdot y-xy\|\le C_{\rm rect}\varepsilon_X\|x\|\|y\|\). | `def-epsilon-cstar-algebra` | `lem-stage1-quantitative-inverse-function` | TeX 663--687; `PROOF-W74F-H-STAGE1.md` 95--110; `VERDICT-W74F-H-STAGE1.md` 55--72 | 8 / 3 |
| `lem-stage1-unitary-chart-control` | lemma / `stated` candidate | Uniform unitary charts: there are universal \(C_{\rm ch}\ge1\) and \(\kappa_{\rm ch}\in(0,\tfrac12]\) such that, for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) with \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), every \(V\in\overline{\mathcal U}_\delta\) and \(A^\parallel\in B^{i\mathcal H}_{2\delta}(0)\) have a unique \(g_V(A^\parallel)\in B^{\mathcal H}_{2\delta}(0)\) for which \(V\boldsymbol\cdot(J+A^\parallel+g_V(A^\parallel))\in\mathcal U\), with \(\|g_V(A^\parallel)+\tfrac12(V^\dagger\boldsymbol\cdot V-J)\|\le C_{\rm ch}(\varepsilon_r\delta+\delta^2)\) and \(\|Dg_V(A^\parallel)\|\le C_{\rm ch}(\varepsilon_r+\delta)\); these maps are \(C^1\) charts and their Maurer--Cartan maps identify \(T_U\mathcal U\) with \(i\mathcal H\) with distortion at most \(1+C_{\rm ch}\varepsilon_r\). | P:`def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-quantitative-inverse-function` | TeX 692--807, especially 728--807; `PROOF-W74F-H-STAGE1.md` 112--133; `VERDICT-W74F-H-STAGE1.md` 74--90 | 11 / 3 |
| `lem-stage1-polar-retraction` | lemma / `stated` candidate | Closed polar retraction: there are universal \(C_{\rm pol}\ge1\) and \(\kappa_{\rm pol}\in(0,\tfrac12]\) such that, for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), the polar map \(\Pi_\delta:\mathcal U\times B^{\mathcal H}_\delta(J)\to\mathcal A\), \(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), is a \(C^1\) diffeomorphism onto an open set \(S_\delta\) satisfying \(\mathcal U_{r_-(\varepsilon_r,\delta)}\subseteq S_\delta\subseteq\mathcal U_{r_+(\varepsilon_r,\delta)}\); its inverse \((u_\delta,h_\delta)\) is \(C^1\), satisfies \(X=u_\delta(X)\boldsymbol\cdot h_\delta(X)\), and restricts to \(u_\delta(U)=U,\ h_\delta(U)=J\) on \(\mathcal U\). | P:`def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-quantitative-inverse-function`; `lem-stage1-unitary-chart-control` | TeX 809--855; `PROOF-W74F-H-STAGE1.md` 122--133; `VERDICT-W74F-H-STAGE1.md` 74--90 | 12 / 3 |
| `lem-stage1-polar-coherence-naturality` | lemma / `stated` candidate | Polar coherence and scalar naturality: if \(\delta_1,\delta_2>0\) satisfy \(C_{\rm pol}(\varepsilon_r+\delta_j)\le\kappa_{\rm pol}\) for \(j=1,2\), then the inverse pairs supplied by `lem-stage1-polar-retraction` agree on \(S_{\delta_1}\cap S_{\delta_2}\), and for every \(c\in U(1)\) and every \(X,cX\in S_{\delta_j}\) one has \(u_{\delta_j}(cX)=c\,u_{\delta_j}(X)\) and \(h_{\delta_j}(cX)=h_{\delta_j}(X)\). | P:`def-approximate-unitary-space` | `lem-stage1-polar-retraction` | TeX 809--845 and the quotient assertion at 945; `VERDICT-W74F-H-STAGE1.md` 89--103, 339--340 | 3 / 2 |
| `lem-stage1-approximate-group-laws` | lemma / `stated` candidate | Quantitative approximate group laws: there is a universal \(C_{\rm grp}\ge1\) such that, for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra and every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\) and \(C_{\rm grp}\varepsilon_r<r_-(\varepsilon_r,\delta)\), the \(C^1\) maps \(\mu(U,V)=u_\delta(U\boldsymbol\cdot V)\) and \(\sigma(U)=u_\delta(U^\dagger)\) are defined on all of \(\mathcal U\), satisfy \(\mu(J,U)=\mu(U,J)=U,\ \sigma(J)=J\), \(\|\mu(U,V)-U\boldsymbol\cdot V\|,\|\sigma(U)-U^\dagger\|\le C_{\rm grp}\varepsilon_r\), and the associativity, left-inverse and right-inverse defects in TeX 872--874 are each at most \(C_{\rm grp}\varepsilon_r\). | P:`def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality` | TeX 845--893; `PROOF-W74F-H-STAGE1.md` 122--133; `VERDICT-W74F-H-STAGE1.md` 74--114 | 10 / 3 |
| `lem-stage1-polar-path-admissibility` | lemma / `stated` candidate | Projected straight paths: there is a universal \(C_{\rm path}\ge1\) such that, for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, every \(\delta>0\) with \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), and \(U_0,U_1\in\mathcal U\), if \(0\le q\le1\), \(\|U_1-U_0\|\le q\), and \(\eta_{\rm path}(\varepsilon_r,q)<r_-(\varepsilon_r,\delta)\), then every \(Z_t=(1-t)U_0+tU_1\) has a right inverse and belongs to \(\overline{\mathcal U}_{\eta_{\rm path}(\varepsilon_r,q)}\), so \(t\mapsto u_\delta(Z_t)\) is a continuous path in \(\mathcal U\) from \(U_0\) to \(U_1\); applying a common scalar \(c\in U(1)\) multiplies the projected path by \(c\). | P:`def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality` | TeX 895--912 (asserted homotopies), with the needed estimates derived from 655--661, 699--725, 845--868; `PROOF-W74F-H-STAGE1.md` 128--160; `VERDICT-W74F-H-STAGE1.md` 74--114 | 7 / 3 |
| `lem-stage1-inversion-derivative-control` | lemma / `stated` candidate | Typed inversion derivative: there are universal \(C_{\rm der}\ge1\) and \(\kappa_{\rm der}\in(0,\tfrac12]\) such that, for every exact-unit \(\varepsilon_r\)-\(C^*\)-algebra, \(s\in\{1,-1\}\), and \(0<r\le\delta\) satisfying \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), and \(C_{\rm der}(\varepsilon_r+r)\le\kappa_{\rm der}\), the source chart \(\chi_s(A)=sJ\boldsymbol\cdot(J+A+g_{sJ}(A))\) and \(F_s(A)=\phi_{sJ}^{\parallel}(\sigma(\chi_s(A)))\) obey \(\|D(F_s-\mathrm{id})(A)+2I_{i\mathcal H}\|\le C_{\rm der}(\varepsilon_r+r)\) for every \(A\in B^{i\mathcal H}_r(0)\). | P:`def-approximate-unitary-space`; `def-epsilon-cstar-algebra` | `lem-stage1-unitary-chart-control`; `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality` | TeX 728--762, 849--892, 943; `PROOF-W74F-H-STAGE1.md` 135--155; `VERDICT-W74F-H-STAGE1.md` 74--103 | 9 / 3 |
| `lem-stage1-polar-constant-ledger` | lemma / `stated` candidate | Closed Stage-1 polar range: for witnesses produced by the seven named dependencies, set \(\delta_*:=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol})\}\), \(\varepsilon_*^r:=\min\{\tfrac14,\kappa_{\rm ch}/(4C_{\rm ch}),\kappa_{\rm pol}/(4C_{\rm pol}),\kappa_{\rm der}/(8C_{\rm der}),1/C_{\rm grp},\delta_*/(12C_{\rm path}C_{\rm grp})\}\), \(e_{\rm S1}:=\min\{e_{\rm rect},\varepsilon_*^r/C_{\rm rect}\}\), and \(r_{\rm iso}:=\min\{\delta_*/2,\kappa_{\rm der}/(8C_{\rm der})\}\); then all chart, polar, group and path guards hold at \((\varepsilon_r,\delta_*)\) for \(0\le\varepsilon_X\le e_{\rm S1}\), with \(r_-(\varepsilon_r,\delta_*)\ge3\delta_*/4\), \(\eta_{\rm path}(\varepsilon_r,C_{\rm grp}\varepsilon_r)\le\delta_*/4\), and \(C_{\rm der}(r_{\rm iso}+\varepsilon_r)\le\kappa_{\rm der}/4<1\). | — | `lem-stage1-rectified-cstar-control`; `lem-stage1-unitary-chart-control`; `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality`; `lem-stage1-approximate-group-laws`; `lem-stage1-polar-path-admissibility`; `lem-stage1-inversion-derivative-control` | `PROOF-W74F-H-STAGE1.md` 112--155, 343--379; `VERDICT-W74F-H-STAGE1.md` 74--103, 157--177; arithmetic from the displayed contracts | 5 / 2 |

Every local-domain guard is literal in the table.  No row is authorized to
replace one by a naked “sufficiently small” premise.

## 3. Per-row feasibility verdicts

| proposed id | verdict | hostile derivation obligation |
|---|---|---|
| `lem-stage1-rectified-cstar-control` | **SUPPORTED-WITH-DERIVATION** | TeX 663--687 gives the explicit \(J,\boldsymbol\cdot\) construction, product closeness and involution preservation.  The missing lower \(C^*\)-bound follows from \(\|x^\dagger\boldsymbol\cdot x\|\ge\|x^\dagger x\|-C\varepsilon_X\|x\|^2\); the Banach-product and associator bounds require the analogous fixed-term expansions.  This stronger existential statement is not present in the current validated contract and must be a new row, rather than a purported consequence of that weaker contract. |
| `lem-stage1-unitary-chart-control` | **SUPPORTED-WITH-DERIVATION** | Replace every \(O(\varepsilon_r+\delta)\) and \(O(\varepsilon_r\delta+\delta^2)\) in TeX 758--807 by one recorded maximum.  Verify the IFT image contains zero under the displayed \(\kappa_{\rm ch}\) guard.  No finite-dimensional norm comparison is permitted. |
| `lem-stage1-polar-retraction` | **SUPPORTED-WITH-DERIVATION** | TeX `prop_polar` is the intended result.  The proof must turn its two \(O\)-losses into \(r_\pm\), prove global injectivity using the common target-centered chart, and repair the notation at TeX 845: the proposition directly supplies the inverse first on \(\mathcal U_{r_-}\), not literally on the unreduced source symbol \(\mathcal U_{\delta_{\max}}\). |
| `lem-stage1-polar-coherence-naturality` | **SUPPORTED-WITH-DERIVATION** | Coherence follows by applying polar injectivity at the larger of two admissible scales.  Scalar naturality follows because \((cU)\boldsymbol\cdot H=c(U\boldsymbol\cdot H)\) and the polar decomposition is unique.  TeX 945 consumes this fact but does not prove it separately. |
| `lem-stage1-approximate-group-laws` | **SUPPORTED-WITH-DERIVATION** | First prove \(U\boldsymbol\cdot V,U^\dagger\in\overline{\mathcal U}_{C\varepsilon_r}\), including right-invertibility via a Neumann estimate for the corresponding left multipliers.  Apply the retraction bound and telescope only a fixed number of associators.  TeX 861--893 supports this, but the printed \(O\)'s are not themselves closed contracts. |
| `lem-stage1-polar-path-admissibility` | **SUPPORTED-WITH-DERIVATION** | This is the missing analytic content behind “projecting the straight path” at TeX 906.  Expand \(Z_t^\dagger\boldsymbol\cdot Z_t-J\) about \(U_0\), and prove \(L_{Z_t}\) invertible from \(L_{U_0}\) by Neumann series.  Endpoint distance alone is not enough unless this right-inverse argument is recorded. |
| `lem-stage1-inversion-derivative-control` | **SUPPORTED-WITH-DERIVATION** | TeX 889--892 gives \(-L_U R_U^{-1}+O(\varepsilon_r)\).  In the \(sJ\)-chart, \(L_U\) and \(R_U^{-1}\) are \(O(r+\varepsilon_r)\)-close to \(sI\), giving the displayed typed operator bound.  Scalar naturality transfers the calculation from \(J\) to \(-J\). |
| `lem-stage1-polar-constant-ledger` | **SUPPORTED-WITH-DERIVATION** | Pure finite-minimum arithmetic.  With \(\kappa_{\rm pol}\le1/2\), the chosen guards give \(C_{\rm pol}(\varepsilon_r+\delta_*)\le\kappa_{\rm pol}/2\), hence \(r_-\ge3\delta_*/4\).  Since \(q=C_{\rm grp}\varepsilon_r\le1\), (1.2) is at most \(3C_{\rm path}C_{\rm grp}\varepsilon_r\le\delta_*/4\). |

No proposed row receives **SUPPORTED** without derivation: the source's
big-\(O\) prose does not itself constitute a closed formula-level registry
contract.

## 4. Consumer needs and unblocking map

| consumer | actual needs | producer(s) | disposition / required correction |
|---|---|---|---|
| `lem-stage1-inversion-derivative-control` | A controlled exact-unit \(C^*\)-datum; \(C^1\) unitary charts; a \(C^1\) polar inverse; scale coherence; a typed chart formula near both \(J\) and \(-J\). | rectified-control, chart-control, polar-retraction, polar-coherence rows | **TRANSCRIBABLE as the seventh proposal row**, not with the v4.1 wording.  Replace the ill-typed \(D(\sigma-\mathrm{id})\) by \(D(F_s-\mathrm{id})\), use \(\varepsilon_r=C_{\rm rect}\varepsilon_X\), and state the literal \(r,\delta\) guards. |
| `lem-stage1-quotient-manifold-package` | \(\mathcal U\) is a \(C^1\) manifold; \(\mathcal U_e\) is bounded and closed; the \(U(1)\)-action is smooth, free and proper; the Maurer--Cartan form descends to \(i\mathcal H/i\mathbb RJ\); the quotient theorem; \(1<\dim_\mathbb C\mathcal X<\infty\). | rectified-control, chart-control, polar-retraction, polar-coherence, polar-ledger, existing `lem-topology-quotient-manifold` | **TRANSCRIBABLE WITH CORRECTION.**  Contract should read: “If \(1<N=\dim_\mathbb C\mathcal X<\infty\) and \(0\le\varepsilon_X\le e_{\rm S1}\), then \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a connected compact orientable \(C^1\) manifold without boundary of real dimension \(N-1\).”  Delete “the analytic construction is in its universal validity range.”  Its body must prove closedness despite the right-inverse clause: a limit satisfying \(U^\dagger U=J\) has invertible \(L_{U^\dagger}L_U\) by a dimension-free Neumann bound, and finite dimensionality then gives a right inverse. |
| `lem-stage1-quotient-left-inversion` | Globally defined continuous \(\mu,\sigma\); scalar descent; exact unit laws; the left-inverse endpoint error; a polar-domain proof for the entire straight homotopy; preservation of \(\mathcal U_e\); connectedness of the quotient. | approximate-group-laws, path-admissibility, polar-coherence, polar-ledger, corrected quotient-manifold-package | **TRANSCRIBABLE WITH CORRECTION.**  Contract should read: “For \(0\le\varepsilon_X\le e_{\rm S1}\), the scalar-equivariant maps \(\mu,\sigma\) and the projected straight paths descend to \(\breve{\mathcal U}\) and make it a connected H-space with left inversion.”  Add the quotient-manifold package as a dependency for “connected,” and do not infer the homotopy from the endpoint \(C_{\rm grp}\varepsilon_r\)-bound without the path row. |

One immediate downstream correction is also mandatory:

| downstream row | required closed replacement |
|---|---|
| `lem-stage1-uniform-inversion-isolation` | Use \(e_{\rm S1}\) and \(r_{\rm iso}\) from the polar ledger.  In each \(sJ\)-chart, apply `lem-stage1-quantitative-inverse-function` to \(F_s-\mathrm{id}\); the derivative error is \(<1\), so \(sJ\) is the unique fixed point in the corresponding chart ball.  The body must then use \(\phi_{sJ}(U)=s(U-sJ)\) and \(\|\phi^\parallel_{sJ}(U)\|\le\|U-sJ\|\) to pass from the chart ball to the claimed ambient-norm ball. |

Thus all three DESIGN-ONLY rows become transcribable, but only after the eight
rows above are reviewed.  The two quotient consumers should not depend on a
single compound “polar packet.”

## 5. Dimension-freeness audit

| constant / radius | why dimension-, amplification-, block-, and stage-independent |
|---|---|
| \(C_{\rm rect},e_{\rm rect}\) | The rectification uses the quantitative IFT, Neumann inversion of \(L_J,R_J\), and a fixed number of product comparisons (TeX 663--687).  All norms are Banach/operator norms; no basis or coordinate sum occurs. |
| \(C_{\rm ch},\kappa_{\rm ch}\) | TeX 758--807 uses the norm-one Hermitian/anti-Hermitian projections, left-multiplier bounds and one quantitative IFT.  The direct-sum norm is fixed between max and sum norms (TeX 560), hence differs by at most a fixed factor two, not by dimension. |
| \(C_{\rm pol},\kappa_{\rm pol}\) | TeX 809--843 inverts a \(2\times2\) block derivative with a fixed Neumann margin.  “\(2\times2\)” refers to tangent/normal splitting, not matrix amplification or \(\dim\mathcal X\). |
| \(C_{\rm grp}\) | Products, adjoints and the three group-law telescopes use a fixed number of associators and polar retractions (TeX 857--893).  There is no summation over algebra dimension or blocks. |
| \(C_{\rm path}\) | Expanding \(Z_t^\dagger Z_t-J\) has three nonzero perturbation terms, and right-invertibility uses one Neumann inverse.  The bound depends only on \(q,\varepsilon_r\). |
| \(C_{\rm der},\kappa_{\rm der}\) | The formula \(-L_U R_U^{-1}+O(\varepsilon_r)\) is in operator norm.  Near \(sJ\), multiplier differences are bounded directly by \(\|U-sJ\|\), without an equivalence to a Euclidean norm. |
| \(\delta_*,\varepsilon_*^r,e_{\rm S1},r_{\rm iso}\) | Each is the displayed finite minimum/quotient of positive universal witnesses.  None contains \(N=\dim\mathcal X\), an amplification level, a block count or dimension, or a stage index. |
| quotient/topological step | \(N<\infty\) is used only for compactness and \(N>1\) for positive quotient dimension.  Properness comes from compact \(U(1)\); orientability comes from the scalar-invariant Maurer--Cartan trivialization.  These facts introduce no analytic coefficient. |

**Amplification audit.**  The polar proof is level-free: if an amplified
algebra satisfies the same \(\varepsilon_r\)-\(C^*\) axioms, the same operator
norm estimates apply verbatim.  No entrywise estimate is allowed.  Therefore
the constants do not depend on amplification level.

**ROUTE-LEVEL ALARM TEST: PASS, conditional on the stated derivations.**  A
future proof that chooses a Euclidean norm, invokes compactness to obtain an
unquantified derivative modulus, or sums matrix entries would fail this audit
and must be challenged.

## 6. Definition provisioning

Exactly one datum/notation shard is needed.

| proposed def id | canonical term | proposed kind/status | exact datum-only content | provenance |
|---|---|---|---|---|
| `def-approximate-unitary-space` | approximate unitary space and its source charts | `consensus` / `draft` pending sign-off | For an exact-unit \(\varepsilon\)-\(C^*\)-algebra \((\mathcal A,J,\dagger)\), define \(\mathcal H=\{X:X^\dagger=X\}\), \(i\mathcal H=\{X:X^\dagger=-X\}\), \(\mathcal U\), \(\overline{\mathcal U}_\delta\), \(\mathcal U_\delta\), the identity component \(\mathcal U_e\), the source charts \(\phi_V(X)=L_V^{-1}(X-V)\) and their \(\parallel/\perp\) parts; reserve \(u,h,\mu,\sigma\) only as notation for maps on domains supplied by result rows, with \(\mu(U,V)=u(UV)\), \(\sigma(U)=u(U^\dagger)\).  The shard asserts no existence, regularity, estimate, homotopy, compactness, or isolation statement. | TeX 692--750, 845--859; v4.1 §4.1 row 397, narrowed to keep R35 theorem-free |

The v4.1 phrase “notation \(\mathcal U,\mathcal U_e,u,\sigma\) only” needs the
chart symbols because the corrected derivative contract is otherwise
ill-typed.  This is still notation only.  In particular:

- \(u,h\) are not total maps by definition;
- “polar-admissible,” \(r_\pm\), \(\delta_*\), \(e_{\rm S1}\), and
  \(r_{\rm iso}\) are theorem-produced formulas, not definitions;
- no second “polar datum” definition is permitted, because packaging
  existence or the retraction identity into it would recreate R35.

## 7. Hostile gap and erratum register

1. **CONTRACT GAP — controlled \(C^*\)-rectification.**  The current
   exact-unit contract is too weak for every polar consumer.  This is closed by
   the first proposed row, not by silently strengthening the existing
   af-validated row.
2. **PROOF GAP — straight-path domain.**  TeX 906 asserts that straight paths
   may be projected but does not display the right-inverse/domain estimate.
   The path-admissibility row is mandatory.  It is
   SUPPORTED-WITH-DERIVATION, not available for verbatim transcription.
3. **SOURCE-RADIUS MISMATCH.**  TeX 809--843 yields an inner radius
   \(\delta-O(\varepsilon_r\delta+\delta^2)\), while TeX 845 writes \(u\) on
   \(\mathcal U_{\delta_{\max}}\).  A closed contract must shrink to \(r_-\);
   treating the two symbols as literally equal would be an overclaim.
4. **TYPING GAP IN v4.1.**  \(D(\sigma-\mathrm{id})\) is not a derivative
   between fixed Banach spaces until source and target charts are specified.
   The \(F_s\) formula above is the required repair.
5. **PRINTED DERIVATIVE ERRATUM.**  TeX 883--888 prints two derivatives with
   the same denominator \(\phi_U^\parallel(X)\); the second is evidently
   intended to be the other multiplication variable, but that corrected
   formula is **NOT BYTE-PRESENT IN THE LOCAL SOURCE**.  None of the eight
   contracts uses the missing second-variable derivative.  Any future
   consumer that needs it has a genuine local-source gap and must stop rather
   than repair it from memory.
6. **NO NUMERICAL POLAR CONSTANTS IN LOCAL REFS.**  The local source supports
   data-independent named witnesses via TeX 458.  It does not support a
   contract such as “\(\delta_*=10^{-3}\).”  Such a demand is **GAP / NOT IN
   LOCAL REFS**.

## 8. Final disposition

Replace the single `gap-stage1-polar-chart-contract` reservation by the eight
rows in §2 only after a separate fresh hostile review accepts the formulas and
dependency directions.  Candidate status is `stated`; after independent
paper-proof reconstruction and review, at most `proved-mod-audit` is
available.  Nothing in this design is rigorous, and no existing status should
be promoted from it.
