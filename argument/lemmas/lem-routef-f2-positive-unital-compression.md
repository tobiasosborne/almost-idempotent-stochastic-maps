---
id: lem-routef-f2-positive-unital-compression
kind: lemma
contract: Route F F2 positive-unital compression: let K >= 1 be a dimension-independent constant, n >= 1, Q: l_inf^n -> l_inf^n row-stochastic, D: M_n -> C^n diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), J: C^n -> M_n diagonal inclusion, Q_C: C^n -> C^n the canonical complex-linear extension of Q, and Phi = J Q_C D, B a finite-dimensional unital C*-algebra, and Delta: B -> M_n, Upsilon: M_n -> B UCP maps; if 0 <= eta <= min{(24K)^{-1},1}, ||Delta Upsilon - Phi||_cb <= K*eta, ||Upsilon Delta - I_B||_cb <= K*eta, and ||Upsilon(Delta x Delta y) - xy|| <= K*eta*||x||*||y|| for all x,y in B, then B is commutative and there are k >= 1 and a unital *-isomorphism iota_C: C^k = l_inf^k(C) -> B such that D Delta iota_C maps R^k into R^n, iota_C^{-1} Upsilon J maps R^n into R^k, and the resulting restrictions and corestrictions A := (D Delta iota_C)|_{R^k}: l_inf^k -> l_inf^n and M := (iota_C^{-1} Upsilon J)|_{R^n}: l_inf^n -> l_inf^k are positive unital maps satisfying ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k.
defs: def-stochastic; def-ucp-map; def-projection-basis
deps:
status: proved-mod-audit
af: seeded
provenance: docs/plans/2026-07-24-fudw-decomposition-artifacts/PROOF-F2F3-BRIDGE.md §1 (prover); hostile verdict VERDICT-F2F3-BRIDGE.md (VALID-WITH-CORRECTIONS, F2: VALID); typing correction 2026-07-27 = docs/plans/2026-07-27-F2-TYPING-design/DESIGN-F2-TYPING.md §1.1 exact text, hostile-endorsed LAND by AUDIT-F2-TYPING.md (a)-(g); closes gap-routef-f2-positive-unital-compression-contract (DESIGN-FUDW-DECOMP-v3.md §2.6)
owner: A
workspace: proofs/lem-routef-f2-positive-unital-compression
---

**Status.** Fresh-codex paper proof, separately hostile-verified
(VALID-WITH-CORRECTIONS; F2 clause VALID), hence `proved-mod-audit` — not
af-validated and not L0-rigorous. Registered on the standing
verdict-driven-registration precedent; contract text was the verdict's §7
"F2 exact contract text" verbatim (LaTeX flattened to registry ASCII only).

**Typing correction (2026-07-27).** The §7 text carried a real-vs-complex
typing defect (D typed into l_inf^n = R^n while the diagonal of M_n lies in
C^n) — the same defect family repaired at T0 on both F0 seam rows, and the
STUCK cause of the first af elevation run (ch-2163ee19860aa3d7). The contract
above is the corrected text of DESIGN-F2-TYPING.md §1.1, VERBATIM, endorsed
LAND by the fresh hostile audit AUDIT-F2-TYPING.md: Phi = J Q_C D through C^n
exactly on the T0 F0 seam typing; A, M are the restrictions/corestrictions to
the real self-adjoint parts; every hypothesis, constant, threshold, and
estimate is unchanged. The pre-correction workspace tree is ill-typed and is
DISCARDED, not resumed (design §4); re-seed from this contract.

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

**Elevation provisioning (DESIGN-F2-TYPING.md §2, audit-endorsed; binding on
the af tree).** (i) The ONLY citable external beyond the registered defs is
the byte-verbatim projection-basis sentence
(refs/kitaev-2405.02434/approximate_algebras.tex:1361, registered in the
workspace as external `projection-basis-kitaev-1361`); the general
finite-dimensional C*-classification (Wedderburn direct-sum form) is NOT IN
LOCAL REFS and must NOT be cited — the noncommutative norm-2 commutator
witness is proved in-tree (minimal projections, matrix units, two Pauli
contractions; design §2.2), and the coordinate isomorphism iota_C is built
in-tree from the projection basis. (ii) UCP complete contractivity
(||T||_cb <= 1) is derived in ONE shared node from 2-positivity + Schwarz +
unitality (design §2.3) and declared as a dependency wherever contractivity
of Delta or Upsilon is used. (iii) Write K*eta in every node — no
epsilon := K*eta shorthand. (iv) Dependency discipline (design §2.4,
audit-corrected): the 10K*eta commutator node depends on approximate
invariance + the typed diagonal-range node; the commutativity-forcing node
binds K, eta and 0 <= eta <= (24K)^{-1} in its own statement and rederives
10K*eta <= 5/12 < 2 locally; the coordinate-isomorphism node depends on the
validated commutativity node + the projection-basis external; the QA-A node
depends on approximate invariance; the lower-modulus child proves only the
lower-modulus inference — the ROOT assembles the branches. (v) Hard stop:
25 live nodes (design §2.5); if exceeded, STOP for registry factoring
(lem-fd-cstar-norm-two-commutator / lem-fd-commutative-cstar-coordinates /
lem-ucp-complete-contractivity) instead of ballooning.
