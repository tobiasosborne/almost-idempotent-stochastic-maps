VERDICT: REDESIGN — Blocks A, B, and C1; C2–C3 and M19-S1 remain transitively blocked.

# Hostile audit of `DESIGN-S1-ENDGAME.md`

Date: 2026-07-29  
Role: fresh hostile design auditor  
Target: `DESIGN-S1-ENDGAME.md` against `BRIEF-S1-ENDGAME.md`

The design cannot be landed. There are two independent load-bearing failures:
Block A cannot instantiate the actual T0 Hopf-structure contract, and Blocks B/C1
do not carry one typed inversion witness across the opaque T0 boundaries. The
rectification estimates themselves are adequate, and most of the source and
M19-S1 accounting is sound, but neither fact repairs those failures.

## 1. Fatal: A1 does not discharge the actual Hopf-row antecedent

`DESIGN-S1-ENDGAME.md:44,107-113` proposes to obtain

> `A=H^*(M;R)` is a connected graded-commutative **bialgebra**

from an arbitrary H-space and then apply
`lem-topology-hopf-structure`. Its actual contract is
`argument/lemmas/lem-topology-hopf-structure.md:4`:

> a finite-dimensional connected graded-commutative bialgebra over a
> characteristic-zero field is an exterior algebra.

The validated export interprets the input through the standard graded-bialgebra
interface (`proofs/lem-topology-hopf-structure/export.md:17-65`), including a
coproduct/counit package. But an H-space in
`def-h-space-left-inversion` is not assumed homotopy associative. Kitaev says
explicitly that the resulting comultiplication may fail to be coassociative and
then introduces a nonstandard use of “bialgebra”
(`approximate_algebras.tex:1007`). The design itself acknowledges the missing
premise when A1 node 5 says not to assume coassociativity
(`DESIGN-S1-ENDGAME.md:111`).

Thus there are only two readings, and both fail:

1. If `bialgebra` has its standard meaning, A1 has not proved it.
2. If it has Kitaev's nonstandard meaning, the term is undefined in the repo and
   does not satisfy the actual T0 contract.

This is not repaired by Kunneth. The actual Kunneth row supplies the ring
isomorphism (`lem-topology-kunneth-cross-product.md:4`; export lines 15-85), not
homotopy associativity or coassociativity.

Block A must be redesigned around Hatcher's actual weak “Hopf algebra”
conditions at `refs/hatcher-algebraic-topology/AT.txt:17654-17677`, followed by
Theorem 3C.4 at `:17798-17800`. Those sources are already local, so no reference
acquisition is needed. A safe design must either add a correctly typed weak-Hopf
bridge or let A1 invoke those byte-matched externals directly. It must not claim
that the present T0 bialgebra row is applicable. Until A1 is repaired, A2 and A3
are blocked.

## 2. Fatal: Block B has no single typed `breve-sigma`

The B1 contract at `DESIGN-S1-ENDGAME.md:52` refers to “the quotient inversion
`breve-sigma`,” and its proof skeleton at lines 136-144 combines:

- the H-space/left-inversion structure from
  `lem-stage1-quotient-left-inversion`;
- isolation/index information from
  `lem-stage1-quotient-inversion-index-data`;
- actual isolation from `lem-stage1-uniform-inversion-isolation`; and
- the remaining topology rows.

All ten dependencies exist, the list at line 52 is verbatim identical to
`DESIGN-S1-POLAR-v6.md:248-259`, and every existing item is
`status: proved` / `af: validated`. That syntactic/status check passes.

The semantic composition does not. The actual contracts of the three analytic
rows quantify only the algebra and hide the selected polar tuple and operation
maps:

- `lem-stage1-uniform-inversion-isolation.md:4`;
- `lem-stage1-quotient-left-inversion.md:4`;
- `lem-stage1-quotient-inversion-index-data.md:4`.

Their exports each independently say “Fix W” from the existential
`lem-stage1-polar-constant-ledger`. None of their root contracts exports a
common typed witness identifying its `sigma`/`breve-sigma` with the maps hidden
by the other roots. Taking a finite minimum of thresholds does not prove map
equality. Reusing the notation `sigma` does not prove witness identity.

This is exactly the already-recorded failure class in
`docs/LEARNINGS.md:93-125,127-155`: an opaque provider must supply the typed
witness, and repeated notation across theorem boundaries is not binder
unification. B1 therefore cannot currently infer that one self-map is
simultaneously the left inversion whose trace is computed and the indexed map
whose sole fixed point is assumed for contradiction.

Block B needs a contract-level common-witness interface: either a supplied
typed quotient/polar package, a new bundling row whose conclusion places the
H-space, smoothness, index, isolation, and phase data on one displayed map, or
upstream parameterized contracts. “Fix the ten dependency witnesses in order”
(`DESIGN-S1-ENDGAME.md:136`) is not such an interface. This repair may require
revisiting the supposedly fixed ten-item dependency architecture.

## 3. Fatal: C1 applies B1 to one hidden inversion and A5 to another

The same defect occurs again in C1:

1. line 148 fixes a tuple `W` from `lem-stage1-polar-constant-ledger`;
2. line 150 applies B1 and obtains a fixed quotient class for B1's hidden
   `breve-sigma`;
3. lines 151-153 phase-lift that class and use ledger clause (A_5) to infer
   `||U-U^dagger||=O(epsilon_r)` for the `sigma` belonging to the newly fixed
   `W`.

No actual dependency contract identifies those two inversion maps. The direct
import of `lem-stage1-quotient-left-inversion` does not help: its root also
hides its selected tuple/map. Consequently C1 has not shown that B1's fixed
class has a representative fixed by the particular A5 map whose adjoint
closeness is used to construct `P_0`.

The repair must make the provider identity explicit. For example, B1 could
export a typed actual fixed representative for a displayed inversion together
with the near-Hermitian and isolation facts C1 consumes, provided B1 itself is
rebuilt on a common-witness package. C1 may not bridge the gap merely by
repeating `sigma`.

## 4. Rectification audit: the algebraic transport is adequate, but it does not repair finding 3

The design's transitive rectification claim at lines 68-74 is otherwise sound:

- `lem-stage1-exact-unit-rectification.md:4` gives the same involutive normed
  space, an exact unit, and product/unit closeness;
- `lem-stage1-rectified-cstar-control.md:4` strengthens this to **every**
  exact-unit `epsilon_r`-C*-axiom;
- `lem-stage1-rectified-cstar-transport.md:4` transports those conclusions to
  a receiving tuple; and
- clause (A_1) of `lem-stage1-polar-constant-ledger.md:4` repeats the complete
  object-level conclusion for the one ledger tuple.

An extended algebra is an epsilon-C*-algebra at level one, so applying (A_1)
after forgetting the additional levels is legitimate. The same norm and
involution plus
`||J-I_X||<=C_rect*epsilon_X` and
`||x bold-dot y-xy||<=C_rect*epsilon_X||x||||y||`
are enough, by fixed-term estimates, to transport the rectified projection
defect and its complement back to the original product/unit. No
dimension-dependent norm equivalence is needed.

What this layer does **not** provide is an equality between a fixed-point map
hidden inside B1 and the A5 map selected in C1. The design's riskiest decision
therefore fails because of witness transport, not because the product/unit
rectification estimates are too weak.

## 5. Source fidelity: all principal loci match, but the C3 universality citation is wrong

The following cited Kitaev loci were checked byte-for-byte and support the
uses claimed, subject to the logical defects above:

- `:917-945`: delta projections, nontriviality, the lemma target, the
  near-Hermitian-unitary bridge, and the quotient phase lift;
- `:945-969`: the quotient fixed-point contradiction;
- `:971-1050`: `prop_H-group`, the augmentation filtration, and its trace
  proof;
- `:1419-1424`: the complementary pair and two basis images; and
- `:1194-1196`: the complete statement of `prop_delta_hominc`, with proof at
  `:1198-1222`.

The proposed C3 external may therefore use the proposition block at
`:1194-1196` byte-verbatim. Its two consumed clauses are exactly:

- automatic `||v||<=1+O(delta+epsilon)` for a non-unital
  delta-homomorphism; and
- a lower upgrade when a supplied modulus `eta` satisfies `eta>2*delta`.

However, `DESIGN-S1-ENDGAME.md:215,258-266` incorrectly attributes
data-independence of the implicit constants to line 1192. Line 1192 supplies
only the implicit smallness quantifiers for `epsilon` and `delta`. The source's
global statement that each big-O is a concrete function independent of
additional data is at `approximate_algebras.tex:458`. C3's provenance and
workspace external/context ledger must add `:458`; otherwise the claimed
dimension- and amplification-independent `C_pair` is not source-grounded by
the cited context.

With `:458` added, C3's all-level argument is structurally dimension-free:
extendedness makes every amplified codomain an epsilon-C*-algebra, the four
basis-product errors are four operator-space tensor terms rather than an
entrywise sum, and the simple-tensor norm identity transports one base
nonvanishing modulus to every amplification.

## 6. M19-S1 interface: clause match passes only conditionally; the readiness claim is false now

Against the literal M15 and M19-S1 contracts at
`DESIGN-MAIN-STRUCTURE-v5.md:343,381`, the proposed C contracts have the right
consumer shape:

- C1 accepts the selected corner as an extended algebra and returns an
  original-corner-product/nontrivial projection;
- C2 uses the corner's own unit, so `P'+P''=u_{P_j}` after specialization;
- C3 returns one level-one `C^2` map with its canonical amplification family,
  exact corner-unit clause, and complete inclusion bounds;
- the internal `P',P''` are correctly distinguished from the outer targets
  `P_[1,m-1],P_j`;
- `lem-compcb-single-compression-transfer` supplies the old side when `m>1`;
  and
- the finite max/min pricing and the `m=1` branch match M15.

But `DESIGN-S1-ENDGAME.md:234` also relies on
`lem-maincb-direct-corner-envelope` (M04), which does **not** currently exist in
`argument/lemmas/`; it is only a proposed MAIN-v5 row at
`DESIGN-MAIN-STRUCTURE-v5.md:287`. Therefore lines 92-95 and 245-247 overstate
the handoff. Completing G-S1 removes one named blocker; it does not by itself
make M19-S1--M28 eligible in the current registry.

The handoff text must say in substance:

> After row 7, the G-S1 producer blocker is removed. M19-S1 remains unavailable
> until the MAIN-v5 P0 gate and the prescribed M01-M18 serial predecessors,
> including M04, are landed and validated.

## 7. Contract-form audit

The seven displayed contract cells are each one physical line, use flattened
ASCII, and assign no numerical value to a universal constant. The theorem-local
binders in A2 and the named scalar witnesses in B/C are in the expected form.

There are nevertheless two contract-level failures:

1. A1's unqualified `bialgebra` is ambiguous between the standard meaning
   required by its T0 dependency and Kitaev's explicitly nonstandard meaning.
2. B1's definite `breve-sigma` has no common typed provider carrying the same
   map through all of its consumed dependency conclusions.

These are contract failures, not proof-detail omissions.

## 8. Dependency/status audit

Every existing direct dependency named in the seven row tables is present at
`status: proved` / `af: validated`. Dependencies on an earlier proposed row
respect the stated serial order. No retired parent or `stated/seeded` row is
imported. The failures are that A1 cannot satisfy one actual antecedent and
that B1/C1 cannot identify hidden witnesses; status alone does not cure either
problem.

The claim in section 8 that the inspected exports need no amendment is therefore
unsupported. At minimum, the endgame design needs a new common-witness
interface. Whether that is supplied by a new row or an upstream T0 contract
change is a redesign decision, not a verifier repair.

## 9. Dimension and budget audit

No independent dimension leak was found in the fixed-term rectification,
projection/complement, topology contradiction, or operator-space
amplification arguments. C3 requires the source-context correction in finding
5. Block A's failure is logical, not quantitative.

The 11-node C1 projection is not a realistic `~12`-node target under the
brief's factoring rule. Its nodes 8-10 each conceal multiple verifier-visible
obligations: the rectified projection expansion, two nonvanishing branches,
original-product defect transport, original-unit complement transport, and
threshold assembly. Comparable banked rows exceeded their design targets
(`lem-stage1-rectified-cstar-control`: target 10, actual 17;
`lem-stage1-explicit-group-closeness`: target 12, actual 16). A repaired C1
should factor a fixed-unitary-to-original-projection bridge or declare a
larger honest budget before seeding. The 26-node hard ceiling is not itself
shown impossible, but the binding `~12` factoring trigger has not been met.

B1's budget must also be recomputed after the common-witness repair, and A1's
budget is meaningless until the Hopf interface is replaced. C2 and C3 are
plausibly below the hard ceiling once their predecessors are sound and C3's
external context is corrected.

## 10. Required redesign surface

1. Redesign A1 so its hypotheses exactly match a locally sourced weak-Hopf
   theorem; then re-audit A2/A3.
2. Introduce one contract-level typed quotient/polar witness shared by the
   H-space, inversion, isolation, and index conclusions used in B1.
3. Make C1 consume a fixed representative/near-Hermitian conclusion attached
   to that same displayed inversion and rectification.
4. Add Kitaev line 458 to C3's dimension-free big-O provenance.
5. Reprice/factor C1 and correct the MAIN handoff to remain conditional on the
   unlanded MAIN predecessors.

