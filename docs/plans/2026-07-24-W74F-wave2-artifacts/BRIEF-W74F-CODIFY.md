# BRIEF — W74F codification: transcribe the four hostile-verified wave-1 survivors into the registry (aism-zbcm)

You are a FRESH TRANSCRIPTION WORKER. Your job is **faithful codification, not proving
and not verifying**: turn the four hostile-verified W74F wave-1 results into registry
shards with honest status tags, passing every repository gate. You add NO mathematics of
your own. Fidelity to the verified artifacts is the whole job; the orchestrator will
audit your output against them line by line.

## Read first (in this order)

1. `CLAUDE.md` — the Laws (L0–L5) and rules. Binding.
2. `argument/README.md` — the registry shard schema.
3. `definitions/README.md` — the definitions shard schema.
4. The verified artifacts (your ONLY mathematical sources):
   - `docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md`
   - `docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-B-DIAGONAL.md`
   - `docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md`
   - `docs/plans/2026-07-23-W74F-artifacts/AUDIT-W74F-D-ALMOSTIDEMP.md`
   - `docs/plans/2026-07-23-W74F-artifacts/VERDICT-W74F-BATCH.md` (the batched hostile
     verdict: A·B·C·D all VALID — this is what licenses `proved-mod-audit`, and nothing
     licenses more).
5. `HANDOFF.md` § "W74-F wave 1" for framing.

## Status law (get this exactly right — the cardinal sin is overclaiming)

- A hostile-verified L5 result is **`proved-mod-audit`**, NEVER `proved` (that is
  reserved for af-validated), NEVER `cited` (these are not byte-matched published
  theorems — they are this repo's own audited proofs).
- Registered open gaps are **`conjecture`** with EMPTY `deps`.
- A source-theorem import whose printed proof was audited but not re-proved here is
  **`stated`** or **`proved-mod-audit`** exactly as the artifact's own verdict warrants —
  transcribe the artifact's honest scope, do not upgrade it.
- Conditional lemmas name their conjecture premises in BOTH the `contract` text AND
  `deps` (standing rule, HANDOFF "Standing rules").
- `af:` field: `none` for all new shards.

## The shards to create (suggested ids — adjust only to satisfy schema/lint, keep slugs
descriptive; one result per shard, ≤~200 lines each)

**(A) PRH — PRIORITY, do this first and completely before the rest.**
1. `lem-prh` — status `proved-mod-audit`. Contract: the PRH statement exactly as proved
   in PROOF-W74F-A §1: positive unital `A : ℓ∞(k)→ℓ∞(n)`, `M : ℓ∞(n)→ℓ∞(k)` with
   probability-vector rows, `‖MA−I_k‖_{∞→∞} ≤ ε < 1/2` ⟹ there is a stochastic
   idempotent `E` with `‖AM−E‖_{∞→∞} ≤ 2√(2ε)`. Constant `2√2` (the verifier settled the
   `2√2` vs `3` dispute at `2√2` — see VERDICT). Body: the construction sketch (cores,
   conditioning, exact retract `NÂ = I_k`), and the FRAMING sentence: this installs the
   reduction *op-classical ⇐ "a positive approximate retract exists"* (`‖AM−Q‖ = O(η)`,
   `‖MA−I‖ = O(η)`, `A`,`M` stochastic).
2. `lem-prh-sharpness` — status `proved-mod-audit`. Contract: the `√ε` order is
   intrinsically sharp for PRH — a family with every stochastic idempotent at distance
   `≥ √(ε/2)` from `AM` (PROOF-W74F-A §7).

**(B) Diagonal repair.**
3. `lem-kitaev-diagonal-repair` — status `proved-mod-audit`. Contract per
   PROOF-W74F-B: the printed direct-sum diagonal formula (Kitaev `tex:1254`,
   `tex:2780-2783`) is false; the finite **phase-balanced** repair yields an exact
   central diagonal of the exact algebra `ℬ` with projective norm **1, block-count-free**;
   plus (separate shard if schema demands atomicity) the entrywise CP-ization corollary.

**(C) th_main_ext decomposition.**
4. `conj-hcb` — status `conjecture`, empty deps. Contract: the H-CB contract verbatim in
   substance from DECOMP-W74F-C §3 (H-CB node): universal `C_H`, threshold `e_H`,
   uniform-in-`n` adjoint/product/homomorphism/identity-closeness estimates for
   `1_{M_n} ⊗ Ha^Q_{P,R}` under the COL-HILB identification, constants independent of
   `n`, `dim 𝒜`, block count, block dimensions.
5. `conj-extcb` — status `conjecture`, empty deps. Contract from DECOMP §3 (EXT-CB
   node): universal `C_ext`, `e_ext`; amplified `lem_extension` carried by ONE map with
   the same level-one unitary at every amplification.
6. `lem-thmainext-conditional` — status `proved-mod-audit`, deps include `conj-hcb` and
   `conj-extcb` (named in the contract too). Contract: conditional on H-CB and EXT-CB,
   `th_main_ext` holds at full amplified strength with a universal constant — the
   MAIN-CB assembly of DECOMP §3 + the corrected `tex:1551-1555` squared estimate
   (DECOMP §4) + the conditional `K`/`η_K` ledger shape (DECOMP §5).

**(D) th_almost_idemp import.**
7. `lem-kitaev-almost-idemp-audit` — status exactly what AUDIT-W74F-D's own verdict
   warrants (`proved-mod-audit` for the re-proved diagrammatic core at **10η**,
   dimension-free, after the local source fixes; `stated` for anything the audit did not
   re-prove — read its scope section carefully and split into two shards if needed).

If the schema/linter forces different id spelling or splitting, follow the schema; record
every deviation in your report.

## Definitions pass

- REUSE `def-stochastic` (stochastic idempotent — already in the registry). Do NOT
  restate it.
- New terms actually needed by the contracts (add ONLY what the contracts use as
  non-textbook vocabulary): *positive approximate retract* (project-introduced →
  `original`), *extended ε-C*-algebra*, *Ha-map*, *diagonal (of a f.d. C*-algebra)* —
  these come from the pinned local source `refs/kitaev-2405.02434/approximate_algebras.tex`
  (SHA256 `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`). Prefer
  `cited` with a byte-verbatim quote + locus that `scripts/check-refs.py --check` accepts;
  if byte-verbatim citation is not cleanly achievable, tag `original` (project
  formulation) with an honest pointer to the source locus in the body.
- BSc/MSc textbook notions (operator norm, probability vector, C*-algebra, unital map,
  completely bounded map…) are common knowledge — do NOT shard them (L2).
- **ALL new definitions get status `draft` — NEVER `locked`.** Locking requires recorded
  user sign-off (Rule 7). List every new definition in a `RATIFICATION NEEDED` section of
  your report.

## Gates (must ALL pass before you finish)

```
python3 scripts/check-defs.py --check && python3 scripts/check-defs.py --generate-index
python3 scripts/argument.py            # check + generate INDEX/DAG + frontier
python3 scripts/check-refs.py --check
python3 scripts/check-provenance.py --check
sh scripts/check-all.sh                # THE gate — must print "[check-all] OK"
```

`check-provenance` requires every new registry id to be either anchored once in the
report status ledger (`report/sections/13_discussion.tex`) or whitelisted in
`report/UNWIRED.md`. Follow the existing pattern in those files for `proved-mod-audit` /
`conjecture` entries (look at how existing non-rigorous ids are anchored). Keep any
report shard you touch ≤~200 lines (hard guard 280) and preserve its `% SHARD-…` header.
If you anchor ids in the ledger, run `cd report && make` and confirm it builds.

## Hard boundaries

- Do NOT touch: `proofs/`, `runs/`, `.beads/`, `.frontier/`, `HANDOFF.md`,
  `docs/plans/*` (except reading), `refs/`, any existing lemma shard's mathematical
  content, any existing definition.
- Do NOT run any `git` command. Do NOT commit. The orchestrator audits then commits.
- Do NOT "improve" the mathematics. If an artifact statement looks wrong to you, do NOT
  fix it — transcribe faithfully and flag it in your report's defect register.
- Do NOT promote any status above what this brief assigns.

## Output

1. The new shards under `definitions/` and `argument/lemmas/`, the regenerated
   `definitions/INDEX.md`, `argument/INDEX.md`, `argument/DAG.md`, and the minimal
   `report/` ledger/UNWIRED anchoring — nothing else.
2. A report at `docs/plans/2026-07-24-W74F-wave2-artifacts/CODIFY-W74F-REPORT.md`
   starting with `STATUS: UNAUDITED TRANSCRIPTION`, listing: every file created/edited;
   every shard id with its status and one-line contract; the `RATIFICATION NEEDED`
   definitions list; gate outputs (paste the final `[check-all] OK`); and a defect
   register (every deviation from this brief, every judgment call, everything you could
   not do).
