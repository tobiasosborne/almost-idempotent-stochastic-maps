---
id: lem-stage1-left-inversion-trace
kind: lemma
contract: Left-inversion trace over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, then Tr(sigma^{*k}:H^k(M;reals)->H^k(M;reals))=(-1)^k*dim_reals H^k(M;reals) for every k >= 0.
defs: def-h-space-left-inversion
deps: lem-stage1-left-inversion-associated-graded
status: stated
af: none
workspace: proofs/lem-stage1-left-inversion-trace
provenance: DESIGN-S1-ENDGAME-v5.md sect-2 (landed verbatim); AUDIT-S1-ENDGAME-v5.md VERDICT LAND (zero corrections); user-ratified 2026-07-30
owner: A
---

**Status.** `stated` — contract transcribed VERBATIM from the audited
`DESIGN-S1-ENDGAME-v5.md` sect-2 (hostile audit v5 verdict LAND, zero
corrections, after a 5-round design cycle; user ratified 2026-07-30).
Elevation position 4/13 in the serial order of DESIGN-S1-ENDGAME-v5.md
sect-3. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
4 / 2 / 8. The per-node skeleton is DESIGN-S1-ENDGAME-v5.md sect-4
(lem-stage1-left-inversion-trace); a hard-cap hit is a factoring stop, not a rounds bump. Constants
live in the proof body, never the contract.

**Provenance loci.** `refs/kitaev-2405.02434/approximate_algebras.tex:971-972,1023-1050`
