---
id: op-hlc
kind: open-problem
contract: (OPEN) Hull-linear cap HLC: there are universal delta_0>0 and C_1<inf (n-free) such that every exact signed idempotent P with delta(P) <= delta_0 satisfies H(P) <= C_1*sqrt(delta(P)), equivalently delta >= H^2/C_1^2.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-height
deps: lem-kernel-implies-hlc; conj-kernel
status: open
af: none
provenance: trunk step <2>5 target; statement per docs/ingest/report/kernel-conjecture.tex thm:chain (a) (mod-audit record), registered in-repo by the W22 wave (aism-pu0)
owner: A
workspace: proofs/op-hlc
---

**Role (the trunk's middle rung).** `op-classical ⇐ op-exposed-hull ⇐ HLC ⇐ conj-kernel`. This shard
makes HLC a first-class DAG node so the linker sees the finisher chain: [[lem-kernel-implies-hlc]]
establishes HLC **conditionally on [[conj-kernel]]** with C₁ = max{B,3} (reviewed, 2026-07-06);
unconditionally it is OPEN — exactly as open as the Kernel Conjecture, by that implication.
Consumed by [[op-exposed-hull]] (the mod-audit trunk step <2>6, never independently checked here).

**Status discipline.** `open`: no unconditional proof exists at any rigour tier. Do not flip on the
strength of the conditional implication alone.
