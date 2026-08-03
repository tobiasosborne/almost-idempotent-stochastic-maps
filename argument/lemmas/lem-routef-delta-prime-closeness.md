---
id: lem-routef-delta-prime-closeness
kind: lemma
contract: Delta-prime CP closeness: with C_Delta' := C_T+4*C_theta and rho_Delta' := min{rho_T, rho_prod}, for 0 <= eta <= rho_Delta', the repaired norm-one diagonal produces a CP map Delta' with ||Delta' - tilde-Delta||_cb <= C_Delta'*eta.
defs: def-fd-cstar-diagonal; def-extended-epsilon-cstar-algebra
deps: cor-kitaev-diagonal-cpization; lem-routef-functional-calculus-closeness; lem-thmainext-conditional; lem-routef-raw-factor-norms; lem-routef-raw-product-estimate
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 5 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; source approximate_algebras.tex:2771-2801; LEDGER-W74F-G-K.md:193-226; argument/lemmas/cor-kitaev-diagonal-cpization.md:4-9; AUDIT-LEDGER-DOMAINS.md:169-171
owner: A
workspace: proofs/lem-routef-delta-prime-closeness
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

**Elevation note.** The projected af budget for this row is 6 / 3 (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.
