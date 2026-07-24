# The L0 af-elevation campaign for Route F (laid 2026-07-24, session 23 close)

**Goal.** Carry the Route F chain — `proved-mod-audit` complete as of sketch v30 —
to `af: validated` (T0), bottom-up, ending at an af tree for `op-classical` itself.
This document is the campaign ground plan; the live tracker is epic **aism-xuvw**.

## Ground rules (all inherited, none new)

1. **CLAUDE.md §6 verbatim.** Claude ONLY orchestrates (`af-orchestrate.py`
   backgrounded, one call); fresh codex provers; validation ONLY by separate fresh
   codex verifiers; Claude never judges, never runs `af accept`/`af challenge`.
2. **Strictly serial.** One orchestration live at a time. While one runs, the
   registry tree (`definitions/`, `argument/`) stays CLEAN — the overreach guard is
   git-porcelain-based; queue registry edits or land them atomically between rounds.
   Banking flips happen AFTER the orchestration lands.
3. **Status propagation is the ordering law.** An af tree may import only
   af-validated deps or `cited` leaves. The Kitaev-derived material CANNOT enter as
   `cited` (its printed proof is invalid; our chain is a repair) — everything is
   re-proved inside af, leaves first.
4. **Contract-match.** Every workspace is seeded from the registry contract verbatim
   (`seed-af-workspaces.py`); the linker enforces root ≡ contract.
5. **Brittleness envelope.** Any tree heading past ~12 nodes / depth 3 is factored
   into registry sub-lemmas FIRST (that is aism-fudw), never pushed through.
6. **Elevation contracts are single minimal statements** (bd memory
   `af-elevation-contracts…`): no "hence" clauses, no compound corollaries —
   compound contracts thrash to STUCK.

## Phases (bead-tracked; deps enforced in bd)

| # | bead | target | status | notes |
|---|---|---|---|---|
| 0 | aism-h9qc | **PRH** (`lem-prh`) | **ORCHESTRATION LIVE** (launched session 23; 3 workers, 8 rounds, node-cap 40, creative tier) | Elementary, self-contained, no factoring needed. Sharpness (`lem-prh-sharpness`) elevates separately afterwards if wanted — do NOT bundle (rule 6 above). |
| 1 | aism-fudw | decomposition pass | open, unblocked | Factor PROOF-W74F-E-HCB (HCB-0/1a/1b/2/3/4), PROOF-W74F-F-EXTCB (EXTCB-1..5), PROOF-W74F-H-STAGE1 (packet sub-claims), the assembly, the ledger into ≤af-sized registry sub-lemma shards with one-line contracts. Pure registry work — schedule it BETWEEN orchestrations. |
| 2 | aism-niwk | H-CB subtree | blocked by 1 | Also needs the Ha/COL-HILB vocabulary as af-consumable defs (byte-matched `af def-add` from the pinned tex where the *definitions* are sound — definitions are citable even though the theorem proofs are not). |
| 3 | aism-fgr7 | EXT-CB subtree | blocked by 2 | Dep imports carry literal `proofs/<dep-id>` paths (check-refs). |
| 4 | aism-5byv | Stage-1 + assembly + ledger | blocked by 3 | Three separate workspaces, in that order. |
| 5 | aism-y81y | F0/F2/F3 glue + `op-classical` root | blocked by 4 | F0/F2/F3 are audit-VALID (AUDIT-W73B-ROUTE-F.md) but NOT yet registry shards — codify them first (small, statements already pinned in sketch v28 §Map-change-1), then the final composition tree. |

## Per-phase workflow (the validated loop from this session, af-adapted)

seed (contract verbatim) → commit seeding → launch `af-orchestrate.py <id>`
backgrounded → on land: if root `validated`, `af export`, flip shard
`status`/`af: validated` (mechanical reflection of the codex ledger), regenerate,
gate, commit; if aborted (balloon/stuck/overreach), classify per §6 (MISSING fact →
provision byte-matched def; DAG dep → factor; genuine gap → STOP and escalate) —
never just bump rounds.

## Failure surface to watch

- **PRH constant discipline:** the af tree must prove `2√(2ε)` as registered — if a
  prover lands a different constant, that is a contract mismatch, not a success.
- **The conditional-inverse clause of `conj-hcb`:** the amended contract is long; if
  it thrashes as an af root, factor the inverse clause into its own sub-lemma shard
  (compound-contract rule).
- **Stage-1 topological inputs** (Lefschetz–Hopf etc.): likely need byte-matched
  external refs or a `consensus` def layer — surface early in phase 1, don't discover
  it mid-orchestration.

## What this campaign does NOT change

The signed trunk stays parked; RDSE/LDHR-48 stay PAUSED; Route X deciders
(aism-ea2f) remain the priced fallback if af-elevation uncovers a genuine gap in the
chain (in which case: bank the failure, escalate, re-route — the W74F wave-3
rejection showed the loop works).
