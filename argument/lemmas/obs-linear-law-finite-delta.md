---
id: obs-linear-law-finite-delta
kind: obstruction
contract: Certified finite-delta exceedance of the empirical linear law: the exact 5x5 signed idempotent with delta = 49/2000 (runs/2026-07-02-web-regime-hunt, verify_instance.py; generator build_from_LambdaC with p=1/40, x=p/3, rho=1/100) has visible set W = {0,1,2}, hidden rows {3,4}, and height H = 1/20 certified by a matching primal/dual pair, so H/delta = 100/49 > 2; mechanism = hull-dip (visible archetypes carry their own negativity, receding conv W); scaling gives H/delta -> 2 and H/tau -> 0, so the exceedance is an O(delta) finite-size term — the asymptotic linear-law constant stays 2 and the kernel conjecture is untouched.
defs: def-signed-idempotent; def-height; def-visible-set; def-negative-mass
deps: 
status: numerical
af: none
provenance: runs/2026-07-02-web-regime-hunt/ (exact-arithmetic certificate; P^2=P over Q, primal 7/15,8/15 and dual phi with ||a||_inf=1, phi|_W in {0,0,-2}, phi(p_3)=1/20; independently recomputed by the orchestrator with fresh Fractions code 2026-07-02)
owner: A
workspace: proofs/obs-linear-law-finite-delta
---

**Arm F wave-1 certified observation (L3 — numerical, NEVER rigorous).** Corrects the record's headline
"`delta >= H/2` with zero exceptions": that held within the inherited generators (which keep visible rows
nonnegative, as at delta = 0); giving the visible archetypes their own negativity budget dips the hull and
buys `H/delta > 2` at finite delta. Search maximum observed `H/delta ~= 2.055`. Do NOT quote the linear
law with constant exactly 2 at finite delta; the global finite-delta constant is > 2 (at least 100/49).
Kernel-safe: the dangerous scaling (H/tau bounded below) is NOT produced (H/tau = 0.319 here, -> 0 in the
family). See FINDINGS 2026-07-02 correction and the bundle README for scope limits.
