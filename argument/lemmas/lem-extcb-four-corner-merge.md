---
id: lem-extcb-four-corner-merge
kind: lemma
contract: Complete four-corner merge: there are universal C_merge < infinity and a_merge > 0 such that four fixed bijective level-one corner maps satisfying def-four-corner-merging-datum with common defect rho and rho+epsilon <= a_merge combine into one extended C_merge*(rho+epsilon)-isomorphism.
defs: def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-compressed-corner; def-four-corner-merging-datum
deps: lem-compcb-corner-algebra; lem-hcb3-uniform-square-lower; lem-extcb-four-corner-norm
status: proved
af: validated
provenance: DESIGN-FUDW-DECOMP-v3.md §2.2 (EXT-CB premise MERGE; TeX 1325-1359); PROOF-W74F-F-EXTCB.md §§1.3,6; VERDICT-W74F-F-EXTCB.md Premise ledger and EXTCB-5; VERDICT-FUDW-DECOMP-V3.md §D
owner: A
workspace: proofs/lem-extcb-four-corner-merge
---

**Status.** `proved`; `af: validated` — root-validated, taint-clean
adversarial tree (22 validated + 4 archived; mechanical ledger reflection;
export at `proofs/lem-extcb-four-corner-merge/export.md`).

**Contract amendment (2026-07-25, verdict-driven).** The transcribed
hypothesis bounded only `rho <= a_merge` with epsilon unconstrained; the
first-run verifier flagged this as a fatal smallness gap (ch-bc4849cd — the
block/bootstrap thresholds need the TOTAL defect small), the prover amended
the root to `rho and rho+epsilon <= a_merge`, and the fresh verifiers
validated the amended root. The contract line now carries the validated
root verbatim (linker contract-match restored). Downstream EXT consumption
supplies small ambient epsilon, so the conditional form is the consumable
one.

**Provenance.** `DESIGN-FUDW-DECOMP-v3.md` §2.2 and
`PROOF-W74F-F-EXTCB.md` §§1.3,6; safe-subset authorization in
`VERDICT-FUDW-DECOMP-V3.md` §D.
