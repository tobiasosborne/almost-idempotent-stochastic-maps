# BRIEF — LEDGER-SETTING-RESCOPE design round (W136)

Date: 2026-08-05. Author: orchestrator (Claude). Status: commissioning brief for a
FRESH codex designer. **USER-RATIFIED commissioning 2026-08-05** ("Design round +
audit" selected over direct mechanical re-scope). A SEPARATE fresh hostile audit
follows; nothing lands without user ratification of the audited package.

## 1. The problem (verifier-caught, systematic)

The 16 LEDGER-DOMAINS rows (landed 2026-08-03, commit `5f08f22c`, from the
W78-ratified `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md`)
carry contracts transcribed verbatim from the design's §2 table. The design's §1
preamble fixes the ambient setting ONCE ("All proposed contracts are restricted to
the finite Route-F setting H = C^n"), and §1's notation note carries
`rho_AI := eta_A`. The per-row contracts do NOT restate any of this.

The af elevation of rows 1 and 3 (first two attempted) validated the mathematics
node-by-node (row 1: 13/20 validated; row 3: 4/5 validated) but fresh verifiers
correctly blocked both ROOTS. The three decisive challenge texts, verbatim:

- `ch-fe50a1d47d30ca64` (row 3 root): "The validated children prove only a
  conditional statement under hypotheses absent from the root: node 1.1 assumes a
  nonzero finite-dimensional H, a UCP map Phi:B(H)->B(H), ||Phi^2-Phi||_cb<=eta,
  and definitions tilde-Delta:=v and tilde-Upsilon:=v^(-1)tilde-Phi, and explicitly
  says these hypotheses are not claimed to follow from the root. The root
  quantifies only eta and neither states those hypotheses nor defines tilde-Delta,
  tilde-Upsilon, tilde-Phi, B, C_A, epsilon_E, rho_theta, or rho_AI through any
  allowed registered definition."
- `ch-d2d3e5c963af4c30` (row 3): "The allowed linearization dependency produces a
  radius eta_A and requires eta <= eta_A, but this node obtains only
  eta <= rho_AI. Neither the registry shard nor any registered definition or
  external states rho_AI := eta_A. [...] the design-provenance documents cannot
  supply an unstated equality here."
- `ch-dd2ab7c37c8541f1` (row 3): "The phrase 'in the finite-dimensional raw-factor
  setting' is not defined [...]. The only registered def-almost-idempotent instead
  concerns row-stochastic matrices with an infinity-to-infinity defect, which
  cannot provide the required UCP/cb assumptions."

Row 1's independent verifier raised the same objection (`ch-782c366f12ac5fee`).

## 2. The worked contrast (what a dischargeable contract looks like)

Every previously af-validated Route-F contract is self-contained. Exemplar,
`lem-routef-ai-defect-linearization` (T0): "...There are universal C_A < infinity
and eta_A > 0 [...] such that for every nonzero Hilbert space H, every UCP map
Phi:B(H)->B(H), and every eta satisfying 0 <= eta <= eta_A and
||Phi^2-Phi||_cb <= eta, if tilde-Phi=..., A=Im(tilde-Phi), ... then ...".

## 3. Deliverables (design ONLY — do not touch definitions/, argument/, proofs/)

Write `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE.md`
containing:

1. **A proposed setting definition shard** (suggested id
   `def-routef-raw-factor-setting`; you may propose better) — full proposed body
   in the `definitions/` schema (read `definitions/README.md`), tag `original`,
   capturing exactly: nonzero finite-dimensional Hilbert space H; UCP
   Phi:B(H)->B(H) with ||Phi^2-Phi||_cb <= eta; tilde-Phi, A=Im(tilde-Phi), the
   star product and epsilon_AI(eta) exactly as in
   `lem-routef-ai-defect-linearization`; the constants C_A, eta_A from that row;
   C_E, epsilon_E from `lem-thmainext-conditional`; rho_theta := 1/8;
   **rho_AI := eta_A (the missing equality, stated explicitly)**; the raw factor
   maps tilde-Delta := v and tilde-Upsilon := v^(-1) tilde-Phi where v:B->A is
   the extended isomorphism supplied by `lem-thmainext-conditional` applied to A
   (state the applicability chain that makes v exist on the relevant radius);
   and the scalar ledger (1.1)-(1.8) of DESIGN-LEDGER-DOMAINS-v2 §1 (with audit
   correction rho_id^corr) as named constants. Mind L2: this must not restate
   existing definitions — reference them.
2. **16 re-scoped contracts**, exact byte-level registry-ASCII texts, one per row,
   each binding its ambient setup by referencing the setting definition (e.g.
   prefix "In every def-routef-raw-factor-setting datum (H, Phi, eta, ...):").
   The mathematical content — every coefficient, radius, inequality — must be
   BYTE-UNCHANGED relative to the landed contracts modulo the added binding. Flag
   any row where the naive prefix is wrong (e.g. rows quantifying over X, Y, or
   amplifications; row 14's PRH/F2/F3 imports; D2/D3).
3. **defs-line corrections**: whether `def-almost-idempotent` (row-stochastic
   picture) should be dropped or replaced on the 16 rows' `defs:` lines, and what
   replaces it (the setting def; anything else needed). List the full corrected
   `defs:` line per row.
4. **An af continuation plan** for the two live trees
   (`proofs/lem-routef-raw-factor-norms`, 20 nodes, 13 validated;
   `proofs/lem-routef-raw-factor-identities`, 5 nodes, 4 validated): whether
   root/interior `af amend` preserves the validated children, which nodes need
   amendment to cite the new def, and the expected node/round budget to finish.
5. **Blast-radius audit**: consumers of the 16 contracts (`lem-routef-k-ledger`
   proposed wiring, F0-assembly design) — confirm the re-scope is
   consumption-compatible; the DO-NOT-REWIRE guard stays untouched.
6. **Ranked risks** for the hostile auditor to attack.

## 4. Constraints (binding)

- Design only. NO edits outside `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/`.
- The scalar ledger, all constants, all radii: mathematically byte-unchanged.
- One canonical definition (L2); contracts reference `def-` ids, never restate.
- The linker's contract-match law: af root node 1 must equal the registry
  contract verbatim after landing — design the texts accordingly.
- Registry ASCII conventions per the landed shards (`a7ab84c7` precedent).
- Read before writing: `CONVENTIONS.md`, `definitions/README.md`,
  `argument/README.md`, the landed row shards `argument/lemmas/lem-routef-*.md`
  (16 ledger rows), `DESIGN-LEDGER-DOMAINS-v2.md`, and the two af trees
  (`af status -d proofs/<id>` with AF=~/go/bin/af).
- This design promotes nothing; all 16 rows stay `stated` until re-elevated.
