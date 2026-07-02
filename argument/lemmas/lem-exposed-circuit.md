---
id: lem-exposed-circuit
kind: lemma
contract: For a signed affine retraction with neg mass <= delta: (i) a (rho,kappa)-exposed row vertex v concentrates, ||v-pi_v||_1 <= C(delta/kappa+delta) for a probability pi_v supported on U_v={j:||p_j-v||_1<rho}; (ii) for pairwise-separated (rho,kappa)-exposed vertices v_a, ||sum c_a v_a||_1 >= (1-C(delta/kappa+delta)) sum|c_a|; both RHS are 1-O(sqrt delta) when kappa >= c sqrt(delta).
defs: def-exposed
deps: lem-leakage
status: proved-mod-audit
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/lem-exposed-circuit
---

Exposed-vertex concentration + circuit cancellation. Feeds [[thm-well-exposed]] and [[thm-cluster]].
