---
id: lem-routef-threshold-minimum
kind: lemma
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Route F scalar threshold: let eta_K := min{rho_fac, (24*K)^(-1), 1}; then eta_K > 0, and every 0 <= eta <= eta_K satisfies eta <= rho_fac, 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-k-finiteness
status: proved
af: validated
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 14 (landed verbatim 2026-08-03, LaTeX flattened to registry ASCII); AUDIT-LEDGER-DOMAINS-v2.md LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; RE-SCOPED 2026-08-05: ambient binding prefix + defs/deps repair per DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-3 (hostile re-audit AUDIT-LEDGER-SETTING-RESCOPE-V2.md LAND-WITH-EXACT-CORRECTIONS, corrections folded in), user-ratified 2026-08-05; source AUDIT-LEDGER-DOMAINS.md:273-317; DESIGN-LEDGER-DOMAINS-v2.md sect-3.5
owner: A
workspace: proofs/lem-routef-threshold-minimum
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
mathematical suffix is byte-identical to the 2026-08-03 landing EXCEPT this row: the SOLE suffix revision of the rescope (v1 rescope audit finding 5).

**Elevation note.** The projected af budget for this row is 5 / 2 (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.

**Row-14 revision (2026-08-05 rescope).** The landed 'threshold minimum' contract asserted F2/F3 smallness and PRH admissibility, which are not exported scalar interfaces of [[lem-routef-f2-positive-unital-compression]], [[lem-routef-f3-retract-defect]], or [[lem-routef-prh-finish]] (AUDIT-LEDGER-SETTING-RESCOPE.md finding 5). The revised contract asserts exactly the scalar inequalities proved in `DESIGN-LEDGER-DOMAINS-v2.md` sect-3.5: the common factor domain, the F2 threshold entry, positivity of the F3 denominator via `3*K*eta <= 1/8`, and the rational retract bound `3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6`. Actual F2/F3/PRH application (where the map data are bound) belongs to the future strengthened [[lem-routef-k-ledger]]; those three rows, `def-stochastic`, `def-positive-approximate-retract`, and [[lem-thmainext-conditional]] accordingly leave this row's imports (DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-3.5).
