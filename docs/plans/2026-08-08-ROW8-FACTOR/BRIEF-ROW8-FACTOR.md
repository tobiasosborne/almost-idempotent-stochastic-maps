# BRIEF — design the factoring of ledger row 8 (`lem-routef-upsilon-prime-closeness`)

You are a fresh design worker. You did NOT build the aborted tree and you must
not trust it — you must re-derive the factoring from the sources below.

## Situation

The af elevation of `lem-routef-upsilon-prime-closeness` (LEDGER-DOMAINS row 8,
design projection 11 nodes) aborted at 28 live nodes > the hard brittleness
ceiling 26 (`scripts/af_constants.py NODE_SOFT_CAP`; CLAUDE.md L4: a tree past
26 nodes is a brittleness FAILURE and must be factored into registry
sub-lemmas). The tree was converging — 18/29 nodes validated, zero open
challenges — so the mathematics is believed sound; the row is simply too big
as one tree. Fresh builds in this family run 1.5–3x the design projections
(formation-instantiation scaffolding), so the honest budget for the factored
pieces must each fit comfortably under 26 WITH that expansion.

## Task

Design a factoring of row 8 into AT MOST two new sub-lemma registry rows plus
a slimmed main row, following the natural branch boundaries visible in
`TREE-ROW8-ABORTED.md` (same directory):

- branch 1.2–1.4: finite-dimensional Choi/twirl data, nonzero-multiplicity
  repair, and the componentwise CP construction of Upsilon';
- branch 1.5: the uniform approximate-left-inverse estimate
  `||UpsilonPrime_q Delta_q(Y) - Y|| <= C_L*eta*||Y||` at every amplification;
- the ambient fixing (1.1) and final telescope/cb assembly (1.6) stay in the
  main row.

You may propose a different split ONLY if you show the natural one cannot fit
the budgets; justify any deviation explicitly.

## Hard constraints (violating any of these makes the design REJECTED)

1. **The main row's `contract:` line must stay BYTE-IDENTICAL.** It is a
   user-ratified re-scoped contract. Only its `deps:` (and if strictly needed
   `defs:`) lines may change, by ADDING the new sub-lemma ids.
2. **Sub-lemma contracts must be self-contained** and follow the family's
   ambient-binding pattern: the exact prefix "After first fixing one global
   witness package W_RF supplied by lem-routef-raw-factor-setting-formation,
   for every input (H,Phi,eta) to which that formation result applies, fix one
   def-routef-raw-factor-setting datum S over that same W_RF supplied by the
   same result, writing the fields of (W_RF,S) as the unqualified symbols
   below:" followed by a mathematically complete suffix. Every symbol either
   comes from (W_RF,S) via `def-routef-raw-factor-setting`, from a declared
   dep's contract, or is defined inside the contract itself. NO symbol may
   rest on the design preamble (that failure mode killed the family once
   already — see FINDINGS.md 2026-08-05, ambient-binding under-specification).
3. **Deps only on af-validated (T0) rows** — the available pool is the current
   registry state (rows 1–7, D2, D3, the formation row, the Kitaev pair,
   functional-calculus-closeness, ai-defect-linearization, thmainext,
   kitaev-almost-idemp-audit are all T0). A sub-lemma may dep on the other
   sub-lemma if the order is acyclic.
4. **No new definitions** unless truly unavoidable; if unavoidable, the def
   must be theorem-free (data/typing/notation only — the deletion test).
5. **Budgets:** for each of the (2 or 3) targets state designed-node count,
   honest live expectation (with the 1.5–3x expansion), max rounds, and hard
   cap <= 26. Every target must have honest expectation strictly under 26.
6. **Provenance:** each new shard's `provenance:` line must cite
   DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 8 loci (TeX 2831-2895; K-ledger
   228-245; audit 181-209), this design, and the balloon-abort classification
   (2026-08-08). `status: stated`, `af: none`, `owner: A`,
   `workspace: proofs/<id>`.
7. Registry ids: kebab-case `lem-routef-...` names consistent with the family.

## Inputs you MUST read

- `docs/plans/2026-08-08-ROW8-FACTOR/TREE-ROW8-ABORTED.md` (the aborted tree)
- `argument/lemmas/lem-routef-upsilon-prime-closeness.md` (the frozen row)
- `definitions/def-routef-raw-factor-setting.md` (the setting/scalar ledger)
- `argument/lemmas/lem-routef-raw-factor-setting-formation.md`
- The T0 sibling rows' contracts (delta-prime/normalization, D2, D3, row 7,
  raw-factor rows) under `argument/lemmas/`
- `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md`
  sect-2 row 8 and its sect-6/7 componentwise material
- `CLAUDE.md` sections 1 (L0–L5) and 6; `FINDINGS.md` 2026-08-05 entries

## Deliverable

Write EXACTLY ONE file:
`docs/plans/2026-08-08-ROW8-FACTOR/DESIGN-ROW8-FACTOR.md` containing:

(a) the complete text of each new sub-lemma shard (full frontmatter + body,
    ready to land verbatim);
(b) the revised `deps:` line of the main row (byte-identical contract);
(c) a complete af tree skeleton per target (node ids + exact statements),
    demonstrating each fits its budget;
(d) the seeding package per target: the def-add list and the exact
    add-external list (name + source-string form; dep externals use the
    literal `proofs/<dep-id>` path + byte-verbatim contract convention);
(e) the elevation order (sub-lemmas first, then the slimmed main row) and
    per-target budgets;
(f) a ranked list of the risks a hostile auditor should attack.

Head the file with: `Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED,
OR PROMOTE — pending fresh hostile audit and user ratification.`

## Discipline (non-negotiable)

Write ONLY the deliverable file. Do NOT edit `argument/`, `definitions/`,
`proofs/`, or any other file. Do NOT run git commit or git push. Do NOT run
`af` mutations. Your final message: a 10-line summary of the proposed split
and budgets.
