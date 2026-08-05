# BRIEF — KITAEV-PAIR elevation design round (W136)

Date: 2026-08-05. Author: orchestrator (Claude). You are a FRESH codex designer
with NO prior context. USER-RATIFIED commissioning 2026-08-05 (bead: unblock
ledger rows 5-14). A SEPARATE fresh hostile audit follows; nothing is seeded or
promoted without user ratification of the audited package.

## Targets (elevate BOTH; the lemma first — it is the dep)

1. `argument/lemmas/lem-kitaev-diagonal-repair.md` — `proved-mod-audit`.
   Contract (verbatim in the shard): the printed Kitaev direct-sum diagonal
   formula is FALSE (already for B = C (+) C), but every finite-dimensional
   C*-algebra B = (+)_{r=1}^m M_{d_r} has a finite phase-balanced diagonal
   D = sum_t q_t W_t^dagger (x) W_t with unitary W_t, q_t >= 0, sum q_t = 1,
   central (ZD = DZ for Z in B), pi(D) = I_B, projective norm 1, independent
   of block count/dimensions. No deps. Existing paper-proof:
   `docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-B-DIAGONAL.md` §§2-3
   (hostile batch verdict VERDICT-W74F-BATCH.md §B: VALID, no correction).
2. `argument/lemmas/cor-kitaev-diagonal-cpization.md` — `proved-mod-audit`.
   Contract: for that D, every involution-preserving linear tilde-Delta:B->B(H)
   and UCP Phi define a CP map Delta'(X) = sum_t q_t Phi(tilde-Delta(X W_t^dagger)
   tilde-Delta(W_t)); complete positivity uses exact centrality of D only.
   Dep: the repair lemma. Paper-proof: PROOF-W74F-B-DIAGONAL.md §4.1.

## Why now

The LEDGER-DOMAINS queue's rows 5-14 rest on the cpization corollary through
row 5 (`lem-routef-delta-prime-closeness`); under the linker's
status-propagation law they cannot reach af:validated until this pair is T0.
The raw packet (formation + rows 1-4) is already T0 (174 rigorous results).

## Deliverables

One file: `docs/plans/2026-08-05-KITAEV-PAIR-ELEVATION/DESIGN-KITAEV-PAIR-ELEVATION.md`:

1. For EACH target: a complete af tree skeleton (per-node exact statements)
   proving the FROZEN contract byte-verbatim as root — do NOT re-scope or
   reword either contract. Work from the existing paper-proofs (read them),
   the shard bodies, and the Kitaev source (`refs/kitaev-2405.02434/
   approximate_algebras.tex`; the false printed formula at :1254 and
   :2780-2783 — the refutation clause of the repair contract needs a
   byte-verbatim GT external for the printed formula).
2. Per-workspace seeding package: exact `af def-add` list (definitions/
   shards; check `def-fd-cstar-diagonal` suffices or list base vocabulary)
   and exact `af add-external` entries (GT externals with verbatim quotes +
   loci; the corollary registers `proofs/lem-kitaev-diagonal-repair`).
   Note the established convention for GT externals
   (`GT-kitaev-def-delta-homomorphism` pattern; name, locus, verbatim text).
3. Projected af budgets (nodes/rounds/hard cap) per target — recall every
   fresh build this session ran ~1.5-3x naive projections; budget honestly.
4. Ranked hostile-audit risks (incl.: does the refutation clause need its
   own counterexample node; is centrality-only CP genuinely dischargeable
   without multiplicativity; Choi/positivity argument scope; phase-balance
   existence for arbitrary block sizes).

## Constraints (binding)

- Design ONLY: write nothing outside `docs/plans/2026-08-05-KITAEV-PAIR-ELEVATION/`.
- Contracts are FROZEN — the design proves them as-is or reports exactly why
  a contract cannot be discharged (that would return to the user).
- Elevation order: repair lemma banks BEFORE the corollary launches (the
  corollary's external must cite a validated workspace).
- L2: reference definitions; no restating. Registry ASCII conventions.
- This design promotes nothing; both rows stay proved-mod-audit.
