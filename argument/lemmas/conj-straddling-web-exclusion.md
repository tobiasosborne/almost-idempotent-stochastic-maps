---
id: conj-straddling-web-exclusion
kind: lemma
contract: (CONJECTURE) Co-top straddling-web exclusion (SL1a): there exists universal delta_0 > 0 such that no exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, and hidden top vertex v of height H > 16*tau admits a probability measure lambda on rows that are simultaneously rho-far from v (||p_f - p_v||_1 >= 4*tau) and co-top (dist_1(p_f, conv W) > H - 4*tau), with barycenter within 2.2*tau of p_v and with average value <= (16/13)*kappa under every admissible exposer at v.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-sl1a-three-cell-reduction
status: conjecture
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): Fable author L2's SL1a, V-L2-audited (the Case-(i) reduction proved with the mu = 0 split and the 3/16-vs-1/8+delta/4 distinction per corrections). Full derivation: docs/waves/2026-07-09-W54-artifacts/l2-attack.md §2.7
owner: A
---

**Role (the unified rigidity core — Branch I and Branch II meet here).** The
mutual-exposure-rigidity target materialized with proved constants: a rho-spanning
co-top web whose barycenter huddles at the top and which every exposer sees only at
(16/13)*kappa cannot exist. With [[conj-shallow-counterweight-exclusion]] it closes
L2-core hence Branch II ([[lem-l2-core-collapse]]); it is simultaneously the shape of
[[conj-cotop-web-coupling]]'s dual-forced web (Branch I). PROVED CORRECTION to the naive
unifier (Proposition E, V-L2-checked): the pure co-top form is NOT forced — a shallow
counterweight of mass ~4*tau/D passes all mass/depth caps at H < ~1/4; only the
universal-shadow pin (SL1b) blocks that escape, so the PAIR is the honest surface.

**Status discipline.** A conjecture — promotes nothing; consumers carry it as a dep.
