# Device-migration notes — what to reconstruct on a fresh clone (2026-07-26)

Written at the session-26 close for the next agent picking this repo up on a
different device. Everything mathematical/process-canonical is in git (pushed
through session 26); the items below are the gitignored/untracked local state
that does NOT travel and how to rebuild each. Nothing else on the old machine
is needed — all session artifacts that matter were landed
(`docs/plans/2026-07-24-fudw-decomposition-artifacts/`,
`docs/plans/2026-07-25-report-wave3-artifacts/`, `report/`, `proofs/*/ledger`).

## 1. `refs/` payloads (gitignored; manifest tracked)

Reconstruct with the standard tooling — no manual work:

```bash
python3 scripts/fetch-refs.py            # fetch everything fetchable
python3 scripts/fetch-refs.py --status   # verify: present=11 expected
cd refs && sha256sum -c manifest/checksums.sha256
```

All 11 manifest payloads were present and byte-verified on the old device.

## 2. `refs-staging/` (untracked scratch; copyrighted PDFs — NEVER commit payloads)

The acquisition log `refs-staging/ACQUIRED.md` is untracked and would be lost;
a verbatim snapshot is committed as
**`docs/plans/2026-07-26-refs-staging-ACQUIRED-snapshot.md`** — it contains,
for every item, the exact source URL, filename, SHA256, size, and an
extraction-check phrase. To rebuild: `mkdir refs-staging`, copy the snapshot
back to `refs-staging/ACQUIRED.md`, then re-download each **acquired** item
from its recorded URL and check `sha256sum` against the recorded hash
(re-extract .txt with `pdftotext`). Priority items (the Stage-1 topology
sources, session 26, log items 9–13):

| item | file | source | sha256 (16) |
|---|---|---|---|
| Hatcher, *Algebraic Topology* | `hatcher-algebraic-topology/AT.pdf` | https://pi.math.cornell.edu/~hatcher/AT/AT.pdf | `bebb3032bf90…` (full hash in snapshot) |
| Cairns 1935 (triangulation, Bull. AMS 41) | `cairns-triangulation-1935.pdf` | AMS open journal archive (URL in snapshot) | `2b36c50098bf…` |
| Arkowitz–Brown 2004 (Lefschetz–Hopf, OA) | `arkowitz-brown-lefschetz-hopf-2004.pdf` | OA journal (URL in snapshot) | `63da10be018c…` |

The older items (ando, chakraborty-rao, douglas, flor, hoffman, luo-pang,
meyer) have their URLs/hashes in the same snapshot; re-download only when a
task actually needs them. **FAILED items (do NOT chase mirrors — user
escalation, purchase/institutional only): Lee, *Introduction to Smooth
Manifolds* (Thm 21.10) and Granas–Dugundji, *Fixed Point Theory*.** Whitehead
1940 is JSTOR-gated; Cairns is the chosen open substitute. Standing user
directive: **legal open access only** (recorded in HANDOFF directive ix).
Locus flag for the design owner: in the canonical Hatcher PDF the Künneth
cross-product theorem is numbered **3.15** (design says 3.16) and the
top-cohomology citation should be **Cor 3.39**.

## 3. `proofs/<id>/` gitignored caches (`nodes/`, `locks/`, …)

Nothing to do: only `ledger/` + `externals/` + `meta.json` are canonical
(tracked); the `af` binary rebuilds its caches from the ledger on first use.
Do NOT `git rm`+reseed a workspace — if a re-seed is ever needed, `rm -rf`
the WHOLE directory first (bd memory: leftover gitignored caches make
`af init` fail with a ledger sequence-gap error).

## 4. `report/.build/` and `report/main.pdf`

Rebuild with `cd report && make` (or let `check-all`'s provenance `--build`
step do it). Note: the first `check-all` run after fresh .tex changes can
fail transiently at `check-provenance` while latexmk's incremental state
settles — rerun once before diagnosing.

## 5. Beads (Dolt DB)

`bd dolt pull` on the new device (the JSONL mirror `.beads/issues.jsonl` is
tracked and current through session 26; `bd import` from it if the Dolt
remote is unavailable).

## 6. Scratchpad

Device-local and fully harvested — nothing to recover. The review-evidence
chain for the report waves (briefs, hostile verdicts, change logs, WIRING,
AUTHOR-NOTES, landing report) is landed at
`docs/plans/2026-07-25-report-wave3-artifacts/`.

## Where to start

`HANDOFF.md` (current through session 26) → sketch v33 via
`docs/plans/CURRENT.md` → `bd ready`. The frontier is the user-gated edge:
(i) v4.1 def sign-offs (20), (ii) the two paywalled refs above,
(iii) the GAP-EA contract-form decision (`aism-fbh8` — the validated
conj-extcb node-1.2 subtree is the discharge candidate).
