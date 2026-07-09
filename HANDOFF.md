<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read **`docs/plans/2026-07-09-top-down-proof-sketch-v19.md`** — THE canonical strategic map
   (v19, W55 strategy delta; v18 and earlier superseded in place, kept for line citations).
   Then **`docs/plans/2026-07-09-w54-huddle-charge-decomposition-tree.md`** — the VERIFIED
   decomposition of the terminal node (read PART A through PART B).
   **STEWARDSHIP (user mandate, 2026-07-06, binding): reconciling the sketch with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **STANDING DIRECTIVES (user, binding):** (i) TIER-1 FOCUS; (ii) Fable-grade agents
   liberally for deep proof/strategy while Tier-1 nodes remain (verification stays
   fresh-codex-only, §6); (iii) once Tier 1 falls, farm out the parked queue; (iv) no
   progress theatre; **(v) NEW 2026-07-09: the objective function of every Tier-1 attack
   is DECOMPOSITION into lower-complexity pieces** (case trees, small-lemma systems with
   checkable assemblies) — W53/W54 are the template.
4. Run `fr board` and `bd ready`. Read
   `docs/waves/2026-07-09-W55-cotop-web-coupling-strategy.md` after the W54 tree. This
   checkout currently lacks the local Dolt beads database, so `bd ready` reports
   “no beads database found”; do not silently `bd init` over the configured project.
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-09, W55 strategy close)

**Rigorous (af-validated, T0): 28** (unchanged — no af runs this session).
**Registry: 140** (unchanged in W55; L0 claimed ONLY for the af-validated 28).

**THE STATE OF THE PROOF (sketch v19): the terminal node remains a VERIFIED four-leaf system.**
Session 13 executed the decomposition mandate end-to-end: W53 collapsed the three W52
binding constraints into THE HUDDLE CHARGE (sketch v17); W54's Fable-architect case tree
was hostile-verified (INVALID -> prescribed repairs -> VALID-WITH-CORRECTIONS, all
applied), its easy/medium leaves proved or reduced, and both creative branches collapsed:

- **Branch II == {`conj-straddling-web-exclusion` (SL1a) + `conj-shallow-counterweight-
  exclusion` (SL1b)}** via `lem-l2-core-collapse` + `lem-intersection-witness-confinement`
  (the identity-level averaging cap). Alternative: Theorem-C route via
  `conj-summit-cylinder-exclusion` + narrow dual face (wave doc).
- **Branch I == {`conj-cotop-web-coupling` (L6.5) + the L5 dual-face mass minimax
  (aism-vuc)}** via `lem-cotop-witness-pinning`, `lem-downhill-cotop-conic-mass`,
  `lem-psi-corner-trap` (the t*-FREE toolkit — the t*-division death trap is closed).
- Consumption above the node: `lem-absorption-implies-low-slab-cap` wires tall-emptiness
  (+ `conj-far-low-slab-cap`) => `conj-low-slab-cap` => the Kernel height clause.

W55 attacked `conj-cotop-web-coupling` decomposition-first. Two exact, independently
hostile-reviewed reductions emerged but remain uncodified/non-L0: failure of coupling
creates a top-funded high-return near corner (E1-E5), and every small-conic-gauge display
(`A0<=3/32`) reduces to the existing SL1a/SL1b pair. Moderate gauge, conditionally on
SL1b, reduces to a new OPEN mixed co-top straddle. Large gauge does NOT reduce by harmonic ledgers: an exact local
`A0=5, g=5*tau` starvation gadget survives all of them. The live large-gauge mechanism is
global completion obstruction through `P=L*B`, `B*L=I`, or an exact refuter completion.

**New dead routes (W55):** identifying `lambda*P` with `p_v`; treating dual conic weights
as transition mass; a thin/thick split from the single `g/A0` separator moment; and an
untyped “some web member is exposed” step without vertexization, pairwise separation, and
same-carrier inheritance. The transient-row extension and the exact starvation gadget are
mandatory tests.

## Next steps (ranked) — W56/W57

-1. **RESUME W56 (user central priority 2026-07-09: reduce ALL Tier-1 new-math leaves
   to Tier-2).** SL1a (`conj-straddling-web-exclusion`) was selected as the most open
   Tier-1 leaf and a codex architect (gpt-5.6-sol, ultra) was INTERRUPTED mid-run: the
   DAG shape (L-S selector -> L-V same-carrier reproduction at the selected web row ->
   L-P discard/horn split -> ONE hard leaf H-SCCO) and the proved-input audit are
   preserved in `docs/waves/2026-07-09-W56-artifacts/decomposition-PARTIAL.md` (+ the
   full worker session log, gzipped, same dir); §3-§6 (leaf statements, assembly,
   red tests) are MISSING and NOTHING is hostile-verified. Resume per
   `docs/waves/2026-07-09-W56-sl1a-decomposition-interrupted.md` §Next session.
0. **Fresh standalone prover/verifier passes on W55 E1-E5**, then codify only if valid.
1. **Fresh pass on the small-gauge bridge** `A0<=3/32 => SL1a or SL1b`; this is the
   cleanest new joint edge and must carry its conditioning constants verbatim.
2. **Exact completion/refutation LP** for the `A0=5, g=5*tau` starvation gadget in
   `P=L*B`, `B*L=I` coordinates. A rational feasible family refutes L6.5; stable dual
   infeasibility multipliers should define the global completion theorem.
3. **Mixed co-top straddle + SL1a as one joint wave**; explicitly solve nonvertex support,
   pairwise separation, and same-carrier vertexization. SL1b remains the easiest sibling.
4. **L5 dual-face mass minimax** (aism-vuc): codex geometry problem on Y_v (linear in y;
   the simplex obstruction is sharp — the proof must use Y_v structure + idempotence).
5. Parked: L7 gaps (aism-2ii), elevation queue (the W53/W54 proved families are prime
   af-elevation shapes — single minimal contracts), trunk <2>7 (aism-ik6), Kernel(i)
   rank >= 3, refs ingest (aism-5de).
6. USER DECISIONS pending: `aism-nlg`, `aism-z98` (standing).

## Standing rules (unchanged from session 12 + the new decomposition directive)

Codex workers for all proving/verifying; codex model is **gpt-5.6-sol** (user directive
2026-07-09) at effort ULTRA for truly creative/demanding jobs and lower effort (high or
below) for lower-priority routine jobs — `af-orchestrate.py --tier` encodes this;
Fable-grade for deep proof/strategy (AUTHOR
output — always hostile-verified by fresh codex before codification); ONE af
orchestration at a time; wave docs carry verbatim verdict first-lines; `fr orient` on
no-bank turns; ▣ banked only via `fr verify` against the af oracle. Worker-prompt
patterns + verifier-prompt patterns for decomposition waves: see the W53/W54 scratchpad
prompts quoted in the wave docs (self-contained workspaces: definitions + argument +
CONVENTIONS + the target artifact; verdict-first-line discipline; status discipline
stated in every prompt). NOTE: `codex exec -o FILE` overwrites with the final MESSAGE —
point -o at a scratch FINAL.md, never at the worker's ANSWER.md; recover answers from
the session log if clobbered. Fable agents: instruct INCREMENTAL file writes (<~10k
tokens per call) — one died on the 64k output ceiling and was resumed via SendMessage.

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>       # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 6 --max-rounds 14 --node-cap 40   # background
#   effort tiers (user directive 2026-07-09): default --tier creative (prover ultra /
#   verifier xhigh) for creative-demanding conjectures; --tier routine (high/high) for
#   lower-priority mechanical elevations; --prover-effort/--verifier-effort to fine-tune.
codex exec --skip-git-repo-check -C <scratch-workdir> -m gpt-5.6-sol \
  -c 'model_reasoning_effort="ultra"' -s workspace-write -o <scratch>/FINAL.md - < <prompt>
#   manual workers: gpt-5.6-sol; effort ultra for creative/demanding jobs, high (or lower)
#   for routine ones (supported: low..ultra).
```

## What is intentionally NOT here

- Any claim more than TWENTY-EIGHT results are af-validated. All session-13 codified
  proofs are L5 (fresh-hostile-verified), NOT L0.
- Any claim W55 proves L6.5, the huddle charge, tall-emptiness, any leaf, or the Kernel
  Conjecture is proved. The W54 tree is a VERIFIED CONDITIONAL derivation — its leaves
  are conjectures.
- Any claim the W55 E1-E5 or small-gauge bridge are L0/registry results. They passed
  strategy-level hostile review only and await fresh standalone codification passes.
- Any claim the W52 BLOCKED search or any numerical evidence is a proof (L3).
