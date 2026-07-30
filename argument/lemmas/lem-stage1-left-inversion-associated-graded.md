---
id: lem-stage1-left-inversion-associated-graded
kind: lemma
contract: Associated-graded action of a left inversion over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, F^{p,q}=(A^+)^p intersect A^{p+q}, and E^{p,q}=F^{p,q}/F^{p+1,q-1}; then sigma^* preserves every F^{p,q} and induces (-1)^(p+q)*id on every E^{p,q} for p >= 0 and p+q >= 0.
defs: def-h-space-left-inversion
deps: lem-stage1-exterior-cohomology
status: stated
af: none
workspace: proofs/lem-stage1-left-inversion-associated-graded
provenance: DESIGN-S1-ENDGAME-v5.md sect-2 (landed verbatim); AUDIT-S1-ENDGAME-v5.md VERDICT LAND (zero corrections); user-ratified 2026-07-30
owner: A
---

**Status.** `stated` — contract transcribed VERBATIM from the audited
`DESIGN-S1-ENDGAME-v5.md` sect-2 (hostile audit v5 verdict LAND, zero
corrections, after a 5-round design cycle; user ratified 2026-07-30).
Elevation position 3/13 in the serial order of DESIGN-S1-ENDGAME-v5.md
sect-3. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
9 / 3 / 14. The per-node skeleton is DESIGN-S1-ENDGAME-v5.md sect-4
(lem-stage1-left-inversion-associated-graded); a hard-cap hit is a factoring stop, not a rounds bump. Constants
live in the proof body, never the contract.

**Provenance loci.** `refs/kitaev-2405.02434/approximate_algebras.tex:1016-1049`
