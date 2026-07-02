<!--
ROLE: construction+theory wave for arm A, wave 6: under-cap mechanism killers.
STATUS: L3 numerical/exploration report only. Nothing below proves (EX), conj-kernel, or op-classical.
Tier legend: T0 = exact repo-file fact or exact rational recomputation in this wave;
T1 = elementary derivation / conservative synthesis from T0;
T2 = plausible proof lemma or obstruction hypothesis;
T3 = speculation.
Worker: codex. Arm A wave 6. Answers bd aism-f9y.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd were not run.
Primary exact bundle: runs/2026-07-02-undercap-killers/.
-->

# Arm A Wave 6: Under-Cap Mechanism Killers

## T1. Rescale Attack

The chart vocabulary is the actual-row setup in
`docs/ingest/report/kernel-conjecture-v2.tex`: theta-half charts
`M_{1/2}(P)`, coefficients `a_s(j)`, pivot rows
`beta_s(j)=P_{u_sj}`, `E_s(j)`, `Phi_s(U)`, and `V_s(U)`. [T0]

I tested a generalized B6 staircase with amplitude `a`, perturbation
`eps=1/1000`, and a free transverse dual scale `u`.  The archived B6 row is
`a=1/2`, `u=1/(2m)`, `m=5`, hence `delta=1/2`.  Moving `u` alone does not port
the witness: for fixed `a=1/2`, the signed rows acquire large negative mass
unless `u` is near the archived balance. [T0/T1]

For the balanced port I used

`u*(m,a)=m a/(1+2a(m-1)+4m^2a^2)`.

This is the elementary balance between the basis-row negative mass
`u(1+2a(m-1))` and the signed-row negative mass
`m a(1-4mau)` in the `eps=0` model.  The table below is not the model: it is
the exact `eps=1/1000` full theta-half enumeration written to
`runs/2026-07-02-undercap-killers/data/undercap_killers.csv`. [T0/T1]

### m=5 staircase tradeoff

| row | `a` | `u` | `delta` | cap? | `Phi/delta` | `sum Phi/delta` | active pivots `Phi_s>delta/2` | `max E/delta` | `V/delta` |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| archived B6 | `1/2` | `1/10` | `1/2` | no | `1` | `5005003/1000000` | `5` | `10` | `1/500000` |
| balanced | `1/5` | `5/33` | `13/33` | no | `26000099/26000000` | `7384623/2000000` | `6` | `66/13` | `33/13000000` |
| balanced | `1/6` | `15/92` | `35/92` | no | `17500069/17500000` | `55000069/17500000` | `1` | `92/21` | `23/8750000` |
| balanced | `1/8` | `10/57` | `20/57` | no | `40000171/40000000` | `90000171/40000000` | `1` | `57/16` | `57/20000000` |
| balanced | `1/10` | `5/28` | `9/28` | no | `1500007/1500000` | `7000021/4500000` | `1` | `28/9` | `7/2250000` |
| balanced | `1/12` | `3/17` | `5/17` | no | `10000051/10000000` | `10000051/10000000` | `1` | `17/6` | `17/5000000` |
| balanced | `1/16` | `20/121` | `30/121` | yes | `20000121/20000000` | `20000121/20000000` | `1` | `121/48` | `121/30000000` |
| balanced | `1/20` | `5/33` | `7/33` | yes | `14000099/14000000` | `14000099/14000000` | `1` | `33/14` | `33/7000000` |

The collapse is discontinuous relative to the cap target: the many-active
behavior dies between `a=1/5` and `a=1/6`, while the cap is not entered until
between `a=1/12` and `a=1/16`.  High `E/delta>3` survives to `a=1/10`, but
still outside the cap.  Tiny positive `V` does port under the cap. [T0/T1]

### rank-scaled cap rows

The cap-scale choice `a=1/(4m)` keeps the balanced staircase under the cap for
the checked ranks, but every selected chart has one active pivot and
`Phi/delta` essentially `1`. [T0]

| `m` | `a` | `delta` | `Phi/delta` | active pivots | `max E/delta` | `V/delta` |
|---:|---:|---:|---:|---:|---:|---:|
| `2` | `1/8` | `5/24` | `1250009/1250000` | `1` | `12/5` | `3/625000` |
| `3` | `1/12` | `4/19` | `8000057/8000000` | `1` | `19/8` | `19/4000000` |
| `4` | `1/16` | `11/52` | `5500039/5500000` | `1` | `26/11` | `13/2750000` |
| `5` | `1/20` | `7/33` | `14000099/14000000` | `1` | `33/14` | `33/7000000` |
| `6` | `1/24` | `17/80` | `425003/425000` | `1` | `40/17` | `1/212500` |
| `8` | `1/32` | `23/108` | `11500081/11500000` | `1` | `54/23` | `27/5750000` |

Verdict for T1: the B6 staircase killers do not port as high-`E`, high-sum, or
many-active obstructions under `delta<=1/4`.  The only B6 mechanism that ports
is `V>0`, and it ports at tiny scale. [T1]

## T2. Free-Form Adversarial Construction

The useful new witness is not a staircase.  It is the decoupled multiblock fan
mechanism from A3, now measured for active pivots.  The Hadamard reduction
certifies the whole theta-half class: all foreign unit rows plus one signed row
per anchor.  In that class each anchor pivot contributes independently, so
`max_s Phi_s` remains bounded while `sum_s Phi_s` and the number of active
pivots grow with the number of anchors. [T0/T1]

### certified under-cap active-pivot witnesses

| family | parameters | `delta` | `max Phi/delta` | `sum Phi/delta` | active pivots | `max E/delta` | `V/delta` | certification |
|---|---|---:|---:|---:|---:|---:|---:|---|
| two-anchor overlapping stars | foreign `5`, centers `0,4` | `1/100` | `11/8` | `11/4` | `2` | `2` | `0` | Hadamard reduction, `64` charts |
| repeated star | foreign `5`, anchors `3` | `1/100` | `11/8` | `33/8` | `3` | `2` | `0` | Hadamard reduction, `512` charts |
| repeated star | foreign `5`, anchors `5` | `1/100` | `11/8` | `55/8` | `5` | `2` | `0` | Hadamard reduction, `32768` charts |
| complete vs star | foreign `4` | `1/100` | `3/2` | `17/6` | `2` | `2` | `0` | Hadamard reduction, `72` charts |
| complete vs star | foreign `8` | `1/100` | `7/4` | `89/28` | `2` | `2` | `0` | Hadamard reduction, `784` charts |

This is decision-grade for target (a): `>=2` active pivots at a certified
under-cap `Phi`-argmin.  In fact, the repeated-star rows show that any proof
step of the form `sum_s Phi_s = O(max_s Phi_s)` is false without normalization
or a genuinely max-based argument. [T0/T1]

Target (d) is also hit, but only weakly: the balanced staircase has selected
`V/delta=121/30000000` at `delta=30/121`.  Thus `V=0 at an argmin` is false
under the cap, but the witness gives no large-`V` obstruction. [T0]

Targets (b) and (c) were not hit:

- Best under-cap `max E/delta` in the new bundle is `121/48` on the
  `m=5,a=1/16` balanced staircase; the cap-scale rows stay near `2.4`, and
  multiblocks have `max E/delta=2`. [T0]
- Best under-cap selected `max Phi/delta` in the new bundle is `7/4`; existing
  certified A2/A3 rows reach `27/14` and `28/15`, still below `2`. [T0:
  `runs/2026-07-02-ex-no-center-highrank/`,
  `runs/2026-07-02-ex-multiblock-coupling/`]

I did not find an under-cap plateau breaker `max Phi/delta>2`. [T1]

## T3. Obstructions And Candidate Lemmas

### Refuted candidates

**At most one active pivot at an argmin** is false.  The repeated-star rows give
`active=2,3,5` under the cap with exact certificates.  The same construction
plainly scales by adding decoupled anchors, so no fixed active-pivot count
should be trusted without an additional coupling hypothesis. [T0/T1]

**Unnormalized aggregate-sum control** `sum_s Phi_s(U*) <= C delta(P)` is false
as a dimension-free proof target for the selected chart: repeated-star rows
have `sum Phi/delta = 11g/8` for `g=2,3,5` anchors while
`max Phi/delta=11/8`.  This directly threatens the A5 "probabilistic
sum_s interface" unless it is normalized, localized, or replaced by a max-based
charge. [T0/T1]

**`V_s(U*)=0` under the cap** is false: balanced staircase `m=5,a=1/16` gives
`V/delta=121/30000000`. [T0]

### Elementarily provable survivor

For every chart and pivot,

`V_s(U) <= Phi_s(U)/2`.

Proof: on a row with `lambda_s(j)<0`,
`E_s(j)=sigma_s(j)+2(-lambda_s(j)) >= 2(-lambda_s(j))`; on rows with
`lambda_s(j)>=0`, the `V` contribution is zero.  Multiplying by
`beta_s(j)_+` and summing gives the inequality. [T1]

This explains why the under-cap `V>0` hit is not dangerous for the plateau
picture when `Phi` is small. [T1]

### Unbroken candidates

1. **Plateau-2 argmin bound.** For every exact signed idempotent with
   `delta<=1/4`, every theta-half `Phi`-argmin satisfies
   `max_s Phi_s(U*) <= 2 delta(P)`.  Tested against A2/A3/A4/A5 benches and
   this bundle; still unbroken, not proved. [T2]

2. **Selected pointwise `E` cap.** At a theta-half `Phi`-argmin under
   `delta<=1/4`, `max_{s,j} E_s(j) <= 3 delta(P)`.  The staircase rescale
   explains the obstruction in that family: under the cap the amplitude must be
   small enough that `E/delta` drops below `3`.  Tested here, but not proved and
   not obviously needed downstream. [T2]

3. **Max-based, not sum-based, aggregate charge.** A useful GAP-B statement
   should control each pivot or the maximum over pivots directly; any proof that
   first sums over all active pivots needs a normalization or quotient measure
   that kills decoupled-anchor amplification. [T2]

## T4. Verdict

**Killers that port under the cap.** Active-pivot multiplicity ports, and in
decoupled-anchor form it likely scales without bound.  Tiny positive selected
`V` also ports. [T0/T1]

**Killers that did not port.** The B6 staircase high-`E`, many-active, and
high-sum behavior collapses before `delta<=1/4`.  No certified construction in
this wave gives `max Phi/delta>2` or `max E/delta>3` under the cap. [T0/T1]

**Threat to plateau-2.** None found.  The strongest certified max ratios remain
below `2`: repeated active pivots amplify `sum Phi`, not `max Phi`. [T1]

**Sharpest surviving statements, ranked.**

1. `max_s Phi_s(U*) <= 2 delta(P)` at a theta-half argmin: unproved but most
   useful for GAP B and still exactly unbroken. [T2]
2. `V_s <= Phi_s/2` for every chart and pivot: elementary and useful cleanup,
   but not enough to prove `(EX)`. [T1]
3. `max E <= 3 delta` at an under-cap argmin: unbroken evidence, lower
   usefulness because pointwise `E` is not the right final charge. [T2]
4. Any active-count or unnormalized `sum_s Phi_s` lemma: refuted / dead for
   this route. [T0/T1]

**Next-wave recommendation.** Pivot away from unnormalized total
`sum_s Phi_s`.  Attack a max-based exchange/charge lemma, or deliberately
construct genuinely coupled anchors where the theta-half chart cannot choose
each anchor independently.  Non-uniform anchor weights, shared signed rows, or
non-paired shear sets are the next plausible plateau-breaker attempts. [T1/T2]
