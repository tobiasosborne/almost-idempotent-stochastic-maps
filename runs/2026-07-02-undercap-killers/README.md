# Run bundle: under-cap (EX) mechanism killers - 2026-07-02

**Status: L3 numerical evidence. NEVER rigorous.** All certified quantities are
computed over exact rationals with SymPy; there are no certified float fields.

## Hypothesis

Can any mechanism-killing behavior for the `(EX)` chart bound survive under the
campaign cap `delta(P) <= 1/4`?  This bundle focuses on active pivots at a
theta-`1/2` `Phi`-argmin, and records exact near-misses for high `E/delta`,
positive `V`, and selected `Phi/delta > 2`.

## Command

```bash
python3 runs/2026-07-02-undercap-killers/scripts/certify_undercap_killers.py
```

The command writes:

```text
runs/2026-07-02-undercap-killers/data/undercap_killers.csv
```

## Finding

A decision-grade active-pivot witness exists under the cap: multiblock charts
with `delta=1/100` have certified theta-half `Phi`-argmins with multiple active
anchor pivots satisfying `Phi_s > delta/2`.  Repeated-star rows certify
`active=3` and `active=5` with the same `max Phi/delta = 11/8`; the two-anchor
row has `sum Phi/delta = 11/4`.

The same exact table also finds tiny positive selected `V` under the cap in the
balanced staircase rows, e.g. `V/delta = 121/30000000` at `delta=30/121`.  It
did not find an under-cap selected chart with `max E/delta > 3` or
`max Phi/delta > 2`.  The balanced staircase rows show the archived many-active
staircase behavior collapsing before the cap is entered.

## Invariant / certificate

- The script asserts that at least one emitted row has `under_cap=True` and
  `active_pivots_gt_delta_half >= 2`.
- For multiblock rows, `BL=I`, row sums, direct `delta`, and harmonic `DEF` are
  checked exactly; the Hadamard bound `4*R2*a^2 < 1/4` certifies that omitted
  bases are outside the theta-half class.
- For staircase rows, every actual-row basis is fully enumerated; `BL=I`,
  `P^2=P`, row sums, and harmonic `DEF` are checked exactly.


- **Orchestrator independent recomputation (2026-07-03):** the decision-grade row
  `multi_anchor_repeated_star, anchors=3, foreign=5, a=1/100` was recomputed with
  fresh, bundle-independent `fractions.Fraction` code (full 512-chart sweep):
  `BL=I`, `P^2=P`, row sums, `delta=1/100` confirmed; argmin `max_s Phi_s/delta
  = 11/8`, `sum_s Phi_s/delta = 33/8` at the argmin, `3` active pivots — exact
  match with the CSV row.

## Next

Use the two-active-pivot witness to avoid any proof step that replaces
`sum_s Phi_s` by `max_s Phi_s` for free.  The remaining live construction target
is a genuinely coupled under-cap family with selected `Phi/delta > 2`, high
`E/delta > 3`, or positive `V` at an argmin.
