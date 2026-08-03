DESIGN-REJECTED

The M28 external is sufficient to close the existential ledger choice; I do
not find the alleged hidden eighth premise.  The design nevertheless fails at
the frozen method clause.  `THX-HCB`, `THX-EXT`, and `THX-RESET` prove only
conditional interfaces of the form “whenever the fixed assembly invokes this
packet”; they never prove that M28's actual assembly invokes any packet, never
identify the packet applications with M28's actual `B,v`, and never connect
M28's `W.epsilon_MAIN` to the separately selected packet thresholds.  Their
children merely restate imported contracts.  Thus deletion leaves the
target-shaped M28 conclusion unchanged and leaves the method clause equally
unproved: the six branches are decorative, not a proof of “the assembly
uses ...”.  This is a structural/import-level stop, not an editorial repair.

## Disposition and minimal amendment

**Substantive findings.** The packet-to-M28 trace is absent (attacks 2--3),
the direct M03 branch does not identify its improved map with M19-R's output
(attack 5), and the seed omits `def-epsilon-cstar-algebra` (attack 8).  The
first two findings reject the design independently of the vocabulary omission.

**Minimal amendment.** Return to design/user.  Provision and validate one
explicit packet-trace bridge whose contract says, non-vacuously, that the
*same* M28 construction, with its one fixed `W` and its actual `B,v`, invokes
the corrected COL-HILB, H-CB, EXT-CB/four-corner, and Stage-1 reset steps under
their hypotheses, including the required threshold and same-map identities.
User-ratify adding that bridge to the frozen target `deps:` line, then redesign
the elevation around M28 plus the bridge.  Amending M28 itself would be more
invasive; deleting the frozen method clause would weaken the target.  Do not
add `lem-maincb-reset-constant-ledger` to the target merely for Q-A: attack 1
does not justify that amendment.  The redesigned seed must also add
`def-epsilon-cstar-algebra`.

**Editorial corrections.** None.  No replacement prose can cure the missing
implication, so I give no mechanical patch to the rejected skeleton.

## 1. Q-A — no hidden eighth premise

**Finding: the designer's route (1) is correct.** The M28 contract is not
merely `P(W)` for an arbitrary datum.  It binds the datum as one “supplied by”
the ledger theorem and ends by asserting that its projections are universal
witnesses:

> “Fix the def-maincb-witness-ledger datum W supplied by
> lem-maincb-reset-constant-ledger” and “hence
> C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive
> universal witnesses.”

That is byte-verbatim from
`argument/lemmas/lem-maincb-structural-assembly.md:4`.  M28 imports the supplier
itself (`argument/lemmas/lem-maincb-structural-assembly.md:6`), and its validated
proof explicitly closes universality:

> “By lem-maincb-reset-constant-ledger and
> lem-maincb-witness-arithmetic, every field of the fixed ledger W ... is
> positive, finite, universal”

(`proofs/lem-maincb-structural-assembly/export.md:231-239`).  The root containing
that binding and closing clause is `validated` and clean
(`proofs/lem-maincb-structural-assembly/export.md:3-13`).

This is exactly the module boundary: “The proof *implementation* of each
module lives in its own tiny af workspace,” while the contract is what “every
dependent's import must ... match” (`argument/README.md:14-16`).  `af` describes
an external as a theorem usable “as foundations for proof steps without
requiring re-derivation”
(`/home/tobiasosborne/Projects/vibefeld/cmd/af/add_external.go:19-23`).  A
consumer of the validated M28 theorem does not re-import M28's proof
dependencies.

The definition alone cannot supply `W`: it says “Statement (data and typing
only)” (`definitions/def-maincb-witness-ledger.md:13`) and “contains no ...
existence” (`definitions/def-maincb-witness-ledger.md:19`).  The supply comes
from the closed M28 theorem, not the definition.

I also searched every `proofs/*/externals/*.json` import containing the exact
“Fix ... W supplied by ...” phrase.  There is no consumer precedent omitting
the supplier; for example, Stage-1 maximality imports both the fixed-`W`
provider (`proofs/lem-maincb-stage1-maximality/externals/f976ff680e44bad5.json:3-4`)
and the supplier
(`proofs/lem-maincb-stage1-maximality/externals/84c15c8c37c86e7b.json:3-4`).
That absence is not contrary precedent: those consumers compose several
`W`-parameterized results and need one shared `W`; this target consumes M28's
final existential witnesses.  M28's own direct registration of the supplier
(`proofs/lem-maincb-structural-assembly/externals/351da4ada25c6898.json:3-4`)
is proof-internal encapsulation, not a transitive-import rule.

## 2. Decorative dependency branches — fatal

**Finding: all six packet nodes fail the semantic deletion test.** The target
asserts the factual method clause:

> “the assembly uses the corrected squared COL-HILB estimate and the
> hostile-verified H-CB (conj-hcb), EXT-CB (conj-extcb), and Stage-1 reset
> packets”

(`argument/lemmas/lem-thmainext-conditional.md:4`).  In contrast, the designed
parents say only:

> “Whenever the fixed assembly invokes an H-CB datum”

(`DESIGN-THMAINEXT-ELEVATION.md:101`),

> “For every EXT-CB datum used by the fixed assembly”

(`DESIGN-THMAINEXT-ELEVATION.md:131`), and

> “For every Stage-1 raw call in the fixed assembly satisfying ...”

(`DESIGN-THMAINEXT-ELEVATION.md:162`).

None asserts that such a datum or call occurs.  `THX-COL` and `THX-MERGE` are
the imported contracts verbatim (`DESIGN-THMAINEXT-ELEVATION.md:115-124,144-155`),
and `THX-IMPROVE` is likewise a contract restatement
(`DESIGN-THMAINEXT-ELEVATION.md:174-187`).  They establish available tools, not
their use in M28.  Deleting any leaf removes a name/constants from its
conditional parent but removes no proposition linking M28 to the method.  Deleting
any parent leaves M28's complete target-shaped existential untouched.  The
method clause was unsupported before and after deletion.  Calling the children
“load-bearing” in `THX-BIND` (`DESIGN-THMAINEXT-ELEVATION.md:67`) is the missing
conclusion, not a derivation of it.

## 3. Provider-to-M28 trace — fatal

**Finding: the conditional interfaces are insufficient.** M28 exports only
`W.epsilon_MAIN`, the final `B,v`, and their estimates
(`argument/lemmas/lem-maincb-structural-assembly.md:4`).  It does not export an
identity between its internal H-CB/EXT-CB/reset witnesses and new witnesses
selected from the six direct providers.  The H-CB contract applies only when
`e=delta+epsilon <= e_H` (`argument/lemmas/conj-hcb.md:4`), EXT-CB only when
`e <= e_ext` (`argument/lemmas/conj-extcb.md:4`), and the merge only when
`rho+epsilon <= a_merge`
(`argument/lemmas/lem-extcb-four-corner-merge.md:4`).  No frozen direct contract
states `W.epsilon_MAIN <= e_H`, `W.epsilon_MAIN <= e_ext`, or the corresponding
local-scale inequalities.

The design admits the defect: its packet nodes “do not assert unrecorded
inequalities such as `W.epsilon_MAIN<=e_H`” and says the seven contracts are
insufficient if actual top-level application is required
(`DESIGN-THMAINEXT-ELEVATION.md:330-336`).  Actual application is required by
the word “uses.”  A true implication with an unproved antecedent cannot prove
that factual clause.

## 4. Witness and map identity — passes in isolation

The skeleton fixes one `W`, then defines exactly
`C_E:=W.c0_cb*W.K_call` and `epsilon_E:=W.epsilon_MAIN`, and takes “the very
same B and v furnished by THX-M28” (`DESIGN-THMAINEXT-ELEVATION.md:67`).  The
constant ledger repeats the same order and expressions
(`DESIGN-THMAINEXT-ELEVATION.md:193-197`).  It neither substitutes M19-R's map
for the final `v` nor renames a corner codomain as the final ambient `A`.
This attack does not cure attacks 2--3.

## 5. Reset same-map discipline — input passes, output use fails

`THX-RESET` does require M03 and M19-R to receive “that same call and same map”
(`DESIGN-THMAINEXT-ELEVATION.md:162`), and M19-R itself promises unchanged
source, target corner, and amplification form
(`argument/lemmas/lem-maincb-reset-invariant-preservation.md:4`).  There is no
direct use of undeclared M02 or M18 in the planned workspace; as with Q-A,
their roles may be encapsulated inside validated externals.

But M03 says only that the raw map “can be replaced by” some `v_tilde`
(`argument/lemmas/lem-maincb-error-improvement.md:4`), while M19-R independently
says the raw call “admits an error-improved map v_R”
(`argument/lemmas/lem-maincb-reset-invariant-preservation.md:4`).  The skeleton
never identifies those two existential outputs.  Its `v_R` comes solely from
M19-R; the direct M03 child at most supplies constants that M19-R already
encapsulates.  Thus the direct M03 branch is decorative for the actual reset.
Trying to make it non-decorative would require a same-output instantiation
trace, not repeated notation.

## 6. Squared and conditional clauses — passes

The COL estimate has the required square
`C_col*e*||X||_{n,1}^2` (`DESIGN-THMAINEXT-ELEVATION.md:118`).  `THX-HCB`
invokes only the provider's “stated conditional inverse conclusions”
(`DESIGN-THMAINEXT-ELEVATION.md:101`), and the registered provider retains the
level-one lower-modulus and bijectivity hypotheses
(`DESIGN-THMAINEXT-ELEVATION.md:257`).  The merge uses
`rho+epsilon<=a_merge` (`DESIGN-THMAINEXT-ELEVATION.md:147`).  I found no
unsquared or unconditional strengthening.

## 7. Universality leakage — passes, but exposes attack 3

The receiving constants are exactly M28's field expressions and are not shrunk
(`DESIGN-THMAINEXT-ELEVATION.md:193-197`).  No dimension, amplification, class,
stage, or block parameter enters them.  That is correct.  It also prevents the
obvious illicit repair of replacing `epsilon_E` by a minimum of newly selected
packet thresholds; the missing compatibility must be proved by a trace bridge,
not hidden in a smaller radius.

## 8. Vocabulary hygiene and omissions — one missing definition

The seventeen names are unique, but the proof uses an extended
epsilon-C*-algebra whose definition says each amplification is “an
`epsilon`-C*-algebra” (`definitions/def-extended-epsilon-cstar-algebra.md:15`).
The canonical base definition exists as `def-epsilon-cstar-algebra`
(`definitions/INDEX.md:16`) and is absent from the literal seed list
(`DESIGN-THMAINEXT-ELEVATION.md:225-243`).  The binding M28 lesson explicitly
requires “base def-epsilon-cstar-algebra” at seeding
(`HANDOFF.md:73-76`; `argument/lemmas/lem-maincb-structural-assembly.md:40-44`).
This is a real provisioning omission.

As written, the tree performs no delta-homomorphism arithmetic: it consumes
M03, M19-R, and M28 opaquely.  Therefore the design is correct that no
`GT-kitaev-def-delta-homomorphism` external is needed for this rejected tree
(`DESIGN-THMAINEXT-ELEVATION.md:296-302`).  Any redesign that internalizes M28
or directly checks such arithmetic must reassess that conclusion.

## 9. Node cap — not realistic for this skeleton

Nine live nodes and cap 14 are plausible only if a packet-trace theorem is
already available.  It is not.  Repairing attacks 2--3 inside this workspace
would require internalizing substantial parts of MAIN; M28 alone validated at
20 nodes (`argument/lemmas/lem-maincb-structural-assembly.md:13-18`).  The
design's own balloon table correctly classifies an inaccessible ledger or
missing method connection as a stop (`DESIGN-THMAINEXT-ELEVATION.md:306-316`),
but the latter condition already holds.  The cap must not be raised to conceal
it.

## 10. Status boundary — passes

The design states that it changes no status, leaves the target at
`proved-mod-audit` / `af: none`, T0 at 168, and `op-classical` open
(`DESIGN-THMAINEXT-ELEVATION.md:3-6`).  The current shard confirms
`status: proved-mod-audit` and `af: none`
(`argument/lemmas/lem-thmainext-conditional.md:7-8`).  Nothing in the design is
a promotion.

## What remains undetermined; likely first verifier challenge

I cannot determine from the seven frozen contracts alone a non-vacuous theorem
that connects the packet providers to M28's actual `W,B,v`; no such statement
is exported.  Nor can I determine whether a future verifier would treat the
method clause as documentary prose rather than a proposition, but the frozen
contract says “uses,” and the commissioning brief requires it to be proved.

The first competent verifier challenge should land on `THX-BIND`: its three
packet children establish only conditional availability, not use by M28.  The
next likely challenge is `THX-RESET`: the direct M03 output is not shown to be
M19-R's `v_R`.  A build cohort may first encounter the missing
`def-epsilon-cstar-algebra`, but that mechanical omission is not the reason for
rejection.
