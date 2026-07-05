<!--
WAVE: decision-check DC2 (direct NSC-ratio search — arm G wave 14, refute side) — 2026-07-05, session 8.
WORKER: fresh codex exec (prompt: session scratchpad PROMPT-dc2-nsc-ratio.md). Worker answer VERBATIM below.
ORCHESTRATOR: worker script rerun clean (exit 0). **Headline REFUTATION independently recomputed
  with orchestrator-authored code** (runs/2026-07-05-nsc-zero-denominator-refuter/scripts/
  orch_verify_refuter.py — takes ONLY the P matrix from the certificate JSON; re-derives
  coordinates, volumes, theta-half census, unique argmin (0,3,4) with Phi=(0,0,0),
  B_{1,0}=1/4020000000, single carrier with nu=0): CONFIRMED. Broad conj-nsc is DISPROVED
  (zero-denominator mode); shard flipped; run bundle = the death certificate.
SCOPE (orchestrator): kills the broad charging shape only — B ~ 2.5e-10 << delta and Phi ≡ 0 at
  the argmin (no clean high-self non-fan Gamma branch), so the branch-restricted B-lemma target
  B <= K*delta is untouched. Successor shape escalated to the user.
TIER: T0 refutation certificate (orchestrator-confirmed); T1 amplifier-family ratio law.
-->

# DC2 NSC-Ratio Direct Search Report

## Verdict

[T0] Broad `conj-nsc` is refuted by an exact rank-3 signed idempotent with

```text
B_{1,0}=1/4020000000 > 0
SUM_carriers=0
```

at capped theta-half Phi-argmin `U=(0,3,4)`, maximal pivot `s=0`, transverse `r=1`.

The carrier row is entrywise nonnegative in the ambient idempotent, so its `nu_i(P)` is exactly zero. This is the zero-denominator refutation mode, not a large finite lower bound for `K0`.

## Re-run

```bash
python3 waves-scratch/dc2-nsc-ratio/nsc_ratio_search.py
```

Artifacts:

```text
waves-scratch/dc2-nsc-ratio/ANSWER.md
waves-scratch/dc2-nsc-ratio/nsc_pair_table.csv
waves-scratch/dc2-nsc-ratio/nsc_certificates.json
waves-scratch/dc2-nsc-ratio/nsc_ratio_search.py
```

(Banked copies: `runs/2026-07-05-nsc-zero-denominator-refuter/`.)

## Refuting Certificate

Two-carrier parameters `(p,e,q,g,v,w)`:

```text
(1/200, 1/100, 0, 1/200, 20099999/20200500, 1/1000)
```

`delta(P)=20099999/4040100000 <= 1/4`.

Complete theta-half argmin result:

```text
unique theta-half argmin: U=(0,3,4)
m=1
phi=(0,0,0)
```

Refuting pair:

```text
s=0, r=1
B=1/4020000000
SUM_carriers=0
```

Only carrier:

```text
i=1
a=(-1/40399, 200/40399, 40200/40399)
beta=40399/4020000000
a_s=-1/40399
nu=0
B_contrib=1/4020000000
volume-inadmissible=True
```

## Known Witness Reconstruction

The script hard-asserts the three requested known ratios:

| instance | pair | B | SUM_carriers | R |
|---|---|---:|---:|---:|
| `insert-y=681/10000` | `U=(0,2,4), s=2, r=1` | `42/985` | `18664233/500000000` | `200000000/175088281` |
| `two-carrier-B` | `U=(0,2,4), s=2, r=1` | `3/50` | `53757/2500000` | `50000/17919` |
| `G12-calibration` | `U=(0,1,2), s=2, r=1` | `2/57` | `8/513` | `9/4` |

It also recomputes every transverse pair at every maximal pivot; see `nsc_pair_table.csv`.

## Search Notes

[T0] A three-carrier split of the zero-nu carrier was also certified: three volume-inadmissible zero-`nu` carriers split the same `B` mass and still have `SUM_carriers=0`.

[T1] Along the amplifier boundary family,

```text
R_amp(a) = (12/197) / (1929/100000 + (49/50)*(a+1/2)*2679363/(49000*(22a+799))).
```

At `a=6332623/370881409` this gives

```text
R_amp=59294712699400000/52518828228799361 ≈ 1.129018
```

so the amplifier family is not the NSC-ratio stress.

## Hard Asserts

[T0] For every reported matrix: `B_left * L = I_3`, `P=L*B_left`, `P^2=P`, row sums are `1`, `0<delta(P)<=1/4`, and all actual-row charts are enumerated exactly with `fractions.Fraction`.

[T0] `python3 -m py_compile waves-scratch/dc2-nsc-ratio/nsc_ratio_search.py` passes.
