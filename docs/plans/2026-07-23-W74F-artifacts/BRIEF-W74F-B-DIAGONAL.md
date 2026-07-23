# BRIEF — W74F-B: the exact whole-algebra diagonal repair + use-site recheck (aism-0m77)

You are a FRESH PROVER working directly against a byte-verified source. Your job is to
**repair a specific, identified flaw** in a published proof and then **recheck every place
downstream that consumed the flawed object**. You are NOT a verifier and must not
self-certify; a separate fresh hostile verifier will attack your output.

## Source (ground truth, local, byte-verified)

`refs/kitaev-2405.02434/approximate_algebras.tex` — Kitaev, "Almost-idempotent quantum
channels and approximate C*-algebras", arXiv:2405.02434v2. SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. Cite by **tex line
number** and quote verbatim whenever you make a claim about what the paper says. Never
paraphrase the source from memory.

Companion (context, itself unverified beyond its own audit protocol):
`docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md` — the hostile audit that found
this flaw. Read its Q3 section and its Correction ledger. Treat its conclusions as leads to
re-derive, not as facts.

## The flaw (as identified)

A **diagonal** for an associative algebra `𝒜` is an element `D = Σ_j A_j ⊗ B_j ∈ 𝒜 ⊗ 𝒜`
with the two exact identities

- (centrality) `Σ_j Z A_j ⊗ B_j = Σ_j A_j ⊗ B_j Z` for all `Z ∈ 𝒜`;
- (normalization) `Σ_j A_j B_j = I`.

For a finite-dimensional C*-algebra one such object is `D = ∫ dU (U† ⊗ U)` over Haar
measure on the unitary group (see the discussion around `tex:460`ff.).

At **`tex:1254`** the paper builds a diagonal for a direct sum out of per-block unitary
designs, and at **`tex:2780-2783`** it repeats that formula. The audit's finding: **the
printed direct-sum diagonal formula is false** — a Cartesian product of per-block designs
need not give a diagonal of the direct sum, because the cross-block terms do not vanish (an
exact `ℂ ⊕ ℂ` counterexample is given in the audit). The audit's proposed repair: use the
full Haar diagonal of the whole algebra, or add independent block phases/signs so that all
cross-block first moments vanish.

This matters because the diagonal's **exact centrality** is what the downstream CP-ization
argument actually needs: the audit showed the positivity claim at `tex:2786-2796` DOES go
through entrywise *given an exact central diagonal* (contrary to a sibling repo's diagnosis
that blamed approximate multiplicativity of `Δ̃`), and fails as printed because centrality
is lost.

## What you must deliver

1. **Confirm or refute the flaw yourself.** Read `tex:1254` and `tex:2780-2783` verbatim.
   State the printed formula exactly. Construct (or refute) the smallest explicit
   counterexample to the two diagonal identities for that formula. Do not take the audit's
   word for it.
2. **Prove the repair as a standalone lemma.** For an arbitrary finite-dimensional
   C*-algebra `𝒜` (a finite direct sum of matrix blocks `⊕_j M_{d_j}`), construct a
   **finite** diagonal `D = Σ_{j=1}^{J} A_j ⊗ B_j` satisfying BOTH identities **exactly**,
   with:
   - an explicit bound on whatever norm of `D` the downstream argument uses (identify that
     norm from the use sites — do not guess: the relevant quantity is typically
     `Σ_j ‖A_j‖‖B_j‖` or the projective/`⊗`-norm; say which and why),
   - the bound **universal**: independent of the number of blocks, the block dimensions,
     and `dim 𝒜`. Dimension-freedom is the whole point; a bound like `O(dim 𝒜)` is a
     failure, and the paper itself notes (around `tex:460`ff.) that naive constructions
     have exactly that defect in the *approximate* setting.
   - Finiteness: an integral over Haar measure is acceptable only if you either (a) show
     the downstream uses tolerate an integral form, or (b) discretize it (unitary
     1-design / random-sign / phase-balanced construction) with the cross-block moments
     provably vanishing. Say which route you take and prove the moment conditions.
   - Note carefully whether you need a diagonal of the **exact** finite-dimensional
     C*-algebra `ℬ` (which has one) or of the **approximate** algebra `𝒜` (which is the
     hard case the paper explicitly avoids). Getting this distinction wrong invalidates
     everything; state at each use site which algebra's diagonal is being used.
3. **A complete use-site recheck ledger.** Grep the source for every consumer of the
   diagonal, of its centrality, and of its norm-one/normalized representation — at minimum
   the neighbourhoods of `tex:1254`, `tex:2780-2783`, and the CP-ization at
   `tex:2786-2796`, plus the error-reduction argument (`cor_improvement`) which the paper
   says works "because `ℬ` does have a diagonal". For each site produce a row:
   `tex-locus | what it uses (centrality / normalization / a norm bound / finiteness) | does the repaired diagonal supply it | any constant that changes`.
4. **The CP-ization step, re-proved.** At `tex:2786-2796` the map `Δ'` is claimed manifestly
   positive. Re-derive that claim from scratch under the repaired diagonal: state the
   hypothesis it needs (the audit's finding: *centrality of an exact diagonal*, NOT exact
   multiplicativity of `Δ̃`), give the estimate with explicit constants, and confirm
   unitality is preserved (or state the unitalization cost).
5. **Item 4 of the residual register: no unproved shortcut.** Confirm explicitly that your
   repair uses **no cone-projection / nearest-CP-map step**. If you find any step that
   still needs one, state precisely the missing theorem it would require — a bound on the
   cb-norm distance to the CP cone with a universal constant, plus preservation of
   unitality and of the degree-two/three multiplicativity estimates — and flag that as an
   open blocker rather than assuming it.
6. **A defect register.** Everything you could not close; every place your repair changes a
   constant downstream; every place the printed proof needs a further edit you did not make.

## Rules of engagement (repository law — non-negotiable)

- **Byte-verbatim provenance.** Every claim about the source is a quoted line with its tex
  line number. If something is not in the source, say so — never fill a gap from memory of
  the literature.
- **Universality is the deliverable, numerical constants are optional.** A constant may be
  left as an unevaluated universal `K`; a constant that secretly depends on a dimension is
  a fatal defect and must be flagged as such.
- **Do not overclaim.** Label heuristic steps heuristic in the text. Do not write
  "verified"/"validated"/"rigorous" about your own output.

## Output

Write your report to exactly ONE file:

`docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-B-DIAGONAL.md`

Do **not** create, edit, move or delete ANY other file in the repository. In particular do
not touch `definitions/`, `argument/`, `report/`, `runs/`, `.beads/`, `.frontier/`, `refs/`,
or any other agent's artifacts, and do not run any `git` command. Start the file with a
`STATUS: UNVERIFIED PROVER OUTPUT` line.
