---
id: lem-routef-f2-positive-unital-compression
kind: lemma
contract: Route F F2 positive-unital compression: let K >= 1 be a dimension-independent constant, n >= 1, Q: l_inf^n -> l_inf^n row-stochastic, D: M_n -> l_inf^n diagonal extraction and J: l_inf^n -> M_n diagonal inclusion, Phi = J Q D, B a finite-dimensional unital C*-algebra, and Delta: B -> M_n, Upsilon: M_n -> B UCP maps; if 0 <= eta <= min{(24K)^{-1},1}, ||Delta Upsilon - Phi||_cb <= K*eta, ||Upsilon Delta - I_B||_cb <= K*eta, and ||Upsilon(Delta x Delta y) - xy|| <= K*eta*||x||*||y|| for all x,y in B, then B is commutative and there are k >= 1 and a unital *-isomorphism iota: l_inf^k -> B such that A := D Delta iota: l_inf^k -> l_inf^n and M := iota^{-1} Upsilon J: l_inf^n -> l_inf^k are positive unital maps satisfying ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k.
defs: def-stochastic
deps:
status: proved-mod-audit
af: none
provenance: docs/plans/2026-07-24-fudw-decomposition-artifacts/PROOF-F2F3-BRIDGE.md §1 (prover); hostile verdict VERDICT-F2F3-BRIDGE.md (VALID-WITH-CORRECTIONS, F2: VALID; contract = verdict §7 exact text); closes gap-routef-f2-positive-unital-compression-contract (DESIGN-FUDW-DECOMP-v3.md §2.6)
owner: A
workspace: proofs/lem-routef-f2-positive-unital-compression
---

**Status.** Fresh-codex paper proof, separately hostile-verified
(VALID-WITH-CORRECTIONS; F2 clause VALID), hence `proved-mod-audit` — not
af-validated and not L0-rigorous. Registered on the standing
verdict-driven-registration precedent; contract text is the verdict's §7
"F2 exact contract text" verbatim (LaTeX flattened to registry ASCII only).

**What it closes.** The former reservation
`gap-routef-f2-positive-unital-compression-contract`: this is the closed
hypothesis block that manufactures the positive unital maps `A, M` consumed by
`lem-routef-prh-finish`. Commutativity of `B` is derived, not assumed. Together
with `lem-routef-f3-retract-defect` its conclusions literally supply that row's
hypothesis list at threshold `eta <= (24K)^{-1}` (verdict §composition).

**Verifier corrections (recorded, wording-level).** (i) The proof's strict
inequality chain was false at `eta = 0`; replaced by
`<= (24/7)K*eta <= 4K*eta <= 1/6 < 1/2`. (ii) A stale GAP sentence updated:
W74F-H closed the relative ledger at `proved-mod-audit` (component factoring /
L0 remain open).

**Import discipline (verdict-mandated).** This row must NOT import the
quarantined component-domain rows (GAP-LEDGER-DOMAINS): its factorization
estimates are explicit contract hypotheses.
