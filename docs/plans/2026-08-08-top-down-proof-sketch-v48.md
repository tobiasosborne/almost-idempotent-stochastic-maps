# Top-down proof sketch v48: op-classical (2026-08-08, session 44 — THE LEDGER-DOMAINS QUEUE IS COMPLETE: T0 176 → 190; the entire 19-row family is rigorous)

## UNCHANGED from v47

`op-classical` is OPEN. The Route-F architecture (F0 seam → MAIN → ledger →
K-ledger → F2/F3/PRH finish), the sharp-exponent ground truth (`ex-hume`),
the dead routes (FINDINGS Rule 13), and the root-rewire-LAST discipline all
stand. The DO-NOT-REWIRE guard on `lem-routef-k-ledger` stays ON until the
strengthened replacement lands.

## Map change 1: the LEDGER-DOMAINS queue is COMPLETE (14 banks, T0 176 → 190)

Session 44 elevated, in the design's §D serial order under the re-scoped
contracts: row 5 (15/15 after two user-ratified deps repairs), row 6 (6/6),
D2 (7/7), row 7 (7/7), D3 (15/15), row 8 (factored — see change 2), row 9
(21/21), row 10 (4/4 after a fresh-prover re-seed), row 11 (7/7), row 12
(13/13), row 13 (18/18), row 14 (5/5). Every bank: fresh codex prover,
separate fresh verifier per node, oracle registered, external `fr verify`
PASS, mechanical flip, gates green, committed.

**The entire family is now T0**: the formation backbone, rows 1–14, D2, D3,
and the two ROW8-FACTOR sub-lemmas — 19 rows. In scalar terms: the full
ledger (1.1)–(1.8) is rigorously grounded, K and eta_K are rigorously
finite/positive/dimension-free, and the Delta/Upsilon factor maps with all
five closeness/telescope estimates are af-validated.

## Map change 2: row 8 was factored under the brittleness ceiling (ratified)

Row 8's honest one-tree size (~29 nodes) exceeded NODE_SOFT_CAP 26. The
user-ratified ROW8-FACTOR package (fresh-codex design; separate fresh
hostile audit VERDICT LAND, zero corrections; docs/plans/2026-08-08-ROW8-FACTOR/)
split it along its natural branches:

- `lem-routef-upsilon-prime-component-construction` (T0 182; 23/23) — the
  Choi/twirl data, the (2*C_R)^(-1) nonzero-multiplicity repair, and the
  componentwise CP construction of Upsilon' with ||Upsilon'||_cb <= 1;
- `lem-routef-upsilon-prime-left-inverse` (T0 183; 14/14) — the uniform
  amplified approximate-left-inverse estimate C_L*eta;
- the byte-frozen main row 8 (T0 184; 11/11) telescopes the two black boxes
  to the frozen conclusion.

Registry 365 → 367. New reusable GT externals (byte-matched to the pinned
source): `GT-kitaev-fd-cstar-structure` (tex:257) and
`GT-kitaev-canonical-stinespring` (tex:1621-1634).

## Map change 3: two rescope oversights in row 5's deps line, verifier-caught and ratified

The af verifiers refused row 5 as provisioned: (i) the row consumes
pi(D)=1_B, q_t>=0 with sum 1, and the norm-one representation — exported
ONLY by `lem-kitaev-diagonal-repair`, absent from the deps line; (ii) the
CP-ization hypothesis needs A's involution identified with the inherited
ambient adjoint — exported verbatim by `lem-routef-ai-defect-linearization`
(which rows 1–4 all carry), also absent. Both deps additions user-ratified
2026-08-08 (contract bytes unchanged, cone stays fully T0). The verifier
pressure was correct both times; the interface-projection lesson (v47 map
change 4.2) recurred exactly as predicted.

## Map change 4: operational lessons (FINDINGS 2026-08-08)

1. Never resume an af run across a registry ratification — recreate the
   worktree at the new HEAD.
2. STUCK + ordering/bookkeeping challenges = build-shape pathology → fresh-
   prover clean re-seed (row 10: 26-node thrash → 4/4 first pass). Distinct
   from the balloon signature (missing fact → provision).
3. Seeding-exactness audits must enumerate the TEXTBOOK THEOREMS a skeleton
   silently invokes (Wedderburn/Stinespring cost row 8's sub-lemma a 37-node
   balloon before the GT externals landed).

## The open surface after this delta

1. **F0-assembly landing + the strengthened `lem-routef-k-ledger`
   replacement** (W78 §5 step 6; releases the DO-NOT-REWIRE guard). The
   rescope audit's blast-radius section is BINDING: the strengthened parent
   must add the formation row AND rows 5/6/8/9 as direct deps; honest budget
   ~17 nodes / 4 rounds / cap 22. NOTE: the row-8 deps now factor through
   the two sub-lemmas — the strengthened-parent design should import the
   packet from `lem-routef-upsilon-prime-component-construction` directly
   where it needs construction data.
2. **Root rewire LAST** — unchanged.
3. Report sync `aism-9kmt` (unanchored banks now ~120–190 + the family).
4. Cross-device beads decision (HANDOFF §9 of session 43, still open).

## Controller note

Wave W137 logged bank-by-bank on arm FH: 14 banked pulls, 2 registry-repair
progress pulls, 1 landing progress pull, 4 null pulls (2 balloons, 1 stuck,
1 stale-checkout stall — each classified and remedied per the tripwire
taxonomy), and the design/audit dispatches. Reviewer ≠ author throughout;
zero self-judged steps; the fr bank gate exercised on every bank.

`op-classical` remains **OPEN**. T0 = 190. Registry = 367.
