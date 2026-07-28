# Independent adjudication of the T0 synchronization allegation

This adjudication treats each registered external as an opaque theorem with
exactly its recorded contract.  Reusing the name \(u_\delta\) in two opaque
contracts is not itself an equality premise.  The common-knowledge uniqueness
principle used below is:

> If a map is injective, two *typed preimages under that same map* of the same
> point are equal.

Thus one may identify two polar factors either from two fully typed inverse
data for the same polar map, or pointwise from a typed witness
\(\Pi_\delta(u(X),h_X)=X\).  Uniqueness cannot supply the second preimage
premise.

## T1: `lem-stage1-inversion-derivative-control`

### Inference at issue

The decisive sentence in `export.md`, node 1.3, is:

> Global polar factorization: for A in B_r^{icalH}(0), U=chi_s(A) belongs to
> calU by lem-stage1-unitary-graph-control. The common polar inverse supplied
> by lem-stage1-polar-retraction, identified across admissible polar data by
> lem-stage1-polar-coherence-naturality, and the all-calU adjoint domain in
> lem-stage1-approximate-group-laws give C1 maps
> W=sigma(U)=u_delta(U^dagger) and Q=h_delta(U^dagger)-J in calH with
> ||Q||<delta and the exact identity
> U^dagger=W bold-dot (J+Q). Moreover
> ||W-U^dagger||<=C_grp*epsilon_r; scalar naturality, or directly
> u_delta(sJ)=sJ, also gives sigma(sJ)=sJ.

The same \(W\) is used twice: the group-law external supplies the closeness
estimate for its polar factor, while the retraction external supplies the
exact factorization for its inverse first component.

### Exact registered externals

These are the only four external JSON inputs:

| JSON id | name | content hash | operative exact clause |
|---|---|---|---|
| `36342a3be0cf1dad` | `lem-stage1-unitary-graph-control` | `34841ccef6e8762af1b5334becf9c6acd3dadbaa45491b3d78face9e728fee34` | It supplies the unique \(C^1\) graph function \(g_V\), its displayed \(f_V=0\) equation, estimates, and covering charts. |
| `1c99250f251f0e99` | `lem-stage1-polar-retraction` | `aaf5b1caf16ca66e58188e2e57b1af6ae519e5b37f52eda3ae714a0a343dde47` | “Pi_delta(U, H) = U bold-dot H is a C^1 diffeomorphism from calU x B… onto an open S_delta, its inverse (u_delta, h_delta) obeys X = u_delta(X) bold-dot h_delta(X)”. |
| `73f77e90ae421562` | `lem-stage1-polar-coherence-naturality` | `cd502a0f3075af269f9c1705897c429d71e9105bd366cc23b70f391941eecb84` | Given **two polar data** \((\delta_j,S_j,u_j,h_j)\) for which the explicitly typed \(\Pi_{\delta_j}\) is bijective with inverse \((u_j,h_j)\), their inverses agree on the target overlap. |
| `848cb6207a25d600` | `lem-stage1-approximate-group-laws` | `d510c2188a3c30ee73450f3740c80e8bd4c0687b94a1c45be48db698663f6d53` | “the inverse u_delta of the polar map defines C^1 maps” \(\mu(U,V)=u_\delta(U\mathbin{\boldsymbol\cdot}V)\) and \(\sigma(U)=u_\delta(U^\dagger)\), followed by the stated estimates.  It gives no \(S_{\rm grp}\), \(h_{\rm grp}\), typed source/target for that polar map, or preimage identity for this function. |

The two registered definitions add no synchronization premise.
`def-approximate-unitary-space` expressly reserves \(u,h\) only as partial
notation on domains supplied by result rows and asserts no inverse theorem;
`def-epsilon-cstar-algebra` supplies only the algebraic and norm axioms.

### Derivability

Rename the retraction inverse \((u_{\rm pol},h_{\rm pol})\) and the function
in the group-law contract \(u_{\rm grp}\).  The exact inputs yield

\[
 U^\dagger
 =u_{\rm pol}(U^\dagger)\boldsymbol\cdot h_{\rm pol}(U^\dagger)
 \quad\text{and}\quad
 \|u_{\rm grp}(U^\dagger)-U^\dagger\|
 \le C_{\rm grp}\varepsilon_r.
\]

They do not yield
\[
 u_{\rm grp}(U^\dagger)=u_{\rm pol}(U^\dagger).
\]

Here \(U^\dagger\in S_\delta\) is not the obstruction: \(U^\dagger\) is
unitary and the positive inner-radius inclusion in the retraction contract
places it in \(S_\delta\).  The missing premise is a typed
\(h_X\in B_\delta^{\mathcal H}(J)\) satisfying
\[
 U^\dagger
 =u_{\rm grp}(U^\dagger)\boldsymbol\cdot h_X.
\]
The available identity with \(h_{\rm pol}(U^\dagger)\) is paired with
\(u_{\rm pol}\), not \(u_{\rm grp}\).  Taking
\(h_X=h_{\rm pol}(U^\dagger)\) would already assume the equality being
proved.

Coherence does not repair this: it is conditional on two already typed polar
data, and only the retraction datum is available.  Applying coherence to that
datum twice is tautological.  Consequently node 1.3 cannot use one \(W\) for
both the exact factorization and the group-law closeness estimate.  Every
later differentiated factorization depends on that unsupported step.

T1 VERDICT: DEFECTIVE (export.md node 1.3)

## T2: `lem-stage1-inversion-derivative-transport`, run 2

### Inferences at issue

`export.md`, node 1.3, says:

> Polar binder identification: under the transported
> lem-stage1-polar-retraction guard, Pi_delta(U,H)=U bold-dot H is a C^1
> diffeomorphism from calU times B_delta^{calH}(J) onto the same image
> S_delta used in node 1. Hence its inverse exists uniquely, and the u_delta
> explicitly bound in node 1 is exactly the first inverse component supplied
> by lem-stage1-polar-retraction and consequently the polar inverse component
> used by the imported group and inversion statements.

Node 1.4 makes the graph identification:

> Graph binder identification: for s in {+1,-1}, sJ lies in calU and hence
> in calUbar_delta. Under the transported graph guard,
> lem-stage1-unitary-graph-control at V=sJ supplies exactly one C^1 map
> g_{sJ}:B_{2delta}^{icalH}(0) to B_{2delta}^{calH}(0) satisfying the
> displayed f_{sJ} equation. Thus it is exactly the g_{sJ} bound in node 1,
> and the resulting graph parametrization is exactly
> chi_s(A)=sJ bold-dot (J+A+g_{sJ}(A)).

Node 1.5.5 then says:

> Operation upgrade: the transported polar and group-defect guards apply
> lem-stage1-approximate-group-laws, defining
> sigma(U)=u_delta(U^dagger) on all calU for the unique inverse component
> identified in node 1.3. This result and node 1.5.4 are precisely the three
> antecedents named by lem-stage1-smooth-unitary-operations: approximate
> group laws, smooth unitary atlas, and smooth polar inverse. Therefore that
> external makes the same sigma smooth as a self-map of calU and explicitly
> changes no point or first derivative.

Finally node 1.6 invokes the parent after those identifications:

> Final derivative transport: apply
> lem-stage1-inversion-derivative-control with its selected I-witnesses and
> the transported five guards. After the polar, graph, and sigma
> identifications above, its chi_s, sigma, F_s and chart are precisely those
> in node 1.

### Exact registered externals

Run 2 has exactly seven external JSON inputs:

| JSON id | name | content hash | relevant exact content |
|---|---|---|---|
| `9b9fbd865ce00979` | `lem-stage1-polar-retraction` | `aaf5b1caf16ca66e58188e2e57b1af6ae519e5b37f52eda3ae714a0a343dde47` | The typed \(\Pi_\delta\) diffeomorphism and inverse pair \((u_\delta,h_\delta)\), with \(X=u_\delta(X)\boldsymbol\cdot h_\delta(X)\). |
| `251f701f67623c41` | `lem-stage1-unitary-graph-control` | `34841ccef6e8762af1b5334becf9c6acd3dadbaa45491b3d78face9e728fee34` | The unique \(C^1\) \(g_V\) satisfying the displayed \(f_V=0\) equation. |
| `3913dc87b5569340` | `lem-stage1-approximate-group-laws` | `d510c2188a3c30ee73450f3740c80e8bd4c0687b94a1c45be48db698663f6d53` | Group conclusions for “the inverse u_delta of the polar map”, without a typed companion or preimage identity. |
| `8bf3dc1f6dc5fe9f` | `lem-stage1-smooth-unitary-atlas` | `6ebc1a63c5de8eec9bcec99863a36d5d43ed7b6f010e7611e15a90e5e1fca1fc` | It upgrades the **same graph functions and charts** furnished by graph control. |
| `8a04f65eda6b51ca` | `lem-stage1-smooth-polar-inverse` | `a28e688168e5061b2acf7b20cb0e3443f676681540a3cb31690729d6a5cef313` | It upgrades the **same ambient-bilinear Pi_delta** and its **same set-theoretic inverse (u_delta,h_delta)** from polar retraction. |
| `bb300325401de04d` | `lem-stage1-smooth-unitary-operations` | `81f77027a22f4515345aa9d0468ba640b4636b6557be5391bd39973106836056` | Under group laws, smooth atlas, and smooth polar inverse, it makes the “same maps” \(\mu,\sigma\) smooth and changes no point or first derivative; it states no equality between a separately named group-law factor and the retraction inverse. |
| `63d9de5caf21a034` | `lem-stage1-inversion-derivative-control` | `1a4de57ede66ca7c7d13f681b989dfe2bdbacaafcdcf45ab6ff7205ddb851f14` | It exports the derivative estimate for the anaphoric \(\sigma(U)=u_\delta(U^\dagger)\) and \(\chi_s\), but does not type its \(u_\delta\) as the first component of the displayed \(\Pi_\delta\) inverse. |

The registered `def-stage1-polar-witness-data` is scalar data only, and the
other two definitions are the same vocabulary/algebra definitions described
under T1.  None adds a map-identification theorem.

### Derivability

The first half of node 1.3 is sound: the root displays the same
\(\Pi_\delta\), source, and image as polar retraction, so ordinary inverse
uniqueness identifies the root \(u_\delta\) with
\(u_{\rm pol}\).  Node 1.4 is also sound: its domain, codomain, displayed
\(f_{sJ}=0\) condition, and \(C^1\) requirement match graph control, whose
contract asserts uniqueness.  The smooth-atlas and smooth-polar-inverse
upgrades preserve those explicitly identified objects.

The word “consequently” in the second half of node 1.3 does not follow.
Polar retraction supplies one typed datum
\((u_{\rm pol},h_{\rm pol})\).  It supplies no typed datum containing the
function \(u_{\rm grp}\) from approximate group laws or the anaphoric
function \(u_I\) in the parent control contract.  Smooth-unitary-operations
does not create that equality: its “same maps” clause preserves the maps
whose common identity is required in its antecedent; it does not assert
\(u_{\rm grp}=u_{\rm pol}\).  Thus node 1.5.5 cannot use that external as a
synchronization lemma.

The explicit root map
\(\sigma_{\rm pol}(U)=u_{\rm pol}(U^\dagger)\) can in fact be shown \(C^1\)
directly from polar retraction plus smooth-polar-inverse (and the smooth
linear involution), so global regularity alone is not the fatal gap.  The
fatal use is node 1.6: the parent external's derivative conclusion concerns
\(\sigma_I(U)=u_I(U^\dagger)\).  No registered clause gives a typed
\(h_X\) with
\[
 X=u_I(X)\boldsymbol\cdot h_X
\]
for the explicit root \(\Pi_\delta\), nor otherwise states
\(u_I(X)=u_{\rm pol}(X)\).  Hence its estimate cannot be substituted for the
root's explicitly bound \(F_s\).  This remains true even granting the
sound graph identification.

T2 VERDICT: DEFECTIVE (export.md nodes 1.3, 1.5.5, and 1.6)

## Comparison with the W93 STUCK record

W93's final workspace had exactly
`lem-stage1-approximate-group-laws`,
`lem-stage1-polar-retraction`, and
`lem-stage1-polar-coherence-naturality` as externals.  Thus it already had
the same typed retraction datum and the same conditional coherence theorem
as T1.  Its validated nodes 1.7.5.2--1.7.5.2.2 correctly reduced the needed
comparison to pointwise typed preimages; nodes 1.7.7.1.1 and 1.7.8.1 record
that the group-law contract supplies no second polar datum.  The last
challenge at node 1.7.8.2 correctly notes that group laws *does* supply the
unitary-valuedness of its outputs; the genuinely absent ingredients are the
explicit-image/preimage connection and, decisively, an \(h_X\) satisfying
\(\Pi_\delta(u_{\rm grp}(X),h_X)=X\).

For W93's product inputs \(X=U\boldsymbol\cdot V\), even membership in the
explicit \(S_\delta\) was not supplied by those contracts.  For T1 and T2,
the relevant input is \(X=U^\dagger\), so the retraction's inner inclusion
and exact unitarity give \(X\in S_\delta\).  That difference removes the
membership subproblem but not the preimage/synchronization subproblem.
Therefore W93 is not identical in every auxiliary premise, but its
missing-\(h_X\) obstruction is exactly the one used unsoundly in T1 and T2.
T2's additional atlas and smoothness externals correctly identify the graph
and the retraction inverse; none attaches the group or parent-control
function to that inverse.

No currently af-validated result other than T2 depends on T1, and no
currently af-validated result depends on T2.  The two targets themselves
must therefore be re-elevated in dependency order; their present stated
descendants do not add further T0 re-elevations.

CASCADE: lem-stage1-inversion-derivative-control, lem-stage1-inversion-derivative-transport
