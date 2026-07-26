# BRIEF — hostile audit of DESIGN-S1-POLAR.md (second stage, fresh verifier)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-S1-POLAR.md` and you must assume it is wrong until proven otherwise.
Finding a defect — a wrong formula, an unclosable guard, a circular
dependency, a hidden dimension-dependence, a misread TeX locus, a contract
that smuggles theorem content into a definition — is a BIG SUCCESS.

## Your target

`docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR.md` — an eight-row
formula-level replacement for the `gap-stage1-polar-chart-contract`
reservation, plus consumer corrections and one definition shard.

## Audit against (read all)

1. `docs/plans/2026-07-26-S1-POLAR-design/BRIEF-S1-POLAR.md` (what was asked).
2. `refs/kitaev-2405.02434/approximate_algebras.tex` — CHECK EVERY CITED LOCUS
   (TeX 458, 560, 655–912, 943–955) against what the design claims it says.
   A miscited or overread locus is a finding.
3. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   §2.4, §2.6, §4.1, R14/R35 — does the design respect the v4.1 discipline
   (no compound contracts, no theorem content in definitions, no guessed
   radii, ≤12 nodes / depth ≤3)?
4. `docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-H-STAGE1.md` and
   `VERDICT-W74F-H-STAGE1.md` — the cited campaign loci.
5. The landed shards `argument/lemmas/lem-stage1-exact-unit-rectification.md`,
   `lem-stage1-quantitative-inverse-function.md`,
   `lem-topology-quotient-manifold.md` — does the design correctly state what
   their contracts do and do NOT provide? (Its claim that the validated
   rectification contract is too weak for the polar consumers is load-bearing:
   verify it rather than accept it.)

## Specific attack surface (check each, then hunt beyond)

- **Formula arithmetic**: the ledger row's finite minima (δ*, ε*^r, e_S1,
  r_iso) and the claimed implications (r_- ≥ 3δ*/4; η_path ≤ δ*/4;
  C_der(r_iso+ε_r) ≤ κ_der/4). Recompute them from the displayed guards.
- **Dependency directions**: is the 8-row DAG acyclic, well-founded, and does
  every row's proof plan use only earlier rows / existing registry rows?
- **The claimed gaps** (§7): is the straight-path gap (TeX 906) real — i.e.
  is the right-inverse/domain estimate genuinely absent from the local
  source? Is the TeX 883–888 erratum real, and is the design right that none
  of the eight contracts consumes the second-variable derivative?
- **Consumer sufficiency**: do the corrected contracts for
  `lem-stage1-inversion-derivative-control`,
  `lem-stage1-quotient-manifold-package`, `lem-stage1-quotient-left-inversion`
  actually deliver everything their downstream consumer
  (`lem-stage1-extra-fixed-class` per v4.1 §2.4) needs? A silent shortfall
  here is the most dangerous possible defect — check the fixed-class row's
  dependency list item by item.
- **Definition hygiene**: does `def-approximate-unitary-space` as specified
  assert any existence/estimate (R35 violation)? Is reserving μ, σ as
  notation legitimate?
- **Dimension-freeness**: attack §5 — find any step where a chosen norm,
  a compactness argument, or the direct-sum norm comparison (TeX 560) could
  smuggle in dimension dependence.

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR.md`

- Verdict line per proposed row and per claimed gap/erratum:
  VALID / VALID-WITH-CORRECTIONS (state them exactly) / REFUTED (show the
  defect concretely).
- A final disposition: LAND (with any corrections) / REDESIGN (what must
  change) / ROUTE-ALARM (a genuine obstruction — describe it).
- Cite every check you performed with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR.md`.
  Touch nothing else.
- Do not repair the design yourself beyond stating corrections; do not
  promote any status; nothing here is rigorous.
- If a needed fact is not in the local sources, say NOT IN LOCAL REFS — do
  not fill from memory.
