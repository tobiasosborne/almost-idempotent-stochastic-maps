---
id: lem-thmainext-conditional
kind: lemma
contract: Conditional th_main_ext assembly: assuming conj-hcb (H-CB) and conj-extcb (EXT-CB), every finite-dimensional extended epsilon-C*-algebra A is carried by one map v from a finite-dimensional C*-algebra B at full amplified O(epsilon) strength with a universal constant; the assembly includes the corrected estimate |<X,X>_n-||X||_{n,1}^2| <= C(delta+epsilon)||X||_{n,1}^2 and, with the verified diagonal CP-ization and th_almost_idemp interface, yields the conditional universal K=max{K_DeltaUpsilon,K_mult,K_UpsilonDelta,1} and a positive threshold eta_K given by the finite minimum ledger of DECOMP-W74F-C-THMAINEXT.md §5.
defs: def-extended-epsilon-cstar-algebra; def-fd-cstar-diagonal
deps: conj-hcb; conj-extcb; cor-kitaev-diagonal-cpization; lem-kitaev-almost-idemp-audit
status: proved-mod-audit
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md §§3-5; hostile batch verdict VERDICT-W74F-BATCH.md §C and Cross-target checks (VALID, no correction); report lem:thmainext-conditional
owner: A
workspace: proofs/lem-thmainext-conditional
---

**Status.** Hostile-verified conditional paper proof, hence
`proved-mod-audit`; the two conjecture premises are named in both the
contract and `deps`.  It is not `af`-validated and does not prove either
premise.

**MAIN-CB assembly.** The transcribed invariant is that every extension,
binary merge, and error-reduction step produces one level-one map whose
amplifications share the same estimate.  Error reduction resets the
error after each raw step, so neither block count nor block dimension is
accumulated.

**Squared correction.** The printed unsquared display at
`approximate_algebras.tex:1551-1555` is replaced by
\[
\left|\langle X,X\rangle_n-\lVert X\rVert_{n,1}^2\right|
\le C(\delta+\varepsilon)\lVert X\rVert_{n,1}^2.
\]
The W74F-C artifact derives this by treating \(X\) as one rectangular
operator-space element, with no entrywise \(n\)-sum.

**Conditional ledger.** Once H-CB and EXT-CB provide universal constants
and positive thresholds, all remaining coefficients form finite
sum/product expressions.  Their maximum defines \(K\), and the minimum
of the functional-calculus, H-CB, EXT-CB, Neumann, normalization, and
raw-step thresholds defines \(\eta_K>0\).  Without the two conjectures
this ledger is conditional only.
