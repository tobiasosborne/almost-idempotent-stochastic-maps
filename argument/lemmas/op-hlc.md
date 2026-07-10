---
id: op-hlc
kind: open-problem
contract: (OPEN) Hull-linear cap HLC: there are universal delta_0>0 and C_1<inf (n-free) such that every exact signed idempotent P with delta(P) <= delta_0 satisfies H(P) <= C_1*sqrt(delta(P)), equivalently delta >= H^2/C_1^2.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-height
deps: 
routes: [lem-kernel-implies-hlc; conj-kernel] | [lem-min-a-implies-height]
status: open
af: none
provenance: trunk step <2>5 target; statement per docs/ingest/report/kernel-conjecture.tex thm:chain (a) (mod-audit record), registered in-repo by the W22 wave (aism-pu0)
owner: A
workspace: proofs/op-hlc
---

**Role (the trunk's middle rung).** `op-classical ⇐ op-exposed-hull ⇐ HLC ⇐ {Kernel route ∨ MIN-A
route}`. This shard makes HLC a first-class DAG node so the linker sees the finisher chain. HLC has
**two independent conditional routes** to closure (an OR-ROUTE, `routes:` field, aism-3ne — the
honest encoding: BOTH are declared without falsely asserting their conjunction):

- **Route 1 (Kernel).** [[lem-kernel-implies-hlc]] establishes HLC **conditionally on [[conj-kernel]]**
  with C₁ = max{B,3} (reviewed, 2026-07-06).
- **Route 2 (MIN-A).** [[lem-min-a-implies-height]] establishes the height bound (H ≤ 13·√δ on the
  nonempty-visible regime) conditionally on the MIN-A/absorption web (`conj-min-a-w4` and its
  29-node component).

Unconditionally HLC is OPEN — exactly as open as *whichever* single open input a route bottoms out
in. Consumed by [[op-exposed-hull]] (the mod-audit trunk step <2>6, never independently checked here).

**Status discipline.** `open`: no unconditional proof exists at any rigour tier on *either* route. Do
not flip on the strength of a conditional implication alone. The disjunction is satisfied (→ `ready`)
only when some ONE route's members are all `af: validated`/`cited` (linker rule, `--closure-min op-hlc`
prints the per-route ancestor sets).
