Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, OR PROMOTE —
pending focused fresh hostile re-audit and user ratification.

# ADDENDUM v3 — closing AUDIT-EXHUME-SHARPNESS-V2 finding 1 (the 51st locus)

Author: Claude (orchestrator), as a MECHANICAL transcription of the v2
re-audit's prescribed repair (AUDIT-EXHUME-SHARPNESS-V2.md finding 1).
Everything in DESIGN-EXHUME-SHARPNESS-V2.md is carried forward VERBATIM;
this addendum ONLY adds the omitted locus and its exact repair text. A
separate fresh hostile re-audit adjudicates this addendum before any
ratification.

## The omitted locus (finding 1)

`definitions/def-near-positive-projection.md:24-25` (a `locked`,
`consensus` definition shard) actively asserts: "; the $\sqrt{}$ exponent
is sharp (Hume's $3\times3$ family)." — attributing sharpness to the
about-to-be-retracted `ex-hume` family, with the uncitable eponym, in
unqualified active prose. Its generated twin
`report/generated/defs/layer-1-classical-picture.tex:448-449` repeats it.

## Exact repair (locus 51)

In `definitions/def-near-positive-projection.md`, replace (old string,
byte-exact including punctuation):

```
unital idempotent — a [[def-stochastic|stochastic idempotent]] $E$; the $\sqrt{}$ exponent is sharp
(Hume's $3\times3$ family).
```

with:

```
unital idempotent — a [[def-stochastic|stochastic idempotent]] $E$. In the *stochastic-defect*
formulation this is `op-classical` (af-validated 2026-08-08), and sharpness of the
$\sqrt{}$ exponent in the stochastic parameter $\eta$ is the registry row
`cor-classical-sharpness` (see its shard for status). In the *signed* parameter $\delta$
used by THIS definition, no sharpness claim is currently established at any rigorous
rung: the historical $3\times3$ family record (`ex-hume`) is `disproved` as literally
stated, and its corrected distance-to-set statement remains an unproved candidate.
```

Constraints honoured (per the v2 audit's finding-1 text):
- the eponym leaves active prose;
- `cor-classical-sharpness` (an $\eta$-parameter statement) is NOT
  substituted as a certificate for the $\delta$-parameter claim — the
  $\delta$-side is explicitly stated as unestablished;
- the reference to the retraction carries its `disproved` status
  explicitly.

Mechanics: this is a change to a `locked`/`consensus` definition BODY
(the **Statement**'s trailing remark), not to the defined object, its
term, aliases, or mathematical content. Per L2/Rule 7 it still requires
recorded user sign-off; ratification of this package IS that sign-off,
to be recorded in the shard's `consensus:` line as:
`; sharpness remark corrected 2026-08-08 (user-ratified, W139 package —
AUDIT-EXHUME-SHARPNESS-V2 finding 1)`.
After the edit, regenerate the defs layer
(`gen-report-defs.py --dag-anchors`) so the generated twin refreshes from
source; verify `check-defs.py --check` remains green (body prose is not
drift-gated between shards, but run the gate).

## Manifest delta

DESIGN-EXHUME-SHARPNESS-V2.md's manifest gains exactly this locus (51)
plus the regeneration note above. The survivor test (v2 lines 780-786)
must be re-run at landing with the ex-hume/sharp sweep INCLUDING
`definitions/` and `report/generated/defs/` — the v2 sweep's blind spot.

Nothing else in the v2 design changes.
