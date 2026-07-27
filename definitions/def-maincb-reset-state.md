---
id: def-maincb-reset-state
term: MAIN-CB current reset state
aliases: MAIN reset state
kind: original
status: locked
source: internal
locus: DESIGN-FUDW-DECOMP-v4.1.md:419-423; DESIGN-MAIN-STRUCTURE-v5.md sect 1.2
sha256: -
consensus: user-ratified 2026-07-27 (W79 decision D2, docs/plans/2026-07-27-W78-ratification-package.md; verbatim from the audited MAIN v5 design)
---

**Statement (datum only).** A *MAIN-CB current reset state* consists of: a
current index union $U$; its compressed ambient $A_U$ (a
[[def-compressed-corner|compressed corner]]); a recorded ambient defect
$\varepsilon_U$; a named finite-dimensional $C^*$-algebra $B_U$; a supplied
level-one map $v_U:B_U\to A_U$; the fixed amplification family
$(I_n\otimes v_U)_{n\ge1}$; a recorded map-defect number $d_U$; and a
supplied tag saying whether the map is an
[[def-extended-delta-inclusion|extended inclusion]] or extended isomorphism.

**Notes / provenance.** The tag is hypothesis data, not an existence or
success assertion. This shard asserts NO theorem content (R35): no
$d_U\le c_0^{\rm cb}\varepsilon_U$ invariant (that is the proof obligation of
the result row `lem-maincb-reset-invariant-preservation` / M19-R), no
smallness, admissibility, preservation, or construction. Companion data
packages: [[def-maincb-partition-state]] (geometry),
[[def-maincb-raw-call]] (one literal attempted call). Provisioned as P0 of
`DESIGN-MAIN-STRUCTURE-v5.md` (audited `AUDIT-MAIN-STRUCTURE-v4.md` §2,
VALID-WITH-CORRECTIONS applied; `AUDIT-MAIN-STRUCTURE-v5.md` REPAIR-CONFIRMED).
