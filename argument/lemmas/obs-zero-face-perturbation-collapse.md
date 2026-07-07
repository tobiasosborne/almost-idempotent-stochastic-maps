---
id: obs-zero-face-perturbation-collapse
kind: obstruction
contract: Zero-face perturbation collapse: in the setting of lem-separator-zero-face-obstruction, every produced blocker z (h*(p_z) = 0, psi(p_z) < 0) makes h* + s*psi infeasible for the exposedness LP for EVERY s > 0; realized exactly by the 4x4 exact signed idempotent with rows (1,0,0,0), (10099/10000, 0, 1/10000, -1/100), (0,0,1,0), (0,0,0,1) at u = 0 (0-based; t*(0) = 1/100, always-tight T = {3}, O = {2}, blocker z = 1 with psi(p_1) = -1/100).
defs: def-signed-idempotent; def-exposed
deps: lem-separator-zero-face-obstruction
status: proved
af: none
provenance: W47 wave (docs/waves/2026-07-07-W47-mechanism.md): fresh-codex prover (worker AY) + SEPARATE fresh-codex hostile verifier (VAY, VALID — full exact recomputation: P^2 = P, delta = 1/100, t*(0) = 1/100 via the row-1 constraint h_2 >= 100*h_3, h* = (0,0,1,1/100) P-fixed, psi = (0,-1/100,-1,99/100) a valid separator direction at m = 0, and (h* + s*psi)(p_1) = -s/100 < 0 for every s > 0; also the honest note P^+_{1,3} = 0 while P^+_{1,2} = 1/10000 — the eta = t* slab contains row 2)
owner: A
---

**Role (a dead sub-route, certified).** The naive repair of a failed intersection — slide
the optimal exposer along the separator direction — is impossible: the blocker kills every
positive step exactly. Any (T2) mechanism must CHARGE the blocker (as in
[[lem-blocker-capacity-bridge]]), not perturb past it. Recorded as an obstruction so the
sliding family is never re-walked.

**Rigour tier.** Exact finite certificate + general one-line argument, hostile-reviewed (L5).
