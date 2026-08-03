---
id: lem-routef-raw-factor-identities
kind: lemma
contract: Raw factor-map identities: for 0 <= eta <= rho_id^corr := min{rho_theta, rho_AI, epsilon_E/C_A}, tilde-Delta tilde-Upsilon = tilde-Phi and tilde-Upsilon tilde-Delta = I_B.
defs: def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-kitaev-almost-idemp-audit; lem-routef-ai-defect-linearization; lem-thmainext-conditional
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 3 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; source approximate_algebras.tex:2749-2753; LEDGER-W74F-G-K.md:183-187; AUDIT-LEDGER-DOMAINS.md:163-165
owner: A
workspace: proofs/lem-routef-raw-factor-identities
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

**Elevation note.** The projected af budget for this row is 3 / 2 (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.

**Audit correction 1 (applied).** `AUDIT-LEDGER-DOMAINS-v2.md` sect-0 and sect-7 replace `rho_id := min{rho_AI, epsilon_E/C_A}` by `rho_id^corr := min{rho_theta, rho_AI, epsilon_E/C_A}`, exposing the `eta < 1/4` domain of the landed [[lem-kitaev-almost-idemp-audit]] contract (`rho_theta = 1/8`). No downstream radius or primitive-minimum entry changes; later rows referring to `rho_id` denote the corrected value.
