# BRIEF — GAP-MAIN-STRUCTURE design job (de-risk front #2)

You are a fresh, independent, HOSTILE design mathematician. Your target is
**GAP-MAIN-STRUCTURE**: the eight `stated` MAIN-CB structural rows — the glue
of the main induction — which have NEVER been verified even once ("new glue,
not verified artifact results"). Your job: produce per-row proof plans, or
find the structural defect if one exists. Finding a genuine gap is a BIG
SUCCESS, equal in value to producing the plans. Do not be charitable.

RISK CALIBRATION: the source argument (Kitaev arXiv:2405.02434, TeX
~1414–1444) is almost certainly correct; the realistic failure modes are
(i) the v4.1 contract factoring being wrong/circular, (ii) the compressed
prose hiding steps that need real derivation. Judge the CONTRACTS and the
INDUCTION STRUCTURE, and report exactly which it is if something fails.

## Context (read these, in this order)

1. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   — §2.4 (the eight rows marked REFACTOR BEFORE SEEDING (GAP-MAIN-STRUCTURE):
   `lem-maincb-stage1-strict-refinement`, `lem-maincb-stage1-maximality`,
   `lem-maincb-corner-equivalence`, `lem-maincb-cross-class-merging-datum`,
   `lem-maincb-one-class-extension`, `lem-maincb-binary-block-merge`,
   `lem-maincb-stage3-finite-recombination`, `lem-maincb-structural-assembly`),
   §3.3 (`lem-thmainext-conditional` assembly wiring), risk rows R17–R23, R36.
2. The registered shards in `argument/lemmas/` for those eight ids (the
   landed contracts are authoritative over the design doc if they differ) and
   `argument/lemmas/lem-maincb-error-improvement.md` (IMPROVE-CB — the
   user-ratified NARROWED contract; its proof plan is also your deliverable).
3. `refs/kitaev-2405.02434/approximate_algebras.tex` — the main-induction
   source, approximately lines 1180–1450 (one-dimensional δ-projections,
   corner relation, class recombination, the main theorem assembly).
4. The already-validated inputs the glue consumes (read their shards for the
   exact contracts): `conj-extcb`, `lem-extcb-four-corner-merge`,
   `lem-extcb-one-dimensional-product`, `lem-extcb-one-dimensional-corner-dimension`,
   `lem-extcb-corner-dimension-additivity`, `lem-extcb-exact-target-correction`,
   plus the `proved-mod-audit` reset chain rows in v4.1 §2.4
   (`lem-maincb-reset-constant-ledger`, the three raw-reset rows,
   `lem-maincb-uniform-reset-chain`) and `lem-compcb-single-compression-transfer`.

## Deliverable — write `docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE.md`

1. **Per-row proof plan** for the eight rows, in the §3.3 branch order
   (refinement/maximality; equivalence; one-class; cross-class-datum/merge/
   recombination; assembly), plus IMPROVE-CB. For each: the proof mechanism at
   contract level (which validated/mod-audit inputs supply which step, with
   their EXACT hypotheses matched — no silent strengthening), the projected af
   node budget (≤12 nodes / depth ≤3; factor further if it exceeds), and any
   missing definition shards.
2. **Explicit adjudication of the three named structural hazards:**
   - R19 (circularity): verify the strict-refinement induction has a
     well-founded measure (source dimension m strictly increases; termination
     at maximality). State the measure explicitly.
   - R21 (conflated inductions): verify one-class extension and cross-class
     recombination are genuinely separate inductions joined only at assembly.
   - R22 (missing zero-datum): verify the cross-class merging datum PRODUCES
     the zero off-diagonal corners from dimension additivity rather than
     assuming them.
3. **Per-row FEASIBILITY VERDICT**: SUPPORTED / SUPPORTED-WITH-DERIVATION
   (state exactly what must be derived) / **GAP (describe the hole precisely —
   and classify it: contract-factoring defect vs genuine mathematical gap in
   the source argument)**.
4. **Dimension-freeness audit**: every constant the glue threads (L, C_pre,
   c_0^cb, ε_E^corr, …) must be independent of dimension, amplification, block
   data, and stage index — verify the threading, flag any leak LOUDLY.
5. **Contract corrections**: if a landed contract is wrong as stated, say so
   and propose the exact correction — corrections are ESCALATED to the user,
   never silently applied.

## Hard constraints

- DESIGN ONLY. Write ONLY inside `docs/plans/2026-07-26-MAIN-STRUCTURE-design/`.
  Do NOT touch `definitions/`, `argument/`, `proofs/`, or any other path.
- No status promotion; nothing you write is rigorous.
- v4.1 discipline: one result per row; no compound contracts; explicit local
  domains; no guessed radii.
- Cite loci exactly (file + line ranges). If a needed fact is NOT in the local
  sources listed above, say NOT IN LOCAL REFS and stop on that point — do not
  paraphrase literature from memory.
