---
id: lem-weighted-min
kind: lemma
contract: Weighted minimum bound: let p_1, ..., p_m be positive reals with sum_i p_i = 1 and let n_1, ..., n_m be real numbers; then min over i in {1, ..., m} of n_i <= sum_i p_i * n_i.
defs: 
deps: 
status: proved
af: validated
provenance: docs/waves/2026-07-03-A10-weighted-payment.md (arm A wave 10, codex; the support-averaging step of the fan payment proof: if every n_i exceeded the weighted average the average would exceed itself); factored out of proofs/lem-fan-payment after the run-1/run-2 balloon aborts (aism-ugk)
owner: A
workspace: proofs/lem-weighted-min
---

Second factored dependency of [[lem-fan-payment]]: the index-selection step (some support point has
value at most the weighted average). Textbook-adjacent but registered as a shard so the af tree can
import it as a validated external instead of re-deriving it across siblings (the run-1/run-2
cross-sibling churn). **af-VALIDATED IN-REPO 2026-07-03** (8-node tree, root `validated`, taint 8/8 clean; the build run's verifier calls were blanked by a network outage and the verify phase was resumed cleanly). Export: `proofs/lem-weighted-min/export.md`. Status flip is the mechanical reflection of the codex ledger.
