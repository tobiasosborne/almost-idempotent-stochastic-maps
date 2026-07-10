---
id: def-top-support-functional
term: top support functional
aliases: top support functional phi; Phi_v; support functional at the top; averaged phi-bar
kind: original
status: draft
source: internal
locus: internal; first pinned in argument/lemmas/lem-top-deficit-price.md and lem-top-support-dual-face.md
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by lem-top-deficit-price (existence) + lem-top-support-dual-face (the dual face Phi_v)
---

**Statement.** Fix an [[def-signed-idempotent|exact signed idempotent]] $P$ with nonempty
[[def-visible-set|visible set]] $\mathcal W$, write $C_{\mathcal W}=\operatorname{conv}\{p_w:w\in\mathcal W\}$,
and let $v$ be a [[def-height|hidden top vertex]] of height $H$.

A **top support functional** at $v$ is an affine $\phi:\mathbb R^n\to\mathbb R$ with
$$\phi(p_v)=H,\qquad \phi\le 0\ \text{on}\ C_{\mathcal W},\qquad \phi\ \text{is $1$-Lipschitz for }\ell^1.$$
The set of all such is $\Phi_v$; it is nonempty ([[lem-top-deficit-price]]), convex and compact, and
by [[lem-top-support-dual-face]] equals $\{\phi_y(x)=y\cdot x-h_{C}(y):y\in Y_v\}$ where
$h_C(y)=\sup_{c\in C_{\mathcal W}}y\cdot c$ and $Y_v=\{y:\lVert y\rVert_\infty\le1,\ y\cdot p_v-h_C(y)=H\}$.
A finite convex average of top support functionals (an **averaged $\bar\phi$**) is again a top support
functional (the three defining conditions are convex).

**Notes / provenance.** Project-original; the affine functional that realizes the height of the top
and pins the [[def-top-deficit|top-deficit]] $z_j=H-\phi(p_j)\ge0$. It is the charging channel of
[[lem-top-deficit-price]]. `status: draft` — A+B sign-off pending (Rule 7). Related:
[[def-top-deficit]], [[def-height]], [[def-visible-set]].
