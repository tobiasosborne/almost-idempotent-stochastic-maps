# BRIEF — LEDGER-DOMAINS repair round (fresh designer; audit binding, corrections mostly prescribed)

You are a fresh, independent design mathematician. Prior state:
`DESIGN-LEDGER-DOMAINS.md` (14-row local-domain DAG, disposition
LAND-13-HOLD-1) was audited in `AUDIT-LEDGER-DOMAINS.md` with disposition
**REDESIGN** and three finding groups, most with EXACT prescribed repairs.
Your job: produce the corrected design incorporating every audit finding — or
refute a finding with exact loci.

Read, in order: `BRIEF-LEDGER-DOMAINS.md` (original constraints bind),
`DESIGN-LEDGER-DOMAINS.md`, `AUDIT-LEDGER-DOMAINS.md` (BINDING), and the
sources they cite.

## The findings to incorporate

1. **`lem-routef-upsilon-prime-closeness` radius repair:** add \((2C_R)^{-1}\)
   with \(C_R=C_V+C_\Delta+C_2\) to \(\rho_{\Upsilon'}\) so the Choi
   multiplicity space \(\mathcal E_j\) is nonzero where the proof selects a
   unit vector. Verify the corrected radius still composes downstream
   (telescopes, k-finiteness) and stays dimension-free.
2. **Dependency-list corrections:** apply the audit's exact import additions
   on the four raw/Delta rows and the degree-two reconnection (its §
   listing them — take each verbatim, then re-verify acyclicity and the
   serial order).
3. **Terminal-row closure (the audit's GAP-overstatement finding):** rewrite
   `lem-routef-threshold-minimum` per the audit's construction
   \(\eta_K=\min\{\rho_{\rm fac},(24K)^{-1},1\}\) using the landed
   `lem-thmainext-conditional` contract as the black-box producer of
   \(C_E,\varepsilon_E\) — WITHOUT importing the unlanded MAIN reset package.
   State explicitly in the row's notes: (a) this consumes
   `lem-thmainext-conditional` at its CONTRACT level (that row itself remains
   design-blocked/proved-mod-audit — consuming its contract in a design does
   not promote it, and the eventual af elevation of the threshold row will
   have it as a dep, inheriting its status per the linker rules); (b) the
   reset-shard absence and the v4.1 ε_max^cb omission remain TRUE findings
   for the MAIN front (W76) — record them as a cross-reference, not as a
   ledger blocker.
4. Re-run your own finite-minimum audit and dimension-freeness audit on the
   corrected DAG.

## Deliverable — write `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md`

Full corrected table (all 14 rows + the two degree reconnections + the
proposed parent wiring with the DO-NOT-REWIRE guard intact), same discipline
as before, plus a "disposition of audit findings" table (CLEARED-BY /
REFUTED with loci / ESCALATED per finding).

## Hard constraints

Design only; write ONLY inside `docs/plans/2026-07-26-LEDGER-DOMAINS-design/`;
no registry mutation; no status promotion; no guessed radii; NOT IN LOCAL
REFS discipline.
