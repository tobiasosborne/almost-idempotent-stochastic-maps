---
id: def-near-cluster
term: near-cluster
aliases: rho-near deep cluster; near-deep cluster; cluster C(v); C(v); huddle cluster; cluster mass
kind: original
status: draft
source: internal
locus: internal; first pinned in argument/lemmas/conj-near-cluster-absorption.md
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by conj-near-cluster-absorption (the summand set C(v)) and the W54 huddle-charge tree
---

**Statement.** Fix an [[def-signed-idempotent|exact signed idempotent]] $P$ with nonempty
[[def-visible-set|visible set]] $\mathcal W$, a [[def-height|hidden top vertex]] $v$ of height $H$,
$\tau=\sqrt{\delta(P)}$, $\rho=4\tau$, and a width constant $a\ge4$. Write
$d_j=\operatorname{dist}_1(p_j,\operatorname{conv}\{p_w:w\in\mathcal W\})$.

The **near-cluster** (or $\rho$-near deep cluster) of $v$ is
$$C(v)\;:=\;\{\,j:\ \lVert p_j-p_v\rVert_1<4\tau\ \text{ and }\ d_j>a\,\tau\,\}$$
— rows simultaneously $\rho$-near $v$ **and** deep (both conditions required). The **cluster mass**
is $\sum_{j\in C(v)}\max(P_{vj},0)$; a top is **heavy** when this is $\ge1-\theta_0$. A
**cluster vertex** is a geometrically distinct row vertex $u$ carrying positive disintegrated weight
from $C(v)$-rows (or, in the re-rooted assembly, $u:=v$ itself).

**Notes / provenance.** Project-original; the exact summand set of
[[conj-near-cluster-absorption]] and the pinned target of the W54 huddle-charge decomposition tree.
The width $a$ is a calibration constant (any universal $a\ge4$; $a=16$ in the W54 assembly), not
load-bearing downstream. NOTE ON DIVERGENCE: the bare word "cluster" is also used generically for an
arbitrary row-index subset $C$ (e.g. [[lem-cluster-return-flow]]'s return flow over any subset) — that
generic set-theoretic use is common knowledge and is NOT this term; this shard defines only the
huddle near-cluster $C(v)$. `status: draft` — A+B sign-off pending (Rule 7). Related: [[def-co-top]],
[[def-slab]].
