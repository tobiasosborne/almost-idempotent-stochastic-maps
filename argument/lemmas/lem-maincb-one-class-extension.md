---
id: lem-maincb-one-class-extension
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, all atomic images are one-dimensional, and C is one equivalence class, then there is a current reset isomorphism v_C:M_{|C|}->A_C whose recorded ambient field epsilon_C is selected so that A_C is an extended epsilon_C-C*-algebra and epsilon_C <= W.L*epsilon <= W.K_call*epsilon, and which satisfies d_C <= W.c0_cb*epsilon_C and ||v_C(I_{M_{|C|}})-u_{A_C}|| <= W.c0_cb*epsilon_C.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-maincb-witness-ledger; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-direct-corner-envelope; lem-maincb-corner-equivalence; lem-maincb-initial-raw-inclusion; lem-maincb-stage2-raw-extension; lem-maincb-stage2-call-envelope; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger; lem-maincb-reset-constant-ledger; lem-maincb-reset-output-typing
status: stated
af: seeded
workspace: proofs/lem-maincb-one-class-extension
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M25 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1378-1412,1430-1441; recorded-field ENV repair per DESIGN-RECFIELD-REPAIR.md sect-3 (hostile-audited AUDIT-RECFIELD-REPAIR.md DESIGN-CONFIRMED zero corrections; user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, second ratification)); deps aligned with the contract's own W-supplier reference (F3-class wiring fix, 2026-08-01: contract names lem-maincb-reset-constant-ledger, deps must import it — argument/README module rule); DEMOTED 2026-08-01 (latent unregistered-premise gap, AUDIT-CONSUMER-REPAIR.md F1 (nodes 1.1.2.2/1.1.3.2: bijective=>isomorphism without the extended-inclusion typing); docs/LEARNINGS.md 2026-08-01; re-validation pending) per DESIGN-CONSUMER-REPAIR.md + AUDIT-CONSUMER-REPAIR.md (F-corrections applied verbatim); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, fifth ratification)
owner: A
---
**Status.** `stated` — DEMOTED 2026-08-01 (the banked certificate's nodes
1.1.2.2/1.1.3.2 inferred bijective=>isomorphism without the
extended-inclusion typing, AUDIT-CONSUMER-REPAIR.md F1; docs/LEARNINGS.md
2026-08-01; the CONTRACT was never refuted). The 2026-08-01 re-validation
(2 runs) churned on the dual-provider distinct-witness and
induction-packaging challenges (parked tree preserved at commit 0288aa43)
and is superseded by the fresh 2026-08-02 re-seed below. Contract per the
audited `DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M25 (hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session). MAIN campaign row M25. NOT proved in-repo; af re-validation
pending. NOTE (banking order): deps lem-maincb-reset-constant-ledger /
lem-maincb-structural-domain-ledger are linker-SUSPENDED pending the
M19-S3 re-bank — M25 may validate but can only FLIP after they re-flip.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
10 / 3 / 14; scoped cap amendment 14->17 exercised transparently in the
2026-08-01 runs (flagged) and CARRIED into the 2026-08-02 re-seed; repo
ceiling 26. Per-row skeleton and audit delta: DESIGN-MAINCB-REPAIR-v2.md
sect-4 (and sect-8 re-seed guidance where applicable). A hard-cap hit is a
factoring stop, not a rounds bump. Constants live in the proof body, never
the contract.

**Re-seed architecture (BINDING on the fresh tree, 2026-08-02; from the
parked runs' challenges + the F1 audit prescription, HANDOFF session-39).**
(a) Use the typed-reset provider lem-maincb-reset-output-typing ALONE for
EVERY reset step — its conclusion subsumes lem-maincb-reset-invariant-
preservation's; citing both providers for the same step invites the
distinct-witness challenge that killed the parked runs. A consumer of an
existential provider must fix ONE witness explicitly and thread that SAME
witness through all subsequent uses (the same-map law). (b) Explicit
induction dependencies: every inductive step node names the exact prior
node(s) supplying its hypothesis — no floating 'inductively constructed
state' nodes. (c) The F1 cure: any bijective=>isomorphism inference must
cite the extended-inclusion typing (def-extended-delta-inclusion or the
typed-reset provider's conclusion) explicitly at the point of use.

**Provenance loci.** approximate_algebras.tex:1378-1412,1430-1441
