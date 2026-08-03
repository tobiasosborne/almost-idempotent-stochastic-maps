---
id: lem-routef-delta-phi-product
kind: lemma
contract: Normalized Delta product: for rho_DeltaPhi := min{rho_theta, rho_Delta, rho_2} and 0 <= eta <= rho_DeltaPhi, every amplification satisfies ||tilde-Phi_n(Delta_n X Delta_n Y) - tilde-Delta_n(XY)|| <= (C_2+C_theta+C_Delta)*eta*||X||*||Y||.
defs: def-almost-idempotent; def-extended-epsilon-cstar-algebra
deps: lem-routef-functional-calculus-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 7 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; source LEDGER-W74F-G-K.md:374-383; approximate_algebras.tex:2803-2812
owner: A
workspace: proofs/lem-routef-delta-phi-product
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
