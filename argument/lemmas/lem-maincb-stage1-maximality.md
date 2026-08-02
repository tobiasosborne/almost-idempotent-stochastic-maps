---
id: lem-maincb-stage1-maximality
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN and w:C^m->A has maximum source dimension among all extended W.c0_cb*epsilon-inclusions satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, then every projection-basis image P_j=w(e_j) satisfies dim S_{P_j}=1.
defs: def-maincb-partition-state; def-maincb-witness-ledger; def-projection-basis; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-maximal-reset-selection; lem-maincb-stage1-strict-refinement; lem-maincb-reset-constant-ledger; lem-maincb-corner-nontriviality
status: proved
af: validated
workspace: proofs/lem-maincb-stage1-maximality
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M24 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1417-1426; deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule); DEPS-ONLY amendment 2026-08-02 per DESIGN-M24-NONTRIVIALITY-v2.md sect-2.2 (contract byte-UNCHANGED; adds the lem-maincb-corner-nontriviality lower-bound provider; AUDIT-M24-NONTRIVIALITY.md DESIGN-CONFIRMED; user pre-ratified in-session, session 41); af-VALIDATED 2026-08-02 (second elevation, first-pass 5/5 clean, zero challenges; oracle af-lem-maincb-stage1-maximality PASS)
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated, 5/5 nodes
clean, taint clean, zero challenges, FIRST-PASS on the post-repair
re-elevation, tier routine, 2026-08-02; oracle PASS; tree: fixed-W
binder/admissibility -> provider lower bound -> M23 upper bound ->
integer squeeze). Contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M24 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M24. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9 (DESIGN-M24-NONTRIVIALITY-v2.md sect-2.2, superseding the
original 4/2/8 for the rebuilt four-child tree). Per-row skeleton:
DESIGN-M24-NONTRIVIALITY-v2.md sect-4.2. A hard-cap hit is a factoring
stop, not a rounds bump. Constants live in the proof body, never the
contract.

**Elevation guidance (BINDING, 2026-08-02; design v2 sect-8.2 + the
session-39 worked patterns).** (i) FIRST child = the fixed-W
binder/admissibility child: eliminate the single M18-supplied W and its
already-fixed witness provenance before defining the admissible family;
choose no new universal constant and introduce no fresh witness
afterward. (ii) One shared W, one shared admissible-family definition,
one shared maximal w, one arbitrary but fixed j. (iii) The lower bound
comes ONLY from lem-maincb-corner-nontriviality on that exact W,w,e_j —
do NOT cite paper line 1066, do NOT infer it from P_j != 0, do NOT
manufacture a partition state. (iv) The upper bound comes ONLY from
lem-maincb-stage1-strict-refinement for the same W,w,j, feeding w_+ into
the first child's admissibility predicate. (v) NO reset provider anywhere
(no lem-maincb-reset-output-typing, no M19-R); no second maximal map, no
fresh ledger, no fresh M04 witness. (vi) NO node may cite a PENDING
SIBLING — validate the lower- and upper-bound children before the
equality/root assembly cites either. (vii) Cite def-extended-delta-inclusion
at the exact point map typing is used.

**REPAIR RECORD (2026-08-02, aism-twpa RESOLVED by option (a)).** First
elevation aborted STUCK: `dim S_{P_j} >= 1` was underivable (challenges
ch-94ae993f6abc0f5b / ch-7411a0325c917f52; root weakening rejected as
scope drift, ch-37eff8dcb9a3b5d1). Repair: the NEW additive provider
`lem-maincb-corner-nontriviality` (this shard's contract byte-UNCHANGED;
deps-only amendment). Serial order: elevate the provider to T0 FIRST,
then cleanly re-seed and elevate this row, then M28.

**Provenance loci.** approximate_algebras.tex:1417-1426
