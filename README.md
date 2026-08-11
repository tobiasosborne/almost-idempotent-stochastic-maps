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
| `assets/site.css` | The design system: palette tokens (validated for colourblind safety), typography, status chips, layout primitives. |
| `assets/site.js` | Shared shell: three-state theme toggle, JSON loading with the `file://` notice, escaping helpers, the rigour-rung → badge mapping. |
| `assets/theorem.js`, `assets/defense.js`, `assets/atlas.js` | One module per page (classic scripts; `file://` blocks ES modules). |

Nav entries for **Replay**, **Ledger**, **Lexicon**, and **Evidence** are deliberately disabled
placeholders — those are Phase 3/4 of the plan.

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
the HTML. On `defense.html` this is a hard rule: not one count on that page is a literal in the source,
so a future regeneration cannot leave it stale.

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
- The Atlas uses a deterministic longest-path layering rather than a force simulation — reproducible,
  instant, and dependency-free, at the cost of a wide canvas (≈2600×1000 units, aspect 2.6:1 for the
  current 374 nodes). The default view fits the whole graph, which makes individual nodes small;
  pan/zoom is the intended way to read it, and node labels appear once you zoom past 1.5×.
- **Footer links into the repository** (`../paper/main.tex`, `../report/main.pdf`, `../GLOSSARY.md`,
  `../proofs/README.md`, `../llms.txt`, `../argument/…`) assume the **repository root** is what gets
  served — true for a local clone and for Pages serving the branch root. If hosting is ever flipped to
  serve `site/` *as* the web root, those five relative links must be repointed at the GitHub blob URLs
  (the Atlas's "audit deeper" links already use absolute `github.com` URLs and are unaffected).

## Honesty rules this site is built under (L0)

- Every status shown is the registry's own `status` / `af` field, never a rounded-up paraphrase.
- The rung reached is **af-validated**, and each page says so explicitly. There is **no Lean/mathlib
  proof**, nothing here is peer-reviewed or published, and the constant `C` is not explicit.
- Numerical results are evidence, never proof, wherever they appear.
