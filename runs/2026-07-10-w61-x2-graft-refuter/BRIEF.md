# W61 decider A — X2 thin-transient-graft REFUTER SEARCH (L3, exact arithmetic)

You are a fresh, independent worker. Your workspace is this directory: a snapshot of
the registry (`argument/`, `definitions/`) plus context docs (`context/`). Everything
you produce stays INSIDE this directory. This is an L3 (numerical/constructive
evidence) job: **nothing you produce is a proof**, and your report must say so.

## Target

`context/DECOMPOSITION-W60-CODEX.md` §X2 proposes (NOT registered, status conjecture):

> **X2 (microfreight exclusion).** There exist universal eps_mu in (0,1/16) and
> delta_mu in (0,2^-16] such that no bad H-X datum C with delta(P) <= delta_mu
> satisfies T_B(C) <= eps_mu.

where a **bad H-X datum** C = (P, v, phi, h, f, xi, B) is a selected-corner
configuration (see `definitions/def-selected-corner.md` — read it FIRST and follow it
clause by clause) with B in {B_F, B_N}, Gamma_f(B) >= 1/4, M_X(B) > 1/8, and T_B is
the truncated quotient transport cost defined in the §1 "Shared clone-quotient
notation" of the same context doc:

    T_B(C) = integral over B ∩ {p_x != p_u} of min(1, ||p_x - p_u||_1 / tau) dGamma_f(x,u),
    tau = sqrt(delta(P)).

## Your job: try to REFUTE X2

Find an explicit FAMILY of exact signed idempotents P_k (square real matrices,
P_k^2 = P_k EXACTLY, delta(P_k) = total negative row mass -> 0 as k grows) such that
each P_k carries a bad H-X datum C_k with T_B(C_k) -> 0 (equivalently: for every
fixed eps > 0 the family eventually has T_B < eps while remaining bad).

The registered likely refuter shape (from the X2 honest-price paragraph): a **thin
nonclone transient-row graft** — extra rows carrying constant incoming freight mass
whose row-point displacement from their carrier tends to 0 (so the transport cost
vanishes) while they remain genuinely off-diagonal (p_x != p_u). Study
`argument/lemmas/obs-thin-zero-face-blocker-graft.md` for the banked graft
construction pattern. You may also try any other shape; you are NOT limited to
grafts. Adverse constraints to respect (they are what makes this nontrivial):

- P^2 = P must hold EXACTLY (rational arithmetic; use Python `fractions.Fraction`).
- ALL selected-corner clauses of `def-selected-corner` must hold exactly for C_k
  (the corner-score selection, the legal disintegration kernel xi, the radial block
  B, hiddenness of the relevant vertices, etc. — whatever the definition demands).
- Gamma_f(B_k) >= 1/4 and M_X(B_k) > 1/8 with M_X the mass of pairs with
  p_x != p_u in B (the strict off-diagonal predicate — points, not indices: clones
  re-sum inside fibers).
- delta_k -> 0 (at minimum: delta_k <= 2^-16 for the family tail, decreasing).

## Deliverables (all inside this directory)

1. `search.py` — self-contained exact-rational construction + verification script.
   For each candidate it must VERIFY (exact, no floats): P^2 = P; delta(P); every
   selected-corner clause it claims; Gamma_f(B), M_X(B), T_B. It must print a
   verdict table. "Runs without errors" is not a pass: every check asserts an exact
   invariant.
2. `certificates.json` — for a successful refuter family: the matrices (rationals as
   strings), the datum (v, phi, h, f, xi, B), and the exact values
   (delta, Gamma_f(B), M_X(B), T_B) for at least 3 increasing k.
3. `REPORT.md` — the decider verdict, one of:
   - **REFUTED**: family found; X2 is false as stated. Include the mechanism in
     2-3 sentences and the smallest witness.
   - **NOT REFUTED (search failed)**: for EVERY shape you attempted, name the
     exact clause/inequality that blocked it (e.g. "graft rows with displacement
     < tau/8 could not carry Gamma_f mass >= 1/4 because <specific ledger>").
     A failed search is evidence, not proof of X2 — say so explicitly.
   - **PARTIAL**: anything in between, honestly scoped.
   Also record: shapes tried, parameter ranges, dead ends, compute used.

## Discipline

- Read `context/FINDINGS.md` dead routes BEFORE constructing: do not spend effort on
  shapes already killed (raw-index path products, censoring without norm gap, etc.).
  The cloning obstruction CUTS BOTH WAYS: your T_B and M_X must be computed on the
  row-point quotient (fibers), never on raw indices.
- The corner data must be LEGAL: xi a genuine disintegration kernel per the
  definition (exact barycentric identities), not an arbitrary matrix.
- Timebox: if a full selected-corner witness is out of reach, degrade honestly to
  the strongest partial witness (e.g. all clauses except one, named) and report
  which clause is the obstruction — that is itself decisive information.
- Work entirely inside this directory. Final answer: a one-paragraph summary of
  REPORT.md's verdict.
