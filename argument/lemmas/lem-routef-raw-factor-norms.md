---
id: lem-routef-raw-factor-norms
kind: lemma
contract: Raw factor-map norms: with C_V, C_T, rho_T from (1.1), for 0 <= eta <= rho_T, every amplification satisfies (1-C_V*eta)*||X|| <= ||tilde-Delta_n X|| <= (1+C_V*eta)*||X|| and max{||tilde-Delta||_cb, ||tilde-Upsilon||_cb} <= 1+C_T*eta.
defs: def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-routef-functional-calculus-closeness; lem-routef-ai-defect-linearization; lem-thmainext-conditional
status: stated
af: seeded
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 1 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; source approximate_algebras.tex:2749-2753; LEDGER-W74F-G-K.md:154-190
owner: A
workspace: proofs/lem-routef-raw-factor-norms
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

**Elevation note.** The projected af budget for this row is 8 / 3 (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.

**Audit correction 2 (wording, applied).** The design's sect-3.1 prose is read as "the MAIN contract supplies the extended isomorphism, whose unit defect is at most C_V*eta" -- NOT as a unital extended isomorphism. No arithmetic changes; the unit defect is carried explicitly by [[lem-routef-raw-factor-units]].
