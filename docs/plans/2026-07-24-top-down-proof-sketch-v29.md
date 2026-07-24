<!--
ROLE: the top-down FULL proof sketch of op-classical, VERSION 29 (W74F wave-2 + W72
  discharge delta). Supersedes v28; everything not restated here is unchanged from v28.
STATUS DISCIPLINE (L0): a SKETCH / STRATEGY artifact; promotes nothing. Route F's chain
  now closes at the proved-mod-audit rung (hostile-verified paper proofs), which is NOT
  rigorous by this repo's L0: nothing below is af-validated unless said so.
-->

# Top-down proof sketch v29: op-classical (2026-07-24, W74F wave-2 delta — both th_main_ext gaps close at L5; the W72 debt is discharged)

## UNCHANGED from v28

The signed-geometry trunk (op-classical ⇐ op-exposed-hull ⇐ HLC ⇐ Kernel/(EX)), the
three-cell SL1a surface, all dead routes (FINDINGS.md, Rule 13), H-D, H-I, SL1b, L6.5,
the small-gauge bridge, Route X as the registered fallback shape (deciders aism-ea2f,
unrun). **T0 count 34 af-validated.** The Route F skeleton F0–F5 and the W73b audit
verdicts stand exactly as v28 records them.

## Map change 1: the wave-1 survivors are CODIFIED (registry 200 → 208)

The 4/4-verified W74F wave-1 batch is now in the registry at honest statuses
(aism-zbcm closed): `lem-prh` + `lem-prh-sharpness` (F4, constant **2√2**, `√ε`
intrinsically sharp), `lem-kitaev-diagonal-repair` + `cor-kitaev-diagonal-cpization`
(risk-register item 3), `conj-hcb` + `conj-extcb` (the two named gaps),
`lem-thmainext-conditional` (the conditional assembly + conditional `K`/`η_K` ledger),
`lem-kitaev-almost-idemp-audit` (item 5, the `10η` core + explicit `ε_AI(η) = O(η)`
interface). Four new draft definitions await **user ratification**
(`def-positive-approximate-retract` original; `def-extended-epsilon-cstar-algebra`,
`def-ha-map`, `def-fd-cstar-diagonal` cited byte-verbatim from the pinned tex).

**The PRH reduction is on the map as a registry fact:** *op-classical ⇐ "a positive
approximate retract exists"* (`‖AM−Q‖ = O(η)`, `‖MA−I_k‖ = O(η)`, `A`,`M` stochastic)
— a clean target independent of whether the Kitaev import survives.

## Map change 2: W74F wave 2 — BOTH `th_main_ext` gaps close at the hostile-verified rung

Each gap got one fresh codex xhigh prover and a SEPARATE fresh hostile codex xhigh
verifier (artifacts in `docs/plans/2026-07-24-W74F-wave2-artifacts/`):

- **H-CB closed** (`conj-hcb` → `proved-mod-audit`, aism-wwur). Verdict
  VALID-WITH-CORRECTIONS: the `n`-uniform analytic content holds with `C_H = 4000c`,
  `e_H = 1/(10000c)` (`c` = max of the sanctioned COMP-CB/COL-HILB universal constants
  — explicit RELATIVE constants, not decimals); no `n`-growth family found. One
  genuine finding: the **unconditional inverse for `h_{P,P}` is FALSE** (exact `ℂ⊕ℂ`
  counterexample); the contract was amended to the verifier's exact conditional-inverse
  clause, which is precisely the form `lem_extension` consumes. NOT an escalation: a
  contract refinement, not a refutation of the claimed dimension-free uniformity.
- **EXT-CB closed** (`conj-extcb` → `proved-mod-audit`, dep `conj-hcb`, aism-9lb7).
  Verdict VALID-WITH-CORRECTIONS: one level-one unitary carries every amplification;
  the prover's deliberate **transported-corner construction**
  (`γ_jk = h_jk^{-1}μ_jk`, `γ₁₁ = v`) was confirmed valid — it makes the three
  off-`11` corners exactly close at all levels, closing the single-map issue the
  printed source left open. `C_ext = C_merge[1 + 5C_H + 20C_app(C_H+1)]`. One
  proof-level correction (level-one close-idempotent normalization folded into
  `e_sel`); no contract amendment.

**Consequence.** Through `lem-thmainext-conditional`, `th_main_ext` now holds at the
`proved-mod-audit` rung — the principal blocker of the W73b audit (risk-register
item 1) is closed at L5. The Route F chain
`F0 → F1(th_factorization ⇐ th_main_ext + th_almost_idemp + diagonal repair) → F2 →
F3 → F4(PRH) → F5` is now **proved-mod-audit end-to-end conditional on nothing but
the unconditional `K`/`η_K` extraction**, with the conditional finish
`‖Q−E‖ ≤ (K+4√(2K))√η`.

### The residual risk register, re-scored (v28 §"residual risk register")

1. `th_main_ext` at amplified strength — **CLOSED at L5** (H-CB + EXT-CB + verified
   decomposition; not af-validated).
2. universal-constant ledger — **IN FLIGHT** (wave 3, aism-xpxk: the unconditional
   `K`/`η_K` extraction; the one possibly-new inequality is the raw-step/reset
   threshold check, DECOMP §7 item 10).
3. diagonal repair — **CLOSED at L5 and codified** (wave 1).
4. no cone shortcut — **CLOSED** (wave 1, entrywise CP-ization).
5. `th_almost_idemp` audit — **CLOSED at L5 and codified** (wave 1; `tex:2239-2723`
   audited with local fixes, not re-proved line-by-line — recorded honestly in the
   shard scope).
6. PRH — **CLOSED at L5 and codified**; af-elevation now the natural next rung
   (aism-h9qc, unblocked).
7. rigour-status/provenance closure — ongoing by construction (every flip above went
   through fresh-codex hostile verdicts + gates).

## Map change 3: the W72 debt is discharged (registry 208 → 214)

The interrupted POTI-0 batched hostile verifier was re-dispatched from a rebuilt
`build-workspace.sh` snapshot with the committed brief verbatim: **S0 · RX · O48 ·
ASM2 all VALID**, cross-cutting clean (selected-root provenance sound on partially
selected clone fibers; foldback ledgers legal; walls K5/F19 respected). Codified as
six shards: S0/RX/O48 + the conditional assembly at `proved-mod-audit`
(`Z_v(q_A) > (7c_m/960)τ` assuming the residuals), RDSE + LDHR-48 registered as
`conjecture` (empty deps). **POTI-0 == RDSE + LDHR-48 is now a proved-mod-audit
conditional reduction on the signed-trunk map.** The creative attacks on the two
residuals remain PAUSED (user directive 2026-07-23; Route F is P0).

## Tier-1 order (unchanged priority logic, updated content)

1. **Wave 3: the unconditional `K`/`η_K` ledger** (aism-xpxk, prover in flight) —
   the last purely mathematical Route F item; hostile verification gates codification.
2. **PRH af-elevation** (aism-h9qc) — small, self-contained, first Route F node to
   attempt the T0 rung; CLAUDE.md §6, strictly serial, clean tree while live.
3. af-elevation queue for the new chain (H-CB/EXT-CB are large; factor per §6
   playbook before seeding) + the standing aism-88r candidates.
4. Route X deciders (aism-ea2f) — cheap kill-or-confirm; the fallback stays priced.
5. Signed-trunk surface (unchanged from v28): SL1a cells, sigma-cap, halo-robust
   finisher — all now BEHIND Route F in priority but not retired.

## What v29 explicitly does NOT claim

- That op-classical is proved. The chain is `proved-mod-audit` end-to-end modulo the
  in-flight `K`/`η_K` extraction; **nothing new is af-validated (T0 remains 34)** and
  nothing meets L0 rigour.
- That `K` or `η_K` have numerical values — the source's unnamed big-O constants make
  the ledger RELATIVE by construction; the wave-3 deliverable is the closed symbolic
  chain, not decimals.
- That the H-CB/EXT-CB hostile verdicts equal af-validation: they are single fresh
  hostile passes (the batched-verification default), one rung below T0.
- That the four draft definitions are ratified (they are not — user sign-off pending).
- That RDSE/LDHR-48 or any signed-trunk conjecture moved: they did not.
- That the strategists' altitude diagnosis of RDSE/LDHR-48 became a theorem: it
  remains banked interpretation.
