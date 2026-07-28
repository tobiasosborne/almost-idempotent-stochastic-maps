# Hostile audit — 13e explicit-binder repair

1. **Location:** `DESIGN-13E-BINDER.md` §§0, 3, especially lines 37–45 and
   204–217; `argument/lemmas/lem-stage1-smooth-unitary-operations.md:4`;
   `proofs/lem-stage1-smooth-unitary-operations/export.md`, nodes 1.2–1.4.
   **Defect:** The rows-14+ consumer trace silently reintroduces the rejected
   identification with the elliptical family.  Repaired 13e and row-13
   clause `(A_5)` define the explicit maps
   `mu_pol(U,V)=u_pol(U bold-dot V)` and
   `sigma_pol(U)=u_pol(U^dagger)`.  The existing smooth-operations contract
   upgrades the “same maps” supplied under
   `lem-stage1-approximate-group-laws`, hence the anaphoric
   `mu_grp,sigma_grp`.  Importing that contract together with row 13 does not
   prove `mu_grp=mu_pol` or `sigma_grp=sigma_pol`.  Row 13 supplies a typed
   datum only for `u_pol`; it does not retroactively put `u_grp` into a second
   typed polar datum.  This is exactly the W93 gap, not a consequence of
   having both assertions in the same downstream proof.  The defect is
   load-bearing for `lem-stage1-uniform-inversion-isolation`,
   `lem-stage1-quotient-left-inversion`, and
   `lem-stage1-quotient-inversion-index-data`, which need smoothness and/or
   scalar covariance for the explicit row-13 operation.  **Severity:
   MAJOR.** **Prescribed repair:** Either adopt R2, or add and elevate an
   explicit-binder smooth-operations bridge whose contract binds the displayed
   `Pi_delta` inverse and derives smoothness and scalar covariance directly
   from repaired 13e, the smooth atlas, the explicit smooth polar inverse, and
   scalar naturality.  Rewire every affected rows-14+ consumer to that bridge
   and redo the consumer/cost trace.

2. **Location:** `DESIGN-13E-BINDER.md` §§1.4, 2.1, 3 and 5, especially lines
   132–134, 163–176, 198–202, and 247–250;
   `proofs/lem-stage1-inversion-derivative-control/export.md`, node 1.2;
   `proofs/lem-stage1-inversion-derivative-transport/export.md`, nodes
   1.3 and 1.5; the corresponding external JSON files importing
   `lem-stage1-approximate-group-laws`.  **Defect:** The claimed untouched
   `(A_7)` path already contains the same invalid synchronization.  The
   inversion-control export calls the polar factor “common” and invokes
   coherence although its group-laws input supplies no typed second polar
   datum.  The 13g export then states that whenever the anaphoric group,
   smooth-operation, or inversion-control result uses a polar inverse,
   uniqueness identifies it with the root's explicit first component.  W93
   established verbatim that this inference is unavailable without typed
   preimage witnesses.  Thus the fact that the 13g registry contract matches
   `(A_7)` verbatim does not make its actual proof-body sound under its exact
   externals.  Consequently “existing T0 re-elevations / external swaps =
   0 / 0” is not a sound campaign price, even though the narrow grep claim
   that the two proposed new contracts themselves alter no existing external
   JSON is correct.  **Severity: MAJOR.** **Prescribed repair:** Put
   `lem-stage1-inversion-derivative-control` and
   `lem-stage1-inversion-derivative-transport` back through hostile
   re-audit/re-elevation on an explicit-binder dependency spine (or adopt R2).
   In particular, repaired explicit 13e may provide the globally `C^1`
   explicit `sigma`, but the derivative-control estimate must also be
   restated or re-derived for that same explicitly bound inverse.  Update the
   action table, cascade statement, and cost counts accordingly.

3. **Location:** `DESIGN-13E-BINDER.md` §§1.1–1.2 and 4, especially lines
   52, 70, and 235; paused W93 ledger nodes 1.7.5.2.1–1.7.5.2.2 and challenge
   `ch-5b4d3d15682d1903`.  **Defect:** The two new bridge contracts do not
   carry “exactly” the premises W93 found missing for an identification
   argument.  W93's final pointwise criterion already had
   `u_grp(X) in calU`; the missing data were `X in S_delta` and an
   `h_X in B_delta^{calH}(J)` with
   `Pi_delta(u_grp(X),h_X)=X`.  The first new bridge supplies explicit-image
   membership plus an algebraic right inverse of `X`, which is not such an
   `h_X`; the second supplies closeness estimates for `u_pol`.  This is
   mathematically acceptable only as a bypass that discards `u_grp`, not as
   completion or factoring of the missing synchronization premises.
   **Severity: MINOR.** **Prescribed repair:** State explicitly that the new
   rows do not discharge the W93 missing-premise test and are instead the two
   quantitative ingredients of a fresh direct proof for `u_pol`; remove any
   wording suggesting that an algebraic right inverse is the missing polar
   preimage witness.

4. **Location:** `DESIGN-13E-BINDER.md` §1.3, lines 96 and 109–113.
   **Defect:** `lem-stage1-polar-coherence-naturality` is not a genuine
   dependency of the proposed direct 13e proof.  If the two new contracts'
   explicit definite descriptions are available, all applications concern
   the unique inverse of the identical displayed map and equality is ordinary
   inverse uniqueness.  If those definite descriptions are not available,
   coherence cannot manufacture them, as W93 showed.  Calling coherence a
   “synchronization check” therefore makes it either redundant or circular
   and obscures the point of the repair.  The actual `8*G_c` proof template
   uses only the two explicit bridges, polar retraction, the algebra axioms,
   and the guard arithmetic; its estimates are endpoint-safe at
   `epsilon_r=0`, and the constants
   `max{G_d,8*G_c,8}`, `max{P_d,P_c,P_r}`, and
   `min{k_d,k_c,k_r,1/16}` are arithmetically sufficient.
   **Severity: MINOR.** **Prescribed repair:** Delete
   `lem-stage1-polar-coherence-naturality` from the repaired 13e `deps:` line
   and from its external-registration list, and state synchronization solely
   by the identical explicit map/domain/image and uniqueness of its inverse.

VERDICT: REJECT (the repaired 13e itself is plausible, but the claimed no-elliptical-identification consumer closure and untouched A_7/T0 path are false)
