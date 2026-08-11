<!--
ROLE: what site/ is, how it is generated, how to view it, and which deviations from the ratified
  plan the current build carries.
UPDATE POLICY: edited in lockstep with the site itself (Rule 9).
-->

# `site/` — the Glass-Box Lab static site

The public communication layer of this repository: a **static, self-contained, zero-build** site that
publishes the theorem, the epistemic machinery behind it, and the whole knowledge DAG — with every
number generated from the canonical record rather than typed by hand. It implements Phase 2 of
`docs/plans/2026-08-11-communication-artifacts-plan.md` ("The Glass-Box Lab").

No CDN, no framework, no bundler, no CI. Vanilla HTML + CSS + JS, served as files. It works from any
static server and from GitHub Pages (Rule 12: no Actions).

## Pages

| File | What it is |
|---|---|
| `index.html` | **The Theorem** — the `op-classical` statement, its status chips read from the registry, the live 4×4 sharpness witness (slider over λ, the matrix, η/floor/achieved readouts, and the δ–η chart with the forbidden region), the non-explicit-constant story, and the two-panel *what is proved / what is not*. |
| `defense.html` | **The Swiss-Cheese Defense** (the headline page) — six error-catching layers with live counts, the schematic with two real error trajectories, the retraction ledger as dated cards, the honest af-vs-Lean paragraph, and the protocol explainer. |
| `atlas.html` | **Proof Atlas** — all registry nodes and edges as an interactive DAG: rigour-rung colours, status filters, route lenses, pan/zoom, and a side panel with the verbatim one-line contract plus a link to the exported af tree for validated results. |
| `replay.html` | **Campaign Replay** — the append-only explore/exploit record: the af-validated (T0) count over the whole campaign as a line chart with every *decrease* marked (de-bankings — retractions, and the point of the page), plus the full log as a filterable, searchable, paginated explorer (outcome · arm · free text; rows expand to the complete note). |
| `ledger.html` | **The Honesty Ledger** — every retracted claim as a dated card (what was claimed, why it was wrong, which layer caught it, how it was resolved), followed by a prose section on **dead routes**: the death certificates live in `FINDINGS.md` and are deliberately not parsed into data; the seven inherited families barred by `CLAUDE.md` Rule 13 are listed as static cards. |
| `lexicon.html` | **The Lexicon** — the canonical definition shards, searchable over term/alias/id and filterable by provenance and lock status, each body shown as the shard's own source text. Below it, the process glossary reproduced as a *list of term names* linking to `GLOSSARY.md` — one canonical source per term, so the bodies are not duplicated. |
| `evidence.html` | **The Evidence Layer** — every run bundle as a sortable, searchable table (date · bundle · headline finding), each row linking to its README in the repository, under a permanent **“evidence, never proof (L3)”** banner. |
| `assets/site.css` | The design system: palette tokens (validated for colourblind safety), typography, status chips, layout primitives, and the shared page components (toolbars, chart chrome, log rows, cards, tables). |
| `assets/site.js` | Shared shell: three-state theme toggle, JSON loading with the `file://` notice, escaping helpers, the rigour-rung → badge mapping. |
| `assets/theorem.js`, `assets/defense.js`, `assets/atlas.js`, `assets/replay.js`, `assets/ledger.js`, `assets/lexicon.js`, `assets/evidence.js` | One module per page (classic scripts; `file://` blocks ES modules). |

All seven nav entries are live.

## Where the numbers come from

`site/data/*.json` is a **generated layer**, not hand-maintained:

```bash
python3 scripts/gen-site-data.py --generate   # rebuild site/data/*.json from the canonical record
python3 scripts/check-site.py --check         # freshness gate (wired into scripts/check-all.sh)
```

The gate re-derives the data from `argument/`, the `proofs/*/ledger/` event files, `docs/LEARNINGS.md`,
`runs/`, `refs/`, `definitions/`, and `.frontier/log.jsonl`, and fails the commit if the committed JSON
differs. So a registry change that is not regenerated **blocks the commit** rather than letting a page
publish a count the repository no longer supports (plan principle P1).

Every page fetches those files at runtime with relative paths (`data/*.json`) — nothing is baked into
the HTML. On `defense.html` this is a hard rule: the counts on that page are runtime-rendered from
the data layer (the only literals are structural words like "six layers"), so a future regeneration
cannot leave it stale.

**Prose is reviewed; numbers are machine-generated.** The narrative text on each page is human-written
and independently reviewed (Rule 3 / L5); every count, status chip, and contract string is rendered from
the JSON at load time.

## Viewing it locally

```bash
python3 -m http.server 8000 -d site     # from the repository root
# or:  cd site && python3 -m http.server 8000
```

then open <http://localhost:8000/>.

Opening `site/index.html` directly as a `file://` URL will render the shell but **not** the data:
browsers block `fetch` for `file://` origins. The pages detect that and show an inline notice telling
you to run the command above — no silent blank sections.

## Known deviations from the ratified plan (MVP)

- **No KaTeX.** The plan calls for vendored KaTeX; this build renders mathematics as HTML + Unicode
  (`‖Q²−Q‖<sub>∞→∞</sub>`, `√(η/2)`, `λ`) instead. Deliberate MVP choice: it keeps the site to three
  small text assets with zero vendored third-party code, and the statements on these three pages are
  short enough to typeset legibly without a layout engine. Revisit when a page needs displayed,
  multi-line mathematics (the drill-down pages of Phase 3 are the likely trigger).
- **No δ–H scatter on `evidence.html` (follow-up).** The plan's slate I calls for an interactive
  δ–H scatter over the certified instance record; this build ships the bundle table only. The scatter
  needs the *per-instance* data lifted into `site/data/` by `gen-site-data.py` (today the generator
  carries only each bundle's date, slug, title, and headline excerpt), and plotting it from summary
  prose would be precisely the number-without-provenance this project refuses. Follow-up work:
  export the instance records, then add the scatter under the same L3 banner.
- **The T0 timeline is a parse, and says so.** `replay.html` charts `t0_timeline`, which the generator
  recovers from free-text wave notes (liberal match on the last T0 count mentioned). The generator's own
  caveat is printed under the chart verbatim. The *decreases* are real de-bankings, cross-checked against
  the retraction ledger; the exact horizontal position of a point is only as good as the note it came from.
- **`GLOSSARY.md` term names are transcribed onto `lexicon.html`.** Its entries are bold terms inside one
  file rather than headings, so there are no anchors to link to; the list carries names only (19 at the
  time of writing) and every link points at the file. If the glossary gains an entry, the list is merely
  short — it never misstates what an entry *says*, because it does not reproduce any body.
- The Atlas uses a deterministic longest-path layering rather than a force simulation — reproducible,
  instant, and dependency-free, at the cost of a wide canvas (≈2600×1000 units, aspect 2.6:1 for the
  current 374 nodes). The default view fits the whole graph, which makes individual nodes small;
  pan/zoom is the intended way to read it, and node labels appear once you zoom past 1.5×.
- **Links into the repository** (`paper/main.tex`, `report/main.pdf`, `GLOSSARY.md`,
  `proofs/README.md`, `llms.txt`, `FINDINGS.md`, `docs/LEARNINGS.md`, `argument/…`) are **absolute
  GitHub URLs** on every page — there are no repo-relative (`../`) links left, so the site renders
  correctly whether it is served from the repository root or with `site/` *as* the web root.
- **Still deferred from the plan.** Per-result drill-down pages and stable per-result anchors
  (slates D and J), site-wide hover-cards (slate H), and hash deep-linking into the Atlas
  (`#<node-id>` selecting a node) are not built. The plan's `argument.py --emit-json` step was
  superseded by `scripts/gen-site-data.py`, which generates the whole `site/data/` layer instead.

## Honesty rules this site is built under (L0)

- Every status shown is the registry's own `status` / `af` field, never a rounded-up paraphrase.
- The rung reached is **af-validated**, and each page says so explicitly. There is **no Lean/mathlib
  proof**, nothing here is peer-reviewed or published, and the constant `C` is not explicit.
- Numerical results are evidence, never proof, wherever they appear.
- `sh scripts/check-all.sh` is green from a fresh clone through every gate except the byte-match step:
  the `refs/` source payloads are gitignored (copyright), so `check-refs` reports their quotes as
  unverifiable until you supply them (`python3 scripts/fetch-refs.py --status` lists which of the 23
  are auto-fetchable and which must be obtained manually).

## Deployment

Hosted at <https://tobiasosborne.github.io/almost-idempotent-stochastic-maps/> — GitHub Pages serving
the `gh-pages` branch (legacy build, no Actions). `gh-pages` is a mirror of this directory, produced by

```sh
git subtree split --prefix=site -b gh-pages-tmp
git push -f origin gh-pages-tmp:gh-pages
git branch -D gh-pages-tmp
```

Re-run those three commands after any `site/` change lands on master (a deliberate local step — this
repo runs no CI by policy, CLAUDE.md Rule 12).
