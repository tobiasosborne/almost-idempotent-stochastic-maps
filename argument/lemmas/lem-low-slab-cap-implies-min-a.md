---
id: lem-low-slab-cap-implies-min-a
kind: lemma
contract: Low-slab-cap implies MIN-A: assuming conj-low-slab-cap at width a = 4 (constants theta in (0,1), delta_0 > 0) together with lem-cs-low-slab-pincer, conj-min-a-w4 holds, i.e. every exact signed idempotent P with 0 < delta(P) <= min(delta_0, (17-12*sqrt(2))/2), nonempty visible set W(P), and height H > 13*tau (tau = sqrt(delta)) has a hidden top vertex v with sigma_4(v) <= 1/2 (positive coefficient mass on rows at l1-distance > 4*tau from conv W), by splitting G_4 = {j in G_4 : h_v*(p_j) < tau/4} (capped 1 - theta - 4*tau by conj-low-slab-cap) and {j in G_4 : h_v*(p_j) >= tau/4} (capped O(tau) via lem-cs-low-slab-pincer at s = tau/4).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height; def-slab; def-near-cluster
deps: conj-low-slab-cap; lem-cs-low-slab-pincer
status: stated
af: none
provenance: transcribed 2026-07-10 (Phase-2 DAG-wiring wave) from conj-low-slab-cap's role note ("At (a, theta) = (4, 1/2) this implies conj-min-a-w4") + the lem-cs-low-slab-pincer composition; STATED (unverified in-repo), pending a hostile-verification pass
owner: A
workspace: proofs/lem-low-slab-cap-implies-min-a
---

**Role (wiring bridge, low-slab component -> MIN-A height culmination).** Makes the prose-only
implication "[[conj-low-slab-cap]] $\Rightarrow$ [[conj-min-a-w4]]" a DAG edge, so the linker sees the
[[def-near-cluster|near-cluster]]/[[def-slab|low-slab]] absorption machinery feeding
[[lem-min-a-implies-height]] (the height bound $H\le 13\tau$). The MIN-A slab-mass
$\sigma_4(v)$ is over ALL deep rows $G_4=\{j:\operatorname{dist}_1(p_j,\operatorname{conv}\mathcal W)>4\tau\}$;
[[conj-low-slab-cap]] caps only the sub-sum on the deep LOW-exposer slab $\{h_v^*<\tau/4\}$, so the
complementary shell $\{h_v^*\ge\tau/4\}$ must be capped separately — that is exactly
[[lem-cs-low-slab-pincer]] at $s=\tau/4$ ($\nu_v/\kappa\le 4\tau$).

**STATUS DISCIPLINE (L0).** `status: stated` — transcribed from the sketch/role-note prose, NOT
independently verified here. The constant bookkeeping (that the two caps sum to $\le 1/2$ at the
stated $\delta$ ceiling, and that the $(a,\theta)=(4,1/2)$ calibration of [[conj-low-slab-cap]] is the
intended instance) is the content a hostile-verification wave must confirm before any promotion.
Locus: [[conj-low-slab-cap]] role note; sketch `docs/plans/2026-07-10-top-down-proof-sketch-v24.md`
lineage (v9 five-route convergence). FLAGGED for the batch hostile pass.
