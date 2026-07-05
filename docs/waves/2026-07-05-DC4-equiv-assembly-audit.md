<!--
WAVE: decision-check DC4 (equivalence + assembly pricing audit — the unpriced trunk) — 2026-07-05,
  session 8, bd aism-pu0 (audit half).
WORKER: fresh codex exec (prompt: session scratchpad PROMPT-dc4-equiv-audit.md). Answer VERBATIM below.
ORCHESTRATOR: locus-citation audit (no certificates to recompute). Headline: the conj-ex <=>
  conj-kernel "equivalence" has NO proof in EITHER direction anywhere in the record (both
  directions priced GENUINE GAP; T2) — the campaign's (EX)-facing work currently has no proved
  edge to the Kernel/HLC chain that feeds op-classical. Three quantifier/weight/interface
  mismatches named (chart-vs-vertex; P_vj-vs-P_{u_s j} weights; maximal-pivot drift). Recommended
  v2 redraw: Kernel = theorem-facing input; (EX) = separate attack route with a NEW OPEN edge.
  Adopting the redraw changes PRD wording + the frontier = USER decision (escalated).
TIER: T0 loci/statuses; T1 short inferences; T2 gaps and the redraw proposal.
-->

# DC4 Equivalence + Assembly Pricing Audit

Tier legend: **T0** exact repo locus / registered status; **T1** elementary inference from T0 loci; **T2** named gap or interface mismatch; **T3** speculation. I made no tracked-file edits.

## Executive Verdict

**[T0]** `conj-ex` and `conj-kernel` assert equivalence only in registry prose (`argument/lemmas/conj-ex.md:4,14`; `argument/lemmas/conj-kernel.md:14`; `report/sections/13_discussion.tex:26`). **[T0]** The operational audit classifies `conj-ex <=> conj-kernel` as "asserted in prose, empty deps" with the same risk profile as retired dual-localization (`docs/audits/2026-07-04-operational-audit.md:31-43`). **[T2]** I found no proof of either implication.

**[T2] Recommendation:** sketch-v2 should treat **Kernel** as the theorem-facing input for the HLC/exposed-hull chain. Keep **(EX)** as a separate conjectural upstream attack route with an explicit **OPEN** edge `EX => Kernel/HLC`; cut `Kernel => EX` and cut bidirectional "equivalent" wording.

## Priced Gap Table

| Link | Status / price | Blocking? | Exact locus |
|---|---:|---:|---|
| `(EX)` statement | **T0 conjecture** | no | `conj-ex.md:4`; `kernel-conjecture-v2.tex:219-231` |
| `Kernel` statement | **T0 conjecture** | no | `conj-kernel.md:4`; `kernel-conjecture.tex:151-166` |
| `EX => S* / signed-face` via `lem-factorization` | **T0 proved conditional; trivial** | no | `lem-factorization.md:4,14-31`; `w42_factor_audit/audit.md:144-168` |
| `EX => Kernel` | **T2 missing; genuine gap** | yes | only prose: `top-down-proof-sketch.md:60-69` |
| `Kernel => HLC` | **T1 short proof, recorded** | no if Kernel is input | `kernel-conjecture.tex:176-221` |
| `Kernel => EX` | **T2 missing; genuine gap** | no if edge cut | registry prose only: `conj-kernel.md:14` |
| Upper collapse `H(1-sigma)<=nu(2+4delta)` | **T0 af-validated; trivial** | no | `obs-height-collapse.md:4,14-22` |
| Halo collapse | **T0 af-validated; trivial** | no | `conj-halo-collapse.md:4,14-30` |
| Halo/sigma cap lower side | **T2 genuine gap** | yes | `conj-no-free-frontier.md:27-36`; `B4-walls-check.md:183-215` |
| HLC => `op-exposed-hull` | **T0/T2 mod-audit; moderate** | yes for rigor | `04-reduction-chain.tex:57-79` |
| `<1>7` output => `thm-cluster` assumptions | **T2 interface moderate** | yes | `thm-cluster.md:4`; `01-linear-markov-setting.tex:142-167` |
| `<1>7` output => `prop-approx-simplex` | **T2 genuine interface gap** | yes if used | `prop-approx-simplex.md:4`; `op-classical.md:16-20` |
| `thm-classical-factorization` => stochastic idempotent | **T2 JB identification gap** | yes if used | `thm-classical-factorization.md:4,14`; audit `:37-43` |
| `<1>9` distance accounting | **T1 short after prior links** | no | sketch: `top-down-proof-sketch.md:71-80` |

## Mismatches Found

- **[T2] Chart vs vertex:** `(EX)` gives one existential theta-half chart; Kernel quantifies over hidden row vertices.
- **[T2] Weight mismatch:** Kernel invisible mass uses row `v` coefficients `P_vj`; `Phi_s` uses pivot-row weights `P_{u_sj}`.
- **[T2] Maximal-pivot drift:** sketch narrows Lemma K to a "maximal pivot" (`top-down-proof-sketch.md:88-90`), not enough for an arbitrary hidden top vertex without a pivot/vertex selection lemma.
- **[T2] Raw sigma false:** exact certificate has `delta=252559/1280000`, `sigma=5343/5000>1`, halo mass `0`; any cap must use `sigma_g` (`obs-sigma-halo-nonrobust.md:4,14-19`).
- **[T2] Cluster interface:** `dist(rows,conv W)=O(tau)` is weaker than separated exposed representatives plus disjoint clusters.
- **[T2] Approx-simplex interface:** near-hull geometry does not provide affine coordinates with `O(delta)` coefficient negative mass.
- **[T2] JB output mismatch:** factorization outputs `J, Delta, Upsilon`, not an explicit stochastic idempotent matrix `E`.
- **[T1] Norm/scale check passed:** `delta=O(eta)` gives `sqrt(delta)=O(sqrt(eta))` via `lem-classical-equiv.md:4,14-18`.

## Recommended v2 Redraw

```text
conj-kernel  [OPEN theorem-facing input]
  => HLC / height cap                         [short conditional]
  => op-exposed-hull                          [proved-mod-audit, re-audit]
  => thm-cluster / prop-approx-simplex route  [proved-mod-audit, re-audit]
  => op-classical

conj-ex [separate conjectural attack route]
  => lem-factorization / coordinate cleansing [proved]
  => EX-to-sigma-door / EX-to-HLC             [NEW OPEN GAP]
  => conj-kernel                              [only after that gap is proved]
```

Do not label `conj-ex` as equivalent to `conj-kernel`; do not keep either direction as a corollary. The safe label is: "`(EX)` is a conjectural strengthening/alternative route that currently has a rigorous factorization link but no proved edge to the geometric Kernel input."
