---
id: lem-negpart-subadditive
kind: lemma
contract: Negative-part subadditivity: for all vectors x and y in R^d, writing n(w) = sum_l max(-w(l), 0), one has n(x + y) <= n(x) + n(y).
defs: 
deps: 
status: proved
af: validated
provenance: docs/waves/2026-07-03-A11-drestricted-fan.md (arm A wave 11, codex; the barycenter-subadditivity step of the DRF proof — pointwise max(-(x(l)+y(l)), 0) <= max(-x(l), 0) + max(-y(l), 0), summed over l); pre-factored before elevation per the lem-fan-payment balloon lesson (aism-ugk)
owner: A
workspace: proofs/lem-negpart-subadditive
---

Pre-factored dependency of [[lem-fan-payment-restricted]] (the D-restricted fan payment, sharp
constant `2+sqrt(2)`): the DRF proof's barycenter step `D >= n(sum_{i in A} p_i w_i)` uses exactly
this pointwise subadditivity (with nonnegative homogeneity, which is definitional). **af-VALIDATED IN-REPO 2026-07-03** (run 1 clean): 16-node tree, root `validated`, taint 16/16
clean. Export: `proofs/lem-negpart-subadditive/export.md`. Status flip is the mechanical
reflection of the codex ledger.
