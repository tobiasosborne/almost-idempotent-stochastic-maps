# BRIEF v4 — S1-ENDGAME repair round 3 (fix audit v3's three interface fatals)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation. Read, in this order:
1. `docs/plans/2026-07-29-S1-ENDGAME-design/BRIEF-S1-ENDGAME.md` (original
   constraints — ALL still binding);
2. `docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME-v3.md` (v3 —
   your starting point; keep everything audit v3 did not attack);
3. `docs/plans/2026-07-29-S1-ENDGAME-design/AUDIT-S1-ENDGAME-v3.md` (VERDICT
   REDESIGN — fatals F1-F3, correctables F4-F5; every finding must be
   repaired or refuted with a line-cited argument).
(The v2 round documents exist for history; v3 + its audit supersede them.)

Write the complete repaired design to
`docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME-v4.md` — a
SELF-CONTAINED replacement (same deliverables list as the original brief),
not a diff.

## SETTLED by audit v3 (preserve verbatim; do not re-litigate)

Six of eight round-2 repairs HELD: direct manifold imports (B0b/B0i), the
literal near-adjoint estimate re-export at every hop, existentially
introduced `r_bidx`, C0/C1 architecture (b) (C0 eliminates one B1 package
internally; C1 consumes C0 alone; bridge locus contains tex:939), the exact
Hatcher externals (weak-Hopf tail only; 3C.4 exterior-tensor-polynomial
only) with A0 proving Delta(1) and A1 excluding polynomial generators +
proving finiteness, and A0's reals/finite-family declarations. Also clean:
all Hatcher/Kitaev loci (re-extracted), the M19-S1/M15 clause match, the
factoring coverage, the status graph and serial order, the G-S1-only
hand-off. The budget SHAPE (13 rows, targets <=10, caps <=15) was accepted
conditional on the repairs below.

## Mandatory repairs

**R-G1 (the B0a ledger-witness selection — audit F1, fatal).** B0a's root
says "writing `W=...` for one tuple supplied by
`lem-stage1-polar-constant-ledger`" — a non-unique existential package
selected by definite description (the prohibited pattern), and B0i's
skeleton then instantiates row-13 (A_7) "for the package's `W`", which a
fresh application of the existential ledger root cannot legally
synchronize. `def-stage1-polar-witness-data` does NOT rescue this: it is
fourteen scalar fields with no analytic assertion
(`definitions/def-stage1-polar-witness-data.md:13-28`); the fact that one
`W` satisfies (A_1)-(A_7),(R) lives only in the ledger ROOT. Choose ONE
honest architecture and state it explicitly:
  (a) PARAMETERIZE: B0a (and every receiving row) is conditional on one
      explicitly quantified ledger witness — "for every W and displayed
      data satisfying <the exact (A_i),(R) conjuncts consumed, spelled out
      in the root>" — and ONE row (the first consumer, or B1) applies the
      ledger root exactly once to instantiate the chain; or
  (b) SINGLE-SELECTION: the row that needs (A_7) applies the ledger root
      exactly ONCE, reconstructs the maps from that one selection
      internally, and exports everything downstream rows need — accepting
      that this repeats B0a's reconstruction and REPRICING that row's
      skeleton honestly (audit F1 says the eight-node B0i skeleton is
      invalidated under this option).
Do NOT invent an undefined `LedgerPackage(W)` predicate; do NOT apply the
existential ledger twice anywhere in the chain. Whichever option you take,
every consumed ledger clause must appear spelled out in the consuming
row's root.

**R-G2 (free symbols — audit F2, fatal).** B0i uses `breve-calU` in its
conclusion (quotient equation, H-space/manifold conclusions, domain of
`breve-sigma`, local-index clause) without ANY binder — no existential "and
a space breve-calU", no "set breve-calU := ...". Add the explicit binder
(match B0s/B0b/B1's form). Additionally ALL B rows introduce `breve-e` only
via the bare expression `breve-e=[J]`: make it an explicit "set
breve-e:=[J]" binder everywhere first used. Then RE-SCAN all 13 contracts
for any remaining free symbol (a bare equation inside a such-that clause
does NOT quantify its left-hand side).

**R-G3 (the ambient isolation ball — audit F3, fatal, the one genuinely
quantitative repair).** B0i exports chart data (`chi_s` on a coordinate
ball, inverse on the chart image, sigma-invariance, an F_s derivative
estimate) but NO quantitative inclusion
`calU intersect B_rho(sJ) subseteq chi_s(B_{r_iso}(0))` for a UNIVERSAL
`rho > 0`, and no dimension-free lower-Lipschitz estimate for `chi_s`. B0s
nonetheless claims one universal `r_bidx` making `J`,`-J` the only fixed
points in AMBIENT balls — "translate chart injectivity back" only yields an
algebra-DEPENDENT radius. Repair options (pick and justify):
  (i) import the already-validated
      `lem-stage1-uniform-inversion-isolation` root, which has EXACTLY the
      desired universal ambient-ball conclusion
      (`argument/lemmas/lem-stage1-uniform-inversion-isolation.md:4`) —
      but its anaphoric `sigma` then REQUIRES an explicit same-map
      synchronization clause proving its map is the displayed
      `breve-sigma` (do this with the typed-binder discipline; if the
      synchronization cannot be proved from the roots, say so and take
      (ii)); or
  (ii) prove the missing bridge as an explicit root clause: a universal
      ambient inradius or a uniform (dimension-free) inverse-chart /
      lower-Lipschitz estimate derived from the QIFT root's quantitative
      data (`argument/lemmas/lem-stage1-quantitative-inverse-function.md`)
      — as its own factored row if the granularity demands it.
Preserve the identity of the displayed `sigma` throughout. The claimed
dimension-freeness of `r_bidx` and everything downstream (B1's distance
bounds, C0's vanishing-alternative exclusion) must become PROVED, not
asserted.

**R-G4 (re-budget B0i/B0s — audit F8-conditional + F13).** After R-G1/R-G3
the B0i/B0s skeletons change. Re-budget honestly against the benchmarks
(quotient-index 12, isolation 7, hopf-structure 13); if same-witness
reconstruction or the ambient-inradius proof exceeds the present
granularity, FACTOR AGAIN (~<=12 targets; caps <= 15; never conceal
multi-obligation nodes).

**R-G5 (the two correctables — audit F4/F5).** (1) A2's skeleton phrase
"Insert A0's ... formula" and the budget-table phrase "imports A0 and A1
separately" both violate the root-only import rule — A2's only dep is A1,
whose root re-exports the finite-tail clause; fix both phrases to say A2
consumes it FROM A1's ROOT. (2) A1 concludes "isomorphic as a GRADED
algebra" while the registered 3C.4 external says only "isomorphic as an
algebra": add the explicit A1 skeleton obligation deriving that the
isomorphism sending exterior generators to the homogeneous odd-degree
generators preserves degree (Kitaev's guide: `approximate_algebras.tex:1016`)
— never silently strengthen the registered external.

## Unchanged constraints (binding as ever)

One-line ASCII contracts; typed-witness law (NO free symbols, NO untyped
definite descriptions of non-unique existential packages); T0-only imports
consumed with their ACTUAL root antecedents (root contract only, never the
explanatory body); dimension-free constants; ~<=12-target factoring rule
vs cap 26; def-layer minimization (zero new defs unless forced); L1 source
discipline (`\n`-only loci); the M19-S1 producer shapes and the G-S1-only
hand-off exactly as v3 has them.

Your final answer: a <=15-line executive summary — per-finding disposition
(F1-F5: fixed how, incl. WHICH option you took for R-G1 and R-G3 / refuted
why), the new row count and budget table if factoring changed it, and
whether any NEW row, external, or def was added relative to v3.
