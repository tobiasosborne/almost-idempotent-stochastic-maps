---
id: lem-maincb-improvement-iteration
kind: lemma
contract: There are universal e_it > 0, K_disp < infinity, and K_floor < infinity such that, if B is a finite-dimensional C*-algebra, A is an extended epsilon-C*-algebra, and v:B->A is an extended d-inclusion with d+epsilon <= e_it, then one dagger-preserving v_tilde, with v_tilde_n = I_n tensor v_tilde, satisfies sup_n ||v_tilde_n - v_n|| <= K_disp*d and is an extended K_floor*epsilon-inclusion; for epsilon > 0 it is reached after finitely many correction steps, and for epsilon = 0 it is their operator-norm limit.
defs: def-operator-space; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-fd-cstar-diagonal
deps: lem-maincb-improvement-one-step
status: stated
af: seeded
workspace: proofs/lem-maincb-improvement-iteration
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M02 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1313,1508-1535
owner: A
---

**Status.** `stated` — CONTRACT STRENGTHENED 2026-07-30 (USER-RATIFIED
in-session): the conclusion 'has extended defect at most
K_floor*epsilon' is replaced by 'is an extended
K_floor*epsilon-inclusion', matching the source's actual iteration
output (approximate_algebras.tex:1313,1508-1535). Driver: three
independent M03 verifier cohorts + a clean-re-seed rebuild established
that the weaker wording under-exports the amplified norm bounds every
downstream consumer needs (M03 ballooned to 26 nodes internalizing the
iteration). The 2026-07-30 af validation of the WEAKER statement
(7-node first-pass, oracle pass, fr banked cycle) is SUPERSEDED, not
retracted — no incorrect claim entered the record; its ledger is
preserved in git history. T0 count -1 pending re-elevation of the
strengthened contract. Workspace cleanly re-seeded.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M02. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1313,1508-1535
