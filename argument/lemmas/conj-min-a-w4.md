---
id: conj-min-a-w4
kind: lemma
contract: (CONJECTURE) MIN-A at width 4: for every exact signed idempotent P with 0 < delta(P) <= (17-12*sqrt(2))/2, nonempty visible set W(P), and height H > 13*tau (tau = sqrt(delta)), some hidden top vertex v has sigma_4(v) <= 1/2, where sigma_4(v) is the positive coefficient mass v places on rows at ell-1 distance > 4*tau from conv{p_w : w in W}.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass; def-height
deps: 
status: conjecture
af: none
provenance: W25 wave (docs/waves/2026-07-06-W25-step4-decider.md): the g-bootstrap's step 4 reduced to this single statement — prover M (worker-T1 partial) shows it contradicts lem-parametric-halo-collapse's forced mass in tall configs, closing H <= 13*tau; obstructor N (exact certificate, orchestrator-recomputed 17/17) proves the current fact-set CANNOT derive it — the mandatory missing input is HIDDENNESS (non-exposedness) of the deep vertices, never consumed by any banked lemma
owner: A
workspace: proofs/conj-min-a-w4
---

**Role (THE frontier statement — the g-bootstrap's one remaining open step, sharpened by W25).**
If this holds, then together with [[lem-parametric-halo-collapse]] (which forces `sigma_4 > 1/2` at
EVERY hidden top when `H > 13*tau`) it yields a contradiction: hence `H <= 13*tau` for every exact
signed idempotent with `delta <= (17-12*sqrt2)/2` — the height side of [[conj-kernel]] with B = 13
(assembly via the re-aimed aism-yxa; W-nonemptiness and the delta = 0 endpoint remain separate).

**What W25 established about it (both workers blind, convergent):**
- *Prover side (worker M, T1 partial, verifier pass pending at codification):* the once-applied
  maximum principle with an affine support functional proves the OPPOSITE-direction structure —
  in a tall configuration the top's positive mass concentrates on `G_4`
  (`sum_{j notin G_4} P_vj^+ < tau*(2+4delta)/9`) and the disintegration slack obeys
  `R_v < tau*(2+4delta)/9`, so `M_v^4 > 1/2 - delta - tau*(2+4delta)/9`. The equivalent working
  form of THIS conjecture given [[lem-genuine-disintegration]] is the cap `M_v^4 + R_v <= 1/2 -
  delta` — an UPPER bound the imported facts cannot supply.
- *Obstructor side (worker N, exact certificate, L3 bundle `runs/2026-07-06-w25-step4-decider/`):*
  the banked fact-set (harmonicity + collapse conclusion + Lemma-A conclusion + disintegration +
  generic row facts) is INSUFFICIENT — a 3x3 exact idempotent satisfies all of them under labels
  while its "hidden" top is actually (rho,kappa)-exposed. **Any proof of this conjecture MUST
  consume hiddenness quantitatively:** t*(v) < kappa, i.e. every admissible exposer of v fails the
  kappa-margin against some rho-far row. No banked lemma consumes that; this is the named missing
  geometric input.

**Relation to CAP-1/2.** This is the WIDTH-4, TALL-CONFIGURATION restriction of the old CAP-1/2
surface (which remains the refuter target at any height, record sigma_g = 5991/80000 at a = 1/4).
Strictly weaker than CAP-1/2-at-width-4-any-height; exactly what MIN-A needs.

**Attack guidance (sketch v6):** the two-observable argument (mass observable g + affine deficit
H - phi, both harmonic) + the exposer-failure witnesses of hiddenness; sub-target: re-establish
[[lem-canonical-separator]] (mod-audit) if the deficit machinery is used as more than
first-principles.
