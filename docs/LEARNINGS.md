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

## 2026-07-26 — "Route F proved-mod-audit COMPLETE": PARTIALLY RETRACTED (15 rows demoted to GAP)

- **Claimed:** session 23 (2026-07-24) closed with the headline "ROUTE F IS proved-mod-audit
  COMPLETE" (`docs/worklog.md:1233`, echoed in the fr frontier trail and session summaries):
  every link of the Route-F chain carried a worker paper-proof with a hostile wave-level VALID,
  so the remaining work was presented as *elevation/verification only — no new mathematics*.
- **Why wrong (in part):** the af-decomposition of the large chain (the `aism-fudw` design,
  verdicts v1–v3 in `docs/plans/2026-07-24-fudw-decomposition-artifacts/`) forced every step
  into a one-line contract with explicit domains, and under that stricter bar a subset of the
  proved-mod-audit record FAILED hostile review: fourteen K-ledger rows assert their
  inequalities on domains "stronger than the verified ledger" (η_A is only the
  source-linearization radius — each row needs its own dependency-produced local radius,
  e.g. `(C_T+C_Δ′)η ≤ ½`); the MAIN-CB assembly rows carried relocation-not-factoring residue;
  the Stage-1 polar estimates existed only as prose (no formula-level contract); and one
  EXT-chain approximation step had no supporting lemma (EA). As stated, those proofs are not
  theorems. VERDICT-FUDW-DECOMP-V3.md §2.1 (BLOCKER) prescribed stripping all fifteen ids to
  uncontracted GAP reservations (Registry impact C) — i.e. their proved-mod-audit status was
  WITHDRAWN, not merely refined.
- **Caught by:** the fresh-codex hostile design verdicts v1–v3 (2026-07-24), reviewer ≠ author.
- **Resolution:** the fifteen ids are held as GAP reservations (DESIGN-FUDW-DECOMP-v4.1.md §2.6,
  the four families GAP-EA / GAP-S1-POLAR-CONTRACT / GAP-MAIN-STRUCTURE / GAP-LEDGER-DOMAINS);
  bead `aism-0163`; phase-4 work re-proves them with derived local domains. The headline was
  never formally retracted here until today (user escalation 2026-07-26) — later agents kept
  repeating both "complete mod-audit" and "genuine open mathematics remains" without
  reconciling them. THE LESSON: a status-bearing HEADLINE demoted by a later verdict must get
  a LEARNINGS entry in the same commit as the demotion (Rule 9 applies to claims, not just
  files). What remains true: Route F requires no conjecture and no new idea; what was false:
  that only verification labour remained.

## 2026-07-28 — `lem-stage1-inversion-derivative-control` (97th) + `lem-stage1-inversion-derivative-transport` (107th): af validations RETRACTED (defective polar-inverse synchronization; T0 107 → 105)

- **Claimed:** both results were af-VALIDATED (2026-07-27 first-pass 10/10 zero challenges; 2026-07-28
  run-2 13/13 taint clean respectively) and banked as the 97th and 107th rigorous results with passing
  oracle + `fr verify` certificates. The CONTRACTS are not in dispute — only the validated proofs.
- **Why wrong:** both proof bodies identify the anaphorically-bound polar inverse of an imported
  contract (`lem-stage1-approximate-group-laws` u_grp; the parent control lemma's u_I) with the
  explicitly typed `lem-stage1-polar-retraction` inverse u_pol without a typed preimage witness
  h_X satisfying X = u_grp(X)·h_X (resp. u_I): the available exact identity X = u_pol(X)·h_pol(X)
  is paired with u_pol, and taking h_X = h_pol(X) assumes the equality being proved;
  `lem-stage1-polar-coherence-naturality` is conditional on TWO typed polar data and only one is
  available. Loci: control export node 1.3 ("the common polar inverse … identified across admissible
  polar data"); transport export nodes 1.3 (second half), 1.5.5, and 1.6. This is exactly the
  missing-h_X obstruction that three W93 verifier cohorts had established for transport 13e — the
  earlier cohorts that validated these two trees accepted the same inference the W93 cohorts
  (correctly) rejected.
- **Caught by:** the W97 design-audit chain, NOT the runs' own verifier cohorts: the hostile audit of
  `DESIGN-13E-BINDER.md` raised the allegation (AUDIT-13E-BINDER.md finding 2, MAJOR), and an
  independent fresh-codex adjudication primed to refute it instead CONFIRMED it per-locus
  (`docs/plans/2026-07-28-13E-BINDER-design/ADJUDICATION-T0-ALLEGATION.md`: T1 DEFECTIVE, T2
  DEFECTIVE, CASCADE exactly these two). The adjudicator also partially REFUTED the allegation's
  W93-equivalence claim (for X = U† the S_delta-membership subproblem IS discharged by the retraction
  contract's inner inclusion) — the defect is the preimage/synchronization step alone.
- **Resolution:** statuses mechanically demoted proved→stated / af validated→seeded same day
  (linker-verified: T2 was T1's only validated dependent, so the demotion is closed under the pair);
  report shards 48/51 + PROVENANCE claim rows corrected; stats regenerated (T0 = 105); workspaces and
  ledgers retained as re-elevation bases; re-derivation on an explicit-binder dependency spine folded
  into the 13e repair campaign (design round v2; bead `aism-e1qs`). Sketch superseded (v37).
- **Process lesson (recorded):** a verifier cohort can accept an inference that a differently-framed
  cohort rejects — cross-workspace CONSISTENCY of what "the same map" means is not enforced by
  per-node verification. The 13e repair design v2 must carry an explicit-binder discipline for every
  map a root binds by definite description (the 13g external-provider lesson, now strengthened: the
  provider must supply the TYPED WITNESS, not merely a same-named conclusion).

## 2026-07-28 (second entry) — the Stage-1 binder sweep: four more af validations RETRACTED (T0 105 → 101); fourteen certified sound

- **Claimed:** `lem-stage1-approximate-group-laws` (95th), `lem-stage1-smooth-unitary-operations`
  (100th), `lem-stage1-maurer-cartan-transport` (104th), and `lem-stage1-polar-path-transport`
  (106th) were af-VALIDATED and banked. Contracts are NOT in dispute — only the validated proofs.
- **Why wrong:** the same untyped-map inference class as the first 2026-07-28 retraction, found by a
  comprehensive fresh sweep over all 18 remaining Stage-1 polar T0 exports
  (`docs/plans/2026-07-28-13E-BINDER-design/SWEEP-ADJUDICATION-STAGE1.md`): group-laws node 1.1.2
  invokes coherence on children exporting only anaphoric components; smooth-operations nodes
  1.2.1–1.2.2/1.3.1.2/1.3.2 attach the typed smooth inverse to the anaphoric group inverse;
  maurer-cartan-transport node 1.3.3 asserts a derivative equality whose pointwise-equality premise
  its own sibling records as absent (a sound bypass exists in nodes 1.3.4–1.3.7 — pruning +
  revalidation suffices); polar-path-transport node 1.3.1 attaches the parent's anaphoric path
  formula to the root's explicit binder by sameness of notation.
- **Caught by:** the second allegation wave of the W97 audit chain (AUDIT-13E-BINDER-v2.md finding
  1) routed into a comprehensive per-target sweep adjudication rather than piecemeal checks. The
  sweep also CERTIFIED FOURTEEN trees sound — including the entire typed backbone
  (polar-retraction, coherence-naturality, graph rows, smooth atlas/polar-inverse, group
  membership/closeness, path-admissibility, scalar arithmetic, and transports 13a/13b/13d) — so
  the defect class is now settled for the whole Stage-1 layer in one pass, cascade CLOSED (no
  other validated result descends from the demoted four).
- **Resolution:** four statuses mechanically demoted proved→stated / af validated→seeded; report
  shards 47/49/50/51 + PROVENANCE corrected; stats regenerated (T0 = 101); workspaces/ledgers
  retained; repairs folded into the W97 explicit-binder campaign design v3 (bead `aism-e1qs`).
- **Root cause (sweep's finding, recorded verbatim in substance):** the elevating cohorts
  systematically treated repeated notation and definite descriptions as binder unification across
  opaque theorem boundaries — same-named anaphora elevated into missing equality premises.
  Ordinary uniqueness remains valid in single-construction chains, which is exactly why fourteen
  trees survive.

## 2026-08-01 — M25, M19-S2, M19-S3: three af-VALIDATED certificates carried latent unregistered-premise gaps (demoted, re-validation pending)

- **Claimed:** `lem-maincb-one-class-extension` (M25, 166th rigorous result),
  `lem-maincb-stage2-call-envelope` (M19-S2, 159th), and
  `lem-maincb-stage3-call-envelope` (M19-S3, 160th) were banked af-VALIDATED T0
  on 2026-08-01.
- **Why wrong (the certificates, not the statements):** each validated tree
  used an inference not derivable from its REGISTERED premises. M25 (nodes
  1.1.2.2/1.1.3.2) inferred "bijective hence extended isomorphism" from old
  M19-R's export, which supplies only recorded-number/unit bounds and
  conditional bijectivity — never the extended-INCLUSION typing that
  `def-extended-delta-inclusion` requires of an isomorphism. M19-S2 (node 1.4)
  and M19-S3 (node 1.3.3) applied defect/tolerance monotonicity without
  importing `lem-maincb-extended-inclusion-monotone` — the exact fact the
  repo had just factored for M18 after verifiers rejected the same implicit
  step in M21. No countermodel to the CONTRACTS is known; the defect is that
  the banked certificates do not prove their roots from their registered
  inputs (the exact-input standard).
- **Caught by:** the aism-mc54 design round (fresh codex) alleged the M25 gap;
  the fresh hostile audit (`AUDIT-CONSUMER-REPAIR.md` F1/F5) independently
  CONFIRMED it by reading the exports, and widened the finding to M19-S2/S3.
- **Resolution:** user-ratified 2026-08-01 (in-session): all three demoted
  proved->stated / validated->none (T0 159->156), contracts byte-identical;
  fresh re-validation with the explicit typed providers
  (`lem-maincb-reset-output-typing`, `lem-maincb-extended-inclusion-monotone`)
  required before any re-bank. The oracle verdicts staled automatically with
  the ledger changes. A retraction here is the rigour machinery succeeding:
  the gap classes were surfaced by later, stricter verifier cohorts within
  the same day and nothing downstream was banked on the flawed certificates
  (M26/M27/M28 remained unproved).

  **Propagation addendum (same date):** the linker's status-propagation law
  then suspended banked M18 (`lem-maincb-reset-constant-ledger`) and M20
  (`lem-maincb-structural-domain-ledger`) — their certificates are intact and
  their workspaces preserved, but they rest on the demoted M19-S2/S3
  premises; they re-flip mechanically once those re-validate (T0 156->154
  in the interim).

## 2026-08-08 — `ex-hume`: “distance to every stochastic idempotent equals one common value” is false

- **Claimed:** `ex-hume` carried `proved-mod-audit` / `af: seeded` with the historical contract: “The explicit 3x3 family P_s=I-u_s v_s^T (v_s=(1,-1+s,-s), u_s=(1-s+s^2,-s,0)^T) is a signed affine retraction with neg mass delta=s^2 whose distance to every stochastic idempotent is 2s-2s^2+2s^3 = 2 sqrt(delta)+O(delta): no bound C delta^beta with beta>1/2 holds, so the exponent 1/2 in op-classical/op-npps is sharp.”
- **Why wrong:** for `0<s<1`, put `a=1-s+s^2`.  Although `v_s^T 1=0`, `v_s^T u_s=1`, and the only negative entry of `P_s` is `(P_s)_{23}=-s^2`, the stochastic idempotent `I_3` satisfies `||P_s-I_3||_{infinity->infinity}=||u_s v_s^T||_{infinity->infinity}=2a`, while the claimed common value is `2sa`; the difference is `2(1-s)a>0`.  Thus the per-idempotent equality is false.  The old contract also omitted `0<s<1`, left its quantifiers and asymptotic variable unstated, and mixed in the out-of-scope `op-npps`.
- **Caught by:** the fresh hostile audit of `DESIGN-EXHUME-SHARPNESS.md`, finding 3, after the paper faithfulness audit had already corrected “distance to every” to a distance-to-set candidate.
- **Resolution:** replace the malformed contract by the fully quantified false proposition solely so it can be honestly marked `disproved`; set `af: none`; delete and never resume the stale old-contract workspace; record the corrected 3x3 distance-to-set formula only as a non-rigorous candidate; and use `cor-classical-sharpness`, via the direct stochastic 4x4 PRH family, as the separately elevated active carrier.  All active consumers are covered by the 50-locus manifest in `DESIGN-EXHUME-SHARPNESS-V2.md`.
