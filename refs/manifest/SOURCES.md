<!--
ROLE: catalogue of ground-truth reference sources for this repo — citation, local path, role, integrity hash.
UPDATE POLICY: append a row when a source is added; never rewrite a hash without re-deriving it from the
bytes on disk. Authoritative hashes live in refs/manifest/checksums.sha256; the fetch recipe in
refs/manifest/sources.lock.json. A source is PINNED only once its bytes exist locally and a real SHA256
was computed — never fabricate a hash.
-->

# SOURCES — ground-truth reference registry

**Policy.** Every `cited` definition and every byte-verified result names a `source-id` here. The payload
under `refs/<source-id>/` is **gitignored** (copyright + size); only this catalogue, `checksums.sha256`,
and `sources.lock.json` are tracked, so provenance is auditable from a clean checkout and reconstructable
with `python3 scripts/fetch-refs.py`. A `cited` claim's quote must **byte-match** its source at the recorded
locus (`check-refs.py`); the recorded SHA256 pins the exact bytes. Verify integrity from the store root:
`cd refs && sha256sum -c manifest/checksums.sha256`.

## Source registry

| source-id | citation | locator | retrieved | local path | key file (sha256-16) | role |
|-----------|----------|---------|-----------|------------|----------------------|------|
| `baake-sumner-2007.11433` | Baake, Sumner, *On equal-input and monotone Markov matrices*, J. Appl. Probab. (2022), DOI 10.1017/apr.2021.39 | arXiv:2007.11433 [math.PR] | 2026-07-02 | `refs/baake-sumner-2007.11433/equal-fin.tex` | `f358c71c066293f8` | idempotent Markov-matrix structure — the commutative case (`op-classical` / `def-stochastic` / `thm-simplex`); arXiv e-print reproducible |
| `hognas-mukherjea` | G. Högnäs, A. Mukherjea, *Probability Measures on Semigroups*, 2nd ed., Springer 2011, ISBN 978-0-387-77548-7 | Springer (Probability and Its Applications) | 2026-06-11 | `refs/hognas-mukherjea/hognas-mukherjea-2011.pdf` (+ `.txt`) | `d74844072a1b96a2` | the δ=0 classification anchor — idempotent probability measures (Thms 1.11 / 1.12 / 1.16); copyright, cache-only |

**Provenance status (this ingest).** Both sources are FOUND-AND-PINNED: the bytes exist locally and the
recorded 16-hex prefixes are real SHA256 values computed from the on-disk files (they byte-match the
copies carried over from `almost-idempotent-positive-maps/refs/`).

- `baake-sumner-2007.11433/equal-fin.tex` — `f358c71c066293f8`. Fetch-reproducible: `sources.lock.json`
  pins it as an `arxiv-eprint-member` of arXiv `2007.11433`, so `fetch-refs.py` rebuilds and hash-verifies
  it on any clone (a wrong/hallucinated file cannot match the official arXiv source, so the hash-match
  independently certifies genuineness).
- `hognas-mukherjea` — `.pdf` `d74844072a1b96a2`, `.txt` `ac5e74eb1c346c24`. **Cache-only** (copyrighted;
  no public reproducible source). `sources.lock.json` marks both files `fetch: null` with note
  "acquire manually"; restore from a content-addressed cache you control (`$EXTPROP_REFS_CACHE/<sha256>`)
  seeded once via `python3 scripts/fetch-refs.py --populate-cache <dir>`.

## hognas-mukherjea

G. Högnäs and A. Mukherjea, *Probability Measures on Semigroups: Convolution Products, Random Walks, and
Random Matrices*, 2nd ed., Springer Probability and Its Applications, 2011. ISBN 978-0-387-77548-7. **The
δ=0 anchor's proof source**: the structure theorem for idempotent probability measures (§2.2, "Invariant
and Idempotent Probability Measures"; Thms 1.11/1.12/1.16) — the result Baake–Sumner
(`baake-sumner-2007.11433`) cite without proof for the classification of idempotent Markov matrices.
Acquired by the user (2026-06-11, personal download). Files: `hognas-mukherjea-2011.pdf` (user-supplied) +
`hognas-mukherjea-2011.txt` (local `pdftotext -layout` extraction — greppable loci; byte-quote against the
`.txt`). Cache-only (copyrighted; no public fetch).
