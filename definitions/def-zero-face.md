---
id: def-zero-face
term: zero-face row
aliases: zero face; zero-face family; always-tight zero-face family; Z(u); h-zero row; zero-face conic mass
kind: original
status: draft
source: internal
locus: internal; first pinned in argument/lemmas/lem-zero-face-localization.md and lem-always-tight-dual-support.md
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by lem-zero-face-localization (rho-nearness) + lem-always-tight-dual-support (the alpha-carrier family Z)
---

**Statement.** Fix an [[def-signed-idempotent|exact signed idempotent]] $P$ and a hidden
([[def-exposed|not $(\rho,\kappa)$-exposed]]) geometrically distinct row vertex $u$, with the
exposedness LP at $u$ (the program defining $t^*(u)$, see [[def-exposed]]) and an *optimal exposer*
$h^*$ (an admissible affine $h$ attaining $t^*(u)$).

A row $z$ is a **zero-face row** of $u$ if $h^*(p_z)=0$, i.e. $z$ lies on the zero face
$\{x:h^*(x)=0\}$ of the optimal exposer. The **always-tight zero-face family** $Z(u)$ is the set of
rows whose lower-box constraint $h\ge 0$ is tight on the *whole* primal optimal face of the LP
(equivalently, $\operatorname{supp}(\alpha)\subseteq Z(u)$ for every reduced optimal hiddenness
[[def-dual-witness|dual witness]] $(\lambda,\alpha,\beta)$, by [[lem-always-tight-dual-support]]).
The **zero-face conic mass** is $\sum_{z\in Z(u)}a_z$ for the reduced optimal display's zero-face
coefficients $a_z\ge 0$.

By [[lem-zero-face-localization]] every zero-face row is $\rho$-near $u$
($\lVert p_z-p_u\rVert_1<4\tau$, $\tau=\sqrt{\delta}$); if $u$ is within $4\tau$ of a
[[def-height|hidden top]] $v$ of height $H$ then additionally $\lVert p_z-p_v\rVert_1<8\tau$ and $z$
has depth $>H-8\tau$.

**Notes / provenance.** Project-original; the vocabulary in which the huddle-charge terminal node
is posed (kill or bound the zero-face conic mass). Distinguish two uses in the shards, kept
consistent here: the *pointwise* zero-face row ($h^*(p_z)=0$ for one fixed optimal exposer) and the
*always-tight family* $Z(u)$ (tight on the entire optimal face). $Z(u)$ is the always-tight version;
statements that fix one optimal exposer $h^*$ use the pointwise version, and the two agree on the
relative interior optimal exposer. `status: draft` — A+B sign-off pending (Rule 7). Related:
[[def-actor-hull]] (the always-tight far/upper-box hulls $K_T,K_O$), [[def-dual-witness]].
