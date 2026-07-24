# BRIEF — W74F-G hostile verification: attack the unconditional relative K/η_K ledger (aism-xpxk)

You are a FRESH HOSTILE VERIFIER. You wrote none of what you read; your job is to BREAK
it. A dangling symbol, an undefined threshold, a hidden block-count or dimension factor,
a wrong coefficient, or a smuggled unproved estimate is a BIG SUCCESS. Reach your own
verdict from the primary source; treat NO repository document as an oracle.

## Target

`docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md` — UNVERIFIED prover
output claiming: with H-CB and EXT-CB as inputs, the Route F chain has a CLOSED relative
universal-constant ledger — symbol table (§1), MAIN-CB reset verification (§2), `K`
(§3), `η_K` (§4), and the finish `‖Q−E‖ ≤ (K+4√(2K))√η` (§5) — with no dangling symbol,
no dangling threshold, and no dimension/block dependence.

## Primary source (verify FIRST)

`refs/kitaev-2405.02434/approximate_algebras.tex` — `sha256sum` must equal
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. The ledger's cited
loci run through the functional calculus (`tex:2171-2179`), approximate algebra
(`tex:2192-2209`), improvement (`tex:1317-1318`), MAIN-CB stages (`tex:1414-1444`),
factor maps (`tex:2749-2766`), CP-izations (`tex:2780-2899`), and degree-2/3 estimates
(`tex:2803-2829`). Check each locus yourself.

Wave-2 inputs (hostile-verified separately; re-derive if you doubt):
`PROOF-W74F-E-HCB.md`+`VERDICT-W74F-E-HCB.md`, `PROOF-W74F-F-EXTCB.md`+
`VERDICT-W74F-F-EXTCB.md`; wave-1: `DECOMP-W74F-C-THMAINEXT.md` (esp. §5),
`PROOF-W74F-B-DIAGONAL.md`, `AUDIT-W74F-D-ALMOSTIDEMP.md`, `VERDICT-W74F-BATCH.md`.

## Attack surface (hit at least these)

1. **Symbol table completeness (§1).** Walk the ENTIRE Route F pipeline and hunt for
   any universal coefficient or threshold NOT in the table (that is the definition of
   failure for this artifact). Check each entry's producing inequality and locus.
2. **The reset verification (§2)** — the one genuinely new inequality. Is the claimed
   invariant actually maintained through the printed MAIN-CB stages (`tex:1414-1444`)?
   Is "at most one compression transfer between reset and next extension/merge" true of
   the printed proof? Do (2.1)–(2.3) really bound every pre-reset raw packet below
   `δ_max^cb` with NO block-count factor, and is `L = C_co(1+c_0^cb)` legitimate?
3. **Normalization judgments (§0, defect 3).** The prover enlarged `C_co` once and
   shrunk `δ_max^cb` to a common radius — is every source use genuinely covered by the
   stated packet, or does some use exceed it?
4. **The corrected normalization thresholds (defect 5).** Verify that
   `(C_T+C_Δ')η < 1/2` (not `C_Δ'η < 1/2`) is what the `a = Δ'(I)` inversion needs, and
   likewise for `Υ'`; check the degree-2/3 constants `C_2, C_3` against
   `tex:2803-2829`.
5. **`K` (§3) and `η_K` (§4).** Recompute the finite expressions. Every entry of the
   `η_K` minimum: defined? positive? actually sufficient for the step it guards
   (including `e_sel` with the EXTCB-1 close-idempotent enlargement, `e_H`, `e_ext`,
   the Neumann conditions, and the `1/4` triggers)? Any circularity (a threshold
   defined via a constant whose own admissibility needs that threshold)?
6. **The finish (§5).** Check (5.1)–(5.2): the `ε_PRH < 1/2` gate, the `4Kη` bound,
   `η_K ≤ (24K)^{-1}` and `≤ 1` used consistently, and the PRH constant `2√2` composing
   to `(K+4√(2K))`.
7. **Honesty of the rigour caveat (§5) and defect register (§6).** Does the artifact
   anywhere overclaim (numerical constants, af-validation, byte-verbatim import)? Is
   the D-audit scope statement accurate to `AUDIT-W74F-D-ALMOSTIDEMP.md`'s own residual
   register?

## Deliverable

Write exactly ONE file:
`docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-G-KLEDGER.md`

1. `SHA CHECK:` line.
2. Per-section verdicts (symbol table, reset verification, normalizations, K, η_K,
   finish, honesty): `VALID` / `VALID-WITH-CORRECTIONS` (state exactly) / `INVALID`
   (exhibit the failure: the missing symbol, the failing inequality, the locus).
3. **Overall verdict** + one-paragraph bottom line: is the relative ledger CLOSED (no
   dangling symbol/threshold, no dimension/block dependence), yes or no; what exactly
   remains open for Route F.
4. **Registry-impact note:** what should be codified and at what statuses (e.g. a
   ledger lemma; whether lem-thmainext-conditional's conditional framing should be
   restated), and whether any existing contract needs amending. Quote exact text for
   any amendment.
5. Every check performed that PASSED.

## Rules

Fresh eyes; exhibit failures explicitly; no co-authoring beyond stating what a
correction must say; write ONLY the verdict file; no `git` commands.
