# BRIEF — fresh hostile audit of DESIGN-MAIN-STRUCTURE-v3.md (fourth stage)

You are a fresh, independent, HOSTILE auditor. You did NOT write any of the
three designs or the two prior audits. Assume `DESIGN-MAIN-STRUCTURE-v3.md`
is wrong until proven otherwise. The v4.1 factoring fell, the first repair
fell, and v2 fell — each to a fresh audit. Finding a defect here — a
non-closed envelope, a leaked scale factor, a circular invariant, theorem
content in a definition, a hidden dimension-dependence, a prior finding
papered over — is a BIG SUCCESS.

## Your target

`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v3.md` —
a P0 definition-provisioning gate (§1), a canonical scale discipline (§2),
pre-gate rows (§4), the unchanged G-S1 gate (§5), post-gate call envelopes
M19-S1/S2/S3 + the invariant row M19-R (§6), the MAIN structural targets
(§7), hazards R19/R21/R22 (§8), dimension-freeness (§9), a serial landing
order (§10), a complete escalation ledger (§11), and a disposition of EVERY
`AUDIT-MAIN-STRUCTURE-v2.md` finding (§12).

## Audit against (read all)

1. `AUDIT-MAIN-STRUCTURE-v2.md` — the binding re-audit. Its §10 gave eight
   exact requirements; verify each is REALLY met (its two fatal defects: A —
   M19 non-closed/acyclic with the unabsorbed C_s2 scale; B — the dropped
   definition gate). For EVERY finding, verify v3 §12 genuinely dispositions
   it, not by renaming.
2. `AUDIT-MAIN-STRUCTURE.md`, `BRIEF-MAIN-STRUCTURE.md`,
   `BRIEF-MAIN-STRUCTURE-REPAIR-v3.md` — original constraints; the v3
   brief's "do not redo" list (M07–M13, the two-induction architecture,
   R19 measure, G-S1 placement were CONFIRMED and to be kept; retained
   contracts verbatim). Diff retained rows against v2; any silent contract
   change is a finding.
3. `refs/kitaev-2405.02434/approximate_algebras.tex` — check every cited
   locus (esp. 1054–1082, 1162–1187, 1239–1359, 1414–1450, 1451–1475,
   1508–1557) against what each row claims.
4. Landed shards: the `lem-compcb-*` rows, `lem-extcb-*` rows, `conj-extcb`,
   `lem-extcb-four-corner-merge`, `lem-extcb-exact-target-correction`,
   `lem-maincb-error-improvement` (narrowed contract stays VERBATIM — only
   deps may change), `lem-thmainext-conditional`. Every v3 dep must use only
   what the landed contract exports.
5. `DESIGN-FUDW-DECOMP-v4.1.md` §2.4 rows 221–228, §3.3, §4.1 (the
   datum-only definition specs ~403–428), R17–R23, R35, R36.
6. `definitions/INDEX.md` and `definitions/README.md` — the four P0
   proposals must be well-formed by the repo's definition schema and
   contain NO theorem content (R35). `def-operator-space` claims a
   byte-match candidate at TeX 1451–1475 — verify the locus actually
   supports a `cited` definition.

## Specific attack surface (check each, then hunt beyond)

- **The M19 replacement (the load-bearing repair; §2, §6).** Attack
  hardest: (a) Are M19-S1/S2/S3 genuinely CLOSED conditional envelopes —
  every supplied current map named as a hypothesis with its defect bound,
  nothing "constructed from w", no assertion of later existence? (b) Trace
  the claimed acyclicity: does any envelope still semantically require
  M25/M27 output? (c) The scale discipline: M13 outputs s_EXT = C_s2·t,
  M16 accepts s_EXT and outputs defect ≤ D₂·t with C_s2 absorbed into
  D₂ — verify this against `conj-extcb`'s actual landed contract (is
  applying EXT-CB at scale s_EXT legitimate, and is the output really
  expressible at base scale t with a UNIVERSAL enlarged D₂)? (d) M20's
  finite maximum K_call = max{1, L, c₀, K₁, K₂, K₃}: is every K_i produced
  by an earlier row, and does M20's guard now genuinely cover every literal
  call each structural target makes (no call type omitted)?
- **The invariant row M19-R (§6–7).** Is RI(U): d_U ≤ c₀·ε_U (i) actually
  strong enough for the M25 induction (walk the M25 proof plan step by
  step); (ii) actually PRESERVED by each call type (the row's proof
  obligation — is the claimed derivation from IMPROVE-CB's c₀ legitimate
  given `lem-maincb-error-improvement` is a `stated` target, not a proved
  input — does anything pre-gate consume M19-R)?; (iii) non-circular (ε_U
  is the CURRENT corner's ambient defect — produced by which row at the
  time of the call)?
- **The P0 definitions (§1).** For each of the four: any smuggled
  existence/estimate/success clause (R35)? Is the partition-state's
  "when that relation is an equivalence, its class family" clause
  data-only or a hidden theorem? Is the `def-operator-space` byte-match
  candidate honest (TeX 1451–1475)?
- **Pre-gate rows (§4).** Diff against v2's M01–M18: verbatim retention
  except named corrections (M03 dep rewire; M05/M07/M09 exact ids). Verify
  the exact-id dependency lists against the landed shard ids
  (`lem-compcb-amplified-compression`, `-identities`,
  `-almost-containment`, `-rectangular-product`, etc. — each must exist and
  export what the row needs). Does anything pre-gate now depend on a P0
  definition that makes it non-landable before ratification — is P0's
  position in the landing order honest?
- **Hazards (§8).** R19: strict measure at the actual call sites. R21: the
  two measures (|C|−r, q−r) and the M28-only join retained. R22: the new
  subsection must record the M11→M12 production/consumption chain with the
  canonical data.
- **Dimension-freeness (§9).** The C_s2 absorption and the K_call finite
  maximum must stay universal; any n-, block-count-, class-count-, or
  stage-index dependence is a ROUTE-LEVEL ALARM.
- **Landing order (§10).** Genuine topological sort: P0 first, G-S1
  placed exactly as in v2, no step's inputs missing at execution time.
- **Escalation ledger (§11).** The v2 audit's §9 omission list is the
  floor: four definition packages, M09 amplified-compression dep, the M19
  replacement + M16/M20 scale correction, the future
  `lem-thmainext-conditional` deps rewire. Verify all present and nothing
  new is missing (any landed contract v3 needs to read differently must
  appear).

## Deliverable — write `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v3.md`

- Verdict per P0 definition (all 4), per row (pre-gate and post-gate,
  including M19-S1/S2/S3 and M19-R), per hazard adjudication, per §12
  disposition claim, and for the landing order and escalation ledger:
  VALID / VALID-WITH-CORRECTIONS (state them exactly) / REFUTED (show the
  defect concretely).
- Final disposition: REPAIR-CONFIRMED (land v3 with any corrections, gated
  on P0 + G-S1) / DESIGN-REFUTED (what fails; what a fourth repair must
  change) / ROUTE-ALARM (a genuine obstruction — describe it).
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v3.md`.
  Touch nothing else.
- No repairs beyond stating corrections; no status promotion; nothing here
  is rigorous. NOT IN LOCAL REFS discipline applies.
