---
id: lem-routef-raw-product-estimate
kind: lemma
contract: Raw tilde-Delta-product estimate: for 0 <= eta <= rho_prod := rho_T, every amplification and all X, Y satisfy ||tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y) - tilde-Delta_n(XY)|| <= C_T*eta*||X||*||Y||.
defs: def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-ai-defect-linearization; lem-thmainext-conditional
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 4 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; source approximate_algebras.tex:2754-2766; LEDGER-W74F-G-K.md:174-181; AUDIT-LEDGER-DOMAINS.md:166-168
owner: A
workspace: proofs/lem-routef-raw-product-estimate
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
