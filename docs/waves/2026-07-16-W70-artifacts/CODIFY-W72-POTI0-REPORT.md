STATUS: UNAUDITED TRANSCRIPTION

# W72 POTI-0 codification report

## Files touched

- Six new registry shards under `argument/lemmas/`:
  `conj-w72-poti0-exact-cause-split`,
  `conj-w72-poti0-root-selection-exchange-ledger`,
  `conj-w72-poti0-fixed-level-starvation-ledger`,
  `conj-w72-poti0-root-dilution-selected-support-exchange`,
  `conj-w72-poti0-low-deficit-huddle-ray-48`, and
  `conj-w72-poti0-routine-conditional-assembly`.
- `argument/INDEX.md` and `argument/DAG.md` (generated).
- `report/UNWIRED.md` (the six exploration-track ids are deliberately unanchored from the paper track, matching the existing POTI/DTR-era handling).
- This report.

No definition was added or changed. `definitions/INDEX.md` was regenerated only if the required idempotence gate changed it.

## Registry transcription

| id | status | one-line contract |
|---|---|---|
| `conj-w72-poti0-exact-cause-split` | `proved-mod-audit` | Every pinned clone-invariant W72 POTI-0 datum with `G_phi = 0` lies in exactly one of `r = 0` or `r > 0` with `t_phi(u) <= D_0*delta(P)` on positive `rho`-mass. |
| `conj-w72-poti0-root-selection-exchange-ledger` | `proved-mod-audit` | On the pinned `r = 0` subclass, the forced full-fiber RX package satisfies `sigma_B >= w_*M_B - e_delta`. |
| `conj-w72-poti0-fixed-level-starvation-ledger` | `proved-mod-audit` | On the pinned positive-overlap orientation-starved subclass, the forced fixed-level statistic satisfies `H_48 > tau/16`, with `z = 48*tau` on the high side. |
| `conj-w72-poti0-root-dilution-selected-support-exchange` | `conjecture` | On the pinned `r = 0` subclass equipped with the forced RX package, every arbitrary attained top-face ray obeys the exact RAY-EC inequality. |
| `conj-w72-poti0-low-deficit-huddle-ray-48` | `conjecture` | On the pinned orientation-starved subclass equipped with the forced O48 package, every arbitrary attained top-face ray obeys the exact RAY-EC inequality. |
| `conj-w72-poti0-routine-conditional-assembly` | `proved-mod-audit` | Assuming RDSE and LDHR-48, the verified S0/RX/O48 split and exact B4/ray assembly give `Z_v(q_A) > (7*c_m/960)*tau` for every pinned POTI-0 datum with `G_phi = 0`. |

All six shards have `af: none`. RDSE and LDHR-48 have empty dependency lists. ASM2 names both conjecture premises in its contract and dependency list.

## Dependency audit

- S0 consumes only `lem-dtr-canonical-overlap`.
- RX consumes exactly `lem-ihorn-cotop-sl1a-package`, `lem-ihorn-selected-corner-extraction`, `lem-dcap-root-closure`, `lem-dtr-canonical-overlap`, and `lem-l5-positive-flow-foldback`.
- O48 consumes exactly `lem-dtr-canonical-overlap`, `lem-top-deficit-price`, `lem-aesc-synthetic-finance-tail-amplification`, and `lem-l5-positive-flow-foldback`.
- ASM2 consumes S0, RX, O48, the two named creative premises, `lem-l5-top-face-ray-formula`, `lem-dcap-tall-same-center-packet`, and `lem-ihorn-tall-halo-saturation`.
- No `lem-icap-*`, `lem-huddle-charge-assembly`, `lem-intersection-branch-production`, or `lem-dtr-poti-assembly` shard is consumed.

## Gate outputs

```
$ python3 scripts/check-defs.py --check && python3 scripts/check-defs.py --generate-index
check-defs: 23 shards, 0 errors, 14 warnings
wrote definitions/INDEX.md (23 terms)
check-defs: 23 shards, 0 errors, 14 warnings

$ python3 scripts/argument.py
wrote argument/INDEX.md + DAG.md (214 results)
argument: 214 results, 32 ready, 100 blocked, 0 errors, 6 warnings

$ python3 scripts/check-provenance.py --check
check-provenance: 214 registry results, 62 claim rows, 110 tex labels — 0 errors, 153 warnings

$ sh scripts/check-all.sh
[check-all] OK
```

The warnings are the repository's existing draft-definition, large-af-tree, hash-freshness, off-paper whitelist, and report-coverage warnings; none is a W72 gate error.

## Defect register

- None. The S0, RX, and O48 pinned contracts agree with the appendix statements marked verbatim; the ASM2 strict conclusion agrees with the appendix proof. RDSE and LDHR-48 were registered as conjectures and were not treated as proved.
- The attack and appendix predate the hostile verdict and label all nodes proposed/conjectural. Per the codification brief and `VERDICT-poti0-batch.md`, only S0, RX, O48, and ASM2 were retagged `proved-mod-audit`; this is metadata reconciliation, not a mathematical change.
- No new or unregistered non-textbook term was required; there is no `RATIFICATION NEEDED` item.
