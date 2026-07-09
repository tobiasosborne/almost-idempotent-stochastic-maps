---
id: conj-shallow-counterweight-exclusion
kind: lemma
contract: (CONJECTURE) Shallow universally-shadowed counterweight exclusion (SL1b): there exists universal delta_0 > 0 such that no exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, and hidden top vertex v of height H > 16*tau admits a sub-probability measure mu_S of total mass >= tau/(2+4*delta) on rows f with ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv W) <= H - 4*tau such that sum_f mu_S(f)*h(p_f) <= kappa for every admissible exposer h at v.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): Fable author L2's SL1b, V-L2-audited (the Case-(ii) reduction proved; the per-row universal-shadow pin sup_h h(p_f) <= t*/m for lambda_f >= m is part of the proved split). Full derivation: docs/waves/2026-07-09-W54-artifacts/l2-attack.md §2.7
owner: A
---

**Role (the small leaf — attack FIRST).** A definite mass of rho-far SHALLOW rows that
every admissible exposer at v shadows below kappa: shallow rows live near the visible
hull where exposers have room, so universal shadowing is a strong constraint — the
L2 author grades this the most attackable open leaf. It is exactly the escape hatch of
the pure co-top rigidity (Proposition E); killing it plus
[[conj-straddling-web-exclusion]] closes L2-core (proved sub-assembly, V-L2-audited)
hence Branch II of the W54 tree.

**Status discipline.** A conjecture — promotes nothing; consumers carry it as a dep.
