# BRIEF — W74-F wave 1 BATCHED HOSTILE VERIFIER

You are a **FRESH, HOSTILE VERIFIER**. You did not write any of the documents below and you
owe their authors nothing. **Finding a gap, a wrong constant, a false lemma, a hidden
dimension dependence, a misquoted source line, or an unstated hypothesis is a BIG
SUCCESS** — it is the outcome this project most values. Confirming a target without
finding a flaw is acceptable only if you genuinely attacked it, and you must show the
attack.

You are the gate: nothing in this batch enters the repository's registry unless it clears
you. The orchestrator performs no mathematical judgment — your verdicts are the record.

## The batch (four independent targets, all in `docs/plans/2026-07-23-W74F-artifacts/`)

| target | document | its brief (what it was asked to do) |
|---|---|---|
| **A** | `PROOF-W74F-A-PRH.md` | `BRIEF-W74F-A-PRH.md` |
| **B** | `PROOF-W74F-B-DIAGONAL.md` | `BRIEF-W74F-B-DIAGONAL.md` |
| **C** | `DECOMP-W74F-C-THMAINEXT.md` | `BRIEF-W74F-C-THMAINEXT.md` |
| **D** | `AUDIT-W74F-D-ALMOSTIDEMP.md` | `BRIEF-W74F-D-ALMOSTIDEMP.md` |

Each was produced by a separate fresh worker that could not see the others. Read each
target **against its own brief** (did it deliver what was asked, or something easier?) and
against the ground truth below. If a target file is missing or truncated, say so and move
on — report `ABSENT` rather than inventing a verdict.

## Ground truth

- `refs/kitaev-2405.02434/approximate_algebras.tex`, SHA256
  `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. **Every claim any
  target makes about the paper must be checked against the actual line.** A misquoted or
  misnumbered tex citation is a defect, and a *silently shifted* statement is a serious one.
- `docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md` — the prior audit that
  defined this wave's targets. It is **not** an oracle: if a target contradicts it and is
  right, say so.

## Per-target hostile checklist (attack at least these; do not stop there)

### A — PRH

1. The conversion `‖MA − I_k‖_{∞→∞} ≤ ε ⟹ Σ_i μ_s(i)(1 − a_{is}) ≤ ε/2`. This is the one
   step turning an operator norm into a one-sided mass statement. Is the factor 2 earned?
   Does it use that the rows of `MA` are probability vectors — and is that true here?
2. Core disjointness. `λ < 1/2` is claimed to force the `C_s` disjoint. Check the boundary
   (`a_{is} = 1 − λ` exactly, `λ = 1/2` exactly, `k = 1`, `ε` at the threshold).
3. `C_s ≠ ∅`. Markov gives `β_s ≤ λ`; does `β_s ≤ λ < 1` really force a nonempty core, and
   what happens if `μ_s(C_s) = 0` degenerately?
4. `N Â = I_k` **exactly** — the identity the whole construction hangs on. Verify it
   entrywise, including rows outside every core.
5. The final assembly `‖AM − E‖ ≤ 4λ`. Are the three pieces (conditioning, in-core rows,
   out-of-core rows) each bounded as claimed, and is taking the **max over rows** (not a
   sum) legitimate for the `∞→∞` norm? A hidden sum over `k` or `n` here is fatal.
6. **The constant.** Confirm or refute the value the target settles on. Check whether the
   two published derivations (`2√2` vs `3`) actually prove the same statement.
7. The `ε = 0` endpoint: does the construction return `AM = E` exactly?
8. The sharpness claim, if any: does the exhibited family really force `≳ √ε` **for every
   stochastic idempotent** `E`, or only for the constructed one? This is a favourite place
   to overclaim. Note also that op-classical's known `√η` sharpness does **not**
   automatically transfer to PRH's `√ε` — flag any conflation.

### B — the diagonal repair

1. The claimed counterexample to the printed direct-sum formula at `tex:1254`: reproduce it
   yourself. Does the printed formula really fail, and is the failure the one described?
2. The repaired diagonal: are **both** identities (centrality and `Σ_j A_j B_j = I`) exact,
   or only approximate? Approximate centrality would silently reopen the flaw.
3. Is the construction **finite**, or does it hide a Haar integral where the argument needs
   a finite sum? If discretized, are the vanishing-moment conditions actually proved?
4. **Universality.** Is the norm bound independent of the number of blocks, the block
   dimensions, and `dim 𝒜`? Hunt specifically for a factor that grows with the number of
   summands — this is exactly where the paper's own approximate-setting construction fails.
5. Which algebra's diagonal is used at each site — the exact C*-algebra `ℬ`, or the
   approximate `𝒜`? A diagonal for `𝒜` would be a much stronger (and probably false)
   claim. Check every use site for this substitution.
6. The re-proved CP-ization at `tex:2786-2796`: is positivity genuinely established, with
   unitality preserved? Are the constants unchanged downstream?
7. Is the use-site ledger **complete**? Grep the source yourself for consumers of the
   diagonal / centrality / normalization the target may have missed.
8. Confirm no cone-projection step survives anywhere in the repaired chain.

### C — the `th_main_ext` decomposition

1. **Under-scoping is the main risk.** Is the decomposition *complete* — does closing every
   listed node actually prove `th_main_ext` at the strength `th_factorization` consumes?
   Name anything missing.
2. Every node marked **(b) MECHANICAL** must carry a checkable reason. "Straightforward",
   "analogous", "the same argument works" are **not** reasons; re-classify any such node as
   (c). Attack the (b) list hardest: it is where an outline gets laundered into a proof.
3. Every node marked **(a) ESTABLISHED** must cite lines that genuinely prove the
   *extended* (tensor-amplified) statement, not merely the unamplified one.
4. Are the stated contracts uniform in `n`? A contract quietly quantified for fixed `n`
   is worthless downstream.
5. The corrected `tex:1551-1555` estimate: is the squared form proved, and does the norm
   comparison the paper draws really follow from it?
6. **The constant ledger.** Walk it end to end and try to break it: find one step where the
   constant could depend on `dim ℋ`, `dim ℬ`, the number of summands `m`, a block dimension,
   or `n`. Check in particular the error-reduction step (`cor_improvement`), where a
   `δ`-independent output constant is claimed from a `δ`-dependent input.
7. If the target claims the theorem may be **false** at the claimed uniformity: is that
   supported by an explicit obstruction, or is it speculation? Say which.

### D — the `th_almost_idemp` audit

1. Spot-check the audit's verdicts by re-deriving at least three of its blocks yourself,
   including at least one it marked VALID. An auditor that rubber-stamps is a defect.
2. Are the extracted constants correct, and are the dimension-independence justifications
   real arguments rather than assertions?
3. The functional-calculus step (`tex:2171-2179`) and the `η < 1/4` threshold: is the
   convergence argument genuinely cb-norm-level and dimension-free?
4. The interface claim: does the proof establish the **extended** (tensor-amplified) form
   of the Choi–Effros algebra structure, which `th_factorization` consumes via
   `th_main_ext`? A mismatch here would be decisive — check it directly.
5. Any block the target left unchecked: is it load-bearing? Unchecked-but-load-bearing is a
   finding.

## Cross-target checks (do these last, and do not skip them)

- **Consistency of `K` and `η₀`.** A, B, C and D each touch the constant chain. Do their
  conventions agree? Any inconsistency in what `K` denotes, or in the smallness threshold,
  is a defect of the batch even if each document is internally coherent.
- **Circularity.** Does any target's argument depend on another target's unproved output,
  or on `th_factorization` itself? Route F must not close a loop.
- **Aggregate honesty.** Does the batch, taken together, support the claim "the residual
  register items 1–6 are discharged"? Almost certainly not — say precisely which items
  remain open and what is now needed. Under-claiming here is not a virtue either: state
  exactly what *did* survive.

## Output format (strict)

Write your report to exactly ONE file:

`docs/plans/2026-07-23-W74F-artifacts/VERDICT-W74F-BATCH.md`

Begin with a verdict block, one line per target, no hedging:

```
A: VALID | VALID-WITH-CORRECTIONS | INVALID | ABSENT
B: …
C: …
D: …
```

Then, per target: the attacks you ran, what survived, what broke, and — for every
correction — the **corrected statement**, written out in full so it can be transcribed
into a registry shard verbatim. Close with a short **residual register** saying what
remains open across the whole of Route F after this batch.

Do **not** create, edit, move or delete any other file. Do not touch `definitions/`,
`argument/`, `report/`, `runs/`, `refs/`, `.beads/`, `.frontier/`, and do not run any `git`
command. Do not fix the targets' proofs for them: your job is the verdict, plus the
corrected statement where a correction is unambiguous.
