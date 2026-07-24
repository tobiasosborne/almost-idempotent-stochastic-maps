# BRIEF — W74F-E hostile verification: attack the H-CB proof (aism-wwur)

You are a FRESH HOSTILE VERIFIER. You did not write the proof you are about to read, and
your job is to BREAK it. **Finding a counterexample, a gap, an n-dependent constant, or
an error is a BIG SUCCESS** — a rubber stamp is worthless. You must reach your own
verdict from the primary source; treat NO prior repository document as an oracle.

## Target

`docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-E-HCB.md` — an UNVERIFIED prover
output claiming to close the H-CB node: uniform-in-`n` complete column-Hilbert /
operator-module estimates for the amplified Ha-maps `1_{M_n} ⊗ Ha^Q_{P,R}`, with
explicit universal `C_H = 4000c`, `e_H = 1/(10000c)`, plus the claim that the
UNCONDITIONAL inverse estimate for `h_{P,P}` is FALSE (exact `ℂ⊕ℂ` counterexample) and
must be replaced by a conditional one.

## Primary source (verify integrity FIRST)

`refs/kitaev-2405.02434/approximate_algebras.tex` — `sha256sum` must give
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. Work source-first:
read `Ha_def` and the level-one Hilbert lemmas (`tex:1123-1160`), the amplification
section (`tex:1470-1557`), and the ε-C*-axioms (`tex:425` ff.) YOURSELF before reading
the proof.

Context (read AFTER the source, and do not treat as oracle): the contract being targeted
is `conj-hcb` in `argument/lemmas/conj-hcb.md`, isolated by
`docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md` (whose §4 corrected
COL-HILB estimate the proof imports as a sanctioned input — re-derive it yourself if you
doubt it).

## What the claimed proof rests on (attack surface)

1. **HCB-0** (§3): a five-term compressed-associator bound in one square `M_N ⊗ 𝒜`.
2. **HCB-1a** (§4): an exact amplified variational identity obtained by summing `Ha_def`
   algebraically. Exactness claims are favourite hiding places — check every term.
3. **HCB-1b** (§5): column action uniformly close to module multiplication. Hunt hidden
   `n`-sums: any step that estimates entries or sums over `ℓ ∈ [n]` breaks uniformity.
4. **HCB-2** (§6): exact amplified adjointness + the product defect via a whole
   rectangular associator.
5. **HCB-3** (§7): unit/norm bounds; the `ℂ⊕ℂ` counterexample to the unconditional
   inverse (§2.1 — CHECK IT: is it genuinely a counterexample to the *literal* clause,
   and is the conditional replacement genuinely what `lem_extension` at `tex:1382-1412`
   consumes?); the lower/inverse bootstrap (7.7)–(7.12) with its Neumann arguments.
6. **HCB-4** (§8): the Gram estimate (8.4)–(8.7) — the scalarization
   `Z†·Z = G ⊗ u_Q` leans on level-one one-dimensionality of `Q`; verify it is never
   applied to `I_n ⊗ Q`.
7. **The constant ledger** (§10): recompute the arithmetic chain
   (`C_as = 9c` → … → `C_H = 4000c`); check EVERY entry's claimed independence of `n`,
   `dim 𝒜`, block count, block dimensions.
8. **§2.2's negative counterexample search**: is it honest? Can YOU produce an
   `n`-growth family the prover missed? Spend genuine effort here — a refutation of
   H-CB re-routes the whole campaign and is the single most valuable possible finding.

## Deliverable

Write exactly ONE file:
`docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-E-HCB.md`

Structure:
1. `SHA CHECK:` line (pass/fail).
2. **Per-section verdict lines**: for each of HCB-0, HCB-1a, HCB-1b, HCB-2, HCB-3
   (including the §2.1 counterexample and the conditional-inverse replacement), HCB-4,
   and the constant ledger: `VALID` / `VALID-WITH-CORRECTIONS` (state them precisely) /
   `INVALID` (exhibit the breaking input or the unbridgeable gap).
3. **Overall verdict**: `VALID` / `VALID-WITH-CORRECTIONS` / `INVALID`, with a one-
   paragraph bottom line: does H-CB (in the conditional-inverse form) hold with a
   universal constant, yes or no, and what exactly remains open.
4. **Contract-impact note**: does the conditional-inverse refinement require amending
   the registered `conj-hcb` contract text, and if so, to what (quote the exact
   replacement clause)? Does it weaken what EXT-CB / `lem_extension` can consume?
5. A list of every check you performed that PASSED (so silence is never read as
   endorsement).

## Rules

- Fresh eyes only: your verdict must be derivable from the source tex + the proof text.
- If you find an error, exhibit the failing configuration explicitly — "seems wrong" is
  not a verdict.
- Do not repair the proof beyond stating precisely what a correction must say; you are a
  verifier, not a co-author.
- Do NOT create, edit, move or delete any other file; do not run any `git` command.
