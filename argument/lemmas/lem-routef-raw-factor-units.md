---
id: lem-routef-raw-factor-units
kind: lemma
contract: Raw factor-map units: for 0 <= eta <= rho_unit := rho_T, max{||tilde-Delta(I)-I||, ||tilde-Upsilon(I)-I||} <= C_T*eta.
defs: def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-routef-raw-factor-norms; lem-routef-ai-defect-linearization; lem-thmainext-conditional
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 2 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; source approximate_algebras.tex:2754-2757; LEDGER-W74F-G-K.md:169-181; AUDIT-LEDGER-DOMAINS.md:187
owner: A
workspace: proofs/lem-routef-raw-factor-units
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

**Elevation note.** The projected af budget for this row is 4 / 2 (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.
