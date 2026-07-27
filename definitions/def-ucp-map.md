---
id: def-ucp-map
term: unital completely positive map
aliases: UCP map; UCP; completely positive unital map
kind: consensus
status: locked
source: internal
locus: standard operator-algebra textbook notion (e.g. Paulsen, Completely Bounded Maps and Operator Algebras, ch. 2-3); adopted for the Route-F rows per AUDIT-F0-ASSEMBLY.md sect 1.1
sha256: -
consensus: user-ratified 2026-07-27 (W79 decision D3, docs/plans/2026-07-27-W78-ratification-package.md; def shard chosen over an L2 textbook exemption because the F0 lift row's contract concludes "Phi is UCP")
---

**Statement.** Let $A$ and $B$ be unital $C^*$-algebras (in this repo's
Route-F usage: finite-dimensional, typically $\ell_\infty^n$, $M_n$, or a
finite-dimensional unital $C^*$-algebra $\mathcal B$). A linear map
$\varphi:A\to B$ is *positive* if $\varphi(a)\ge0$ whenever $a\ge0$;
*completely positive* (CP) if for every $r\ge1$ the amplification
$\mathrm{id}_{M_r}\otimes\varphi: M_r(A)\to M_r(B)$ is positive; and
*unital* if $\varphi(1_A)=1_B$. A *UCP map* is a unital completely positive
map. Standard facts used silently at the BSc/MSc level: a UCP map is
contractive; a positive map out of a commutative $C^*$-algebra is
automatically CP; compositions of UCP maps are UCP.

**Notes / provenance.** Provisioned per the F0 assembly audit
(`AUDIT-F0-ASSEMBLY.md` §1.1: the acronym UCP appeared in proposed
contracts with no canonical anchor in the definitions layer). Consensus
adoption of the universal textbook notion — no project-specific content.
Consumers: the F0 lift rows (`lem-routef-f0-ucp-lift`), the K-ledger
factorization rows (UCP $\Delta,\Upsilon$), F2. Related:
[[def-stochastic]] (row-stochastic = unital positive on $\ell_\infty^n$),
[[def-fd-cstar-diagonal]].
