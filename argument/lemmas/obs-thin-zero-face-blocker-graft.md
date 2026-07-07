---
id: obs-thin-zero-face-blocker-graft
kind: obstruction
contract: Thin zero-face blocker graft: the explicit coordinate-row signed idempotent with rows u = e1, z = (1 + eps*(1-t), 0, t*eps, -eps), o = e3, a = e4 (any eps in (0,1/4], t in (0,1)) is an exact signed idempotent with delta = eps, t*(u) = t, whole-face h(z) = 0, and z a nonclone separator blocker (psi(p_z) < 0 for the standard separator) whose kappa-high positive mass in the hidden fixture t < kappa is exactly m_kappa(z) = t*eps — arbitrarily below the 4*tau bridge threshold.
defs: def-signed-idempotent; def-negative-mass; def-exposed
deps: lem-separator-zero-face-obstruction; lem-affine-exposer-row-capacity
status: proved
af: none
provenance: W49 wave (docs/waves/2026-07-07-W49-face-deciders.md): fresh-codex prover (worker BD) + SEPARATE fresh-codex hostile verifier (VBD, VALID-WITH-CORRECTIONS — exact recomputation at eps = t = 1/100: P^2 = P, delta = 1/100, t* = 1/100, whole-face h(z) = 0, psi(z) = -101/10000, m_kappa(z) = 1/10000 vs 4*tau = 2/5; corrections adopted: the general graft preserves idempotence only when appending a NEW STATE with zero old-row column (old rows embed as [P_i, 0]); the m_kappa = t*eps value is fixture-specific, not claimed for arbitrary grafts)
owner: A
---

**Role (the death certificate for ledger-only (F2) proofs).** A universal zero-face blocker
can carry arbitrarily little kappa-high mass — so no proof of
[[conj-downhill-zero-face-lower-mass]] can proceed from the separator/harmonicity ledger
alone; tallness/heaviness must EXCLUDE or SELECT AWAY thin near-clone blockers (the
tightness-promotion wall, FINDINGS 2026-07-07). The gadget instance is OUT of the tall-heavy
class; whether it can be realized in-class is the open refutation path (BE: never realized).

**Rigour tier.** Exact finite certificate + verified graft convention (L5).
