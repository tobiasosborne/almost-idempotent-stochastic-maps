# AUDIT — hostile review of `DESIGN-S1-POLAR.md`

Date: 2026-07-26  
Role: fresh hostile auditor; not the design author  
Status: **AUDIT ONLY; NON-RIGOROUS; no status promotion**

## 0. Final disposition

**REDESIGN.**

The conditional finite-minimum arithmetic is correct, the straight-path gap
and the printed derivative erratum are real, and I found no dimension-dependent
analytic coefficient.  Nevertheless, the proposed eight-row table is **not a
closed, landable result DAG**.  There are three independent blockers.

1. **The fixed-class consumer is not supplied with smooth objects.**  The
   proposed analytic and quotient rows stop at \(C^1\)
   (`DESIGN-S1-POLAR.md:68--73,101--102`).  The landed quotient-manifold theorem
   requires a **smooth** manifold and smooth action
   (`argument/lemmas/lem-topology-quotient-manifold.md:4`); the landed
   finite-triangulation row requires a **compact smooth** manifold
   (`argument/lemmas/lem-topology-finite-triangulation.md:4,22--29`); and the
   landed local-index row requires a **smooth self-map** of a compact orientable
   manifold (`argument/lemmas/lem-topology-local-index-sign.md:4,14--22`).
   TeX itself makes the same unsupported jump: it has established only a
   \(C^1\) manifold, then invokes a “smooth free action” and the smooth quotient
   theorem (`approximate_algebras.tex:795--807,947--954`).  A smooth-upgrade
   producer, or locally sourced and validated \(C^1\) replacements for all
   three topology inputs, is mandatory.  **The latter replacements are NOT IN
   LOCAL REFS among the audited sources.**
2. **Several proposed contracts are not self-contained.**  The symbols
   \(r_\pm\) and \(\eta_{\rm path}\) are defined only in design prose
   (`DESIGN-S1-POLAR.md:36--61`) and are then used naked in proposed registry
   contracts.  More seriously, \(C_{\rm pol},\kappa_{\rm pol}\),
   \(C_{\rm ch},\kappa_{\rm ch}\), and other existential witnesses from earlier
   rows occur free in later contracts (`ibid.:69--74`).  A dependency on an
   existential theorem does not make a selected witness a global constant.
   Each root contract must quantify compatible witnesses or use its own
   existential threshold, and every auxiliary formula must be inlined with a
   `where` clause or supplied by a theorem-free notation shard.
3. **The declared dependency map is incomplete.**
   `lem-stage1-inversion-derivative-control` uses the globally defined map
   \(\sigma(U)=u(U^\dagger)\), but its deps omit
   `lem-stage1-approximate-group-laws`, the proposed row that proves
   \(U^\dagger\) lies in the polar domain and makes \(\sigma\) a map on all of
   \(\mathcal U\) (`DESIGN-S1-POLAR.md:71,73`;
   `approximate_algebras.tex:857--868`).  In addition, the unblocking map does
   not discharge the landed smoothness and maximal-simplex obligations of
   `lem-stage1-extra-fixed-class`.

These are redesign defects, not a route-level mathematical obstruction.  The
operator-norm analytic route still appears repairable, but the current table
must not be transcribed or seeded.

## 1. Source-locus audit

I checked every TeX locus demanded by the brief and every TeX range cited in
the proposal.

| locus | hostile check | verdict |
|---|---|---|
| TeX 458 | It says each big-\(O\) instance is a concrete function independent of additional data.  It does **not** print numerical coefficients or radii.  Named universal witnesses are legitimate; invented decimal constants are not. | **VALID** |
| TeX 560 | A direct sum may use any norm between max and sum.  For a two-component vector space the norms differ by at most \(2\); comparisons of induced operator norms can cost another fixed factor.  Thus the dimension-free conclusion is correct, but “differs by at most factor two” is too terse for an operator-matrix estimate. | **VALID-WITH-CORRECTION** |
| TeX 655--661 | These are the fixed operator-norm associator/commutator estimates and the characterization of invertibility of \(L_X\).  They support dimension-free Neumann arguments; they do not themselves make a straight segment right-invertible. | **VALID** |
| TeX 663--687 | `prop_unit` states an \(O(\varepsilon)\)-Banach algebra with an exact unit, close product, and preserved involution.  It does not state that the new product is an \(O(\varepsilon)\)-\(C^*\)-algebra.  Moreover, the proof at 681--686 establishes algebraic two-sided unitality but does not visibly prove the exact-unit norm condition \(\lVert J\rVert=1\) required at TeX 429--439.  The proposed first row therefore needs a genuinely expanded construction, not only the one lower \(C^*\)-bound written in its feasibility note. | **VALID-WITH-CORRECTIONS** |
| TeX 692--725 | The definitions of \(\mathcal U,\overline{\mathcal U}_\delta,\mathcal U_\delta\) include a right-inverse clause.  `lem_U_delta` obtains uniform bounds and invertibility of \(L_X\) after explicit smallness.  These facts support the chart and path arguments in operator norm. | **VALID** |
| TeX 728--807 | `lem_gV` gives a unique \(C^1\) graph, the two displayed \(O\)-bounds, and the Maurer--Cartan identification.  The text proves only \(C^1\), not smoothness.  The proposal accurately recognizes the formulae but overstates consumer closure unless a smooth upgrade is added. | **VALID-WITH-CORRECTION** |
| TeX 809--843 | `prop_polar` gives the polar diffeomorphism and the inner/outer losses \(\delta\mp O(\varepsilon\delta+\delta^2)\).  Turning these into named coefficients is a derivation, not a verbatim transcription.  Global injectivity at a common larger admissible scale does give scale coherence. | **VALID-WITH-DERIVATION** |
| TeX 845--855 | Line 845 writes \(u,h\) on \(\mathcal U_{\delta_{\max}}\), whereas `prop_polar` directly guarantees only the shrunken inner set.  The design's radius-mismatch warning is correct.  There is also a harmless source typo at line 849 (“derivatives of \(v\) and \(h\)”); the displayed formula at 852 correctly uses \(u\). | **VALID-WITH-CORRECTION** |
| TeX 857--880 | The source defines \(\mu,\sigma\), asserts \(UV,U^\dagger\in\overline{\mathcal U}_{O(\varepsilon)}\), and states the group-law defects.  The all-\(\mathcal U\) domain of \(\sigma\) is load-bearing for the derivative row. | **VALID-WITH-DERIVATION** |
| TeX 881--893 | The inversion derivative is exactly the typed local formula needed after charts are fixed.  Lines 883--888 print the same denominator twice; the second display is not a valid second-variable derivative as printed. | **VALID-WITH-CORRECTION** |
| TeX 895--912 | Line 906 asserts projection of a straight path but supplies neither a right-inverse proof nor a polar-domain estimate.  This is a genuine omitted argument.  The H-space definition also has the known type typo \(\mu:M\to M\) at line 895; the locked definition shard correctly uses \(M\times M\to M\). | **VALID-WITH-CORRECTION** |
| TeX 943--955 | The source asserts uniform isolation, scalar quotienting, compactness, orientability, finite-CW type, and left inversion.  It does not repair the \(C^1\)-versus-smooth mismatch described above, and line 950 merely asserts that Maurer--Cartan trivializes the quotient tangent bundle. | **REFUTED as sufficient provenance for the proposed consumer closure** |

## 2. Conditional arithmetic recomputation

For this section only, assume compatible positive witnesses satisfying all
seven producer contracts, with
\[
C_{\rm ch},C_{\rm pol},C_{\rm grp},C_{\rm path},C_{\rm der}\ge1,\qquad
0<\kappa_{\rm ch},\kappa_{\rm pol},\kappa_{\rm der}\le\tfrac12.
\]
Put \(d=\delta_*\), \(e=\varepsilon_r\), and
\(q=C_{\rm grp}e\).  From the displayed minima at
`DESIGN-S1-POLAR.md:74`,
\[
\begin{aligned}
C_{\rm ch}e,\ C_{\rm ch}d&\le\kappa_{\rm ch}/4,\\
C_{\rm pol}e,\ C_{\rm pol}d&\le\kappa_{\rm pol}/4,\\
C_{\rm der}e&\le\kappa_{\rm der}/8,\\
q&\le1,\\
q&\le d/(12C_{\rm path}).
\end{aligned}
\]
Consequently:

1. **Chart and polar guards.**
   \[
   C_{\rm ch}(e+d)\le\kappa_{\rm ch}/2<\kappa_{\rm ch},\qquad
   C_{\rm pol}(e+d)\le\kappa_{\rm pol}/2<\kappa_{\rm pol}.
   \]
2. **Inner radius.**
   \[
   r_-(e,d)
   =d\bigl(1-C_{\rm pol}(e+d)\bigr)
   \ge d(1-\kappa_{\rm pol}/2)
   \ge 3d/4.
   \]
3. **Group-domain guard.**  Since \(C_{\rm path}\ge1\),
   \[
   C_{\rm grp}e=q\le d/(12C_{\rm path})\le d/12<3d/4\le r_-(e,d).
   \]
   Thus the strict group guard really does hold.
4. **Path radius.**  Since \(e\le1/4\) and \(q\le1\),
   \[
   \eta_{\rm path}(e,q)
   =C_{\rm path}q(1+e+q)
   \le3C_{\rm path}q
   \le d/4<r_-(e,d).
   \]
5. **Isolation derivative.**  The definition of \(r_{\rm iso}\) gives
   \(0<r_{\rm iso}\le d/2\) and
   \[
   C_{\rm der}(r_{\rm iso}+e)
   \le\kappa_{\rm der}/8+\kappa_{\rm der}/8
   =\kappa_{\rm der}/4<1.
   \]
6. **Rectified input.**  If
   \(0\le\varepsilon_X\le e_{\rm S1}\), then
   \(\varepsilon_X\le e_{\rm rect}\) and
   \(e=C_{\rm rect}\varepsilon_X\le\varepsilon_*^r\), as required.

Thus all three advertised numerical implications are correct **conditional on
a logically valid threading of the witnesses**:
\[
r_-\ge3\delta_*/4,\qquad
\eta_{\rm path}\le\delta_*/4,\qquad
C_{\rm der}(r_{\rm iso}+\varepsilon_r)\le\kappa_{\rm der}/4.
\]
The defect in the ledger row is logical closure, not arithmetic.

## 3. Verdict per proposed row

### 3.1 `lem-stage1-rectified-cstar-control`

**VALID-WITH-CORRECTIONS.**

The contract is mathematically plausible and dimension-free, but its cited
source does not provide the complete advertised conclusion.  TeX 672--679
states only an \(O(\varepsilon)\)-Banach rectification plus involution
preservation.  The proof at TeX 681--686 is also silent about the exact norm of
the new unit, despite the exact-unit definition at TeX 429--439.  The landed
`lem-stage1-exact-unit-rectification` contract supplies only exact-unit and
closeness conclusions
(`argument/lemmas/lem-stage1-exact-unit-rectification.md:4`); it does **not**
export the product-norm, associator, involution-product, or \(C^*\)-lower
axioms for the new product.  The new proof must explicitly establish:

- the exact-unit norm and involution conditions;
- the product-norm and associator bounds;
- compatibility of the new product with the involution; and
- the lower \(C^*\)-bound.

Merely writing
\(\|x^\dagger\boldsymbol\cdot x\|\ge
\|x^\dagger x\|-C\varepsilon_X\|x\|^2\)
does not close the other axioms.  The declared dependency on the quantitative
IFT is not by itself a contract-level producer of those properties.

### 3.2 `lem-stage1-unitary-chart-control`

**VALID-WITH-CORRECTIONS.**

The graph existence and estimates match TeX 758--793, and the tangent
identification matches TeX 795--807.  The row is nevertheless compound:
graph/estimate control and global Maurer--Cartan tangent trivialization are
distinct consumer interfaces.  They should be split if the proof projection
approaches the 12-node cap.  More importantly, the regularity must be upgraded
from \(C^1\) to smooth if this row is to feed the landed quotient,
triangulation, and local-index leaves.  That upgrade is not stated in the
audited TeX or in the landed quantitative-IFT contract
(`argument/lemmas/lem-stage1-quantitative-inverse-function.md:4`).

### 3.3 `lem-stage1-polar-retraction`

**VALID-WITH-CORRECTIONS.**

The sandwich and inverse identities are supported with derivation by TeX
809--855, and the design correctly shrinks the source's line-845 domain to the
inner radius.  The contract must inline
\[
r_\pm=\delta\pm C_{\rm pol}(\varepsilon_r\delta+\delta^2)
\]
or import theorem-free notation; the current prose-only definition is not
available to a registry root.  The proof must also state whether “diffeomorphism”
means \(C^1\) or smooth.  \(C^1\) is insufficient for the landed consumers.

### 3.4 `lem-stage1-polar-coherence-naturality`

**VALID-WITH-CORRECTIONS.**

The larger-scale injectivity argument proves coherence, and bilinearity plus
uniqueness proves
\[
u(cX)=c\,u(X),\qquad h(cX)=h(X).
\]
TeX 945 consumes scalar descent but does not prove this row separately, so the
row is correctly a derivation rather than a cited transcription.  Its current
contract, however, refers to the particular \(C_{\rm pol},\kappa_{\rm pol}\)
and sets \(S_\delta\) “supplied” by an existential dependency without
quantifying the selected witness package.  That witness interface must be made
explicit.

### 3.5 `lem-stage1-approximate-group-laws`

**VALID-WITH-CORRECTIONS.**

TeX 857--893 supports the intended result after the right-inverse and polar
domain estimates are expanded.  The one-line contract is not self-contained:
“the defects in TeX 872--874” must be replaced by the three literal norm
inequalities.  It also uses free polar witnesses and the unsharded \(r_-\)
notation.  For downstream smooth topology, \(\mu\) and \(\sigma\) must be
smooth, not merely \(C^1\).

### 3.6 `lem-stage1-polar-path-admissibility`

**VALID-WITH-CORRECTIONS.**

The gap is real, and the proposed result is derivable dimension-freely.  If
\(D=U_1-U_0\), bilinearity and the two endpoint equations give the sharper
identity
\[
Z_t^\dagger\boldsymbol\cdot Z_t-J
=t(t-1)\,D^\dagger\boldsymbol\cdot D,
\qquad Z_t=U_0+tD.
\]
Thus the unitary defect is \(O(q^2)\).  TeX 699--725 gives a universal bound
for \(L_{U_0}^{-1}\); comparing
\(L_{Z_t}=L_{U_0}+tL_D\) and choosing \(C_{\rm path}\) large enough gives
invertibility by Neumann series.  None of these estimates is printed at TeX
906.  The final contract must inline \(\eta_{\rm path}\) and quantify the polar
witnesses.  The quotient consumer's proof must use the displayed formula to
obtain **joint** continuity in the endpoint and homotopy parameters, not just
continuity of each individual path.

### 3.7 `lem-stage1-inversion-derivative-control`

**REFUTED as dependency-closed.**

The typed formula is the right repair of the v4.1 expression, and TeX 889--892
supports its analytic shape.  But the proposed deps stop at chart, polar, and
coherence rows (`DESIGN-S1-POLAR.md:73`).  Those rows do not prove that
\(U^\dagger\) lies in the polar domain for every unitary \(U\).  That fact, and
hence the all-\(\mathcal U\) definition of \(\sigma\), is supplied by the
approximate-group row from TeX 861--868.  Add
`lem-stage1-approximate-group-laws` as a dependency, or add an earlier atomic
polar-domain-for-adjoint producer.  The current row also contains free chart
and polar witnesses and supplies only \(C^1\) regularity.

### 3.8 `lem-stage1-polar-constant-ledger`

**REFUTED as a closed registry contract; conditional arithmetic VALID.**

Section 2 above verifies every displayed inequality.  The row is nevertheless
not self-contained: “witnesses produced by the seven named dependencies” does
not bind particular existential witnesses, and its contract uses the
prose-only symbols \(r_-\) and \(\eta_{\rm path}\).  The redesign must quantify
one compatible witness tuple and define every finite minimum and auxiliary
formula inside the contract, or replace the cross-row constants by independent
existential validity radii.  Any smooth-upgrade radius must also be included if
the topology is to be closed.

## 4. Dependency-direction audit

Ignoring the free-witness problem, the proposed edge order is syntactically
acyclic:

\[
\text{IFT}\to\{\text{rectification},\text{charts}\}
\to\text{polar}\to\text{coherence}
\to\{\text{group},\text{path},\text{derivative}\}
\to\text{ledger}.
\]

The following corrections are mandatory.

1. Add
   `lem-stage1-approximate-group-laws -> lem-stage1-inversion-derivative-control`
   (or a smaller adjoint-domain producer), for the reason in §3.7.
2. Add an explicit smooth-chart/smooth-polar producer before the quotient
   package.  Its proof may be qualitative, but its contract must match the
   smooth hypotheses of the landed topology rows.
3. Thread selected existential witnesses formally; prose declaration in
   design §1 is not a DAG edge or a quantifier.
4. Keep chart existence/estimates separate from quotient topology if either
   proof exceeds 12 nodes or depth 3.  The projected counts in the design are
   estimates, not evidence that the compound contracts will remain under the
   cap.

With these changes the dependency directions can remain acyclic.

## 5. Consumer-sufficiency attack

### 5.1 `lem-stage1-inversion-derivative-control`

The typed chart expression \(F_s\) is an improvement over v4.1, but the
consumer is not transcribable from the declared deps because \(\sigma\)'s
all-unitary domain is missing.  Even after that edge is added, the isolation
proof must show that \(\sigma(\chi_s(A))\) remains in the same graph chart when
using equality of parallel coordinates to conclude equality of unitary
points.  This follows from the group/polar closeness estimates after a radius
shrink, but it is not exported by the current derivative contract.

### 5.2 `lem-stage1-quotient-manifold-package`

The proposed package correctly identifies the elementary obligations:
boundedness, closedness, freeness, properness, quotient dimension, and
orientation.  The suggested closedness argument is sound only with its
finite-dimensional step made explicit: from
\(L_{U^\dagger}L_U=I+O(\varepsilon_r)\) one gets injectivity of \(L_U\);
finite dimensionality then gives surjectivity and hence a right inverse.

The decisive failure is regularity.  A \(C^1\) manifold/action does not meet
the landed smooth quotient theorem's hypothesis
(`lem-topology-quotient-manifold.md:4`).  TeX 947--950 does not supply the
missing upgrade.  The corrected contract in design line 101 is therefore
**not transcribable** as claimed.

The orientability proof must also be written, not cited to TeX line 950:
\[
\omega_{cU}(cZ)=\omega_U(Z),\qquad
\omega_U(iU)=iJ,
\]
so the quotient tangent bundle is identified with the fixed real vector space
\(i\mathcal H/i\mathbb RJ\).  This is dimension-free, but it is theorem
content for the quotient-package proof.

### 5.3 `lem-stage1-quotient-left-inversion`

Once the domain, scalar naturality, and joint path continuity are genuinely
available, the quotient H-space/left-inversion construction works:
\[
\mu(cU,dV)=cd\,\mu(U,V),\qquad
\sigma(cU)=\overline c\,\sigma(U),
\]
and the scalar factors cancel in
\(\mu(\sigma(U),U)\).  Continuity and the fact that the maps contain the
basepoint keep their images in \(\mathcal U_e\).

This row is therefore **VALID-WITH-CORRECTIONS** as a topological statement,
but it does not repair the smoothness needed later: its proposed contract says
only “continuous”/H-space data.  The induced \(\breve\sigma\) must separately
be proved smooth (or the local-index dependency must be replaced).

### 5.4 Item-by-item check against `lem-stage1-extra-fixed-class`

The fixed-class row's eight dependencies are listed at
`DESIGN-FUDW-DECOMP-v4.1.md:208`.  Their required interfaces are:

| dependency | what the fixed-class proof needs | audit |
|---|---|---|
| `lem-stage1-uniform-inversion-isolation` | isolation/nondegeneracy of the scalar quotient fixed class, with dimension-free derivative control | The proposed derivative and ledger can give the norm bound, but the descent of the derivative to \(i\mathcal H/i\mathbb RJ\) and positivity of \(\det(I-D\breve\sigma)\) are not in the unblocking map.  They must be derived explicitly. |
| `lem-stage1-quotient-manifold-package` | connected, compact, orientable, positive-dimensional manifold without boundary, at the regularity used by later leaves | **FAIL:** only \(C^1\), while landed consumers require smoothness. |
| `lem-stage1-quotient-finite-cw` | finite polyhedron/CW model | **FAIL with current inputs:** the landed triangulation row assumes a compact smooth manifold (`lem-topology-finite-triangulation.md:4,22--29`). |
| `lem-stage1-quotient-left-inversion` | continuous H-space multiplication and left-inversion homotopy | Repairable from the group/path rows after the domain and joint-continuity corrections. |
| `lem-stage1-left-inversion-trace` | trace formula for the induced left inversion | No new polar defect found, conditional on the H-space row and finite-CW input. |
| `lem-topology-lefschetz-hopf` | finite polyhedron, finite fixed set, and every fixed point in a maximal simplex | The landed contract is the narrowed maximal-simplex form (`argument/lemmas/lem-topology-lefschetz-hopf.md:4,25--33`).  The design does not mention or discharge this consumer obligation.  Under the contradiction assumption the fixed set is finite, but the maximal-simplex placement still has to be written against the chosen triangulation. |
| `lem-topology-local-index-sign` | smooth self-map of a compact orientable manifold and \(\det(I-Df)\ne0\) | **FAIL:** the proposed quotient/inversion interfaces are only \(C^1\).  The landed row explicitly flags this obligation (`argument/lemmas/lem-topology-local-index-sign.md:14--22`). |
| `lem-topology-orientable-top-cohomology` | connected compact orientable positive-dimensional manifold without boundary | Supplied if the quotient package is repaired; its exact landed contract is at `argument/lemmas/lem-topology-orientable-top-cohomology.md:4`. |

For the determinant sign, a repaired derivative row would suffice:
if \(\|D\breve\sigma+I\|<1\), then
\(I-D\breve\sigma=2I-E\) stays invertible along \(2I-tE\),
\(0\le t\le1\), so its determinant has the positive sign of \(2I\).
This uses the quotient norm and introduces no dimension-dependent constant.
It still requires a smooth \(\breve\sigma\) to invoke the landed local-index
row.

The design's statement that all three blocked consumers become transcribable
(`DESIGN-S1-POLAR.md:110--112`) is therefore **REFUTED**.

## 6. Definition-hygiene verdict

### `def-approximate-unitary-space`

**VALID-WITH-CORRECTIONS.**

The sets \(\mathcal H,i\mathcal H,\mathcal U,
\overline{\mathcal U}_\delta,\mathcal U_\delta,\mathcal U_e\) are datum/notation
and contain no theorem.  Reserving \(u,h,\mu,\sigma\) is legitimate only in the
explicitly partial form “whenever a result row supplies the required polar
domain”; the design correctly says that these maps are not total by
definition.

The source-coordinate clause is not clean as written.  Calling
\[
\phi_V(X)=L_V^{-1}(X-V)
\]
a “source chart” for an unqualified approximate-unitary \(V\) presupposes both
invertibility of \(L_V\) and the chart theorem.  TeX introduces the formula at
728--732 only after the small-domain inverse result at 699--725.  The shard
must instead say:

> for every \(V\) for which \(L_V\) is invertible, reserve
> \(\phi_V(X)=L_V^{-1}(X-V)\) and its Hermitian/anti-Hermitian components as
> source-coordinate notation; no assertion that it is a chart is made.

Do not put existence, regularity, polar admissibility, compactness,
orientation, isolation, or any estimate into the definition.  With that
qualification, the proposal respects R35
(`DESIGN-FUDW-DECOMP-v4.1.md:375--404,607`).

## 7. Claimed-gap and erratum verdicts

| design §7 item | verdict | exact hostile finding |
|---|---|---|
| Controlled \(C^*\)-rectification contract gap | **VALID-WITH-CORRECTIONS** | The landed rectification contract really is too weak (`lem-stage1-exact-unit-rectification.md:4`).  The replacement proof must also close exact-unit norm, product norm, associator, and involution compatibility; TeX 663--687 does not export the complete \(C^*\) package. |
| Straight-path domain gap | **VALID** | TeX 906 has only the assertion.  The right-inverse/Neumann and \(\overline{\mathcal U}_\eta\) estimates are absent. |
| Source-radius mismatch | **VALID** | TeX 809--843 supplies an inner shrunken radius; TeX 845 writes the larger \(\mathcal U_{\delta_{\max}}\) domain without deriving equality. |
| v4.1 derivative typing gap | **VALID** | \(D(\sigma-\mathrm{id})\) needs fixed source and target charts.  The proposed \(F_s\) repairs the type, subject to the missing domain dependency. |
| Printed second-variable derivative erratum | **VALID** | TeX 883--888 repeats \(\phi_U^\parallel(X)\) in both denominators.  The expected other-variable formula is not byte-present.  None of the eight proposed conclusions needs a quantitative second-variable derivative; \(C^1\) of multiplication follows from composition once the polar map is regular. |
| No numerical polar constants | **VALID** | TeX 458 gives data-independent concrete big-\(O\) functions, not printed numerical coefficients. |
| **Additional: \(C^1\)/smooth consumer mismatch** | **VALID — NEW DEFECT** | TeX 795--807 and the proposed rows stop at \(C^1\), but the landed quotient, triangulation, and local-index contracts are smooth. |
| **Additional: free witness / naked formula symbols** | **VALID — NEW DEFECT** | Design §1 prose does not bind existential constants across registry roots; rows 3--8 are not self-contained as written. |
| **Additional: inversion-derivative missing dep** | **VALID — NEW DEFECT** | Row 7 uses global \(\sigma\) without importing row 5's adjoint polar-domain result. |

## 8. Dimension-freeness audit

No genuine dimension-, amplification-, block-, or stage-dependent analytic
coefficient was found.

- Rectification, multiplier inversion, graph charts, and the polar map use
  Banach/operator norms and a fixed number of products
  (TeX 655--687,699--725,758--843).
- The tangent/normal direct sum always has two components.  TeX 560 permits
  norms between max and sum; all conversions therefore cost a fixed universal
  factor (possibly two conversions for an operator norm), never
  \(\dim\mathcal X\).
- The path identity in §3.6 has one quadratic term, and its right-inverse proof
  uses one Neumann comparison.
- The derivative formula at TeX 889--892 is an operator-norm formula.
  Passing to the quotient norm cannot enlarge the induced error once the
  vertical line is invariant.
- Finite dimensionality is used qualitatively for compactness and for
  injective \(\Rightarrow\) surjective in the closedness proof.  It does not
  choose an analytic coefficient.
- If an amplification satisfies the same extended
  \(\varepsilon_r\)-\(C^*\) axioms, the same level-free estimates apply.
  No entrywise or basis sum is present.

The dimension-freeness claim is therefore **VALID-WITH-CORRECTION**: the
factor-two sentence about direct-sum operator norms must be stated carefully,
and the proposed smooth upgrade must remain qualitative/operator-norm based.
There is **NO ROUTE-LEVEL DIMENSION-FREENESS ALARM** in the audited material.

## 9. Required redesign before any landing

1. Add a closed smoothness producer (smooth unitary charts, smooth polar
   inverse, and smooth \(\mu,\sigma\)), or acquire and validate exact \(C^1\)
   quotient/triangulation/local-index theorems.  Do not claim either option is
   already in the audited local sources.
2. Rewrite every root contract so all witnesses are quantified and
   \(r_\pm,\eta_{\rm path}\) are inlined or theorem-free defined.
3. Add the group/adjoint-domain dependency to the inversion-derivative row.
4. Expand the rectified \(C^*\) proof to every axiom, including exact-unit norm.
5. Qualify \(\phi_V\) in the proposed definition by invertibility of \(L_V\)
   and call it coordinate notation, not a chart.
6. Extend the fixed-class consumer plan to discharge smoothness,
   quotient-derivative descent and determinant sign, the triangulation
   hypothesis, and the landed Lefschetz maximal-simplex obligation.
7. Preserve the conditional finite-minimum arithmetic from §2; it needs no
   numerical change once the witness interface is repaired.

Until all seven corrections receive a new hostile audit, the correct
disposition remains **REDESIGN; DO NOT LAND OR SEED**.
