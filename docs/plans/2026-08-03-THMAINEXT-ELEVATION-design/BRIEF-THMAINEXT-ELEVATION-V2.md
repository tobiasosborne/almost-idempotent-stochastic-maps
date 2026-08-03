# BRIEF v2 — `lem-thmainext-conditional` af-elevation design, against the RE-SCOPED contract

You are a fresh, independent **design mathematician**. **Design only** — mutate no
registry shard (`argument/`), no definition (`definitions/`), no proof workspace
(`proofs/`), and no status. Your only new file is

```
docs/plans/2026-08-03-THMAINEXT-ELEVATION-design/DESIGN-THMAINEXT-ELEVATION-V2.md
```

Repo root: `/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps`.
Read `CLAUDE.md` §§0–6 first.

## 1. What changed since design v1 (read this carefully)

Design v1 (`DESIGN-THMAINEXT-ELEVATION.md`) was **DESIGN-REJECTED** by a fresh
hostile audit (`AUDIT-THMAINEXT-ELEVATION.md`). Read **both** — they are the
substrate for your job, and the audit is the more important document.

The audit's rejection turned on the contract's **method clause** ("the assembly
*uses* the corrected squared COL-HILB estimate and the hostile-verified H-CB,
EXT-CB, and Stage-1 reset packets"): a factual claim about how the proof is
built, not about `A`, `B`, `v`, and not dischargeable from the seven frozen
deps, since `lem-maincb-structural-assembly` (M28) exports no trace of its own
construction and no frozen contract supplies `W.epsilon_MAIN <= e_H` or
`<= e_ext`.

**The user has since ratified removing that clause** (option B, commit
`7b044403`). The clause is now documentary provenance in the shard. **The
contract's mathematical content is byte-unchanged.** The current, and now
authoritative, `contract:` is:

```text
Extended th_main_ext assembly: there are universal C_E < infinity and epsilon_E > 0 such that every finite-dimensional extended epsilon-C*-algebra A, for 0 <= epsilon <= epsilon_E, is carried by one extended C_E*epsilon-isomorphism v:B->A from a finite-dimensional C*-algebra, with constants independent of dimension, amplification level, and block data.
```

Re-read it from `argument/lemmas/lem-thmainext-conditional.md` and treat THAT
byte string as the frozen root — not the text quoted in v1 or in the audit.

`defs:` and `deps:` are **unchanged and frozen**: the same two defs, the same
seven T0 providers. The deps were deliberately NOT reduced to M28 alone — they
are the linker-enforced record of the same "uses" statement. **That is a
registry-hygiene decision, not a licence to invent proof work for six imports
the reduced argument does not need.** See §3.

## 2. What the audit already settled (do not redo, but do sanity-check)

Attacks that **passed** in v1 and bear directly on your skeleton:

- **Q-A — no hidden eighth premise.** M28 consumed as one validated `af`
  external DOES close the ledger-datum existential: its contract binds `W` as
  "supplied by" `lem-maincb-reset-constant-ledger` and closes by asserting its
  projections are finite positive universal witnesses; `af` treats an external
  as usable without re-deriving its proof dependencies. A search of every
  `proofs/*/externals/*.json` carrying the `"Fix ... W supplied by ..."` phrase
  found **no contrary precedent**. So `lem-maincb-reset-constant-ledger` is NOT
  needed as an import.
- **Witness and map identity (attack 4).** Fixing one `W`, then
  `C_E := W.c0_cb*W.K_call` and `epsilon_E := W.epsilon_MAIN`, and taking the
  final `v:B->A` to be M28's very same typed witness, is sound.
- **Universality (attack 7).** The two receiving constants must be exactly
  M28's field expressions, **un-shrunk** — no minimum against freshly selected
  thresholds. The audit noted this pass forecloses hiding any missing
  compatibility inside a smaller `epsilon_E`.

The audit's own words on the reduced core: deleting v1's packet branches "leaves
M28's complete target-shaped existential untouched". With the method clause gone,
that is no longer a defect — it is the proof.

## 3. Your job

Design the `af` skeleton for the **re-scoped** contract. It should be small.
Deliver, in this structure:

1. **Verdict.** Is the re-scoped contract derivable from the frozen deps? If
   not — stop and say so as a contract-level finding.
2. **Node-by-node skeleton**: id/label, exact statement, parent, children, and
   the complete per-node import list (`defs:` shards, `externals:` registry-dep
   imports and any byte-verbatim ground-truth externals), plus constants
   introduced or consumed. Expect roughly three to five live nodes; justify
   whatever number you choose rather than padding to look thorough.
3. **The six non-M28 deps.** State plainly, per dep, whether the reduced proof
   uses it. If it does not, say so — **do not manufacture a node to make a
   registered import look busy**; v1 was rejected for exactly that, and the
   auditor will apply a deletion test. Recommend explicitly how the seeding
   step should handle a registered-but-unused import (register it and leave it
   unused? omit the registration and rely on the registry deps line? something
   else?) and flag any `check-refs` / linker consequence you can identify.
4. **Witness/constant ledger** — one table; `W` fixed once, before `C_E` and
   `epsilon_E`.
5. **Seeding package** — the root text byte-identical to §1; the `af def-add`
   list (names must be **UNIQUE**; `af def-add` does not reject duplicates, it
   assigns fresh ids and silently pollutes the seed); the `af add-external`
   entries with literal `proofs/<dep-id>` paths and byte-verbatim current
   contract text. **The v1 audit found a real omission you must fix: base
   `def-epsilon-cstar-algebra` was missing** (`def-extended-epsilon-cstar-algebra`
   is defined in terms of it). Provision the PROOF's vocabulary, not the
   contract's — that is the binding M19-S3/M28 lesson.
6. **Node-cap proposal** with justification (soft cap 26), and what a balloon
   past it would mean.
7. **Risk register for the hostile auditor**, ranked.

## 4. Honest framing you should engage with, not paper over

After the re-scope this row is a **thin** existential repackaging of M28: it
hides `W`, the block form `B = ⊕_C M_{|C|}`, and the unit estimate, keeping only
the two universal constants. Say whether, in your judgement, the elevation is
therefore near-trivial, and whether any step is subtler than it looks — for
instance the existential-elimination of `W`, the "from a finite-dimensional
C*-algebra" typing of `B`, or the universality clause. If the honest answer is
"this is three easy nodes", say that plainly. A short correct design is worth
more here than a long one.

## 5. Stop conditions

Escalate rather than improvise if: the re-scoped contract does not follow from
the frozen deps; a needed import is not a declared dep; a definition would have
to change; or you find yourself wanting to reword the root. The root is
byte-frozen — any weakening is scope drift and will be correctly rejected.

## 6. What must remain true

`lem-thmainext-conditional` stays `status: proved-mod-audit`, `af: none`; T0
stays 168; `op-classical` stays **OPEN**. Your output is a plan, and it is worth
exactly what a separate fresh hostile audit says it is worth.
