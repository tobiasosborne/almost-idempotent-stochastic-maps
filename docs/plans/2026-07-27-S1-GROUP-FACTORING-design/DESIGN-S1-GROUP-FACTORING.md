# DESIGN — Stage-1 approximate-group factoring

**Scope and status.** Design only. This file proposes a surgical factoring
of the proof of `lem-stage1-approximate-group-laws`; it does not alter the
registry and proves nothing. The row-6 contract remains byte-for-byte
unchanged. The retained failed ledger is evidence about a viable proof
architecture, not a rigorous result.

## 1. Decision

Use exactly **two** new sub-lemmas:

1. `lem-stage1-group-domain-membership`, for right-invertibility and
   membership of the two raw group inputs in the polar domain; and
2. `lem-stage1-group-closeness`, for the two polar-correction estimates.

Leave the basepoint identities and the three defect telescopes in the
parent.

This is the smallest clean split. The retained tree shows that domain
membership and polar closeness are the two reusable quantitative blocks.
Once closeness is available as a validated registry import, associativity
and the two inverse defects are fixed-length telescopes. A third
defect-telescope shard would be inferior: under the requirement that every
new shard import only T0 rows, it could not import the closeness sibling and
would have to reproduce the whole polar-correction proof. Keeping those
telescopes in the parent avoids that duplication and remains within the
12-node parent budget.

The two new shards are deliberately independent. In particular,
`lem-stage1-group-closeness` does not import
`lem-stage1-group-domain-membership`; its compact proof repeats the raw
input-domain calculation before estimating the polar factor. This small
duplication is the price of eliminating every cross-sibling import.

## 2. Registry-ready interfaces

All displayed contracts below are one physical line, use flattened ASCII,
and contain no numerical choice of a universal constant.

### 2.1 `lem-stage1-group-domain-membership`

```text
contract: Group-input polar-domain membership: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta:S_delta -> calU of the polar map is defined at U bold-dot V and U^dagger for every U, V in calU; moreover, U bold-dot V and U^dagger each have a right inverse.
```

Prospective shard imports, exactly:

```text
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
```

The explicit right-inverse conclusion is intentional. Membership in
`calU_delta` is not merely a defect estimate under
`def-approximate-unitary-space`; it also requires a right inverse. The proof
must therefore include the finite-dimensional left-multiplier argument for
`U bold-dot V`, not silently infer membership from
`||(U bold-dot V)^dagger bold-dot (U bold-dot V) - J||` alone.

Prospective provenance: derivation from
`lem-stage1-polar-retraction` and the two registered definitions, with the
orientation supplied by Kitaev TeX 845--868 already recorded on row 6.
The source says only `O(epsilon_r)` and is not a byte-verbatim quantitative
theorem for this contract; accordingly the shard enters as `stated` and
requires its own af validation. No new cited external is proposed.

### 2.2 `lem-stage1-group-closeness`

```text
contract: Group-input polar closeness: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta:S_delta -> calU of the polar map satisfies ||u_delta(U bold-dot V) - U bold-dot V|| <= C_grp*epsilon_r and ||u_delta(U^dagger) - U^dagger|| <= C_grp*epsilon_r for every U, V in calU.
```

Prospective shard imports, exactly:

```text
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
```

The displayed expressions themselves assert that both inputs are in the
domain of `u_delta`; the proof must establish that fact internally rather
than appeal to the membership sibling. The conclusion is non-strict and is
therefore meaningful at `epsilon_r = 0`.

Prospective provenance: derivation from
`lem-stage1-polar-retraction` and the two registered definitions, with
Kitaev TeX 845--868 as the already-recorded qualitative source locus.
Again, the local source does not state this flattened universal-constant
contract byte-verbatim. The shard is `stated` until independently
af-validated; no additional published claim is introduced.

### 2.3 Unchanged parent

The parent contract must remain exactly:

```text
contract: Quantitative approximate group laws: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta of the polar map defines C^1 maps mu(U, V) = u_delta(U bold-dot V), sigma(U) = u_delta(U^dagger) on all of calU, with mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), W) - mu(U, mu(V, W))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.
```

Its prospective imports become exactly:

```text
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-group-domain-membership; lem-stage1-group-closeness; lem-stage1-polar-retraction; lem-stage1-polar-coherence-naturality
```

The two retained T0 imports have distinct jobs:
`lem-stage1-polar-retraction` supplies the C1 inverse, its calU-valued
corestriction, and `u_delta(U) = U`; coherence/naturality keeps the chosen
inverse compatible on overlaps. The other three named T0 rows
(`lem-stage1-unitary-graph-control`,
`lem-stage1-rectified-cstar-control`, and
`lem-stage1-quantitative-inverse-function`) remain transitive inputs of the
polar retraction and should not be added as unused direct imports.

## 3. Universal-witness synchronization

The two sub-lemmas quantify their constants independently. This creates no
interface gap. In the parent, take:

- `C_pol` to be the maximum of the polar constants supplied by the two
  sub-lemmas and `lem-stage1-polar-retraction`;
- `C_grp` to be the maximum of the two sub-lemma loss constants and the
  finitely many telescope coefficients; and
- `kappa_pol` to be the minimum of their positive smallness thresholds and
  any fixed endpoint-safe threshold used by the telescope proof.

These choices occur only in the proof body. Increasing `C_pol` and
`C_grp`, and decreasing `kappa_pol`, strengthens both row-6 guards. Indeed,
if `P >= P_i` and `G >= G_i`, then

```text
P*(epsilon_r + delta) <= kappa <= kappa_i
```

implies the first guard for child `i`, while

```text
G_i*epsilon_r <= G*epsilon_r < delta - P*(epsilon_r*delta + delta^2) <= delta - P_i*(epsilon_r*delta + delta^2)
```

implies its margin guard. Its estimate with coefficient `G_i` then implies
the parent estimate with coefficient `G`. Thus the independently
existential child interfaces combine monotonically without adding a
hypothesis to row 6. The failed prover's workable choice `C_grp = 600` may
be reused inside a proof attempt, but no numerical choice belongs in any
contract.

## 4. Endpoint-safe proof obligations

Write

```text
t = delta - C_pol*(epsilon_r*delta + delta^2).
```

The inherited margin is `C_grp*epsilon_r < t`, hence `t > 0`, including
when `epsilon_r = 0`. Every defect and correction estimate in the clean
trees must use `<=`. In particular:

- unitary norm and multiplier estimates are stated with `<=`;
- the raw defects of `U^dagger` and `U bold-dot V` are `<= K*epsilon_r`;
- both associator comparisons in the polar-factor calculation are
  `<= K*epsilon_r`;
- the resulting bounds for `||h_delta(X)-J||` and
  `||u_delta(X)-X||` are `<= K*epsilon_r`; and
- every propagated correction and every defect telescope uses `<=`.

There is one legitimate strict step: to invoke the definition of the open
`calU_t`, combine a non-strict raw defect
`||X^dagger bold-dot X-J|| <= K*epsilon_r` with the inherited strict margin
to obtain `||X^dagger bold-dot X-J|| < 2*t`. At
`epsilon_r = 0`, its left side is `0` and `t > 0`, so this is `0 < 2*t`,
not the false `0 < 0` pattern found in the retained challenges.

No proof node may obtain strictness merely by multiplying a strict norm
bound by `epsilon_r`: that operation loses strictness at
`epsilon_r = 0`.

## 5. Node budgets and dependency skeletons

The labels below are design labels, not proposed af node ids. An arrow list
after a node gives all of its proof dependencies. Imported T0 results are
named explicitly. A verifier should reject any node that mentions an
unlisted sibling.

### 5.1 Domain membership: target 9 nodes, hard design cap 12

| node | obligation | explicit dependencies |
|---|---|---|
| D1 | root contract and final assembly | D8 |
| D2 | choose proof-body constants; derive the polar retraction and `t > 0` | `lem-stage1-polar-retraction` |
| D3 | for `T in calU`, prove `||T|| = ||T^dagger|| <= K` | the two definitions |
| D4 | prove `L_T` is bounded below, hence bijective in finite dimension with uniformly bounded inverse | D3; the two definitions |
| D5 | prove `U^dagger` has right inverse `U` and raw defect `<= K*epsilon_r` | D3, D4 |
| D6 | prove `L_{U bold-dot V}` is an invertible perturbation of `L_U L_V`, hence `U bold-dot V` has a right inverse | D3, D4 |
| D7 | telescope associators to bound the raw product defect by `<= K*epsilon_r` | D3; the two definitions |
| D8 | combine D2 and D5--D7 to place both inputs in `calU_t subseteq S_delta` | D2, D5, D6, D7; D9 if retained |
| D9 | optional notation-only normalization if af requires the two inputs to be named before D8 | D3 |

If D9 is unnecessary, omit it rather than padding the tree. D5 must not
cite D4 as a pending sibling: it is an explicit child/import edge. D6 must
likewise name D4. This directly repairs challenges
`ch-fe5a3e5c6156f90e` and `ch-bcb1423b02741b55`.

### 5.2 Polar closeness: target and hard design cap 15 nodes

| node | obligation | explicit dependencies |
|---|---|---|
| C1 | root contract | C15 |
| C2 | choose proof-body constants; obtain the polar inverse, smallness, and `t > 0` | `lem-stage1-polar-retraction` |
| C3 | unitary norm bounds | the two definitions |
| C4 | left-multiplier lower bound and finite-dimensional inverse bound | C3; the two definitions |
| C5 | right inverse and raw defect for `U^dagger` | C3, C4 |
| C6 | right inverse for `U bold-dot V` by the multiplier perturbation | C3, C4 |
| C7 | raw defect for `U bold-dot V` by a non-strict associator telescope | C3; the two definitions |
| C8 | independently put both raw inputs in `calU_t subseteq S_delta` | C2, C5, C6, C7 |
| C9 | for either input `X`, bind `u = u_delta(X)`, `h = h_delta(X)`, `a = h-J` and record the polar decomposition and norm bounds | C2, C8 |
| C10 | first comparison in `X^dagger bold-dot X` versus `h bold-dot h`, with `<=` | C9; the two definitions |
| C11 | second comparison, with `<=`, and no reference to C10 | C9; the two definitions |
| C12 | combine the two comparisons only after both are available | C10, C11 |
| C13 | combine C5/C7 with C12 and solve the quadratic inequality for `||h-J|| <= K*epsilon_r` | C5, C7, C12 |
| C14 | derive `||u_delta(X)-X|| <= K*epsilon_r` from `X = u bold-dot h` | C9, C13 |
| C15 | specialize C14 to `X = U^dagger` and `X = U bold-dot V`, then absorb the proof-body coefficient into `C_grp` | C14 |

C11 proves only its own comparison; C12 performs the addition. This is the
repair for `ch-55c845650213104a`. C13 explicitly imports both raw-defect
branches and their combined comparison C12, repairing
`ch-a7d1fd3a5b5e60fe`. C14 and C15 use
only non-strict final estimates, repairing
`ch-6afca6cb47447c4e` and the same endpoint issue seen in
`ch-fd51d1ba33561893`.

### 5.3 Re-seeded parent: target 11 nodes, hard design cap 12

| node | obligation | explicit dependencies |
|---|---|---|
| P1 | unchanged row-6 root and final assembly | P2, P3, P4, P5, P6, P7, P8, P9, P10, P11 |
| P2 | synchronize universal witnesses by maxima/minima as in Section 3, including the coherence check on overlaps | both new sub-lemmas; both retained T0 imports |
| P3 | define the globally calU-valued C1 maps `mu` and `sigma` | P2; `lem-stage1-group-domain-membership`; `lem-stage1-polar-retraction` |
| P4 | prove `mu(J,U)=mu(U,J)=U` and `sigma(J)=J` | P3; `lem-stage1-polar-retraction` |
| P5 | instantiate the two closeness estimates, including at later unitary outputs | P2, P3; `lem-stage1-group-closeness` |
| P6 | propagate closeness through left or right multiplication using the product-norm axiom, always with `<=` | P5; the two definitions |
| P7 | add the two outer corrections, two propagated corrections, and one ambient associator to prove the associativity defect | P5, P6; the two definitions |
| P8 | telescope `sigma(U)` against `U^dagger` and use `U^dagger bold-dot U=J` for the left-inverse defect | P5, P6; the two definitions |
| P9 | derive the unitary norm and left-multiplier inverse bounds needed for the one-sided defect | the two definitions |
| P10 | derive `||U bold-dot U^dagger-J|| <= K*epsilon_r` | P9; the two definitions |
| P11 | telescope as in P8 and add the one-sided defect for the right-inverse bound | P5, P6, P10 |

The coherence check is folded into P2 rather than left as an orphaned
optional branch. P5 is the only quantitative correction import used by P6--P11;
it receives those estimates from a validated registry child rather than
the pending membership/correction siblings that caused
`ch-dae10d5f420f8290`. No defect branch cites another pending sibling. In
particular, P7 depends
explicitly on both P5 and P6, repairing
`ch-48d353ace6a9dc20` and `ch-c198eb48accb8bb0`. P8 binds
`S = sigma(U)` locally, and P11 binds it again rather than inheriting
sibling-local notation, repairing `ch-07cce128499ce3ca` and
`ch-569fb0ca4ff346d7`.

## 6. Consumer re-check

Rows 8 (`lem-stage1-inversion-derivative-control`), 11
(`lem-stage1-smooth-unitary-operations`), and 13e
(`lem-stage1-approximate-group-laws-transport`) import and consume the
contract of `lem-stage1-approximate-group-laws`, not its internal proof
deps. The direct downstream quotient consumer
`lem-stage1-quotient-left-inversion` does the same, while the remaining
quotient chain receives the group data through those rows and the polar
constant ledger. Because the row-6 contract is unchanged, none of these
consumer contracts, `defs:` lines, or `deps:` lines needs modification.
Only the internal deps line of row 6 changes as specified in Section 2.3.

## 7. Landing and hostile-check conditions

This design is suitable for verbatim escalation only if a fresh hostile
review confirms all of the following:

- both child contracts inherit exactly the row-6 algebra/domain
  quantifiers and both guards;
- no numerical constant appears in either child contract;
- each child imports only the listed T0 row and the two definitions;
- the closeness proof independently establishes its input typing;
- every estimate is non-strict at `epsilon_r = 0`;
- the only strict derived inequality is the endpoint-safe open-domain
  membership step with `t > 0`;
- every proof node has the explicit edges listed above; and
- the parent contract is byte-for-byte identical to the landed row 6.

The local TeX loci 845--878 support the qualitative architecture and the
three printed defects, but do not by themselves certify the quantitative
contracts. No theorem not present byte-verbatim in local refs is being
smuggled in as a cited external.
