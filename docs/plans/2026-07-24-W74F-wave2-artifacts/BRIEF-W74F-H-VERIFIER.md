# BRIEF — W74F-H hostile verification: attack the Stage-1 split packet + ledger delta (aism-xpxk)

You are a FRESH HOSTILE VERIFIER. You wrote none of what you read; your job is to BREAK
it. A hidden dimension factor, an unproved uniformity, a threshold that does not guard
what it claims, or a defect the packet fails to bound is a BIG SUCCESS. Reach your own
verdict from the primary source; treat NO repository document as an oracle.

## Target

`docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-H-STAGE1.md` — UNVERIFIED prover
output supplying the ONE packet the previous hostile verdict
(`VERDICT-W74F-G-KLEDGER.md`, INVALID) found missing from the Route F K-ledger
(`LEDGER-W74F-G-K.md`): universal `C_split ≥ 1`, `e_split > 0` for the
`lem_nontriv_projection` Stage-1 split construction, plus the corrected MAIN-CB reset
chain (`C_main = max{C_co, C_split}`) and the `e_split/(C_pre·C_A)` guard in `η_K`.

## Primary source (verify FIRST)

`refs/kitaev-2405.02434/approximate_algebras.tex` — `sha256sum` must equal
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. Read YOURSELF:
`lem_nontriv_projection` and its full proof (`tex:915-969`, statement `tex:931-943`),
its Stage-1 use (`tex:1414-1434`, split inclusion `tex:1419-1425`), the extended norms
and isometric amplification (`tex:1470-1480`). Then the G-verdict (for what the packet
must supply) and the target.

## Attack surface — hit hardest where the prover itself flags load-bearing expansion

1. **THE `tex:943` UNIFORM-ISOLATION EXPANSION (prover defect 3 — the #1 target).**
   The paper compresses the isolation-radius step into one sentence; the target expands
   it at (1.3)–(1.4) into a claimed dimension-free chart-radius/quotient argument. Is
   that expansion actually valid with universal constants? Is the passage to the
   quotient legitimate? Could the radius secretly depend on `dim 𝒳`? If you cannot
   confirm dimension-independence here, the packet FAILS — say so.
2. **The topological inputs (prover defect 4).** Lefschetz–Hopf, Hopf structure,
   finite-CW: is it true they introduce no analytic coefficient, and is their use as
   printed sufficient for the quantitative conclusion claimed?
3. **Exact-unit transfer (prover defect 5).** The projection is produced for the
   rectified product/unit; check (1.1) and (1.10)–(1.11) recover the original corner
   packet with only a `C_split·ε_X` loss.
4. **The all-level claim (prover defect 7).** The extended bounds rest on the four-term
   identity (1.14) + the `tex:1475` isometry. Verify no step is entrywise; verify the
   split inclusion `v_comm^(2)`'s amplifications really are `I_n ⊗ ·` of one level-one
   object.
5. **The corrected reset chain (§3).** With the packet included, is EVERY Stage-1/2/3
   pre-extension/merge raw packet now bounded by `L²ε` below `δ_max^cb`, with no
   block-count factor? Does `C_main = max{C_co, C_split}` interact correctly with the
   `C_co` producing inequalities (the G-verdict warned mere relabelling is illegal —
   check the delta does more than relabel)?
6. **The corrected `η_K` (§4).** Is `e_split/(C_pre·C_A)` the right guard (consumed
   where the reset proof needs it, no circularity)? Is the corrected minimum now
   sufficient for EVERY Route F step — i.e., is the G-verdict's sole objection actually
   discharged, and is there any OTHER unnamed coefficient you can find anywhere in the
   pipeline (one more sweep)?
7. **Scope discipline.** Confirm the artifact does not touch the `K` formula, PRH,
   H-CB, EXT-CB (the G-verdict found those VALID), and that the two honesty sentences
   match what the G-verdict required.

## Deliverable

Write exactly ONE file:
`docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-H-STAGE1.md`

1. `SHA CHECK:` line.
2. Per-section verdicts (packet statement §0, construction decomposition §1 — with the
   `tex:943` expansion called out separately, constant ledger §2, reset chain §3, `η_K`
   delta §4, scope §5/§7): `VALID` / `VALID-WITH-CORRECTIONS` (state exactly) /
   `INVALID` (exhibit the failure).
3. **Overall verdict** + one-paragraph bottom line: with this packet, is the Route F
   relative `K`/`η_K` ledger now CLOSED, yes or no; what exactly remains open.
4. **Registry-impact note:** if closed, confirm (or amend) the codification plan the
   G-verdict pre-specified (the ledger node contract + the `lem-thmainext-conditional`
   restatement — quote exact contract text you endorse); if not closed, state exactly
   what is still missing.
5. Every check performed that PASSED.

## Rules

Fresh eyes; exhibit failures explicitly; no co-authoring beyond stating what a
correction must say; write ONLY the verdict file; no `git` commands.
