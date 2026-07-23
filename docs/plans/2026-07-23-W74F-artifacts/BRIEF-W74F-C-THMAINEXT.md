# BRIEF — W74F-C: decompose `th_main_ext` + the universal-constant ledger (aism-2r3m)

You are a FRESH STRATEGIST-PROVER working directly against a byte-verified source. This is
the **principal blocker** of the whole route. Your objective function is **DECOMPOSITION**,
not heroics: this project's standing directive is that the deliverable of an attack on a
hard theorem is a *fully scoped* set of lower-complexity pieces, each with a pinned
statement, an honest price, and a verified interface — not a triumphant one-shot proof and
not a pile of activity. You are NOT a verifier and must not self-certify.

## Source (ground truth, local, byte-verified)

`refs/kitaev-2405.02434/approximate_algebras.tex` — Kitaev, "Almost-idempotent quantum
channels and approximate C*-algebras", arXiv:2405.02434v2. SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. Cite by **tex line
number** with verbatim quotes. Never paraphrase the source from memory.

Companion (context, re-derive rather than trust):
`docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md` (the hostile audit that
identified this blocker; see its Q2, Q3 and Correction ledger).

## The target

**`th_main_ext`** at `tex:1538-1540`:

> For any finite-dimensional extended `ε`-C*-algebra `𝒜`, there exist a C*-algebra `ℬ` and
> an extended `O(ε)`-isomorphism `v : ℬ → 𝒜`. (The implicit constant in `O(ε)` does not
> depend on `𝒜` or its dimensionality.)

Its proof occupies `tex:1542-1557` and is an **adaptation outline**: it says δ-projections
extend "straightforwardly", that compression maps and subspaces extend, that the
one-dimensional-projection Hilbert-space structure "satisfies essentially the same
equation", that `cor_improvement` (error reduction) "should be adapted", and that the
arguments of `sec_proof_main` "require only trivial modifications". The W73b audit's
verdict: **it does not prove that one single map carries ALL the uniform amplified bounds**,
which is exactly what the downstream `th_factorization` consumes. The audit also found a
typo at `tex:1551-1555`: the extended inner-product estimate is printed without squares and
does not imply the norm comparison that follows; the corrected form is

  `| ⟨X,X⟩ − ‖X‖_{n,1}² | ≤ O(δ+ε)·‖X‖_{n,1}²`.

Read `th_main` at `tex:460-462` and the informal proof-strategy discussion that follows it
(incremental construction of `ℬ`, nontrivial δ-projections via approximate unitary groups /
Lefschetz–Hopf, merging `cor_merge_sum`, extension `lem_extension`, error reduction
`cor_improvement`) — the extended theorem is an amplification of exactly that machine.

## What you must deliver

### 1. The decomposition (the primary deliverable)

Produce the explicit list of **amplified lemmas** that `th_main_ext` actually requires, at
minimum covering: δ-projections and their `I_n ⊗ P` extensions; compression maps
`Co_{P,Q}` and the subspaces `𝒮_{P,Q}`; one-dimensional projections and the induced
Hilbert-space structure (`lem_PQ_Hilb`, `(1dQ_ip)`, `(1dQ_ip_ext)`, `(1dQ_ip_norm_ext)`);
the `Ha^Q_{P,R}` maps and equations `(Ha_dag)`, `(Ha_prod)`; the approximate-diagonal
machinery (`lem_approx`, `lem_approx_ext`, `prop_inc_ext`); merging (`cor_merge_sum`);
extension (`lem_extension`); error reduction (`cor_improvement`); and the assembly in
`sec_proof_main`. Locate each in the tex yourself and correct my list where it is wrong or
incomplete — establishing the true dependency set is part of the job.

For **each** node give:

- a **one-line contract**: the precise amplified statement, quantified over the
  amplification level `n ≥ 1`, in the form it must hold to be consumable downstream;
- its **dependency edges** (which other nodes it imports);
- the **exact source** of its uniform-in-`n` constant — the specific mechanism that makes
  the bound independent of `n`, `dim 𝒜`, the number of blocks, and the block dimensions;
- a **classification**:
  - **(a) ESTABLISHED** — the printed argument genuinely proves the extended statement;
    cite the lines.
  - **(b) MECHANICAL** — a repeat of the unamplified proof with `𝒜 ⇝ 1_{M_n} ⊗ 𝒜`, valid
    for a reason you state explicitly (e.g. `P ↦ I_n ⊗ P` commutes with involution and
    product and preserves the norm, so `1_{M_n} ⊗ 𝒜` is itself an `ε`-C*-algebra with the
    *same* `ε`). "Straightforward" is not a reason; the reason must be checkable.
  - **(c) GAP** — a genuine gap requiring new proof. For each gap: say what breaks, what
    shape of argument would close it, and what its price is.

The classification is the point. A node marked (b) must come with the sentence that makes
it mechanical; a node marked (c) is a piece of real mathematics we will then attack.

### 2. The `tex:1551-1555` correction, proved

State the corrected inner-product estimate, prove it (or exhibit why it fails), and check
that the norm comparison the paper draws from it — `‖X‖_Euc = √⟨X,X⟩` equals `‖X‖` up to a
`1 ± O(ε+δ)` factor — genuinely follows from the corrected form. This is a small, sharply
defined, high-value target: do it properly.

### 3. The universal-constant ledger (residual item 2)

Thread one ledger end-to-end through the chain that `th_factorization` rests on:
functional calculus (`θ(2Φ−1)`, `tex:2171-2179`, valid for `η < 1/4`) → approximate-algebra
estimates → error reduction → tensor extension → CP-ization → normalization. For each step
record: the constant it contributes, what it depends on, and whether that dependence is
dimension-free. Deliver a single existential `K` and a single `η_K > 0` if the chain
supports it — **a numerical value is NOT required, universality IS**. Any step where a
constant could silently acquire dependence on `dim ℋ`, `dim ℬ`, the number of simple
summands `m`, a block dimension `dim ℒ_j`, or the amplification level `n` must be called
out explicitly, even if you believe it is fine.

Note the paper's own convention, at `tex:458`: "each instance of big-O or similar notation
stands for a concrete function, not depending on any additional data" — so universality is
*claimed*; your job is to determine whether it is *earned*, step by step.

### 4. A prioritized attack plan

Rank the (c)-nodes by (difficulty × load-bearing weight) and say which one you would attack
first and with what mechanism. Flag any node where you suspect the theorem might actually be
**false** at the claimed uniformity — that would be the most valuable finding in this wave,
and you should say so plainly rather than softening it.

### 5. A defect register

Everything you could not close; every place you had to guess what the author meant; every
place where the extended statement you wrote down is *stronger* than what the source
sketches (that is where the real risk lives).

## Rules of engagement (repository law — non-negotiable)

- **Byte-verbatim provenance**: every claim about the source is a quoted line with its tex
  line number. If it is not in the source, say so — never fill a gap from memory.
- **No overclaiming**: this wave produces a *decomposition*, not a proof. Do not label
  anything "verified"/"validated"/"rigorous". Non-rigorous steps must say so in the open.
- **Decomposition over volume**: five honestly-scoped nodes beat twenty vague ones. Do not
  pad. Do not report activity as progress.
- **Do not attempt the whole theorem.** If, in the course of scoping, you actually prove a
  (c)-node, put the proof in an appendix and keep the decomposition clean.

## Output

Write your report to exactly ONE file:

`docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md`

Do **not** create, edit, move or delete ANY other file in the repository. In particular do
not touch `definitions/`, `argument/`, `report/`, `runs/`, `.beads/`, `.frontier/`, `refs/`,
or any other agent's artifacts, and do not run any `git` command. Start the file with a
`STATUS: UNVERIFIED STRATEGIST OUTPUT` line.
