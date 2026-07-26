---
id: lem-kitaev-almost-idemp-audit
kind: lemma
contract: Corrected th_almost_idemp audit: let H be nonzero and let Phi:B(H)->B(H) be UCP with ||Phi^2-Phi||_cb <= eta < 1/4; for tilde-Phi=(1/2)(I+(2Phi-I)(I-4(Phi-Phi^2))^(-1/2)), A=Im(tilde-Phi), and X star Y=tilde-Phi(XY), one has tilde-Phi^2=tilde-Phi, both amplified associativity identities Phi_assoc1 and Phi_assoc2 have error at most 10*eta*||X||||Y||||Z|| after the local source type/index corrections, and for sufficiently small universal eta the inherited operator-space norms, involution, and unit make A an extended epsilon_AI(eta)-C*-algebra with epsilon_AI=max{r,20eta+2(M^5-1),3r-r^2}=O(eta), r=(3/2)((1-4eta)^(-1/2)-1), M=1+r, dimension-free at every amplification.
defs: def-extended-epsilon-cstar-algebra
deps:
status: proved
af: validated
provenance: docs/plans/2026-07-23-W74F-artifacts/AUDIT-W74F-D-ALMOSTIDEMP.md Executive verdict, Explicit estimate engine, Interface, and Hostile bottom line; hostile batch verdict VERDICT-W74F-BATCH.md §D (VALID, no correction)
owner: B
workspace: proofs/lem-kitaev-almost-idemp-audit
---

**Status.** Hostile-verified corrected audit, hence `proved-mod-audit`;
not `cited`, not `af`-validated, and not L0-rigorous.

**Transcribed core.** At every amplification, write \(T=\Phi\) and
\(D=T^2-T\), so \(\lVert T\rVert\le1\) and
\(\lVert D\rVert\le\eta\).  The corrected diagram ledger gives:
\[
\lVert S_X\rVert\le\sqrt{3\eta}\lVert X\rVert,\qquad
\lVert W\rVert\le3\eta\lVert X\rVert\lVert Y\rVert\lVert Z\rVert,
\]
and a \(7\eta\) reduction remainder, hence \(10\eta\) for each
associativity identity.  The second identity follows from the first by
adjoints with \((Z^\dagger,Y^\dagger,X^\dagger)\).

**Local source fixes.** The operator variables at source lines 2603,
2608, 2620, and 2624 belong to the relevant operator algebras, not the
Hilbert spaces, and the final isometry at line 2665 is \(V_{1+k}\), not
\(V_1\).

**Honest scope.** The registered statement includes the explicit
extended interface verified by the hostile batch.  It makes no claim
about `th_main_ext`; the canonical Stinespring construction remains a
source dependency, and optimality of the displayed constants is not
claimed.
