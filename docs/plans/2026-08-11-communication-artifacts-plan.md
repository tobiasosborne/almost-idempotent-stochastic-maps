# Communication-artifacts plan — "The Glass-Box Lab" (RATIFIED 2026-08-11)

Epic: `aism-xvcq` (shareability campaign, Phase-2 design). User-ratified 2026-08-11 in-session.
Rendered proposal (design treatment + working sharpness-witness demo):
https://claude.ai/code/artifact/6d0be821-6f3d-4780-b65d-d546b30989b2

## Thesis

The repo's communication layer is rebuilt as an interactive, provenance-first scientific
artifact — NOT a PDF with a repo attached. The headline claim is the epistemology itself:
a **Swiss-cheese formalisation** — six independent error-catching layers, each with known
holes, whose composition caught every error found so far (quantified below, from the record).
In a world of unlimited plausible LLM mathematics, the scarce resource is checkable
provenance; the site exposes the whole epistemic machine.

## The Swiss-Cheese Defense — quantified (HEADLINE, core deliverable)

User mandate 2026-08-11: this is *more than a plain Lean formalisation* — the formalisation is
composed of many levels, each with holes, which under composition catch independent errors.
Measured record (repo at HEAD b171edd2, campaign 2026-07-02 → 2026-08-09):

> **CORRECTION (2026-08-11, same day, by the Phase-1 data layer — truth-from-canon working as
> designed):** four figures below were wrong when written and are superseded by
> `site/data/defense.json` / `stats.json`: retractions are **7** (the "8th" was the entry
> template inside an HTML comment); run bundles are **38**; "1,133 quotes byte-matched" is a
> mis-read — the 1,133 externals split as **30 byte-matched literature quotes + 1,080
> workspace dep-imports + 23 no-quote**; and "1,016 byte-matched imports" was the ledger
> `def_added` **event** count, not an import count. Downstream surfaces read the JSON, never
> this prose.

| Layer | Error class targeted | Measured record | Known holes |
|---|---|---|---|
| L1 vocabulary & provenance | hallucinated citations; definition drift | 47 canonical def shards (drift = build failure); 23 SHA256-pinned sources; 1,133 quotes byte-matched per commit; 1,016 byte-matched imports in proof workspaces | says nothing about proof correctness |
| L2 contract DAG + linker | contract mismatch; circularity; rigour resting on non-rigour | 374 one-line contracts / 860 edges, acyclicity + contract-match + status propagation per commit; propagation law mechanically suspended 2 banked results (M18/M20, 2026-08-01); one-line-contract bar stripped 15 overclaimed inherited rows (2026-07-26) | cannot read proof bodies |
| L3 hostile review (reviewer ≠ author) | plausible-but-wrong paper proofs | W56 closed whole route families; demoted the "Route F complete" headline; produced the ex-hume counterexample | batched review misses corners (documented: the empty-N corner) |
| L4 af adversarial trees | in-proof gaps; silent assumptions; unregistered premises | 202 validated workspaces; 2,819 node validations by fresh verifiers (never the prover); 435 challenges raised / 428 resolved / 381 nodes amended (~1 challenge per 6.5 validations); challenge ch-9388e571 = the counterexample batched review missed | a cohort can accept an inference class a differently-framed cohort rejects |
| L5 meta-audit sweeps | the af cohorts' own blind spots | 9 af-validated certificates retracted (6 binder/anaphora, 3 unregistered-premise); same sweeps certified 14 trees sound; nothing downstream ever banked on a flawed certificate | runs only when a design round triggers re-audit |
| L6 oracles, numerics, tripwires | wishful conjectures; ballooning proofs | 3 registry claims disproved (2 oracle-verified refutations + ex-hume counterexample); 16 balloon-tripwire aborts; 39 exact-rational run bundles; 67k instances held at evidence-never-proof; 6+ death-certificated route families | refutes but cannot certify |
| backstop: retraction ledger | errors that survived N layers | 8 dated LEARNINGS entries, every one naming the layer that caught it | — |

Independence evidence (the crossings): lem-hx-financing-floor passed L3, caught at L4 (three
challenges). Nine certificates passed L4 cohorts, caught at L5 sweeps. Fifteen inherited rows
passed L3 as proved-mod-audit, fell at L2's contract bar. ex-hume survived ingest a month,
killed at L3 with an explicit counterexample. Different layers, different mechanisms — the
holes do not line up.

Honest Lean framing (front page): per-inference af < Lean; the top rung remains open. But
L1–L2 target the specification-level class a kernel never sees; L3–L6 attack the proof-level
class at four granularities with a measured catch record. Headline claim, precisely: NOT
"as strong as Lean per step" but "measured defense-in-depth across the error classes no
single formalisation covers."

## Design principles (P1–P6)

1. **Truth from canon, enforced** — every number on every surface generated from repo data
   by scripts with `--check` freshness gates wired into `check-all.sh` (the fourth generated
   layer, after report defs/dag/stats). A stale site fails the gate; overclaim = build error.
2. **Status visible everywhere** — the rigour ladder as a validated colorblind-safe badge
   system (af-validated / proved-mod-audit / numerical / conjecture / disproved), rendered
   from the registry, never hand-typed; badges always carry text.
3. **Progressive disclosure of proof** — one line → statement → sketch → af tree → verifier
   verdict lines → byte-matched reference.
4. **The process is the exhibit** — search log, dead routes, retractions as first-class pages.
5. **Two first-class readers** — humans AND agents (`llms.txt`, stable JSON of DAG +
   provenance + defense counts, stable per-result anchors).
6. **Self-contained, zero-build** — static HTML, vendored KaTeX, no CDN, no framework, no CI
   (Rule 12 intact); readers verify with stdlib `check-all.sh` alone.

## Artifact slate (A–J)

- **A README** — rewrite; leads with theorem + status chips + honest boundary; three entry
  routes; links sibling `aic_stoch` as "run it yourself". Fixes survey defect #1. Reviewer ≠
  author on status claims.
- **B The Theorem** — explorable statement; live 4×4 sharpness-witness slider
  (`lem-prh-sharpness` family: η = 2λ², floor √(η/2), achieved √(2η), forbidden region);
  the non-explicit-constant story (C = K+4√(2K), C ≥ 6.657); proved/not-proved panel.
- **C Proof Atlas** — zoomable/filterable 374-node DAG; preset lenses: 156-node Route-F
  closure (default), 44-node legacy route, 3-lemma sharpness island. Source:
  `argument.py --emit-json` (new flag).
- **D Provenance drill-down** — per-result page: contract + export.md + ledger verdict lines
  + byte-match rows; "audit this theorem in 20 minutes" trail.
- **E Campaign Replay** — 1,287-entry `.frontier/log.jsonl` as scrubbable timeline; T0-over-
  sessions chart with the de-banking dip visible.
- **F Honesty Ledger** — LEARNINGS + FINDINGS death certificates as browsable dated cards.
- **G The Defense** — THE HEADLINE PAGE (ranked with B): the six layers with live counts
  regenerated from ledgers per commit; error-trajectory walkthroughs; each retraction linked
  to its ledger entry + catching layer; protocol explainer (fresh prover ≠ fresh verifier ≠
  orchestrator-never-judges); links to the public `af` (github.com/tobiasosborne/vibefeld)
  and `fr` repos.
- **H Lexicon** — 47 defs as dependency-ordered hypertext (reuse `report/generated/defs`
  ordering); NEW GLOSSARY.md (T0, af, fr, banking, waves, arms, rigour rungs); site-wide
  hover-cards.
- **I Evidence Layer** — 39 run bundles browsable; interactive δ–H scatter; every view
  bannered "evidence, never proof" (L3); re-run commands + SHA256s beside figures.
- **J Machine Layer** — `llms.txt` + `site/data/*.json` (DAG, statuses, contracts,
  provenance, retractions, runs, defense counts) + stable anchors.

## Architecture

Canonical repo → stdlib-Python generators (`gen-site-data.py`, `gen-site.py`,
`check-site.py --check` wired into `check-all.sh`) → `site/` static+committed (self-contained
HTML, vendored KaTeX, vanilla JS) → GitHub Pages served from the branch (no Actions) +
opened-locally-from-clone. Visual identity: iron-gall-indigo archival palette, Palatino
(mathpazo lineage) display/body, mono contracts; status palette validated (dataviz
six-checks, light + dark).

## Phases

0. **Hygiene — make every existing surface true** (1 session): survey defects 1–3 & 6
   (stale counters incl. PROVENANCE "112"→200, INDEX.md past W25, SCHEMA gaps, path
   fallbacks `/home/tobias/…`, wire the missing test); rebuild `paper/main.pdf`; triage the
   ~45 superseded beads. No user input needed.
1. **Data layer** (1 session): JSON exporters + parsers (LEARNINGS/FINDINGS/log/runs/ledger
   challenge counts); `llms.txt`; the `check-site` gate. (Slate J.)
2. **Front door + core** (1–2 sessions): README (A, independently reviewed); site shell +
   design system; Theorem page (B); **Defense headline page (G)**; Proof Atlas MVP (C).
3. **Story layers** (1–2 sessions): Replay (E); Honesty Ledger (F); Lexicon (H); drill-down
   + audit trail (D); Defense walkthrough animations (G cont.).
4. **Evidence + polish** (1 session): runs explorer (I); a11y/perf pass; sibling cross-links;
   hosting flip; final review wave.

Per phase: reviewer ≠ author on content-bearing text (Rule 3); `check-all.sh` green per
commit; one atomic step per commit; `fr` log per wave.

## Ratified decisions (user, 2026-08-11)

1. **Venue/hosting:** public GitHub repo + GitHub Pages (committed `site/`, no Actions) +
   arXiv eventually. YES.
2. **Honesty prominence:** front page — folded into the Defense headline. YES.
3. **Tooling:** `af` and `fr` are BOTH public GitHub repos of the author (correcting the
   survey's "unshippable" premise) — link + document install on the Defense page; verify
   path stays stdlib-only. (`af` = github.com/tobiasosborne/vibefeld; `fr` repo link to be
   wired in Phase 2.)
4. **Site residence:** in-repo `site/`, lockstep with gates (Rule 9). YES.
