VERDICT: LAND-WITH-CORRECTIONS

## Required correction (exact replacement text)

Replace `DESIGN-S1-GROUP-FACTORING.md` lines 170--175 with:

> There is one legitimate strict step: to invoke the definition of the open
> `calU_t`, let `K` dominate the raw-defect coefficients for both inputs and,
> when choosing the child lemma's proof-body witnesses, require
> `C_grp >= K`. Then
> `||X^dagger bold-dot X-J|| <= K*epsilon_r <= C_grp*epsilon_r < t < 2*t`.
> At `epsilon_r = 0`, this reads `0 < t < 2*t`, because the inherited
> margin gives `t > 0`; it is not the false `0 < 0` pattern found in the
> retained challenges.

This is a proof-body correction only. It changes neither child contract nor
the byte-frozen parent contract.

## (a) Quantifiers, guards, and contract preservation — PASS

The landed row-6 contract is the single line at
`argument/lemmas/lem-stage1-approximate-group-laws.md:4`. The proposed parent
text at `DESIGN-S1-GROUP-FACTORING.md:98` is byte-identical to it (direct
string comparison and SHA256 comparison both passed).

Both child contracts retain, without alteration, the existential
`C_grp, C_pol, kappa_pol`, the finite-dimensional exact-unit
`epsilon_r`-C*-algebra quantifier, `delta > 0`, and both guards
`C_pol*(epsilon_r + delta) <= kappa_pol` and
`C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2)`:
`DESIGN-S1-GROUP-FACTORING.md:44` and
`DESIGN-S1-GROUP-FACTORING.md:71`. Neither adds a hypothesis or changes the
algebra/domain. The membership child adds right-invertibility as a
conclusion, not an antecedent. There is no selected numerical value such as
the failed proof's `600` in either contract; the literals `1` and `1/2` are
the byte-inherited normalizations in row 6, not new constant choices.

## (b) Child provability and independence — PASS subject to the stated correction

The proposed imports really are only the two definitions and
`lem-stage1-polar-retraction`
(`DESIGN-S1-GROUP-FACTORING.md:47-52`, `74-79`). Those inputs suffice.

For `T in calU`, the definition gives `T^dagger bold-dot T=J` and a right
inverse (`definitions/def-approximate-unitary-space.md:19-22`). The C*-lower
bound, product bound, associator bound, isometric involution, and exact unit
are precisely available in
`definitions/def-epsilon-cstar-algebra.md:17-22`,
`definitions/def-epsilon-cstar-algebra.md:29-37`, and
`definitions/def-epsilon-cstar-algebra.md:39-48`. The two inherited guards
force a universal small
upper bound on `epsilon_r`: since `C_pol,C_grp >= 1`,
`epsilon_r+delta <= 1/2` and
`epsilon_r < delta(1-epsilon_r-delta)`, hence
`epsilon_r < 1/6`. Consequently
`L_{T^dagger}L_T` is a uniformly small perturbation of the identity;
finite-dimensional injectivity makes `L_T` bijective with a uniform inverse
bound. Then `L_{U bold-dot V}` is a uniformly small associator perturbation
of the invertible `L_U L_V`, so it is invertible and
`U bold-dot V` has a right inverse. Also `U^dagger` has the exact right
inverse `U`. Thus the proposed D3--D8 route is genuine, not an illicit
inference from the defect estimate alone
(`DESIGN-S1-GROUP-FACTORING.md:193-205`). This directly repairs the missing
multiplier and membership dependencies recorded in
`proofs/lem-stage1-approximate-group-laws/ledger/000084.json:1`
(`ch-fe5a3e5c6156f90e`) and
`proofs/lem-stage1-approximate-group-laws/ledger/000096.json:1`
(`ch-bcb1423b02741b55`).

The closeness child does not need the membership sibling. It repeats the
preceding typing argument (C3--C8), then uses the polar decomposition
`X=u bold-dot h`, with `u in calU` and `h` in the `delta`-ball, supplied by
the T0 polar-retraction contract
(`argument/lemmas/lem-stage1-polar-retraction.md:4`). Two associator
comparisons give
`X^dagger bold-dot X = h bold-dot h + O(epsilon_r)`. Writing `h=J+a`,
exact unitality gives `h bold-dot h-J=2a+a bold-dot a`; because
`||a||<delta<=1/2`, the product axiom absorbs the quadratic term and yields
`||a||=O(epsilon_r)`, then
`||u-X||=||u-u bold-dot h||=O(epsilon_r)`. This uses no conclusion of the
membership sibling. The C9--C15 dependencies correctly isolate and then
combine the comparisons (`DESIGN-S1-GROUP-FACTORING.md:219-233`), repairing
`ch-55c845650213104a` and `ch-a7d1fd3a5b5e60fe`
(`proofs/lem-stage1-approximate-group-laws/ledger/000121.json:1`,
`proofs/lem-stage1-approximate-group-laws/ledger/000108.json:1`). The source
itself supports
only this qualitative architecture and `O(epsilon_r)` scale
(`refs/kitaev-2405.02434/approximate_algebras.tex:845-868`), so the design is
also correct not to mark either child as cited.

## (c) Endpoint safety and witness synchronization — PASS after correction

With
`t=delta-C_pol*(epsilon_r*delta+delta^2)`, the inherited strict margin gives
`t>0` even at `epsilon_r=0`
(`DESIGN-S1-GROUP-FACTORING.md:152-159`). All defect, correction, propagation,
and telescope estimates are expressly non-strict
(`DESIGN-S1-GROUP-FACTORING.md:160-168`), which addresses the actual
endpoint failures in `ch-6afca6cb47447c4e` and
`ch-fd51d1ba33561893`
(`proofs/lem-stage1-approximate-group-laws/ledger/000086.json:1`,
`proofs/lem-stage1-approximate-group-laws/ledger/000106.json:1`). The original
lines 170--175 omitted the needed
comparison between `K` and `C_grp`; the exact replacement above closes that
gap and makes the sole strict open-domain step valid at every endpoint.

The maxima/minima synchronization is monotone in the correct direction.
For nonnegative `epsilon_r,delta`, increasing `C_pol` shrinks the right side
of the margin guard, increasing `C_grp` enlarges its left side, and
decreasing `kappa_pol` strengthens the first guard. The displayed implication
chain at `DESIGN-S1-GROUP-FACTORING.md:129-145` is therefore correct.
Coherence on overlaps is available from
`argument/lemmas/lem-stage1-polar-coherence-naturality.md:4`.

## (d) Parent skeleton and all conclusions — PASS

P3 supplies both globally defined, `calU`-valued C1 maps: multiplication and
adjoint are ambient smooth maps, the membership child puts their raw inputs
in `S_delta`, and the T0 inverse is C1 with codomain `calU`
(`DESIGN-S1-GROUP-FACTORING.md:241`;
`argument/lemmas/lem-stage1-polar-retraction.md:4`). Thus the skeleton does
include C1 regularity of `mu` on `calU x calU` and the corestriction of
`sigma` into `calU`.

P4 gives all three basepoint identities from exact unitality,
`J^dagger=J`, and `u_delta(U)=U`. P5 gives both closeness estimates. P7 is
the five-term associativity telescope; P8 gives the left-inverse defect from
`U^dagger bold-dot U=J`; and P9--P11 establish and use the one-sided
`U bold-dot U^dagger=J+O(epsilon_r)` defect for the right-inverse estimate
(`DESIGN-S1-GROUP-FACTORING.md:242-249`). Hence no parent conclusion is
missing.

The challenge repairs are structurally real: P5 is a validated-child import
instead of the pending sibling criticized by `ch-dae10d5f420f8290`
(`proofs/lem-stage1-approximate-group-laws/ledger/000098.json:1`); P7
explicitly depends on P5/P6, addressing
`ch-48d353ace6a9dc20` and `ch-c198eb48accb8bb0`
(`proofs/lem-stage1-approximate-group-laws/ledger/000093.json:1`,
`proofs/lem-stage1-approximate-group-laws/ledger/000115.json:1`); and the
independent local bindings in P8/P11 address `ch-07cce128499ce3ca` and
`ch-569fb0ca4ff346d7`
(`proofs/lem-stage1-approximate-group-laws/ledger/000111.json:1`,
`proofs/lem-stage1-approximate-group-laws/ledger/000123.json:1`). Every
challenge id named by the brief or by the design exists in the retained
ledger.

## (e) Consumer re-check — PASS

The four direct consumers are exactly the direct dependents reported by the
registry. Their `deps:` lines import the parent id, not its proof internals:

- row 8: `argument/lemmas/lem-stage1-inversion-derivative-control.md:6`;
- row 11: `argument/lemmas/lem-stage1-smooth-unitary-operations.md:6`;
- row 13e:
  `argument/lemmas/lem-stage1-approximate-group-laws-transport.md:6`; and
- quotient left inversion:
  `argument/lemmas/lem-stage1-quotient-left-inversion.md:6`.

Their contracts use the global maps/domain/estimates furnished by row 6
(`argument/lemmas/lem-stage1-inversion-derivative-control.md:4`,
`argument/lemmas/lem-stage1-smooth-unitary-operations.md:4`,
`argument/lemmas/lem-stage1-approximate-group-laws-transport.md:4`, and
`argument/lemmas/lem-stage1-quotient-left-inversion.md:4`). Because the row-6
contract is unchanged, the factoring does not require any consumer edit.

## (f) DAG and linker legality — PASS

Each child depends only on `lem-stage1-polar-retraction`. The parent then
depends on both children, polar retraction, and coherence; coherence itself
already points to polar retraction
(`argument/lemmas/lem-stage1-polar-coherence-naturality.md:6`). This ordering
is acyclic, provided the two child shards are landed/elevated before the
parent is re-seeded as proposed.

The prospective parent imports all have explicit jobs:
membership in P3, closeness in P5, the C1 inverse and basepoint identity in
P2--P4, and coherence in P2
(`DESIGN-S1-GROUP-FACTORING.md:239-249`). Although the closeness child proves
its own input typing internally, the parent skeleton deliberately uses the
membership child's explicit conclusion for P3 and the closeness child's
quantitative conclusion for P5; there is no dangling or unused planned
import. The exact proposed `defs:`/`deps:` lines at
`DESIGN-S1-GROUP-FACTORING.md:101-106` therefore resolve and remain
linker-legal.
