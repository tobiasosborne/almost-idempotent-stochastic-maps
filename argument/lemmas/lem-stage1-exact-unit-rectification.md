---
id: lem-stage1-exact-unit-rectification
kind: lemma
contract: Dimension-free exact-unit rectification: there are universal C_unit < infinity and e_unit > 0 such that every finite-dimensional epsilon_X-C*-algebra with epsilon_X <= e_unit admits on the same involutive normed space an exact unit J and product bold-dot with ||J-I_X|| <= C_unit*epsilon_X and ||x bold-dot y-xy|| <= C_unit*epsilon_X*||x||||y||.
defs: def-epsilon-cstar-algebra
deps: lem-stage1-quantitative-inverse-function
status: proved
af: validated
provenance: PROOF-W74F-H-STAGE1.md §1 SPLIT-A (1.1); VERDICT-W74F-H-STAGE1.md Construction exact-unit rectification (VALID); DESIGN-FUDW-DECOMP-v3.md §2.4; VERDICT-FUDW-DECOMP-V3.md §§4.1,B,D
owner: A
workspace: proofs/lem-stage1-exact-unit-rectification
---

**Status.** af-VALIDATED in-repo (2026-07-26): 6-node tree, taint clean,
fresh-codex prover/verifier protocol (§6); consumes the validated
[[lem-stage1-quantitative-inverse-function]] external and byte-matched
`def-epsilon-cstar-algebra`; export in
`proofs/lem-stage1-exact-unit-rectification/export.md`; banking oracle
registered, `fr verify` pass. L0-rigorous.

**Provenance.** `PROOF-W74F-H-STAGE1.md` §1 SPLIT-A and
`VERDICT-W74F-H-STAGE1.md`; dependency correction and safe-subset
authorization in `VERDICT-FUDW-DECOMP-V3.md` §§4.1,B,D.
