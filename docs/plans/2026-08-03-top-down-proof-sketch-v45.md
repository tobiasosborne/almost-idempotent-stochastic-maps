# Top-down proof sketch v45: op-classical (2026-08-03, session 42 — the thmainext elevation is BLOCKED: its frozen method clause is not dischargeable from its frozen deps; T0 unchanged at 168)

## UNCHANGED from v44

The global architecture (Route F via positive approximate retract), the
completed MAIN campaign (M01–M28 all T0), the complete Stage-1 record, the
parked arms, the parallel-`af` discipline, and the honest headline
(`op-classical` **OPEN**) all stand. **T0 remains 168; nothing was seeded,
proved, or promoted this round.**

## Map change 1: `lem-thmainext-conditional` is elevation-READY but NOT elevation-ABLE

v44 listed the thmainext elevation as the next step after the deps rewire, on
the grounds that the row had become unblocked: all seven direct providers and
all 120 ancestors are T0, and the workspace is a clean unseeded scaffold. That
readiness is real, but it is **not sufficient**, and v44 did not distinguish
the two.

The W133 design round (fresh codex, xhigh) produced a nine-node skeleton, and a
**separate** fresh hostile audit returned **DESIGN-REJECTED**
(`docs/plans/2026-08-03-THMAINEXT-ELEVATION-design/AUDIT-THMAINEXT-ELEVATION.md`).
The rejection is structural, not editorial, and it is a fact about the **frozen
contract**, not about the skeleton that was tried.

### What was settled affirmatively (Q-A)

The auditor **confirms** the designer: there is **no hidden eighth premise**.
`lem-maincb-structural-assembly` (M28) consumed as one validated `af` external
does close the ledger-datum existential — its contract binds `W` as *"supplied
by"* the ledger theorem and closes by asserting its projections are finite
positive universal witnesses, and `af` treats an external as usable without
re-deriving its proof dependencies. A search of every
`proofs/*/externals/*.json` carrying the `"Fix ... W supplied by ..."` phrase
found **no contrary precedent**. So `lem-maincb-reset-constant-ledger` does
**not** need to join the deps line, and the ratified witness choice
`C_E := W.c0_cb*W.K_call`, `epsilon_E := W.epsilon_MAIN` (with `W` fixed first)
stands. The DESIGN-THMAINEXT-REWIRE §3 flag is discharged.

### What blocks the row (the method clause)

The frozen contract does not only assert an existential. It also asserts *how*
the assembly is built:

> "the assembly **uses** the corrected squared COL-HILB estimate and the
> hostile-verified H-CB (`conj-hcb`), EXT-CB (`conj-extcb`), and Stage-1 reset
> packets"

That clause is **not dischargeable from the seven frozen T0 deps**:

- M28 exports only `W.epsilon_MAIN`, the final `B,v`, and their estimates. It
  exports **no trace of its own internal construction** — no identity between
  its internal H-CB / EXT-CB / reset witnesses and witnesses freshly selected
  from the six other providers.
- The provider contracts apply only under thresholds (`e <= e_H`, `e <= e_ext`,
  `rho+epsilon <= a_merge`), and **no frozen contract states**
  `W.epsilon_MAIN <= e_H`, `W.epsilon_MAIN <= e_ext`, or the corresponding
  local-scale inequalities.
- Consequently every packet branch can only prove a **conditional interface**
  ("whenever the fixed assembly invokes …"), never that M28's actual assembly
  invokes anything. All six branches fail the **semantic deletion test**:
  deleting them leaves M28's target-shaped existential untouched and the method
  clause equally unproved. A true implication with an unproved antecedent cannot
  prove a factual "uses" clause.

Secondary substantive finding: in the reset branch, `lem-maincb-error-improvement`
says a raw map *"can be replaced by"* some `v_tilde` while
`lem-maincb-reset-invariant-preservation` independently says the call *"admits
an error-improved map `v_R`"* — the skeleton never identifies those two
existential outputs, so that branch is decorative as well. Mechanical finding:
the seed omitted base `def-epsilon-cstar-algebra` (the binding M28 seeding
lesson requires it).

Attacks that **passed**: one `W` bound before the receiving constants; the final
`v` is M28's own typed witness; the squared COL estimate and the conditional
H-CB inverse clauses are intact; `rho+epsilon <= a_merge` is used; the constants
are exactly M28's field expressions, un-shrunk; nothing is promoted. The last of
these matters strategically — it **forecloses the illicit repair** of hiding the
missing threshold compatibility inside a smaller `epsilon_E`.

## Map change 2: a new class of obstruction is now on the map

This is the first row whose blocker is neither a missing lemma nor a balloon,
but a **contract that asserts its own provenance**. The clause names
*hostile-verified packets* and reads like a transcription of the W74F verdict's
registry-impact note rather than a mathematical proposition — yet once frozen
into a `contract:`, the linker's contract-match law makes it a proof obligation
like any other. **Any registry row whose contract narrates its own method
inherits this problem**, and the cost is invisible until an elevation is
attempted. Worth a sweep of the remaining un-elevated rows before their design
rounds are commissioned.

## The open surface after this delta

- **BLOCKED, pending user decision (bead `aism-g83q`)** — the thmainext
  elevation. Three options are on the table, unjudged by the orchestrator:
  **(A)** provision a packet-trace bridge lemma + user-ratify adding it to the
  frozen deps line, then redesign — with the cost risk that such a theorem may
  require MAIN to export construction data it currently does not, which
  `DESIGN-MAINCB-REPAIR-v2`'s hand-off clause forbids;
  **(B)** re-scope the frozen contract to its existential content (which M28
  already discharges), treating the method clause as documentary provenance —
  the auditor judged this "would weaken the target" but could not determine
  whether a verifier reads the clause as prose or as a proposition;
  **(C)** park thmainext and run the decoupled campaigns first.
- **UNBLOCKED and untouched by this finding** — the 14-row ledger local radii,
  the k-ledger, and the F0-assembly design. These are the natural lane while the
  decision is pending.
- The **root rewire LAST** — unchanged from v41–v44.
- Carried: `aism-9kmt` report sync (P2; unanchored banks ~120–177), the typeset
  flags, dormant signed-trunk defs, the `aism-wazy` duplicate-contract tripwire.

## Controller note

fr arm FH: one design wave and one hostile-audit wave, harvested as a single
`progress` pull (class design, tier T2). **The round bought a real reduction of
the open question without banking a result** — it converted "elevate thmainext
next" into a precisely located contract-level obstruction plus a settled Q-A,
which is exactly what the adversarial design/audit protocol exists to produce.
No self-judged step: designer, auditor, and orchestrator were three distinct
agents, and the orchestrator judged neither artifact.
