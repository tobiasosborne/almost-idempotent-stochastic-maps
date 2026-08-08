<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v48** (current).
3. **Rigorous (af-validated, T0): 190.** Registry: **367**. `op-classical` OPEN.
4. **SESSION-44 RECORD (2026-08-08, W137): THE LEDGER-DOMAINS QUEUE IS
   COMPLETE.** Fourteen banks in one session (T0 176 → 190), closing bead
   `aism-3fjg`:

   | T0 | row | tree | note |
   |---|---|---|---|
   | 177 | row 5 `lem-routef-delta-prime-closeness` | 15/15 | after TWO user-ratified deps repairs (see §5) |
   | 178 | row 6 `lem-routef-delta-normalization-closeness` | 6/6 | first pass, on projection |
   | 179 | D2 `lem-routef-degree-two-estimate` | 7/7 | first pass |
   | 180 | row 7 `lem-routef-delta-phi-product` | 7/7 | first pass |
   | 181 | D3 `lem-routef-degree-three-estimate` | 15/15 | first pass |
   | 182 | `lem-routef-upsilon-prime-component-construction` | 23/23 | NEW row (ROW8-FACTOR) |
   | 183 | `lem-routef-upsilon-prime-left-inverse` | 14/14 | NEW row (ROW8-FACTOR) |
   | 184 | row 8 `lem-routef-upsilon-prime-closeness` | 11/11 | byte-frozen contract, factored |
   | 185 | row 9 `lem-routef-upsilon-normalization-closeness` | 21/21 | first pass |
   | 186 | row 10 `lem-routef-delta-upsilon-telescope` | 4/4 | after fresh-prover re-seed (STUCK run 1) |
   | 187 | row 11 `lem-routef-multiplicative-telescope` | 7/7 | first pass |
   | 188 | row 12 `lem-routef-upsilon-delta-telescope` | 13/13 | first pass |
   | 189 | row 13 `lem-routef-k-finiteness` | 18/18 | first pass |
   | 190 | row 14 `lem-routef-threshold-minimum` | 5/5 | revised scalar contract; QUEUE COMPLETE |

   **The entire re-scoped family is T0** (formation + rows 1–14 + D2 + D3 +
   the two factoring sub-lemmas = 19 rows): the scalar ledger (1.1)–(1.8)
   is rigorously grounded and K, eta_K are rigorously finite, positive,
   dimension-free. Every bank: fresh codex prover, separate fresh verifier
   per node, oracle registered (inserted before the
   `af-lem-thmainext-conditional` anchor in `.frontier/portfolio.json`
   config.oracles — a LIST of dicts), external `fr verify` PASS, mechanical
   flip, `check-all` OK, committed.

5. **The two ratified registry deltas of this session:**
   - Row 5 `deps:` += `lem-kitaev-diagonal-repair` AND
     `lem-routef-ai-defect-linearization` (verifier-caught rescope
     oversights: the diagonal facts and the inherited-involution
     identification; contract bytes unchanged; user-ratified 2026-08-08,
     dated provenance notes in the shard).
   - **ROW8-FACTOR** (registry 365 → 367): row 8's honest tree (~29 nodes)
     exceeded NODE_SOFT_CAP 26 → fresh-codex design + SEPARATE fresh
     hostile audit (VERDICT: LAND, zero corrections) + user ratification →
     two new sub-lemma rows landed verbatim + main deps extended (contract
     SHA-verified unchanged). Artifacts:
     `docs/plans/2026-08-08-ROW8-FACTOR/` (BRIEF/DESIGN/AUDIT/TREE dump).
   - Two NEW reusable byte-matched GT externals:
     `GT-kitaev-fd-cstar-structure` (tex:257, fd C*-algebra = direct sum of
     full matrix algebras) and `GT-kitaev-canonical-stinespring`
     (tex:1621-1634). Register these wherever a workspace needs the
     structure theorem or Stinespring — do NOT let provers re-derive them.

6. **NEXT SESSION, ranked:**
   1. **F0-assembly landing + the strengthened `lem-routef-k-ledger`
      replacement** (W78 §5 step 6; releases the DO-NOT-REWIRE guard).
      BINDING constraints: the strengthened parent adds the formation row
      AND rows 5/6/8/9 as direct deps (the telescopes don't export packet
      existence); honest budget ~17 nodes / 4 rounds / cap 22. NEW note:
      row 8 now factors through the two sub-lemmas — where the design needs
      construction data (the componentwise package), import
      `lem-routef-upsilon-prime-component-construction` directly. Needs its
      own fresh design + fresh hostile audit + user ratification (it
      REPLACES a landed contract).
   2. **Root rewire LAST** (unchanged).
   3. `aism-9kmt` report sync (unanchored banks now ~120–190 + the family;
      all whitelisted in `report/UNWIRED.md`).
   4. Cross-device beads decision (aism-l4uw / aism-ccso live only on the
      Hannover device; substance is in FINDINGS.md).

7. **Worked-pattern deltas learned this session (BINDING; also in
   FINDINGS.md 2026-08-08):**
   - **Never resume an af run across a registry ratification** — the
     workers judge external allowedness from the CHECKOUT's `deps:` line;
     recreate the worktree at the new HEAD (clean re-seed if polluted).
   - **STUCK + ordering/bookkeeping challenges = build-shape pathology** →
     fresh-prover clean re-seed with identical provisioning (row 10:
     26-node 5-deep thrash → 4/4 first pass). Distinct from the balloon
     signature (missing fact → provision a byte-matched GT external).
   - **Audit briefs must enumerate silently-invoked textbook theorems**
     (Wedderburn/Stinespring cost a 37-node balloon before provisioning).
   - Elevation cadence per row: seed+provision (commit) → fresh worktree →
     ONE backgrounded `af-orchestrate.py` call (workers 4, tier routine,
     cap 26 unless a design says lower) → on validation: rsync back, remove
     worktree, export md+tex, oracle insert, `fr verify`, mechanical flip,
     regenerate (`argument.py --generate`, `gen-report-dag.py`,
     `gen-report-defs.py --generate --dag-anchors`,
     `gen-report-stats.py --extract`), `check-all`, `fr log banked`, commit.

8. **Open beads:** `aism-3fjg` CLOSED this session (queue complete).
   `aism-wazy` (P1 tripwire), `aism-9kmt` (P2 report sync, updated),
   `aism-xjnc` (P3 CHANGELOG stale). Carried P1 items unchanged.

9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).
   All work committed AND pushed. **NOTHING is in flight** (no af runs, no
   codex, no worktrees; all elevation worktrees removed after banking).

## Next steps (ranked)

1. F0-assembly landing + strengthened K-ledger replacement (guard release):
   design → hostile audit → user ratification → land → elevate.
2. Root rewire LAST.
3. `aism-9kmt` report sync.
4. Cross-device beads decision.

## What is intentionally NOT here

- Any claim `op-classical` is proved — **OPEN**. T0 = 190.
- Any claim the 14 banks are new mathematics: they re-establish the
  twice-audited LEDGER-DOMAINS design at T0 under the honestly re-scoped
  contracts (with the row-8 factoring the only structural novelty, itself
  design+audit+ratification-gated).
- The `lem-routef-k-ledger` parent rewire (guard still ON until the
  strengthened replacement lands).
- Report anchoring of the new banks (carried in `aism-9kmt`).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
