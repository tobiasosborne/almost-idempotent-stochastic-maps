# BRIEF — `lem-thmainext-conditional` af-elevation design (proof skeleton + workspace vocabulary)

You are a fresh, independent **design mathematician**. **Design only.** You mutate
no registry shard, no definition, no proof workspace, and no status. Everything
you produce is escalated for a *separate* fresh hostile audit and user
ratification before anything is seeded or launched. Write your design to

```
docs/plans/2026-08-03-THMAINEXT-ELEVATION-design/DESIGN-THMAINEXT-ELEVATION.md
```

Repo root: `/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps`.
Read `CLAUDE.md` §§0–6 before you begin; the rigour ladder (L0) and the
"reviewer ≠ author" law (L5) bind you.

## 1. The situation

`lem-thmainext-conditional` (the extended `th_main_ext` assembly) is the last
un-elevated node between the completed MAIN campaign and the K-ledger. It is
now **elevation-READY**:

- its **contract is byte-FROZEN** and its **`deps:` line is FROZEN** — both
  user-ratified (design v5 sect-10 step 15, re-validated by
  `docs/plans/2026-08-02-THMAINEXT-REWIRE-design/DESIGN-THMAINEXT-REWIRE.md`,
  hostile-audit verdict `DESIGN-CONFIRMED` in `AUDIT-THMAINEXT-REWIRE.md`,
  landed 2026-08-02 in commit `a3d62afd`);
- **all seven direct providers, and all 120 ancestors, are `status: proved` /
  `af: validated` (T0)** — there is no non-rigorous input;
- the workspace `proofs/lem-thmainext-conditional/` is an **unseeded empty
  scaffold** (five empty directories; no `meta.json`, no ledger, no externals),
  matching `af: none`.

So the mathematical content is settled and audited. **What is missing, and what
you are commissioned to produce, is the `af` proof skeleton and the workspace
vocabulary that goes with it.**

### Why a design round precedes the seed (the binding operational lesson)

Demonstrated twice in the MAIN campaign (M19-S3, and M28 where run 1 aborted
`[BALLOON]` at 20 nodes over a cap of 13 with the root never challenged):

> **A shard `defs:` list sized to the CONTRACT's vocabulary is not sized to the
> PROOF's vocabulary.** Four of six balloon-causing challenges were *missing
> workspace vocabulary* — definitions and externals the proof needed but which
> were never provisioned, because provisioning was driven off the shard's
> `defs:` line. Provision the **proof-plan** vocabulary — per-node import lists
> read off the design skeleton — **at seeding time**, not after a balloon.

Your skeleton is what the seeding step will be driven from. Every definition,
external, and dependency import it names must be listed explicitly, per node.

## 2. The target (byte-verbatim from `argument/lemmas/lem-thmainext-conditional.md`)

**`contract:`** — this text is FROZEN; the `af` root conjecture must equal it
verbatim (the linker enforces contract-match):

```text
Extended th_main_ext assembly: there are universal C_E < infinity and epsilon_E > 0 such that every finite-dimensional extended epsilon-C*-algebra A, for 0 <= epsilon <= epsilon_E, is carried by one extended C_E*epsilon-isomorphism v:B->A from a finite-dimensional C*-algebra; the assembly uses the corrected squared COL-HILB estimate and the hostile-verified H-CB (conj-hcb), EXT-CB (conj-extcb), and Stage-1 reset packets, with constants independent of dimension, amplification level, and block data.
```

**`defs:`** `def-extended-epsilon-cstar-algebra; def-fd-cstar-diagonal`
(the *contract's* vocabulary — expect the proof to need more; see §5).

**`deps:`** (FROZEN, seven ids, all T0):

```text
conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-assembly; lem-extcb-four-corner-merge
```

Read each provider's **current** `contract:` line from
`argument/lemmas/<id>.md` (never a paraphrase; the rewire design quotes them as
Q1–Q8 in its §2 and those quotations are current as of 2026-08-02, but
re-verify). Note that `conj-hcb` and `conj-extcb` retain historical `conj-`
prefixes with **no status semantics** — both are T0.

## 3. The mathematical spine (already established — you are routing it, not re-deriving it)

`lem-maincb-structural-assembly` (M28) supplies the final map directly:

```text
Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits a finite-dimensional C*-algebra B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon; hence C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive universal witnesses.
```

The ratified witness choice (`DESIGN-THMAINEXT-REWIRE.md` §3, hostile-audited)
is

- `C_E := W.c0_cb * W.K_call`
- `epsilon_E := W.epsilon_MAIN`

with **`W` fixed FIRST**, once, and only then the two receiving constants
defined. `B = ⊕_C M_{|C|}` is the required finite-dimensional C*-algebra, and
M28's final `v : B → A` — including its source, target, bijectivity,
amplification and unit data — **is** the target's witness map. §3 of that design
also flags the one workspace construction requirement you must now discharge:

> an `af` elevation must explicitly unpack one ledger witness (or consume M28 as
> the final typed external) before defining `C_E` and `epsilon_E`. If the proof
> language cannot elaborate that existential-elimination step directly, the
> remedy is a small typed witness-instantiation child under the unchanged root
> contract, not a root contract amendment and not a reopening of M28.

## 4. The three design questions you must answer (in order of risk)

**Q-A — the ledger-witness existential.** M28's contract *opens* with
"Fix the ... datum `W` supplied by `lem-maincb-reset-constant-ledger`". That
supplier is an ancestor of M28 but is **not** among the seven frozen direct
deps. Decide, and argue precisely:

1. Does M28's contract, consumed as a single `af` external, already discharge
   the existence of `W` (its trailing clause asserts `C_struct`, `e_struct` are
   *finite positive universal witnesses*) — so that the root can bind `C_E`,
   `epsilon_E` with no further import? **or**
2. Does the tree genuinely need `lem-maincb-reset-constant-ledger` (and/or
   `lem-maincb-witness-arithmetic`) registered as an additional external?

If your answer is (2), **STOP and escalate**: adding an import that is not a
declared dep is a `deps:` change to a user-ratified frozen line, and
`check-refs`/the linker will treat an unregistered import as a violation.
Report it as a design finding with the exact minimal amendment you would
recommend — do **not** design around it, and do **not** propose weakening the
contract. (Note for your analysis: `def-maincb-witness-ledger` is *pure data* —
it asserts no existence; the analytic-witness relation lives only in
`lem-maincb-witness-arithmetic` and `lem-maincb-reset-constant-ledger`.)

**Q-B — the "the assembly uses …" clause.** The frozen contract does not only
assert an existential; it also asserts *how* the assembly is built: "the
assembly **uses** the corrected squared COL-HILB estimate and the
hostile-verified H-CB (`conj-hcb`), EXT-CB (`conj-extcb`), and Stage-1 reset
packets". A hostile verifier will ask what discharges that clause. Design the
tree so the clause is **literally true of the tree**: plan dedicated nodes that
cite `lem-hcb-column-hilbert-squared` (the squared estimate — the corrected
replacement for the printed unsquared display at
`refs/kitaev-2405.02434/approximate_algebras.tex:1551-1555`), `conj-hcb`,
`conj-extcb`, `lem-extcb-four-corner-merge`, `lem-maincb-error-improvement` and
`lem-maincb-reset-invariant-preservation` **at their point of use**, rather than
leaving six of the seven deps as decorative unused imports. State explicitly, per
dep, which node consumes it and for what. If you conclude that some dep cannot
be given a load-bearing use under the frozen contract, say so plainly and record
it in the risk register for the auditor — do not fabricate a use.

**Q-C — the final clause.** "with constants independent of dimension,
amplification level, and block data" — plan the node that discharges universality
from M28's closing universality clause, without re-deriving MAIN.

## 5. Required deliverable (structure your design exactly like this)

1. **Verdict and one-paragraph summary** — is the frozen contract provable from
   the seven frozen T0 deps? If not, that is a contract-level finding: STOP,
   state it, and escalate (see §7).
2. **Node-by-node skeleton.** For each node: its id/label, its exact
   statement, its parent, its children, and the *complete* import list —
   - `defs:` the `definitions/def-*.md` shards it needs (verify each exists —
     `ls definitions/`),
   - `externals:` the registry-dep imports (by exact registry id) and any
     byte-verbatim ground-truth externals,
   - the constants it introduces or consumes.
3. **Witness/constant ledger.** The single table of every constant in the tree,
   where it is bound, and by which provider clause — with `W` fixed once at the
   top and `C_E`, `epsilon_E` derived from it.
4. **Seeding package.** The literal provisioning list: the root conjecture text
   (byte-identical to §2), every `af def-add` name (**names must be UNIQUE** —
   `af def-add` does *not* reject duplicates; it assigns fresh ids and silently
   pollutes the seed), every `af add-external` entry with the literal
   `proofs/<dep-id>` path for dep imports, and any byte-verbatim ground-truth
   external with its `refs/` locus and quoted text. If δ-homomorphism arithmetic
   appears anywhere, reuse the registration of `GT-kitaev-def-delta-homomorphism`
   from `proofs/lem-maincb-extended-inclusion-monotone/externals/`.
5. **Node-cap proposal** with justification. The brittleness soft cap is 26
   (`scripts/af_constants.py NODE_SOFT_CAP`); anything above it is a REFACTOR
   failure. Propose the run's hard cap and say what a balloon past it would mean.
6. **Risk register for the hostile auditor** — ranked, in the style of
   `DESIGN-THMAINEXT-REWIRE.md` §7: what to attack first, and what a correct
   rejection would look like.

## 6. Binding construction laws (violating these is what causes balloons)

From the eight first-pass banks of the MAIN campaign:

- **Constant-choice / binder node FIRST child.** Fix `W`, then `C_E`,
  `epsilon_E`, before any analytic node.
- **One fixed `W` threaded everywhere** (the same-map law). Never select a
  second ledger witness; never let a later node re-bind it.
- **Typed-witness law.** The final `v` is M28's very same typed witness. Do not
  identify it with any intermediate corner map, or with an M19-R map, merely by
  reusing a symbol.
- **No pending-sibling citations.** A node may cite only its own validated
  children and registered imports — never a sibling that has not itself been
  validated.
- **Explicit typing citations at point of use.**
- **No reset provider unless the row genuinely resets.**
- Bottom-up validation: a node reaches a verifier only when all its live
  children are `validated`.

## 7. Stop conditions (escalate, do not improvise)

- The frozen contract does **not** follow from the seven frozen T0 deps
  (contract-level finding → returns to design/user, per the orchestration law).
- A needed import is not a declared dep (Q-A route 2).
- A definition would have to change, or a new definition would have to be
  provisioned that is not derivable from existing locked shards.
- You are tempted to weaken, restate, or "clarify" the root contract. It is
  byte-frozen. Any weakening is scope drift and will be correctly rejected — the
  M24 run-1 prover's root weakening was rejected on exactly this ground.

## 8. What must remain true when you are done

`lem-thmainext-conditional` stays `status: proved-mod-audit`, `af: none`; no
registry row, definition, workspace, or export is touched by you; `op-classical`
remains **OPEN**; T0 stays at 168. Your output is a plan, and it is worth
exactly what a fresh hostile audit says it is worth.
