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

## 2026-07-10 — `lem-hx-financing-floor`: contract quantified over all reals A; the A<0 reading is false (quantifier corrected)

- **Claimed:** the W60 engine lemma carried status `proved` (L5, batched hostile
  verdict 'E3: VALID-WITH-CORRECTIONS') with contract "... all reals A, Lambda > 0,
  and every set N ... |chi(p_Q)| <= A for every Q in N ...". On the literal reading
  A ranges over ALL reals; with N = empty the A-hypothesis is vacuous, so A < 0 is
  admissible and the claimed floor (1 - A*l_chi)/Lambda strictly exceeds what the
  unit moment supplies.
- **Why wrong:** at A < 0, N = empty the true bound is a^+(F)+b^+(F) >= 1/Lambda -
  nu(a) - nu(b); the claimed floor adds |A|*l_chi/Lambda for free. Already the 2x2
  identity idempotent (rows e1, e2; chi = (1/2, -1/2); Lambda = 1/2; A = -1) gives
  claimed floor 6 vs actual joint mass 2. The af verifier challenge ch-9388e571
  (proofs/lem-hx-financing-floor/ledger/) carries the counterexample; the W60
  batched verifier and prover both missed the empty-N corner.
- **Caught by:** the W61 af elevation (fresh per-node codex verifiers) — three
  challenges pinned the silent A>0 assumption in the proof chain and the root
  amendment mismatch. The orchestrator's STUCK tripwire surfaced it.
- **Resolution:** contract restated with "all reals A > 0 and Lambda > 0" (matching
  the mechanism actually proved in W60 and the amended af root; a strict weakening).
  Status stays `proved` (L5) FOR THE CORRECTED STATEMENT; no rigorous rung was ever
  held by the false reading. Consumers audited: lem-hx-forced-exterior-coupling
  instantiates A*l = 1/2; route-fork scaffolds use A >= 4 — none touch A <= 0.
  Correction note in-shard; af elevation resumed on the aligned contract.
