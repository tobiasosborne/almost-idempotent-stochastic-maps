---
id: lem-ihorn-selected-corner-extraction
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, admits a nonempty family of public selected-corner certificates C = (phi, h, f, eta), each obtained from the lem-ihorn-cotop-sl1a-package measure lambda_A by choosing a top support functional phi at v, an admissible exposer h at v, the lem-sl1a-score-selector row point f in supp(lambda_A), an arbitrary legal row-point vertex kernel xi (probability weights on geometrically distinct row vertices, constant on clone fibers, Dirac at vertex points, with p_x = sum_u xi_x(u)*p_u), the lem-sl1a-corner-ledger coupled measure Gamma_f, the lem-radial-horn-partition block B with Gamma_f(B) >= 1/4, and eta = Gamma_f restricted to B with the kernel erased; every such certificate has eta(1) >= 1/4 and satisfies exactly one of: M_X(eta) > 1/8; or M_X(eta) <= 1/8 and M_I(eta) >= 1/16; or M_X(eta) <= 1/8, M_I(eta) < 1/16, and M_D(eta) > 1/16, where M_X, M_I, M_D restrict eta to the three def-selected-corner type predicates.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top
deps: lem-ihorn-cotop-sl1a-package; lem-sl1a-score-selector; lem-sl1a-corner-ledger; lem-radial-horn-partition
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node SC + Appendix A.6; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'SC: VALID' (universal-over-kernels ledger, radial block >= 1/4, and the exhaustive 1/4 - 1/8 - 1/16 = 1/16 type partition with all equality boundaries checked). Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 10/10 — selected-corner extraction; the structural
unification).** Routes the ultra-isotropic thin-rim core of the L5 minimax into
the SAME X/I/D selected-corner cell trichotomy as the SL1a fronts: the public
certificate (two affine profiles, one selected row, one coupled nonnegative
measure, three derived scalars) is constant-complexity and dimension-free.
Downstream, the creative leaves X / I-cap / D-cap of DECOMPOSITION-W63-I.md own
the three cells; the sign-cube plateau threat is isolated in the intersection
cell.

**Mechanism (one line).** [[lem-ihorn-cotop-sl1a-package]] implies the
[[lem-sl1a-score-selector]] hypotheses (its constants are stronger); any legal
vertex kernel feeds [[lem-sl1a-corner-ledger]] (\(\Gamma_f(C_f)>1/2\));
[[lem-radial-horn-partition]] gives a block of mass \(\ge1/4\); the three-way
type arithmetic \(1/4-1/8-1/16=1/16\) closes the trichotomy.

**Honest scope.** The kernel may be ARBITRARY — no favorable disintegration; the
certificate retains one coupled measure and its clone-invariant type masses, not
a dimension-free encoding of \(\xi\). A datum may admit certificates in
different cells; the W63 assembly fixes ANY one and follows its forced cell,
never choosing favorably. Radial equality belongs to the ledger block, M_X = 1/8
to the diagonal cells, M_I = 1/16 to the intersection cell.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
