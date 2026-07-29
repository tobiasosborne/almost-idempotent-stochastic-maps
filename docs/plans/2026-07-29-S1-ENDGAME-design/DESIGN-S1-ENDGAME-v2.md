# DESIGN-S1-ENDGAME-v2 — repaired Stage-1 endgame

Date: 2026-07-29
Role: fresh independent design mathematician
Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND, SEED, OR PROMOTE before a fresh hostile audit and user ratification**

## 0. Executive disposition

This is a self-contained replacement for `DESIGN-S1-ENDGAME.md`. It retains
every v1 component not attacked by `AUDIT-S1-ENDGAME.md` and repairs every
REDESIGN finding.

- **R-A1:** take option (a) from the repair brief. A1 no longer imports
  `lem-topology-hopf-structure` or says “bialgebra.” It constructs exactly
  Hatcher's weak coproduct package from Kunneth and the H-space unit homotopies,
  then invokes the already-local Hatcher theorem directly. Coassociativity is
  neither assumed nor claimed.
- **R-B1:** the actual root contracts do not export a common witness. The exact
  phrases are: row 13 (A_5) says “writing `(u_delta, h_delta)` for the unique
  inverse of `Pi_delta: ...`”; quotient-left-inversion only says “the
  scalar-equivariant `mu, sigma` ... descend”; quotient-manifold-package binds
  only the canonical space; quotient-index-data says “the smooth
  `breve-sigma`” and gives a representative phase lift, but does not bind its
  `W` to the left-inversion root. Therefore two small synchronization helpers
  re-derive the relevant conclusions for one displayed row-13 tuple and carry
  that exact package into B1. The audited ten B1 dependencies remain in their
  original order; one earlier typed-provider dependency is appended because
  the ten opaque roots alone cannot prove witness identity.
- **R-C1:** B1 now exports an actual fixed lift, its row-13 inversion, its
  near-Hermitian estimate, and its isolation distances in one package. A new
  fixed-unitary-to-projection bridge consumes those exact witnesses; the
  original C1 id becomes a seven-node rectification/transport wrapper.
- **R-C3:** line `approximate_algebras.tex:458` is added to the universality
  provenance.
- **R-M04:** this design removes only the G-S1 blocker. MAIN still requires its
  P0 definition gate and M01--M18, including the currently absent M04, before
  M19-S1 or any later MAIN row is eligible.

The repair adds **three proposed helper rows**, no definition shard, no
reference acquisition, and no amendment to any T0 contract or existing
workspace external. All proposed direct dependencies are T0 or earlier in the
serial order below.

## 1. Registry-ready row tables

Every `contract:` value below is one physical source line, flattened registry
ASCII, and gives no numerical value to an existential universal constant.

### Block A — trace rows

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | target / rounds / hard cap | feasibility |
|---|---|---|---|---|---|---|
| `lem-stage1-exterior-cohomology` | Exterior cohomology of a finite H-space: if M is a connected CW complex with dim_R H^*(M;R) < infinity and (M,mu,e) is an H-space, then A=H^*(M;R) is a finite-dimensional connected graded-commutative associative algebra and, for Delta=(cross product)^(-1) o mu^*, Delta:A->A tensor_R A is a degree-preserving algebra homomorphism satisfying Delta(1)=1 tensor 1 and Delta(a)=a tensor 1+1 tensor a+sum_j a'_j tensor a''_j with a'_j,a''_j in A^+ for every homogeneous a in A^+; consequently A is an exterior algebra on finitely many odd-degree homogeneous generators. | `def-h-space-left-inversion` | `lem-topology-kunneth-cross-product` | `refs/hatcher-algebraic-topology/AT.txt:17654-17677,17798-17800`; construction guide `refs/kitaev-2405.02434/approximate_algebras.tex:975-1016` | 8 / 3 / 12 | **SUPPORTED-WITH-DIRECT-LOCAL-EXTERNALS.** This is the precise non-coassociative package Hatcher calls a Hopf algebra; the inapplicable standard-bialgebra T0 contract is not used. |
| `lem-stage1-left-inversion-associated-graded` | Associated-graded action of a left inversion: if M is a connected CW complex with dim_R H^*(M;R) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, set A=H^*(M;R), A^+=direct_sum_{k>0} A^k, F^{p,q}=(A^+)^p intersect A^{p+q}, and E^{p,q}=F^{p,q}/F^{p+1,q-1}; then sigma^* preserves every F^{p,q} and induces (-1)^(p+q)*id on every E^{p,q} for p >= 0 and p+q >= 0. | `def-h-space-left-inversion` | `lem-stage1-exterior-cohomology` | `refs/kitaev-2405.02434/approximate_algebras.tex:1016-1049` | 9 / 3 / 14 | **SUPPORTED-WITH-DERIVATION.** Unchanged from v1. |
| `lem-stage1-left-inversion-trace` | Left-inversion trace: if M is a connected CW complex with dim_R H^*(M;R) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, then Tr(sigma^{*k}:H^k(M;R)->H^k(M;R))=(-1)^k*dim_R H^k(M;R) for every k >= 0. | `def-h-space-left-inversion` | `lem-stage1-left-inversion-associated-graded` | `refs/kitaev-2405.02434/approximate_algebras.tex:971-972,1023-1050` | 4 / 2 / 8 | **SUPPORTED-WITH-DERIVATION.** Unchanged from v1. |

#### A1 source decision

The exact T0 contract at
`argument/lemmas/lem-topology-hopf-structure.md:4` assumes a
“finite-dimensional connected graded-commutative bialgebra.” The source note
in that same shard says Hatcher's theorem needs less
(`argument/lemmas/lem-topology-hopf-structure.md:20-33`), but an af consumer
may import only the root contract, not that explanatory body. Hatcher's actual
conditions are the two displayed clauses at `AT.txt:17654-17677`; his Theorem
3C.4 is at `AT.txt:17798-17800`. These are already under `refs/`.

A1 will therefore register two byte-matched workspace externals:

1. `GT-hatcher-weak-hopf-conditions` at `AT.txt:17654-17677`;
2. `GT-hatcher-hopf-structure-3C4` at `AT.txt:17798-17800`.

This is repair option (a): A1 derives the weaker structure it needs from
Kunneth and the H-space axioms in its own nodes. It does not add a
`lem-topology-*` row and does not acquire a source.

### Block B — synchronized quotient data and corrected extra fixed class

The two helpers are forced by the typed-witness law. They factor the
same-object reconstruction below the approximately twelve-node threshold;
combining them with the fixed-point contradiction would recreate the
audit-rejected, implausibly dense B1.

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | target / rounds / hard cap | feasibility |
|---|---|---|---|---|---|---|
| **NEW** `lem-stage1-bound-quotient-left-inversion` | Bound quotient H-space package: there is a universal e_bind^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_bind^r and 1 < N=dim_C calX < infinity, writing W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) for one tuple supplied by lem-stage1-polar-constant-ledger, writing (u_delta,h_delta) for the unique inverse of Pi_delta:calU x B_delta^{calH}(J)->S_delta:=Pi_delta(calU x B_delta^{calH}(J)), Pi_delta(U,H)=U bold-dot H, at delta=delta_*, defining mu(U,V)=u_delta(U bold-dot V), sigma(U)=u_delta(U^dagger), breve-calU=calU_e/U(1), breve-mu([U],[V])=[mu(U,V)], and breve-sigma([U])=[sigma(U)], these same displayed maps make (breve-calU,breve-mu,[J]) a connected H-space and make the smooth breve-sigma a left inversion; moreover sigma(cU)=conj(c)*sigma(U) and ||sigma(U)-U^dagger|| <= C_grp*epsilon_r for every c in U(1) and U in calU. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion` | `lem-stage1-polar-constant-ledger`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse`; `lem-stage1-explicit-smooth-unitary-operations`; `lem-stage1-quotient-manifold-package`; `lem-topology-quotient-manifold` | row 13 clauses (A_2),(A_4)-(A_6),(R) at `argument/lemmas/lem-stage1-polar-constant-ledger.md:4`; quotient structure `argument/lemmas/lem-topology-quotient-manifold.md:4`; `refs/kitaev-2405.02434/approximate_algebras.tex:895-912,945-955` | 8 / 3 / 12 | **SUPPORTED-WITH-RECONSTRUCTION.** It repeats the validated quotient-left-inversion mechanism for one contract-visible tuple instead of identifying an opaque root map. |
| **NEW** `lem-stage1-bound-quotient-index-data` | Bound quotient index package: there are universal e_bidx^r > 0 and r_bidx > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_bidx^r and 1 < N=dim_C calX < infinity, writing (W,(u_delta,h_delta),mu,sigma,breve-calU,breve-mu,breve-sigma) for the exact displayed witnesses supplied by lem-stage1-bound-quotient-left-inversion with no reselection, the same breve-calU is a connected compact orientable smooth manifold without boundary of real dimension N-1 and a finite polyhedron, breve-sigma is its smooth left inversion, breve-e=[J] is an isolated fixed point of local index +1, J and -J are the only sigma-fixed points in their ambient r_bidx-balls, and every breve-sigma-fixed class [U_0] has representatives U_0 and phases c,a in U(1) with sigma(U_0)=c*U_0, a^2=c, and sigma(a*U_0)=a*U_0, sigma(-a*U_0)=-a*U_0. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-bound-quotient-left-inversion`; `lem-stage1-polar-constant-ledger`; `lem-stage1-quotient-finite-cw`; `lem-stage1-quantitative-inverse-function`; `lem-topology-local-index-sign` | row 13 clause (A_7),(R) at `argument/lemmas/lem-stage1-polar-constant-ledger.md:4`; phase lift `refs/kitaev-2405.02434/approximate_algebras.tex:939-955`; index argument `:947-968` | 9 / 3 / 14 | **SUPPORTED-WITH-RECONSTRUCTION.** The receiving package is fixed before its threshold is decreased; no inversion is chosen in this row. |
| `lem-stage1-extra-fixed-class` | Bound extra fixed class: there are universal C_fix < infinity and e_fix^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_fix^r and 1 < N=dim_C calX < infinity, writing (W,(u_delta,h_delta),mu,sigma,breve-calU,breve-mu,breve-sigma) for the exact displayed witnesses supplied by lem-stage1-bound-quotient-index-data with no reselection, there exist a breve-sigma-fixed class breve-U != breve-e=[J], a representative U_0 in calU_e, and c,a in U(1) such that sigma(U_0)=c*U_0, a^2=c, U=a*U_0, [U]=breve-U, sigma(U)=U, ||U-U^dagger|| <= C_fix*epsilon_r, ||U-J|| >= r_bidx, and ||U+J|| >= r_bidx. | `def-epsilon-cstar-algebra`; `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-finite-cw`; `lem-stage1-quotient-left-inversion`; `lem-stage1-left-inversion-trace`; `lem-topology-lefschetz-hopf`; `lem-topology-local-index-sign`; `lem-topology-orientable-top-cohomology`; `lem-stage1-quotient-inversion-index-data`; `lem-finite-polyhedron-maximal-simplex-placement`; `lem-stage1-bound-quotient-index-data` | `refs/kitaev-2405.02434/approximate_algebras.tex:945-969`; trace input `:971-1050`; original ten-item ledger `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md:234-263` | 10 / 3 / 15 | **SUPPORTED-WITH-TYPED-PROVIDER.** The original ten deps are byte-order-preserved; the eleventh is the minimal forced provider. |

The appended B1 dependency is not optional bookkeeping. The audit proved that
the ten root contracts imply properties of same-named but independently hidden
maps. Appending the synchronization row is the smallest change compatible with
both the fixed obligation ledger and the repository's typed-witness law. No
existing T0 row is amended or reinterpreted.

### Block C — projection bridge and the three G-S1 producers

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | target / rounds / hard cap | feasibility |
|---|---|---|---|---|---|---|
| **NEW** `lem-stage1-fixed-unitary-projection-bridge` | Fixed-unitary projection bridge: there are universal C_bridge < infinity and e_bridge^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_bridge^r and 1 < dim_C calX < infinity, writing (W,(u_delta,h_delta),mu,sigma,breve-calU,breve-mu,breve-sigma,breve-U,U_0,c,a,U) for the exact witnesses supplied by lem-stage1-extra-fixed-class with no reselection, the element P=(2J+U+U^dagger)/4 is a nontrivial C_bridge*epsilon_r-projection for the displayed exact-unit product bold-dot. | `def-epsilon-cstar-algebra`; `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-delta-projection` | `lem-stage1-extra-fixed-class` | `refs/kitaev-2405.02434/approximate_algebras.tex:929-943` | 8 / 3 / 12 | **SUPPORTED-WITH-DERIVATION.** This is the factored phase-lift/near-Hermitian-to-projection algebra; its contract cannot select another inversion. |
| `lem-stage1-rectified-nontrivial-projection` | There are universal C_proj < infinity and e_proj > 0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0 <= epsilon_X <= e_proj and 1 < dim_C calX < infinity contains a nontrivial C_proj*epsilon_X-projection P_0 for the original product and original unit I_X. | `def-extended-epsilon-cstar-algebra`; `def-epsilon-cstar-algebra`; `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-delta-projection` | `lem-stage1-polar-constant-ledger`; `lem-stage1-extra-fixed-class`; `lem-stage1-fixed-unitary-projection-bridge` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-945`; rectification interface `argument/lemmas/lem-stage1-polar-constant-ledger.md:4` (A_1) | 7 / 3 / 12 | **SUPPORTED-WITH-DERIVATION.** Contract unchanged from v1; now only a one-rectification wrapper and original-product transport. |
| `lem-stage1-original-complementary-pair` | There are universal C_np < infinity and e_np > 0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0 <= epsilon_X <= e_np and 1 < dim_C calX < infinity contains nonvanishing C_np*epsilon_X-projections P' and P'' for the original product such that P'+P''=I_X and ||P'P''||,||P''P'|| <= C_np*epsilon_X. | `def-extended-epsilon-cstar-algebra`; `def-delta-projection` | `lem-stage1-rectified-nontrivial-projection` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-929,1419-1424` | 6 / 2 / 10 | **SUPPORTED-WITH-DERIVATION.** Unchanged from v1. |
| `lem-stage1-fresh-two-point-inclusion` | There are universal C_pair < infinity and e_pair > 0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0 <= epsilon_X <= e_pair and 1 < dim_C calX < infinity contains nonvanishing C_pair*epsilon_X-projections P',P'' with P'+P''=I_X for which the linear map v^(2):C^2->calX, v^(2)(lambda,mu)=lambda*P'+mu*P'', is an extended C_pair*epsilon_X-inclusion, satisfies v^(2)(1,1)=I_X, and sends the standard projection basis Pi',Pi'' to P',P''. | `def-extended-epsilon-cstar-algebra`; `def-delta-projection`; `def-extended-delta-inclusion`; `def-operator-space`; `def-projection-basis` | `lem-stage1-original-complementary-pair` | `refs/kitaev-2405.02434/approximate_algebras.tex:458,1192-1222,1419-1424`; direct external statement `:1194-1196`, proof `:1198-1222` | 9 / 3 / 14 | **SUPPORTED-WITH-DERIVATION AND ONE LOCAL CITED EXTERNAL.** C3 is unchanged except for the audit-required line-458 provenance. |

## 2. Serial landing and elevation order

The requested seven rows retain their v1 relative order. The three forced
helpers are inserted immediately before their consumers:

1. `lem-stage1-exterior-cohomology`;
2. `lem-stage1-left-inversion-associated-graded`;
3. `lem-stage1-left-inversion-trace`;
4. `lem-stage1-bound-quotient-left-inversion` **(new helper)**;
5. `lem-stage1-bound-quotient-index-data` **(new helper)**;
6. `lem-stage1-extra-fixed-class`;
7. `lem-stage1-fixed-unitary-projection-bridge` **(new helper)**;
8. `lem-stage1-rectified-nontrivial-projection`;
9. `lem-stage1-original-complementary-pair`;
10. `lem-stage1-fresh-two-point-inclusion`.

Each row is landed only after hostile audit and user ratification, then elevated
only after every direct dependency is T0/cited or an earlier validated row.
Use one fresh prover and a separate fresh hostile verifier per row.

After row 10, the **G-S1 gate alone** is discharged: the three ids named at
`DESIGN-MAIN-STRUCTURE-v5.md:355-369` exist and have the producer shapes
needed by M19-S1. This does **not** make M19-S1--M28 currently eligible. The
MAIN campaign must first clear P0 and land/validate M01--M18 in the serial order
at `DESIGN-MAIN-STRUCTURE-v5.md:512-538`, including M04
`lem-maincb-direct-corner-envelope`.

## 3. Per-row af proof skeletons

Each numbered item is one intended af node, including assembly. Routine
fixed-term estimates stay in their assigned node; a challenge repairs that node
instead of spawning an unpriced subtree.

### A1. `lem-stage1-exterior-cohomology` — 8 nodes

1. Fix `M,mu,e`; set `A=H^*(M;R)` and `A^+=direct_sum_{k>0}A^k`; record connectedness, graded commutativity, associativity, and finite total dimension.
2. Apply `lem-topology-kunneth-cross-product` to `M x M` and define `Delta=(cross product)^(-1) o mu^*`.
3. Use naturality of cup and the ring form of Kunneth to prove that `Delta` is a degree-preserving algebra homomorphism.
4. Use the two H-unit homotopies to identify the two edge components of `Delta(a)` as `a tensor 1` and `1 tensor a`.
5. Split by positive degree to prove the displayed positive-positive remainder formula, exactly matching `GT-hatcher-weak-hopf-conditions`.
6. Apply `GT-hatcher-hopf-structure-3C4`; no coassociativity, counit, antipode, or homotopy associativity is introduced.
7. Total finite dimensionality excludes every nontrivial polynomial factor, leaving only odd exterior generators.
8. Assemble the precise weak-coproduct and exterior-algebra conclusions.

### A2. `lem-stage1-left-inversion-associated-graded` — 9 nodes

1. Fix the H-space and left inversion; import A1 and fix one odd exterior-generator system.
2. Degree and multiplicativity of `sigma^*` preserve `A^+`, every `(A^+)^p`, and every `F^{p,q}`.
3. Translate the first, basepoint-preserving `homo_inverse` homotopy into `cup o (sigma^* tensor id) o Delta = unit o augmentation`.
4. Insert A1's positive-positive coproduct formula.
5. For every exterior generator `x`, derive `sigma^*(x)=-x mod (A^+)^2`.
6. By multiplicativity obtain `(-1)^p` modulo `(A^+)^{p+1}` on each length-`p` exterior monomial.
7. Odd generator degrees make monomial length congruent to total degree modulo two.
8. Those monomials give a basis of each `E^{p,q}`.
9. Assemble preservation and action `(-1)^(p+q)*id`.

### A3. `lem-stage1-left-inversion-trace` — 4 nodes

1. For fixed `k`, record the finite exhaustive filtration of `A^k`.
2. Apply finite-dimensional trace additivity to its associated graded.
3. Apply A2 and sum the quotient dimensions.
4. Assemble the trace identity for all `k`.

### B0a. `lem-stage1-bound-quotient-left-inversion` — 8 nodes

1. Fix the single universal row-13 tuple `W`, decrease one receiving threshold, and set `delta=delta_*`.
2. Invoke (A_4) with the literal binder “writing `(u_delta,h_delta)` for the unique inverse of `Pi_delta`”; no other polar inverse is introduced.
3. Use (A_2), the smooth-atlas row, and the smooth-polar-inverse row to provide the typed antecedents of `lem-stage1-explicit-smooth-unitary-operations` for that same inverse.
4. Obtain smooth `mu,sigma`, their exact formulas, scalar covariance, and the (A_5) near-adjoint estimate for those maps.
5. Restrict the maps to `calU_e` and define `breve-mu,breve-sigma` by the displayed orbit formulas; prove representative independence.
6. Use the canonical quotient-manifold package only for the underlying quotient's smooth structure; check smoothness of the displayed descended maps through local quotient sections.
7. Use (A_5)--(A_6) to prove the H-unit laws, connectedness, and the basepoint-preserving left-inversion homotopy for this same `breve-sigma`.
8. Assemble the bound package and threshold.

### B0b. `lem-stage1-bound-quotient-index-data` — 9 nodes

1. Receive the complete B0a package first, keep its `W,u_delta,sigma,breve-sigma`, and only then decrease the threshold.
2. Attach compactness, orientability, dimension `N-1`, no boundary, and finite-polyhedron structure to the same canonical `breve-calU`; no map is selected here.
3. Apply row-13 (A_7) for the received `W`; use scalar covariance to identify the vertical line and induce the derivative of the received `breve-sigma`.
4. Prove the quotient-norm bound and positive determinant by the fixed Neumann homotopy.
5. Apply `lem-topology-local-index-sign` to obtain local index `+1` for the received map.
6. Apply the quantitative inverse-function row to the `+J` chart from the same (A_7) data and obtain `J`-ball isolation.
7. Apply the sign-symmetric argument to the `-J` chart and obtain `-J`-ball isolation.
8. For any fixed quotient class, use the received covariance to perform the square-root phase lift; near `[J]`, label the roots into the two isolation balls and deduce quotient isolation.
9. Assemble the package with one finite minimum and `r_bidx`.

### B1. `lem-stage1-extra-fixed-class` — 10 nodes

1. Receive B0b's exact displayed package; take the finite minimum with the original ten dependency thresholds without replacing any map.
2. Assume for contradiction that `breve-e=[J]` is the only fixed class of the received `breve-sigma`.
3. The fixed set is the singleton `{breve-e}`; use the finite-polyhedron placement row to put it in a maximal simplex.
4. Apply Lefschetz-Hopf and the received local index to obtain `Lambda(breve-sigma)=1`.
5. Apply A3 to this same received left inversion, obtaining `Tr(breve-sigma^{*k})=(-1)^k dim H^k`.
6. Substitute the traces into the definition of the Lefschetz number to obtain the sum of Betti numbers.
7. Connectedness gives nonzero degree-zero cohomology; orientable top cohomology and `N-1>0` give a second nonzero degree, so the sum is at least two.
8. Contradict node 4 and choose a fixed class `breve-U != [J]`.
9. Apply B0b's phase clause to the same map, choosing `U_0,c,a,U`; fixedness plus B0a's (A_5) estimate gives `||U-U^dagger||<=C_fix*epsilon_r`.
10. Since `[U]!=[J]`, the actual fixed lift is neither `J` nor `-J`; B0b's two isolation clauses give both distance bounds, and the full package is assembled.

### C0. `lem-stage1-fixed-unitary-projection-bridge` — 8 nodes

1. Receive B1's complete witness package, including its exact `sigma` and actual fixed lift `U`; do not choose another inversion or phase.
2. Use `sigma(U)=U` and the package's (A_5) estimate to retain the displayed near-Hermitian bound.
3. Define `P=(2J+U+U^dagger)/4` and prove `P^dagger=P`.
4. Expand `P bold-dot P-P` using a fixed number of terms, the exact unitary equation for `U`, the exact unit, and the epsilon-C* axioms.
5. Bound the expansion by a universal multiple of `epsilon_r`.
6. If `P` is in the vanishing alternative, the formula and near-Hermitian estimate place `U` inside the `-J` isolation ball.
7. If `J-P` is in the vanishing alternative, the same fixed-term argument places `U` inside the `J` isolation ball.
8. B1's distance bounds exclude both branches; enlarge one coefficient, decrease one threshold, and assemble nontriviality.

### C1. `lem-stage1-rectified-nontrivial-projection` — 7 nodes

1. Fix one row-13 tuple and its single (A_1) rectification `(J,bold-dot)` of the base algebra underlying the extended input.
2. Record `epsilon_r=C_rect*epsilon_X`, exact-unit axioms, product closeness, and unit closeness; choose the receiving threshold monotonically.
3. Apply B1 to this fixed rectified algebra and retain its entire same-map witness package.
4. Apply C0 to that exact package, obtaining one nontrivial rectified-product projection `P`.
5. Transport the fixed-term projection defect from `bold-dot` to the original product.
6. Replace `J-P` by `I_X-P` using unit closeness and show that both original-product alternatives remain nonvanishing after threshold decrease.
7. Enlarge one universal coefficient, take one finite minimum, and assemble the original-product/original-unit conclusion.

### C2. `lem-stage1-original-complementary-pair` — 6 nodes

1. Fix C1's witnesses and one projection `P_0` before choosing receiving constants.
2. Set `P'=P_0`, `P''=I_X-P_0`; record `P'+P''=I_X`.
3. Retain Hermiticity and nonvanishing for both.
4. Expand the projection defect of `P''`, including approximate-unit errors.
5. Expand `P'P''` and `P''P'` by fixed-term estimates.
6. Enlarge/decrease once and assemble.

### C3. `lem-stage1-fresh-two-point-inclusion` — 9 nodes

1. Fix the exact C2 pair before choosing any receiving coefficient.
2. Define one level-one `v^(2)` and all amplifications as `id_{M_n} tensor v^(2)`.
3. Verify linearity, dagger, basis-image, and exact unit clauses.
4. Expand the four basis products at every amplification.
5. Use the operator-space simple-tensor identity to transport nonvanishing uniformly.
6. Multiply by the amplified projection associated with a larger source coordinate to obtain one amplification-independent crude lower modulus.
7. Invoke byte-matched `GT-kitaev-prop-delta-hominc` at `:1194-1196` at each level; line `:458` licenses data-independent implicit constants and `:1192` supplies smallness quantifiers.
8. Choose one threshold and coefficient uniformly over all levels.
9. Apply `def-extended-delta-inclusion` and assemble.

## 4. Definition-layer audit

| definition | use | disposition |
|---|---|---|
| `def-h-space-left-inversion` | A1--A3 and the displayed H-space/left-inversion package | Reuse unchanged. |
| `def-lefschetz-fixed-point-data` | B0b/B1 local index and Lefschetz number | Reuse unchanged. |
| `def-epsilon-cstar-algebra` | Exact-unit rectified input in B0a--C1 | Reuse unchanged. |
| `def-extended-epsilon-cstar-algebra` | MAIN-facing inputs of C1--C3 | Reuse unchanged. |
| `def-stage1-polar-witness-data` | The one explicit `W` carried from B0a through C0 | Reuse unchanged. |
| `def-approximate-unitary-space` | `calU`, `calU_e`, quotient, polar notation, and fixed lifts | Reuse unchanged. |
| `def-delta-projection` | Nontrivial/nonvanishing outputs in C0--C3 | Reuse unchanged. |
| `def-extended-delta-inclusion` | Complete C3 conclusion | Reuse unchanged. |
| `def-operator-space` | Canonical amplifications and simple-tensor norm in C3 | Reuse unchanged. |
| `def-projection-basis` | Standard `C^2` basis in C3 | Reuse unchanged. |
| `def-compressed-corner` | M19-S1 interface typing only | Reuse unchanged. |

**Proposed new definitions: none.** Hatcher's weak coproduct package is
spelled out in A1 rather than named; this fixes R-form without creating an
ambiguous project term. Singular cohomology, CW complexes, graded algebras,
associated gradeds, trace, exterior algebras, and `C^2` remain BSc/MSc common
knowledge.

## 5. Dimension-freeness audit

| place | audit |
|---|---|
| A1 | Kunneth is structural over real coefficients. Hatcher's theorem is qualitative; total finite dimensionality removes polynomial generators without producing a quantitative constant. |
| A2--A3 | Filtration length and Betti numbers affect only finite algebraic sums, never a stability coefficient. |
| B0a | One row-13 tuple and one finite minimum supply every threshold. The quotient operations are formula-defined, not chosen by dimension. |
| B0b | QIFT and derivative bounds are in Banach/operator and quotient norms. Determinant positivity is homotopy-sign information; no determinant magnitude or dimension-dependent norm equivalence is used. |
| B1 | The contradiction uses only “at least two” cohomology classes. Triangulation size, Betti sum, and number of simplices enter no bound. |
| C0 | `P=(2J+U+U^dagger)/4` has a fixed number of terms. Both nonvanishing branches use the universal isolation radius already carried by B1. |
| C1 | Rectification and return to the original product use the same involutive normed space and fixed-term product/unit comparisons; no basis expansion occurs. |
| C2 | Complement and cross-defect estimates are fixed algebraic identities. |
| C3 | Four basis products are tensor-level terms, not matrix-entry sums. `approximate_algebras.tex:458` explicitly makes each big-O function independent of additional data; `:1192` supplies universal smallness quantifiers. |
| M19-S1 specialization | Once MAIN's M04 exists, a selected corner has defect `L*epsilon`; multiplying producer constants by universal `L` and taking finite maxima/minima introduces no dimension, amplification, atom-count, or block dependence. |

The two highest-risk dimension checks are B0b's quotient derivative norm and
C3's all-level lower modulus. Their proof nodes forbid coordinate-summed
estimates.

## 6. Exact M19-S1 interface match

The audited consumer contract is, verbatim in substance from
`DESIGN-MAIN-STRUCTURE-v5.md:381`:

> After G-S1, there are universal \(K_1\ge1\) and
> \(e_{{\rm call},1}>0\), with \(K_1e_{{\rm call},1}\le e_1\) and all
> G-S1/old-side prerequisite thresholds absorbed into
> \(e_{{\rm call},1}\), such that, if \(A\) is a finite-dimensional extended
> \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le
> e_{{\rm call},1}\), \(w:\mathbb C^m\to A\) is a supplied extended
> \(c_0^{\rm cb}\varepsilon\)-inclusion (including its unit clause), and some
> \(P_j=w(e_j)\) has \(\dim S_{P_j}>1\), then the three G-S1 producers and
> the literal old-side compression furnish an explicit Stage-1 raw-call
> datum satisfying M15 with base scale \(t_1=K_1\varepsilon\).

M15 is the contract at `DESIGN-MAIN-STRUCTURE-v5.md:343`.

| M19-S1 / M15 clause | producer-side discharge |
|---|---|
| Selected corner is a finite-dimensional extended algebra | **Not discharged by G-S1.** Future M04, after P0/M01--M03, must make `S_{P_j}` an extended `L*epsilon`-C*-algebra with unit `u_{P_j}`. C1 deliberately accepts precisely that generic extended ambient. |
| `dim S_{P_j}>1` | Specializing `calX=S_{P_j}` gives the strict dimension hypothesis of C1--C3; no `N=1` quotient branch is used. |
| Fresh nontrivial split | C1 returns a nontrivial projection for the original compressed product/unit; C2 sets `P''=u_{P_j}-P'`, proves the exact sum, and controls both cross defects. |
| Fresh `C^2` inclusion | C3 gives `v^(2):C^2->S_{P_j}`, exact images `Pi'->P'`, `Pi''->P''`, and `v^(2)(1,1)=u_{P_j}`. |
| Fixed amplification family | C3 fixes one level-one map, then uses only `id_{M_n} tensor v^(2)`. |
| Outer complementary targets | These remain `P_[1,m-1]` and `P_j`, supplied later by M04/the original inclusion; they are not C2's internal `P',P''`. |
| Literal old side | For `m>1`, T0 `lem-compcb-single-compression-transfer` supplies the old map. It remains a direct M19-S1 dependency, not a G-S1 producer. |
| Every defect at most `t_1` | Future M19-S1 chooses `K_1` above the old-side coefficients and `L*C_proj,L*C_np,L*C_pair`; this is a finite universal maximum. |
| Thresholds and `K_1*e_call,1<=e_1` | Future M19-S1 takes a finite minimum after `L`-rescaling, but only after M04 and all other M01--M18 providers exist. |
| `m=1` | M15 omits the old side; C1--C3 still supply the fresh inclusion. |

Thus the three G-S1 contracts have the right consumer shape clause-by-clause.
The design makes no claim that M04, M19-S1, or any other MAIN row already
exists.

## 7. Reference and provenance disposition

No reference acquisition is required.

A1 requires two workspace externals from the already-local clean Hatcher text:

- `GT-hatcher-weak-hopf-conditions`:
  `refs/hatcher-algebraic-topology/AT.txt:17654-17677`;
- `GT-hatcher-hopf-structure-3C4`:
  `refs/hatcher-algebraic-topology/AT.txt:17798-17800`.

C3 retains the v1 external:

- `GT-kitaev-prop-delta-hominc`:
  `refs/kitaev-2405.02434/approximate_algebras.tex:1194-1196`;
- proof: `:1198-1222`;
- smallness context: `:1192`;
- **data-independent big-O context: `:458`**.

The Kitaev TeX is clean LaTeX, not scan OCR. The cited passages were checked in
newline-counted source space. No Borel, Leray--Hirsch, standard coassociative
bialgebra theorem, or unavailable source is used.

## 8. Binder, dependency, and cascade audit

The following root contracts/exports were checked:

- `lem-stage1-polar-constant-ledger`: (A_5) explicitly binds the unique inverse
  and defines `mu,sigma`; (A_6),(A_7) reuse that binder.
- `lem-stage1-quotient-left-inversion`: its proof export fixes a `W` and defines
  the descents, but its root contract does not expose `W`, `u_delta`, or the
  formulas.
- `lem-stage1-quotient-manifold-package`: its root exports the canonical
  quotient space and manifold properties, not an inversion.
- `lem-stage1-quotient-inversion-index-data`: its proof export again fixes a
  `W`, but its root does not identify that `W` with the one hidden by the
  left-inversion root.
- `lem-stage1-uniform-inversion-isolation`: likewise hides the selected
  `sigma` at root.

Consequently B0a starts from row 13 rather than attempting cross-root equality;
B0b says “for the exact displayed witnesses supplied by B0a with no
reselection”; B1 and C0 repeat the complete receiving tuple in the same way.
This is the validated 13e binder pattern, not notational unification.

No T0 contract or existing external is amended. The synchronization helpers
re-derive only the same-object conclusions needed here from T0 typed
primitives. The original ten B1 rows remain dependencies and obligation
cross-checks; B0b is the additional contract-level equality provider.

The rectification is also single-construction: C1 fixes one (A_1) product/unit,
applies B1 and C0 inside that exact algebra, and returns the resulting element
to the original product. There is no comparison of two rectifications.

## 9. Budget delta and build granularity

| row | v1 target | v2 target | reason |
|---|---:|---:|---|
| A1 | 7 | 8 | Standard-bialgebra shortcut removed; weak-coproduct matching and finite-dimensional corollary are separate nodes. |
| A2 | 9 | 9 | Unchanged. |
| A3 | 4 | 4 | Unchanged. |
| B0a | — | 8 | New explicit map/descent/H-space binder. |
| B0b | — | 9 | New same-map derivative, isolation, index, and phase package. |
| B1 | 9 | 10 | Carries the fixed class through the synchronized phase lift and exports the actual near-Hermitian lift. |
| C0 | — | 8 | New fixed-unitary projection bridge. |
| C1 | 11 | 7 | Rectification/transport wrapper only; the former concealed expansion and two nonvanishing branches moved to C0. |
| C2 | 6 | 6 | Unchanged. |
| C3 | 9 | 9 | Proof unchanged; provenance corrected. |

Every row is at or below ten target nodes. Hard caps remain below the repository
cap 26. Each skeleton item is one build node. If B0a, B0b, or C0 reaches its
hard cap, stop and classify the gap; do not merge helpers back into B1/C1 or
raise the cap automatically.

## 10. Honest hostile-verifier risk register

| row | first likely hostile attack | designed response / stop condition |
|---|---|---|
| A1 | Does the external theorem really accept a non-coassociative coproduct? | Match only Hatcher's printed clauses at `17654-17677`; the contract spells them out and never uses “bialgebra.” Stop if the external is registered with a stronger standard definition. |
| A2 | Does left inversion yield the sign in total degree rather than word length? | Separate the primitive-mod-square step, multiplicativity, and odd-degree parity into distinct nodes. |
| A3 | Is the filtration finite and exhaustive in each degree? | Establish this before trace additivity. |
| B0a | Is `sigma` from the smooth bridge literally the A5 map? | Instantiate the bridge only after fixing the displayed row-13 inverse; its actual T0 contract explicitly returns equal maps. Any second `u_delta` is a blocker. |
| B0b | Are index and isolation being imported for an opaque same-named map? | They are re-derived from the received `W,sigma` using A7 and QIFT. The opaque quotient-index/isolation roots are not identity providers. |
| B1 | Do trace, index, and fixed-set hypotheses concern one map? | The complete tuple is received once from B0b and repeated in B1's contract; no dependency witness is selected in the proof. |
| C0 | Does small `P` or `J-P` really force `U` into the correct isolation ball? | Give one node to each branch with the explicit bridge formula and near-Hermitian estimate. |
| C1 | Is the projection returned for the original corner product and unit? | Fix one rectification, apply B1/C0 there, then give distinct nodes to product transport and complement/unit transport. |
| C2 | Does complementarity survive an approximate unit? | Expand both orders and the complement projection defect explicitly. |
| C3 | Is complete near-isometry inferred from multiplicativity alone, or are big-O constants level-dependent? | Prove a crude modulus at every canonical amplification first, then use the byte-matched proposition with both `:458` and `:1192`. Stop if the external cannot be registered with that context. |

## 11. Ratification surface and honest hand-off

User ratification is required for the three new helper ids and all ten proposed
contracts before registry landing. No definition ratification and no reference
acquisition are requested. A fresh hostile audit must specifically verify:

1. A1's contract against Hatcher's weak conditions and Theorem 3C.4;
2. the literal binder hand-off B0a -> B0b -> B1 -> C0;
3. the two C0 nonvanishing implications;
4. C1's return to the original product/unit;
5. C3's line-458 universality context; and
6. the G-S1-only hand-off wording.

If all ten rows later validate, the result is exactly this: the trace chain,
the bound extra fixed class, and the three G-S1 producers are available. The
MAIN campaign remains separately gated on P0 and M01--M18. No claim about
M19-S1--M28, `lem-thmainext-conditional`, or `op-classical` is promoted by
this design.
