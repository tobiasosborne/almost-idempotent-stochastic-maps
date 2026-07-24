# BRIEF — W74F-H (wave 3b): extract the Stage-1 split packet and repair the K-ledger (aism-xpxk)

You are a FRESH PROVER. The hostile verifier of the wave-3 K-ledger
(`VERDICT-W74F-G-KLEDGER.md`) returned **INVALID** for exactly ONE reason: the MAIN-CB
Stage-1 `lem_nontriv_projection` split construction has no named universal coefficient
or threshold, so the reset verification does not cover its raw packet and `η_K` lacks
one guard term. Your job: **extract that packet rigorously and produce the corrected
ledger delta.** You are NOT a verifier; a separate fresh hostile verifier will attack
your output.

## Primary source (verify FIRST)

`refs/kitaev-2405.02434/approximate_algebras.tex` — `sha256sum` must equal
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`.

Read YOURSELF, in this order:
1. `lem_nontriv_projection` and its full construction, `tex:915-969` (statement at
   `tex:931-943`): the approximate-unitary/topological argument producing a nontrivial
   `O(ε)`-projection in any `ε`-C*-algebra of dimension `> 1`.
2. Its Stage-1 use, `tex:1414-1434`: the fresh projections `P′, P″`, the induced
   two-dimensional commutative split inclusion `v_comm^(2) : ℂ² → 𝒮_{P_m}` at
   `tex:1419-1425`, and the Stage-1 merge at `tex:1426` — BEFORE any compression or
   reset applies.
3. The failed target it must repair: `LEDGER-W74F-G-K.md` §§0–2, 4 and
   `VERDICT-W74F-G-KLEDGER.md` (the INVALID sections quote the exact defect and a
   sufficient correction shape).

## Deliverable 1 — the Stage-1 packet (the mathematics)

Prove, from the printed construction, a statement of the shape the verifier demands:

> There are universal `C_split ≥ 1` and `e_split > 0` such that whenever the current
> corner algebra has defect `ε_X ≤ e_split` and dimension `> 1`,
> `lem_nontriv_projection` and the two induced commutative split inclusions at
> `tex:1419-1425` have ALL raw defects (projection defects, inclusion/homomorphism
> defects, unit defects, lower bounds) at most `C_split·ε_X`, with the required
> nonvanishing conclusions.

Requirements:
- Constants independent of `dim 𝒜`, the amplification level, block count, block
  dimensions, and the stage index. Say exactly where each independence comes from.
- The amplified/extended versions: Stage 1 runs inside the extended setting — state
  whether the packet's defects are extended (all-levels) bounds and why (the split
  inclusion is a level-one object; its amplifications are `I_n ⊗ ·`; use the isometric
  amplification argument, `tex:1475`, not entrywise sums).
- If the printed `tex:915-969` construction hides any additional universal input
  (functional-calculus radius, Neumann threshold), NAME it and put it in the packet.
- DECOMPOSITION FIRST: if the packet does not fall in one piece, split it into named
  sub-claims and prove what you can; a scoped residual beats a hand-wave.

## Deliverable 2 — the corrected ledger delta (the bookkeeping)

Starting from the verifier's sufficient correction, verify it against YOUR packet:

1. `C_main := max{C_co, C_split}`, `L := C_main(1 + c_0^cb)`,
   `C_pre := 2L²·max{1, C_ext, C_merge}`; add `e_split/C_pre` to the `ε_E` guard and
   `e_split/(C_pre·C_A)` to the `η_K` minimum (or an equivalent named common MAIN
   radius — if you choose the alternative, define it exactly).
2. Re-verify the reset argument (LEDGER §2) with the Stage-1 packet included: every
   pre-extension/merge raw packet — compression-transfer packets AND the fresh split
   packet — bounded by `L²ε`, below `δ_max^cb`, with no block-count factor. State the
   corrected (2.2)–(2.5) chain in full.
3. Restate the two corrected honesty sentences exactly as the verdict's Honesty
   section requires (the closure claim conditional on this packet now being supplied).
4. Confirm (do not re-derive) that the `K` formula and the finish are unchanged — the
   verdict already found them VALID; your delta must not touch them.

## Rules

- Source-first; the verifier's correction shape is a HYPOTHESIS to verify, not an
  oracle — if it is insufficient (e.g. Stage 1 needs more than one new coefficient),
  say so loudly and give the correct packet.
- No overclaiming; you are the author, not the reviewer; never write
  "verified"/"validated"/"rigorous" about your own output.
- Do not touch the `K` formula, PRH, H-CB, or EXT-CB.

## Output

Write exactly ONE file:
`docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-H-STAGE1.md`
starting with `STATUS: UNVERIFIED PROVER OUTPUT`, containing: the packet proof, the
corrected ledger delta, a constant ledger (each constant, producing inequality,
independence), hypothesis hygiene, and a LOUD defect register. Do not create/edit any
other file; no `git` commands.
