# BRIEF — W74F-G (wave 3): the unconditional K/η_K ledger for Route F (aism-xpxk)

You are a FRESH PROVER. Your job: turn the CONDITIONAL universal-constant ledger of the
Route F factorization chain into an UNCONDITIONAL one, now that its two premise nodes
are closed. You are NOT a verifier; a separate fresh hostile verifier will attack your
output. Flag loudly anything you cannot close.

## Context and inputs

Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`; verify
`sha256sum` = `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb` first.

The state of the chain (read in this order, source-first where you doubt anything):

1. `docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md` — §5 defines the
   conditional `K` (5.1) and `η_K` (5.2); §5.1 is the step-by-step ledger table; §6
   Priority 3 scopes exactly this job. Hostile-verified VALID.
2. `docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-E-HCB.md` +
   `VERDICT-W74F-E-HCB.md` — H-CB closed: `C_H = 4000c`, `e_H = 1/(10000c)`, `c` the
   max of the sanctioned COMP-CB/COL-HILB constants and inverse threshold
   (VALID-WITH-CORRECTIONS; corrections recorded, coefficient-neutral).
3. `docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-F-EXTCB.md` +
   `VERDICT-W74F-F-EXTCB.md` — EXT-CB closed:
   `C_ext = C_merge[1 + 5C_H + 20C_app(C_H+1)]`, threshold (1.8) plus the EXTCB-1
   `e_sel` enlargement (close-idempotent range identifications).
4. `docs/plans/2026-07-23-W74F-artifacts/AUDIT-W74F-D-ALMOSTIDEMP.md` — the
   `th_almost_idemp` interface: `ε_AI(η) = O(η)` explicit, `10η` associativity.
5. `docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-B-DIAGONAL.md` — the repaired
   norm-one diagonal (block-count-free) used by APPROX-CB and both CP-izations.

## The deliverable

A single closed relative-constant chain with NO dangling symbol and NO dangling
threshold:

1. **Symbol table.** One named symbol per universal coefficient actually appearing in
   the pipeline: functional calculus (`C_θ`), approximate-algebra (`C_A`, `η_A`), error
   reduction (`C_app`, `C_inc`, `δ_max^cb`, `c_0^cb`), tensor extension (`C_co`,
   `C_col`, `C_H`, `e_H`), extension/merge (`C_merge`, `C_ext`, `e_ext`, `e_sel`), main
   assembly (`C_E`, `ε_E`, `C_pre`), factor maps (`C_T`), CP-izations and
   normalizations (`C_Δ'`, `C_Δ`, `C_Υ'`, `C_Υ`, `C_2`, `C_3`), final (`K_ΔΥ`,
   `K_mult`, `K_ΥΔ`). For each: the producing inequality (source locus or wave-2
   artifact equation number) and its (absent) dependence on `n`, `dim`, block data.
2. **The reset verification.** The MAIN-CB induction resets errors after every binary
   extension/merge (DECOMP §3 MAIN-CB). Verify, with one common inequality, that every
   pre-reset error lies below `δ_max^cb` — the previously "unexpanded raw-step
   thresholds" defect (DECOMP §7 item 10). This is the one place a genuinely new
   inequality may be needed; if it fails for the natural threshold choice, say so
   LOUDLY and give the corrected threshold ordering.
3. **`C_E` and `ε_E` made explicit** as expressions in the tensor-extension constants
   (this is what MAIN-CB earns once H-CB/EXT-CB are inputs).
4. **Evaluate (5.1)–(5.2)**: `K` and `η_K` as fully explicit RELATIVE expressions in
   the symbol table (absolute decimals are impossible — the source's big-O constants
   are unnamed; do NOT invent numbers). Every entry of the `η_K` minimum must be
   defined, positive, and threshold-complete (including `e_sel`).
5. **The conditional finish, restated unconditionally-in-the-gaps:** the Route F chain
   now gives `‖Q−E‖ ≤ (K+4√(2K))√η` for `η ≤ η_K`, at the `proved-mod-audit` rung,
   resting on the named artifact set. State the exact rigour caveat (nothing here is
   af-validated or L0-rigorous; `th_almost_idemp`'s long identities `tex:2239-2723`
   were audited, not re-proved line-by-line — record what the D-audit's own scope
   says).
6. **Defect register.** Anything you could not close, every judgment call, every place
   the source's unnamed constant forces a symbolic (rather than numeric) entry.

## Rules

- Source-first: re-check each ledger row's locus yourself; do not copy DECOMP §5.1
  uncritically — its rows predate the H-CB/EXT-CB closures.
- No overclaiming: `proved-mod-audit`-grade inputs stay flagged as such; never write
  "rigorous"/"verified" about your own output.
- No new mathematics beyond the reset verification (item 2) — if you find yourself
  proving a new operator estimate, STOP and record it as a named gap instead.

## Output

Write exactly ONE file:
`docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md`
starting with `STATUS: UNVERIFIED PROVER OUTPUT`. Do not create/edit/move/delete any
other file; no `git` commands.
