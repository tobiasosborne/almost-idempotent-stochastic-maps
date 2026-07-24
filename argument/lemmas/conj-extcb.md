---
id: conj-extcb
kind: lemma
contract: EXT-CB: there are universal C_ext < infinity and e_ext > 0 such that if e=delta+epsilon <= e_ext, P,Q are delta-projections in an extended epsilon-C*-algebra A with ||P+Q-I|| <= delta, v:M_r->S_P is an extended delta-isomorphism, dim S_Q=1 at level one, and S_{P,Q} is nonzero, then there is one map v_+:M_{r+1}->A whose every amplification is a C_ext*e-isomorphism; the same level-one unitary and the same four corner maps carry all amplification levels, with constants independent of r, n, and dim A.
defs: def-extended-epsilon-cstar-algebra
deps:
status: conjecture
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md §3 EXT-CB; hostile batch verdict VERDICT-W74F-BATCH.md §C (VALID decomposition, EXT-CB remains a GAP); report conj:extcb
owner: A
workspace: proofs/conj-extcb
---

**Open gap.** This is the EXT-CB node isolated by W74F-C.  It is a
`conjecture` with empty `deps`, not an imported theorem and not
conditionally marked proved.

The single-map clause forbids choosing unrelated unitaries or extension
maps at different matrix levels.  The source outline does not establish
the complete closeness of all four corner maps or a bound independent of
\(r\).
