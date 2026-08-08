# Top-down proof sketch v49: op-classical (2026-08-08, session 45 — THE KLEDGER-STRENGTHENED v2 PACKAGE IS LANDED: registry 367 → 371; T0 = 190 unchanged; the guard is released)

## UNCHANGED from v48

`op-classical` is OPEN. The Route-F architecture (F0 seam → MAIN → ledger →
K-ledger → F2/F3/PRH finish), the sharp-exponent ground truth (`ex-hume`),
the dead routes (FINDINGS Rule 13), and the root-rewire-LAST discipline all
stand. T0 = 190; no status was promoted by this landing.

## Map change 1: the strengthened `lem-routef-k-ledger` replacement is LANDED (user-ratified)

The W78 §5 step-6 package went through the full discipline in one session:

- **v1 design** (fresh codex, `docs/plans/2026-08-08-KLEDGER-STRENGTHENED/
  DESIGN-KLEDGER-STRENGTHENED.md`): strengthened ∀n ∀Q ∀η parent per
  DESIGN-F0-ASSEMBLY §1.3 + AUDIT-F0-ASSEMBLY corrections + the rescope-v2
  §6.2 deps block (15 ids retained; the ROW8-FACTOR sub-lemmas stay
  transitive — row 8's public contract already exports Υ′).
- **Hostile audit** (separate fresh codex): VERDICT **REJECT** — 1 FATAL
  (monolithic parent honestly 26–51 nodes vs hard cap 22; fallback
  factoring not auditable) + 3 HIGH (pre-∀ quantifier hoist of K ≥ 1,
  η_K > 0; missing textbook-fact census; stale report prose), with 10
  attacks CLEARED (all seams, packet existence, 15-vs-16, same-datum,
  dimension-freeness, status honesty, guard scope).
- **v2 design** (fresh codex): three first-class helper rows —
  `lem-routef-scalar-header-positivity` (pre-∀ option (a): K, ρ_fac, η_K
  are header-scalar formulas of (1.1)–(1.8), positive/finite before any
  input), `lem-routef-factor-map-packet` (F0 → formation → rows 5/6/8/9,
  one serial packet per input), `lem-routef-factor-estimate-packet` (the
  three common-K estimates + terminal arithmetic for that same packet) —
  plus the byte-identical parent contract with the three helper ids
  appended, the byte-identical F0-assembly contract, a 30-item fact
  census, and the exhaustive stale-prose manifest.
- **Fresh hostile re-audit**: VERDICT **LAND, zero corrections**, all 13
  attack items CLEARED (strict 3×-cap margins 12<14, 15<18, 15<18, 18<21,
  6<8; option-(a) validity confirmed against the definition's header-only
  formulas; census complete; byte-identity of all cleared v1 material).
- **User ratification** 2026-08-08 (land + elevate).

Landed: the replacement `lem-routef-k-ledger` (now `stated`/`af: none`, 18
deps = the ratified 15 + 3 helpers; the W74F proved-mod-audit paper ledger
recorded as superseded history), the three helper rows, and
`lem-routef-f0-assembly` (`stated`/`af: none`, deps exactly
`lem-routef-k-ledger`). Registry 367 → 371. The DO-NOT-REWIRE guard on
`lem-routef-k-ledger` is RELEASED by this landing; the `op-classical` root
rewire remains a separate, LAST, user-ratified step.

## Map change 2: the report status prose is truthful again

Per the v2 manifest §7.2 (and the round-1 audit's finding 4), eleven stale
loci were repaired: `lem-thmainext-conditional` and the MAIN/ledger cone
are now described as T0 everywhere; the open frontier is stated as the
K-ledger/helper/F0 package; `report/UNWIRED.md` whitelists the four new
stated ids and re-annotates the T0 ledger-domain block.

## The open surface after this delta

1. **The five-stage elevation queue** (per the v2 design §8; every stage
   fresh prover + separate fresh verifiers, bottom-up, never resuming
   across a ratification):
   1. `lem-routef-scalar-header-positivity` — 4 designed / cap 14 / 3 rounds.
   2. `lem-routef-factor-map-packet` — 5 / cap 18 / 4 rounds (seed only
      after stage 1 is T0; externals H1 + E1–E7).
   3. `lem-routef-factor-estimate-packet` — 5 / cap 18 / 4 rounds
      (H1, H2, E8–E12).
   4. strengthened `lem-routef-k-ledger` — 6 / cap 21 / 4 rounds (all 18
      externals; prover directed to use H1/H2/H3 + E13–E15 without
      reopening helper internals).
   5. `lem-routef-f0-assembly` — 2 / cap 8 / 2 rounds (external P).
2. **Root rewire LAST** — only after `lem-routef-f0-assembly` is T0, and
   only under a separate user-ratified package (the D1 sharpness split of
   the W78 package still governs the root contract question).
3. Report sync `aism-9kmt` (unanchored banks ~120–190 + the family).
4. USER P0 (bead `aism-aywn`): the standalone 3–5pp paper (draft in
   flight; faithfulness audit before the user sees it).

## Controller note

Wave W138 on arm FH: design/audit/redesign/re-audit dispatches and
harvests logged (`fr dispatch`/`fr log progress`); the landing wave logged
at landing. Reviewer ≠ author throughout: both audits are fresh codex; the
landing itself is a mechanical transcription of the twice-audited,
user-ratified v2 package. No banking language — nothing new is T0.

`op-classical` remains **OPEN**. T0 = 190. Registry = 371.
