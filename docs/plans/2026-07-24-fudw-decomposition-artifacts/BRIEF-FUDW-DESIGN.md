# BRIEF — aism-fudw decomposition DESIGN: factor the Route F chain into af-sized registry sub-lemmas

You are a FRESH DECOMPOSITION ARCHITECT (codex, independent context). Your job is a
**design document, not registry edits and not new mathematics**: factor the four large
hostile-verified Route F proof artifacts into a DAG of af-sized registry sub-lemma
*proposals*, each with a single minimal one-line contract, so that every future af
workspace stays inside the brittleness envelope (≤12 nodes, depth ≤3). You re-arrange
and quote the existing verified mathematics; you never alter, strengthen, or "fix" it.

## Read first (in this order)

1. `CLAUDE.md` — Laws L0–L5 and §6 (binding; especially the rigour ladder and the
   single-minimal-contract rule).
2. `argument/README.md` — the registry shard schema (contract/defs/deps/routes/status/af).
3. `docs/plans/2026-07-24-af-elevation-campaign.md` — the campaign plan you are phase 1 of.
4. The verified proof artifacts (your ONLY mathematical sources; all in
   `docs/plans/2026-07-24-W74F-wave2-artifacts/`):
   - `PROOF-W74F-E-HCB.md` + `VERDICT-W74F-E-HCB.md` (H-CB, internal nodes HCB-0..4)
   - `PROOF-W74F-F-EXTCB.md` + `VERDICT-W74F-F-EXTCB.md` (EXT-CB, internal nodes EXTCB-1..5)
   - `PROOF-W74F-H-STAGE1.md` + `VERDICT-W74F-H-STAGE1.md` (Stage-1 packet, SPLIT-A/B/C)
   - `LEDGER-W74F-G-K.md` + `VERDICT-W74F-G-KLEDGER.md` (the K/η_K ledger)
5. `docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md` (the MAIN-CB
   assembly decomposition the wave-2 proofs implement).
6. The existing registry shards these proposals must slot under (read, do not edit):
   `argument/lemmas/conj-hcb.md`, `conj-extcb.md`, `lem-thmainext-conditional.md`,
   `lem-routef-k-ledger.md`, `lem-kitaev-diagonal-repair.md`,
   `lem-kitaev-almost-idemp-audit.md`, `lem-prh.md`.
7. `definitions/INDEX.md` — the existing def vocabulary (reuse; never restate).
8. `proofs/lem-prh/` ledger (skim `af export` output or `meta.json`) — the one af tree
   validated so far, as a calibration point for "af-sized".

## Binding design rules

- **Single minimal contracts** (standing bd memory, hard-won): each proposed sub-lemma
  contract is ONE minimal mathematical statement — no "hence" clauses, no corollary
  glosses, no meta-commentary about downstream composition. Compound contracts thrash
  af runs to STUCK. Consequences go in the shard body; compositions become separate
  sub-lemmas. Avoid degenerate boundary hypotheses the downstream chain does not need.
- **Envelope**: for each proposal, project the af tree size (nodes/depth) from the
  length and internal structure of the corresponding proof section. Any projection
  > ~10 nodes or depth > 3 must be factored further, now, in this design.
- **Status law**: every sub-lemma whose proof is a section of a hostile-verified
  artifact is proposed at `proved-mod-audit` with a provenance locus
  (`PROOF-…​.md §N` + verdict file). Any NEW glue statement you must introduce to make
  the DAG compose (e.g. an interface restatement) is proposed at `stated` and flagged
  LOUDLY in the risk register — it will need its own prover pass. Do NOT invent
  mathematics to fill a gap; if you find a genuine gap, record it as a
  GAP entry and leave it open.
- **Dep discipline**: `deps` edges must form a DAG that maps cleanly onto campaign
  phases 2–5 (H-CB subtree → EXT-CB subtree → Stage-1 + assembly + ledger → F0/F2/F3 +
  root). The existing parent shards (`conj-hcb`, `conj-extcb`,
  `lem-thmainext-conditional`, `lem-routef-k-ledger`) become ASSEMBLY shards whose
  `deps` are your new sub-lemmas; their contracts DO NOT change (contract changes are a
  user-escalation event).
- **Def provisioning (surface it ALL here, phase-1 mandate)**: list every definition
  each contract needs. Reuse existing `def-` ids where they exist. For missing
  vocabulary (Ha/COL-HILB layer, compressed associator, canonical corner maps, …)
  propose def shards with source loci in the pinned
  `refs/kitaev-2405.02434/approximate_algebras.tex` **where the definitions are sound**
  (definitions are citable even though the source's theorem proofs are not). For the
  Stage-1 topological inputs (Lefschetz–Hopf or whatever SPLIT-A/B/C actually consume —
  read the proof, do not guess): identify the precise external statements needed, and
  for each say whether it can be a byte-matched `cited` leaf (name a candidate
  published source for `refs/` acquisition) or must be a `consensus` def/lemma —
  this is the campaign's known failure surface; be exhaustive.

## Output (the ONLY files you create; no other repo edits, no git commands)

Write `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP.md`
containing:

1. **Proposal table** — one row per proposed shard: proposed id (`lem-hcb0-…` style,
   descriptive slugs), kind, the one-line contract VERBATIM as it would appear in the
   shard, defs (existing + proposed), deps, provenance locus (artifact §), projected
   af nodes/depth.
2. **Assembly wiring** — for each existing parent shard, the exact new `deps` list
   (and `routes` if genuinely disjunctive), demonstrating the parent's af tree
   collapses to ≤10 nodes given validated sub-lemmas.
3. **Def-provisioning list** — proposed new `def-` shards with source loci and
   proposed status (`cited` candidate vs `original`/`consensus`), plus the Stage-1
   external-input register (statement, candidate source, cited-vs-consensus call).
4. **Phase map** — which proposals belong to campaign phases 2/3/4/5 and the
   seeding order within each phase (bottom-up by deps).
5. **Risk register** — every judgment call, every `stated` glue node, every GAP,
   every place the envelope projection is uncertain.

Also write a ≤15-line `ANSWER-DESIGN.md` summary (headline counts: shards proposed,
defs proposed, glue nodes, gaps).

## Hard boundaries

- Do NOT touch `definitions/`, `argument/`, `proofs/`, `report/`, `refs/`, `runs/`,
  `.beads/`, `.frontier/`, `HANDOFF.md`, or any existing file. You create ONLY the two
  output files named above.
- Do NOT run git. Do NOT prove anything. Do NOT verify anything. Do NOT alter any
  contract of an existing shard.
- If an artifact statement looks wrong to you, transcribe faithfully and flag it in
  the risk register — a separate hostile reviewer will adjudicate.
