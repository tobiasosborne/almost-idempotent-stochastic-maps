<!--
ROLE: schema + conventions for the Argument registry (Layer 1 — the module graph / DAG of the proof).
UPDATE POLICY: edit when the registry shard schema changes; one lemma/result per file under argument/lemmas/<id>.md.
TRIGGER: adding/changing a result's contract or dependencies, or changing scripts/argument.py.
-->

# Argument registry (the module graph)

The whole argument as a **typed module system**: each result is a *module* whose **contract** is its
statement and whose **imports** are the definitions and lemmas it uses. One shard per result; the
dependency edges form a **DAG**. `scripts/argument.py` is the *linker*: it enforces the contracts
(no cycles, no drift, no dangling imports, no oversized/brittle modules) and generates the index + graph.

The proof *implementation* of each module lives in its own tiny af workspace (`proofs/<id>/`, Layer 2);
the registry **contract** is the single source of truth that the af workspace root conjecture and every
dependent's import must both match.

## Shard schema (`argument/lemmas/<id>.md`)

Flat YAML frontmatter (one `key: value` per line), then an optional markdown body:

```
---
id: lem-square-hole-almost-positive    # lem-|thm-|prop-|cor-|op-<slug>; unique; == filename stem
kind: lemma                            # lemma | proposition | theorem | corollary | open-problem | obstruction
contract: For r in A, q_r = P(r^2)-r^2 satisfies q_r >= -C·eta·||r||^2·1.   # THE statement (one line)
defs: def-spectral-idempotent; def-near-fixed-algebra; def-square-hole      # def-ids used (semicolon list)
deps: lem-P-properties                 # lemma-ids imported (semicolon list; the DAG edges)
status: stated                         # stated | proved | cited | consensus | open | obstruction | disproved (the MATH status)
af: none                               # none | seeded | validated  (formalization progress in proofs/<id>/)
provenance: theorem-B-algebraic-bridge.md:301-372 (B; A-verified v0.5 §10)
owner: B                               # A | B  (who drives the prover role by default)
workspace: proofs/lem-square-hole-almost-positive
---

<optional notes; link to the theory shard and to report label>
```

### Fields

- **kind** — the result type. `open-problem`/`obstruction` are tracked too (the frontier and the no-gos).
- **contract** — the canonical statement, ONE line. It must equal (modulo whitespace) the af workspace
  root conjecture and any dependent's import of this id. This is the anti-drift invariant.
- **defs / deps** — imports. `defs` resolve to `definitions/<id>.md`; `deps` resolve to other registry ids.
- **status** — the mathematical status. `stated` = asserted+proved in the upstream manuscript,
  transcribed faithfully here, **not yet independently verified in-repo** (the default for a transcribed
  result — this repo audits an existing paper); `proved` = a proof we have independently checked (ready
  to formalize in af); `cited` = from the literature, byte-matched to a `refs/` source; `consensus` =
  agreed project-internal; `open`/`obstruction`/`disproved` as named.
- **af** — formalization state: `none` (no workspace), `seeded` (af workspace exists, not yet validated),
  `validated` (af root is `validated`+`clean`). A lemma may be `af: validated` only if every `dep` is too.
- **owner**, **workspace** — default prover (A/B) and the `proofs/<id>/` path.

## What the linker enforces (`scripts/argument.py`)

1. **Acyclic** — `deps` form a DAG (cycle ⇒ ERROR).
2. **Imports resolve** — every `dep` is a known registry id; every `def` is a known `definitions/` id (ERROR on dangling).
3. **Contract match** — for `af != none`, the registry `contract` ≡ the af root conjecture (`af get 1 -f json`); drift ⇒ ERROR.
4. **Status propagation** — `af: validated` requires all deps `af: validated` (ERROR otherwise); computes
   the **ready frontier** (status `proved`/`consensus`, `af != validated`, all deps validated) and the **blocked** set.
5. **Brittleness** — for a workspace with node-count or depth over threshold (default >12 / depth >3),
   WARN **REFACTOR: factor into sub-lemmas** (principle 2's failure signal, made mechanical).
6. **Orphans** — registry lemma with `af != none` but missing `proofs/<id>/` ⇒ ERROR; a `proofs/*` workspace
   with no registry entry ⇒ ERROR.

Generates `argument/INDEX.md` (id · contract · status · af · owner) and `argument/DAG.md` (Mermaid),
and syncs one `bd` issue per lemma with `bd dep` edges = `deps` (so `bd ready` is the proof frontier).
INDEX/DAG are generated — do not hand-edit.

## Viewing the argument DAG

- **Whole map:** `argument/DAG.md` (a Mermaid `graph LR` of every result + its edges, each node labelled
  `id — status/af`; renders in GitHub/VS Code) and `argument/INDEX.md` (the same set as a table). Both are
  **generated** by the linker — never hand-edit.
- **Live frontier:** `python3 scripts/argument.py` prints `N results, R ready, B blocked` plus the **ready
  frontier** (results whose deps are all validated and so are next to prove).
- **One result's neighbourhood:** `python3 scripts/argument.py --show <id>` prints that result's contract,
  `defs`, direct `deps`/dependents, and the **full ancestor (all prerequisites) and descendant (all
  dependents) closures** — the local map for "what must I prove first" / "what does changing this affect".

## Tooling
- `python3 scripts/argument.py --check` — run all checks (exit ≠ 0 on ERROR). Part of the pre-commit suite.
- `python3 scripts/argument.py --generate` — (re)write `INDEX.md` + `DAG.md`.
- `python3 scripts/argument.py --show <id>` — local map (contract, deps/dependents, ancestor/descendant closures).
- `python3 scripts/argument.py --sync-beads` — mirror the registry into beads.
