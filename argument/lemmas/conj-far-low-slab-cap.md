---
id: conj-far-low-slab-cap
kind: lemma
contract: (CONJECTURE) Far very-low-slab coefficient cap: there exist universal a_0 >= 4, theta_0 in (0,1), delta_0 > 0 such that every exact signed idempotent P with 0 < delta(P) <= min(delta_0, (theta_0/24)^2), nonempty visible set W(P), and height H > (4*(5*a_0/4 + 3/2)/theta_0)*tau has a hidden top vertex v and an optimal exposer h_v* at v with sum over {j : dist_1(p_j, conv{p_w : w in W}) > a_0*tau, ||p_j - p_v||_1 >= 4*tau, h_v*(p_j) < tau/8} of max(P_vj, 0) <= theta_0/4.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
af: none
provenance: W54 wave (E1 sub-wave): codex prover E1's GAP-1, V-E1-audited as fully quantified and exactly the missing piece of the absorption-to-low-slab bridge (lem-absorption-implies-low-slab-cap)
owner: A
---

**Role (the FAR sibling of the huddle charge).** [[lem-absorption-implies-low-slab-cap]]
proves: this + [[conj-near-cluster-absorption]] => [[conj-low-slab-cap]] (explicit
constants). The near deep slab is the huddle charge's territory; this caps the top's
positive coefficient mass on rho-FAR deep rows that the exposer barely sees
(h_v* < tau/8) — the band the pincer cannot reach (it controls h >= tau/8 at cost 8*tau).
The known wall it must dodge: no proved contract compares witness mass lambda with the
top row's coefficient measure P_v^+ (the anti-splitting/witness-coupling gap — E1 §4);
[[lem-top-witness-third-actor]] locates large lambda-mass exactly far-and-deep, so a
coefficient-coupled version of that statement would be the natural mechanism.

**Refuter target.** A tall instance with substantial P_v^+-mass on rho-far deep rows with
h_v* < tau/8 for EVERY optimal exposer at EVERY hidden top, while near-cluster absorption
holds. No such instance is realized (W52 evidence, L3).

**Status discipline.** A conjecture — promotes nothing; consumers carry it as a dep.
