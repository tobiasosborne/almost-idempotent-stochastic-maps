---
id: lem-routef-f0-ucp-lift
kind: lemma
contract: Route F F0 UCP lift: let n >= 1, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C) and J: C^n -> M_n the diagonal inclusion, let Q: l_inf^n -> l_inf^n be row-stochastic, and let Q_C: C^n -> C^n be the canonical complex-linear extension of Q; then Phi := J Q_C D: M_n -> M_n is a unital completely positive map.
defs: def-stochastic; def-ucp-map
deps:
status: proved-mod-audit
af: seeded
provenance: docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md Q4 (fresh hostile audit, verdict VALID); design + fresh hostile audit docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md sect 1.1 + AUDIT-F0-ASSEMBLY.md sect 1.1 (VALID-WITH-CORRECTIONS; the Q_C typing and def-ucp-map import corrections are applied here); user-ratified landing 2026-07-27 (W79/W80, docs/plans/2026-07-27-W78-ratification-package.md sect 5 step 1)
owner: A
workspace: proofs/lem-routef-f0-ucp-lift
---

**Status.** Local paper proof, hostile-audited twice (W73B Q4; F0-assembly
audit §1.1) — `proved-mod-audit`, NOT rigorous. Elevation-ready: projected
af budget 3 nodes / depth 2 (positivity/complete positivity, unitality,
root).

**Proof sketch (per the audited design).** A row-stochastic $Q$ is positive
and unital on $\ell_\infty^n$ ([[def-stochastic]]); its complexification
$Q_{\mathbb C}$ is a positive unital map of the commutative $C^*$-algebra
$\ell_\infty^n(\mathbb C)$, hence completely positive
([[def-ucp-map]]: positivity out of a commutative $C^*$-algebra is
automatically CP); the diagonal extraction $D$ and inclusion $J$ are UCP;
and compositions of UCP maps are UCP.

**Role.** First of the two F0 seam rows: transfers the stochastic input
into the Kitaev matrix-algebra setting. Companion:
[[lem-routef-f0-defect-identity]]. Future consumer: the strengthened
[[lem-routef-k-ledger]] parent (per the ratified package §5; the
DO-NOT-REWIRE guard on that row remains until its designated step).
Independent of the MAIN, polar, and ledger fronts.
