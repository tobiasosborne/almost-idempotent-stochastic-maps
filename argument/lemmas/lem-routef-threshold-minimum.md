---
id: lem-routef-threshold-minimum
kind: lemma
contract: Route F threshold minimum: importing the black-box constants C_E, epsilon_E used in rows 1-4, let eta_K := min{rho_fac, (24*K)^(-1), 1}; then eta_K > 0, and for 0 <= eta <= eta_K the three factorization estimates have common coefficient K, the F2 and F3 smallness conditions hold, and the PRH finish is admissible.
defs: def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-stochastic; def-positive-approximate-retract
deps: lem-thmainext-conditional; lem-routef-k-finiteness; lem-routef-f2-positive-unital-compression; lem-routef-f3-retract-defect; lem-routef-prh-finish
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 14 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; source AUDIT-LEDGER-DOMAINS.md:262-301; argument/lemmas/lem-thmainext-conditional.md:4-9; lem-routef-f2-positive-unital-compression / lem-routef-f3-retract-defect / lem-routef-prh-finish shards:4-9
owner: A
workspace: proofs/lem-routef-threshold-minimum
---

**Status.** Landed verbatim from the hostile-audited design; `stated` (transcribed, unchecked
in-repo) and `af: none`. Landing promotes NOTHING -- the mathematics is adjudicated by the af
elevation queue (fresh prover, separate fresh verifier), not by this transcription.

**Numbered equations.** `(1.1)`--`(1.8)` are the closed scalar-ledger equations of
`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md` sect-1, with audit
correction 1 (`rho_id^corr`) applied. The ledger is serial: every coefficient and radius is a
finite max/min/sum/product of quantities produced by declared dependencies, and
`AUDIT-LEDGER-DOMAINS-v2.md` sects-4--5 independently recomputed it as finite, positive,
noncircular, and dimension-free.

**Elevation note.** The projected af budget for this row is 5 / 2 (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.

**Terminal-row note (design sect-2).** This row consumes [[lem-thmainext-conditional]] AT CONTRACT LEVEL as the black-box producer of `C_E, epsilon_E`. That producer remains `proved-mod-audit`; using its contract here promotes it not at all, and under the linker's status-propagation rule this row's own af elevation inherits its status restriction. The first audit's claim that the terminal threshold was a GAP was REFUTED by `AUDIT-LEDGER-DOMAINS-v2.md` sect-0 and sect-5: the ten-entry expanded minimum is finite, positive, noncircular, and dimension-free.
