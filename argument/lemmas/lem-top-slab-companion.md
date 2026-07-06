---
id: lem-top-slab-companion
kind: lemma
contract: Top-slab companion: for an exact signed idempotent P with 0 < delta(P) <= (17 - 12*sqrt(2))/2, nonempty visible set W(P), and hidden top vertex v of height H > 13*tau (tau = sqrt(delta)), there is a row f with ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv{p_w : w in W}) > H - (1/2 + delta)*tau.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass; def-height
deps: lem-hiddenness-dual-witness
status: proved
af: none
provenance: W26 wave (docs/waves/2026-07-06-W26-hiddenness-consumption.md): fresh-codex prover (worker P, claim 2 of its PARTIAL) + SEPARATE fresh-codex hostile verifier (VP, VALID-WITH-CORRECTIONS — exact symbolic constant chain 13 - (1/2 + delta) >= 4 + 6*sqrt(2) > 4 at delta <= (17-12*sqrt2)/2)
owner: A
workspace: proofs/lem-top-slab-companion
---

**Role (tall hidden tops have deep, far company).** The first consequence of consuming
hiddenness: in the tall width-4 regime the hidden top v is accompanied by a rho-far row f whose
depth is within (1/2 + delta)*tau of the top height. Since 13 - (1/2 + delta) >= 4 + 6*sqrt(2) > 4
for delta <= (17-12*sqrt2)/2 [T0, VP-checked symbolically], f lies in
G_4 = {j : dist_1(p_j, conv W) > 4*tau} — the genuine set is provably NONEMPTY in every tall
configuration, with an inhabitant far from the top. (Contrast W20: no KNOWN construction enters
G_a for a >= 1; this shard shows tall configs, if any exist, are forced to.)

**Proof shape (worker P, T1; VP).** Take the ell1/ell-infty support functional phi at v
(phi(p_v) = H, phi <= 0 on C_W, 1-Lipschitz — first principles, as in
[[lem-top-concentration]]'s proof); set psi = H - phi, so psi(p_v) = 0 and 0 <= psi <= D = 2+4*delta
on all rows. The pairing consequence of [[lem-hiddenness-dual-witness]] (E = D > 0) yields a
rho-far row f with H - phi(p_f) < kappa*D = (1/2 + delta)*tau; phi(p_f) <= d_f gives
d_f > H - (1/2 + delta)*tau.

**Honest limits.** Existence of ONE far deep row; no mass statement, no bound on P_vf, no cap on
sigma_4 — the coupling of the witness to row coefficients remains exactly [[conj-min-a-w4]].

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
