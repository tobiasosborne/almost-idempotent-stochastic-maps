# BRIEF — W74F-E (wave 2): prove or REFUTE H-CB (aism-wwur)

You are a FRESH PROVER. Your job is to **prove — or refute by explicit counterexample —
the H-CB node**: uniform-in-`n` complete column-Hilbert / operator-module estimates for
the amplified Ha-maps `1_{M_n} ⊗ Ha^Q_{P,R}`. You are NOT a verifier and you must NOT
self-certify: a separate fresh hostile verifier will attack your output. Write down what
you actually proved and flag, loudly and in a dedicated section, anything you could not
close.

## Context (orientation, not licence to hand-wave)

The project's north star is the OPEN problem `op-classical` (dimension-free stochastic
almost-idempotent stability at `√η`). Route F reduces it to an imported factorization
theorem (Kitaev, arXiv:2405.02434) whose principal theorem `th_main_ext` was found, by a
hostile audit, to have an incomplete printed proof. A verified decomposition
(`docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md` — READ IT FIRST, it is
your spec) reduced `th_main_ext` to exactly TWO gap nodes: **H-CB** (yours) and EXT-CB
(assumes yours; not your problem). H-CB is the single most load-bearing open statement in
the campaign.

Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`. Verify its integrity
first: `sha256sum` must give
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. All `tex:NNNN` loci
below refer to line numbers of that file. Read the relevant sections of the source
yourself — do not trust any summary, including this brief.

## The statement (H-CB) — pin it precisely yourself, starting from this contract

Setting: `𝒜` a finite-dimensional extended `ε`-C*-algebra (source's axioms, `tex:425`
ff. and the extended/amplified norms `‖·‖_n` of `sec` around `tex:1470-1540`);
`P, Q, R, S` are `δ`-projections; `Q` is **one-dimensional at level one**
(`dim 𝒮_Q = 1`); `e := δ + ε`. Write `T_n := 1_{M_n} ⊗ T` and
`𝒜_n := M_n ⊗ 𝒜`, `P_n := I_n ⊗ P`.

Let `h_{P,R} := Ha^Q_{P,R} : 𝒮_{P,R} → ℬ(𝒮_{R,Q}, 𝒮_{P,Q})` (definition `Ha_def`,
`tex:1140-1150`). For all `n ≥ 1`, identify
`M_n ⊗ ℬ(𝒮_{R,Q}, 𝒮_{P,Q}) ≅ ℬ(ℂ^n ⊗ 𝒮_{R,Q}, ℂ^n ⊗ 𝒮_{P,Q})` using the COL-HILB
column norms. Then a **universal** constant `C_H` and a universal smallness threshold
`e_H > 0` must give, simultaneously, for all `n ≥ 1` and `e ≤ e_H`:

1. `(h_{P,R})_n(Z)† = (h_{R,P})_n(Z†)` (exact adjointness, amplified);
2. `‖(h_{P,R})_n(Z·W) − (h_{P,S})_n(Z)(h_{S,R})_n(W)‖ ≤ C_H e ‖Z‖ ‖W‖`
   (the amplified `Ha_prod` defect);
3. the uniform unital, norm, and inverse estimates needed for
   `(h_{P,P})_n` to be an extended `C_H e`-homomorphism;
4. `(h_{P,Q})_n` and `(h_{Q,P})_n` completely `C_H e`-close to their canonical identity
   identifications.

**All constants must be independent of `n`, `dim 𝒜`, the number of simple blocks, and
every block dimension.** A bound with any `n`-, `r`-, or block-count factor is a FAILURE
of the statement, not a weaker success.

## The trap (why the source's "straightforward" is not a proof)

- At level one the source gives exact adjointness (`tex:1151-1153`) and approximate
  multiplicativity (`tex:1156-1159`), via `lem_PQ_Hilb` — which REQUIRES `Q`
  one-dimensional.
- `Q_n = I_n ⊗ Q` is NOT one-dimensional: `𝒮_{Q_n,Q_n} = M_n ⊗ 𝒮_{Q,Q}` has dimension
  `n²`. Applying the level-one lemmas to `Q_n` is INVALID.
- An entrywise proof of the product estimate sums `n` terms and risks an `n`-factor.
  **Never estimate entry by entry. Never sum over the `n` entries of a column.**

## The sanctioned starting material (what you may assume)

- The source's extended `ε`-C*-algebra axioms and amplified norms (`tex:425` ff.,
  `tex:1470` ff.), and the isometric inclusion `X ↦ I_n ⊗ X` (`tex:1475`).
- P-TENS and COMP-CB (persistence and amplified compression) as in DECOMP §3 — their
  amplification is established/mechanical there; you may use their contracts with a
  named constant `C_co`. If you doubt one, prove it — do not silently assume more.
- COL-HILB **in its corrected squared form** (DECOMP §4, eq. (4.1)):
  `|⟨X,X⟩_n − ‖X‖²_{n,1}| ≤ C(δ+ε)‖X‖²_{n,1}` — the printed `tex:1551-1553` display
  omits the squares; use the corrected version, whose proof is in DECOMP §4.2 and does
  not depend on H-CB.
- The level-one Ha facts (`tex:1140-1159`).

Everything else you must prove.

## The suggested attack shape (improve or replace it if it is wrong)

From DECOMP §6, Priority 1:

1. Prove from `Ha_def`, inside a single rectangular corner of `M_{2n} ⊗ 𝒜`, that
   `(h_{P,R})_n(Z)·X` is `O(e)‖Z‖‖X‖_Euc`-close to `Z · X` (column action ≈ module
   multiplication).
2. Use corrected COL-HILB to convert this to a uniform operator-norm estimate.
3. Test operator norms on arbitrary unit columns and use associativity in
   `M_{2n} ⊗ 𝒜` to prove the product defect (2) without expanding matrix entries.
4. Obtain the special-map bounds (3)–(4) and the inverse estimates by a Neumann
   argument at the operator level.

**DECOMPOSITION FIRST (standing user directive):** if H-CB does not fall in one piece,
split it into named sub-lemmas (e.g. HCB-1 column action, HCB-2 norm conversion, HCB-3
product defect, HCB-4 Neumann/special maps), prove what you can, and state exactly which
sub-lemma remains open and why. A fully scoped partial decomposition with one honest
residual gap is worth more than a hand-wave over the whole.

## The refutation branch (equally valuable — search before you assemble)

DECOMP §6 flags H-CB as the diagnostic node for failure of `th_main_ext`'s claimed
uniformity: "if an extended approximate C*-algebra can have column norms for which left
multiplication is not uniformly controlled by the corrected scalar inner product, H-CB —
and therefore th_main_ext at the claimed uniformity — may be false." Spend genuine effort
hunting a counterexample family (constants growing with `n`) BEFORE committing to the
assembly. If you find one: exhibit it fully explicitly, verify the growth, and mark the
report `ESCALATION REQUIRED: H-CB REFUTED` at the top. A true counterexample re-routes
the whole campaign and is a BIG SUCCESS, not a failure.

## What you must deliver

1. **A rigorous proof of (1)–(4) with one explicit universal `C_H` and threshold `e_H`**
   — every inequality justified, every norm identified (level-`n` operator norm vs
   column-Euclidean norm vs level-one norm; state each identification you use), OR
2. **a counterexample** as above, OR
3. **a fully scoped decomposition** with the proved sub-lemmas and the named residual
   gap(s).

Plus, in all cases:

4. **Constant ledger.** Every constant you introduce, with the inequality that produced
   it and its dependence (must be: none) on `n`, `dim 𝒜`, block data.
5. **Hypothesis hygiene.** Exactly where one-dimensionality of level-one `Q` is used;
   exactly where the `ε`-C*-axiom is applied and at which amplification level.
6. **A defect register.** Every step you could not close, every place you strengthened
   or weakened the contract, every constant you could not pin. An honest register is
   worth more than a clean-looking proof.

## Rules of engagement (repository law — non-negotiable)

- **"Runs without errors" / "looks plausible" is never a proof.**
- **No appeal to the source's own claim** that the generalization is "straightforward"
  (`tex:1555`) — that sentence is the gap you are closing.
- **Do not overclaim.** If a step is heuristic, label it heuristic in the text itself.
- **You are the author, not the reviewer.** Do not write "verified", "validated", or
  "rigorous" about your own output.

## Output

Write your report to exactly ONE file:

`docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-E-HCB.md`

Do **not** create, edit, move or delete ANY other file in the repository. In particular
do not touch `definitions/`, `argument/`, `report/`, `runs/`, `.beads/`, `.frontier/`, or
any other agent's artifacts, and do not run any `git` command. Markdown with
LaTeX-in-`$…$` is fine. Start the file with a `STATUS: UNVERIFIED PROVER OUTPUT` line
(or the `ESCALATION REQUIRED` line described above, then the STATUS line).
