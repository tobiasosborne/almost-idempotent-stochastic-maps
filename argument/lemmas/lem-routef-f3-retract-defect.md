---
id: lem-routef-f3-retract-defect
kind: lemma
contract: Route F F3 retract defect: let K >= 1 be a dimension-independent constant, n,k >= 1, A: l_inf^k -> l_inf^n and M: l_inf^n -> l_inf^k positive unital maps, Q: l_inf^n -> l_inf^n row-stochastic, and eta >= 0 with 3K*eta < 1; if ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k, then ||MA - I_k||_{inf->inf} <= 3K*eta/(1-3K*eta).
defs: def-stochastic
deps:
status: proved
af: validated
provenance: docs/plans/2026-07-24-fudw-decomposition-artifacts/PROOF-F2F3-BRIDGE.md §2 (prover); hostile verdict VERDICT-F2F3-BRIDGE.md (VALID-WITH-CORRECTIONS, F3: VALID, "the advertised constant is supported exactly"; contract = verdict §7 exact text); closes gap-routef-f3-retract-defect-contract (DESIGN-FUDW-DECOMP-v3.md §2.6)
owner: A
workspace: proofs/lem-routef-f3-retract-defect
---

**Status.** af-VALIDATED 2026-07-27 (87th rigorous result): first-pass
elevation, root validated with 11/11 nodes epistemic=validated, taint clean,
ZERO challenges (fresh codex prover, separate fresh codex verifiers, routine
tier). Export: `export.md`/`export.tex` in the workspace; oracle
`af-lem-routef-f3-retract-defect` + `fr verify` PASS. Originally registered
`proved-mod-audit` on the fresh-codex paper proof + separate hostile verdict
(VALID-WITH-CORRECTIONS; F3 clause VALID, no dimension or norm loss);
contract text is the verdict's §7 "F3 exact contract text" verbatim (LaTeX
flattened to registry ASCII only; unchanged by the 2026-07-27 F2 typing
correction — this row is real-space only).

**What it closes.** The former reservation
`gap-routef-f3-retract-defect-contract`: the quantitative retract bound
`||MA - I|| <= 3K*eta/(1-3K*eta)` that `lem-routef-prh-finish` consumes,
derived exactly from the three F2 output estimates (which are this row's
explicit hypotheses — consumable directly from
`lem-routef-f2-positive-unital-compression`'s conclusion).

**Verifier corrections.** Shared with the F2 shard (recorded there): the
`eta = 0` strict-chain fix and the stale-GAP-sentence update; both
wording-level, no constant changes.

**Import discipline (verdict-mandated).** Must NOT import the quarantined
component-domain rows (GAP-LEDGER-DOMAINS); hypotheses are explicit.
