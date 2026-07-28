# DESIGN — 13e explicit-binder repair

Date: 2026-07-28  
Role: fresh independent design mathematician  
Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND OR SEED before a fresh hostile audit and user ratification**

## 0. Verdict

**Recommend R1, factored through two new explicit-binder bridge rows.** Keep
the ratified contract of `lem-stage1-approximate-group-laws-transport`
byte-for-byte unchanged, remove its dependence on the elliptical group-laws
family, and re-prove its seven group conclusions for the explicitly bound
polar inverse. The two reusable quantitative blocks are exposed as new
explicit-binder rows:

1. explicit group-input membership/right-invertibility; and
2. explicit polar closeness at the product and adjoint inputs.

Their proofs replay the already validated membership and closeness
derivations, but directly against the typed
`lem-stage1-polar-retraction` datum. They do **not** claim to transport the
elliptical children: the W93 ledger establishes that no exact allowed input
identifies those children's `u_delta` with the root-bound inverse.

This route is the smallest repair that reaches row 13's explicit binder
without mutating an af-validated contract. It preserves every existing
validity certificate and every existing byte-matched external. Its price is
two narrowly named bridge interfaces whose mathematical estimates parallel
the existing children; that duplication is preferable to invalidating the
three-member T0 family and cascading a changed external through three other
validated trees.

The paused W93 ledger is decisive. It proves guard transport but leaves
`R(u_pol,h_pol)` and `G(u_grp)` separate. The conditional coherence row
cannot create the missing second typed datum, and pointwise injectivity
cannot be used without the absent preimage witnesses. The contract of
`lem-stage1-smooth-unitary-operations` does not repair this: it says “the
same maps” under the group-laws and smooth-polar antecedents, but does not
export an independent typed datum containing `u_grp` or an equality
`u_grp = u_pol`. Using it as an identification bridge would assume the
synchronization it is meant only to regularity-upgrade. This does not make
the row useless downstream: once row 13 has independently supplied the
explicitly synchronized `(A_4)`/`(A_5)` datum, the same theorem can upgrade
those already identified maps. It cannot be used earlier to manufacture the
identification needed to prove `(A_5)`.

## 1. Exact registry text

### 1.1 NEW — `lem-stage1-explicit-group-domain-membership`

```text
contract: Explicit group-input polar-domain membership: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU is defined at U bold-dot V and U^dagger for every U, V in calU; moreover, U bold-dot V and U^dagger each have a right inverse.
```

```text
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
```

This is a new binder-closed bridge, not an amendment or promotion of
`lem-stage1-group-domain-membership`. Its proof is the latter's validated
10-node calculation with the polar datum named explicitly from the start:
derive the common smallness node, uniform left-multiplier bounds, the
product defect and invertible-product multiplier, the adjoint defect and
right inverse, and then use the explicit retraction's inner inclusion.

### 1.2 NEW — `lem-stage1-explicit-group-closeness`

```text
contract: Explicit group-input polar closeness: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU satisfies ||u_delta(U bold-dot V) - U bold-dot V|| <= C_grp*epsilon_r and ||u_delta(U^dagger) - U^dagger|| <= C_grp*epsilon_r for every U, V in calU.
```

```text
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
```

This is likewise new. Its proof replays the validated 12-node closeness
tree: independently type both inputs in the explicit `S_delta`, write
`X = u_delta(X) bold-dot h_delta(X)`, compare
`X^dagger bold-dot X` with `h_delta(X) bold-dot h_delta(X)`, absorb the
quadratic term in `h_delta(X)-J`, and return to the first polar factor.
Every estimate remains non-strict at `epsilon_r = 0`.

### 1.3 AMENDED deps only — `lem-stage1-approximate-group-laws-transport`

Its existing one-line `contract:` is **BYTE-UNCHANGED**, exactly:

```text
contract: Parameterized approximate-group transport: there exist C_grp^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_grp >= C_grp^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the formulas mu(U, V) = u_delta(U bold-dot V) and sigma(U) = u_delta(U^dagger) define C^1 maps on all of calU x calU and calU, respectively, and for every U, V, Z in calU, mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), Z) - mu(U, mu(V, Z))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.
```

Replace only its `deps:` line by:

```text
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-explicit-group-closeness; lem-stage1-polar-retraction; lem-stage1-polar-coherence-naturality
```

The proof chooses witnesses `(G_d,P_d,k_d)` and `(G_c,P_c,k_c)` from the
two new rows and `(P_r,k_r)` from polar retraction, and takes, in the proof
body,

```text
C_grp^0 = max{G_d, 8*G_c, 8},
C_pol^0 = max{P_d, P_c, P_r},
kappa_pol^0 = min{k_d, k_c, k_r, 1/16}.
```

For a receiving witness tuple `W`, the unchanged guards monotonically imply
all three base guards. Because all three imported polar data explicitly use
the same `delta`, source, formula, and image-defined target, ordinary inverse
uniqueness applies; `lem-stage1-polar-coherence-naturality` is retained as
the named synchronization check. The validated parent export then gives the
remaining proof verbatim at the level of estimates: compose the explicit
`C^1` inverse with multiplication and dagger, use
`u_delta(U) = U` for the three basepoint identities, and run the fixed
associativity and two inverse-defect telescopes. The choices
`C_grp^0 >= 8*G_c` and `C_grp^0 >= 8` absorb both the polar-correction
terms and the raw associator/opposite-product terms into the receiving
`C_grp*epsilon_r` budget.

### 1.4 Complete shard classification

| shard | classification | exact action |
|---|---|---|
| `lem-stage1-explicit-group-domain-membership` | **NEW** | Land the exact contract, defs, and deps above; status `stated`, then seed/elevate. |
| `lem-stage1-explicit-group-closeness` | **NEW** | Land the exact contract, defs, and deps above; status `stated`, then seed/elevate. |
| `lem-stage1-approximate-group-laws-transport` | **AMENDED** | Contract byte-unchanged; replace only `deps:` as above, then re-seed. |
| `lem-stage1-group-domain-membership` | **BYTE-UNCHANGED** | No registry or workspace mutation. |
| `lem-stage1-group-closeness` | **BYTE-UNCHANGED** | No registry or workspace mutation. |
| `lem-stage1-approximate-group-laws` | **BYTE-UNCHANGED** | No registry or workspace mutation. |
| `lem-stage1-inversion-derivative-control` | **BYTE-UNCHANGED** | Its validated tree and externals remain untouched. |
| `lem-stage1-smooth-unitary-operations` | **BYTE-UNCHANGED** | Its validated tree and externals remain untouched. |
| `lem-stage1-inversion-derivative-transport` | **BYTE-UNCHANGED** | Its validated tree and externals remain untouched. |
| `lem-stage1-polar-constant-ledger` | **BYTE-UNCHANGED** | In particular, clauses `(A_5)`–`(A_7)` remain ratified verbatim. |

## 2. Re-elevation plan

The two new bridges must validate before 13e is re-seeded. Runs are
sequential.

| workspace | action | target / hard live-node budget | exact external registrations |
|---|---|---:|---|
| `proofs/lem-stage1-explicit-group-domain-membership/` | Seed new; routine prover; fresh hostile verification. | 10 / 14 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-polar-retraction`. |
| `proofs/lem-stage1-explicit-group-closeness/` | Seed new; routine prover; fresh hostile verification. | 12 / 16 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-polar-retraction`. |
| `proofs/lem-stage1-approximate-group-laws-transport/` | **Re-seed, do not resume**, after both bridges validate; routine prover; fresh hostile verification. | 16 / 22 | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; both new bridges; `lem-stage1-polar-retraction`; `lem-stage1-polar-coherence-naturality`. |

The paused 13e tree should not be resumed. Its 28 validated nodes certify
useful guard arithmetic and negative dependency audits, but its live
37-node architecture is already above the repository soft cap and every
positive synchronization branch imports `G(u_grp)`. The repaired proof has
a different dependency spine and fits the observed 10-, 12-, and 14-node
validated templates. Preserve the three-run STUCK record in the shard and
git history, then re-seed a clean root.

The hard caps above are below 26 and within the observed 5–22-node transport
range. A cap hit is a factoring failure, not permission to enlarge the cap.
A repeated binder challenge after the exact retraction external is present
is a STUCK classification and returns to design.

### 2.1 Certificate and external cascade

No af-validated contract changes under this recommendation. Therefore:

- `lem-stage1-group-domain-membership`,
  `lem-stage1-group-closeness`, and
  `lem-stage1-approximate-group-laws` keep their current validity
  certificates and workspaces;
- `lem-stage1-inversion-derivative-control`,
  `lem-stage1-smooth-unitary-operations`, and
  `lem-stage1-inversion-derivative-transport` keep both their validity
  certificates and their current byte-matched external JSON files;
- **no mechanical external re-registration is required anywhere**; and
- the only genuine af work is the two new elevations and the clean 13e
  re-elevation. The 13e workspace has no root validity certificate to
  preserve.

This is the decisive cascade advantage over R2.

## 3. Consumer re-check

**Row 13 `(A_5)`.** The 13e root contract is unchanged and already equals
`(A_5)` after dropping only the helper's outer threshold quantifiers. The
new proof establishes its conclusions for the unique inverse of the exact
displayed
`Pi_delta: calU x B^{calH}_delta(J) -> S_delta`, not for an anaphoric
surrogate. Row 13 may therefore instantiate 13e and copy the explicit
binder, both `C^1` formulas, three exact identities, two closeness bounds,
and three group-defect bounds verbatim. No amendment to `(A_5)` is needed.

**Row 13 `(A_6)`.** Nothing in 13f or `(A_6)` changes. Their first inverse
component is explicitly bound to the same image-defined `Pi_delta` as
`(A_4)` and repaired `(A_5)`. For a fixed receiving tuple, algebra, and
`delta`, uniqueness identifies that component with the repaired 13e
component. The path guards, continuity, endpoints, and scalar equivariance
remain verbatim.

**Row 13 `(A_7)`.** Nothing in 13g or `(A_7)` changes. The existing explicit
polar and graph binders, global `C^1` `sigma`, same-chart retention, and
derivative inequality are untouched. The repaired `(A_5)` now supplies the
group operations for exactly the same explicit polar inverse; it introduces
no competing map, radius, or smoothness threshold.

**Rows 14 and later.** Every audited downstream contract in
`DESIGN-S1-POLAR-v6.md` §5 receives exactly the interface it previously
expected: row 13 still exports one compatible witness tuple, explicit group
operations, the projected paths, and the inversion derivative data. Thus
uniform inversion isolation, the quotient-manifold package, finite-CW
package, quotient left inversion, quotient inversion-index data, and the
maximal-simplex/topological obligations require no contract or deps change.
Smoothness and scalar equivariance continue to come from the existing T0
`lem-stage1-smooth-unitary-operations`. Every rows-14+ consumer of that row
also imports `lem-stage1-polar-constant-ledger`, whose `(A_4)` and repaired
`(A_5)` now provide the fully typed common polar datum and the same formulas.
Thus smooth operations is used only to upgrade those already identified
maps; it is not asked to create `u_grp = u_pol`, and none of its conclusions
is weakened.

The helper thresholds survive exactly. The 13e contract still exports
universal `C_grp^0, C_pol^0 >= 1` and
`kappa_pol^0 in (0, 1/2]`; the proof-body maxima/minimum above merely
construct them. No new field is added to
`def-stage1-polar-witness-data`, and the receiving hypotheses
`C_grp >= C_grp^0`, `C_pol >= C_pol^0`,
`0 < kappa_pol <= kappa_pol^0` are byte-unchanged. Row 13 therefore takes
the same finite maxima/minima over its seven transports, and the scalar
arithmetic thresholds `delta_*`, `epsilon_*^r`, `e_S1`, and `r_iso`
survive verbatim.

## 4. Rejected alternatives

| direction | disposition |
|---|---|
| **R2: amend the three validated family contracts** | Mathematically clean but operationally dominated here. Strictly priced under L0, it requires seven genuine re-elevations: both children, their parent, inversion control, smooth operations, inversion transport, and finally 13e. The latter three roots are byte-unchanged, but their exact allowed parent external changes, so mechanical re-registration alone is not a fresh verification of the new premise set. Smooth atlas and smooth polar inverse keep their certificates because neither imports the family. The row-13 contract itself need not change, but seven registry shards pass through the status/workspace transaction. |
| **R3: one identification lemma** | Not derivable from the exact T0 inputs. The old family supplies neither a companion `h_grp` nor even the pointwise preimage witnesses needed for injectivity. A “single explicit restatement” would have to re-prove membership and closeness internally and recreates the old balloon. The two bridge rows are the necessary factoring of that work. |
| **R4: anaphoric 13e** | Rejected. It moves the defect into explicit row-13 clause `(A_5)`. Amending `(A_5)` anaphorically would then weaken the ratified common-ledger interface and make the rows-14+ map-identification burden worse, while saving no mathematical derivation. |

## 5. Cost and principal risk

| item | cost under the recommendation |
|---|---|
| Design jobs | **1 spent** (this document). |
| Hostile audit jobs | **1 fresh** audit of the exact contracts, deps, budgets, consumer trace, and duplication risk before landing. |
| Prover jobs | **3 fresh** prover builds: two bridges, then 13e. No role reuse. |
| Verifier jobs | **2 fresh hostile verifier cohorts** under the routine batched policy: one batch with per-shard verdicts for the two independent bridges, then a separate verifier for 13e after both deps validate. AF's per-node verification calls remain bounded by the live-node caps, at most `14 + 16 + 22 = 52`. |
| Total campaign-level codex jobs | **7** including the already-spent design job, before any challenged repair round. |
| Registry shards touched | **3**: two NEW shards and one deps-only AMENDMENT; 13e's contract remains byte-unchanged. |
| Workspaces created/re-seeded | **3**: two new seeds and one clean 13e re-seed. |
| Genuine af elevations | **3** total: two first elevations plus one 13e re-elevation. Strictly counting only previously existing roots, the re-elevation count is **1**. |
| Existing T0 re-elevations / external swaps | **0 / 0**. |

The highest risk is **interface duplication**: the two new bridge rows
parallel existing validated children. The hostile audit must enforce their
narrow role, exact explicit `Pi_delta` binder, single consumer (13e), and
derivation directly from polar retraction; it must reject any claim that
they identify or supersede the old elliptical maps. The highest proof-level
risk is the endpoint-safe witness synchronization in 13e, especially the
`8*G_c` budget at `epsilon_r = 0`; the validated exports already exhibit the
needed non-strict telescopes, so no new mathematical mechanism is being
assumed.
