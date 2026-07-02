# runs/ — numerical experiment bundles (NON-rigorous evidence, L3)

**A numerical result is NEVER rigorous** (CLAUDE.md L0/L3). It is admissible only as a reproducible
*run bundle*. The `check-runs.py` gate enforces this; nothing here may be promoted up the rigour ladder
without independent byte-matched or `af`-validated backing.

## Bundle layout

```
runs/<YYYY-MM-DD>-<slug>/
  README.md            # REQUIRED — the 4 fields below + a checkable invariant
  data/                # CSV outputs (column contract in data/SCHEMA.md)
  figures/             # generated plots
```

`<slug>` is lowercase-kebab and names the *question*. The producing script lives in `scripts/` (or a
project code dir) and must write **only** under its own bundle's `data/`/`figures/`.

## Required `README.md` fields (all four, gated)

1. **Hypothesis** — the precise claim being probed (with its rigour tag; usually `numerical`).
2. **Command** — the exact, copy-pasteable re-run command line (with `--seed` where relevant).
3. **Finding** — the headline result **with honest scope limits** (e.g. "n≤8 only, no thermodynamic
   limit"). Never state a numerical finding as a theorem.
4. **Next** — the follow-up / what would make it rigorous.

Plus at least one **checkable invariant**: a certificate (e.g. exact-arithmetic SDP dual feasibility),
a known value, an independent recomputation, or a declared `residual`/`tolerance`. A number without an
invariant is not a finding.

## Numerical hygiene (mirror in `data/SCHEMA.md`)

- Prefer **exact / interval / finite-field arithmetic and boolean certificates** over floats.
- Column suffixes: `_exact` (string of the exact value), `_float` (approximation), `_residual`
  (declared normed error; denominator documented in `data/SCHEMA.md`).
- A CSV row whose first cell begins with `#` is a **sentinel comment** (caveat / supersession /
  negative-control), not data — parsers skip it.

Every bundle also gets a row in the top-level `INDEX.md` (the reverse lookup).
