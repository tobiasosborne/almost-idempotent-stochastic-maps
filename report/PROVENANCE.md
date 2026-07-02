# PROVENANCE — report audit ledger

**Policy.** Every Definition and Theorem reproduced in the report (`sections/*.tex`) must have an
entry in the per-claim ledger. An entry records: (1) the report label; (2) the ground-truth source
(a `## Ground-truth source registry` key → path + SHA256-16); (3) the source/internal-proof locus the
statement is matched to; (4) any harmonisation applied. "Provenanced" = a faithful
transcription/derivation of registered source material, or an internal project statement tied to a
hashed proof/consensus file. Results original to this project are marked `ORIGINAL`.

Verify a hash with: `sha256sum "<path>" | cut -c1-16`.

> **Day 1.** The registry and ledger below are EMPTY by design — the report (`report/main.tex`)
> reproduces no result until its `argument/` shard exists and a row here binds it to a source. The
> `check-provenance` gate keys off the two `##` headers below and parses an empty table to zero rows
> (green).

## Ground-truth source registry

| Key | Path | SHA256 (16) | What it is |
|-----|------|-------------|------------|

## Per-claim ledger

Status column: **V** = byte-verified against the registered local source; **I** = inline-provenanced
(source+locus in a `% PROV:` comment), awaiting byte-check; **O** = ORIGINAL/internal result tied to a
hashed file; **OPEN** = project target/conjectural, not a proved theorem; **HEURISTIC** = perturbative/
field-theory argument (NON-rigorous); **NUMERICAL** = supported only by a `runs/` bundle (NON-rigorous);
**EXTRACT** = supported by a hashed extraction, not yet byte-matched; **PDF** = PDF not yet text-verified.

| Report label | Source | Loc. | Status | Note |
|--------------|--------|------|--------|------|
