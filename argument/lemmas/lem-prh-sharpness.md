---
id: lem-prh-sharpness
kind: lemma
contract: PRH square-root sharpness: for every 0 < lambda < 1/2 there are positive unital maps A:l-infinity(2)->l-infinity(4) and M:l-infinity(4)->l-infinity(2) with epsilon_lambda=||MA-I_2||_{infinity->infinity}=2*lambda^2 tending to 0 such that every stochastic idempotent F on l-infinity(4) satisfies ||AM-F||_{infinity->infinity} >= lambda=sqrt(epsilon_lambda/2); hence the sqrt(epsilon) order in PRH is intrinsically sharp.
defs: def-positive-approximate-retract; def-stochastic
deps: lem-prh-sharpness-family-arithmetic; lem-prh-sharpness-row-coincidence
status: proved
af: validated
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md §7; hostile batch verdict VERDICT-W74F-BATCH.md §A (VALID, no correction); af elevation run 3 (post-factoring clean re-seed per DESIGN-PRHSHARP-FACTOR.md sect-5.3) VALIDATED 2026-08-09 FIRST-PASS: 12/12 nodes, taint clean, cap 18 respected, 3 rounds, zero challenges; fresh xhigh prover + separate fresh xhigh verifiers; both T0 sub-lemma externals byte-verbatim; export proofs/lem-prh-sharpness/export.md; fr verify pass via oracle af-lem-prh-sharpness
owner: A
workspace: proofs/lem-prh-sharpness
---

**Status.** `proved` / `af: validated` (2026-08-09, run 3 — the post-factoring
clean re-seed). Mechanical reflection of the codex ledger: root validated
first-pass with 12/12 nodes clean under hard cap 18, zero challenges, resting on
the two T0 sub-lemma externals; externally banked via `fr verify` on the export
path.

**Transcribed family.** The encoder rows are
\[
(1,0),\quad(0,1),\quad(1-\lambda,\lambda),\quad
(\lambda,1-\lambda),
\]
and the decoder rows put masses \(1-\lambda,\lambda\) respectively on
the first and third states, and on the second and fourth states.  The
artifact computes
\[
\lVert MA-I_2\rVert_{\infty\to\infty}=2\lambda^2.
\]
Its row-coincidence argument for stochastic idempotents shows that an
idempotent within distance \(<\lambda\) would have two equal rows whose
corresponding \(AM\)-rows are \(2\lambda\) apart, a contradiction.

**Honest scope.** This is sharpness for PRH itself, not a transfer of the
independent sharpness statement for `op-classical`; the optimal universal
constant remains undetermined.
