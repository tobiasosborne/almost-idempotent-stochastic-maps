<!--
ROLE: the top-down FULL proof sketch of op-classical, VERSION 30 (W74F waves 3/3b
  delta). Supersedes v29; everything not restated here is unchanged from v29.
STATUS DISCIPLINE (L0): a SKETCH / STRATEGY artifact; promotes nothing. Route F is
  proved-mod-audit COMPLETE — which is NOT rigorous by this repo's L0. T0 = 34;
  nothing below is af-validated unless said so.
-->

# Top-down proof sketch v30: op-classical (2026-07-24, W74F wave-3 delta — Route F is proved-mod-audit COMPLETE; the remaining open work is L0 closure)

## UNCHANGED from v29

The signed-geometry trunk and its whole surface (SL1a cells, sigma-cap, halo-robust
finisher, POTI-0 == RDSE + LDHR-48, all dead routes), Route X as the registered
fallback, the four draft definitions pending user ratification, **T0 = 34
af-validated**. Registry: 215 (was 214).

## Map change: the relative K/η_K ledger closed — after one hostile rejection

Wave 3 (`LEDGER-W74F-G-K.md`) claimed the closed relative ledger; its fresh hostile
verifier returned **INVALID** for exactly one reason — the MAIN-CB Stage-1
`lem_nontriv_projection` split packet (`tex:1419-1425`) had no named coefficient or
threshold, so the reset chain missed its raw packet and `η_K` lacked one guard. (The
`K` formula and the PRH finish were confirmed VALID even in that verdict.)

Wave 3b (`PROOF-W74F-H-STAGE1.md`) extracted the packet — universal
`C_split ≥ 1`, `e_split > 0` from the printed `tex:915-969` construction, all-level
bounds via the `tex:1475` isometry (no entrywise sums), corrected reset chain
`C_main = max{C_co, C_split}`, guard `e_split/(C_pre·C_A)` added to `η_K`. Its fresh
hostile verifier returned **VALID-WITH-CORRECTIONS**: the load-bearing `tex:943`
uniform-isolation expansion is dimension-free; the topological inputs add no analytic
coefficient; two wording/ledger corrections (separate the old ambient defect `ε_0`
from the fresh split-corner defect `ε_S`; make the nonvanishing shrink `e_nv`
explicit) — **the ledger is CLOSED at `proved-mod-audit`**.

Codified per the verdicts' verbatim-endorsed contracts:

- **`lem-routef-k-ledger`** (new, `proved-mod-audit`): universal relative `K ≥ 1`,
  `η_K > 0` (dimension/amplification/block-free; explicit relative expressions, no
  decimals — the source's big-O constants are unnamed), with the finish
  `‖Q−E‖_{∞→∞} ≤ (K+4√(2K))√η` for `η ≤ η_K`. Deps: the assembly, the diagonal
  CP-ization, the `th_almost_idemp` interface, PRH.
- **`lem-thmainext-conditional`** restated (id stable): the `C_E`/`ε_E` extended
  `th_main_ext` assembly via the hostile-verified H-CB + EXT-CB + Stage-1 packets.

## Where op-classical now stands

**Route F is `proved-mod-audit` COMPLETE.** Every node of
`op-classical ⇐ F0 (cb-lift) ⇐ th_factorization (⇐ th_main_ext ⇐ H-CB + EXT-CB +
Stage-1; + th_almost_idemp interface; + repaired diagonal) ⇐ F2/F3 (commutativity
forcing + compression) ⇐ PRH ⇐ finish (K+4√(2K))√η` is hostile-verified
(fresh-codex prover ≠ fresh-codex verifier per node or batch) and codified. The
sharp exponent 1/2 is preserved; all constants are dimension-free by construction
and verifier-recomputed.

**What this is NOT:** rigorous. `proved-mod-audit` is one rung below T0. The entire
chain rests on repaired source material plus this repo's own hostile-verified paper
proofs; none of it is byte-verbatim-citable, af-validated, or Lean-proved.

## The remaining open work (the new Tier-1 face): L0 closure

1. **PRH af-elevation** (aism-h9qc) — small, self-contained, elementary; the natural
   first T0 attempt. CLAUDE.md §6 verbatim; strictly serial.
2. **af-elevation strategy for the large chain** (H-CB, EXT-CB, Stage-1, assembly,
   ledger): each exceeds the af brittleness envelope as one tree — factor into
   registry sub-lemmas per the §6 playbook BEFORE seeding. This is a decomposition
   task, not a proving task.
3. Alternatively/complementarily: **byte-provenance hardening** — the repaired chain
   cannot cite the source verbatim (its printed proof was invalid); an af-validated
   spine is the only currently-approved route to L0.
4. Route X deciders (aism-ea2f) stay filed as the fallback; the signed trunk stays
   parked behind Route F.

## What v30 explicitly does NOT claim

- That op-classical is proved or rigorous. T0 = 34; L0 closure is fully open.
- That `K`, `η_K` have numerical values (relative expressions only, by construction).
- That any hostile verdict equals af-validation (single fresh passes, one rung below).
- That the draft definitions are ratified, or that anything on the signed trunk moved.
