# BRIEF v5 — S1-ENDGAME repair round 4 (fix audit v4's two plumbing fatals)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation. Read, in this order:
1. `docs/plans/2026-07-29-S1-ENDGAME-design/BRIEF-S1-ENDGAME.md` (original
   constraints — ALL still binding);
2. `docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME-v4.md` (v4 —
   your starting point; keep everything audit v4 did not attack);
3. `docs/plans/2026-07-29-S1-ENDGAME-design/AUDIT-S1-ENDGAME-v4.md` (VERDICT
   REDESIGN — fatals F1-F2, correctable F3; every finding must be repaired
   or refuted with a line-cited argument).
(Earlier round documents exist for history; v4 + its audit supersede them.)

Write the complete repaired design to
`docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME-v5.md` — a
SELF-CONTAINED replacement (same deliverables list as the original brief),
not a diff.

## SETTLED by audit v4 (preserve verbatim; do not re-litigate)

- **The ambient-ball bridge PASSED hostile checking**: `r_bidx = r_iso` is
  valid in the ambient norm and dimension-free. Keep B0s's bridge clause,
  derivation skeleton, and constant EXACTLY as v4 has them.
- The B-only same-witness path is synchronized correctly (W quantified
  before the algebra, formulas repeated, B1 binds one ledger witness and
  calls B0b on it, class-before-representative order everywhere). Preserve.
- All binders/free-symbol discipline (R-G2), A1's explicit grading node,
  A2's A1-root-only tail use, all source loci, zero new defs, T0-only
  acyclic deps, the M19-S1/M15 clause match, the G-S1-only hand-off.
- The smooth-atlas / smooth-polar-inverse / explicit-operations roots
  receive exactly what they require (audit v4 verified this) — do not
  disturb those consumptions.

## Mandatory repairs

**R-H1 (C1's second ledger application — audit F1, fatal).** v4 declares B1
the unique ledger instantiator, but C1 has a direct dep on
`lem-stage1-polar-constant-ledger` and its first node says "Fix one row-13
tuple and its single (A_1) rectification" — while C0 has deliberately
forgotten B1's package. C1 therefore RESELECTS a second, possibly different
witness; the single-instantiation law is broken and v4's dependency summary
(one ledger edge) is falsified. Choose ONE repair and state it explicitly:
  (a) W-FREE PROVIDER (auditor-suggested): drop C1's ledger dep; import an
      already-T0 exact-unit rectification theorem that needs no `W` — the
      candidate is `lem-stage1-rectified-cstar-control`. READ ITS ACTUAL
      ROOT (`argument/lemmas/lem-stage1-rectified-cstar-control.md`) and
      verify it supplies the exact-unit rectification C1 consumes with its
      actual antecedents; if it does not suffice alone, name what else is
      needed (still W-free) or take (b).
  (b) CARRY THE WITNESS: thread B1's typed witness through C0 into C1 —
      this means C0's root must EXPORT the witness data C1 needs (C0 no
      longer "forgets"), with the package's conjuncts spelled explicitly in
      C0's conclusion and C1 consuming C0's exported package only. Keep the
      single-application law: after the repair the ledger root must appear
      in EXACTLY ONE row's deps/skeleton across all 13 rows — re-scan and
      say so.
Update contract, deps, skeleton, dependency-graph prose, and budget
consistently (audit F1 notes the summary table must match).

**R-H2 (the threshold mismatch — audit F2, fatal).** B0i and B0b are
quantified over ALL exact-unit algebras with `epsilon_r <= epsilon_*^r`,
but they consume `lem-stage1-quotient-manifold-package`, whose root gives
the manifold package only below its OWN separate existential threshold
`e_quot^r` — and nothing states `epsilon_*^r <= e_quot^r`. A parameterized
row cannot promise a conclusion on a range wider than its providers
deliver. Choose ONE repair:
  (1) COMMON RECEIVING THRESHOLD: restructure the parameterized B rows so
      their conclusions hold below an explicitly BOUND receiving radius —
      e.g. the row's conclusion existentially introduces a universal
      `epsilon_B > 0` (obtained as the minimum of `epsilon_*^r` and every
      non-parameterized provider threshold it consumes, each received
      TYPED: the provider's existential threshold must be bound by the
      consuming row, not assumed comparable) — and every downstream row
      receives and propagates the SAME `epsilon_B`. Check the C rows and
      the three G-S1 producers still deliver the M19-S1 shape under the
      restricted threshold (M19-S1 tolerates a universal threshold — check
      the consumer clause at DESIGN-MAIN-STRUCTURE-v5.md:381 and say so).
  (2) REDERIVE THE PACKAGE: add and spell the actual parameterized
      manifold/orientation antecedents — including the ledger's (A_3)
      same-graph Maurer-Cartan data and the global tangent trivialization
      (the actual root: `argument/lemmas/lem-stage1-maurer-cartan-trivialization.md:4`,
      or its parameterized transport row) — and rederive compactness,
      orientation, smoothness, boundarylessness, and dimension inside the
      parameterized chain without the non-parameterized manifold root.
      Root-only consumption: nothing may be recovered from a dependency's
      body or closure.
Option (1) is less invasive if the M19-S1 interface tolerates it — justify
your choice either way. B0b's identical defect must be repaired by the same
mechanism. Rebudget B0i/B0b honestly afterwards (audit F2: the ten-node
B0i skeleton hid the range/orientation obligation; benchmarks:
quotient-index 12, isolation 7, hopf-structure 13; ~<=12 targets, caps <=15,
factor again if needed).

**R-H3 (B1's (R) prose — audit F3, correctable but MUST be visible).** The
ledger's actual (R) clause is quantified over rectified `epsilon_X <= e_S1`
after setting `epsilon_r = C_rect*epsilon_X` — it does NOT hand over the
specialized guards in the quantifier form B1 claims. Add an explicit
scalar-arithmetic derivation node in B1 (derive the guards for arbitrary
exact-unit `epsilon_r <= epsilon_*^r` from the displayed minimum formula),
and fix the prose that calls them literal root conjuncts. This obligation
must remain visible in whatever B1 becomes after R-H1/R-H2.

## Unchanged constraints (binding as ever)

One-line ASCII contracts; typed-witness law (no free symbols, no untyped
definite descriptions, class before representative, providers' existential
thresholds received typed); T0-only imports consumed with their ACTUAL root
antecedents (root contract only); the existential ledger applied exactly
once chain-wide; dimension-free constants; ~<=12-target factoring rule vs
cap 26; def-layer minimization (zero new defs unless forced); L1 source
discipline (`\n`-only loci); the M19-S1 producer shapes and the G-S1-only
hand-off.

Your final answer: a <=15-line executive summary — per-finding disposition
(F1-F3: fixed how, incl. WHICH option for R-H1 and R-H2 / refuted why), the
budget table if it changed, whether any NEW row, external, or def was added
relative to v4, and confirmation that the ledger root now appears in
exactly one row.
