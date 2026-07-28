# Hostile audit — 13e explicit-binder repair v2

1. **Location:** `DESIGN-13E-BINDER-v2.md` §§1.7–1.8 and §4, especially
   lines 215–218, 233, and 325–326;
   `proofs/lem-stage1-approximate-group-laws/export.md`, nodes 1.1–1.1.2;
   `proofs/lem-stage1-smooth-unitary-operations/export.md`, nodes
   1.2.1–1.3.2; and the corresponding registry contracts and externals.
   **Defect:** The claimed preservation of the old group-laws family and
   old smooth-operations certificate overlooks the adjudicated defect inside
   those actual export trees.  Approximate-group node 1.1.2 says that the
   membership and closeness children have produced polar *data* and invokes
   coherence to identify their inverse components with the retraction
   inverse.  Their opaque contracts export only an anaphoric first component
   (and no typed companion \(h\), displayed source map, or preimage identity);
   hence the two-data antecedent of coherence is not available.  Smooth-
   operations nodes 1.2.2, 1.3.1.2, and 1.3.2 then compose the smooth
   explicitly typed retraction inverse and invoke scalar naturality for the
   anaphoric group-law inverse without a typed datum attaching the two.
   This is the same missing-\(h_X\) inference confirmed by the adjudication,
   now found one level upstream.  The scalar-action subcalculation of the
   smooth-operations export is sound, but it is not a separately certified
   registry result; a valid sub-conjunct cannot preserve the certificate of
   the defective compound root.  Consequently
   `lem-stage1-quotient-manifold-package` cannot safely retain the old
   smooth-operations row merely because it needs only the scalar action, and
   the claim that zero existing certificates are disturbed is false.
   **Severity: MAJOR.** **Prescribed repair:** Demote and either re-elevate or
   retire `lem-stage1-approximate-group-laws` and
   `lem-stage1-smooth-unitary-operations` under the typed-witness law.  Since
   the v2 spine bypasses both, the cheaper repair is to demote them, delete
   the old smooth-operations dependency from
   `lem-stage1-quotient-manifold-package`, and prove smoothness of the
   binder-free scalar action locally from scalar preservation plus the
   embedded atlas; alternatively depend on the new explicit smooth bridge
   and register every one of its typed antecedents.  Amend the complete
   classification, certificate-cascade statement, shard count, T0/cost
   accounting, and the quotient-manifold consumer trace.

2. **Location:** `DESIGN-13E-BINDER-v2.md` §1.6 and §§2–4, especially lines
   165–169, 247–248, 286–294, and 328–333;
   `proofs/lem-stage1-inversion-derivative-control/export.md`, nodes 1.4,
   1.8, and 1.9.  **Defect:** The proposed direct 13g replay says that
   repaired 13e supplies the *receiving-\(W\)* closeness and that a universal
   fresh \(C_{\rm der}^0\) absorbs the old derivative calculation.  This is
   not the estimate used by the old control tree.  Repaired 13e instantiated
   at the receiving tuple gives only
   \(\|u_\delta(X)-X\|\le C_{\rm grp}\varepsilon_r\), while the receiving
   fields \(C_{\rm grp}\) and \(C_{\rm der}\) have independent lower bounds
   and \(C_{\rm grp}\) is unbounded above.  Control nodes 1.4 and 1.8 make
   the normal and differentiated-error constants depend on the closeness
   coefficient, and node 1.9 can absorb that dependence only because its
   \(C_{\rm grp}\) is one fixed existential witness.  No universal
   \(C_{\rm der}^0\) can absorb an arbitrary receiving \(C_{\rm grp}\).
   Thus the stated receiving-\(W\) replay does not prove the byte-frozen 13g
   contract, even though the remaining polar/graph identifications and the
   25-node cap are otherwise realistic.  **Severity: MAJOR.**
   **Prescribed repair:** Use a fixed closeness coefficient.  Either add
   `lem-stage1-explicit-group-closeness` to 13g's deps and external list and
   put its fixed witness into the 13g maxima/minima, or explicitly construct
   a fixed auxiliary witness tuple \(W_0\) whose
   \(C_{\rm grp},C_{\rm pol},\kappa_{\rm pol}\) are the universal 13e base
   witnesses, prove by monotonicity that the receiving guards imply the
   \(W_0\) guards, and apply 13e at \(W_0\), not at the receiving tuple.
   Then make \(C_{\rm der}^0\) depend only on that fixed coefficient and
   update the node skeleton/budget narrative.  Do not cite hidden proof-body
   constants of 13e through its opaque contract.

VERDICT: REJECT (the design preserves upstream certificates containing the adjudicated untyped-map inference and its direct 13g replay uses an unbounded receiving closeness coefficient)
