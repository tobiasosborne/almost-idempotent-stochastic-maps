# Top-down proof sketch v51: op-classical (2026-08-08, session 45 close — sharpness campaign W139 in progress: ex-hume RETRACTED, the prh-sharpness route landed + factored; elevations pending)

## UNCHANGED from v50

**`op-classical` is `proved` / `af: validated`** (root discharge 2026-08-08;
explicit dimension-free eta_0 = eta_K, C = K+4*sqrt(2K)). The honest
boundary stands: af-validated rung only (no Lean); the discharged contract
is the upper bound only. T0 = 196.

## Map change 1: `ex-hume` is RETRACTED (disproved) — the project's first formal retraction

The W139 campaign (three fresh-hostile-audit rounds: REJECT → REJECT →
LAND-WITH-EXACT-CORRECTIONS; artifacts in
`docs/plans/2026-08-08-EXHUME-SHARPNESS/`) established that the inherited
`ex-hume` contract is FALSE as literally stated ("distance to every
stochastic idempotent is <one common value>" — refuted by `I_3`:
`||P_s-I_3|| = 2(1-s+s^2)` vs the claimed `2s(1-s+s^2)`). User-ratified
landing: the shard now carries the precisely-quantified false proposition
at `status: disproved` with the counterexample in-body; first entry in
`docs/LEARNINGS.md`; 51-locus citation sweep landed (incl. the
`thm-rank-one` contract correction and the locked
`def-near-positive-projection` status/scoping correction). HONEST
BOUNDARY: **signed-parameter (delta) sharpness is currently established at
NO rigorous rung.**

## Map change 2: the active sharpness route (stochastic parameter eta)

- `cor-classical-sharpness` LANDED (`stated`): the direct 4x4 witness
  corollary (Q_lambda = A_lambda M_lambda row-stochastic, defect <=
  2*lambda^2, every stochastic idempotent at distance >= lambda; explicit
  quantified negative: no C*eta^beta with beta > 1/2). Sole dep:
  `lem-prh-sharpness`.
- `lem-prh-sharpness` (proved-mod-audit, byte-frozen contract) was
  FACTORED after two balloon aborts (user-ratified;
  AUDIT-PRHSHARP-FACTOR.md LAND-WITH-EXACT-CORRECTIONS): new rows
  `lem-prh-sharpness-family-arithmetic` + `lem-prh-sharpness-row-coincidence`
  (both `stated`), main deps extended. Registry 372 → 374.
- Elevation state at session close: family-arithmetic run 1 ALSO ballooned
  (27 > 26, 20 validated; third balloon in this family — see FINDINGS
  2026-08-08 "family-specific pathology" with the recommended remedy
  order: xhigh fresh prover first, then a skeleton-tightening addendum,
  then further factoring; NEVER a cap bump). No sharpness row is T0 yet.

## The open surface (next session)

1. **Finish W139** (bead `aism-4fl4`): elevate family-arithmetic (remedy
   (a): fresh prover at xhigh, cap 26) → row-coincidence (cap 22) →
   slimmed main `lem-prh-sharpness` (cap 18; its workspace MUST be
   cleanly re-seeded — the deps ratification crossed it; seeding package
   in DESIGN-PRHSHARP-FACTOR.md §5.3) → `cor-classical-sharpness`
   (cap 20; external = the T0 main row). Then Stage D of
   DESIGN-EXHUME-SHARPNESS-V2.md: the deferred active-carrier halves of
   the 50-locus sweep, the report/02_prh sharpness subsection,
   PROVENANCE/UNWIRED reconciliation, paper §5 switch to the 4x4 witness,
   sketch supersede, PRD/README/HANDOFF.
2. Report sync `aism-9kmt` (unanchored banks ~120-196 + the family).
3. Paper polish (bead `aism-aywn`, delivered draft).
4. Lean/mathlib top rung — only on user elevation.

## Controller note

W139 logged wave-by-wave on arm FH: 3 design + 4 audit rounds (sharpness
package v1/v2/v3-addendum + factoring), Stage-A landing, factoring
landing, three classified balloon aborts (2 monolith + 1 factored piece),
one fresh-prover clean re-seed. Reviewer ≠ author throughout; nothing
promoted; T0 = 196 unchanged since the root discharge.

`op-classical`: **proved / af: validated**. T0 = 196. Registry = 374.
Sharpness: active campaign, not yet T0. Lean: open.
