# BRIEF — hostile audit of `DESIGN-THMAINEXT-ELEVATION-V2.md`

You are a **fresh, independent hostile auditor**. You did not write the design
and you owe it nothing. **Finding a gap, a hidden premise, a smuggled step, or
an overclaim is a BIG SUCCESS.** Write your audit to

```
docs/plans/2026-08-03-THMAINEXT-ELEVATION-design/AUDIT-THMAINEXT-ELEVATION-V2.md
```

Repo root: `/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps`.
Read `CLAUDE.md` §§0–6 first. **Audit only** — mutate no registry shard, no
definition, no proof workspace, no status. Your only new file is the audit.

## The object and its history

`DESIGN-THMAINEXT-ELEVATION-V2.md` proposes a **three-node** `af` tree
(`THX2-ROOT` → `THX2-REPACKAGE` → `THX2-M28`) for elevating
`lem-thmainext-conditional`, plus a seeding package: 6 definitions, all 7
frozen deps registered as externals but **only M28 cited**.

History you must hold, because it shapes the failure modes:

- **v1 was DESIGN-REJECTED** (`AUDIT-THMAINEXT-ELEVATION.md`) — read it. Its
  nine-node tree failed a **semantic deletion test**: six branches proved only
  conditional interfaces and were decorative. That audit also *settled*, in the
  design's favour, that M28 consumed as one validated external closes the
  ledger-datum existential (no hidden eighth premise).
- **The contract has since CHANGED.** The user ratified removing the method
  clause (commit `7b044403`); it is now documentary provenance. v1's quoted
  root and the v1 audit's quoted root are both **STALE**. Read the current
  `contract:` byte-for-byte from `argument/lemmas/lem-thmainext-conditional.md`
  and hold the design to THAT.
- The `deps:` line was deliberately NOT reduced — the six non-M28 edges are
  kept as the linker-enforced record of the corrected-COL-HILB etc.
  dependence. That is registry hygiene, explicitly **not** a claim that the
  proof uses them.

## Pre-checks already run (do not redo; do challenge what they don't cover)

Mechanically verified: all 8 relevant contract strings quoted in the design (the
target + 7 providers) **byte-match** the current registry; all 6 named
definition shards exist. These are provenance facts, not correctness facts.

## Attack in this order

1. **Is three nodes actually enough — or is something being smuggled?** The
   design calls this "a near-trivial existential repackaging". Test that
   claim hard. In particular:
   - **Existential elimination of `W`.** `THX2-REPACKAGE` fixes one `W` from
     M28 and only then defines `C_E`, `epsilon_E`. Is that a legitimate step as
     the design states it, or does it need its own node / a typed
     witness-instantiation child? The v1 rewire design (`DESIGN-THMAINEXT-REWIRE.md`
     §3) flagged exactly this as the one workspace construction requirement.
   - **The typing of `B`.** The root says "from a finite-dimensional
     C*-algebra"; M28 gives `B = ⊕_C M_{|C|}`. Does the design actually
     discharge that `⊕_C M_{|C|}` IS a finite-dimensional C*-algebra, or does
     it assume it? Is a definition or a citation missing?
   - **"extended `C_E*epsilon`-isomorphism".** Does the all-amplification
     meaning transfer without argument, as the design asserts, given
     `def-extended-delta-inclusion`?
   - **Universality.** The root demands independence of dimension,
     amplification level, and block data. M28 asserts its two projections are
     "finite positive universal witnesses". Is quoting that enough, or is there
     a quantifier gap — e.g. does "universal" in M28 cover exactly the three
     parameters the root names?
2. **The reverse of v1's failure: under-specification.** v1 padded; this design
   may have cut too far. Name any step `THX2-REPACKAGE` performs that a
   competent verifier would challenge as unproved, and say whether it needs its
   own node.
3. **Registered-but-uncited externals.** The design registers all seven deps but
   cites only M28, and argues this is mechanically safe (`check-refs` classifies
   `proofs/<id>` sources as `skip_import`; the linker does not equate registry
   deps with cited af externals). **Verify that claim against the actual
   scripts** (`scripts/check-refs.py`, `scripts/argument.py`,
   `scripts/af-orchestrate.py`). Is registering six unused externals safe,
   inert, or does it risk a prover being prompted to "use" them and re-inflating
   the tree? Would omitting them be better? Give a definite recommendation.
   Same question for `def-fd-cstar-diagonal`, registered as frozen metadata and
   cited nowhere.
4. **Witness and map identity.** Exactly one `W`, bound before `C_E`,
   `epsilon_E`; final `v` is M28's own typed witness; nothing renamed into it.
5. **No shrinkage.** `epsilon_E` must be exactly `W.epsilon_MAIN`, un-shrunk
   against any other threshold — the v1 audit noted this forecloses hiding a
   missing compatibility in a smaller radius. Confirm the design honours it.
6. **Vocabulary.** Are these 6 definitions the right 6? v1 omitted base
   `def-epsilon-cstar-algebra`; v2 adds it plus `def-operator-space`. **What is
   still missing?** The binding M19-S3/M28 lesson is that a defs list sized to
   the CONTRACT is not sized to the PROOF.
7. **Node cap and balloon classification.** Is the proposed cap right for a
   3-node tree, and is the design's account of what a balloon would mean
   correct?
8. **Status boundary.** Confirm the design promotes nothing: target stays
   `proved-mod-audit` / `af: none`, T0 stays 168, `op-classical` stays OPEN.

## A question I want answered explicitly

Given the re-scope, is `lem-thmainext-conditional` still a **mathematically
meaningful row**, or is it now a redundant alias for M28? The shard itself
records that it is a *thin* existential repackaging that hides `W`, the block
form, and the unit estimate. If your judgement is that elevating it buys
nothing that consuming M28 directly would not, **say so** — that is a
structural finding worth having before any codex time is spent, even though it
is outside the strict design-correctness question.

## Deliverable

Open with exactly one of `DESIGN-CONFIRMED`,
`DESIGN-CONFIRMED-WITH-CORRECTIONS` (each correction as verbatim replacement
text), or `DESIGN-REJECTED` (minimal amendment named; do not repair it
yourself). Then a section per attack with your independent finding and quoted
file/line evidence. Separate substantive from editorial. Close with what you
could not determine and what a prover/verifier cohort would challenge first.

Do not soften a finding to be agreeable, and do not manufacture one to look
thorough. If the design is right, say so and say exactly why the strongest
attack fails.
