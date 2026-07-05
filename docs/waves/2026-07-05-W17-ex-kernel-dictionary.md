<!--
WAVE: trunk scoping probe wave 17 (the (EX)=>Kernel dictionary, sketch-v2 <3>3) — 2026-07-05,
  session 8, bd aism-pb5.
WORKER: fresh codex exec (prompt: session scratchpad PROMPT-w17-ex-kernel-dictionary.md). Answer
  VERBATIM below.
ORCHESTRATOR: stress script rerun clean (exit 0). Headline: the v1 sigma-door prose DOES NOT
  close as written. Proved short (worker T1, unreviewed): D0 (EX)+factorization; D1 the low-halo
  reduction (only sigma_g > 1/2 hidden top vertices matter — H <= 29tau/8 otherwise, from the
  validated halo-collapse); D8 the financing algebra. GENUINE GAPS: D4 (quantifier bridge), D5
  (THE WALL: row-v weights P_vj vs pivot weights P_{u_s j} — no transport lemma exists), D7
  (self-support replacement); D2 (W nonempty) moderate and untouched; D6 (carrier-nu) DEAD by
  DC2. Closability estimate: <3>3 may be Kernel-sized — relative value shifts toward Route A.
  Named decider: the door ratio max_s S*_s(U)/(sigma_g*H) over rank-3 families.
TIER: worker-tagged throughout (T0 loci/certificates; T1 short proofs, unreviewed; T2 gaps).
-->

# W17 Scoping Report: `(EX) => Kernel/HLC` Dictionary

Tier legend: **T0** = exact repo locus / banked certificate; **T1** = short proof from T0 facts, proved here; **T2** = named gap or priced proof obligation; **T3** = speculation. No tracked files were edited. I did not run `fr`, `bd`, or mutating `git`.

## Target

**[T0] Exact Kernel target.** `conj-kernel` asks for universal `delta_0>0, B<inf` such that every exact signed idempotent `P` with `delta(P)<=delta_0` has `W(P) nonempty`, and every hidden row vertex `v` with raw invisible mass `sigma~_v > tau=sqrt(delta)` satisfies
`dist_1(p_v, conv{p_w:w in W}) <= B tau`.

**[T0] `(EX)` input.** `conj-ex` gives one theta-`1/2` actual-row chart `U0` with `max_s Phi_s(U0) <= C0 delta(P)`.

**[T0/T1] What `(EX)` already buys.** By `lem-factorization`, for the same chart,
`max_s S*_s(U0) <= C_sf delta(P)`, where `C_sf = 2 C0 + 6`.

**[T1] Weakest HLC-facing reduction.** It is enough to handle hidden **top** vertices with halo-robust mass `sigma_g > 1/2`. Indeed `conj-halo-collapse` gives
`H(1-sigma_g) <= (sigma-sigma_g) tau/4 + nu_v(2+4delta)`. Since `sigma-sigma_g <= 1+nu_v <= 1+delta <= 5/4`, `nu_v<=delta`, `delta<=1/4`, and `delta=tau^2<=tau/2`, the right side is at most `29 tau/16`. Hence if `sigma_g<=1/2`, then `H<=29 tau/8`. Non-top hidden vertices are bounded by the top height.

**[T1] Door statement that would close the edge.** A sufficient intermediate is:
for every hidden top vertex `v` with `sigma_g(v)>tau`, the `(EX)` chart satisfies
`max_s S*_s(U0) >= c sigma_g(v) H` for a universal `c>0`. Then `H <= (C_sf/c) tau`.
With an additive/error form `max_s S*_s >= c sigma_g(H-tau/4)-A delta`, the conclusion is
`H <= (1/4 + (C_sf+A)/c) tau`. This is the precise sigma-door financing shape.

## Factored Skeleton

| id | sub-statement | status | price | stress result | locus |
|---|---|---:|---:|---|---|
| D0 | `(EX)+factorization` gives `max_s S*_s<=C_sf delta`. | **T0/T1 proved** | trivial | Passes; exact constants `(2,6)`. | `conj-ex.md`, `lem-factorization.md` |
| D1 | HLC only needs the high-halo branch `sigma_g>1/2`; low halo gives `H<=29 tau/8`. | **T1 proved here** | short | Sigma-halo run is low halo and non-vacuously bounded. | `conj-halo-collapse.md`; stress summary |
| D2 | Kernel also needs `W(P) nonempty`. | **T2 OPEN** | moderate/genuine | Not touched by sigma-door; most current collapse lemmas assume nonempty `W`. | `conj-kernel.md`, `def-height.md` |
| D3 | Geometry lemma: if `conv(U0) subset C_W`, then coordinate negative mass in `U0` controls height: `neg_U0(x) >= dist_1(x,conv U0)/(2+4delta) >= H/(2+4delta)`. | **T1 conditional proof** | short under chart-visibility | Not refuted, but premise is not supplied by `(EX)`. | `def-signed-idempotent.md` row diameter |
| D4 | Chart-visibility/quantifier bridge: the one existential `(EX)` chart is good for every hidden top vertex, or can be replaced by such a chart. | **T2 OPEN** | genuine gap | High-self argmins use nontrivial hidden-looking rows; no visible-chart guarantee exists. | DC4 mismatch (i) |
| D5 | Weight bridge: row-`v` positive coefficients `P_vj^+` can be charged by pivot weights `beta_s(j)^+=P_{u_sj}^+`. | **T2 OPEN** | genuine gap | Naive same-pivot seeing is false: DC2 has `a_s(i)<0`, `beta_s(i)=0`, but transverse carrier mass `B_{1,0}>0`. | DC4 mismatch (ii); DC2 |
| D6 | Replacement via carrier own negativity `nu_i` finances chart negativity. | **T0 false for broad form** | dead as stated | DC2 has `B_{1,0}=1/4020000000>0`, carrier `nu_i=0`, and `SUM_carriers=0`. | `runs/2026-07-05-nsc-zero-denominator-refuter/` |
| D7 | Replacement via self-support, "v listens to itself". | **T2 OPEN** | genuine gap | Raw self-mass can be pure halo (`sigma=5343/5000`, `sigma_g=0`); if a chart contains the row, coordinate excess can vanish. Needs a real lemma. | `obs-sigma-halo-nonrobust.md`; D3/D5 |
| D8 | Financing algebra once a door lower bound exists. | **T1 proved here** | trivial | No stress issue; all difficulty is D3-D7. | this report |

## Stress Checks

Rerun command:

```bash
python3 waves-scratch/w17-ex-kernel-dictionary/stress_dictionary.py
```

**[T0] Hard asserts in the scratch script:** for the July 5 certificates, `B*L=I`, `P=L*B`, `P^2=P`, row sums `1`, and exact `delta`; for DC2, `B_{1,0}>0`, `SUM_carriers=0`, carrier `nu=0`, same-pivot `beta_s=0`; for the sigma self-mass witness, `delta=252559/1280000`, raw `sigma=5343/5000`, halo `sigma_g=0`.

**[T0] Wave-15 clean Gamma block.** `delta=55319/1000000`, `U=(0,2,4)`, maximal pivot `s=2`, high-self row `j=1` has `a=(-8/197,5/197,200/197)`, `P_jj=203/400`, `nu_j=1/50`, `beta_s(j)=19988231/40000000`, `E_s(j)=11/197`, and its `Phi/S*` atom is exactly `219870541/7880000000`. This confirms the clean high-self branch is real below the cap; emptiness/high-self exclusion is dead.

**[T0] DC2 zero-nu carrier.** `delta=20099999/4040100000`, unique argmin `U=(0,3,4)`, `Phi=(0,0,0)`. The carrier row `i=1` has `a=(-1/40399,200/40399,40200/40399)`, `a_s=-1/40399`, `nu_i=0`, same-pivot `beta_s(i)=0`, but transverse `beta_r(i)=40399/4020000000` and `B_{1,0}=1/4020000000`. This directly kills the broad carrier-`nu` financing shape and the naive "same pivot sees every negative coordinate" rule.

**[T0] G13 amplifier high-self family.** Record `delta=590855669597640985598471/10775740230179796072754000`, `B/delta=90516217933510287011133600/116398566910735274162898787`, high-self `P_jj=203/400`, and `B-(Phi_r+I)=637/49250`. Existing pivot budgets do not absorb the B-term.

**[T0] Sigma-halo nonrobust witness.** Hidden top `v=0` has `delta=252559/1280000`, `H=962906/108276325`, `P_vv=5343/5000`, raw `sigma=5343/5000>1`, but `sigma_g=0`. Any dictionary using raw `sigma` as a cap quantity is false; the halo version survives this stress.

## Verdict

**[T2] The v1 prose dictionary does not close as written.** The algebraic financing step is easy once a door lower bound is available, but the door lower bound hides two genuine gaps: chart geometry/quantifiers (D3-D4) and row-weight to pivot-weight transport (D5-D7). The DC2 certificate already falsifies the most tempting carrier-`nu` replacement.

**[T2] Hardest piece.** D5 is the central wall: `(EX)` controls `S*` with pivot-row weights, while Kernel/HLC is driven by row-`v` reproduction weights. No current lemma transports `P_vj^+` demand into `P_{u_sj}^+` demand uniformly over all hidden vertices.

**[T2] Closability estimate.** `<3>3` looks larger than a K-block leaf and closer to a new Kernel-sized wall unless a decisive selection/transport lemma is found. The stress zoo does not refute the final high-halo door statement, but it refutes several natural factorizations of it.

**[T1/T2] Most informative next wave.** Run a joint exact decider over banked and generated rank-3 families computing `W,H,sigma_g`, all theta-half `Phi` argmins, and the ratio
`max_s S*_s(U)/(sigma_g H)` for hidden top vertices. The wave should specifically hunt: (i) high `sigma_g` with low `S*`; (ii) an `(EX)` argmin containing the hidden top vertex; (iii) row-`v` positive mass on rows with zero pivot visibility. A single exact counterexample to the door lower bound would redraw sketch v3 toward Route A.