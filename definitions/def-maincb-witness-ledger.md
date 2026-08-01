---
id: def-maincb-witness-ledger
term: MAIN-CB witness ledger
aliases: MAIN witness tuple; MAIN-CB constants tuple
kind: original
status: locked
source: internal
locus: DESIGN-MAINCB-REPAIR-v2.md sect 2 (hostile-audited AUDIT-MAINCB-REPAIR.md, verdict VALID AS DATA)
sha256: -
consensus: user-ratified 2026-08-01 (tobiasosborne, in-session sign-off; delegated ratification for consensus/original tiers; aism-jl4g repair package)
---

**Statement (data and typing only).** A *MAIN-CB witness ledger* is a tuple W of twelve named real scalar fields
$$
W=(c0_{cb},L,K1,K2,K3,K_{call},e_{env},e1,e_{s2},e_{cross},r_{reset},epsilon_{MAIN}).
$$
The first five fields are receiving coefficients, the sixth is a derived coefficient, the next four are receiving margins, and the last two are derived scales.

**Notes / provenance.** Pure data: this shard contains no inequality between fields, no existence, uniqueness, estimate, map, regularity, admissibility, or dimension-freeness assertion. The analytic-witness relation and scalar arithmetic are exported only by `lem-maincb-witness-arithmetic` and `lem-maincb-reset-constant-ledger`. This is the MAIN-CB instance of the typed-witness pattern in `def-stage1-polar-witness-data` and `DESIGN-S1-POLAR-v6.md` sects 2--3 and 8, motivated by `docs/LEARNINGS.md` 2026-07-28 laws (i)--(ii). Related: [[def-maincb-reset-state]], [[def-maincb-raw-call]], [[def-maincb-partition-state]].
