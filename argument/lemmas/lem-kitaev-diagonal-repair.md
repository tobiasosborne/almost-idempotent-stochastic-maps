---
id: lem-kitaev-diagonal-repair
kind: lemma
contract: Kitaev diagonal repair: the direct-sum diagonal formula printed at approximate_algebras.tex:1254 and :2780-2783 is false (already for B=C direct-sum C), but every finite-dimensional C*-algebra B=direct-sum_{r=1}^m M_{d_r} has a finite phase-balanced diagonal D=sum_t q_t W_t^dagger tensor W_t with unitary W_t, q_t >= 0, sum_t q_t=1, ZD=DZ for every Z in B, pi(D)=I_B, and projective norm ||D||_pi=sum_t q_t||W_t^dagger||||W_t||=1, independently of block count and block dimensions.
defs: def-fd-cstar-diagonal
deps:
status: proved-mod-audit
af: seeded
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-B-DIAGONAL.md §§2-3; hostile batch verdict VERDICT-W74F-BATCH.md §B (VALID, no correction)
owner: B
workspace: proofs/lem-kitaev-diagonal-repair
---

**Status.** Hostile-verified repair proof, hence `proved-mod-audit`; not
`cited`, not `af`-validated, and not L0-rigorous.

**Printed defect.** For
\(\mathcal B=\mathbb C\oplus\mathbb C\), the printed product construction
gives \(I_{\mathcal B}\otimes I_{\mathcal B}\).  It is normalized but not
central, so it is not a diagonal.

**Transcribed repair.** Choose a finite convex unitary representation
\[
D_r=\sum_{\alpha\in S_r}p_{r\alpha}
U_{r\alpha}^{\dagger}\otimes U_{r\alpha}
\]
of the Haar diagonal in each block.  For
\(\alpha=(\alpha_1,\ldots,\alpha_m)\) and
\(\sigma\in\{\pm1\}^m\), put
\[
W_{\alpha,\sigma}=\bigoplus_r\sigma_rU_{r\alpha_r},
\qquad
q_{\alpha,\sigma}=2^{-m}\prod_rp_{r\alpha_r}.
\]
The phase moment
\[
2^{-m}\sum_\sigma\sigma_r\sigma_s=\delta_{rs}
\]
deletes every cross-block tensor.  Thus the construction is an exact
diagonal of the exact algebra \(\mathcal B\), with convex coefficient
sum and projective norm exactly one.  The number of terms may grow with
the block data, but no downstream estimate counts terms.
