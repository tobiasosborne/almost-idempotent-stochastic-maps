---
id: def-slab
term: slab
aliases: low slab; low-slab; deep low slab; very-low slab; top slab; top-slab; far slab; slab leakage
kind: original
status: draft
source: internal
locus: internal; first pinned across argument/lemmas/conj-low-slab-cap.md, lem-cs-low-slab-pincer.md, lem-top-slab-companion.md
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by conj-low-slab-cap (exposer-value slab) and lem-top-slab-companion (depth slab)
---

**Statement.** Fix an [[def-signed-idempotent|exact signed idempotent]] $P$, $\tau=\sqrt{\delta(P)}$,
nonempty [[def-visible-set|visible set]] $\mathcal W$. A **slab** is the set of rows on which a fixed
affine functional lies in a prescribed threshold band. Two families recur, kept distinct here:

- **Low slab** (exposer-value): for an [[def-exposed|optimal exposer]] $h^*$ at a vertex and a
  threshold $s$, the set $\{j:h^*(p_j)<s\}$. The **deep / very-low slab** takes $s=\kappa=\tau/4$ or
  $s=\tau/8$; combined with depth ($d_j>a\tau$) it is the summand set of [[conj-low-slab-cap]] and
  [[conj-far-low-slab-cap]]. The pincer [[lem-cs-low-slab-pincer]] controls its complementary shell
  $\{s\le h^*<\kappa\}$.
- **Top slab** (depth / [[def-top-deficit|top-deficit]]): the near-top band
  $\{j:d_j>H-c\tau\}$ (equivalently small top-deficit $z_j<c'\tau$); the **far slab** additionally
  imposes $\rho$-farness. [[lem-top-slab-companion]] forces a $\rho$-far row in the top slab.

**Notes / provenance.** Project-original; "slab" is overloaded in the shards between the
exposer-value cut ($h^*$) and the depth cut ($d$ / $z$) — this shard records BOTH canonical instances
and which functional each uses, so downstream statements can name the functional explicitly and avoid
drift. `status: draft` — A+B sign-off pending (Rule 7). Related: [[def-top-deficit]],
[[def-near-cluster]], [[def-exposed]].
