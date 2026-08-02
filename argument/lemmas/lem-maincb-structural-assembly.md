---
id: lem-maincb-structural-assembly
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits a finite-dimensional C*-algebra B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon; hence C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive universal witnesses.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-witness-ledger; def-operator-space; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-full-corner-identification; lem-maincb-corner-equivalence; lem-maincb-structural-domain-ledger; lem-maincb-maximal-reset-selection; lem-maincb-stage1-maximality; lem-maincb-one-class-extension; lem-maincb-stage3-finite-recombination; lem-maincb-reset-constant-ledger; lem-maincb-extended-inclusion-monotone; lem-maincb-witness-arithmetic
status: proved
af: validated
workspace: proofs/lem-maincb-structural-assembly
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M28 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1414-1444; deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule); af-VALIDATED 2026-08-02 (second elevation post-balloon-response, 20/20 clean under the scoped cap 20; oracle af-lem-maincb-structural-assembly PASS)
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated, 20/20
nodes clean, taint clean, 2026-08-02, tier routine, second elevation
under the flagged scoped cap 20: run 1 ballooned on missing workspace
vocabulary; run 2 built 20 nodes, resolved all in-run challenges incl.
the cross-unit monotonicity pair via an amplification-wise direct
check, and validated fully in the resumed verify phase; oracle PASS).
THE MAIN STRUCTURAL-ASSEMBLY CAPSTONE — with this bank every MAIN
campaign row M01-M28 is af-validated T0. Contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M28 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M28.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
9 / 3 / 13; **SCOPED CAP AMENDMENT 2026-08-02 (flagged): hard cap 20**
(ceiling 26) — the W129 first elevation aborted BALLOON at 20 nodes with
transparent repair growth (each round-1 child answered a specific
challenge; root never challenged); the enlarged cap covers the glue
nodes below. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where
applicable). A hard-cap hit is a factoring stop, not a rounds bump.
Constants live in the proof body, never the contract.

**Elevation guidance (BINDING, 2026-08-02; the W129 balloon lessons —
challenges ch-33d9c549284c60fd, ch-261ab25fa415cf4a, ch-5294728017efdb3f,
ch-6e65073fecfd7483, ch-02181cc73c5a694b, ch-81b32a18e3409c3b).**
(i) WORKSPACE VOCABULARY (provisioned; use it, do not re-derive):
def-delta-projection, def-projection-basis,
def-one-dimensional-delta-projection, def-compressed-corner,
def-epsilon-cstar-algebra, and the byte-verbatim
GT-kitaev-def-delta-homomorphism external — every t-projection /
one-dimensionality / compressed-unit inference cites these explicitly at
the point of use. (ii) CONSTRUCT the MAIN partition state EXPLICITLY in
an early dedicated node BEFORE any M25/M27 citation: fix W, the maximal
w (M22), one-dimensional atomic images (M24), the class family
(corner-equivalence M10 + def-maincb-partition-state), the current
subset, and the per-class initial reset-state data; never write "the
supplied MAIN partition state" without having constructed it. (iii) A
dedicated identification node derives A_J = A and u_{A_J} = Co_R(R) = R
from lem-maincb-full-corner-identification (Co_R = I, S_R = A) +
def-compressed-corner; every downstream node that uses either fact
declares THIS node as a dependency. (iv) NO node may cite a PENDING
SIBLING — declare real dependencies (the W129 1.5/1.7 failures were
exactly sibling anaphora). (v) One fixed W threaded throughout; no
witness reselection; constants through the ledger only.

**W129 ABORT RECORD (2026-08-02).** First elevation BALLOON 20 > 13:
6 major challenges, 4 curable by the missing vocabulary above, 2 by the
explicit partition-state/identification nodes; classification on the
session-41 bead; ballooned 102-entry tree preserved in the session-41
scratchpad. Root contract NEVER challenged (not a contract-level
finding). Workspace re-seeded clean.

**Provenance loci.** approximate_algebras.tex:1414-1444
