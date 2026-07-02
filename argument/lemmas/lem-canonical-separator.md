---
id: lem-canonical-separator
kind: lemma
contract: For a signed affine retraction P with hidden top vertex v of height H there exists a canonical separator: a 1-Lipschitz (ell^1) affine phi with phi <= 0 on C_W, sup_{C_W} phi = 0, phi(p_v) = H (existence by ell^1/ell^inf duality); the deficit g_i := H - phi(p_i) satisfies g >= 0, g_v = 0, g = Pg (harmonicity: phi affine and rows reproduce, p_i = sum_j P_ij p_j), and Omega := max_i g_i - min_i g_i <= 2 + 4*delta.
defs: def-signed-idempotent; def-height; def-visible-set; def-negative-mass
deps: 
status: proved-mod-audit
af: none
provenance: docs/ingest/report/kernel-conjecture.tex:225-232 (canonical separator, deficit harmonicity, Omega bound; transcribed verbatim-faithful 2026-07-02)
owner: A
workspace: proofs/lem-canonical-separator
---

The canonical separator + harmonic deficit machinery from the inherited kernel-conjecture attack
(`docs/ingest/report/kernel-conjecture.tex:225-232`). Imported into the registry as the input of
[[obs-deep-leakage]] (arm B wave 1). Inherited paper-proof — NOT independently audited here.
