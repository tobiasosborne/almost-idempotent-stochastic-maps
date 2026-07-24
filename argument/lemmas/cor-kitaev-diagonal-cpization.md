---
id: cor-kitaev-diagonal-cpization
kind: corollary
contract: Entrywise CP-ization from the repaired diagonal: for the finite phase-balanced diagonal D=sum_t q_t W_t^dagger tensor W_t supplied by lem-kitaev-diagonal-repair, every involution-preserving linear map tilde-Delta:B->B(H) and every UCP map Phi define a completely positive map Delta'(X)=sum_t q_t Phi(tilde-Delta(X W_t^dagger) tilde-Delta(W_t)); complete positivity uses exact centrality of D and does not require exact multiplicativity of tilde-Delta.
defs: def-fd-cstar-diagonal
deps: lem-kitaev-diagonal-repair
status: proved-mod-audit
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-B-DIAGONAL.md §4.1; hostile batch verdict VERDICT-W74F-BATCH.md §B (VALID, no correction); report cor:kitaev-diagonal-cpization
owner: B
workspace: proofs/cor-kitaev-diagonal-cpization
---

**Status.** Hostile-verified corollary, hence `proved-mod-audit`; not
`af`-validated and not L0-rigorous.

**Transcribed entrywise identity.** Exact centrality moves the
whole-algebra unitary from the right of \(Y_{bc}\) to the left.  With
\[
Z_t=\widetilde\Delta_n((I_n\otimes W_t)Y),
\]
the artifact obtains, at every matrix level,
\[
\Delta'_n(Y^\dagger Y)
=\sum_tq_t\,\Phi_n(Z_t^\dagger Z_t)\ge0.
\]
Only linearity and preservation of the involution are used from
\(\widetilde\Delta\); no exact multiplicativity and no projection onto a
CP cone is used.

**Scope.** The diagonal belongs to the exact finite-dimensional algebra
\(\mathcal B\), never to the approximate algebra.  This local corollary
does not close the separate amplified structure-theorem gaps.
