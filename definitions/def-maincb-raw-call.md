---
id: def-maincb-raw-call
term: MAIN-CB raw call
aliases: MAIN raw-call datum
kind: original
status: locked
source: internal
locus: DESIGN-FUDW-DECOMP-v4.1.md:424-428; DESIGN-MAIN-STRUCTURE-v5.md sect 1.3
sha256: -
consensus: user-ratified 2026-07-27 (W79 decision D2, docs/plans/2026-07-27-W78-ratification-package.md; verbatim from the audited MAIN v5 design)
---

**Statement (literal-call record only).** A *MAIN-CB raw call* consists of: a
literal call-type tag (global scalar, compressed-corner scalar, Stage 1,
Stage 2, or Stage 3); the supplied input reset states/maps
([[def-maincb-reset-state]]); the named finite-dimensional $C^*$-algebra
source and explicit target corner; a pre-helper base scale $t$; any
post-helper datum scale; the literal output level-one map and its fixed
amplification family; the recorded target ambient defect
$\varepsilon_{\rm target}$; and a recorded raw-defect number $d_{\rm raw}$.

**Notes / provenance.** A recorded number does NOT assert that the literal
map is an extended inclusion or isomorphism — result rows consuming a raw
call must state that hypothesis explicitly (`AUDIT-MAIN-STRUCTURE-v3.md`
fatal defect C; the corrected M19-R does so). No hidden domain, smallness,
success, reset, preservation, or iteration clause is present (R35). The two
scalar tags are distinct because the global scalar call uses base scale
$t_0=\varepsilon$ whereas the compressed-corner scalar call at the one-class
induction base uses $t_{\rm atom}=K_{\rm call}\varepsilon$
(`AUDIT-MAIN-STRUCTURE-v3.md` fatal defect D; MAIN v5 §2). Companions:
[[def-maincb-partition-state]], [[def-maincb-reset-state]].
