# BRIEF — fresh hostile audit of DESIGN-S1-POLAR-v3.md (fourth stage)

You are a fresh, independent, HOSTILE auditor. You did NOT write any of the
three designs or the two prior audits. Assume `DESIGN-S1-POLAR-v3.md` is
wrong until proven otherwise. v1 claimed closable → audit said REDESIGN;
v2 claimed closable → audit said REDESIGN. This is the third claim of
DESIGNED-CLOSABLE on this front. Finding a defect — a wrong formula, an
ill-formed contract, an unclosable guard, a circular dependency, a hidden
dimension-dependence, a misread locus, a prior finding papered over — is a
BIG SUCCESS.

## Your target

`docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v3.md` — thirteen
factored analytic rows (§3), a two-row witness-unification architecture
(§2, rows 12–13), six corrected downstream rows (§5), the corrected
`lem-stage1-extra-fixed-class` obligation ledger with the phase-lift (§6),
dimension-freeness (§7), definitions (§8), a serial landing order (§9), and
a disposition of EVERY `AUDIT-S1-POLAR-v2.md` finding (§10).

## Audit against (read all)

1. `AUDIT-S1-POLAR-v2.md` — the binding second audit. For EVERY finding,
   verify v3 §10 genuinely dispositions it. Its §10 required: factor rows
   2 and 8; export a genuine common-witness relation; add the quotient
   phase-lift; correct the two provenance items. Check each is REALLY done,
   not renamed.
2. `AUDIT-S1-POLAR.md`, `BRIEF-S1-POLAR.md`, `BRIEF-S1-POLAR-REPAIR-v3.md`
   (what was asked at each stage; check v3 did not silently narrow scope,
   and that the v3 brief's "do not redo" list was respected — rows
   3/4/6/7's contracts, both definition shards, and the arithmetic content
   were to be retained VERBATIM; diff them against v2 and flag any silent
   change).
3. `refs/kitaev-2405.02434/approximate_algebras.tex` — check every cited
   locus (407–440, 458, 554–560, 655–687, 692–807, 809–855, 857–893,
   895–912, 943–955), especially the CORRECTED provenance cells (group-law
   row: closeness from 845–868 + polar; defects literal at 872–874;
   basepoints 876–878) and the new Maurer–Cartan row's TeX 795–807.
4. The Lee/Munkres loci (C.34 txt:31134–31137, C.36 txt:31286–31298, C.40
   txt:31330–31344, 31374–31385; Munkres fallback loci) — verify each says
   what v3 claims and that the hypotheses of each smooth-upgrade row are
   delivered by its stated deps.
5. Landed shards: `lem-stage1-exact-unit-rectification.md`,
   `lem-stage1-quantitative-inverse-function.md`,
   `lem-topology-quotient-manifold.md`, `lem-topology-lefschetz-hopf.md`,
   `lem-topology-local-index-sign.md`, `lem-topology-finite-triangulation.md`,
   `lem-topology-orientable-top-cohomology.md` — v3's deps must use only
   what these contracts actually export (the rectification row must
   RECONSTRUCT TeX 672–687, not import from the landed proof export).
6. `DESIGN-FUDW-DECOMP-v4.1.md` §2.4/§2.6/§4.1/R14/R35 — no compound
   contracts, no theorem content in definitions, no guessed radii,
   ≤12 nodes / depth ≤3 PER FACTORED ROW (projections must now be honest).

## Specific attack surface (check each, then hunt beyond)

- **The witness-unification architecture (rows 12–13) — the new load-bearing
  repair.** Attack hardest here: (a) Is row 13's contract WELL-FORMED as a
  one-line registry contract — is "after replacing the leading existential
  constants in the contracts of [7 named rows] by these exact corresponding
  fields, the entire remaining universally quantified conclusion of every
  one of those seven contracts is true simultaneously" a closed,
  linker-checkable statement, or does it quantify over contract TEXT
  (meta-level) in a way the registry/af cannot represent? If it is
  meta-level, propose the exact object-level repair (e.g. restating the
  seven parameterized conclusions inline) or REFUTE the row. (b) Is the
  monotonicity argument (§2) actually valid for EVERY one of the seven
  producers — check each contract's quantifier structure: is a larger
  coefficient/smaller margin really always weaker-conclusion/stronger-
  antecedent (watch the two-sided uses of constants, e.g. C_ch appearing in
  both an upper guard and a distortion bound, C_pol in both radii of the
  sandwich)? A producer that is NOT monotone in a shared constant breaks
  the finite-maxima unification. (c) Do rows 12–13 together deliver exactly
  what each downstream consumer needs where v2's ledger failed?
- **The factored rows.** Are rows 2–3 (graph vs Maurer–Cartan) and 9–11
  (atlas / polar inverse / operations) each genuinely atomic now? Does row
  3's contract depend on constants produced only inside row 2's proof (the
  shared C_ch, κ_ch — is using the SAME names in two separate existential
  contracts a new witness-threading defect of exactly the kind that killed
  v2)? Does row 11 need smoothness of μ, σ INTO the manifold and does its
  dep list deliver that?
- **The retained rows.** Diff rows 1, 4, 5, 6, 7, 8 (v3 numbering) against
  their v2 counterparts — the brief required verbatim retention except
  named corrections. Any silent contract change is a finding.
- **The phase-lift (§5–6).** Is the quotient fixed-class phase-lift now an
  explicit proof obligation of the quotient-index row, stated with the
  square-root-of-phase + scalar-naturality mechanism, and does the
  obligation ledger record it? Is the derivation actually supported by the
  named deps (σ(cU) = c̄σ(U) comes from which row)?
- **Ledger arithmetic (row 12).** Recompute all eight guards and the three
  final bounds from the displayed minima (the v2 arithmetic was verified;
  v3 claims verbatim retention — verify the transcription introduced no
  error).
- **Dependency structure.** Acyclicity of the 13-row DAG + 6 downstream
  rows; row 13 must not depend on rows 9–11 (v3 claims this); node budgets
  per row honest.
- **Dimension-freeness (§7)** and **definition hygiene (§8)** — carried
  from v2; verify nothing in the factoring changed either.
- **Serial landing order (§9)** — a genuine topological sort including the
  definition/ratification gate.

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v3.md`

- Verdict per analytic row (all 13), per downstream repair (all 6), per
  obligation-ledger line, per definition shard, and per §10 disposition
  claim: VALID / VALID-WITH-CORRECTIONS (state them exactly) / REFUTED
  (show the defect concretely).
- A final disposition: LAND (with any corrections) / REDESIGN (what must
  change) / ROUTE-ALARM (a genuine obstruction — describe it).
- Cite every check with exact loci (file:line / TeX line / txt line).

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v3.md`.
  Touch nothing else.
- Do not repair the design beyond stating corrections; do not promote any
  status; nothing here is rigorous.
- If a needed fact is not in the local sources, say NOT IN LOCAL REFS — do
  not fill from memory.
