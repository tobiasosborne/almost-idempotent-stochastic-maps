# BRIEF v2 — 13e repair design, round 2 (post-audit, post-retraction)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; everything you produce is escalated for verbatim landing after a
fresh hostile check. You are NOT the round-1 designer and owe its choices
nothing beyond what survives the record.

## Required reading (in order)

1. `BRIEF-13E-BINDER.md` (the original problem statement + constraints).
2. `DESIGN-13E-BINDER.md` (round-1 design: R1, two explicit-binder bridge
   rows — its §1 contracts survived the audit unchallenged).
3. `AUDIT-13E-BINDER.md` (VERDICT: REJECT; findings 1–4).
4. `ADJUDICATION-T0-ALLEGATION.md` (finding 2 CONFIRMED; as a result
   `lem-stage1-inversion-derivative-control` and
   `lem-stage1-inversion-derivative-transport` were RETRACTED 2026-07-28 —
   read their demoted shard bodies and `docs/LEARNINGS.md` 2026-07-28 for
   the exact defect loci; their CONTRACTS are undisputed and byte-frozen).

## What is settled (do not relitigate)

- The two round-1 bridge contracts (§1.1, §1.2 of the round-1 design)
  drew no audit finding; carry them forward verbatim unless your
  consumer trace forces a change (justify any change).
- Audit finding 4: `lem-stage1-polar-coherence-naturality` is dropped from
  the repaired 13e deps; synchronization is stated solely by identical
  explicit map/domain/image + inverse uniqueness.
- Audit finding 3: the bridges are a BYPASS discarding u_grp, not a
  discharge of the W93 missing premises — say so plainly.
- The binding process law (LEARNINGS 2026-07-28): every map a root binds
  by definite description must have a provider external supplying the
  TYPED WITNESS, not a same-named conclusion. Apply it to EVERY row you
  design.

## Your task — write `DESIGN-13E-BINDER-v2.md` in this directory

Extend the round-1 plan to the full explicit-binder spine that the audit
and the retraction demand. Deliver, with EXACT verbatim-landable registry
texts (one-line `contract:`, `defs:`, `deps:`; NEW / AMENDED /
BYTE-UNCHANGED classification per shard):

1. The two bridge rows (from round 1, re-examined).
2. **An explicit-binder smooth-operations bridge** (audit finding 1): a
   row asserting smoothness (and the scalar covariance actually needed by
   the rows-14+ consumers `lem-stage1-uniform-inversion-isolation`,
   `lem-stage1-quotient-left-inversion`,
   `lem-stage1-quotient-inversion-index-data` — read them) for the
   explicit maps mu_pol, sigma_pol, derived from the typed T0 layer
   (polar-retraction, smooth-polar-inverse, smooth-unitary-atlas) WITHOUT
   routing through the anaphoric group-laws family. Decide and state
   whether the rows-14+ consumers then need a deps swap (they are all
   `stated`/`af: none` — a deps swap there is cheap; verify none is
   validated).
3. **The re-derivation contracts/plans for the retracted pair**: does the
   UNDISPUTED contract of `lem-stage1-inversion-derivative-control`
   re-elevate soundly once its workspace registers the RIGHT externals
   (which? — per the adjudication the defect was using the group-laws
   closeness for the polar factor without a typed witness; your round-1
   bridge rows supply exactly the typed closeness — check they suffice for
   node 1.3's role), or does its deps line need the bridges added
   (deps-only amendment, contract byte-unchanged)? Same question for the
   transport (whose polar/graph identifications were adjudicated SOUND;
   the failures were 1.5.5's smooth-ops use and 1.6's parent
   substitution — with a repaired parent and your smooth-ops bridge, state
   the exact external list that makes each node derivable).
4. The repaired 13e (round-1 §1.3 minus coherence-naturality).
5. **Elevation order and budgets** (strictly sequential; observed range
   5–22 nodes; caps below 26): bridges → smooth-ops bridge → control →
   13e → 13g transport. Per workspace: the exact external-registration
   list satisfying the typed-witness law.
6. **Consumer re-check** (row 13 (A_5)–(A_7) verbatim; rows 14+ with the
   smooth-ops-bridge deps decision applied) and a cost table.

Do NOT edit anything under `argument/`, `definitions/`, `proofs/`, or
`report/`. Write ONLY the design file named above.
