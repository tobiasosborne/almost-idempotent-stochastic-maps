# BRIEF — fresh hostile audit of DESIGN-S1-POLAR-v5.md (sixth stage)

You are a fresh, independent, HOSTILE auditor. You did NOT write any prior
design or audit on this front. `DESIGN-S1-POLAR-v5.md` claims to repair
`AUDIT-S1-POLAR-v4.md`'s four clause-level defects and adds a NEW
architectural element: seven parameterized transport helper rows (13a–13g),
each receiving the same witness tuple W, which discharge the
coefficient/margin monotonicity object-level; row 13's deps are now the
seven helpers + the scalar-arithmetic row, projected 11/3. New architecture
= new attack surface. Assume it is wrong until proven otherwise.

## Audit against (read all)

1. `AUDIT-S1-POLAR-v4.md` — binding: §§1.3, 1.5–1.7 (the four refuted
   clauses), §2.2 (binder rules), §3 (arithmetic, already VALID), §6 (the
   prescribed corrections, incl. §6(4)'s helper-factoring option and its
   constraint: helpers receive the same W; no unrelated existential
   tuples; cap not raised).
2. `DESIGN-S1-POLAR-v4.md` — the carry-forward base. v5 declares exactly
   six changes; diff everything else for silent drift (rows 1–12
   contracts, downstream rows, obligation ledger, dimension-freeness,
   definitions, sources).
3. `argument/README.md` and v4.1 R14/R35/§4.1 (contract discipline;
   ≤12 nodes / depth ≤3; datum-only definitions).
4. The TeX/Lee loci pinned in v5 §1 (spot-check stability).

## Specific attack surface (check each, then hunt beyond)

- **The seven transport helpers (13a–13g) — the new load-bearing layer.**
  For EACH helper: (a) is its contract a faithful PARAMETERIZED version of
  its base producer — same domains, same guards, same conclusions, with
  the base row's existential constants replaced by "for every W with
  C_• ≥ C_•⁰ and margin ≤ κ_•⁰" — and nothing dropped or added? (b) Is
  the monotonicity claim it encodes actually TRUE for that producer —
  check two-sided constant uses (C_ch appears in an upper guard AND in
  the distortion bound 1+C_ch·ε_r; C_pol in BOTH radii of the sandwich
  ⊆ S_δ ⊆; the strict < 1 in A₂'s normal-derivative bound): enlarging
  C_• weakens some conclusions but STRENGTHENS others (a larger distortion
  bound is weaker, but is a larger inner-sandwich loss still a true
  statement of the base row's conclusion form?). For each helper, decide
  whether "for every W above the base witnesses" genuinely follows from
  the base row — if the base row's conclusion is an EXACT description
  (e.g. S_δ defined as the image, inverse identities) rather than an
  inequality, monotonicity is trivial; where it is an inequality, check
  the direction. A helper whose parameterized claim fails for some W is
  REFUTED. (c) Does the helper's dep (the base row) plus pure
  monotonicity really give a 4-node/depth-2 tree honestly?
- **Row 13's A-clauses vs the helpers.** Row 13's contract restates
  A₁–A₇ + R inline. Check each clause is EXACTLY the corresponding
  helper's conclusion instantiated at the selected W (not the base row's
  — the quantifier structure must match the helper). Then the binder
  repairs: (i) domains: A₅/A₆/A₇ now "every exact-unit" (not
  finite-dimensional) — but check A₁–A₄'s domains still match THEIR
  producers (rows 1, 2 ARE finite-dimensional; is A₃'s domain right?);
  (ii) map bindings: A₃ binds the family (g_U) by its defining zero
  equation; A₅/A₆/A₇ introduce u_δ, g_sJ, χ_s, σ by defining properties —
  verify each introduction is well-defined GIVEN ONLY earlier conjuncts
  of the same contract (e.g. A₅ writes "the unique inverse of Π_δ" — is
  bijectivity of Π_δ guaranteed by A₄ for the SAME δ range A₅ quantifies,
  including the non-finite-dimensional algebras A₅ now covers but A₄
  does not? THIS IS THE CRITICAL CHECK: A₄ is finite-dimensional, A₅–A₇
  quantify over every exact-unit algebra — where does the polar inverse
  COME FROM in the infinite-dimensional case inside row 13's own
  statement?). If a clause references a map whose defining property is
  only guaranteed on a narrower domain than the clause quantifies, that
  is exactly the v4 flaw in a new form — REFUTE it.
- **Producer-side coherence.** The base producers 6, 7, 8 (group, path,
  derivative) quantify over every exact-unit algebra; their own proofs
  go through the polar row (row 4) which is stated finite-dimensionally?
  Check rows 6–8's contracts in v5 (carried from v4/v3): do THEY have the
  same domain mismatch internally (a row quantifying over every algebra
  whose dep only covers finite-dimensional ones)? If so this is a
  pre-existing defect the previous audits accepted — flag it explicitly
  either way with loci.
- **Budget honesty.** Helpers 4/2 each; ledger 11/3 with 8 deps. Under
  the declared atomic-import convention, is 11/3 credible for selecting
  W + applying 7 helper imports + the arithmetic row? State your own
  projection.
- **Carry-forward integrity.** Only the six declared changes; everything
  else byte-stable vs v4 (normalize and diff).
- **Serial order + downstream deps.** The seven helpers must appear in
  the landing order before row 13; downstream rows depend on the ledger
  and factored smooth rows as before — check nothing now dangles.

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v5.md`

- Verdict per helper row (13a–13g), per row-13 clause (A₁–A₇, R), for
  the producer-side coherence check, budget, carry-forward, and serial
  order: VALID / VALID-WITH-CORRECTIONS (exact) / REFUTED (concrete
  defect).
- Final disposition: LAND (with any corrections) / REDESIGN /
  ROUTE-ALARM.
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v5.md`.
- No repairs beyond stating corrections; no status promotion; nothing
  here is rigorous. NOT IN LOCAL REFS discipline applies.
