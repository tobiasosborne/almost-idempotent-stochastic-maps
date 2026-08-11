<!--
ROLE: reader's map of proofs/ — what an af workspace is, what is tracked, and how to audit one.
Describes PROCESS and LAYOUT only; it asserts no mathematics. Every path below is a real path.
UPDATE POLICY: edit when the workspace layout, the tracking rules, or the audit trail change.
-->

# `proofs/` — the `af` proof workspaces (Layer 2)

One directory per registry result that has been elevated to formalisation: `proofs/<id>/` where `<id>`
is the id of a shard in `argument/lemmas/`. There are **211** such directories; **200** registry rows
carry `af: validated` in `argument/INDEX.md`, and **202** directories hold an `export.md`.

`af` is the Adversarial Proof Framework (external tool; see `GLOSSARY.md`). A workspace is an
**append-only event ledger**, not a document: the proof tree is a projection of the events.

## What is in a workspace

| Path | Tracked? | What it is |
|---|---|---|
| `ledger/NNNNNN.json` | **yes** | the append-only event log — one JSON object per event, numbered in order. 17,506 events are tracked repo-wide. This is the source of truth. |
| `externals/<hash>.json` | **yes** | one file per registered import: `name`, freeform `source`, `content_hash`. Either a byte-matched quote from `refs/`, or an import of another workspace (`proofs/<dep-id>`). |
| `meta.json` | **yes** | workspace format version. |
| `export.md`, `export.tex` | **yes** | the rendered proof tree, written by `af export` after validation. **`export.md` is the human-readable artifact** — start here. |
| `nodes/`, `defs/`, `lemmas/`, `assumptions/`, `locks/`, `.af/`, `*.lock` | no | per-command caches and claim locks, rebuildable from `ledger/`. Ignored by the repo-root `.gitignore`. |

Note: the per-workspace `.gitignore` that `af init` writes (e.g. `proofs/op-classical/.gitignore`) lists
`assumptions/` among the tracked directories, but the repo-root `.gitignore` ignores
`proofs/**/assumptions/` and no such file is tracked. The root file is the one in force.

Ledger event types, repo-wide: `nodes_claimed` 4633 · `nodes_released` 4633 · `node_created` 2883 ·
`node_validated` 2819 · `def_added` 1016 · `challenge_raised` 435 · `challenge_resolved` 428 ·
`node_amended` 381 · `proof_initialized` 211 · `node_archived` 58 · `node_unvalidated` 7 ·
`approach_tried` 2.

## The protocol, in brief

Set out in full in `CLAUDE.md` §6. The parts that make the ledger meaningful:

- The orchestrating agent **never judges a proof** and never runs `af accept` / `af challenge`. It
  dispatches workers and does bookkeeping.
- **Provers and verifiers are separate fresh external `codex` runs**; the roles never mix, and a node's
  verifier is fresh per node. A verifier is told that finding a counterexample, gap or error is a
  success — hence the 435 challenges in the record.
- Validation is **bottom-up**: a node reaches a verifier only once its live children are `validated`.
- Guardrails abort the run rather than push through: a prover-overreach guard (a prover may not dirty
  `definitions/` or `argument/`), a balloon tripwire on tree size (`scripts/af_constants.py`,
  `NODE_SOFT_CAP = 26`; the orchestrator's `--node-cap` defaults to twice that), and a stuck guard.

## How the registry and the workspaces stay in step

`scripts/argument.py` is the linker, run by `sh scripts/check-all.sh` on every commit. Two checks bind
this directory to `argument/`:

- **contract match** — the workspace root conjecture must equal the registry shard's `contract` string
  verbatim; otherwise `contract drift: <id> — af root conjecture != registry contract`
  (`scripts/argument.py:247`).
- **orphans** — every workspace directory must have a registry entry, and every shard with
  `af: seeded|validated` must have its declared workspace present (`check_orphans`,
  `scripts/argument.py:262`).

Quote provenance is gated separately by `scripts/check-refs.py`, which string-matches every claimed
verbatim external against its local `refs/` source. Current run: **1133 externals, 0 failed** — 30
checked-and-passed refs quotes, 1080 skipped as workspace-to-workspace imports, 23 skipped as
carrying no extractable quote.

## Audit recipe (about 20 minutes)

Walked end to end on 2026-08-11; the files and event ids below are the ones actually opened.

1. **Start at the root.** `proofs/op-classical/export.md` (62 lines) — five nodes, all
   `Status: validated`, `Taint: clean`. Node 1 is the theorem statement; it matches the `contract:`
   line of `argument/lemmas/op-classical.md` word for word.
2. **Follow the single import.** Node 1.1 names `lem-routef-f0-assembly`. The registered import is
   `proofs/op-classical/externals/6cfd54946b268b6d.json`, whose `source` begins `imports validated
   registry lemma proofs/lem-routef-f0-assembly` — so `check-refs.py` classifies it `skip_import` and
   the trail continues in that workspace.
3. **Descend two more hops.** `proofs/lem-routef-f0-assembly/export.md` (86 lines) imports
   `lem-routef-k-ledger`; `proofs/lem-routef-k-ledger/` registers 18 externals, among them
   `lem-routef-f2-positive-unital-compression`.
4. **Read a challenge and its resolution.** In
   `proofs/lem-routef-f2-positive-unital-compression/ledger/` (117 events):
   - `000103.json` — `challenge_raised`, `ch-a5432952230b16be`, node `1.12`, target `gap`, severity
     `major`, raised while the node was claimed by verifier `v-1_12-r5`. The objection: the root allows
     `eta = 0`, but dependency 1.6 assumes `0 < eta`, so the assembled conclusions are unsupported at
     the endpoint.
   - `000106.json` — `node_created` for a new node `1.12.1`, written by prover `pf-1_12-r6`, supplying
     the `eta = 0` endpoint argument.
   - `000107.json` — `challenge_resolved`, same `challenge_id`.
   - `000110.json` — `node_validated` for `1.12.1`, `verified_by` `v-1_12_1-r7`, a different worker
     again. Prover, challenger and validator are three distinct workers.
   (A second, independent pair in the same file: `ch-f317c020f5ab28a8`, raised `000053`, resolved
   `000062`. A longer worked example — a missing `k,n >= 1` premise, `ch-ec63f317ac865d41`, raised
   `proofs/lem-routef-prh-finish/ledger/000043.json`, node amended `000068.json`, resolved
   `000078.json` — sits one hop further along.)
5. **Check a byte-match by hand.** The same workspace registers
   `proofs/lem-routef-f2-positive-unital-compression/externals/2a397de199d7600b.json`, name
   `projection-basis-kitaev-1361`, source `refs/kitaev-2405.02434/approximate_algebras.tex:1361
   VERBATIM: "The second application of Lemma~\ref{lem_merging} …"`. Run
   `grep -n -F 'projection basis' refs/kitaev-2405.02434/approximate_algebras.tex`: the quoted text is
   line 1361 of that file, character for character. (`refs/` payloads are gitignored for copyright and
   size; `python3 scripts/fetch-refs.py --status` reports what is reconstructable, and
   `refs/manifest/checksums.sha256` pins what was matched.)

## The honest boundary

An `af`-validated tree is rung **(b)** of this repo's rigour ladder (`CLAUDE.md` L0,
`CONVENTIONS.md` §(a)): validated in an `af` workspace by the adversarial protocol. It is **not** a
Lean/mathlib proof, which is rung (c) and the top rung. **No Lean proof of anything in this repo
exists.** What the ledger certifies is that a stated tree of inferences survived fresh adversarial
verifiers who were rewarded for breaking it — not that a kernel checked it.
