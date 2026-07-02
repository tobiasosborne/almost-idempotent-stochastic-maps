---
id: conj-halo-collapse
kind: lemma
contract: Halo-robust height collapse: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), and hidden top vertex v of height H, let sigma be the invisible mass of v, sigma_g the halo-robust invisible mass (the positive coefficient mass v places on rows at ell-1 distance > tau/4 from conv W, tau = sqrt(delta)), and nu_v the row negative mass; then H * (1 - sigma_g) <= (sigma - sigma_g) * tau/4 + nu_v * (2 + 4*delta).
defs: def-signed-idempotent; def-height; def-visible-set; def-invisible-mass; def-negative-mass
deps: lem-mass-split; lem-residual-lower; lem-residual-upper
status: proved
af: validated
provenance: docs/waves/2026-07-02-F2-sigma-cap-refuter.md (arm F wave 2, opus worker, [check] mechanism: split the row reproduction with halo recipients priced at tau/4 instead of H); verified exact and non-vacuous on the three certified instances of runs/2026-07-02-sigma-cap-refuter/ (halo_bound_check.py)
owner: A
workspace: proofs/conj-halo-collapse
---

**af-VALIDATED IN-REPO 2026-07-02** (run 2 on the fresh factored workspace, clean): 20-node
adversarial tree, root `validated`, taint 20/20 clean; fresh codex prover/verifiers per node, Claude
orchestrated only (§6); imports the three af-validated deps [[lem-mass-split]],
[[lem-residual-lower]], [[lem-residual-upper]] as externals. Ledger:
`proofs/conj-halo-collapse/ledger/`; export: `proofs/conj-halo-collapse/export.md`. Status flip is
the mechanical reflection of the codex ledger. (Run 1, pre-factoring, ballooned 49>40; the factoring
cured it: 20 vs 49 nodes.)

**Original framing (arm F wave-2 candidate).** The self-mass-immune refinement of the af-validated
[[obs-height-collapse]]: recipients inside the `τ/4`-halo of `C_W` are priced at their actual distance
(`≤ τ/4`) rather than the worst case `H`, so the bound stays non-vacuous even when raw `σ̃ ≥ 1` via
self/halo mass (see [[obs-sigma-halo-nonrobust]]). Same proof shape as the validated bound plus one
extra split of the positive mass into halo vs genuine pots.

**Role:** if af-validated, this replaces obs-height-collapse as the finisher bridge: together with a
halo-robust cap `σ̃_g ≤ 1 − c` (mechanism candidate: [[conj-no-free-frontier]]) it yields
`H = O(τ)` — the Kernel Conjecture's height cap.

**Elevation history:** run 1 (2026-07-02) ABORTED [BALLOON] at 49 live nodes (> cap 40) in 2 rounds,
20/49 validated, root pending. Classification: 6× DAG/cross-sibling (the mass-split identity
`Σ a_j⁺ = 1+ν` / `σ−σ_g ≥ 0` bookkeeping and the residual-distance bounds are re-derived inline and
cross-referenced between siblings) + 1 missing bridge fact. NOT a mathematical refutation — a
structure signal per §6.3: FACTOR the mass-split bookkeeping and the residual-distance estimates into
registry sub-lemmas (deps of this node), then re-seed and re-orchestrate (bd aism-*, quota-gated).
The partial tree remains in `proofs/conj-halo-collapse/` pending the factoring.

**Factoring (2026-07-02, aism-q7e):** three sub-lemma deps registered — [[lem-mass-split]] (the
`sum a_j^+ = 1 + nu` pot bookkeeping, run-1 nodes 1.1.2/1.1.3/1.4.1.3.x), [[lem-residual-lower]]
(the convex-outsourcing lower bound, run-1 node 1.4.2), [[lem-residual-upper]] (the residual-distance
upper bound, run-1 node 1.4.3). Both residual lemmas are stated frame-free (pure l1 convex geometry).
Plan: af-validate the three sub-lemmas, then wipe + re-seed this workspace (root contract UNCHANGED)
with the deps registered as externals, and re-orchestrate.
