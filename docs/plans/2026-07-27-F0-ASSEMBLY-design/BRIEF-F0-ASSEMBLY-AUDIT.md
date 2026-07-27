# BRIEF — hostile audit of DESIGN-F0-ASSEMBLY.md (second stage, fresh verifier)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-F0-ASSEMBLY.md` and must assume it is wrong until proven otherwise.
It claims the Route-F root composition op-classical ⇐ K-ledger + F2 + F3 +
PRH closes with two thin new rows, one K-ledger contract correction, and a
two-node assembly row — and that EVERY seam is an exact match. A
falsely-clean seam audit here poisons the very last step of the route;
finding a defect is a BIG SUCCESS.

## Your target

`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md` — two new
rows (§1.1–1.2), a required `lem-routef-k-ledger` contract correction
(§1.3), the assembly row (§1.4), the single-K seam audit (§2), root wiring
with OR-routes (§3), the sharpness/equivalence side-check (§4),
dimension-freeness (§5), and the landing order (§6).

## Audit against (read all)

1. `BRIEF-F0-ASSEMBLY.md` (what was asked; note the brief itself wrongly
   called F2/F3 T0 — the design corrected this; verify the correction is
   right by reading the frontmatter of both shards).
2. The authoritative registry shards — check every interface claim
   LITERALLY against the contract lines:
   `argument/lemmas/op-classical.md`, `lem-routef-k-ledger.md`,
   `lem-routef-f2-positive-unital-compression.md`,
   `lem-routef-f3-retract-defect.md`, `lem-routef-prh-finish.md`,
   `lem-prh.md` (if present), `cor-kitaev-diagonal-cpization.md`,
   `lem-kitaev-almost-idemp-audit.md`, `lem-thmainext-conditional.md`,
   `ex-hume.md`, `lem-classical-equiv.md`, and the current `deps:` of
   `op-classical.md` (what IS the legacy route wiring? does the proposed
   OR-route syntax `routes:` even exist in this repo's argument schema —
   read `argument/README.md` and check whether the linker supports
   alternative routes; if not, the §3 wiring proposal needs a different
   mechanism and that is a finding).
3. `docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md` Q4 — the
   claimed provenance of both new rows. Does it actually prove Φ = JQD is
   UCP AND the exact identity ‖Φ²−Φ‖_cb = ‖Q²−Q‖_{∞→∞}? An equality (not
   just ≤) needs both directions — check the lower-bound direction is
   really there.
4. `DESIGN-LEDGER-DOMAINS-v2.md` §§3.5, 6.2 and `AUDIT-LEDGER-DOMAINS-v2.md`
   — the ledger's exported K, η_K, and the parent wiring the design builds
   on; verify the design consumes the AUDITED (corrected) version,
   including the ρ_id^corr correction's non-effect claim on η_K.
5. `docs/plans/2026-07-26-top-down-proof-sketch-v34.md` — is the F0 shape
   consistent with the governing sketch; anything the sketch requires of F0
   that the design omitted?

## Specific attack surface (check each, then hunt beyond)

- **The seam table (§2) — recompute every row of it yourself.** Especially:
  (a) F2's multiplicativity antecedent — read F2's contract: it demands
  ‖Υ(Δx·Δy) − xy‖ ≤ Kη‖x‖‖y‖ for all x,y ∈ B at level one; the ledger's
  telescope estimate is claimed "stronger" (all amplifications) — is the
  ledger's estimate really of the SAME composite (Υ(Δx Δy) vs Υ_r(Δ_r X Δ_r Y)),
  same orientation, same normalization? (b) F2's hypothesis set includes
  Δ, Υ UCP and B a finite-dimensional unital C*-algebra — which ledger row
  exports UCP-ness of Δ, Υ and the algebra data? If none does, the corrected
  parent contract must — is that in the §1.3 correction? (c) The claim
  "no η→ε_AI(η) conversion occurs at this seam" — verify against
  `lem-routef-ai-defect-linearization`'s contract: where DOES the
  conversion happen, and does the ledger's Kη truly refer to the same η as
  ‖Q²−Q‖ ≤ η? (d) F3's "for every x" quantifier and the strict 3Kη < 1.
  (e) PRH's exact hypothesis list vs what F2+F3 export.
- **The K-ledger correction (§1.3).** Is the corrected contract honestly a
  BINDER/closure correction (same mathematics), or does it silently
  strengthen what the hostile-verified ledger actually established (the
  W74F-G/H verdicts)? Compare against
  `docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md` and
  `VERDICT-W74F-H-STAGE1.md`: did the verified ledger actually produce the
  three estimates FOR ALL amplifications, and the E-conclusion for the SAME
  Q? Any strengthening beyond the verified content must be flagged as new
  proof obligation, not a "correction".
- **The two new rows (§1.1–1.2).** Node budgets honest? Is the defect
  identity really an EQUALITY with constant 1 (attack the cb lower bound:
  does ‖Φ²−Φ‖_cb ≥ ‖Q²−Q‖_{∞→∞} follow from DJ = I alone — write the
  two-line argument or refute it)? Deps really empty (does the UCP lift
  need def-* imports beyond def-stochastic — where is "UCP" defined in this
  repo's definitions layer? A naked symbol is a finding)?
- **The assembly row (§1.4).** Only dep = the corrected K-ledger: does its
  contract really follow by pure specialization (η₀ = η_K, C = K+4√(2K)),
  or does it need the two lift rows as direct deps too (they are wired into
  the LEDGER's parent list in §1.3 — is that the right place, given the
  ledger's contract as corrected already binds Q and Φ)?
- **The sharpness split (§4).** Is the recommendation coherent with L0
  discipline (changing op-classical's contract is a definition-level
  ripple — Rule/stop-condition territory)? Is the alternative
  ([f0-assembly; ex-hume] route) actually sufficient to discharge the
  literal compound contract (does ex-hume prove SHARPNESS of the exponent
  in the exact sense the parenthetical asserts — read ex-hume's contract)?
- **Double-counting and the OR-route (§3).** Verify F2/F3/PRH appear
  exactly once in the proposed DAG; verify the proposed root wiring
  mechanism is representable in this repo's schema; verify the
  DO-NOT-REWIRE guards are respected by the proposal text.
- **Dimension-freeness (§5)** — check the constants 2, 3, 24, 4, √2 claims
  against the F2/F3/PRH contracts.
- **Landing order (§6)** — well-founded? Is "elevate F2 and F3" correctly
  placed (they are proved-mod-audit with af: none — confirm), and is the
  decoupling claim (F0 has no direct MAIN/polar dependency; only through
  the thmainext black box) verified against the dep chains?

## Deliverable — write `docs/plans/2026-07-27-F0-ASSEMBLY-design/AUDIT-F0-ASSEMBLY.md`

- Verdict per proposed row (both new rows, the ledger correction, the
  assembly row), per seam-table line, for the wiring proposal, the
  sharpness recommendation, dimension-freeness, and the landing order:
  VALID / VALID-WITH-CORRECTIONS (state them exactly) / REFUTED (show the
  defect concretely).
- Final disposition: LAND (with corrections) / REDESIGN / ROUTE-ALARM.
- Cite every check with exact loci (file:line).

## Hard constraints

- Write ONLY `docs/plans/2026-07-27-F0-ASSEMBLY-design/AUDIT-F0-ASSEMBLY.md`.
  Touch nothing else.
- No repairs beyond stating corrections; no status promotion; nothing here
  is rigorous. NOT IN LOCAL REFS discipline applies.
