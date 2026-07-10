<!--
ROLE: W61 wave record — the two pre-decision L3 deciders for the aism-ur9 route fork
+ the engine-bank af-elevation pair. Written live during the wave; finalized at close.
STATUS DISCIPLINE (L0): a process record; promotes nothing.
-->

# W61 — route-fork deciders (L3) + engine-bank af-elevation

**Session 16, 2026-07-10. User directive: continue attacking the Tier-1s; objective
function = DECOMPOSITION into lower-complexity pieces.**

All three W61 lines are sanctioned by HANDOFF item 0 and run BEFORE (and independent
of) the aism-ur9 route decision, which remains with the user.

## Dispatches

1. **af-elevation pair (aism-zo1).** `lem-hx-transverse-moment-identity` (dep leaf,
   routine tier) + `lem-hx-robust-scalar-starvation` (PRIME, creative tier), seeded
   at commit `1eb04a8`, orchestrated via `af-orchestrate.py` wrapped in
   `codex-dispatch.sh`. The pair is dep-closed, so a clean `validated` flip is
   reachable (linker rule: a validated result may not rest on a non-validated dep;
   flip order: dep first).
2. **Decider A (aism-3nk, Route A lane).** Fresh codex xhigh worker, self-contained
   workspace (`build-workspace.sh` + DECOMPOSITION-W60-CODEX.md + sketch v25):
   exact-rational search for a thin-transient-graft family with delta_k -> 0, bad
   H-X data, and transport cost T_B -> 0. A hit kills X2
   (`conj-w60-hx-microfreight-exclusion`, proposed) and moves Route A toward its
   H-X-selector fallback.
3. **Decider B (aism-kup, Route B lane).** Fresh codex xhigh worker, workspace +
   DECOMPOSITION-W60-FABLE.md + W29/W35 frontier READMEs: exact-rational search for
   a configuration financing the `lem-hx-financing-floor` demand entirely through
   leaks the banked ledgers permit at the N5(ii)/N6 constants. A hit means N5/N6
   need restating before creative spend.

Both deciders are L3: their outputs are evidence, never proof; banking (if any
instance is found) goes through the `runs/` bundle discipline.

## Process lesson (recorded for the methodology file)

**af orchestrations must run SERIALLY in this repo.** The two elevation
orchestrations were initially launched in parallel; each one's prover-overreach
guard (git-porcelain over everything outside its own workspace) flagged the
sibling's legitimate own-workspace writes as stray edits, and the
moment-identity run ABORTED after its prover build (exit 3, false positive).
Remedy applied: the aborted run's own-workspace ledger (append-only, legitimate)
was committed immediately; the moment-identity orchestration re-runs serially
after the prime lands. This extends the 2026-07-02 orchestrator gotcha
(uncommitted registry edits abort every live run) to: one orchestration's
workspace writes are another's guard trip — never co-schedule two
`af-orchestrate.py` runs.

**Second guard trip, same session, harsher lesson:** the guard is REPO-WIDE
(git porcelain over everything outside the run's own `proofs/<id>/`), not just
`definitions/` + `argument/`. The orchestrator's own live wave-doc draft
(`docs/waves/...W61...md`, untracked) aborted the prime run at its round-0
check — after 9/12 nodes had validated with zero challenges. Standing rule
while ANY `af-orchestrate.py` run is live: **the working tree stays completely
clean** — no uncommitted files anywhere in the repo; draft session artifacts in
the scratchpad and copy them in (and commit) between runs. The abort was clean
and the workspace resumes (append-only ledger).

## Outcomes

*(This section is filled in strictly as results land; a dispatch is not an
outcome.)*

- Prime elevation (`lem-hx-robust-scalar-starvation`): prover build produced a
  depth-3, 12-node tree (explicit delta_R; imported unit-moment external; core
  estimate; two sign-union tail bounds; scalar close). Verification rounds IN
  FLIGHT — no verdict yet; shard remains `af: seeded`/L5.
- Moment-identity elevation: aborted at prover-build (the concurrency false
  positive above); ledger banked; awaiting serial re-run after the prime lands.
- Decider A: IN FLIGHT — no verdict yet.
- Decider B: IN FLIGHT — no verdict yet.
