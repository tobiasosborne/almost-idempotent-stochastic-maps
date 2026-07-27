# BRIEF — fresh hostile audit of DESIGN-S1-POLAR-v4.md (fifth stage)

You are a fresh, independent, HOSTILE auditor. You did NOT write any of the
four designs or the three prior audits. Assume `DESIGN-S1-POLAR-v4.md` is
wrong until proven otherwise. v4 claims a PRESCRIBED two-change repair of
the v3 audit's findings. The highest-value findings would be: the
object-level row-13 rewrite still smuggling meta-language or failing to
restate a producer conclusion faithfully; a restatement that silently
WEAKENS or STRENGTHENS a producer's conclusion (either breaks the
architecture); or a new defect introduced by the rewrite.

## Your target

`docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v4.md`.

## Audit against (read all)

1. `AUDIT-S1-POLAR-v3.md` — the binding audit. Its §0.1 prescribed the
   object-level form ∃W[A₁(W)∧…∧A₇(W)∧R(W)] with the seven producer
   conclusions RESTATED INLINE and R(W) = row 12's minima + conclusions;
   its §0.2 prescribed the exact `defs` lists for the six downstream rows.
   Verify both are executed exactly.
2. `DESIGN-S1-POLAR-v3.md` — v4 claims EVERYTHING else is carried forward
   verbatim. Diff rows 1–12, the six downstream contracts (modulo the added
   `defs`), the obligation ledger, §7 dimension-freeness, §8 definitions,
   and the serial order. Any silent change is a finding.
3. `argument/README.md` (the registry contract discipline row 13 must now
   satisfy) and `DESIGN-FUDW-DECOMP-v4.1.md` R14/R35/§4.1 (≤12 nodes /
   depth ≤3; v4 re-projects row 13 at 11/3 — assess honesty).
4. The TeX/Lee/Munkres loci as pinned in v4 §1 (unchanged from v3 — spot
   check they were not perturbed).

## Specific attack surface (check each, then hunt beyond)

- **The row-13 rewrite — audit it clause by clause.** For EACH of the seven
  analytic clauses A₁–A₇: compare against the corresponding v3/v4 producer
  contract (rows 1, 2, 3, 4, 6, 7, 8). The clause must assert, for the
  tuple W's fields, EXACTLY the producer's conclusion with W's constants
  substituted — same domains, same guards, same quantifier order, same
  estimates, nothing dropped (watch: the graph-control clause must include
  the chart-covering statement and all three displayed estimates; the
  Maurer–Cartan clause the distortion bound and both equivariance
  identities; the polar clause the two-radius sandwich; the group clause
  all seven estimates/identities; the path clause joint continuity and
  equivariance; the derivative clause chart retention and the −2I bound).
  A dropped conjunct silently weakens what consumers receive; an added one
  silently strengthens the proof obligation. Both are findings.
- **Meta-language sweep.** The row-13 contract must contain NO phrase of
  the form "the contract of", "the conclusion of", "replacing constants",
  "as in row N", or ANY reference to another row id inside the
  mathematical statement. Also check R(W): the four finite-minimum
  equations must be written as explicit equations in W's fields, and the
  scalar conclusions as explicit inequalities — not "the full conclusion
  of lem-stage1-polar-scalar-arithmetic".
- **Self-containment vs length.** Is every symbol in the row-13 contract
  quantified within it (or a def import)? Does it still reference μ, σ,
  g_V, u_δ correctly given those maps are INTRODUCED by the producers —
  i.e. does the clause structure existentially introduce the maps it
  constrains, or does it accidentally refer to maps that only exist inside
  other rows' conclusions? (This is the subtle failure mode of an inline
  restatement: the maps' existence must be part of each clause.)
- **Budget honesty.** 11 nodes / depth 3 for the rewritten root: plausible
  for a 7-clause conjunction + arithmetic + tuple selection? If each
  clause realistically needs its own subproof node plus the monotonicity
  argument, could it exceed 12? State your own projection.
- **The `defs` additions.** Check the six downstream rows' defs match the
  audit's §0.2 lists exactly (including `none` for maximal-simplex).
- **Carry-forward integrity.** Rows 1–12 and everything else byte-stable
  vs v3 except the two declared changes.

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v4.md`

- Verdict per row-13 clause (A₁–A₇, R), for the meta-language sweep, the
  budget, the defs additions, and the carry-forward diff: VALID /
  VALID-WITH-CORRECTIONS (exact) / REFUTED (concrete defect).
- Final disposition: LAND (with any corrections) / REDESIGN /
  ROUTE-ALARM.
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v4.md`.
- No repairs beyond stating corrections; no status promotion; nothing here
  is rigorous. NOT IN LOCAL REFS discipline applies.
