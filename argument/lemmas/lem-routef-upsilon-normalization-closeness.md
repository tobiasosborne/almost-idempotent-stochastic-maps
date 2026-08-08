---
id: lem-routef-upsilon-normalization-closeness
kind: lemma
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, and every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and for every X in B(H), writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon UCP normalization: with C_Upsilon := 6*C_T+7*C_Upsilon' and rho_Upsilon := min{rho_unit, rho_Upsilon', [2*(C_T+C_Upsilon')]^(-1)}, for 0 <= eta <= rho_Upsilon, b = Upsilon'(I) is invertible and Upsilon(X) = b^(-1/2)*Upsilon'(X)*b^(-1/2) is UCP with ||Upsilon - tilde-Upsilon||_cb <= C_Upsilon*eta.
defs: def-routef-raw-factor-setting; def-ucp-map
deps: lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-units; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness
status: stated
af: seeded
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 9 (landed verbatim 2026-08-03, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; RE-SCOPED 2026-08-05: ambient binding prefix + defs/deps repair per DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-3 (hostile re-audit AUDIT-LEDGER-SETTING-RESCOPE-V2.md LAND-WITH-EXACT-CORRECTIONS, corrections folded in), user-ratified 2026-08-05; source approximate_algebras.tex:2895-2899; LEDGER-W74F-G-K.md:246-259,415-448; VERDICT-W74F-G-KLEDGER.md:144-149,291-295
owner: A
workspace: proofs/lem-routef-upsilon-normalization-closeness
---

**Status.** Landed from the hostile-audited designs; `stated` (transcribed, unchecked
in-repo). Landing promotes NOTHING -- the mathematics is adjudicated by the af
elevation queue (fresh prover, separate fresh verifier), not by this transcription.

**Numbered equations.** `(1.1)`--`(1.8)` are the closed scalar-ledger equations of
`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md` sect-1, with audit
correction 1 (`rho_id^corr`) applied; they are carried as derived notation of the scalar
header `W_RF` by [[def-routef-raw-factor-setting]]. The ledger is serial: every coefficient
and radius is a finite max/min/sum/product of quantities produced by declared dependencies,
and `AUDIT-LEDGER-DOMAINS-v2.md` sects-4--5 independently recomputed it as finite, positive,
noncircular, and dimension-free.

**Ambient binding (2026-08-05 rescope).** The contract's prefix binds the ambient
finite-dimensional UCP/cb setting through [[def-routef-raw-factor-setting]] (data/notation
only) and [[lem-routef-raw-factor-setting-formation]] (existence, global-W_RF-first). The
mathematical suffix is byte-identical to the 2026-08-03 landing.

**Elevation note.** The projected af budget for this row is 5 / 3 (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.

**Rescope audit correction 1 (applied).** `AUDIT-LEDGER-SETTING-RESCOPE-V2.md` finding 1: the binder `and for every X in B(H)` is inserted in the prefix so the `X` displayed in the normalization formula is bound. The landed suffix is byte-unchanged.
