---
id: def-maincb-partition-state
term: MAIN-CB partition state
aliases: MAIN partition state
kind: original
status: locked
source: internal
locus: DESIGN-MAIN-STRUCTURE-v5.md sect 1.4
sha256: -
consensus: user-ratified 2026-07-27 (W79 decision D2, docs/plans/2026-07-27-W78-ratification-package.md; verbatim from the audited MAIN v5 design); AMENDED user-ratified 2026-07-30 in-session: 'one current union U of classes' -> 'one current nonempty subset U of J' (the strict class-union field made the M13/M19-S2/M25 partial-class hypotheses unsatisfiable — M13 validated VACUOUSLY, bead aism-usmn; class-union-ness, where needed, is a per-row hypothesis and M12/M26/M27 already state it explicitly)
---

**Statement (geometry only).** A *MAIN-CB partition state* consists of: a
finite atomic index set $J$; an ambient $A$; a supplied commutative map
$w:\mathbb C^J\to A$; the images $P_j=w(e_j)$; the conditional relation
$j\sim k\iff\dim S^A_{P_j,P_k}=1$; when this relation is an equivalence, its
class family $\mathcal C$; for $U\subseteq J$, $P_U=\sum_{j\in U}P_j$ and
$A_U=S^A_{P_U}$ (a [[def-compressed-corner|compressed corner]]); one current
nonempty subset $U$ of $J$; and a reference to one separately supplied
[[def-maincb-reset-state]] for that subset.

**Notes / provenance.** This shard records NEITHER the global ambient defect
NOR a defect/unit tag for $w$: every consuming result that needs those
bounds must quantify $A$ as an extended $\varepsilon$-$C^*$-algebra and $w$
as an extended inclusion explicitly, AND must tie the state to that same
displayed $(A,w)$ ("a supplied MAIN partition state for this same $A,w$" —
the identity constraint of `AUDIT-MAIN-STRUCTURE-v4.md` §3.1, applied in
MAIN v5). It asserts neither that $\sim$ is an equivalence nor that a
current map exists ("when the relation is an equivalence" is conditional
data, not an assertion — `AUDIT-MAIN-STRUCTURE-v3.md` §2). Its single
current union cannot supply simultaneous $U,V$ data: cross-class rows (M12,
M19-S3) require two separately supplied reset states. Companions:
[[def-maincb-reset-state]], [[def-maincb-raw-call]];
[[def-extended-delta-inclusion]], [[def-extended-epsilon-cstar-algebra]].
