---
id: lem-huddle-charge-assembly
kind: lemma
contract: Huddle-charge assembly (W54 tree, tall restriction): if lem-l2-core-collapse (Branch-II core), conj-straddling-web-exclusion (SL1a), conj-shallow-counterweight-exclusion (SL1b), and conj-cotop-web-coupling all hold, then conj-near-cluster-absorption holds on its tall regime, i.e. there are universal (a, theta_0) = (16, 1/8) and delta_0 > 0 such that no exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, and hidden top vertex v of height H > 16*tau carries positive coefficient mass sum over {j : ||p_j - p_v||_1 < 4*tau, dist_1(p_j, conv W) > 16*tau} of max(P_vj, 0) >= 1 - theta_0 — modulo the registered assembly gaps AG-1 (t*(v) = 0) and AG-2 (u = v instantiation) and the L5 far-deep minimax sub-leaf, all per the W54 tree Section 4.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height; def-near-cluster; def-co-top; def-actor-hull; def-top-support-functional
deps: lem-l2-core-collapse; conj-straddling-web-exclusion; conj-shallow-counterweight-exclusion; conj-cotop-web-coupling
status: stated
af: none
provenance: transcribed 2026-07-10 (Phase-2 DAG-wiring wave) from docs/plans/2026-07-09-w54-huddle-charge-decomposition-tree.md Section 4 (the assembly implication, G8-v3 constant discipline) — V-ASM-2 verdict VALID-WITH-CORRECTIONS (modulo R4 t*(v)=0 audit, discharged modulo V-R4); STATED (the leaf-set refactor and AG gaps are unresolved in-repo), pending a hostile-verification pass
owner: A
workspace: proofs/lem-huddle-charge-assembly
---

**Role (wiring bridge, the huddle-charge four-leaf system -> the near-cluster charge).** Makes the
W54 assembly implication a DAG edge: the [[def-actor-hull|hull-disjointness]] case tree over a tall
heavy top closes through four leaves — [[lem-l2-core-collapse]] (Branch II, the intersection core),
[[conj-straddling-web-exclusion]] (SL1a, itself the three [[def-co-top|co-top]] cells via
[[lem-sl1a-three-cell-reduction]]), [[conj-shallow-counterweight-exclusion]] (SL1b), and
[[conj-cotop-web-coupling]] — yielding the tall restriction of [[conj-near-cluster-absorption]]. At
$(a,\theta_0)=(16,1/8)$ the assembly regime $H>16\tau$ CONTAINS
[[conj-near-cluster-absorption]]'s regime $H>172\tau$, so the assembly conclusion implies the
conjecture there.

**STATUS DISCIPLINE (L0) — do not over-read.** `status: stated`. This bridge is a faithful
transcription of the W54 tree Section 4 (`docs/plans/2026-07-09-w54-huddle-charge-decomposition-tree.md`),
whose verifier verdict is VALID-WITH-CORRECTIONS, NOT a clean pass. Three honest caveats, part of this
shard's interface:
  - **AG-1** (Step A1): the $t^*(v)=0$ hidden-top boundary; discharged only "modulo V-R4"
    (positive-margin lemma), not cleanly at contract level here.
  - **AG-2** (Step C0): the $u:=v$ instantiation legality of the huddle shards.
  - **L5** (far-deep minimax): the far-deep deficit-visibility sub-leaf is consumed in the assembly
    but is NOT separately registered as a shard; its content is folded into the Branch-I closure.
The exact leaf-to-shard mapping is the session-13 refactor (four-leaf system, sketch v18 lineage), a
reorganization of the original L1-L7 tree; L1/L4 are proved corollaries of
[[lem-top-deficit-price]]/[[lem-affine-exposer-row-capacity]] and are not deps. FLAGGED for the batch
hostile pass; the assembly must NOT be promoted until AG-1/AG-2/L5 are registered and cleared.

**HOSTILE VERDICT: INVALID AS STATED (2026-07-10, fresh codex — docs/waves/2026-07-10-remediation-artifacts/verdict-bridges.md). DO NOT CONSUME.** The consumed contracts do NOT close Branch II: lem-l2-core-collapse gives only the equivalence with intersection-branch emptiness; NO registered contract derives the SL1a-or-SL1b configurations from intersecting hulls; the L5 minimax is an unregistered, unquantified premise. AG-1/AG-2 are individually repairable; the Branch-II gap is not. Repair path: codify the l2-attack §2.6-2.7 intersecting-hulls -> SL1a/SL1b derivation as a registry lemma + register the L5 premise, then re-verify (bead filed at the wave close).
