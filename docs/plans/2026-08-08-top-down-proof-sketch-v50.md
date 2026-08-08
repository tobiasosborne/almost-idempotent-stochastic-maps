# Top-down proof sketch v50: op-classical (2026-08-08, session 45 — **op-classical IS DISCHARGED AT T0**: the strengthened K-ledger queue banked (T0 190 → 195) and the user-ratified root rewire validated; T0 = 196, registry = 371)

## THE HEADLINE

**`op-classical` is `proved` / `af: validated` (2026-08-08).** There exist
universal, dimension-free eta_0 = eta_K > 0 and C = K + 4*sqrt(2K) such
that every row-stochastic Q with ||Q^2 - Q||_{inf->inf} <= eta <= eta_0
admits a stochastic idempotent E with ||Q - E||_{inf->inf} <= C*sqrt(eta).
The discharge runs through Route F: F0 seam → formation → the 19-row
ledger family → the strengthened K-ledger (three-helper factoring) →
F2 → F3 → PRH → F0 assembly → root. Every edge is af-validated (fresh
codex prover, separate fresh hostile verifier per node, external oracle +
`fr verify` per bank); the root's own 5-node tree validated clean.

## The honest boundary (do not overclaim past it)

1. **Rigour rung:** af-validated is this repo's L0 rung (b) — an
   adversarial machine protocol, NOT a Lean/mathlib proof. The top rung
   remains open work if the user wants it.
2. **Sharpness:** the discharged contract is the UPPER BOUND only (the D1
   split, W80). Sharpness of the exponent 1/2 rests on `ex-hume`, still
   `proved-mod-audit` / `af: seeded`. Elevating it is the natural next
   rigour target.
3. The legacy signed-geometry route (`thm-classical-factorization` +
   `prop-approx-simplex`) remains an independent, non-rigorous alternative
   route; it was NOT used in the discharge.

## What happened in session 45 (W138)

1. Design → hostile audit **REJECT** (1 FATAL cap-budget + 3 HIGH) →
   v2 design (three first-class helpers; pre-forall scalar positivity via
   header-only formulas; 30-item census; complete manifest) → fresh
   hostile re-audit **LAND, zero corrections** → user ratification →
   landing (registry 367 → 371; 11 stale report loci repaired).
2. Elevation queue, all five stages banked same-day:
   - `lem-routef-scalar-header-positivity` T0 191 (16 nodes; one
     statement challenge on the (1.6) enumeration, corrected + re-verified)
   - `lem-routef-factor-map-packet` T0 192 (16/16 first pass)
   - `lem-routef-factor-estimate-packet` T0 193 (16/16 first pass)
   - strengthened `lem-routef-k-ledger` T0 194 (7/7 FIRST PASS — the
     factoring absorbed the work exactly as designed)
   - `lem-routef-f0-assembly` T0 195 (7/7; verify-phase resume for the
     root verifier only)
3. User-ratified ROOT REWIRE: the audited OR-routes block
   (`routes: [lem-routef-f0-assembly] | [thm-classical-factorization;
   prop-approx-simplex]`), kind open-problem → theorem (conj-hcb
   precedent), "(OPEN)" contract marker removed, root af tree 5/5
   validated/clean, oracle + `fr verify` PASS, mechanical flip →
   **T0 = 196**.
4. Report: full truthfulness sweep (28 stock "op-classical is open"
   claims + 8 bespoke paragraphs + 5 shard headers + catalog rows).
5. USER P0: the 4-page standalone paper (fresh-codex draft + separate
   faithfulness audit, 4 corrections applied) delivered; its status
   footnote is updated post-discharge.

## The open surface after this delta

1. **`ex-hume` af elevation** (sharpness at T0) — natural next target;
   workspace already `af: seeded`.
2. **Report sync `aism-9kmt`** — anchor/reproduce the ~120–196 banks
   incl. the K-ledger family and the root discharge narrative.
3. **Lean/mathlib** — the ladder's top rung; a separate campaign, only if
   the user elevates it.
4. Paper polish toward submission (user's call).

## Controller note

W138 logged wave-by-wave on arm FH: 2 design + 2 audit dispatches
(REJECT then LAND), the landing, five elevation banks, the root
discharge, the paper draft + faithfulness audit. Reviewer ≠ author
throughout; every bank passed the external oracle gate; the two run-1
non-validations (max-rounds while converging) were same-tree resumes, both
legal (no ratification crossed).

`op-classical`: **proved / af: validated**. T0 = 196. Registry = 371.
Sharpness (`ex-hume`) and Lean remain open.
