# BRIEF — hostile audit of DESIGN-M24-NONTRIVIALITY.md (fresh verifier)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-M24-NONTRIVIALITY.md` and must assume it is wrong until proven
otherwise. It repairs the verifier-established M24 contract-level gap
(`dim S_{P_j} >= 1` underivable; challenges ch-94ae993f6abc0f5b /
ch-7411a0325c917f52 / ch-37eff8dcb9a3b5d1) by selecting option (a): ONE
new ledger-bound provider row `lem-maincb-corner-nontriviality` plus a
deps-only M24 amendment (contract byte-unchanged), rejecting options (b)
and (c). Both directions need attack: an under-repaired design re-parks
M24 after an expensive re-seed; an over-strong or false provider contract
wastes an elevation and can poison M28's launch. Finding an error in
EITHER direction is a BIG SUCCESS. The design's own §8.4 lists its three
most likely failure modes — attack those FIRST, then everything else.

## Your target

`docs/plans/2026-08-02-M24-NONTRIVIALITY-design/DESIGN-M24-NONTRIVIALITY.md`.

## Audit against (read all)

1. `docs/plans/2026-08-02-M24-NONTRIVIALITY-design/BRIEF-M24-NONTRIVIALITY.md`
   (what was asked — check every deliverable and every hard constraint).
2. The defect record: the three challenges quoted verbatim in that brief;
   the aborted tree at
   `/tmp/claude-1000/-home-tobiasosborne-Projects-almost-idempotent-stochastic-maps/3dd18513-bf41-437f-80f3-7515872b1529/scratchpad/stuck-lem-maincb-stage1-maximality/`
   (read-only forensic evidence). Does the design actually answer each
   challenge, or merely relocate the gap?
3. `refs/kitaev-2405.02434/approximate_algebras.tex` — CHECK EVERY CITED
   LOCUS against what the design claims (esp. 407-456 the epsilon-C*
   axioms and inclusion clauses; 917-929 P_alternatives + "nonvanishing";
   1054-1084 compressed corners incl. the deliberately EXCLUDED sentence
   at 1066; 1367-1368; 1417-1428; 1477-1479). The design claims the
   provider can be proved WITHOUT the line-1066 sentence — verify the
   claimed derivation chain actually closes from the cited clauses alone.
4. The frozen T0 exports the provider consumes — verify each supplies
   EXACTLY what the design's proof plan (Deliverable 4) needs, at the
   claimed typing:
   - `argument/lemmas/lem-maincb-direct-corner-envelope.md` (M04) and
     `proofs/lem-maincb-direct-corner-envelope/export.md` — does its
     validated conclusion type the SAME singleton vector space `S_{P_j}`
     as an extended L^0*epsilon-C*-algebra WITH a furnished unit that is
     an ELEMENT of that space? Does it apply to a singleton {j} WITHOUT
     presupposing S_{P_j} != 0 or a partition state? (Design risk #1.)
   - `argument/lemmas/lem-maincb-reset-constant-ledger.md` (M18),
     `lem-maincb-structural-domain-ledger.md` (M20),
     `lem-maincb-witness-arithmetic.md` — do their frozen contracts
     really export the chain epsilon <= W.e_env <= e_env^0,
     L^0*epsilon <= W.L*epsilon <= W.K_call*epsilon <= W.r_reset, and
     W.r_reset <= [2*(1+K_disp)*D_*]^{-1} with K_disp positive and
     D_* >= 1, WITHOUT any unregistered sign/order assumption? Reproduce
     the arithmetic line by line. (Design risk #4/§5.1.)
   - `definitions/def-extended-delta-inclusion.md` — do its clauses
     really yield BOTH the delta-projection estimates for P_j = w(e_j)
     AND | ||P_j|| - 1 | <= W.c0_cb*epsilon from ||e_j|| = 1? Check
     `def-projection-basis.md` actually gives e_j = e_j* = e_j^2 and
     ||e_j|| = 1.
   - `definitions/def-delta-projection.md` — is "nonvanishing" a typed
     predicate of this shard with the quantitative second alternative,
     such that the provider's displayed inequality DISCHARGES it, or is
     there a big-O formalization gap (design risk #2)? If a bridge is
     missing, that is a FINDING.
5. The rejection of option (b): independently verify the consumer-survey
   table (Deliverable 1.1) against the frozen contracts —
   `lem-maincb-corner-equivalence` (M10), `lem-maincb-one-class-extension`
   (M25), `lem-maincb-stage3-call-envelope` (M19-S3),
   `lem-maincb-binary-block-merge` (M26),
   `lem-maincb-stage3-finite-recombination` (M27),
   `def-maincb-partition-state` reflexivity. If ANY listed blocking clause
   is misquoted, or if (b) is in fact viable, that is a major finding.
6. The rejection of option (c): M22/M23/M18 frozen-T0 status
   (`argument/lemmas/` status/af fields) and the claim that any additive
   premise collapses into (a).
7. `docs/plans/2026-08-01-MAINCB-REPAIR-design/DESIGN-MAINCB-REPAIR-v2.md`
   sect-4 (the ratified M24/M28 rows) — the design keeps M24's contract
   and M28's row byte-unchanged; verify no silent drift anywhere in the
   package tables.
8. `docs/LEARNINGS.md` 2026-07-28 typed-witness laws i/ii — is the
   provider contract law-compliant (every definite description typed
   through W; no anaphoric constant)? Is `lem-maincb-witness-arithmetic`
   genuinely among the deps needed, or a spurious import (deps hygiene)?

## Specific attack surface

- **The provider contract line itself:** is it one physical ASCII line,
  free of numerical universal constants, and TRUE as stated? Try to
  construct a counterexample: an extended epsilon-C*-algebra A and
  extended W.c0_cb*epsilon-inclusion w where some P_j = w(e_j) fails the
  claimed norm estimate or S_{P_j} = 0 at the permitted scales. NOTE the
  contract has NO near-unit hypothesis ||w(I_{C^m}) - I_A|| <= W.c0_cb*epsilon
  (M24 has it; the provider drops it) — is the provider still true
  without it, and is dropping it deliberate over-generality or a defect?
- **The M04 singleton application:** M04 (`lem-maincb-direct-corner-envelope`)
  was designed for the partition-state corner family — check its exact
  frozen contract hypotheses: does it require a supplied MAIN partition
  state tied to A,w (which the provider does NOT have — exactly the
  gap flagged in ch-94ae993f6abc0f5b for def-maincb-partition-state), a
  near-unit clause on w, or one-dimensionality anywhere? If M04 cannot be
  invoked with the provider's hypotheses alone, the design fails at its
  core step — ROUTE-LEVEL ALARM.
- **The unit-nonzero arithmetic (§4.1 node 1.4, §5.1):** the design
  derives L^0*epsilon <= 1/2 via W.r_reset <= [2*(1+K_disp)*D_*]^{-1}.
  Check the witness-arithmetic/M18 contracts actually contain that term
  and binder; check no hidden c0 >= 1 (§5.2) and no hidden K_disp >= 0
  beyond what is registered.
- **The unit-membership typing (design risk #1/#3):** does the M04 export
  give the unit as an element of S_{P_j} (not of an isomorphic copy)? Is
  "a vector space containing a nonzero element has dim >= 1" legitimately
  common-knowledge under this repo's L2, applied to the exact S_{P_j}?
- **The rebuilt M24 tree (Deliverable 4.2):** budgets 5/2/9 plausible?
  Does node 1.3 (upper bound via M23) really only need the admissibility
  predicate from 1.1 plus M23's export? Does anything still smuggle
  P_j != 0 => S_{P_j} != 0?
- **No-T0-invalidation (Deliverable 7.1):** independently verify no
  amended/new row forces any change to a validated row's contract, a
  locked def, or a byte-matched external in a validated workspace.
- **Elevation-guidance consistency:** the M24 shard's binding elevation
  guidance (constant-choice FIRST child, no pending-sibling citations,
  typed-reset provider rules) — is the design's §8.2 guidance consistent
  with it, or does it contradict the shard's binding text anywhere?

## Deliverable — write `docs/plans/2026-08-02-M24-NONTRIVIALITY-design/AUDIT-M24-NONTRIVIALITY.md`

- Verdict per deliverable section (1-8): VALID / VALID-WITH-CORRECTIONS
  (state the exact corrected text) / REFUTED (show why).
- Verdict on each of the two package rows (the provider contract; the
  M24 deps-only amendment): same scale, clause by clause for the provider.
- Verdict on the option-(b)/(c) rejections: CONFIRMED / OVERTURNED.
- Final disposition: DESIGN-CONFIRMED (ready for user ratification, with
  any exact corrections listed) / DESIGN-REFUTED (which defect remains
  open and why) / ROUTE-ALARM.
- Cite every check with exact loci (file:line).

## Hard constraints

- Write ONLY `docs/plans/2026-08-02-M24-NONTRIVIALITY-design/AUDIT-M24-NONTRIVIALITY.md`.
- No repairs beyond stating exact corrections; no status promotion; nothing
  here is rigorous. NOT-IN-LOCAL-REFS discipline applies (L1): if a claimed
  ground truth is not at the cited locus, that is a FINDING, not something
  to patch around.
