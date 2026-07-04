---
id: obs-orphan-amplifier
kind: obstruction
contract: Orphan amplifier: for every 0 < h < 1/6, with p = 1/2 + h, e = 1/2 - h, q = 1 - 2h, there is a rank-3 exact signed idempotent P(h) (square real matrix with P(h)^2 = P(h) and all row sums equal to 1) with delta(P(h)) = e*(1/4+h)/p < 1/4, chart rows c0 = (1,0,0), c1 = (0,1,0), c2 = (0,0,1), non-chart rows o0 = (p,-e,q), o1 = (-e,p,q), base chart U = (c0,c1,c2) the unique theta-half Phi-argmin where coordinates a_t(i) are defined by p_i = sum_t a_t(i)p_{c_t}, beta_2(i) = P(h)_{c2,i}, lambda_2(i) = 1 - a_2(i), mu_2(i) = sum_{t != 2} max(-a_t(i),0), E_2(i) = max(mu_2(i)-lambda_2(i),0), Phi_2(U) = sum_i max(beta_2(i),0)E_2(i), beta_2(o0) = beta_2(o1) = 1/4, o0 and o1 active strict-legal orphans, OD(h) = L_mu^orph + F_L^orph + sum_{j in {o0,o1}} beta_2(j)E_2(j) = 1/2 - 2h, G_class^-(h) = h, S_-^mu(h) = 0, R_D^nu(h) = 0, nu_j = sum_l max(-P(h)_{jl},0), SIGMA(h) = sum_{j in {o0,o1}} beta_2(j)nu_j = delta(P(h))/2, and Phi_2(U) = 1/4 - 3h/2, such that OD(h)/(G_class^-(h)+S_-^mu(h)+R_D^nu(h)) = 1/(2h)-2 tends to infinity while OD(h)/(G_class^-(h)+S_-^mu(h)+SIGMA(h)) tends to exactly 4 and Phi_2(U)/delta(P(h)) tends to 1.
defs: def-signed-idempotent; def-negative-mass
deps: 
status: proved-mod-audit
af: none
provenance: docs/waves/2026-07-03-G5-orphan-financing-lemma.md §T0/T1 "Exact Amplifying Family" eqs. (6)-(10), §T0 "Theta-Half Argmin Enumeration", and §T1 "Orphan Classification And OD"; docs/waves/2026-07-03-G6-repaired-horn.md §T0 "Repaired-Horn Replay" eq. (5)
owner: A
workspace: proofs/obs-orphan-amplifier
---

**Exact family.** G5 takes `p=1/2+h`, `e=1/2-h`, `q=1-2h`, rows `(c0,c1,c2,o0,o1)`, and pivot row data `beta_2(o0)=beta_2(o1)=1/4`.

The left inverse rows are:
```text
B0 = [1 - p/4 - e^2/(4p), e/2, -h*q/(2p), 1/4, -e/(4p)]
B1 = [e/2, 1 - p/4 - e^2/(4p), -h*q/(2p), -e/(4p), 1/4]
B2 = [-h/2, -h/2, p, 1/4, 1/4]
```

G5 checks `B L = I_3`, `P=L B`, `P^2=P`, and `P1=1` exactly. The projection rows simplify to the displayed G5 rows, with `delta(P)=e*(1/4+h)/p` and `1/4-delta(P)=h^2/p`.

**Certification.** The theta-half charts are enumerated exactly in G5; `(c0,c1,c2)` is the unique theta-half `Phi`-argmin and `s=c2` is the unique maximal pivot.

**Not an EX refuter.** On the same family,
```text
Phi_s(U)/delta(P) = (1/4 - 3h/2)/(1/4 - h^2/p) -> 1.
```
So the plateau-2 evidence is intact.

**Killed route.** This refutes every finite class/signed-only post-fan orphan budget of the form `G_class^- + S_-^mu + R_D^nu`. The repaired [[conj-rh]] must include own row-negative mass, and the coefficient floor is `4`.
