# DESIGN-S1-ENDGAME — the seven-row Stage-1 endgame

Date: 2026-07-29  
Role: fresh independent design mathematician  
Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND, SEED, OR PROMOTE before a fresh hostile audit and user ratification**

## 0. Disposition and source audit

All seven requested rows are design-feasible under the existing T0 interfaces. No
eighth registry row and no new definition shard is needed. Block A closes through
the banked Kunneth and Hopf-structure rows; Block B uses the audited ten-item
dependency list without alteration; Block C accepts an **extended**
epsilon-C*-algebra and performs exactly one internal rectification, returning its
projection to the original product and original unit. The last producer needs one
new byte-matched workspace external for Kitaev's already-local
`prop_delta_hominc`; it does not need a new reference.

The design honors the polar v6 landing verdict and fixed obligation ledger
(`docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v6.md:8-25`,
`docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md:234-263`) and
the MAIN v5 repaired gate
(`docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v5.md:7-20,160-167`,
`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md:355-381`).
It also enforces the explicit-binder lesson: repeated notation across theorem
boundaries is not witness identity
(`docs/LEARNINGS.md:93-125,127-155`). In every parameterized proof below,
the witnesses of an imported existential are fixed first; all receiving
thresholds are then decreased and constants enlarged monotonically.

No workspace or ledger exists under any of the seven proposed ids as of this
design pass, so there is no prior failed ledger to cite. The related validated
exports inspected are listed in section 8.

## 1. Registry-ready row tables

Every proposed contract below is one physical line and uses flattened registry
ASCII. Named constants are existential and universal; no contract assigns a
numerical value to one.

### Block A — trace rows

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | budget | feasibility |
|---|---|---|---|---|---|---|
| `lem-stage1-exterior-cohomology` | Exterior cohomology of a finite H-space: if M is a connected CW complex with dim_R H^*(M;R) < infinity and (M,mu,e) is an H-space, then Delta=(cross product)^{-1} o mu^* makes A=H^*(M;R) a finite-dimensional connected graded-commutative bialgebra over R, and A is an exterior algebra on finitely many odd-degree homogeneous generators. | `def-h-space-left-inversion` | `lem-topology-kunneth-cross-product`; `lem-topology-hopf-structure` | `refs/kitaev-2405.02434/approximate_algebras.tex:975-1016`; existing T0 ground truth: `refs/hatcher-algebraic-topology/AT.txt:13505-13506,17654-17677,17798-17800` | 7 nodes / 3 rounds | **SUPPORTED-WITH-DERIVATION.** The remaining work is the H-space-to-bialgebra interface; the exterior conclusion itself is imported. |
| `lem-stage1-left-inversion-associated-graded` | Associated-graded action of a left inversion: if M is a connected CW complex with dim_R H^*(M;R) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, set A=H^*(M;R), A^+=direct_sum_{k>0} A^k, F^{p,q}=(A^+)^p intersect A^{p+q}, and E^{p,q}=F^{p,q}/F^{p+1,q-1}; then sigma^* preserves every F^{p,q} and induces (-1)^(p+q)*id on every E^{p,q} for p >= 0 and p+q >= 0. | `def-h-space-left-inversion` | `lem-stage1-exterior-cohomology` | `refs/kitaev-2405.02434/approximate_algebras.tex:1016-1049` | 9 nodes / 3 rounds | **SUPPORTED-WITH-DERIVATION.** The theorem-local filtration notation is bound in the contract, so no new def is needed. |
| `lem-stage1-left-inversion-trace` | Left-inversion trace: if M is a connected CW complex with dim_R H^*(M;R) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, then Tr(sigma^{*k}:H^k(M;R)->H^k(M;R))=(-1)^k*dim_R H^k(M;R) for every k >= 0. | `def-h-space-left-inversion` | `lem-stage1-left-inversion-associated-graded` | `refs/kitaev-2405.02434/approximate_algebras.tex:971-972,1023-1050` | 4 nodes / 2 rounds | **SUPPORTED-WITH-DERIVATION.** This is trace additivity on the finite filtration exported by the preceding row. |

### Block B — corrected extra fixed class

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | budget | feasibility |
|---|---|---|---|---|---|---|
| `lem-stage1-extra-fixed-class` | There is a universal e_fix^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_fix^r and 1 < N=dim_C calX < infinity, the quotient inversion breve-sigma on breve-calU has a fixed scalar class breve-U distinct from breve-e=[J]. | `def-epsilon-cstar-algebra`; `def-approximate-unitary-space`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-finite-cw`; `lem-stage1-quotient-left-inversion`; `lem-stage1-left-inversion-trace`; `lem-topology-lefschetz-hopf`; `lem-topology-local-index-sign`; `lem-topology-orientable-top-cohomology`; `lem-stage1-quotient-inversion-index-data`; `lem-finite-polyhedron-maximal-simplex-placement` | `refs/kitaev-2405.02434/approximate_algebras.tex:945-969`; trace input at `:971-1050`; exact audited dependency order at `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md:248-263` | 9 nodes / 3 rounds | **SUPPORTED-WITH-DERIVATION AFTER BLOCK A.** The fixed list is retained verbatim; no topology claim is re-proved. |

The Block B dependency order above is deliberately identical to the audited
list. In particular, the quotient-index row remains item 9 and the
maximal-simplex row remains item 10. The square-root phase argument is consumed
inside the quotient-index result's local-isolation clause, not rebuilt in this
row.

### Block C — the three G-S1 producers

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | budget | feasibility |
|---|---|---|---|---|---|---|
| `lem-stage1-rectified-nontrivial-projection` | There are universal C_proj < infinity and e_proj > 0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0 <= epsilon_X <= e_proj and 1 < dim_C calX < infinity contains a nontrivial C_proj*epsilon_X-projection P_0 for the original product and original unit I_X. | `def-extended-epsilon-cstar-algebra`; `def-epsilon-cstar-algebra`; `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-delta-projection` | `lem-stage1-polar-constant-ledger`; `lem-stage1-uniform-inversion-isolation`; `lem-stage1-quotient-left-inversion`; `lem-stage1-quotient-inversion-index-data`; `lem-stage1-extra-fixed-class` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-945`; rectification provenance is already carried by the listed T0 ledger and its T0 ancestry | 11 nodes / 3 rounds | **SUPPORTED-WITH-DERIVATION; INTERFACE-SENSITIVE.** Extended input and original-product output match the corner consumer; the internal proof fixes one ledger witness and exposes no rectified witness to downstream consumers. |
| `lem-stage1-original-complementary-pair` | There are universal C_np < infinity and e_np > 0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0 <= epsilon_X <= e_np and 1 < dim_C calX < infinity contains nonvanishing C_np*epsilon_X-projections P' and P'' for the original product such that P'+P''=I_X and ||P'P''||,||P''P'|| <= C_np*epsilon_X. | `def-extended-epsilon-cstar-algebra`; `def-delta-projection` | `lem-stage1-rectified-nontrivial-projection` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-929,1419-1424` | 6 nodes / 2 rounds | **SUPPORTED-WITH-DERIVATION.** Applied to a corner, the contract gives P''=u_P-P' because that corner's I_X is its compressed unit u_P. |
| `lem-stage1-fresh-two-point-inclusion` | There are universal C_pair < infinity and e_pair > 0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0 <= epsilon_X <= e_pair and 1 < dim_C calX < infinity contains nonvanishing C_pair*epsilon_X-projections P',P'' with P'+P''=I_X for which the linear map v^(2):C^2->calX, v^(2)(lambda,mu)=lambda*P'+mu*P'', is an extended C_pair*epsilon_X-inclusion, satisfies v^(2)(1,1)=I_X, and sends the standard projection basis Pi',Pi'' to P',P''. | `def-extended-epsilon-cstar-algebra`; `def-delta-projection`; `def-extended-delta-inclusion`; `def-operator-space`; `def-projection-basis` | `lem-stage1-original-complementary-pair` | `refs/kitaev-2405.02434/approximate_algebras.tex:1192-1222,1419-1424`; proposed direct workspace external `GT-kitaev-prop-delta-hominc` at `:1194-1196`, with universal-quantifier context at `:1192` and source proof at `:1198-1222` | 9 nodes / 3 rounds | **SUPPORTED-WITH-DERIVATION, WITH ONE LOCAL CITED EXTERNAL.** The external upgrades a uniform crude lower modulus plus small multiplicative defect to complete near-isometry; no dimension-dependent estimate is used. |

The C1 rectification dependency choice is intentional. The exact-unit rows
`lem-stage1-exact-unit-rectification`,
`lem-stage1-rectified-cstar-control`, and
`lem-stage1-rectified-cstar-transport` enter **transitively through**
`lem-stage1-polar-constant-ledger` clause (A_1). They are not imported again
as parallel existential providers. C1 fixes one tuple `W`, then its single
rectification, then all maps and thresholds belonging to that same tuple.

## 2. Serial landing and elevation order

The only permitted seven-row order is:

1. `lem-stage1-exterior-cohomology`;
2. `lem-stage1-left-inversion-associated-graded`;
3. `lem-stage1-left-inversion-trace`;
4. `lem-stage1-extra-fixed-class`;
5. `lem-stage1-rectified-nontrivial-projection`;
6. `lem-stage1-original-complementary-pair`;
7. `lem-stage1-fresh-two-point-inclusion`.

Each row is seeded only after every direct dependency is T0/cited or an earlier
validated row in this list. Each row receives a fresh prover and a separate
fresh hostile verifier. Nothing else is merged into this order.

After row 7 is validated and all three G-S1 ids are landed, hand off to the
already-audited MAIN design: the hard gate before M19-S1 is cleared, and
M19-S1 through M28 become eligible for their prescribed serial campaign. This
does not itself prove, land, or promote any M19-S1--M28 row
(`DESIGN-MAIN-STRUCTURE-v5.md:355-381`).

## 3. Per-row af proof skeletons

Each numbered item below is one af node, including the final assembly node.
The budgets in section 1 count exactly these nodes. A prover should not split
routine linear algebra into descendants; a verifier challenge should amend the
affected node rather than balloon the tree.

### A1. `lem-stage1-exterior-cohomology` — 7 nodes

1. Fix `M,mu,e`; put `A=H^*(M;R)` and record that finite total dimension makes every graded piece finite free over `R`.
2. Apply `lem-topology-kunneth-cross-product` to `M x M` and define `Delta=(cross product)^{-1} o mu^*`.
3. Define the cohomological counit from the basepoint and use the two H-unit homotopies to prove the two counit identities.
4. Use naturality of cup and the ring Kunneth isomorphism to prove that `Delta` is a degree-preserving multiplicative map, giving precisely the connected graded-commutative bialgebra interface consumed by the Hopf T0 row.
5. Record connectedness `A^0=R`, characteristic zero, and finite dimensionality; do not assume homotopy associativity or add coassociativity beyond the imported bialgebra interface.
6. Apply `lem-topology-hopf-structure` to obtain an exterior algebra on finitely many odd-degree homogeneous generators.
7. Assemble the bialgebra and exterior conclusions.

### A2. `lem-stage1-left-inversion-associated-graded` — 9 nodes

1. Fix the H-space and left-inversion witnesses, import A1, and fix one exterior-generator system supplied by its conclusion.
2. Since `sigma^*` preserves degree, the augmentation ideal, and products, prove that it preserves every `F^{p,q}`.
3. Translate the basepoint-preserving left-inversion homotopy into `cup o (sigma^* tensor id) o Delta = unit o counit`.
4. From connectedness and the counit identities, record `Delta(a)=a tensor 1+1 tensor a+(A^+ tensor A^+)` for positive-degree `a`.
5. Apply nodes 3--4 to each exterior generator to obtain `sigma^*(x)=-x mod (A^+)^2`.
6. Use multiplicativity of `sigma^*` to obtain the sign `(-1)^p` modulo `(A^+)^{p+1}` on every length-`p` exterior monomial.
7. Because all generators have odd degree, prove `p` has the same parity as the total degree `p+q`.
8. Show that the length-`p` exterior monomials of total degree `p+q` form a basis of `E^{p,q}`.
9. Assemble preservation and the scalar action `(-1)^(p+q)*id`.

### A3. `lem-stage1-left-inversion-trace` — 4 nodes

1. For fixed `k`, record the finite filtration of `A^k` by the `F^{p,k-p}`.
2. Apply finite-dimensional trace additivity along the filtration to express the trace as the sum of traces on `E^{p,k-p}`.
3. Apply A2: every quotient action is `(-1)^k*id`, and the quotient dimensions sum to `dim_R A^k`.
4. Assemble the claimed trace identity for every `k`.

### B1. `lem-stage1-extra-fixed-class` — 9 nodes

1. Fix the ten dependency witnesses in the audited order and choose `e_fix^r` below their finite set of universal thresholds.
2. For contradiction, assume `breve-e=[J]` is the only fixed class of `breve-sigma`.
3. Use the quotient-manifold, finite-CW, and left-inversion rows to type one connected compact orientable boundaryless finite polyhedron of dimension `d=N-1>0` and its smooth self-map.
4. The singleton fixed set is finite; apply maximal-simplex placement to its sole point.
5. Combine quotient-index data with the local-index-sign row to obtain local index `+1` at `breve-e`; consume, rather than repeat, the quotient-index row's local square-root phase-lift.
6. Apply the maximal-simplex Lefschetz-Hopf row to get `Lambda(breve-sigma)=1`.
7. Apply A3 and the definition of Lefschetz number to get `Lambda(breve-sigma)=sum_k dim_R H^k(breve-calU;R)`.
8. Connectedness gives nonzero `H^0`; orientable top cohomology gives nonzero `H^d`, and `d>0`, so that sum is at least two.
9. Contradict node 6 and produce a fixed class distinct from `[J]`.

### C1. `lem-stage1-rectified-nontrivial-projection` — 11 nodes

1. Fix one witness tuple `W` from `lem-stage1-polar-constant-ledger`; no later node may choose another tuple or rectification.
2. Forget the extra matrix levels only to apply (A_1) to the base algebra, obtaining the single rectified `(J,bold-dot)` algebra with `epsilon_r=C_rect*epsilon_X`; choose the receiving threshold monotonically.
3. Apply B1 to that exact-unit rectified algebra and obtain one fixed quotient class different from `[J]`.
4. Choose a representative `U_0`; quotient fixedness and the globally scalar-equivariant inversion from `lem-stage1-quotient-left-inversion` give `sigma(U_0)=c*U_0`; choose `a` with `a^2=c` and set `U=a*U_0`, so `sigma(U)=U`.
5. Use the square-root convention recorded in `lem-stage1-quotient-inversion-index-data`, but do not enlarge its local-neighborhood conclusion: node 4 is the global algebraic phase-lift, while the index row certifies the convention and the local isolation use. Since `[U]!=[J]`, uniform inversion isolation puts `U` a universal distance from both `J` and `-J`.
6. Ledger clause (A_5) and `sigma(U)=U` give a universal bound on `||U-U^dagger||` at scale `epsilon_r`.
7. Define `P_0=(2J+U+U^dagger)/4` and verify Hermiticity.
8. Expand `P_0 bold-dot P_0-P_0` in a fixed number of terms, using the exact defining unitary equation for `U`, node 6, the exact unit, and the rectified epsilon-C* axioms, to obtain a universal `O(epsilon_r)` bound.
9. If `P_0` or `J-P_0` were in the small alternative of `def-delta-projection`, the formula and node 6 would put `U` in the `-J` or `J` isolation ball; hence both are nonvanishing.
10. Transport the fixed-term defect from `bold-dot` to the original product and replace `J` by `I_X` using ledger (A_1); the original complement `I_X-P_0` remains a nonvanishing `O(epsilon_X)`-projection after a universal threshold decrease.
11. Enlarge one universal coefficient and take one finite minimum of thresholds to assemble `C_proj,e_proj` and the original-product conclusion.

### C2. `lem-stage1-original-complementary-pair` — 6 nodes

1. Fix one witness pair `C_proj,e_proj` and one projection witness `P_0` supplied by C1 before choosing any receiving constants.
2. Set `P'=P_0` and `P''=I_X-P_0`; obtain the exact identity `P'+P''=I_X`.
3. Use C1 and `def-delta-projection` to retain Hermiticity and nonvanishing for both elements.
4. Expand the two projection defects for `P''`, pricing the ambient approximate-unit errors and the defect of `P'`.
5. Expand `P'P''` and `P''P'`; the same unit and projection defects give universal `O(epsilon_X)` bounds.
6. Choose `C_np,e_np` by monotone enlargement/decrease and assemble.

### C3. `lem-stage1-fresh-two-point-inclusion` — 9 nodes

1. Fix one witness pair `C_np,e_np` and one pair `P',P''` supplied by C2.
2. Define the single level-one map `v^(2)(lambda,mu)=lambda*P'+mu*P''` and fix all amplifications as `id_{M_n} tensor v^(2)`; make no level-dependent choices.
3. Verify linearity, exact dagger preservation, the basis-image clauses, and the exact unit clause from `P'+P''=I_X`.
4. Expand the four products at every amplification; the two diagonal projection defects and two cross defects make every amplification a universal `O(epsilon_X)`-homomorphism.
5. Use the operator-space simple-tensor identity to pass nonvanishing of `P',P''` uniformly to `I_n tensor P'` and `I_n tensor P''`.
6. Multiply an arbitrary image by the amplified projection corresponding to its larger source coordinate; node 4 and nonvanishing give one universal positive crude lower modulus at every amplification, with no sum over matrix entries.
7. Register and invoke `GT-kitaev-prop-delta-hominc` (`approximate_algebras.tex:1194-1196`) separately on every amplification: its automatic upper bound and lower-modulus improvement turn nodes 4 and 6 into `(1 plus-or-minus O(epsilon_X))` norm bounds.
8. Choose one universal threshold valid for all amplifications and one coefficient dominating the homomorphism and norm errors.
9. Apply `def-extended-delta-inclusion` and assemble `C_pair,e_pair`.

## 4. Definition-layer audit

| definition | use | disposition |
|---|---|---|
| `def-h-space-left-inversion` | H-space, basepoint, multiplication, left inversion in A1--A3 and B1 | Reuse unchanged. |
| `def-lefschetz-fixed-point-data` | Lefschetz number and local index in B1 | Reuse unchanged. |
| `def-epsilon-cstar-algebra` | Exact-unit rectified algebra in B1 and the base-level algebra used by C1 | Reuse unchanged. |
| `def-extended-epsilon-cstar-algebra` | Actual MAIN-facing ambient of C1--C3 | Reuse unchanged. |
| `def-stage1-polar-witness-data` | The one typed tuple fixing C1's rectification and polar operations | Reuse unchanged. |
| `def-approximate-unitary-space` | `calU`, its scalar quotient, and fixed inversion points in B1/C1 | Reuse unchanged. |
| `def-delta-projection` | Nontrivial/nonvanishing projection outputs in C1--C3 | Reuse unchanged. |
| `def-extended-delta-inclusion` | Complete map conclusion in C3 | Reuse unchanged. |
| `def-operator-space` | Canonical amplifications and simple-tensor norm identity in C3 | Reuse unchanged. |
| `def-projection-basis` | The standard two projections of `C^2` and their images in C3 | Reuse unchanged. |
| `def-compressed-corner` | M19-S1 interface typing for `S_{P_j}` and `u_{P_j}`; not used in a new row contract because C1--C3 are generic in their extended ambient | Reuse unchanged. |

**Proposed new definitions: none.** Singular cohomology, CW complexes,
graded algebras, cup products, exterior algebras, filtrations, associated
gradeds, traces, and the two-point C*-algebra `C^2` are BSc/MSc common
knowledge. The symbols `A^+`, `F^{p,q}`, and `E^{p,q}` are theorem-local and
bound explicitly in A2. The basis `Pi',Pi''` is an instance of the existing
projection-basis definition. Therefore there is no user definition-ratification
item.

## 5. Dimension-freeness audit

| place | audit |
|---|---|
| A1--A3 | These are qualitative finite-dimensional cohomology statements. Kunneth is applied because finite total real cohomology makes each graded piece finite free; no Betti-number sum enters a constant. |
| B1 | `e_fix^r` is a finite minimum of universal T0 thresholds. The dimension occurs only as `d=N-1>0`; neither triangulation size, number of simplices, Betti numbers, nor number of fixed points enters a bound. |
| C1 rectification | `epsilon_r=C_rect*epsilon_X` uses the one universal ledger witness. The new threshold absorbs `e_fix^r/C_rect`, the isolation radius, and the ledger guards. No second rectification comparison and no norm-equivalence constant depending on `dim calX` is introduced. |
| C1 projection estimate | The bridge formula has a fixed number of algebra products. Product, associator, inversion, and transport errors are each controlled by ledger constants; no coordinate expansion or basis cardinality appears. |
| C2 | Complement and cross-product estimates are fixed-term algebra identities. `C_np` depends only on `C_proj` and the ambient epsilon-C* constants. |
| C3 multiplicativity | Exactly four basis products occur, independent of amplification and block data. Matrix coefficients are handled by operator-space norms, not entrywise sums. |
| C3 norm control | The crude modulus uses one of two coordinates and amplified nonvanishing. `GT-kitaev-prop-delta-hominc` has universal implicit constants by its source context at TeX line 1192 and applies uniformly to each matrix level. No minimum over `n` and no factor depending on `n` is taken. |
| M19-S1 scale | On a corner, its ambient defect is at most `L*epsilon`; hence producer constants are multiplied only by the universal `L`. `K_1` is a finite maximum of universal old-side and G-S1 coefficients, and `e_call,1` is a finite minimum of universal thresholds after division by those coefficients. |

The two places a hostile verifier should inspect for hidden dimension leakage
are A1's use of Kunneth and C3's all-level lower modulus. The skeletons above
make both arguments structural rather than basis-summed.

## 6. Exact M19-S1 interface match

The audited consumer contract is:

> After G-S1, there are universal \(K_1\ge1\) and \(e_{{\rm call},1}>0\), with \(K_1e_{{\rm call},1}\le e_1\) and all G-S1/old-side prerequisite thresholds absorbed into \(e_{{\rm call},1}\), such that, if \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le e_{{\rm call},1}\), \(w:\mathbb C^m\to A\) is a supplied extended \(c_0^{\rm cb}\varepsilon\)-inclusion (including its unit clause), and some \(P_j=w(e_j)\) has \(\dim S_{P_j}>1\), then the three G-S1 producers and the literal old-side compression furnish an explicit Stage-1 raw-call datum satisfying M15 with base scale \(t_1=K_1\varepsilon\).

This is quoted from
`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md:381`;
M15's required raw datum is at the same file's line 343.

| M19-S1 / M15 clause | producer-side discharge |
|---|---|
| Finite-dimensional extended ambient | M04/`lem-maincb-direct-corner-envelope`, backed by `lem-compcb-corner-algebra`, makes the selected `S_{P_j}` an extended ambient with defect at most `L*epsilon` and unit `u_{P_j}`. C1 deliberately accepts exactly an extended ambient. |
| Positive-dimensional fresh corner | The consumer hypothesis `dim S_{P_j}>1` is exactly the strict dimension hypothesis of C1--C3 after setting `calX=S_{P_j}`. No `N=1` branch is invoked. |
| Nontrivial fresh split | C1, applied inside that corner, returns an original-compressed-product nontrivial projection. C2 turns it into `P',P''` with `P'+P''=u_{P_j}` and controlled projection/cross defects. |
| Fresh `C^2` inclusion | C3 gives `v^(2):C^2->S_{P_j}`, with `v^(2)(Pi')=P'`, `v^(2)(Pi'')=P''`, and `v^(2)(1,1)=u_{P_j}`. Thus the fresh map includes the target corner's unit clause, not the ambient `I_A` by mistake. |
| Fixed amplification family | C3 fixes one level-one map and defines every level as `id_{M_n} tensor v^(2)`. Its external norm upgrade is applied to those same maps, so there is no level-dependent witness. |
| Outer complementary targets | These are the old target `P_[1,m-1]` and fresh target `P_j` already supplied and bounded by the original extended inclusion plus M04. They must not be confused with C2's internal pair `P',P''` in `S_{P_j}`. |
| Literal old-side map | For `m>1`, `lem-compcb-single-compression-transfer` supplies the old extended inclusion into `S_{P_[1,m-1]}`. This is intentionally outside G-S1 and remains a direct M19-S1 dependency. |
| All projection, complementarity, map, and target-ambient defects at most `t_1` | Choose `K_1` above `1`, `L`, every old-side coefficient, and `L` times `C_proj,C_np,C_pair`; monotonicity then puts every displayed defect below `K_1*epsilon`. |
| All prerequisite thresholds and `K_1*e_call,1<=e_1` | Choose `e_call,1` below the M04, old-side, C1, C2, and C3 thresholds after the necessary universal `L` rescaling, and below `e_1/K_1`. This is a finite minimum of positive universal numbers. |
| `m=1` edge | M15 says the old side is absent. C1--C3 still supply the fresh `C^2` inclusion, so no empty old-corner construction is needed. |

Therefore the proposed producer contracts make M19-S1
**SUPPORTED-WITH-DERIVATION** exactly as its audited verdict anticipates. They
do not silently assert M15's final sum-map theorem themselves.

## 7. Reference and provenance disposition

No reference acquisition is required.

One new **workspace external**, not a new source and not a new registry row, is
required for C3:

- proposed name: `GT-kitaev-prop-delta-hominc`;
- exact theorem text: `refs/kitaev-2405.02434/approximate_algebras.tex:1194-1196`;
- universal-smallness context for the source's `O(...)` notation:
  `refs/kitaev-2405.02434/approximate_algebras.tex:1192`;
- source proof available for hostile checking:
  `refs/kitaev-2405.02434/approximate_algebras.tex:1198-1222`.

The external must be added byte-verbatim to the C3 af workspace if that row is
elevated. It says that a non-unital delta-homomorphism has automatic
`1+O(delta+epsilon)` upper norm, and that a supplied lower modulus
`eta>2*delta` improves to `1-O(delta+epsilon)`. C3 supplies the required crude
lower modulus independently at every amplification before invoking it.

All other published theorems used by this design already enter through
af-validated T0 rows. In particular, no Borel, Leray-Hirsch, or additional
Hopf theorem is proposed.

## 8. Cascade / no-amendment check

No proposed wording requires an amendment to a T0 contract or a byte-matched
external in an existing workspace. The following registry contracts and T0
exports were checked:

- `proofs/lem-topology-hopf-structure`;
- `proofs/lem-topology-kunneth-cross-product`;
- `proofs/lem-topology-orientable-top-cohomology`;
- `proofs/lem-topology-lefschetz-hopf`;
- `proofs/lem-topology-local-index-sign`;
- `proofs/lem-topology-finite-triangulation`;
- `proofs/lem-topology-quotient-manifold`;
- `proofs/lem-stage1-uniform-inversion-isolation`;
- `proofs/lem-stage1-quotient-manifold-package`;
- `proofs/lem-stage1-quotient-finite-cw`;
- `proofs/lem-stage1-quotient-left-inversion`;
- `proofs/lem-stage1-quotient-inversion-index-data`;
- `proofs/lem-finite-polyhedron-maximal-simplex-placement`;
- `proofs/lem-stage1-exact-unit-rectification`;
- `proofs/lem-stage1-rectified-cstar-control`;
- `proofs/lem-stage1-rectified-cstar-transport`;
- `proofs/lem-stage1-polar-constant-ledger`;
- `proofs/lem-stage1-explicit-smooth-unitary-operations`;
- `proofs/lem-compcb-corner-algebra`;
- `proofs/lem-compcb-single-compression-transfer`.

The only scope callout is deliberate: the detailed phase-lift clause of
`lem-stage1-quotient-inversion-index-data` is local to its neighborhood of
`[J]`. C1 does **not** reinterpret it globally. Its global representative is
derived from the quotient-left-inversion row's scalar equivariance; the
quotient-index row remains the provider of the certified square-root convention
and the local isolation/index conclusion.

## 9. Honest hostile-verifier risk register

| row | first likely hostile attack | designed response / stop condition |
|---|---|---|
| `lem-stage1-exterior-cohomology` | Does an H-space without homotopy associativity really supply exactly the “bialgebra” hypotheses of the T0 Hopf row? | Match the axioms node-by-node against `proofs/lem-topology-hopf-structure/export.md`; do not smuggle in coassociativity. If its exported interface needs more than the H-unit and multiplicative coproduct proved here, stop and amend this design, not the T0 row. |
| `lem-stage1-left-inversion-associated-graded` | The sign may depend on monomial length rather than cohomological degree, or the left-inversion equation may be unbased. | Keep the basepoint-preserving homotopy explicit and use odd generator degrees only at the separate parity node. |
| `lem-stage1-left-inversion-trace` | Trace additivity may be asserted without a finite exhaustive filtration. | Fix one degree `k`; finite exterior generation and positive generator degrees make the displayed filtration finite and exhaustive before trace additivity is used. |
| `lem-stage1-extra-fixed-class` | Lefschetz-Hopf's maximal-simplex hypothesis or the top-cohomology second class may be missing. | The contradiction makes the fixed set a singleton; items 10 and 6 in the fixed dependency list supply placement and the formula, while item 8 plus `d=N-1>0` supplies a cohomology class distinct in degree from `H^0`. |
| `lem-stage1-rectified-nontrivial-projection` | The extended input may be silently replaced by an unrelated exact-unit algebra; alternatively, the local quotient-index phase lift may be used globally. | Fix one ledger tuple and one rectification, return to the original product in a dedicated node, and derive the global lift only from scalar equivariance. Any need to identify two independently produced rectifications is a blocker. |
| `lem-stage1-original-complementary-pair` | In an approximate-unit algebra, `I_X-P'` may not inherit the same projection and cross defects. | Expand both orders explicitly and price the two approximate-unit errors; enlarge `C_np` rather than claiming exact orthogonality. |
| `lem-stage1-fresh-two-point-inclusion` | Small multiplicative defect plus injectivity may be confused with complete near-isometry. | Prove a uniform crude modulus at every amplification, then invoke the exact local theorem `GT-kitaev-prop-delta-hominc`; do not use a triangle-inequality “near-max” shortcut. If the external cannot be admitted byte-verbatim with its universal context, this row stops. |

The single riskiest interface decision is C1's choice to accept an extended
ambient, select exactly one base-level ledger rectification internally, and
promise a nontrivial projection back in the **original** product/unit. This is
the right shape for M19-S1, but it concentrates the binder, threshold, and
transport obligations in one 11-node row and should be the first target of the
fresh hostile audit.
