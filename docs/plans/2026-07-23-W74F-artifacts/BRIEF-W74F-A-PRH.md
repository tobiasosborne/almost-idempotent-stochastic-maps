# BRIEF — W74F-A: prove PRH (positive-retract hardening) standalone (aism-6m8v)

You are a FRESH PROVER. Your job is to produce a **complete, rigorous, self-contained
proof** of the Positive-Retract Hardening lemma, with every constant explicit. You are
NOT a verifier and you must NOT self-certify: a separate fresh hostile verifier will
attack your output. Write down what you actually proved and flag, loudly and in a
dedicated section, anything you could not close.

## Why this lemma matters (context, not licence to hand-wave)

The project's north star is the OPEN problem `op-classical`: there exist universal,
dimension-free constants `η₀, C > 0` such that every row-stochastic `Q` with
`‖Q²−Q‖_{∞→∞} ≤ η ≤ η₀` admits a **stochastic idempotent** `E` with
`‖Q−E‖_{∞→∞} ≤ C·√η` (the exponent 1/2 is known sharp).

A new architecture ("Route F") reduces `op-classical` to two ingredients: an imported
factorization theorem (Kitaev arXiv:2405.02434, currently under separate audit — NOT your
problem) and **this lemma**. PRH is the only step of Route F that belongs to this project
rather than to the literature, and it is valuable *regardless* of whether the import
survives: it reduces `op-classical` to the clean statement "a positive approximate retract
exists". So prove it on its own terms, assuming nothing about Kitaev.

## The statement to prove (pin it precisely yourself)

Let `k, n ≥ 1`. Let

- `A : ℓ∞(k) → ℓ∞(n)` be positive and unital, with matrix `(a_{is})`, `i ∈ [n]`, `s ∈ [k]`
  — each row `a_i = (a_{i1},…,a_{ik})` is a probability vector ("membership rows");
- `M : ℓ∞(n) → ℓ∞(k)` be positive and unital, with rows `μ_s` probability vectors on `[n]`
  ("decoder measurements"), i.e. `(Mf)_s = Σ_i μ_s(i) f_i`.

Assume `‖MA − I_k‖_{∞→∞} ≤ ε` with `ε < 1/2`.

**Claim (PRH).** There is a **stochastic idempotent** `E : ℓ∞(n) → ℓ∞(n)` (positive,
unital, `E² = E`) with `‖AM − E‖_{∞→∞} ≤ C·√ε` for an absolute constant `C`.

Two independent derivations exist and **disagree on the constant** — `2√2` vs `3` — and
neither has been checked by anyone. Your job includes settling that.

## The candidate construction (audit it; improve or replace it if it is wrong)

From `‖MA − I_k‖ ≤ ε`, the `s`-th row of `R = MA` is claimed to satisfy
`2(1 − R_{ss}) ≤ ε`, hence `Σ_i μ_s(i)(1 − a_{is}) ≤ ε/2`.  *(Check this step with
particular care: it is the one place where the ∞→∞ operator norm of `R − I_k` is converted
into a one-sided mass statement, and it uses that the rows of `R` are probability vectors.
State exactly why the factor 2 is legitimate.)*

Then set `λ = √(ε/2)` and `C_s = { i : a_{is} > 1 − λ }` (the "cores").

1. If `λ < 1/2` the `C_s` are pairwise disjoint, because the coordinates of each `a_i` sum
   to one and two coordinates cannot both exceed `1 − λ > 1/2`.
2. Markov's inequality (in its valid direction only) gives
   `β_s := μ_s(C_s^c) ≤ ε/(2λ) = λ`; in particular `C_s ≠ ∅`.
3. Let `ν_s` be `μ_s` conditioned on `C_s`; then `‖μ_s − ν_s‖_1 = 2β_s ≤ 2λ`.
4. Let `N : ℓ∞(n) → ℓ∞(k)` have rows `ν_s`, and define `Â : ℓ∞(k) → ℓ∞(n)` by
   `â_i = e_s` for `i ∈ C_s`, and `â_i = a_i` for `i ∉ ⋃_s C_s`.
5. Disjointness of the cores plus `supp ν_s ⊆ C_s` gives **`N Â = I_k` exactly**, so
   `E := Â N` satisfies `E² = Â(N Â)N = E` and is positive and unital.
6. `‖AM − AN‖ ≤ 2λ` by (3) and convexity; for `i ∈ C_s`,
   `‖Σ_t a_{it} ν_t − ν_s‖_1 ≤ 2(1 − a_{is}) < 2λ`; outside the cores `A = Â`. Hence
   `‖AM − E‖ ≤ 4λ = 2√(2ε)`.

## What you must deliver

1. **A rigorous proof.** Every inequality justified; every norm identified (`∞→∞` operator
   norm vs `ℓ₁` distance between rows — state and prove the duality you use, e.g. that for
   a difference of two row-stochastic-like matrices the `∞→∞` norm is the max over rows of
   the `ℓ₁` norm of the row difference, and be careful that `AM − E` is a difference of two
   stochastic matrices while `MA − I_k` is not a difference of two stochastic matrices).
2. **The constant, settled.** Either confirm `2√2`, or produce the correct constant, or
   show the two derivations prove different statements. Optimize `λ` (the balance is
   `ε/λ + 2λ`, so `λ = √(ε/2)` is the natural stationary point — verify).
3. **Hypothesis hygiene.** Exactly which hypotheses are used where. In particular: is
   positivity+unitality of `M` needed, or only that its rows are probability vectors? Is
   `ε < 1/2` the right threshold, or is a stronger smallness needed for `λ < 1/2` (note
   `λ = √(ε/2) < 1/2 ⟺ ε < 1/2`, so the threshold is exactly consistent — confirm).
4. **The `ε = 0` endpoint.** If `MA = I_k` exactly, the construction should return an exact
   stochastic idempotent with `AM = E`. Verify this degenerate case explicitly (it is the
   cheapest sanity check and a favourite verifier target).
5. **Sharpness.** Is the `√ε` necessary for THIS lemma? Exhibit a family (a two-scale
   configuration is expected) forcing `‖AM − E‖ ≳ √ε` for every stochastic idempotent `E`,
   or state honestly that you could not, and say what you tried. (Note: `op-classical`'s
   `√η` sharpness is known independently; that does not automatically transfer to PRH's
   `√ε`, and conflating the two is exactly the kind of error the verifier hunts.)
6. **A defect register.** Every step you could not close, every place you strengthened or
   weakened the claimed statement, every constant you could not pin. An honest register is
   worth more than a clean-looking proof.

## Rules of engagement (repository law — non-negotiable)

- **"Runs without errors" / "looks fine" is never a proof.** Assert invariants against
  known-correct values; check degenerate cases.
- **No naked appeals to authority.** Do not cite Kitaev, SBD, or any paper for this lemma:
  it must stand alone at BSc/MSc-textbook level plus your own argument.
- **Do not overclaim.** If a step is heuristic, label it heuristic in the text itself.
- **You are the author, not the reviewer.** Do not write "verified", "validated", or
  "rigorous" about your own output.

## Output

Write your report to exactly ONE file:

`docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md`

Do **not** create, edit, move or delete ANY other file in the repository. In particular do
not touch `definitions/`, `argument/`, `report/`, `runs/`, `.beads/`, `.frontier/`, or any
other agent's artifacts, and do not run any `git` command. Markdown with LaTeX-in-`$…$` is
fine. Start the file with a `STATUS: UNVERIFIED PROVER OUTPUT` line.
