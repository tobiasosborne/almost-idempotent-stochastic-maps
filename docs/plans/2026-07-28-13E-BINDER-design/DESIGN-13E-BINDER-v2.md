# DESIGN v2 — full explicit-binder repair for 13e and the inversion spine

Date: 2026-07-28

Role: fresh independent round-2 design mathematician

Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND, SEED, OR PROMOTE before a fresh hostile audit and user ratification**

## 0. Verdict

Keep the round-1 R1 repair, add one explicit-binder smooth-operations
bridge, and rebuild the inversion spine without importing any conclusion
for an anaphorically bound polar factor into an explicitly bound map.

The two round-1 bridge contracts survive byte-for-byte. They are a
**bypass**: they repeat the membership and closeness calculations directly
for the displayed polar inverse. They do not supply the missing
\(h_X\)-witness for `u_grp`, do not identify `u_grp` with `u_pol`, and do
not discharge the W93 missing-premise test.

The retracted control contract can be re-elevated byte-unchanged after its
deps are replaced by the explicit closeness bridge and the typed polar
retraction. Its former node 1.3 then uses one explicitly bound inverse for
both factorization and closeness.

The retracted transport requires a stricter repair. Re-elevating the
byte-frozen control contract does not make the typed inverse used inside
its proof visible in that contract. As an opaque external, it still binds
its `u_delta` anaphorically. Therefore 13g must not repeat the defective
parent substitution at old node 1.6. It is re-derived directly for its
root-bound inverse, using repaired 13e for the receiving-\(W\) domain and
closeness statements, the explicit smooth bridge for regularity, and the
already sound polar and graph identifications. The control calculation is
replayed inside 13g; the control result is not a 13g dependency.

Audit finding 4 is applied literally: coherence-naturality is absent from
the repaired 13e dependency line. All synchronization below uses identical
displayed map, source, image-defined target, and ordinary uniqueness of the
inverse.

## 1. Exact registry text and shard classification

### 1.1 NEW — `lem-stage1-explicit-group-domain-membership`

Carry the round-1 contract forward verbatim:

```text
contract: Explicit group-input polar-domain membership: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU is defined at U bold-dot V and U^dagger for every U, V in calU; moreover, U bold-dot V and U^dagger each have a right inverse.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
```

Classification: **NEW**. The right inverses here are algebraic
right inverses needed for approximate-unitary membership. They are not the
missing W93 polar preimage witnesses \(h_X\).

### 1.2 NEW — `lem-stage1-explicit-group-closeness`

Carry the round-1 contract forward verbatim:

```text
contract: Explicit group-input polar closeness: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU satisfies ||u_delta(U bold-dot V) - U bold-dot V|| <= C_grp*epsilon_r and ||u_delta(U^dagger) - U^dagger|| <= C_grp*epsilon_r for every U, V in calU.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
```

Classification: **NEW**. This is the typed provider that repairs old
control node 1.3: its closeness estimate and the retraction's exact
factorization concern the unique inverse of the identical displayed
`Pi_delta`.

### 1.3 NEW — `lem-stage1-explicit-smooth-unitary-operations`

```text
contract: Explicit smooth action/operations bridge: for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0, suppose Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, is a C^1 diffeomorphism onto the open set S_delta with inverse (u_delta, h_delta), U bold-dot V and U^dagger lie in S_delta for every U, V in calU, the same graph charts make calU a smooth embedded manifold, and this same Pi_delta and its same set-theoretic inverse are smooth without changing any point or first derivative; then the scalar action U(1) x calU -> calU, (c, U) |-> cU, and the explicit maps mu: calU x calU -> calU, mu(U, V) = u_delta(U bold-dot V), and sigma: calU -> calU, sigma(U) = u_delta(U^dagger), are smooth as maps into the embedded manifold calU, obey mu(cU, dV) = c*d*mu(U, V) and sigma(cU) = conj(c)*sigma(U), and change no point or first derivative.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-polar-retraction; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse
```

Classification: **NEW**.

The contract is deliberately qualitative and conditional on object-level
typed facts, so it introduces no new coefficient or margin that would have
to be added to `def-stage1-polar-witness-data`. Its proof does not import
the anaphoric group-laws family. Smoothness is restriction/corestriction
and composition with the same smooth inverse. For covariance, first prove
directly that scalar multiples of unitaries remain in `calU`. The explicit
domain premise types both \(X\) and \(cX\). Bilinearity gives
\[
 \Pi_\delta(cu_\delta(X),h_\delta(X))=cX,
\]
so injectivity of this one displayed `Pi_delta` gives
\(u_\delta(cX)=c\,u_\delta(X)\). Apply this with
\(X=U\mathbin{\boldsymbol\cdot}V\), \(c=cd\), and with
\(X=U^\dagger\), \(c=\overline c\). No second polar datum and no
coherence lemma are used.

### 1.4 AMENDED deps only — `lem-stage1-inversion-derivative-control`

Its registered `contract:` is **BYTE-UNCHANGED**:

```text
contract: Typed inversion derivative with chart retention: there exist universal C_der, C_ch, C_pol, C_grp >= 1 and kappa_der, kappa_ch, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra, s in {+1, -1}, and 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, the globally defined sigma(U) = u_delta(U^dagger) maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart, where chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)), and F_s(A) = phi_{sJ}^par(sigma(chi_s(A))) satisfies ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for all A in B_r^{icalH}(0).
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-unitary-graph-control; lem-stage1-polar-retraction; lem-stage1-explicit-group-closeness
```

Classification: **AMENDED, deps only**.

The new external list suffices for every old node. In particular, old node
1.3 now takes \(W=u_{\rm pol}(U^\dagger)\) and
\(Q=h_{\rm pol}(U^\dagger)-J\) from the one explicit retraction datum.
`lem-stage1-explicit-group-closeness` types that same value and supplies
\(\|W-U^\dagger\|\le C_{\rm grp}\varepsilon_r\). The retraction supplies
the exact factorization. Nodes 1.4–1.9 then replay without any
map-identification inference. Coherence-naturality and approximate group
laws are removed.

### 1.5 AMENDED deps only — `lem-stage1-approximate-group-laws-transport` (13e)

Its registered `contract:` is **BYTE-UNCHANGED**:

```text
contract: Parameterized approximate-group transport: there exist C_grp^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_grp >= C_grp^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the formulas mu(U, V) = u_delta(U bold-dot V) and sigma(U) = u_delta(U^dagger) define C^1 maps on all of calU x calU and calU, respectively, and for every U, V, Z in calU, mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), Z) - mu(U, mu(V, Z))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-explicit-group-closeness; lem-stage1-polar-retraction
```

Classification: **AMENDED, deps only**. This is round-1 R1 with
`lem-stage1-polar-coherence-naturality` deleted exactly as audit finding 4
requires.

Choose bridge witnesses \((G_d,P_d,k_d)\),
\((G_c,P_c,k_c)\), and retraction witnesses \((P_r,k_r)\), and take

```text
C_grp^0 = max{G_d, 8*G_c, 8},
C_pol^0 = max{P_d, P_c, P_r},
kappa_pol^0 = min{k_d, k_c, k_r, 1/16}.
```

The direct proof uses the bridge membership and closeness for
`u_pol`, then repeats the fixed associativity and inverse-defect
telescopes. It discards `u_grp` entirely. Identical explicit
`Pi_delta`, source, and image-defined target synchronize the three inputs
by ordinary inverse uniqueness.

### 1.6 AMENDED deps only — `lem-stage1-inversion-derivative-transport` (13g)

Its registered `contract:` is **BYTE-UNCHANGED**:

```text
contract: Parameterized inversion-derivative transport: there exist C_der^0, C_ch^0, C_pol^0, C_grp^0 >= 1 and kappa_der^0, kappa_ch^0, kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_der >= C_der^0, C_ch >= C_ch^0, C_pol >= C_pol^0, C_grp >= C_grp^0, 0 < kappa_der <= kappa_der^0, 0 < kappa_ch <= kappa_ch^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0, every s in {+1, -1}, and every 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, and g_{sJ}: B_{2delta}^{icalH}(0) -> B_{2delta}^{calH}(0) for the unique C^1 map such that, for every A in B_{2delta}^{icalH}(0), f_{sJ}(A + g_{sJ}(A)) = 0, where f_{sJ}(B) = (1/2)*(((J + B^dagger) bold-dot (sJ)^dagger) bold-dot (sJ bold-dot (J + B)) - J), define chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)) and the global C^1 map sigma(U) = u_delta(U^dagger); then sigma maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart and, with F_s(A) = phi_{sJ}^par(sigma(chi_s(A))), one has ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for every A in B_r^{icalH}(0).
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-approximate-group-laws-transport; lem-stage1-explicit-group-domain-membership; lem-stage1-polar-retraction; lem-stage1-unitary-graph-control; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-explicit-smooth-unitary-operations
```

Classification: **AMENDED, deps only**.

The polar identification and graph identification from old nodes 1.3
(first half) and 1.4 are retained: their providers display exactly the
root map/domain/image and graph equation/domain/codomain. Old node 1.5.5
is replaced by an application of the explicit smooth bridge, with its
typed antecedents supplied separately. Old node 1.6 is deleted rather than
repaired by assertion: 13g directly repeats control nodes 1.2 and 1.4–1.9
for its own root-bound \(u_\delta,h_\delta,g_{sJ}\). Repaired 13e supplies
the receiving-\(W\) all-domain explicit `sigma` and its closeness;
retraction supplies the exact factorization. A fresh choice of
`C_der^0,kappa_der^0` absorbs the same fixed derivative estimates.

`lem-stage1-inversion-derivative-control` is intentionally not a 13g dep.
Its contract remains anaphoric even after its proof is repaired, so using
it as an opaque external would recreate the adjudicated node-1.6
substitution defect.

### 1.7 Downstream deps-only amendments

All three contracts below are **BYTE-UNCHANGED**. Their current shards are
`status: stated`, `af: none`; none has a validity certificate to preserve.

For `lem-stage1-uniform-inversion-isolation`, replace only `deps:` by:

```text
deps: lem-stage1-quantitative-inverse-function; lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger
```

Row-13 `(A_7)` supplies the derivative estimate for the explicit `sigma`;
the explicit smooth bridge supplies regularity. The byte-frozen
anaphoric control result is therefore removed from this consumer.

For `lem-stage1-quotient-left-inversion`, replace only `deps:` by:

```text
deps: lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger; lem-stage1-quotient-manifold-package
```

Row-13 `(A_5)` supplies the explicit group laws and `(A_6)` supplies the
explicit jointly continuous scalar-equivariant paths. The new bridge
supplies smoothness and covariance for those same explicit maps. The three
anaphoric/duplicate base deps — approximate group laws, polar-path
admissibility, and coherence-naturality — are removed.

For `lem-stage1-quotient-inversion-index-data`, replace only `deps:` by:

```text
deps: lem-stage1-uniform-inversion-isolation; lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger; lem-stage1-quotient-manifold-package; lem-stage1-quotient-left-inversion; lem-topology-local-index-sign
```

Row-13 `(A_7)` supplies the derivative information for the explicitly
bound `sigma`; the new bridge supplies
`sigma(cU) = conj(c)*sigma(U)` for the phase lift and vertical derivative.
Thus the anaphoric control, old smooth-operations, and coherence deps are
removed.

`lem-stage1-quotient-manifold-package` is **BYTE-UNCHANGED**. Its only use
of the old smooth-operations result is the binder-free scalar action, whose
proof and conclusion were not implicated by either adjudicated defect. No
other rows-14+ shard needs a repair here.

### 1.8 Complete classification

| shard | classification | action |
|---|---|---|
| `lem-stage1-explicit-group-domain-membership` | **NEW** | Land §1.1 verbatim as `stated`/`af: none`, then seed. |
| `lem-stage1-explicit-group-closeness` | **NEW** | Land §1.2 verbatim as `stated`/`af: none`, then seed. |
| `lem-stage1-explicit-smooth-unitary-operations` | **NEW** | Land §1.3 verbatim as `stated`/`af: none`, then seed. |
| `lem-stage1-inversion-derivative-control` | **AMENDED** | Contract/defs byte-unchanged; deps-only replacement in §1.4; clean re-seed. |
| `lem-stage1-approximate-group-laws-transport` | **AMENDED** | Contract/defs byte-unchanged; deps-only replacement in §1.5; clean re-seed. |
| `lem-stage1-inversion-derivative-transport` | **AMENDED** | Contract/defs byte-unchanged; deps-only replacement in §1.6; clean re-seed. |
| `lem-stage1-uniform-inversion-isolation` | **AMENDED** | Contract/defs byte-unchanged; deps-only replacement in §1.7. |
| `lem-stage1-quotient-left-inversion` | **AMENDED** | Contract/defs byte-unchanged; deps-only replacement in §1.7. |
| `lem-stage1-quotient-inversion-index-data` | **AMENDED** | Contract/defs byte-unchanged; deps-only replacement in §1.7. |
| old group-laws family, old smooth-operations row, polar/graph/smooth providers, row 13, 13f, quotient-manifold and finite-CW rows | **BYTE-UNCHANGED** | Preserve contracts, deps, workspaces, and certificates. |

## 2. Strict elevation order, budgets, and exact externals

Every old defective or ballooned workspace is cleanly re-seeded; none is
resumed. All hard caps are below 26. A cap hit returns to factoring and is
not permission to enlarge the tree.

| order | workspace | target / hard live-node cap | exact external registration list |
|---:|---|---:|---|
| 1 | `proofs/lem-stage1-explicit-group-domain-membership/` | 10 / 14 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-polar-retraction`. |
| 2 | `proofs/lem-stage1-explicit-group-closeness/` | 12 / 16 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-polar-retraction`. |
| 3 | `proofs/lem-stage1-explicit-smooth-unitary-operations/` | 12 / 18 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-explicit-group-domain-membership`; `lem-stage1-polar-retraction`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse`. |
| 4 | `proofs/lem-stage1-inversion-derivative-control/` | 10 / 14 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-unitary-graph-control`; `lem-stage1-polar-retraction`; `lem-stage1-explicit-group-closeness`. |
| 5 | `proofs/lem-stage1-approximate-group-laws-transport/` | 16 / 22 | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-explicit-group-domain-membership`; `lem-stage1-explicit-group-closeness`; `lem-stage1-polar-retraction`. |
| 6 | `proofs/lem-stage1-inversion-derivative-transport/` | 22 / 25 | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-approximate-group-laws-transport`; `lem-stage1-explicit-group-domain-membership`; `lem-stage1-polar-retraction`; `lem-stage1-unitary-graph-control`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse`; `lem-stage1-explicit-smooth-unitary-operations`. |

The two quantitative bridges are mathematically independent, but the
campaign still elevates them one after the other. The complete order is
strictly sequential as requested:

```text
explicit bridges -> explicit smooth bridge -> control -> 13e -> 13g
```

The typed-witness law is visible in every row of the table. A root-bound
`Pi_delta` inverse is backed by a provider whose exact external text
displays its source, formula, image, and inverse pair. A root-bound graph is
backed by the provider displaying its equation, domain, codomain, and
uniqueness. No same-named conclusion is used as a substitute.

## 3. Consumer re-check

**Row 13 `(A_5)` remains verbatim.** Repaired 13e has the same registered
contract as before. It supplies all of `(A_5)` for the unique inverse of
the identical displayed
`Pi_delta: calU x B_delta^{calH}(J) -> S_delta`, including both global
`C^1` formulas, three basepoint identities, two closeness estimates, and
three group-defect estimates. The proof is a `u_pol` bypass and makes no
claim about `u_grp`.

**Row 13 `(A_6)` remains verbatim.** Existing 13f already binds the first
component of the unique inverse of the same displayed map and image. For
fixed \(W\), algebra, and \(\delta\), ordinary inverse uniqueness identifies
its map with `(A_4)` and repaired `(A_5)`. Its continuity, endpoints, and
scalar equivariance are unchanged.

**Row 13 `(A_7)` remains verbatim.** Repaired 13g retains its exact
registered contract, including the explicit polar binder, explicit unique
graph binder, global `C^1` `sigma`, same-chart retention, and derivative
estimate. Its new proof establishes these directly for the root-bound
objects; it does not substitute the anaphoric parent conclusion.

The witness thresholds survive unchanged. The two quantitative bridges are
absorbed into the existing 13e and 13g proof-body maxima/minima. The new
smooth bridge is qualitative and introduces no scalar field. Therefore
`C_grp^0`, `C_pol^0`, `kappa_pol^0`, the four 13g coefficient thresholds,
the three 13g margin thresholds, and all fourteen fields of
`def-stage1-polar-witness-data` retain their registered types. Row 13 still
takes finite maxima/minima over exactly its seven transports, and its
`delta_*`, `epsilon_*^r`, `e_S1`, and `r_iso` formulas remain byte-for-byte
unchanged.

For rows 14+, §1.7 is the required consumer repair:

- uniform isolation uses row-13 `(A_7)` for the derivative of the explicit
  map and the new bridge for its smoothness;
- quotient left inversion uses `(A_5)` for group laws, `(A_6)` for paths,
  and the new bridge for the covariance needed to descend the same maps;
- quotient inversion-index data uses `(A_7)` for the quotient derivative,
  the repaired uniform-isolation row for actual fixed lifts, and
  `sigma(cU)=conj(c)*sigma(U)` from the new bridge for the square-root
  phase lift.

All three contracts remain verbatim and all three are currently
`stated`/`af: none`. Their projected later budgets remain respectively
6/3, 8/3, and 9/3; the deps cleanup adds no new mathematical conclusion.

## 4. Cost and principal risk

| item | round-2 repair cost |
|---|---|
| Design jobs | **1 spent**: this document. |
| Hostile design-audit jobs | **1 fresh** audit before any landing. |
| Fresh prover builds | **6**: two quantitative bridges, one explicit smooth bridge, control, 13e, and direct 13g. |
| Fresh hostile verifier cohorts | **6** campaign-level cohorts, one after each strictly sequential workspace build; each cohort may batch that workspace's routine node checks but may not verify a later workspace early. |
| Campaign-level codex jobs | **14** before challenged repair rounds: 1 design + 1 audit + 6 provers + 6 verifier cohorts. |
| Per-node verifier ceiling | At most **109** calls from hard caps `14 + 16 + 18 + 14 + 22 + 25`; actual target total is 82. |
| Registry shards touched at landing | **9**: 3 NEW and 6 deps-only AMENDED. |
| Workspaces created or cleanly re-seeded | **6**. |
| Previously validated, now retracted results re-elevated | **2**: control and 13g. |
| Other elevations | **3** new bridge elevations plus the first successful elevation of paused 13e. |
| Existing validated certificates disturbed | **0**. The old group-laws family, old smooth-operations row, and all typed polar/graph/smooth providers remain byte-unchanged. |
| Rows-14+ future re-elevations caused now | **0**: the three amended consumers were never validated; they retain their later 6/3, 8/3, 9/3 campaign slots. |

The highest mathematical risk is the direct 13g replay: it deliberately
duplicates the ten-node derivative mechanism rather than hiding a binder
substitution behind the repaired parent. The hostile audit must check that
every occurrence of \(u_\delta,h_\delta,\sigma,g_{sJ},\chi_s,F_s\) in that
tree descends from the root's displayed data and that the fresh constants
absorb the same endpoint-safe estimates within the 25-node hard cap.

The highest interface risk is downstream use of the qualitative smooth
bridge. Its antecedents must be discharged object-by-object from row-13
`(A_4)`–`(A_5)` and the same atlas/polar upgrades; no proof may silently
instantiate the bridge on the old anaphoric group map. A hostile finding
that tries to recover the control or 13g substitution merely from a
repaired proof's hidden deps is a recurrence of the confirmed defect, not a
minor presentation issue.
