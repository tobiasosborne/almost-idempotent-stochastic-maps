# W60 ENGINE BATCH — prover brief (routine tier)

You are a PROVER. Produce complete, self-contained paper proofs of the five routine
statements below. You are NOT a strategist (do not redesign the statements beyond the
latitude explicitly granted) and NOT a verifier (a separate hostile verifier will
check your work; write for that adversary). Everything stays in the SIGNED picture:
P a finite exact signed idempotent (P² = P, P·1 = 1), δ = δ(P) its negative mass,
τ = √δ, definitions in `definitions/` (esp. def-signed-idempotent, def-negative-mass).

## Source material

- `DECOMPOSITION-W60.md` (nodes X0, X1 and §Shared clone-quotient notation) and
  `DECOMPOSITION-W60-FABLE.md` (nodes N1, N2, N3, N7) in this workspace root — the
  five targets below merge these; where the two formulations differ you must prove
  the form STATED HERE.
- `context/PAPER-PROOF-w59.md` — the T0 anchor proof; its Claims 1, 2, 4 are the
  rank-3/slab special cases of E1/E2; reuse its techniques freely (it is at the top
  rigour rung) but your proofs must be self-contained and rank-free/slab-free.
- `context/FINDINGS.md` — dead routes, ABSOLUTE. In particular: no index-level path
  products (clone obstruction); no censoring without a norm gap; no per-fiber
  budget payments (pay per sign-union, the K-free pattern).

## Notation (fix once, use throughout)

Full row-point fibers Q partition the index set by p_i = p_j. For a coefficient
vector (row) r ∈ R^I and a set S of fibers: r(S) := Σ_{Q∈S} Σ_{j∈Q} r_j and
r^+(S) := Σ_{Q∈S} Σ_{j∈Q} max(r_j, 0). ν(r) := Σ_j max(-r_j, 0). K(P) :=
conv{p_i} the row polytope. A synthetic row is any q ∈ K(P) (a convex combination
of rows); note qP = q, q·1 = 1, ν(q) ≤ max_i ν_i ≤ δ — PROVE these where used.
For an ordered pair (a,b) of synthetic rows, d_Q := Σ_{j∈Q}(a_j − b_j).

## The five targets

**E1 (moment identity; merged N1/X0 at row-hull generality).**
For every finite exact signed idempotent P, every q0, q1 ∈ K(P) with q0 ≠ q1, and
every affine function χ on R^I with χ(q0) = 0 and χ(q1) = 1, the full row-point
fibers satisfy Σ_Q d_Q·χ(p_Q) = 1, where d_Q := Σ_{j∈Q}(q1_j − q0_j).
[Prove also, as a separate labelled construction, non-emptiness of the normalized
class: there exists such a χ with |χ(a) − χ(b)| ≤ ‖a−b‖₁ / ‖q1−q0‖₁ for all a, b
(Hahn–Banach / dual-norm attainment on ℓ¹).]

**E2 (two-sign-union variation ledger).**
For every finite exact signed idempotent P, every ordered pair (a,b) of synthetic
rows (elements of K(P)), and every set S of full row-point fibers:
Σ_{Q∈S} |d_Q| ≤ a^+(S) + b^+(S) + ν(a) + ν(b).
[Pay each row budget ONCE per sign-union, never per fiber. Handle d_Q = 0 fibers
explicitly. Also record the global bound Σ_Q |d_Q| ≤ ‖a−b‖₁.]

**E3 (financing floor; N3 verbatim).**
For every finite exact signed idempotent P, every ordered pair (a,b) of synthetic
rows with ℓ := ‖a−b‖₁ > 0, every affine χ with χ-difference normalized so that
Σ_Q d_Q·χ(p_Q) = 1 is applicable (i.e. χ(b) = 0, χ(a) = 1 after relabelling — state
it cleanly), all reals A, Λ > 0, and every set N of full row-point fibers such that
|χ(p_Q)| ≤ A for all Q ∈ N and |χ(p_Q)| ≤ Λ for all Q ∉ N, the complement F of N
satisfies a^+(F) + b^+(F) ≥ (1 − A·ℓ_χ)/Λ − ν(a) − ν(b), where ℓ_χ := Σ_Q |d_Q|
(≤ ℓ). [Derive from E1 + E2 by splitting the identity over N ∪ F. Include, as a
labelled corollary in the body (not a separate target), the recentred-sign-functional
instantiation: for rows r,s and any center c ∈ K(P), the fibers within ℓ1-distance
Aℓ of c qualify as N with Λ = (2+4δ)/ℓ; prove the row-diameter bound you use.]

**E4 (robust scalar starvation; X1 verbatim — THE T0 GENERALIZATION).**
For every finite K_R, L, K_C ≥ 0 there exists a universal δ_R(K_R, L, K_C) ∈
(0, 2^{-16}] such that no finite exact signed idempotent P with 0 < δ(P) ≤ δ_R
admits full row-point fibers represented by v, f, a pair (A, q) with A ≥ 4,
q ∈ K(P), τ/2 ≤ ‖q − p_v‖₁ ≤ 2τ, ‖p_f − p_v + A(q − p_v)‖₁ ≤ K_R·δ, and an affine
χ with χ(p_v) = 0, χ(q) = 1, |χ(x) − χ(y)| ≤ ‖x−y‖₁/‖q−p_v‖₁ on K(P), such that
Tail_L(v, χ) := Σ_{Q: |χ(p_Q)| > L} (c_Q)_+ ≤ K_C·δ, where c_Q := Σ_{j∈Q} P_{vj}.
[Follow the X1 mechanism sketch: E1 unit moment for D = q − p_v; sign-split the
tail; row budgets of the synthetic row q and of row f (via p_f = p_v − A·D + r,
‖r‖₁ ≤ K_R·δ); core costs ≤ L·‖D‖₁; derive an explicit universal ceiling
δ_R(K_R, L, K_C) in closed form. MANDATORY FIXTURE: verify the T0 configuration
(PAPER-PROOF-w59.md display, q = p_z) lies in the regime (K_R, L, K_C) = (3, 1, 0)
and that your ceiling at (3,1,0) is ≥ some explicit positive number; compare with
the T0 close.]

**E5 (forced exterior coupling; N7 verbatim).**
For every finite exact signed idempotent P, every pair of row indices (r, s), and
every c ∈ K(P), the full row-point fibers Q with ‖p_Q − c‖₁ > 1/2 carry
P_r^+ + P_s^+ ≥ ‖p_r − p_s‖₁ / (2(2 + 4δ(P))) − 2δ(P).
[Instantiate E3. FIXTURE: check the δ = 0 case by hand on a two-block stochastic
idempotent (two disjoint-support recurrent blocks, rows = mixtures) and report the
constant's tightness or slack.]

## Honest-scope duties

For each target: state exactly what is proved, flag every step that uses a property
of synthetic rows (qP = q, ν(q) ≤ δ, row diameter) with its own numbered mini-proof,
and end with a SCOPE paragraph (what the statement does NOT give — e.g. E4 does not
supply the actor pair (A,q), the tail cap, or anything about selected-corner data).
If a target as stated is FALSE, do not repair it silently: give the counterexample,
then prove the nearest true statement and flag the change LOUDLY at the top of that
section. If you need a fact about signed idempotents not in the definitions, prove
it inline — no citations to memory.

## Deliverable

`PROOFS-W60-ENGINE.md` in the workspace root: one section per target E1–E5, each
with STATEMENT (verbatim from above, or amended-and-flagged), PROOF (numbered
displays, adversary-ready), FIXTURES (where mandated), SCOPE. Begin the file with a
5-line summary table: target | proved as stated? | ceiling/constants | fixture
status.
