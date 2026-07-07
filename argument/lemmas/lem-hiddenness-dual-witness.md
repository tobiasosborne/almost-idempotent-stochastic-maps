---
id: lem-hiddenness-dual-witness
kind: lemma
contract: Hiddenness dual witness: for an exact signed idempotent P and a hidden row vertex v (rho = 4*tau, kappa = tau/4, tau = sqrt(delta(P))), writing F_v = {j : ||p_j - p_v||_1 >= rho} for the rho-far row-index set (nonempty for hidden v), there exist lambda_f >= 0 (f in F_v) with sum_f lambda_f = 1 and alpha_i, beta_i >= 0 (over all row indices i) with sum_i beta_i = t*(v) < kappa, such that sum_f lambda_f*(p_f - p_v) + sum_i alpha_i*(p_i - p_v) = sum_i beta_i*(p_i - p_v).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: 
status: proved
af: validated
provenance: W26 wave (docs/waves/2026-07-06-W26-hiddenness-consumption.md): fresh-codex prover (worker P) + SEPARATE fresh-codex hostile verifier (VP, VALID-WITH-CORRECTIONS — re-derived the dual from scratch incl. feasibility/boundedness/attainment/strong duality and the hidden => F_v nonempty step, exact fixture on the banked W19 7x7 duplicate-split matrix, t*(v) = 1/21 < 1/16 with the witness recomputed exactly); first-principles finite LP duality, no imports
owner: A
workspace: proofs/lem-hiddenness-dual-witness
---

**Role (the W25-mandated input, made positive).** W25 proved any step-4 attack MUST consume
hiddenness (t*(v) < kappa); this shard converts that universally-quantified failure statement
("every admissible exposer fails the kappa-margin at some rho-far row") into an EXISTENTIAL
geometric object: a convex combination of rho-far rows that reproduces p_v up to controlled
signed slack. This ties a hidden vertex to its far rows — the coupling the bare scalar fact-list
lacked. Consumed by [[lem-top-slab-companion]]; the frontier [[conj-min-a-w4]] attack (W29)
consumes it at every deep carrier.

**Proof shape (worker P, T1; VP re-derivation).** The exposedness program t*(v) = max t over
affine h with h(p_v) = 0, 0 <= h(p_i) <= 1 (all rows), t <= h(p_f) (f in F_v) is a finite LP in
(u, t) after writing h(x) = u.(x - p_v). Hidden v: the shard convention t* = +infty for empty
F_v forces F_v nonempty, whence t <= 1 and the LP is bounded; feasibility at (0,0); strong
duality + attainment give the witness with sum beta = t*(v) < kappa. The balance equation is the
dual stationarity in u; lambda-normalization is stationarity in t.

**Pairing consequence (body, VP-corrected).** For any affine psi with psi(p_v) = 0 and
0 <= psi(p_i) <= E on all rows with E > 0: applying the linear part of psi to the balance and
dropping the (nonnegative) alpha-term gives sum_f lambda_f psi(p_f) <= t*(v)*E < kappa*E; in
particular SOME rho-far row has psi(p_f) < kappa*E. At E = 0 only the non-strict form survives
(VP's correction; psi = 0 witnesses sharpness of the caveat).

**Honest limits.** (i) The alpha family is NOT removable for free: worker Q's stronger gauge
form (far barycenter within kappa*(2+4*delta) of p_v, alpha-free) matched exact fixtures but was
not independently verified — reconcile before use (FINDINGS 2026-07-06 W26). (ii) The witness is
geometric; nothing here couples it to row-v's own coefficients P_vj^+ (that coupling is exactly
the open content of [[conj-min-a-w4]]).

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous; af-elevation candidate
(deps: none, single-minimal contract).
