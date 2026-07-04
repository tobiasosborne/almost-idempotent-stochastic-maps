<!--
ROLE: the graveyard of RETRACTED claims — results once asserted here that turned out WRONG. NOT live
  gotchas (those are FINDINGS.md) and NOT inherited dead-routes (those are FINDINGS.md dead-route section).
UPDATE POLICY: append a dated entry when an in-repo claim is retracted. A retraction here is a SUCCESS of
  the rigour machinery, not an embarrassment. HOW-to-work is in CLAUDE.md.
TRIGGER: an in-repo result's status is downgraded from a rigorous rung, or a claim is disproved.
-->

# LEARNINGS — retracted claims (dated)

_(The inherited REFUTED routes from the classical-portfolio are recorded as dead-route certificates in
`FINDINGS.md`, not here; this file is only for claims THIS repo asserted and then had to withdraw.)_

## 2026-07-04 — `lem-dual-localization`: the transcribed "open problem" was vacuous (contract retired)

- **Claimed:** the registry carried `lem-dual-localization` (status `open`) as "the single genuine gap
  in the frame-free proof of the linear law": *reproduce `‖Ē‖₁ ≥ H` from `P²=P` without the canonical
  simplex frame*. (No mathematical result was asserted; the wrong claim was the shard's FRAMING — that
  this statement has open content.)
- **Why wrong:** as literally stated it is a distance tautology — once `v₁ = L̄ + Ē` with `L̄ ∈ C_W`,
  `H ≤ dist₁(p_{v₁}, C_W) ≤ ‖Ē‖₁` needs no idempotence. The upstream source
  (`docs/ingest/experiments/DELIVERABLE2_asq_proof.md:86`) mislabelled the tautology as the exactness
  content; the intended difficulty is the skinny mutual-shadow degeneracy.
- **Caught by:** arm B wave 1 (`docs/waves/2026-07-02-B1-dual-localization.md` §6, opus worker),
  independently CONFIRMED by a read-only codex verifier (2026-07-02; bd `aism-136` notes).
- **Resolution:** user decision 2026-07-04 (aism-136) — superseded by `conj-skinny-shadow-cap` (the
  skinny two-shadow cap, the corrected Route-B statement); `lem-dual-localization` retagged
  `obstruction` with a supersession marker in its contract; callouts in `CLAUDE.md`/`AGENTS.md`,
  `FINDINGS.md`, `RESEARCH_NOTES.md`, `HANDOFF.md`, and the report status ledger updated; DAG
  regenerated. No rigorous rung was involved at any point.

<!-- template:
## YYYY-MM-DD — <claim that was WRONG>
- **Claimed:** <the statement + the status it wrongly carried>
- **Why wrong:** <the counterexample / gap>
- **Caught by:** <reviewer / af verifier / numerical refutation / byte-match failure>
- **Resolution:** <status downgraded to …; dependents re-checked; DAG regenerated>
-->
