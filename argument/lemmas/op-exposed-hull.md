---
id: op-exposed-hull
kind: open-problem
contract: (OPEN) Global exposed-hull lemma (pinned-delta form, adopted 2026-07-10 per W46/aism-nlg): there are universal delta_0,c,C>0 such that every exact signed affine retraction P with d = delta(P) <= delta_0 has every row within C*sqrt(d) of conv W_{C*sqrt(d), c*sqrt(d)}(P), where W_{rho,kappa}(P) = {vertices v : e_v(rho) >= kappa}.
defs: def-exposed; def-stochastic
deps: lem-hlc-implies-exposed-hull; op-hlc
status: open
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/op-exposed-hull
---

The intermediate open lemma; blocked on [[op-hlc]] (the classical-portfolio's reduction
op-exposed-hull <= HLC <= Kernel, now wired through the registered HLC node: [[op-hlc]] ⇐
[[lem-kernel-implies-hlc]] ⇐ [[conj-kernel]], W22 2026-07-06). Feeds
[[thm-classical-factorization]] (global form) -> [[op-classical]]. The <2>6 step (HLC ⇒ this)
was re-derived + hostile-verified at reviewed tier in W27 (2026-07-06, session 11):
[[lem-hlc-implies-exposed-hull]] establishes the PINNED-delta form (d = delta(P), W-nonemptiness
explicit, c = 1/4, C = max{4, C_1}). CAVEAT (W27 audit finding): this contract's literal
loose-delta reading (free upper bound delta >= delta(P)) is NOT covered — the robustness lemma
W_{4 sqrt d, sqrt d/4} ⊆ W_{C sqrt delta, c sqrt delta} (d <= delta <= delta_0) remains OPEN,
and the W27 matrix form is row-sum-one signed (NOT stochastic, NOT idempotent) — see FINDINGS
2026-07-06 W27.

**Contract rewording (2026-07-10, USER-ADOPTED — aism-nlg / W46 worker AW).** The
pre-adoption contract is preserved verbatim below; the free upper-bound delta was UNUSED
(every consumer runs pinned at d = delta(P)), and the trailing op-classical consequence
clause moved here: via [[thm-classical-factorization]] (restated form) and
[[lem-classical-equiv]] (d <= K*eta), this statement implies op-classical. The loose-delta
robustness question leaves the ledger WITHOUT proof (officially unneeded, not resolved).

> PRE-ADOPTION CONTRACT (verbatim): (OPEN) Global exposed-hull lemma: there are universal c,C>0 such that for every near-positive signed affine retraction with neg mass <= delta, taking rho=C sqrt(delta) and W_{rho,kappa}={vertices v: e_v(rho)>=kappa} with kappa=c sqrt(delta), every row is within C sqrt(delta) of conv W_{rho,kappa}; by thm-classical-factorization (global form) this implies op-classical.
