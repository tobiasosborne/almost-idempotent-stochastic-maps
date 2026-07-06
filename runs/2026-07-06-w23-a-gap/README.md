# Run bundle: a-gap route (ii) exact checks — small-a Lemma A frontier (W23 worker I) — 2026-07-06

**Status: L3 numerical evidence — the exact-certificate side of an OPEN-BOTH-SIDES verdict; NEVER an
emptiness claim.** Exact ℚ throughout. One codex worker (prompt in the session scratchpad,
`W23/PROMPT-I.md`), mutually blind from the route-(i) worker and its verifier. Orchestrator reran the
script (exit 0; stdout in `data/`). Companion wave artifact: `docs/waves/2026-07-06-W23-a-gap.md`
(where route (i) — the parametric halo collapse, reviewed — closes the a-gap, making this route moot
for the bootstrap).

## Hypothesis / adversarial question

Route (ii) of closing THE A-GAP (bd `aism-sg6`): does Lemma A (`lem-visible-g-small`) extend below
halo width 4 — is there a universal C with `g_w^{(a)} ≤ C·τ` for visible rows at `a ∈ (29/8, 4)` —
or is there an exact counterexample family (target test point a = 15/4)?

## Finding (headline + honest scope)

**OPEN-BOTH-SIDES.** Prove side blocked structurally [T2]: the annulus `aτ < ‖p_j − p_w‖₁ < 4τ = ρ`
is priced by no available tool — the (ρ,κ)-exposer gives lower bounds only at distance ≥ ρ;
shell-row reproduction controls outgoing (not incoming) mass; the hidden-top collapse tools do not
estimate visible-row load. Refute side [T1, exact]: NO tested family enters `G_{15/4}` — the Hume
sharp family (s = 1/100, δ = 1/10000), the W19 rank-3 genuine-partner and rank-5 genuine-self
anchors, the duplicate split (m = 4, q = 5/84) all have `G_{15/4} = ∅`; a shallow-corner
constant-mass ansatz produces an exact idempotent whose ACTUAL δ inflates (1903/1000000 vs the
formal 1/1000000) and exact visibility again empties `G_{15/4}`. Binding constraints named:
δ-inflation + exposedness absorption. NOT an emptiness claim; a counterexample must simultaneously
hold negative mass O(ε²), a row at depth in (15τ/4, 4τ), and a visible row placing non-O(τ) mass on
it — unrealized here.

## Command (re-run)

```bash
python3 runs/2026-07-06-w23-a-gap/scripts/w23_worker_i.py   # all exact assertions; exit 0
```

`data/worker-i-report.md` is the worker's full report (exact matrices for every tested instance);
`data/rerun-i-stdout.txt` is the orchestrator's captured rerun.

## Invariant / known-value check

The script hard-asserts exact idempotence, row sums, δ values, W, and the emptiness of `G_{15/4}`
on each tested instance, anchored to banked exact values (Hume δ = 1/10000; W19 anchors
δ = 74551/1600000 and 3983/96000; duplicate split δ = 1/16). Orchestrator rerun exit 0.

## Next

Route (ii) is MOOT while route (i) (`lem-parametric-halo-collapse`, reviewed) stands — the
contradiction surface now lives at a = 4 with tall threshold 13τ. Only revisit if the step-4
argument turns out to need a < 4 after all.
