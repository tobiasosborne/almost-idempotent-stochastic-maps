# BRIEF — 13e binder-interface repair design (the group-laws transport defect)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; everything you produce is escalated for verbatim landing after a
fresh hostile check.

## The problem

The ratified transport contract
`argument/lemmas/lem-stage1-approximate-group-laws-transport.md` ("13e")
binds `(u_delta, h_delta)` EXPLICITLY as "the unique inverse of
Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(...),
Pi_delta(U, H) = U bold-dot H", while its parent family — the three
af-VALIDATED contracts `lem-stage1-approximate-group-laws`,
`lem-stage1-group-domain-membership`, `lem-stage1-group-closeness` — binds
`u_delta` only by the ELLIPTICAL definite description "the inverse u_delta
of the polar map" (no Pi_delta display, no typed datum). Three af
elevation runs (W93 runs 1–3, the last with prover xhigh) aborted STUCK
with consistent fresh-verifier findings: the identification
u_grp = u_pol is formally underivable from the exact allowed inputs —
`lem-stage1-polar-coherence-naturality` needs TWO typed polar data and the
group-laws side supplies none. The paused workspace
`proofs/lem-stage1-approximate-group-laws-transport/` retains 28/37
validated nodes and both landed dep widenings (polar-retraction,
coherence-naturality) — READ its ledger/ and the challenge texts before
designing. Contrast: transports 13f and 13g cleared the analogous
bare-anaphor gap because their missing premises had verbatim T0 providers
(13g: a deps-only widening with `lem-stage1-polar-retraction`,
`lem-stage1-unitary-graph-control`, `lem-stage1-smooth-unitary-operations`
+ antecedents sufficed — see the run-1 classification recorded in
`argument/lemmas/lem-stage1-inversion-derivative-transport.md`). For 13e
NO T0 provider carries the group-laws conclusions in explicitly-bound
form: that is exactly the defect.

## Hard constraints discovered since the bead was filed

1. **Row 13 consumes the EXPLICIT binder.** The ratified
   `argument/lemmas/lem-stage1-polar-constant-ledger.md` clause (A_5)
   opens "writing (u_delta, h_delta) for the unique inverse of
   Pi_delta ..." and then states the seven group-law conclusions for the
   mu, sigma built from THAT u_delta; (A_6)/(A_7) bind u_delta the same
   way. So a repair that restates 13e's binder anaphorically (bead option
   A as originally phrased) merely moves the identification gap up into
   row 13's elevation. If you nonetheless recommend an anaphoric 13e, you
   MUST also design the row-13 (A_5) amendment and price its ratification
   deviation.
2. **Amending the group-laws family cascades through byte-matched
   externals.** The family's contract texts are registered verbatim as af
   externals in these workspaces (grep verified 2026-07-28):
   `proofs/lem-stage1-inversion-derivative-control/` (T0),
   `proofs/lem-stage1-smooth-unitary-operations/` (T0),
   `proofs/lem-stage1-inversion-derivative-transport/` (T0),
   and the paused 13e workspace itself. `lem-stage1-smooth-unitary-atlas`
   and `lem-stage1-smooth-polar-inverse` also sit downstream via deps. A
   bead-option-B amendment must therefore price: which of these validated
   trees keep their validity certificates (external text unchanged?),
   which need mechanical external re-registration, and which need genuine
   re-elevation. Be precise; "3 contracts touched" was the original
   estimate BEFORE this cascade was mapped.
3. **The registry layer that already exists at T0** (usable as allowed
   inputs for any new lemma you propose): `lem-stage1-polar-retraction`
   (Pi_delta a C^1 diffeomorphism with inverse (u_delta, h_delta), the
   EXPLICIT typed datum), `lem-stage1-polar-coherence-naturality` (two
   typed polar data -> coherence + scalar naturality),
   `lem-stage1-group-domain-membership` and `lem-stage1-group-closeness`
   (elliptical binder, deps = polar-retraction),
   `lem-stage1-smooth-polar-inverse`, `lem-stage1-smooth-unitary-atlas`,
   `lem-stage1-smooth-unitary-operations` (NOTE: its contract defines
   mu(U,V) = u_delta(U bold-dot V), sigma(U) = u_delta(U^dagger) and
   asserts their smoothness — check how ITS u_delta is bound and whether
   it can serve as an identification bridge), and the six validated
   transports 13a–d, f, g. Read the actual shards; do not trust this
   summary.

## Candidate repair directions (weigh ALL; recommend ONE with reasons)

- **(R1) Direct re-derivation transport.** Keep 13e's ratified contract
  BYTE-UNCHANGED and redesign only its PROOF ROUTE: derive the seven
  group-law conclusions for the explicitly-bound u_delta directly from
  the typed T0 layer (polar-retraction + group-domain-membership +
  group-closeness + coherence-naturality), re-proving the identification
  content instead of importing `lem-stage1-approximate-group-laws` as a
  whole. If the group-laws proofs essentially construct u_delta as the
  polar inverse (read `proofs/lem-stage1-approximate-group-laws/export.md`),
  the same derivation should type-check against the explicit binder. If
  this needs the elliptical children's conclusions transported first,
  design the (small) bridging lemmas with explicit binders and price them.
- **(R2) Bead option B, cascade-priced.** Explicit-binder amendment of the
  three group-laws contracts + re-elevation + the constraint-2 cascade.
- **(R3) A new identification lemma.** A single new registry lemma
  asserting u_grp = u_pol (or directly the explicit-binder restatement of
  the three family conclusions) from named T0 inputs, inserted as a dep of
  13e; 13e then elevates against it. State its exact contract text.
- **(R4) Anaphoric 13e + row-13 amendment** (only if you can argue it
  strictly dominates; see constraint 1).

## Your deliverables — write `docs/plans/2026-07-28-13E-BINDER-design/DESIGN-13E-BINDER.md`

1. **The recommended repair**, with the EXACT contract text(s) to land
   verbatim (registry ASCII, one-line `contract:` form, matching the
   house style of the existing transports), the exact `deps:` lines, and
   for every touched shard whether its text is NEW, AMENDED, or
   BYTE-UNCHANGED.
2. **Re-elevation plan**: which workspaces re-seed, which resume, node
   budgets per the observed transport costs (5–22 nodes each), and the
   external-registration list per workspace (every definite description
   the root binds must have its provider imported — the 13g lesson).
3. **Consumer re-check**: one paragraph each proving row 13 (A_5)–(A_7)
   and the rows-14+ requirements (DESIGN-S1-POLAR-v6.md §3, the audited
   design of record in `docs/plans/2026-07-26-S1-POLAR-design/`) are
   satisfied VERBATIM by the repaired conclusion; explicitly confirm the
   witness-data thresholds (C_grp^0, C_pol^0, kappa_pol^0) survive.
4. **Cost table**: codex-job count (design already spent; audit, provers,
   verifiers), touched-shard count, re-elevation count, and the risk you
   see as highest.

Do NOT edit anything under `argument/`, `definitions/`, `proofs/`, or
`report/`. Write ONLY the design file above.
