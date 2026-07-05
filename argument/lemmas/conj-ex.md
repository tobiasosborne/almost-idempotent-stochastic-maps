---
id: conj-ex
kind: open-problem
contract: (CONJECTURE) (EX) working form: every rank->=3 exact signed idempotent P with delta<=1/4 admits a theta-1/2 actual-row chart U0 with Vol(U0)>=(1/2)Vol_max(P) and max_s Phi_s(U0) <= C0 delta(P) (empirically C0=1). Composes with lem-factorization (S*_s <= 2 Phi_s + 6 delta) to C_sf = 2 C0 + 6 (=8 at C0=1); the edge from (EX) to conj-kernel/HLC is OPEN — no proved implication in either direction (DC4 audit, 2026-07-05).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: conjecture
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/conj-ex
---

**A conjectural strengthening / alternative ATTACK ROUTE toward [[conj-kernel]]** (rank>=3), NOT an
equivalent form (user decision 2026-07-05, adopting the DC4 redraw). It has a rigorous
factorization link ([[lem-factorization]]) but **no proved edge to the geometric Kernel input in
either direction** — both implications are genuine gaps, with three named mismatches
(chart-vs-vertex quantifiers; `P_vj` vs `P_{u_s j}` weights; maximal-pivot drift):
`docs/waves/2026-07-05-DC4-equiv-assembly-audit.md`. (EX)-side results feed `op-classical` only
once an `EX => Kernel/HLC` edge is proved. `C0<1` is REFUTED (`FINDINGS.md`); finer vocabulary
(def-actual-row-chart, def-phi-excess) deferred until this arm is worked.
