---
id: lem-routef-f0-assembly
kind: lemma
contract: Route F F0 assembly: there are universal eta_0,C > 0, independent of n, such that for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_0 with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= C*sqrt(eta); for the universal K and eta_K supplied by lem-routef-k-ledger, one may take eta_0 := eta_K and C := K+4*sqrt(2*K).
defs: def-stochastic; def-almost-idempotent
deps: lem-routef-k-ledger
status: proved
af: validated
provenance: docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md sect-1.4 (assembly row and no-double-counting rule), with the canonical complexification typing correction required by AUDIT-F0-ASSEMBLY.md; strengthened-parent interface and exact constants from DESIGN-KLEDGER-STRENGTHENED.md, pending its required fresh hostile audit and user ratification. That v1 package was REJECTED by AUDIT-KLEDGER-STRENGTHENED.md findings 1-4; the byte-identical F0 contract and cleared minimality finding are retained in DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile re-audit and user ratification. This is an upper-bound assembly only; no sharpness claim is imported or promoted.
owner: A
workspace: proofs/lem-routef-f0-assembly
---

**Status.** `proved`, `af: validated` (2026-08-08): root node 1 validated/clean, 7-node
tree all validated/clean, fresh codex provers with separate fresh hostile verifiers per
node, cap 8 held (run 1 hit max-rounds with 6/7 validated and zero challenges; the
verify-phase resume completed the root); external oracle `af-lem-routef-f0-assembly` +
`fr verify` PASS. Mechanical reflection of the codex ledger.

**Specialization.** Take `eta_0:=eta_K` and `C:=K+4*sqrt(2*K)` from the parent. The parent
states that `eta_K>0`, `K>=1`, both are universal and dimension-free, and for every
admissible `n,Q,eta` returns the required stochastic idempotent for the same `Q`.
Elementary square-root positivity gives `C>0`.

**No double counting.** Registry `deps:` is exactly `lem-routef-k-ledger`. The parent
already consumes both F0 seam rows, formation, the factor-map packet, F2, F3, and PRH.
Repeating any of those edges here would misstate the module boundary.

**Sharpness and root guard.** This row proves only the upper-bound statement displayed in
its contract. It does not consume `ex-hume`, does not claim sharpness, and does not edit or
rewire `op-classical`. The name ex-hume here is a historical matrix-family pointer only; this
row has no dependency on it and imports no part of its disproved contract. Root rewire remains the separate LAST step after this row is T0.

**Designed af budget.** Two designed nodes; honest live expectation 3--6 under the
observed 1.5--3x expansion; depth 2; at most 2 rounds; hard cap 8. The 3x endpoint 6 is
strictly below 8.
