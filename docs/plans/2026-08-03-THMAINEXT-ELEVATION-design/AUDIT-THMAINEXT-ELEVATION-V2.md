DESIGN-CONFIRMED

## Disposition

**Substantive findings:** none.  The three-node design proves exactly the
current contract, without smuggling the stale method clause back in.

**Editorial findings:** none.  I recommend no replacement text.  The warning
below about registered-but-uncited externals is operational, not a correction:
the design already distinguishes registration from citation and already tells
the prover not to reconstruct the six historical branches.

## 1. Three nodes are enough

### Existential elimination of `W`

This passes.  M28 is not merely conditional on an already-given `W`.  Its
closed root says

> “Fix the def-maincb-witness-ledger datum W supplied by
> lem-maincb-reset-constant-ledger”

and calls the two projections “finite positive universal witnesses”
(`argument/lemmas/lem-maincb-structural-assembly.md:4`).  The validated export
has the same closed root and validates that conclusion
(`proofs/lem-maincb-structural-assembly/export.md:3-13,219-239`).  The bare
ledger definition expressly contains no existence
(`definitions/def-maincb-witness-ledger.md:13-19`), so M28 genuinely supplies it.

`THX2-REPACKAGE` makes one ordinary first-order move: fix that witness, project
two fields, and suppress extra conclusions.  Its binder order is explicit
(`DESIGN-THMAINEXT-ELEVATION-V2.md:47-62`).  A separate
“witness-instantiation” child would only split this move; it is not a missing
premise.  The cap already allows such a presentation split.

### Typing of `B`

This passes.  M28 does not leave the block expression untyped.  It quantifies

> “a finite-dimensional C*-algebra B=oplus_C M_{|C|}”

(`argument/lemmas/lem-maincb-structural-assembly.md:4`;
`DESIGN-THMAINEXT-ELEVATION-V2.md:64-79`).
“Finite-dimensional C*-algebra” is the asserted type; the formula is extra
structure.  Reusing that `B` requires no direct-sum closure lemma.  Such closure
is also standard finite-dimensional C*-algebra background.

### All-amplification meaning of “extended isomorphism”

This passes by literal reuse.  The canonical definition requires the property
at *every* amplification and bijectivity
(`definitions/def-extended-delta-inclusion.md:13-17`).  After defining `C_E`,
M28's “extended `W.c0_cb*W.K_call*epsilon`-isomorphism” is exactly the root's
“extended `C_E*epsilon`-isomorphism”.  No level-one-to-CB inference occurs.

### Universality

This passes.  `W` and its projections are fixed before arbitrary `A,epsilon`
and before `B,v` (`DESIGN-THMAINEXT-ELEVATION-V2.md:51-62`).  M28 calls them
universal; its validated universality node explicitly includes independence
of dimension, amplification, and block data
(`proofs/lem-maincb-structural-assembly/export.md:219-239`).  Amplification is
also uniform in the word “extended”.  The target is a weakening of that scope.

## 2. Under-specification attack

I find no hidden operation.  The node eliminates M28's closed ledger choice,
defines two constants, instantiates M28 at arbitrary admissible `A,epsilon`,
reuses its typed `B,v`, and forgets the block/unit details.  The last operation
is weakening.  Old packet applications are absent because the current contract
no longer asserts them (`argument/lemmas/lem-thmainext-conditional.md:26-42`);
adding them would recreate V1's padding failure.

## 3. Registered-but-uncited externals

The design's mechanical claim is correct, but “inert” needs qualification.

* `check-refs.py` classifies a `proofs/<id>` source without a `refs/` locus as
  `skip_import` (`scripts/check-refs.py:108-123`) and has no citation/use test
  (`scripts/check-refs.py:159-187`).
* `argument.py` resolves registry imports, enforces status propagation, and
  checks the root contract (`scripts/argument.py:179-248`).  It never reads the
  workspace external set or compares it with node citations.
* `af-orchestrate.py` exposes all deps and directs the prover to register each
  (`scripts/af-orchestrate.py:220-229,248-262`), but says to cite a dep only “in
  any node that uses” it—not that all must be used.

Thus the six registrations are mechanically safe and logically irrelevant if
uncited, but operationally visible: they may tempt reinflation.  **Definite
recommendation:** under the current driver, register all seven, cite only M28,
and prune any revived historical branch.  Initial omission is not better
because the build prompt adds them back; true omission needs a policy change.

Likewise register `def-fd-cstar-diagonal` because it is frozen metadata
(`argument/lemmas/lem-thmainext-conditional.md:5`), but do not cite or use it.

## 4. Witness and map identity

This passes exactly.  V2 binds one `W` once, before either receiving constant,
and then takes `B,v` to be “exactly” M28's witnesses
(`DESIGN-THMAINEXT-ELEVATION-V2.md:47-62,118-131`).  No reset map, corner map,
or renamed target appears.  The final `v:B->A` is M28's own typed witness.

## 5. No shrinkage

This passes.  The ledger sets
`C_E:=W.c0_cb*W.K_call` and
`epsilon_E:=W.epsilon_MAIN` exactly
(`DESIGN-THMAINEXT-ELEVATION-V2.md:60-62,122-128`).  No minimum with H-CB,
EXT-CB, merge, improvement, or reset thresholds is selected; V2 explicitly
states that none of those constants is consumed
(`DESIGN-THMAINEXT-ELEVATION-V2.md:130-131`).

## 6. Vocabulary

The six-definition seed is sufficient:

* `def-epsilon-cstar-algebra` and `def-operator-space` are the base notions in
  the extended-algebra definition
  (`definitions/def-extended-epsilon-cstar-algebra.md:14-16`).
* `def-extended-epsilon-cstar-algebra` types `A`.
* `def-extended-delta-inclusion` supplies `v`'s amplified semantics
  (`definitions/def-extended-delta-inclusion.md:13-17`).
* `def-maincb-witness-ledger` types `W` and its projected fields.
* `def-fd-cstar-diagonal` is the deliberately unused frozen metadata import.

No M28 internals or delta-homomorphism arithmetic are re-derived, so V1's
partition/reset/raw-call definitions and the GT external are unnecessary.

## 7. Node cap and balloon classification

Expected size 3 and hard cap 6 are proportionate.  The driver aborts only when
the live count is greater than the supplied cap
(`scripts/af-orchestrate.py:406-417`), so this permits up to three additional
presentation nodes while remaining far below the shared soft cap 26
(`scripts/af_constants.py:8-16,19`).

A tree exceeding 6 requires challenge inspection, not a cap increase.  V2's
diagnoses—re-proving M28, animating historical deps, duplicating vocabulary,
or failing to consume the closed witness—cover the realistic failure modes.

## 8. Status boundary

This passes.  The design explicitly changes nothing and leaves the target,
T0, and the north star untouched
(`DESIGN-THMAINEXT-ELEVATION-V2.md:3-6,251-255`).  The live shard remains
`status: proved-mod-audit` / `af: none`
(`argument/lemmas/lem-thmainext-conditional.md:7-8`); the current ledger records
T0 = 168 and `op-classical` OPEN (`HANDOFF.md:14-18`).  This audit is not an
elevation or a status promotion.

## 9. Is the row meaningful, or an alias for M28?

**Mathematically, it is redundant relative to M28: a strict weakening with no
new analytic information.**  Any M28 consumer can project the existential
directly; elevation proves no mathematics absent from M28.

**Structurally, it remains a meaningful interface, not a byte-identical
alias.**  It hides `W`, blocks, and the unit estimate, exposing the two Route-F
constants (`argument/lemmas/lem-thmainext-conditional.md:44-50`).  Its value is
validated interface projection and DAG decoupling, not theorem strength.  If
minimising rows were the only criterion, direct M28 consumption would make it
dispensable.

## What remains undetermined; first cohort challenge

I cannot predict whether the build prover will obey the shard's thin-interface
note or be distracted by the six registered historical externals.  That is an
operational risk, not a logical gap, and the unmodified prompt makes complete
registration unavoidable without a policy change.

The first hostile verifier challenge should target `THX2-REPACKAGE` and ask
whether “universal” really covers the target's three named parameters.  The
answer should cite the binder order, the definition of “extended”, and M28's
universal-witness clause; if the prover instead invokes any packet theorem or
shrinks `epsilon_E`, it has departed from this confirmed design.  The next
challenge should confirm that the phrase “a finite-dimensional C*-algebra
B=...” is being reused as a typed assertion, not re-proved from the block
formula.
