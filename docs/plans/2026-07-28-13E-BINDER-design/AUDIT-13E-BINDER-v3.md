# Hostile audit of `DESIGN-13E-BINDER-v3.md`

1. **Location:** design §1.3, line 76; elevation row 3, line 430.
   **Defect:** the NEW contract
   `lem-stage1-explicit-smooth-unitary-operations` is not binder-closed.  Its
   antecedent says “the same graph charts make `calU` a smooth embedded
   manifold,” but no graph family, atlas, or smooth structure has previously
   been quantified or displayed in the contract.  Consequently “the same
   graph charts,” “the embedded manifold,” and the final comparison “change no
   point or first derivative” have no contract-local referent.  The `deps:`
   line does not repair an unbound anaphor: `lem-stage1-smooth-unitary-atlas`
   is an external theorem, not a syntactic binder in this new root.  This is
   the same class of interface failure for which the two parents are being
   retired.  The scalar/product/adjoint calculation described at lines 83–91
   is sound once a smooth structure is fixed, but it does not bind that
   structure.  **Severity: MAJOR.**  **Prescribed repair:** change the NEW
   contract before any landing or seeding so that it explicitly quantifies a
   graph atlas/smooth embedded-manifold structure (or explicitly displays the
   graph family and identifies it with the atlas external), states that the
   displayed `Pi_delta` and its displayed inverse are smooth relative to that
   structure, and states that the resulting `mu` and `sigma` preserve the
   already displayed C1 maps and derivatives.  Recompute the exact external
   list after that binding repair and submit the changed contract to a fresh
   audit.  By the design's own stop rule at lines 507–510, this contract change
   is a return-to-design event, not a local proof repair.

2. **Location:** design §§1.4–1.5, lines 103–110 and 126–132; actual report
   anchors `report/sections/47_stage1_group_laws.tex:122–216` and
   `report/sections/49_stage1_smooth_upgrades.tex:77–105,226–255`.
   **Defect:** “only the explanatory campaign sentence” is not a consistent
   retirement update.  Both anchors still contain a paragraph literally
   headed “Proof (prose account of the af-validated tree)” after the
   retracted conjecture.  The section-47 account repeats the invalid witness
   synchronization at lines 156–165, and section 49 repeats the invalid
   attachment through the anaphoric parent at lines 104–145.  Their
   role-in-chain prose also continues to advertise those retired interfaces
   as dependencies.  The surrounding report metadata is false as well:
   `report/README.md:80–93` calls the parents and six transports validated;
   `report/UNWIRED.md:254–262` repeats those obsolete validation claims; and
   `report/PROVENANCE.md:232,237,241,243–244` records obsolete status/export
   facts.  The parent IDs should remain absent from `UNWIRED` because they are
   anchored; that part of the retirement decision is correct.  **Severity:
   MAJOR.**  **Prescribed repair:** retain each byte-verbatim conjecture and a
   short retraction/retirement/supersession note, but remove the invalid
   material from any paragraph represented as a proof (or move it to a
   plainly labelled historical failed-attempt record outside the paper
   proof track).  Rewrite the role-in-chain prose, README comments, UNWIRED
   comments, source rows/hashes, and claim rows so that the two parents are
   consistently `stated`/`seeded`, retired, anchored, and unsupported by
   their retained historical exports.  Update the parent shard status prose
   too: both actual shard bodies still call their workspaces “the
   re-elevation base,” contrary to permanent retirement.

3. **Location:** design §1.12, lines 401–418, and cost row at line 500; actual
   `scripts/check-provenance.py:349–364` and `argument/README.md:18–35`.
   **Defect:** the landing package is not gate-complete.  The three NEW
   registry IDs have neither report anchors nor prescribed entries in
   `report/UNWIRED.md`; adding any one as proposed would therefore trigger the
   provenance gate's hard “NO report label and NOT in UNWIRED” error.  The
   “exact registry package” also omits required new-shard fields (`id`,
   `kind`, `provenance`, `owner`, and the workspace field after seeding).
   Re-seeding or changing the dependencies of already anchored rows also
   changes registry/export hashes and requires corresponding report
   provenance and narrative updates, none of which is included in the
   landing actions.  Finally, if retirement prose is corrected as required
   above, the two retired registry shards are touched, so “11 registry shards
   touched” is false; the minimum is 13 before counting generated artifacts.
   **Severity: MAJOR.**  **Prescribed repair:** give complete front matter for
   all three NEW shards; place each in `UNWIRED` at its initial unanchored
   landing or add a proper report anchor; prescribe the later paper-track,
   provenance-hash, INDEX/DAG, README/catalog, and status-ledger updates for
   every elevation/reseed; include the two retired shard-body corrections;
   and correct the shard accounting.  Require `check-all.sh` after each
   atomic landing stage.

4. **Location:** design §1.8, lines 203–228, and §4, lines 492–499; actual
   `AGENTS.md:268–288` and `scripts/af-orchestrate.py:4–22`.
   **Defect:** the proposed `af` state transition is semantically valid, but
   the verifier allocation is not.  I exercised the exact sequence on a
   disposable copy with `af` 0.1.6: verifier `unvalidate` changes a validated
   node to pending, and orchestrator `archive` is then accepted only for that
   pending node.  Thus verifier revocation followed by orchestrator archival
   is the correct role order.  Nodes 1.3.4–1.3.7 genuinely form a live bypass:
   they derive right-invertibility of each root-family zero, differentiate
   that root family's own zero curves, use intrinsic tangent dimension to
   upgrade inclusion to equality, and then use the external intrinsic
   `omega`; none depends on 1.3.3.  However, lines 211–218 assign all six
   renewed acceptances to “the same fresh hostile verifier.”  The mandatory
   protocol says every node is validated by a brand-new `codex exec`, fresh
   per node.  The cost table then counts eight verifier *cohorts* as eight
   Codex jobs, which is arithmetically false under that protocol.  At the
   stated target sizes, the seven new/reseeded trees require 92 fresh
   node-verifier jobs and the retained 13c repair requires six, so the
   pre-challenge total is at least 107 Codex jobs
   (`1 design + 1 audit + 7 prover builds + 98 node verifiers`), not 17.  At
   the hard caps the analogous minimum is 138.  **Severity: MAJOR.**
   **Prescribed repair:** a single fresh verifier may perform the revocation
   audit, the orchestrator may archive 1.3.3 after revocation, but dispatch a
   distinct fresh verifier identity/`codex exec` for each bottom-up
   acceptance of 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3, and 1, and use the normal
   per-node orchestration for the seven other workspaces.  Distinguish eight
   scheduling cohorts from actual Codex-job counts and replace the cost
   arithmetic.

5. **Location:** design §§1.11–1.12 and §3, especially lines 391–418 and
   474–486; actual prior v6 downstream table
   `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md:34–49,206–211`.
   **Defect:** the claimed complete rows-14+ consumer re-check omits the sixth
   v6 downstream row,
   `lem-finite-polyhedron-maximal-simplex-placement`.  Its actual shard has no
   Stage-1 dependencies and is algebra-independent, so the omission conceals
   no mathematical break, but “complete classification” and row-by-row
   process-law accounting are not complete.  **Severity: MINOR.**
   **Prescribed repair:** add an explicit BYTE-UNCHANGED/no-dependency/no-binder
   row for `lem-finite-polyhedron-maximal-simplex-placement` to the
   classification and consumer re-check; it does not change the touched-shard
   count.

The exhaustive dependency grep found exactly eight shards whose actual
`deps:` lines mention a retired parent: inversion-derivative control and
transport, 13e, smooth operations, uniform isolation, quotient manifold,
quotient left inversion, and quotient inversion-index data.  Applying the
displayed v3 rewires leaves only the intentionally retired
smooth-operations parent depending on the intentionally retired group-laws
parent.  A simulation over all 298 resulting registry nodes found no dangling
dependency and no cycle; because no validated live consumer retains either
retired parent, linker status propagation remains green.

No additional mathematical defect was found in the two explicit
domain/closeness bridges, control, 13e, 13f, or 13g.  In particular, 13f's
path content is supplied without attaching the parent's anaphoric path:
the parent supplies only `L_{Z_t}` invertibility and approximate-unitary
membership, while 13d supplies the receiving tuple's displayed C1 inverse,
inner inclusion, and fixed endpoints; affine continuity and one-inverse
uniqueness give joint continuity, endpoints, and scalar equivariance.  For
13g, the fixed `G_c,C_g` construction produces universal
`D_0,k_D,C_der^0,kappa_der^0` before the receiving tuple, and the listed
externals suffice for the contract's global C1 `sigma`: polar retraction
gives a C1 `u_delta`, the explicit domain bridge types every adjoint input,
and dagger is real-linear.  Neither the smooth bridge nor smooth polar
inverse is needed for C1 regularity.  The row-13 `(A_5)`–`(A_7)` strings and
all displayed amended contracts are byte-identical to the actual shards;
the fourteen witness fields are unchanged; the strict-radius arguments
remain valid at `epsilon_r = 0`; and the local scalar-action route for the
quotient-manifold package is sufficient.  The current full repository gate
also passes, but it does not cure the proposed landing omissions above.

VERDICT: REJECT (the NEW smooth bridge is not binder-closed, and the landing, report, verifier, and cost plan violates mandatory process gates)
