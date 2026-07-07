---
id: lem-signed-carre-du-champ
kind: lemma
contract: Signed carre du champ: for an exact signed idempotent P and any vector g with P g = g, the field Gamma_i = sum_j P_ij*(g_j - g_i)^2 satisfies Gamma = P(g^2) - g^2 and P*Gamma = 0; with Omega = osc(g) and nu_i the row-i negative mass, -c(nu_i)*Omega^2 <= Gamma_i <= ((1 + nu_i)/4)*Omega^2 with sharp c(nu) = nu/(1+nu) for nu <= 1 and c(nu) = (1+nu)/4 for nu >= 1; for every row v, sum_j max(P_vj,0)*(Gamma_j + delta*Omega^2) <= (delta*(1 + nu_v) + nu_v*(1 + delta)/4)*Omega^2; for every probability row vector mu, lambda = mu*P satisfies lambda*P = lambda, sum_i lambda_i = 1, negative-part mass <= delta, sum_i lambda_i*Gamma_i = 0, and sum_i max(lambda_i,0)*Gamma_i <= delta*(1 + delta)*Omega^2/4; and P annihilates P(g^k) - g^k for every k >= 1.
defs: def-signed-idempotent; def-negative-mass
deps: lem-harmonic-affine-bridge
status: proved
af: none
provenance: W48 wave (docs/waves/2026-07-07-W48-mechanism-bricks.md; ideation candidate 1, re-derived independently): fresh-codex prover (worker AZ — dead-route differentiation stated: exact linear identity on the quadratic field, every harmonic g, no canonical selector, no Jensen/energy step) + SEPARATE fresh-codex joint hostile verifier (VBW, VALID — sharp constants confirmed incl. the nu >= 1 branch and sharpness examples; exact fixtures 2x2 / ex-hume / W29 frontier recomputed)
owner: A
---

**Role (the tau^2-native budget).** The ONLY banked channel operating at the squared scale:
positive row mass cannot sit on rows with large Gamma, and ONE fixed vector lambda = mu*P
budgets the row-variance of EVERY harmonic observable simultaneously (cluster-uniform, the
W42 demand). Feeds the (F2) level-splitting decider and the [[conj-zero-face-elimination]]
mechanism hunt. NOT the canonical-g energy method, NOT Jensen (differentiation in provenance).
