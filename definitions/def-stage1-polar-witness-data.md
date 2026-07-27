---
id: def-stage1-polar-witness-data
term: Stage-1 polar witness data
aliases: polar witness tuple; Stage-1 polar constants tuple
kind: original
status: locked
source: internal
locus: DESIGN-S1-POLAR-v6.md sect 8 (unchanged from v2 sect 8; audited AUDIT-S1-POLAR-v3/v4/v5/v6)
sha256: -
consensus: user-ratified 2026-07-27 (W79 decision D2, docs/plans/2026-07-27-W78-ratification-package.md; verbatim from the audited polar design)
---

**Statement (data and typing only).** A *Stage-1 polar witness datum* is a
tuple $W$ of fourteen named scalar fields:
$$W=(C_{\rm rect},\,C_{\rm ch},\,C_{\rm pol},\,C_{\rm grp},\,C_{\rm path},\,C_{\rm der},\,
e_{\rm rect},\,\kappa_{\rm ch},\,\kappa_{\rm pol},\,\kappa_{\rm der},\,
\delta_*,\,\varepsilon_*^r,\,e_{\rm S1},\,r_{\rm iso}).$$
The first six are called coefficients, the next four margins, the last four
derived scales.

**Notes / provenance.** Pure data: this shard contains NO positivity,
inequality, existence, uniqueness, estimate, map, regularity, admissibility,
or topological assertion (R35; `AUDIT-S1-POLAR-v4.md` §7: "VALID AS DATA").
The analytic-witness relation — that one such tuple simultaneously witnesses
the seven Stage-1 polar producer rows and satisfies the scalar arithmetic —
is exported ONLY by the result rows
`lem-stage1-polar-scalar-arithmetic` and `lem-stage1-polar-constant-ledger`
and their seven parameterized transport helpers
(`DESIGN-S1-POLAR-v6.md` §§2–3), never by this definition. Related:
[[def-approximate-unitary-space]], [[def-epsilon-cstar-algebra]].
