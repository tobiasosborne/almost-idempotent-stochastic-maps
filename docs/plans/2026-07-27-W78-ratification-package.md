<!--
ROLE: the consolidated USER RATIFICATION package for the W75–W78 critical-path
  de-risk campaign (risk register docs/plans/2026-07-26-critical-path-risk-register.md).
STATUS DISCIPLINE (L0): a planning/escalation artifact; promotes NOTHING;
  every referenced design is NON-RIGOROUS by its own header; op-classical is
  OPEN; T0 = 83 and unchanged.
CANONICAL SOURCES: the four landable design files named in §1 are the single
  sources of truth for every proposed contract. This package intentionally
  quotes NO contract text (anti-drift): ratification is of those files as
  audited, plus the enumerated corrections.
NOTHING IN THIS PACKAGE LANDS WITHOUT EXPLICIT USER RATIFICATION.
-->

# W78 consolidated ratification package (2026-07-27)

## 0. What is being asked

The 2026-07-26 user mandate ("de-risk the critical path, riskiest first")
is **executed**: all four fronts of the risk register are now designed and
fresh-hostile-audited to a landable state, with **zero route-level findings**
across the campaign (19 codex jobs on 2026-07-27 alone: 11 hostile audits,
7 prescribed repairs, 1 design; plus the 8 session-29 jobs). No
dimension-dependent constant, no error in Kitaev's theorems, no unclosable
gap was found anywhere; every defect was in this repo's contract factoring
and each now has an audited repair.

This package asks the user to ratify the four landable designs (with the
enumerated corrections folded in verbatim at landing), decide the four
decision points in §3, and authorize the serial landing/elevation campaign
in §5.

## 1. The four landable designs (canonical sources)

| front | landable design | final audit (disposition) | audit trail |
|---|---|---|---|
| 1 — S1-POLAR | `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md` — 13 core analytic rows, 7 parameterized transport helpers (13a–g), 6 downstream contract repairs, 2 datum-only def shards | `AUDIT-S1-POLAR-v6.md` — **LAND** (one documentary correction) | 7 hostile stages (audits of v2–v6); v5 stage caught a pre-existing quantifier defect all earlier audits missed |
| 2 — MAIN-STRUCTURE | `docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md` — P0 definition gate (4 datum-only shards), pre-gate rows M01–M18, G-S1 gate, call envelopes M19-S1/S2/S3 + invariant row M19-R, structural targets M20–M28 | `AUDIT-MAIN-STRUCTURE-v5.md` — **REPAIR-CONFIRMED** | 6 hostile stages; includes one auditor-constructed counterexample (M₄, killed by the restored unit clause) |
| 3 — LEDGER-DOMAINS | `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md` — all 14 K-ledger rows with derived local radii, corrected Υ′ row, terminal η_K, D2/D3 reconnection, guarded parent-wiring proposal | `AUDIT-LEDGER-DOMAINS-v2.md` — **LAND-14** (two exact corrections) | 3 stages (design, audit, repair) + fresh re-audit |
| 4 — F0 assembly | `docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md` — two lift rows (`lem-routef-f0-ucp-lift`, `lem-routef-f0-defect-identity`), the strengthened `lem-routef-k-ledger` replacement contract, `lem-routef-f0-assembly`, OR-route root wiring | `AUDIT-F0-ASSEMBLY.md` — **LAND** (four corrections) | design + fresh audit; every seam recomputed as EXACT MATCH (single K, single η_K, C = K+4√(2K), dimension-free) |

## 2. Corrections to fold in VERBATIM at landing (all prescribed by the audits)

**Front 3 (ledger), from `AUDIT-LEDGER-DOMAINS-v2.md` §7:**
1. ρ_id → ρ_id^corr = min{ρ_θ, ρ_AI, ε_E/C_A} (exposes the η < 1/4 domain of
   `lem-kitaev-almost-idemp-audit`; no downstream radius changes).
2. Wording: "unital extended isomorphism" → "extended isomorphism, with unit
   defect at most C_V·η".

**Front 4 (F0), from `AUDIT-F0-ASSEMBLY.md` §§0–6:**
3. Reclassify the corrected `lem-routef-k-ledger` contract as a
   **strengthened replacement** (a new ∀n ∀Q ∀η parent proof obligation
   requiring its own fresh prover + fresh hostile verifier) — NOT a binder
   edit inherited from the W74F-H verdict.
4. Typing: use the canonical complexification Q_ℂ in Φ = J·Q_ℂ·D in both
   lift rows and the ledger parent.
5. The telescope contracts must, at landing, quantify a common
   (𝓑, Φ, Δ, Υ, η) datum (contract-closure correction).
6. Root wiring per the audit's §3 (depends on decision D1 below).

**Front 1 (polar), from `AUDIT-S1-POLAR-v6.md` §4:**
7. Documentary only: add the three mechanical label substitutions to
   `DESIGN-S1-POLAR-v6.md` §0's diff accounting.

**Front 2 (MAIN):** no residual corrections — v5 audited clean.

## 3. USER DECISIONS required (none pre-empted; D1 changes a landed contract)

- **D1 — the `op-classical` sharpness split** (from `AUDIT-F0-ASSEMBLY.md`
  §§0.2, 4; this is a change to a LANDED root contract and is entirely the
  user's call):
  - *Option A (audit-recommended, cleanest):* make `op-classical`'s
    contract the upper stability bound only; sharpness lives in `ex-hume`
    (already a separate obstruction row). Root wiring:
    `routes: [lem-routef-f0-assembly] | [thm-classical-factorization; prop-approx-simplex]`.
  - *Option B (keep the literal compound contract):* `ex-hume` becomes an
    UNCONDITIONAL root dep shared by both routes (`deps: ex-hume` + the
    same routes block), and `ex-hume` (currently proved-mod-audit,
    af: seeded) must be af-elevated before root discharge.
- **D2 — ratify the six new definition shards** (all datum-only, R35-clean
  per the final audits): `def-operator-space` (CITED, byte-verbatim from
  `approximate_algebras.tex:1453-1464`, SHA prefix e7eb512a2ec2438d),
  `def-maincb-reset-state`, `def-maincb-raw-call`,
  `def-maincb-partition-state` (ORIGINAL drafts, schema-complete in
  `DESIGN-MAIN-STRUCTURE-v5.md` §1), `def-approximate-unitary-space`,
  `def-stage1-polar-witness-data` (specified in `DESIGN-S1-POLAR-v6.md` §8).
- **D3 — UCP vocabulary** (from `AUDIT-F0-ASSEMBLY.md` §1.1): provision a
  canonical "unital completely positive map" definition shard, OR grant an
  explicit L2 textbook-common-knowledge exemption (recorded).
- **D4 — authorize the strengthened `lem-routef-k-ledger` replacement**
  (correction 3 above): the contract text at
  `DESIGN-F0-ASSEMBLY.md` §1.3 with the F0 audit's corrections, its ten
  parent deps, and the release of the DO-NOT-REWIRE guard at the
  designated step of §5 (and ONLY there).

## 4. Explicitly escalated contract/dependency changes (per the designs' own ledgers)

- MAIN v5 §11 (complete escalation ledger): the four P0 shards; M03's
  dependency rewire (contract stays byte-identical to the landed
  `lem-maincb-error-improvement.md:4`); the S2/S3 partition-state identity
  constraints; M13's corner-algebra producer + threshold absorption; the
  future `lem-thmainext-conditional` deps rewire (post-validation only).
- Polar v6: the six downstream contract repairs (all six ids are NEW rows —
  no af-VALIDATED contract is touched; re-validation is NOT triggered).
- Ledger v2 §6.2: the `lem-routef-k-ledger` parent wiring
  (PROPOSED-ONLY; guard stays until D4 + the §5 step).

## 5. Serial landing/elevation order (merged; from the four audited orders)

0. **Ratification** (D1–D4 + the §2 corrections).
1. **Independent quick wins** (no gates): land + af-elevate
   `lem-routef-f0-ucp-lift` (3/2) and `lem-routef-f0-defect-identity`
   (5/3); af-elevate F2 and F3 (`proved-mod-audit`, `af: none` — the F0
   audit's elevation gate).
2. **Polar front** per `DESIGN-S1-POLAR-v6.md` §9: defs → rows 1–12 →
   helpers 13a–g → ledger row 13 → the six downstream rows (elevations
   per the per-row af budgets).
3. **Stage-1 split producers** (the G-S1 gate contents:
   `lem-stage1-rectified-nontrivial-projection`,
   `lem-stage1-original-complementary-pair`,
   `lem-stage1-fresh-two-point-inclusion`) — design + land + elevate on
   top of the landed polar rows. NOTE: these three still need their own
   design/audit round (small; their polar prerequisites now exist) — the
   one remaining design gap on the critical path, deliberately sequenced
   behind the polar landing.
4. **MAIN front** per `DESIGN-MAIN-STRUCTURE-v5.md` §10: P0 → M01–M18 →
   [G-S1 satisfied by step 3] → M19* → M20–M28; then the
   `lem-thmainext-conditional` deps rewire.
5. **Ledger front** per `DESIGN-LEDGER-DOMAINS-v2.md` §D-order (decoupled —
   can in fact run in parallel with steps 2–4 at the design's own
   black-box interface; its L0 status remains capped by
   `lem-thmainext-conditional`'s elevation, which transits MAIN/polar).
6. **The strengthened `lem-routef-k-ledger`** (fresh prover + fresh
   verifier; guard released here), then **`lem-routef-f0-assembly`**
   (2/2), then (if D1 = B) `ex-hume` elevation, then the `op-classical`
   root rewire — the LAST action of the campaign.

## 6. Honest status line

Everything above is design-level and non-rigorous. T0 = 83; registry = 265;
neither moved during this campaign. `op-classical` remains OPEN. What the
campaign bought: the residual risk on Route F is now elevation labour plus
the small step-3 design round — not missing or undesigned mathematics — as
far as 19 + 8 hostile-pipeline jobs can establish.
