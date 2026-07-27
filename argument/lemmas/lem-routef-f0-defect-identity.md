---
id: lem-routef-f0-defect-identity
kind: lemma
contract: Route F F0 defect identity: let n >= 1, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C) and J: C^n -> M_n the diagonal inclusion, let Q: l_inf^n -> l_inf^n be row-stochastic with canonical complex-linear extension Q_C: C^n -> C^n, and put Phi := J Q_C D; then ||Phi^2 - Phi||_cb = ||Q^2 - Q||_{infinity->infinity}.
defs: def-stochastic; def-almost-idempotent; def-ucp-map
deps:
status: proved-mod-audit
af: none
provenance: docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md Q4 (fresh hostile audit incl. the lower-bound direction, verdict VALID); design + fresh hostile audit docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md sect 1.2 + AUDIT-F0-ASSEMBLY.md sect 1.2 (VALID-WITH-CORRECTIONS; the Q_C typing correction is applied here; the audit re-verified BOTH directions of the equality); user-ratified landing 2026-07-27 (W79/W80, docs/plans/2026-07-27-W78-ratification-package.md sect 5 step 1)
owner: A
workspace: proofs/lem-routef-f0-defect-identity
---

**Status.** Local paper proof, hostile-audited twice — `proved-mod-audit`,
NOT rigorous. Elevation-ready: projected af budget 5 nodes / depth 3
($DJ=I$, squaring, cb upper bound, cb lower bound, root).

**Proof sketch (per the audited design; both directions).** Put
$L=Q_{\mathbb C}^2-Q_{\mathbb C}$. Since $DJ=I$, $\Phi^2-\Phi=JLD$. Upper:
at every matrix level, contractivity of $D_r$ and isometry of $J_r$ give
$\lVert(JLD)_r\rVert\le\lVert L_r\rVert$. Lower: on a norm-attaining
diagonal input $J_rX$, $\lVert(JLD)_rJ_rX\rVert=\lVert J_rL_rX\rVert
=\lVert L_rX\rVert$ because $D_rJ_r=I$. Finally
$\lVert L_r\rVert=\max_i\sum_j|l_{ij}|=\lVert L\rVert_{\infty\to\infty}$ by
the sign/phase test. Hence equality, with constant exactly $1$.

**Role.** Second F0 seam row: the stochastic defect $\eta$ with
$\lVert Q^2-Q\rVert_{\infty\to\infty}\le\eta$
([[def-almost-idempotent]]) transfers to the Kitaev input $\Phi$ with NO
$\eta\mapsto\varepsilon$ conversion at this seam (the AI conversion happens
inside the ledger, [[lem-routef-ai-defect-linearization]]). Companion:
[[lem-routef-f0-ucp-lift]]. Independent of the MAIN, polar, ledger fronts,
and of the UCP-lift proof.
