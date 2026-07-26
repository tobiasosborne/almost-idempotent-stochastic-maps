---
id: lem-topology-orientable-top-cohomology
kind: lemma
contract: Top cohomology of a closed orientable manifold: if M is a connected compact orientable d-manifold without boundary, then H^d(M;R) != 0.
defs:
deps:
status: stated
af: none
provenance: hatcher-algebraic-topology AT.txt:14704-14711 (Theorem 3.26: H_n(M;Z)=Z for closed connected orientable) + AT.txt:12385-12394 (field-coefficient UCT) + AT.txt:15531-15534 (Cor 3.39: H^n(M;Z)=Z) — Thm 3.26 + UCT covers the row exactly, loci pinned 2026-07-26; DESIGN-FUDW-DECOMP-v4.1.md §2.3
owner: A
workspace: proofs/lem-topology-orientable-top-cohomology
---

**Status.** Local source-result transcription at `stated`; to be af-elevated
with the byte-matched externals. Not `cited`, not af-validated, not
L0-rigorous yet.

**Source loci (pinned).** Hatcher, *Algebraic Topology* (author's canonical
560pp PDF): Theorem 3.26 (txt:14704-14711) — for M a closed connected
n-manifold, R-orientable, H_n(M;R) ≅ R (in particular H_n(M;Z) = Z when
orientable); "closed" is defined as compact without boundary at
txt:14429-14430. Field-coefficient UCT printed at txt:12385-12394. Optionally
Corollary 3.39 (txt:15531-15534) for the integral top-cohomology form.

**Derivation to close at elevation (one step).** Real coefficients: by Thm
3.26 with R = ℝ, H_d(M;ℝ) ≅ ℝ; the field-form UCT gives
H^d(M;ℝ) ≅ Hom_ℝ(H_d(M;ℝ),ℝ) ≅ ℝ ≠ 0. Neither quoted result alone literally
states the real-coefficient claim (honest scope).

**Consumers.** `lem-stage1-extra-fixed-class` (per §3.3).
