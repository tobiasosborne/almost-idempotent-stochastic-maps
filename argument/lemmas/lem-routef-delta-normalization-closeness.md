---
id: lem-routef-delta-normalization-closeness
kind: lemma
contract: Delta UCP normalization: with C_Delta := 6*C_T+7*C_Delta' and rho_Delta := min{rho_unit, rho_Delta', [2*(C_T+C_Delta')]^(-1)}, for 0 <= eta <= rho_Delta, a = Delta'(I) is invertible and Delta(X) = a^(-1/2)*Delta'(X)*a^(-1/2) is UCP with ||Delta - tilde-Delta||_cb <= C_Delta*eta.
defs: def-extended-epsilon-cstar-algebra
deps: lem-routef-raw-factor-units; lem-routef-delta-prime-closeness
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 6 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; source approximate_algebras.tex:2797-2801; LEDGER-W74F-G-K.md:246-259,415-448; VERDICT-W74F-G-KLEDGER.md:141-145,287-290
owner: A
workspace: proofs/lem-routef-delta-normalization-closeness
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

**Elevation note.** The projected af budget for this row is 5 / 3 (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.
