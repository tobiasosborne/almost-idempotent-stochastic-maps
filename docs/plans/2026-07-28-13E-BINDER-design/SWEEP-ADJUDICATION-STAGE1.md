# Comprehensive Stage-1 binder adjudication

The standard applied throughout is extensional but typed: a shared name does
not identify maps exported by opaque contracts.  Identification is available
when both maps are components of fully typed inverses of the same displayed
polar map, or pointwise when both typed preimages are exhibited.  Conversely,
an anaphor resolving to the tree's sole explicit construction is not treated
as a second map.

## `lem-stage1-rectified-cstar-control`

The product \(\boldsymbol\cdot\) and unit \(J\) are constructed explicitly in
nodes 1.1--1.2 and retained through the axiom-transfer argument.  No opaque
external map is identified with a separately typed map; the two registered
externals do not participate in any such identification.

lem-stage1-rectified-cstar-control VERDICT: SOUND

## `lem-stage1-unitary-graph-control`

Every \(g_V\) is defined inside the tree as the unique zero of the displayed
\(f_V\) on the displayed Hermitian ball.  The quantitative inverse-function
external is applied to that same internally displayed function.  There is no
second graph map or polar inverse to synchronize.

lem-stage1-unitary-graph-control VERDICT: SOUND

## `lem-stage1-maurer-cartan-trivialization`

The root expressly concerns “the graph maps supplied by
lem-stage1-unitary-graph-control,” and the sole external supplies exactly that
one graph family.  The proof never substitutes a separately bound family for
it; \(\omega_U(Z)=(L_U^{-1}Z)^\parallel\) is defined directly on the resulting
intrinsic tangent bundle.

lem-stage1-maurer-cartan-trivialization VERDICT: SOUND

## `lem-stage1-polar-retraction`

The tree constructs the displayed map
\(\Pi_\delta(U,H)=U\boldsymbol\cdot H\), proves its global injectivity, and
defines \((u_\delta,h_\delta)\) as its own set-theoretic inverse.  Its graph
external is used only to build coordinates for this single construction.
Thus every inverse-uniqueness use has two typed preimages under the same
displayed \(\Pi_\delta\).

lem-stage1-polar-retraction VERDICT: SOUND

## `lem-stage1-polar-coherence-naturality`

The hypotheses themselves provide two fully typed inverse data
\((\delta_j,S_j,u_j,h_j)\) for the displayed maps
\(\Pi_{\delta_j}(U,H)=U\boldsymbol\cdot H\).  Nodes 1.1.1--1.1.3 place both
preimages in the larger typed domain and invoke its injectivity.  This is
exactly the permitted inverse-uniqueness argument.

lem-stage1-polar-coherence-naturality VERDICT: SOUND

## `lem-stage1-group-domain-membership`

There is only one polar construction in the tree: the fully typed datum
imported from `lem-stage1-polar-retraction`.  Nodes 1.1 and 1.8 prove that the
two inputs lie in that datum's explicit \(S_\delta\), and the root's anaphoric
“inverse of the polar map” resolves to this sole construction.  No
cross-contract inverse equality is used.

lem-stage1-group-domain-membership VERDICT: SOUND

## `lem-stage1-group-closeness`

Again the only polar datum is the typed retraction external.  In nodes
1.3.1--1.3.3, \(u=u_\delta(X)\) and \(h=h_\delta(X)\) are the two components
of that same inverse and satisfy the supplied typed identity
\(X=u\boldsymbol\cdot h\).  The resulting closeness estimate does not compare
two independently bound \(u_\delta\)'s.

lem-stage1-group-closeness VERDICT: SOUND

## `lem-stage1-approximate-group-laws`

Node 1.1.2 makes the decisive unsupported inference:

> “every polar datum produced above uses the same map
> \(\Pi_\delta:(U,H)\mapsto U\boldsymbol\cdot H\) on the same full domain
> ... The external lem-stage1-polar-coherence-naturality identifies their
> inverse components on that common image.”

Only `lem-stage1-polar-retraction` exports such a fully typed datum.  The
opaque membership and closeness contracts export an anaphoric first
component \(u_\delta:S_\delta\to\mathcal U\), but no companion \(h_\delta\),
no displayed source map, and no preimage identity.  Therefore coherence's
two-data antecedent is unavailable, and the membership, closeness, and
regularity conclusions cannot be attached to one common inverse.

lem-stage1-approximate-group-laws VERDICT: DEFECTIVE (export.md node 1.1.2)

## `lem-stage1-polar-path-admissibility`

The path is placed in the single explicit \(S_\delta\) supplied by the
retraction external.  Node 1.3.3 applies scalar naturality to the fully typed
datum \((\delta,S_\delta,u_\delta,h_\delta)\), after node 1.3.2 proves both
\(X\) and \(cX\) lie in its domain.  No second inverse is introduced.

lem-stage1-polar-path-admissibility VERDICT: SOUND

## `lem-stage1-smooth-unitary-atlas`

The root explicitly upgrades the same unique graph functions supplied by
graph control.  Nodes 1.2--1.3 apply the implicit-function theorem to the
same displayed equation and use its typed uniqueness clause to identify the
local smooth branch pointwise with the original \(g_V\).  This is a valid
single-construction-chain identification.

lem-stage1-smooth-unitary-atlas VERDICT: SOUND

## `lem-stage1-smooth-polar-inverse`

The root displays the same ambient-bilinear \(\Pi_\delta\), source, and target
as the typed retraction import.  Nodes 1.4.3--1.4.4 identify the smooth
inverse with the old inverse because both are fully typed inverses of that
same bijection.  Ordinary inverse uniqueness applies.

lem-stage1-smooth-polar-inverse VERDICT: SOUND

## `lem-stage1-smooth-unitary-operations`

Node 1.2.1 asserts that approximate group laws supplies “the same global
\(C^1\) maps \(\mu\) and \(\sigma\),” and node 1.2.2 then says:

> “Composing with the smooth \(u_\delta:S_\delta\to\mathcal U\) from
> lem-stage1-smooth-polar-inverse proves that \(\mu\) and \(\sigma\) are
> smooth.”

The \(u_\delta\) in smooth-polar-inverse is the typed first component of the
displayed \(\Pi_\delta\) inverse; the \(u_\delta\) in the opaque
approximate-group contract is merely anaphoric.  No typed companion or
pointwise preimage witness attaches them.  The same unsupported attachment
is reused in nodes 1.3.1.2 and 1.3.2 to apply scalar naturality to the
group-law operations.  The scalar-action subargument alone is sound, but it
does not certify the compound root.

lem-stage1-smooth-unitary-operations VERDICT: DEFECTIVE (export.md nodes 1.2.1--1.2.2, 1.3.1.2, and 1.3.2)

## `lem-stage1-polar-scalar-arithmetic`

This tree is scalar arithmetic only.  It imports no external and binds no
polar, graph, or operation map, so the defect class cannot occur.

lem-stage1-polar-scalar-arithmetic VERDICT: SOUND

## `lem-stage1-rectified-cstar-transport`

The transport reuses the product and unit supplied by its sole producer and
only weakens numerical bounds by parameter monotonicity.  It introduces no
second same-named map.

lem-stage1-rectified-cstar-transport VERDICT: SOUND

## `lem-stage1-unitary-graph-transport`

The root and producer display the same domain, codomain, \(f_V\) equation,
and uniqueness clause.  Node 1.1.6 directly takes the producer's unique
graph value, and node 1.1.7 only enlarges constants.  No opaque graph
anaphor is attached to a different family.

lem-stage1-unitary-graph-transport VERDICT: SOUND

## `lem-stage1-maurer-cartan-transport`

Nodes 1.3.4--1.3.7 give a sound alternative derivation that avoids comparing
the root's explicitly typed family \(g\) with the external's distinguished
graph family \(\bar g\).  The current export nevertheless retains a
validated defective inference.  Node 1.3.2 correctly records:

> “The sole registered external does not supply this additional antecedent,
> so this node does not assert the unconditional equality \(g=\bar g\).”

But the sibling node 1.3.3 immediately asserts:

> “Because \(g\) and \(\bar g\) are \(C^1\) and equal pointwise ...
> \(Dg_U(0)=D\bar g_U(0)\).”

The external contract does not type \(\bar g\) on the root's displayed ball
or assert its displayed zero equation, so the equality premise is absent.
Because the task asks whether *any* inference in the exported tree commits
the attachment, the later independent repair does not preserve this current
certificate; pruning and revalidation would be sufficient.

lem-stage1-maurer-cartan-transport VERDICT: DEFECTIVE (export.md node 1.3.3)

## `lem-stage1-polar-retraction-transport`

The root explicitly displays \(\Pi_\delta\), its full source, and its target
as the image of that very map.  The producer external supplies a fully typed
inverse for exactly this displayed bijection.  Nodes 1.3--1.4 retain that
same inverse while only weakening the radius sandwich, so inverse uniqueness
is legitimate.

lem-stage1-polar-retraction-transport VERDICT: SOUND

## `lem-stage1-polar-path-transport`

The root explicitly binds \(u_\delta\) as the first component of the inverse
of its displayed \(\Pi_\delta\).  Its sole external, however, exports only
the anaphoric path formula \(H=u_\delta(Z_t)\), with no \(h_\delta\), no
displayed \(\Pi_\delta\), and no typed preimage identity.  Node 1.3.1 makes
the unsupported attachment:

> “it yields ... the map \(H(t,U_0,U_1)=u_\delta(Z_t)\), with the same
> polar-inverse notation \(u_\delta\) used in node 1.”

Sameness of notation is not an equality premise, and no allowed input
supplies the missing typed witness for the parent's anaphoric factor.

lem-stage1-polar-path-transport VERDICT: DEFECTIVE (export.md node 1.3.1)

## CASCADE

Dependency-ordered demotion set:

1. `lem-stage1-approximate-group-laws` — currently validated; demote for its
   direct node-1.1.2 defect.
2. `lem-stage1-maurer-cartan-transport` — currently validated and independent
   of item 1; demote because node 1.3.3 remains in the certified export.
3. `lem-stage1-polar-path-transport` — currently validated and independent of
   items 1--2; demote for its direct node-1.3.1 defect.
4. `lem-stage1-smooth-unitary-operations` — currently validated and dependent
   on item 1; demote both by cascade and for its own direct attachment defect.
5. `lem-stage1-inversion-derivative-control` — the prior allegation is
   independently confirmed at node 1.3; it depends on item 1 and is already
   demoted to stated/seeded, so no new status action is required.
6. `lem-stage1-inversion-derivative-transport` — the prior allegation is
   independently confirmed at nodes 1.3, 1.5.5, and 1.6; it depends on items
   1, 4, and 5 and is already demoted to stated/seeded, so no new status
   action is required.

The swept validated certificates that survive intact are exactly:

- `lem-stage1-rectified-cstar-control`
- `lem-stage1-unitary-graph-control`
- `lem-stage1-maurer-cartan-trivialization`
- `lem-stage1-polar-retraction`
- `lem-stage1-polar-coherence-naturality`
- `lem-stage1-group-domain-membership`
- `lem-stage1-group-closeness`
- `lem-stage1-polar-path-admissibility`
- `lem-stage1-smooth-unitary-atlas`
- `lem-stage1-smooth-polar-inverse`
- `lem-stage1-polar-scalar-arithmetic`
- `lem-stage1-rectified-cstar-transport`
- `lem-stage1-unitary-graph-transport`
- `lem-stage1-polar-retraction-transport`

No other currently validated result is a descendant of the four newly
demoted validated results.  Their remaining registered descendants
(`lem-stage1-approximate-group-laws-transport`,
`lem-stage1-polar-constant-ledger`, and the quotient/inversion follow-ons)
are already stated, seeded, or otherwise unvalidated and therefore do not
add T0 demotions.

## ROOT-CAUSE

The elevating cohorts systematically treated repeated notation and definite
descriptions as binder unification across opaque theorem boundaries: they
read “the inverse \(u_\delta\) of the polar map,” “the same maps,” or “the
same polar-inverse notation” as if each phrase supplied an equality with the
one explicitly typed \(\Pi_\delta\)-inverse in scope.  That silently removed
coherence's second fully typed inverse datum, or the equivalent pointwise
preimage witness.  The same acceptance pattern also left an invalid
graph-family identification in a certificate after a later branch had
correctly bypassed it.  Ordinary uniqueness remains valid in the surviving
single-construction chains; the defect is precisely the elevation of
same-named anaphora into missing equality premises.
