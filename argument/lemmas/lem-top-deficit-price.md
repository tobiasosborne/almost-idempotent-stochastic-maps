---
id: lem-top-deficit-price
kind: lemma
contract: Top-deficit price: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set W(P), a hidden top vertex v of height H, there exists a top support functional phi (affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1), and for ANY such phi, writing a_j = P_vj and z_j = H - phi(p_j) >= 0: for every subset A of row indices, sum over j in A of max(a_j,0)*z_j <= nu_v*(2+4*delta) <= delta*(2+4*delta); consequently for m >= 0, L >= 0, if sum over A of max(a_j,0) >= m and z_j >= L on A then m*L <= delta*(2+4*delta), and for delta <= 1/4, lambda > 0, theta < 1, positive v-row mass >= 1-theta on rows with z_j >= lambda*H forces H <= 3*delta/(lambda*(1-theta)), hence H <= 4*tau whenever delta <= min(1/4, (4*lambda*(1-theta)/3)^2).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: proved
af: none
provenance: W53 wave (docs/waves/2026-07-09-W53-binding-constraint-lemmaization.md): codex prover B1 (Lemma 1) + fresh hostile codex verifier VB1 (VALID-WITH-CORRECTIONS; corrections applied — the m,L >= 0 sign hypotheses, lambda > 0, theta < 1 made explicit)
owner: A
---

**Statement mechanics.** Existence of phi is l1/l-infinity duality at a closest point of
C_W (VB1-checked first-principles); phi(p_j) <= d_j <= H for every row (v is a height
maximizer), so z_j >= 0; z_j <= 2+4*delta by the [[def-signed-idempotent]] row geometry.
Row reproduction p_v = sum_j a_j p_j (P^2 = P) and sum_j a_j = 1 (P1 = 1) give
0 = z(p_v) = sum_j a_j z_j, so sum a_j^+ z_j = sum a_j^- z_j <= nu_v*(2+4*delta).
Dimension-free; clone-invariant (an index-sum identity — clones split summands).

**Role (the (i) huddle-charge handle).** Converts ANY Omega(H) lower bound on the top
row's positive-mass total top-deficit Z_v(phi) into the linear law delta >= c*H, hence
tall-emptiness: see [[conj-top-deficit-coupling]]. The blind spot is exact and structural:
rows in the rho-ball of v have z_j < 4*tau, so a huddle carrying all positive mass in the
low top-deficit slab evades the pairing — the pairing bites only on mass with definite
top-deficit (FINDINGS 2026-07-09 W53).

**Rigour tier.** L5 (reviewer != author: fresh hostile codex VB1). NOT af-validated.
