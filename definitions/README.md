<!--
ROLE: schema + conventions for the Definitions DB (Layer 0 — the vocabulary/types of the whole argument).
UPDATE POLICY: edit when the shard schema changes; one definition per file under definitions/<id>.md.
TRIGGER: adding/changing a definition, or changing how scripts/check-defs.py parses shards.
-->

# Definitions DB

**Priority 1.** One canonical, deduplicated shard per mathematical term. If two places define the
same concept differently, the project drifts and is sunk — so **every term is defined exactly once
here**, and `report/`, `proofs/` (af), and `theory/` *reference* a `def-<slug>` rather than restating
it. The drift/dedup gate is `scripts/check-defs.py` (run before every commit).

## Shard schema (`definitions/<id>.md`)

Flat YAML frontmatter (one `key: value` per line — no nesting), then a markdown body:

```
---
id: def-jordan-product            # def-<kebab-slug>; unique; == filename stem
term: Jordan product              # the canonical human name
aliases: ∘; symmetrized product   # semicolon-separated; alternate names/symbols (for dedup)
kind: cited                       # cited | consensus | original
status: locked                    # draft | locked
source: hos                       # source-id from refs/manifest/SOURCES.md, or "internal"
locus: joa-m.md:812 (eq. 2.17)    # where in the source the statement is matched
sha256: 28740e73d547dd46          # 16-hex prefix of the source file (cited only; "-" otherwise)
consensus: A+B; report sec:jordan # who agreed / where transcribed (required for consensus|original)
---

**Statement.** <the canonical definition, self-contained, in markdown/LaTeX-ish math>

**Notes / provenance.** <byte-match note for cited; design rationale for consensus/original;
links to related defs as [[def-...]] and to the registry lemmas that use it.>
```

### Field meaning

- **kind** — `cited`: from the literature (must byte-match a local `refs/` source).
  `consensus`: a definition the two agents agreed on (project-internal, no single external source).
  `original`: a notion introduced by this project.
- **status** — `locked` means usable downstream: for `cited`, byte-verified against the source at the
  given locus; for `consensus`/`original`, **A+B have signed off** (the consensus gate). `draft`
  means not yet gated — usable in working notes but flagged by the linker if a *validated* lemma
  depends on it.
- **source / locus / sha256** — for `cited`, `source` is a `refs/manifest/SOURCES.md` id and `sha256`
  is that source file's 16-hex prefix (checked against `refs/manifest/checksums.sha256`). For
  `consensus`/`original`, `source: internal`, `sha256: -`.
- **consensus** — required for `consensus`/`original`: a one-line record of agreement/transcription.
- **used_by** — optional; maintained by the linker (`scripts/argument.py`), not by hand.

## Rules

1. **One term, one shard.** No two shards may claim the same `term` or `alias`. `check-defs.py` fails
   on collision — that *is* the drift guard.
2. **Cited ⇒ byte-matched.** A `cited` shard's statement must be a faithful transcription of the
   source at `locus`; record the harmonised notation. The source file must exist in `refs/` with the
   recorded `sha256` (the gate warns if the gitignored payload is absent locally, fails on hash
   mismatch).
3. **Consensus-gate.** A `consensus`/`original` shard is `locked` only once both agents agree; record
   it in `consensus:`. Until then `status: draft`.
4. **Reference, never restate.** Downstream layers cite `def-<id>`; they must not paste a second copy
   of the statement (that reintroduces drift).
5. **≤ ~200 lines** per shard (they are normally ~20–40).

## Tooling

- `python3 scripts/check-defs.py --check` — dedup/collision + cited-source/hash + required-field +
  consensus-gate checks (exit ≠ 0 on failure). Part of the pre-commit suite.
- `python3 scripts/check-defs.py --generate-index` — (re)writes `definitions/INDEX.md`.

`INDEX.md` is generated — do not hand-edit.
