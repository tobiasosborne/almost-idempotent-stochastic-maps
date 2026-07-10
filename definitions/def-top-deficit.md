---
id: def-top-deficit
term: top-deficit
aliases: top deficit; z_j; deficit; top-deficit slab; Z_v(f); top-deficit supremum
kind: original
status: draft
source: internal
locus: internal; first pinned in argument/lemmas/lem-top-deficit-price.md and lem-top-support-dual-face.md
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by lem-top-deficit-price (z_j) + lem-top-support-dual-face (the supremum Z_v(f))
---

**Statement.** In the setting of [[def-top-support-functional]] — an
[[def-signed-idempotent|exact signed idempotent]] $P$, nonempty [[def-visible-set|visible set]],
[[def-height|hidden top]] $v$ of height $H$, and a top support functional $\phi\in\Phi_v$ — the
**top-deficit** of a row $j$ under $\phi$ is
$$z_j\;:=\;H-\phi(p_j)\;\ge\;0,$$
nonnegative because $\phi(p_j)\le\operatorname{dist}_1(p_j,C_{\mathcal W})\le H$ (and bounded above,
$z_j\le 2+4\delta$). The **top-deficit supremum** of a row $f$ is
$Z_v(f):=\sup_{\phi\in\Phi_v}\big(H-\phi(p_f)\big)=\sup_{y\in Y_v}y\cdot(p_v-p_f)$
([[lem-top-support-dual-face]]). A **top-deficit slab** is a band of rows cut by a threshold on $z$,
e.g. $\{j:z_j\ge L\}$.

**Notes / provenance.** Project-original; "deficit" alone always means this top-deficit in the
huddle-charge shards. The charging identity ([[lem-top-deficit-price]], from $P^2=P$ and $P\mathbf1=\mathbf1$)
is $\sum_j a_j^+z_j=\sum_j a_j^-z_j\le\nu_v(2+4\delta)$ with $a_j=P_{vj}$; its structural blind spot is
that rows in the $\rho$-ball of $v$ carry $z_j<4\tau$. `status: draft` — A+B sign-off pending (Rule 7).
Related: [[def-top-support-functional]], [[def-slab]], [[def-co-top]].
