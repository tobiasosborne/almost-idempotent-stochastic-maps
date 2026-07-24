# BRIEF — W74F-F (wave 2): prove or refute EXT-CB, conditional on H-CB (aism-9lb7)

You are a FRESH PROVER. Your job is to **prove — or refute — EXT-CB**, the second and
last gap node of `th_main_ext`, ASSUMING the H-CB contract as a named premise. You are
NOT a verifier and you must NOT self-certify: a separate fresh hostile verifier will
attack your output. Flag loudly, in a dedicated section, anything you could not close.

## Context

Route F reduces `op-classical` to Kitaev's factorization theorem (arXiv:2405.02434),
whose principal theorem `th_main_ext` was decomposed by a hostile-verified analysis
(`docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md` — READ IT, it is your
spec; §3 EXT-CB node and §6 Priority 2) into two gaps: H-CB and **EXT-CB** (yours).

Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`; verify
`sha256sum` = `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb` first.
Read the level-one extension argument `lem_extension` (`tex:1363-1412`), `lem_merging` /
`cor_merge_sum` (`tex:1330-1359`), `lem_approx_ext` (`tex:1508-1535`), and the level-one
selection lemmas (`tex:931`, `tex:1162-1180`, `tex:1363-1369`) yourself.

## The statement (EXT-CB) — pin it precisely yourself, starting from this contract

There are universal `C_ext < ∞` and `e_ext > 0` such that: if `e = δ+ε ≤ e_ext`,
`P, Q` are `δ`-projections in a finite-dimensional extended `ε`-C*-algebra `𝒜` with
`‖P+Q−I‖ ≤ δ`, `v : M_r → 𝒮_P` is an extended `δ`-isomorphism, `dim 𝒮_Q = 1` at level
one, and `𝒮_{P,Q} ≠ 0`, then there is ONE map `v₊ : M_{r+1} → 𝒜` which is an extended
`C_ext·e`-isomorphism. **Constants independent of `r`, `n`, and `dim 𝒜`.** The same
level-one unitary and the same four corner maps must carry every amplification level —
choosing per-`n` objects is a FAILURE.

## Named premises (assume these; consume them ONLY through their stated interfaces)

1. **H-CB** — the contract in `argument/lemmas/conj-hcb.md`, WITH the refinement of
   `docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-E-HCB.md` §§7.3–7.4 and §9
   (itself unverified; a hostile verifier is attacking it in parallel): the inverse
   estimate for `h_{P,P}` is NOT unconditional — it holds conditionally on a level-one
   lower bound/bijectivity (which `lem_extension`'s own argument establishes). Consume
   H-CB in that conditional form, and STATE EXPLICITLY, in a dedicated subsection, the
   exact list of H-CB clauses your proof uses (this insulates your work against contract
   amendments from the parallel verification).
2. **APPROX-CB** (`lem_approx_ext`, `tex:1508-1535`) and **MERGE-CB** (amplified
   `lem_merging`/`cor_merge_sum`) — classified ESTABLISHED/MECHANICAL in DECOMP §3; use
   their contracts with named constants `C_app`, `C_merge`. If you doubt a mechanical
   step, prove it — do not silently assume more.
3. Level-one `lem_PQR`, `lem_1d_proj`, `lem_add_dim` (level-one selection only — NEVER
   applied to `I_n ⊗ Q`).

## The suggested closing shape (DECOMP §3 EXT-CB node; improve or replace if wrong)

1. Use H-CB to make `h₁₁v` an extended `O(e)`-homomorphism.
2. Apply APPROX-CB with exact target `ℬ(𝒮_{P,Q})`, obtaining one exact *-homomorphism
   `μ₁₁` completely `O(e)`-close to it.
3. The level-one dimension calculation (`dim 𝒮_{P,Q} = r`) forces `μ₁₁` to be
   conjugation by one unitary `U₁ : ℂ^r → 𝒮_{P,Q}`.
4. Amplify that SAME `U₁`; use H-CB and Neumann inversion to prove the four completely
   bounded versions of `merging0h`–`merging3h` (`tex:1330` ff.).
5. Apply MERGE-CB; conclude `v₊` is an extended `C_ext·e`-isomorphism.

## Hostile checkpoints (the verifier will hit exactly these — pre-empt them)

- **No unitary chosen separately for each `n`.** One `U₁`, all levels.
- **Complete closeness of ALL FOUR corner maps**, not just `h₁₁`.
- **No dependence on the matrix size `r`** anywhere (the norm-one diagonal inside
  APPROX-CB is what prevents it — check this is genuinely where `r` would enter).
- **Exact preservation of bijectivity** of the final map.
- **Where does `μ₁₁` being conjugation-by-unitary need finite dimension / exactness?**
- **The `𝒮_{P,Q} ≠ 0` and `dim 𝒮_Q = 1` hypotheses**: where exactly are they consumed?

## DECOMPOSITION FIRST (standing user directive)

If EXT-CB does not fall in one piece, split it into named sub-lemmas (e.g. EXTCB-1
extended `h₁₁v`, EXTCB-2 exact representation, EXTCB-3 one-unitary amplification,
EXTCB-4 corner cb-bounds, EXTCB-5 merge), prove what you can, and state exactly which
sub-lemma remains open and why.

## The refutation branch

If, GIVEN H-CB, you find a genuine obstruction to a uniform EXT-CB (e.g. a family where
no single level-one unitary can carry all amplifications), exhibit it explicitly and
mark the report `ESCALATION REQUIRED: EXT-CB OBSTRUCTED` at the top — that would
challenge `th_main_ext`'s claimed uniformity and re-routes the campaign.

## What you must deliver

1. A rigorous proof with one explicit universal `C_ext` (as an expression in `C_H`,
   `C_app`, `C_merge`, and universal numbers) and threshold `e_ext`, OR a counterexample
   /obstruction, OR a fully scoped decomposition with named residual gaps.
2. **Constant ledger** — every constant, its producing inequality, its (absent)
   dependence on `r`, `n`, `dim 𝒜`, block data.
3. **Premise ledger** — the exact H-CB / APPROX-CB / MERGE-CB clauses consumed.
4. **Hypothesis hygiene** — where each hypothesis is used.
5. **A defect register** — everything you could not close; honest scope beats polish.

## Rules of engagement (repository law — non-negotiable)

- "Looks plausible" is never a proof. No appeal to the source's "only trivial
  modifications" (`tex:1557`) — that sentence is the gap.
- Do not overclaim; label heuristic steps heuristic.
- You are the author, not the reviewer: never write "verified"/"validated" about your
  own output.

## Output

Write your report to exactly ONE file:
`docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-F-EXTCB.md`

Do **not** create, edit, move or delete ANY other file; do not touch `definitions/`,
`argument/`, `report/`, `runs/`, `.beads/`, `.frontier/`, or any other agent's
artifacts; do not run any `git` command. Start the file with a
`STATUS: UNVERIFIED PROVER OUTPUT` line (after the `ESCALATION` line if applicable).
