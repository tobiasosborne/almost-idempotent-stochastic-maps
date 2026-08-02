# Top-down proof sketch v43: op-classical (2026-08-02, session 40 — the re-validation debt CLEARED and the consumer chain EXECUTED: T0 156 → 165; M-chain complete except M24/M28; one contract mis-landing fixed; one contract gap escalated)

## UNCHANGED from v42

The global architecture (Route F via positive approximate retract), the
complete Stage-1 record, the parked arms, the parallel-af discipline
(worktrees, serial banking, scoped cap amendments), and the honest headline
(`op-classical` OPEN) all stand.

## Map change 1: the retraction debt is fully cured (T0 156 → 160)

- **M19-S3 re-banked** (`lem-maincb-stage3-call-envelope`, 19/19 clean).
  The parked tree's churn and a first re-seed balloon (27 live > ceiling;
  the prover assumed an unregistered `c0 >= 1` and let leaves cite pending
  siblings) were resolved by **re-seed architecture v2**, mirroring the
  validated S2 export pattern: one constant-choice FIRST child (nonnegative
  c0 by enlargement under the explicit monotonicity import; L^0 >= 1 from
  M04; K_3^0 CHOSEN to absorb every Stage-3 scalar prerequisite) plus a
  no-pending-sibling-citation rule.
- **M18 + M20 re-flipped mechanically** (certificates intact, workspaces
  untouched, oracles re-verified PASS) exactly as the suspension protocol
  prescribed.
- **M25 re-banked** (`lem-maincb-one-class-extension`, 20/20 clean) under
  the typed-reset-alone architecture (single provider + same-map witness
  law + explicit induction dependencies + the F1 typing cure); its flip
  waited for the M18/M20 restores (serial banking honoured).
- Bead `aism-mc54` CLOSED. docs/LEARNINGS.md 2026-08-01 entries all cured.

## Map change 2: the consumer chain executed — SIX FIRST-PASS banks (T0 160 → 165)

M21 `lem-maincb-initial-reset-inclusion` (6/6), M23
`lem-maincb-stage1-strict-refinement` (11/11), M22
`lem-maincb-maximal-reset-selection` (9/9), M26
`lem-maincb-binary-block-merge` (11/11), M27
`lem-maincb-stage3-finite-recombination` (7/7) — every one FIRST-PASS
clean under the now-standard binding elevation guidance (constant-choice
first child with nonnegative universal constants and absorption; the
same-map witness law with the typed-reset provider alone; no
pending-sibling citations; typing-cited bijective=>isomorphism; explicit
induction dependencies). Zero balloons, zero re-seeds across these five.
The guidance distilled from the session-39 failures is a demonstrated
first-pass pattern.

## Map change 3: an M26 contract MIS-LANDING caught pre-launch and fixed (aism-wazy, P1)

The 894c983f landing had pasted the typed-reset provider's contract
(consumer-repair design block 3) into the M26 shard where block 1
belonged — shard and workspace were mutually consistent, so every gate
stayed green; the defect was visible only against the RATIFIED DESIGN
TEXT. Caught by pre-launch verification, fixed by landing the
user-ratified block byte-verbatim (the restored one-dimensional clause),
workspace re-seeded, then banked first-pass. **Lesson (on the bead): the
linker's contract-match is shard<->workspace only; a cheap
duplicate-contract tripwire (two registry rows sharing one byte-identical
contract) would have caught this class.** Root==ratified-text is now a
pre-launch check in the worked pattern.

## Map change 4: M24 CONTRACT-LEVEL GAP — escalated, blocks the capstone (aism-twpa, P0 USER DECISION)

`lem-maincb-stage1-maximality` requires `dim S_{P_j} = 1`, but its first
elevation established (three verifier challenges, 3/4 nodes validated)
that **no allowed input derives `dim S_{P_j} >= 1`**: the deps give only
`P_j = w(e_j) != 0` and `dim <= 1`, and `nonzero projection => nonzero
corner space` is unregistered. The prover's root weakening to `<= 1` was
correctly rejected as scope drift. The workspace is restored to the clean
ratified seed. Resolution options (design round + hostile audit +
ratification; deliberately unjudged): (a) a compressed-corner
nontriviality provider row (candidate pointer:
`lem-stage1-rectified-nontrivial-projection`, applicability unassessed);
(b) amend M24 to the provable `<= 1` form if the consumer survey (M28,
Stage-1 chain) allows; (c) strengthen a dep to export nontriviality.
**M28 (`lem-maincb-structural-assembly`) imports M24 and M27; M27 is
banked, so M28 is blocked SOLELY on the M24 decision.**

## The open surface after this delta

- **THE ONE PATH BLOCKER: the M24 decision** (aism-twpa) → then M28, the
  MAIN structural-assembly capstone — the last row of the M-chain.
- **THEN** the escalated `lem-thmainext-conditional` rewire (design
  sect-10 step 15), the decoupled campaigns (14-row ledger, k-ledger,
  f0-assembly), and the root rewire LAST — unchanged from v41/v42.
- Carried: `aism-9kmt` report sync (P2; unanchored banks now ~120–174),
  the typeset flags, dormant signed-trunk defs.

## Controller note

fr arm FH carried the session (W113–W124+: 2 re-seed cycles, 6 elevations,
8 banked pulls, 2 contract findings). The notable operational result: the
binding elevation guidance converted a 3-failure re-validation queue into
a 6-for-6 first-pass streak; and both contract defects this session were
caught by protocol (one by pre-launch ratified-text verification, one by
a hostile verifier), zero self-judged.
