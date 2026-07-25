<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (v33, the phase-3
   closure delta). **STEWARDSHIP mandate binding (Rule 9).**
3. **Rigorous (af-validated, T0): 70.** Registry: 255. Phases 0–3 of the L0
   af-elevation campaign (epic `aism-xuvw`) are **CLOSED**: PRH,
   decomposition, H-CB (▣ `af-conj-hcb`), and EXT-CB — **`conj-extcb`
   af-validated 2026-07-25** (46 nodes, taint clean; ▣ banked, oracle
   `af-conj-extcb`, `fr verify` pass; bead `aism-fgr7` closed). Both named
   `th_main_ext` gaps are now L0.
4. **The quarantine repair (`aism-0163`) is DESIGN-COMPLETE:**
   `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   is current (V4 cycle: fresh-codex repair → separate fresh-codex hostile
   verify VALID-WITH-CORRECTIONS → corrections applied; inventory 79
   contracted = 57/15/7 + 15 GAP reservations + 20 proposed defs). Phase 4
   (`aism-5byv`) is single-gated on genuine mathematics: **GAP-EA,
   GAP-S1-POLAR-CONTRACT, GAP-MAIN-STRUCTURE, GAP-LEDGER-DOMAINS**, plus the
   user items below.
5. **USER DECISIONS / ESCALATIONS OPEN:**
   (i) v4.1 def-provisioning register sign-offs (20 proposed defs);
   (ii) two Stage-1 topology sources have NO legal open-access copy — **Lee,
   Introduction to Smooth Manifolds (Thm 21.10)** and **Granas–Dugundji,
   Fixed Point Theory** — purchase/institutional access needed (3/7 acquired
   in `refs-staging/`: Hatcher [NOTE: Künneth locus is Thm 3.15 in the
   canonical PDF, not the design's 3.16; cite Cor 3.39 for top-cohomology],
   Cairns 1935, Arkowitz–Brown 2004; log in `refs-staging/ACQUIRED.md`).
6. **Report waves 3/3b/3c LANDED (commit 92e103d8):** 37 shards / 77pp —
   the full phase-2/3 harvest in prose (conj-hcb, hcb3-offdiagonal-inverse,
   hcb4-canonical trio, seven EXT lemmas, the conj-extcb capstone, recounted
   outlook: 37 reproduced + 33 off-route = 70). Two batched fresh-codex
   hostile reviews + verdict-driven corrections; all landing gates green.
   **Remaining report debt (aism-h0mp):** the 21 session-25 prose shards
   (00–24 set) still need their batched hostile prose-vs-export pass.
7. **STANDING DIRECTIVES (user, binding):** (i) capacity on the open leaves;
   (ii) decomposition as objective function; (iii) FINDINGS dead routes
   absolute; (iv) mostly serial; verification fresh-codex-only; af per §6
   (Claude orchestrates, never judges); (v) no progress theatre; (vi) codex
   capped at xhigh; (vii) Route F L0 closure is P0; (viii) RDSE/LDHR-48
   PAUSED; (ix) refs acquisition legal open-access only (2026-07-25).
8. `fr board` + `bd ready`; beads sync via `bash scripts/beads-sync.sh export`.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-25, session 26 — phase-3 closure boundary)

Session 26 resumed the user-stopped `conj-extcb` orchestration (zero ledger
loss) and closed it in 21 rounds at routine tier (3 workers): root
validated, 40/46 validated + 6 archived, taint clean. Banking flip,
export.{md,tex}, oracle registration (text surgery on portfolio.json — the
registrar refuses on format drift; fallback documented), `fr verify` pass,
▣ `fr log`, bead closed: commits 02fdce5c → fc097e67. Concurrently (repo
frozen under the overreach guard, all work off-repo, landed at the
boundary): the aism-0163 V4 repair cycle (landed 1ebeaeef), topology refs
acquisition (3/7, legal-OA only), report waves 3+3b + batched hostile
review (in correction). Sketch v33 + CHANGELOG + this rewrite = the Rule 9
reconciliation (eabe10f6).

**Process patterns validated this session (reusable):**
- The af ledger is append-only: a user-stopped orchestration resumes with
  `--phase verify` and loses nothing.
- Off-repo pipelining under the overreach guard: repair/verify/authoring
  cycles run in the scratchpad against copied inputs while an orchestration
  is live, and land at its boundary. Codex workers get `-C <scratchpad>`
  so the write sandbox cannot touch the repo.
- Mid-run `fr` appends are safe ONLY as atomic controller-log commits
  (append + commit in one step; porcelain-wide guard).
- The linker does NOT see workspace-provisioned defs (a validated tree can
  consume defs its registry shard omits) — check `defs:` lines against the
  export at banking time (8d0a5061 precedent).

## Next steps (ranked)

1. **Finish the report landing:** prose-fix applier (codex high) → fresh
   codex re-verify of shards 26/27/28/35 → land all 11 shards + WIRING plan
   (report build + `check-report-shards` + `check-provenance` gates) →
   close/update the hostile-review bead `aism-h0mp`.
2. **Phase-4 preliminaries (aism-0163 close-out):** user def sign-offs (20)
   + the two paywalled refs (USER) → promote acquired refs
   `refs-staging/` → `refs/` with manifest rows (per-def L1 step) → then
   the first genuine phase-4 mathematics: GAP-EA attack and the
   ledger-domain local-radius producers per v4.1 §D ordering.
3. **Phase 4 proper (`aism-5byv`):** Stage-1 packet → `lem-thmainext-conditional`
   → `lem-routef-k-ledger`, each per the validated seeding laws (dep
   alignment, default first-class pair, cumulative def kit, tripwire
   factoring). Then phase 5 (`aism-y81y`): F0 codification + root
   composition.
4. Route X deciders (`aism-ea2f`) — unchanged fallback pricing.

## What is intentionally NOT here

- Any claim `op-classical` is proved/rigorous. It is OPEN. T0 is exactly
  **70**; everything in the chain above EXT-CB (Stage-1/MAIN/ledger/F0)
  remains `proved-mod-audit`/`stated`/GAP — the four GAP families are
  genuine open mathematics, not process debt.
- Any movement on RDSE/LDHR-48, the signed trunk, or numerical `K`/`η_K`.
- The report waves 3+3b prose (scratchpad only until re-verified + landed).
