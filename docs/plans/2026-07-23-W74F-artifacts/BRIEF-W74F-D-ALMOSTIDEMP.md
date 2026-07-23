# BRIEF — W74F-D: full hostile audit of `th_almost_idemp` (aism-7gqw)

You are a FRESH, HOSTILE AUDITOR. Your job is to try to **BREAK** a published proof.
Finding a gap, a wrong constant, a hidden dimension dependence, a misapplied hypothesis, or
a diagrammatic equality that does not hold is a **BIG SUCCESS**. Confirming a step without
finding a flaw is acceptable only if you genuinely attacked it. You take nobody's word for
anything — not the author's, not a previous auditor's, not mine.

## Source (ground truth, local, byte-verified)

`refs/kitaev-2405.02434/approximate_algebras.tex` — Kitaev, "Almost-idempotent quantum
channels and approximate C*-algebras", arXiv:2405.02434v2. SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. Cite by **tex line
number** with verbatim quotes.

Context (a prior audit; re-derive rather than trust — its scope explicitly EXCLUDED what
you are now doing): `docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md`.

## The target and why this audit exists

`th_factorization` (`tex:2730`) — the theorem an entire new proof architecture wants to
import — rests on exactly two big results: `th_main_ext` (audited separately, not your
problem) and **`th_almost_idemp`** (`tex:2192`), whose proof runs from `tex:2208` through
roughly `tex:2723`, including a long sequence of **diagrammatic equalities**.

The prior audit traced this theorem's dimension-free *mechanism* — the idempotent
`Φ̃ = θ(2Φ−1)` built by functional calculus in the Banach algebra of completely bounded
maps (`tex:2171-2179`), with the Taylor series used only for `η < 1/4`, so the step depends
on a scalar power series and the cb norm rather than on a matrix-coordinate expansion — and
checked the *interfaces* used downstream (the approximate-associativity estimates at
`tex:2198-2235`). It **did not** independently re-prove the diagrammatic equalities at
`tex:2239-2723` with explicit constants. That is your entire job.

## What you must deliver

1. **A per-block verdict ledger over `tex:2239-2723`.** Partition the proof into its
   natural blocks (each displayed equality / diagram / estimate, grouped sensibly), and for
   each block emit a row:
   `tex-locus | what is claimed | VALID / VALID-WITH-CORRECTIONS / INVALID | the explicit constant | what it depends on`.
   A verdict without an argument is worthless; give the argument, briefly, for every row.
2. **Every constant made explicit.** Wherever the source writes `O(η)`, `O(δ)`, `O(ε)` or
   similar, determine the concrete function it stands for at that step (the paper's own
   convention at `tex:458` says each big-O "stands for a concrete function, not depending on
   any additional data" — hold it to that) and record it. Where the constant cannot be
   extracted from the printed argument, say so — that is a finding, not a failure.
3. **The dimension-freedom attack.** For every step, ask: could this constant depend on
   `dim ℋ`, on the number of simple summands, on a block dimension, or on the amplification
   level `n`? Attack the diagrammatic manipulations specifically — diagram calculus is where
   an innocuous-looking contraction can hide a dimension factor (a normalization by
   `dim ℱ`, a trace where a normalized trace was meant, a sum over a basis whose size grows).
   Any such dependence is the highest-value finding available in this wave; hunt for it.
4. **Hypothesis tracking.** Which properties of `Φ` are actually used where: UCP,
   `‖Φ²−Φ‖_cb ≤ η`, finite-dimensionality, unitality, the `η < 1/4` functional-calculus
   threshold? Flag any step that quietly uses a property not in the hypotheses, and any
   place where an *approximate* identity is used as if *exact*.
5. **The interface to `th_factorization`.** State precisely what `th_almost_idemp` delivers
   — that `𝒜 = Img Φ̃` with the Choi–Effros product `Z ⋆ W = Φ̃(ZW)` is an extended
   `O(η)`-C*-algebra — and confirm (or refute) that the *extended* (tensor-amplified) form
   is what the proof establishes, since `th_factorization` at `tex:2749` consumes it through
   `th_main_ext`, which needs the extended version. A mismatch here would be decisive.
6. **Counterexample attempts.** For at least the two or three steps you judge weakest, try
   to construct an explicit small counterexample (a `2×2` or `ℂ ⊕ ℂ` instance). Report what
   you tried even when it fails to break the step — a failed attack is evidence, and a
   successful one is the finding of the wave.
7. **A residual register.** What remains unchecked after your pass, and what it would take
   to check it.

## Rules of engagement (repository law — non-negotiable)

- **Byte-verbatim provenance**: every claim about the source is a quoted line with a tex
  line number. Never fill a gap from memory of the literature.
- **Hostility is the job.** Do not smooth over a step because the theorem is probably true.
  "Probably fine" is not a verdict; either you checked it or you record it as unchecked.
- **Universality is the deliverable.** A constant left as an unevaluated universal is fine;
  a constant with a hidden dimension dependence is fatal and must be called out loudly.
- **No overclaiming**, in either direction: do not declare the theorem proved, and do not
  declare it broken without an exhibited defect.

## Output

Write your report to exactly ONE file:

`docs/plans/2026-07-23-W74F-artifacts/AUDIT-W74F-D-ALMOSTIDEMP.md`

Do **not** create, edit, move or delete ANY other file in the repository. In particular do
not touch `definitions/`, `argument/`, `report/`, `runs/`, `.beads/`, `.frontier/`, `refs/`,
or any other agent's artifacts, and do not run any `git` command. Start the file with a
`STATUS: UNVERIFIED AUDITOR OUTPUT` line.
