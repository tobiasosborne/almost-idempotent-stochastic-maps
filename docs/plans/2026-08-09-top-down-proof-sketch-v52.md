# Top-down proof sketch v52: op-classical (2026-08-09, session 46 — W139 stages 1-3 BANKED at T0, stage 4 balloon escalated; W140 report sync landed: 92 results anchored)

## UNCHANGED from v51

**`op-classical` is `proved` / `af: validated`** (root discharge 2026-08-08;
explicit dimension-free eta_0 = eta_K, C = K+4*sqrt(2K)). The honest
boundary stands: af-validated rung only (no Lean); the discharged contract
is the upper bound only. `ex-hume` remains RETRACTED (`disproved`);
signed-parameter (delta) sharpness remains established at NO rigorous rung.

## Map change 1: the factored sharpness sub-tree is T0 (T0 196 → 199)

All three rows of the user-ratified prh-sharpness factoring are now
`proved` / `af: validated`, each with a fresh xhigh codex prover, separate
fresh xhigh codex verifiers, an af export, and an external `fr verify`
oracle pass:

- `lem-prh-sharpness-family-arithmetic` — run 2 under FINDINGS remedy (a)
  (xhigh, cap 26 unchanged): 24/24 nodes, taint clean. The two predicted
  challenge classes (strict-vs-weak norm chain incl. the R=0 endpoint;
  cross-sibling row identification) were raised by verifiers and repaired
  in-tree.
- `lem-prh-sharpness-row-coincidence` — run 1 + verify resume: 19/19
  nodes, taint clean, cap 22.
- `lem-prh-sharpness` — run 3, the sect-5.3 clean re-seed on the two T0
  sub-lemma externals: FIRST-PASS, 12/12 nodes, cap 18, zero challenges.
  The monolith that ballooned twice (27, 28 live) closes at 12 nodes once
  factored: the factoring remedy is fully vindicated.

**PRH square-root sharpness is therefore T0**: for every 0 < lambda < 1/2
the explicit 4x2/2x4 pair (A_lambda, M_lambda) has retract defect
epsilon_lambda = 2*lambda^2 → 0 while every stochastic idempotent F on
l-infinity(4) stays at distance >= lambda = sqrt(epsilon_lambda/2).

## Map change 2: stage 4 (`cor-classical-sharpness`) ballooned — USER DECISION pending

The classical-picture carrier (`stated`, sole dep the now-T0
`lem-prh-sharpness`) was seeded per DESIGN-EXHUME-SHARPNESS-V2.md sect-5.2
and its run 1 (xhigh, ratified cap 20 / 4 rounds) ballooned at BUILD: 26
live nodes before any verification — the FOURTH family balloon
(27/28/27/26). Classification (TREE-CORSHARP-ABORTED.md; FINDINGS
2026-08-09): build-shape — the quantifier-discharge branch (~10 nodes of
explicit no-beta>1/2 counterexample arithmetic: b = (C*2^beta)^(-1/(2beta-1)),
per-(C, eta_0, beta) packaging, plus a logical-equivalence wrapper) and the
defect-factorization branch dominate; no missing byte-matched fact, no
genuine-gap tell. Cap NOT bumped; nothing resumed. Remedies escalated for
user ratification:
- **(b) skeleton-tightening design addendum** (make eta_lambda/Q_lambda
  definitional in node 1; state the negation directly as the
  per-(C, eta_0, beta) counterexample family, dropping the equivalence
  wrapper) — fresh hostile audit + ratification, cap unchanged; OR
- **(c) factor the quantifier branch** into a registry sub-lemma
  (e.g. `lem-classical-sharpness-exponent-negation`) — registry change,
  ratification + provisioning + two-row elevation.
Until stage 4 banks, **classical (eta-parameter) sharpness of the exponent
1/2 is still NOT at T0** — it is carried by the `stated` corollary resting
on a T0 lemma.

## Map change 3: the lab-book is synchronized (W140)

92 af-validated registry results that had no paper-track prose (the entire
MAIN campaign, S1-ENDGAME, GAP-EA, the topology toolbox, the Stage-1
quotient package, the Route-F raw-factor/normalization/upsilon/telescope
families, the strengthened K-ledger package + F0 assembly + thmainext, the
Kitaev diagonal pair, and `op-classical` itself) are now anchored as report
shards 52-72: typeset statements, byte-verbatim contract quotes, prose
accounts of the af trees. Authors/auditors/fixer/re-auditor were four
disjoint sets of fresh codex workers; 26 faithfulness findings (incl.
contract-strengthening drifts in typeset statements) were applied verbatim
and re-audited to 10/10 LAND. The campaign-statistics layer was rebuilt
into a retraction-aware artifact-counted census. PROVENANCE +94 claim rows
+184 hashed source rows; UNWIRED -92; PDF clean.

## The remaining rigour surface (ranked)

1. **Stage 4 remedy decision** ((b) vs (c) above) → bank
   `cor-classical-sharpness` → Stage D closure (report sharpness
   subsection, paper sect-5 switch to the 4x4 witness, PRD/README/HANDOFF,
   the deferred active-carrier citation halves).
2. Signed-parameter (delta) sharpness: still NO carrier at any rung
   (deliberately out of scope of the current campaign).
3. Lean/mathlib top rung: only on user elevation.
4. The legacy signed chain (`conj-kernel` / `op-hlc` / `op-exposed-hull`):
   NOT decided by the discharge (implications point downstream), but the
   T0 root + `lem-classical-equiv` reduce the sqrt(delta)-scale rows to a
   single recurrent-to-exposed identification bridge (real content —
   exposedness-window / cloning-obstruction terrain; (EX) is linear-in-delta
   and stays untouched). Reopening is a portfolio decision.
