---
id: lem-routef-prh-finish
kind: lemma
contract: Route F PRH finish: let A:l-infinity(k)->l-infinity(n) and M:l-infinity(n)->l-infinity(k) be positive unital maps and let Q be row-stochastic; if K >= 1, 0 <= eta <= min{(24*K)^(-1),1}, ||Q-AM||_{infinity->infinity} <= K*eta, and ||MA-I||_{infinity->infinity} <= 3*K*eta/(1-3*K*eta), then there is a stochastic idempotent E with ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
defs: def-positive-approximate-retract; def-stochastic
deps: lem-prh
status: proved
af: validated
provenance: LEDGER-W74F-G-K.md §5; VERDICT-W74F-G-KLEDGER.md Finish (VALID); VERDICT-W74F-H-STAGE1.md Scope and finish (VALID); DESIGN-FUDW-DECOMP-v3.md §2.5; VERDICT-FUDW-DECOMP-V3.md §§4.3,B,D
owner: A
workspace: proofs/lem-routef-prh-finish
---

**Status.** Hostile-reviewed detached-finish transcription at
`proved-mod-audit`; it depends only on the already validated `lem-prh`, as
corrected by the v3 verdict. This shard itself is not `af`-validated.

**Provenance.** `LEDGER-W74F-G-K.md` §5 and both hostile finish verdicts;
dependency correction and safe-subset authorization in
`VERDICT-FUDW-DECOMP-V3.md` §§4.3,B,D.
