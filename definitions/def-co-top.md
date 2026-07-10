---
id: def-co-top
term: co-top
aliases: co-top row; co-top vertex; co-top web; co-top far web; co-top zero-face mass; starved set
kind: original
status: draft
source: internal
locus: internal; first pinned in argument/lemmas/lem-cotop-witness-pinning.md and lem-downhill-cotop-conic-mass.md
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by lem-cotop-witness-pinning + lem-downhill-cotop-conic-mass
---

**Statement.** Fix an [[def-signed-idempotent|exact signed idempotent]] $P$ with nonempty
[[def-visible-set|visible set]] $\mathcal W$ and a [[def-height|hidden top vertex]] $v$ of height
$H$; write $d_j=\operatorname{dist}_1(p_j,\operatorname{conv}\{p_w:w\in\mathcal W\})$,
$\tau=\sqrt{\delta(P)}$.

A row $f$ is **co-top** (relative to $v$, at slack $c$) if it sits nearly as deep as the top:
$$d_f\;>\;H-c\,\tau\qquad(c>0\ \text{a small universal constant, typically }c\in\{4,8\}).$$
The **co-top far web** of $v$ is the set of rows that are simultaneously co-top **and** $\rho$-far
from $v$ ($\lVert p_f-p_v\rVert_1\ge4\tau$) — the **starved set**
$\{j:\lVert p_j-p_v\rVert_1\ge4\tau,\ d_j>H-8\tau\}$. By [[lem-cotop-witness-pinning]] more than
$13/16$ of a hidden top's [[def-dual-witness|dual-witness]] $\lambda$-mass sits in this starved set
(at $c=4$, $\delta\le1/4$), and by [[lem-downhill-cotop-conic-mass]] (disjoint
[[def-actor-hull|always-tight hulls]]) a definite share of the [[def-zero-face|zero-face]] conic mass
lands on nonclone, $\rho$-near, co-top rows.

**Notes / provenance.** Project-original; "co-top" names the deep-far actors that a hidden top's dual
witness is forced to charge yet its positive coefficient mass need not reach (the dual-required /
primal-starved tension at the heart of the huddle charge and [[conj-cotop-web-coupling]]). `status:
draft` — A+B sign-off pending (Rule 7). Related: [[def-dual-witness]], [[def-actor-hull]],
[[def-near-cluster]].
