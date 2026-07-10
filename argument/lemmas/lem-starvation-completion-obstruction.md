---
id: lem-starvation-completion-obstruction
kind: lemma
contract: Bounded-slab starvation completion obstruction (K-free): for every finite I, every real A in [4,6], every real tau in (0,1/256], and t := tau^2, a := tau/(1+tau), there is no rank-three exact signed idempotent P (P^2 = P, P*1 = 1, rank P = 3) with row negative mass nu_i <= t for every i in I having five distinct full row-point fibers represented by v,w,f,z,o such that, with D := p_z - p_v and E := p_o - p_v linearly independent, ||D||_1 = tau, p_f - p_v = -A*D + t*E, p_w - p_v = a*(p_f - p_v), top-row fiber masses c_v = 1 - tau, c_w = tau + t, c_f = -t, and c_Q = 0 for every other full row-point fiber Q, every full row-point fiber Q has unique reals x_Q, y_Q with p_Q = p_v + x_Q*D + y_Q*E, and every nonactor support fiber Q satisfies either p_Q in conv{p_v,p_w,p_f,p_z,p_o} or 0 <= y_Q <= 1.
defs: def-signed-idempotent; def-negative-mass
deps: 
status: proved
af: validated
workspace: proofs/lem-starvation-completion-obstruction
provenance: W59 wave (runs/2026-07-10-w58-starvation-completion-extra-vertex/PAPER-PROOF-w59.md): codex prover (gpt-5.6-sol ultra) paper proof from first principles, guided by (but independent of) the W57/W58 exact Farkas certificates; fresh hostile codex verifier verdict first line verbatim 'VERDICT: VALID-WITH-CORRECTIONS — the K-free obstruction is proved; only an index-level coordinate abbreviation is missing.' (single notation correction applied). Reviewer != author.
owner: B
---

**Role (the first proved mechanism on the H-X / large-gauge completion front).** The
W55 starvation gadget (A0 in [4,6], g = A0*tau display) admits NO rank-three
completion with any finite number of exterior zero-top support fibers confined to the
canonical slab 0 <= y <= 1 — the K-FREE strengthening of the W57/W58 certificate
family. Exceeds its L3 ancestry (runs/2026-07-10-w57-* and -w58-*): those bundles
decided finitely many support patterns; this excludes them all uniformly.

**Mechanism (one line).** Exact idempotence at the pinned display demands one unit of
transverse moment (sum_j x_j*D_j = 1), while the actor hull and the aggregated
exterior sign-union row budgets can supply only O(tau) — contradiction below the
universal ceiling tau <= 1/256.

**Consumption.** The candidate closing shape for [[conj-sl1a-off-diagonal-cell]] and
the L6.5 large-gauge wall ([[conj-cotop-web-coupling]]): what must generalize is the
slab confinement hypothesis (0 <= y_Q <= 1) and rank three -> the H-X hypothesis
class. See §HONEST LIMITS of the proof text.

**Rigour tier.** L5 (reviewer != author: fresh hostile codex). NOT af-validated.
Prime af-elevation candidate (single minimal contract).
