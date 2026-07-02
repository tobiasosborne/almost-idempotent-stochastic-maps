---
id: obs-height-collapse
kind: obstruction
contract: Height collapse: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), and hidden top vertex v (height H = dist_1(p_v, conv W) maximal among rows), the invisible mass sigma_v and the row negative mass nu_v satisfy H * (1 - sigma_v) <= nu_v * (2 + 4*delta).
defs: def-signed-idempotent; def-height; def-visible-set; def-invisible-mass; def-negative-mass
deps: 
status: proved
af: validated
provenance: docs/waves/2026-07-02-F1-web-regime-hunt.md (arm F wave 1, opus worker; derivation from row reproduction p_v = sum_j P_vj p_j + the 2+4delta row-diameter bound); numerically 0/500 violations over the exact sweep runs/2026-07-02-web-regime-hunt/
owner: A
workspace: proofs/obs-height-collapse
---

**af-VALIDATED IN-REPO 2026-07-02** (run 2, narrowed contract): 19-node adversarial tree, root
`validated`, taint 19/19 clean; fresh codex prover/verifiers per node, Claude orchestrated only (§6).
Ledger: `proofs/obs-height-collapse/ledger/`; export: `proofs/obs-height-collapse/export.md`. The FIRST
NEW (non-inherited) rigorous result of the campaign. Original derivation sketch (arm F wave 1): split
the exact row reproduction
`p_v = sum_j P_vj p_j` into visible-side positive mass (distance 0 from `C_W`), invisible positive mass
`sigma_v` on rows that are themselves at distance `<= H` (v is the top), and negative mass `nu_v <= delta`
paying the row-diameter price `2+4delta`; convexity of `dist_1(., C_W)` gives
`H <= sigma_v*H + nu_v*(2+4delta)`. The quantitative, clone-invariant sharpening of the record's s8 cap.

**Role:** the structural reason arm F's ~48k-instance hunt never entered the dangerous regime — `sigma_v >
tau` is cheap but INERT for height; the antecedent re-scopes to `sigma_v -> 1`. **If af-validated, this is
a candidate FINISHER input**: together with a bound `sigma_v <= 1 - c*tau` for hidden vertices it yields
`H <= delta(2+4delta)/(c*tau) = O(sqrt(delta))`, i.e. the Kernel Conjecture's height cap.

**Consequences (commentary, NOT part of the contract):** the bound gives `H = O(delta)` unless
`sigma_v -> 1` (non-bootstrapping); together with a future bound `sigma_v <= 1 - c*tau` for hidden
vertices it would yield `H = O(sqrt(delta))` — the Kernel Conjecture's height cap. That composition is a
SEPARATE future lemma, deliberately excluded from this contract.

**Elevation history:** run 1 (2026-07-02) ABORTED [STUCK] at 19/37 validated — the then-compound
contract (inequality + "hence" clauses + closure meta-commentary) forced the prover to build commentary
subtrees cross-depending on the pending core; classification: 6× DAG/cross-sibling dep, 1× missing
bridge fact, and one flagged possible gap in a delta=0 branch (def-visible-set degeneracy at tau=0).
Contract narrowed to the bare inequality with `0 < delta` (the delta=0 case belongs to the
Hognas-Mukherjea anchor, not here); re-seeded fresh.
