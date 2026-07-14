# Run bundle: W69 DTR growing-rank decider — PARTIAL: local DTR geometry realized with ZERO finance negativity at ranks 4-32, but 0 full class entrants and 0 refuters (2026-07-14, session 20)

## Hypothesis

bd `aism-72zn`/`aism-cmk0` / AESC-ATTACK-W67.md §4.2 (DTR target): can the
diffuse-tail ray conversion residual `conj-w67-aesc-diffuse-tail-ray-conversion`
be refuted — or its hypothesis class (1.22) even entered — by an exact
GROWING-RANK family (no clones, no transients) that distributes W55's
order-one finance negativity across many rows? A genuine refuter needs the
full pinned package (exact P = LB, BL = I, tall H > 16τ, legal far selection,
nonempty ultra ω, the D-certificate, all R0/B1–B5/R1 outputs, hull-near
row-far actors, Tail₁ > τ/8, P_f*⁺(U_tail) > τ/2560) and 𝓓_leaf < 0. The
diagnostics 𝓓_EC (refutes only the stronger (EC) residual contract) and
𝓓_leaf (refutes the leaf) are NOT interchangeable. (Rigour tag: `numerical`
— exact rational L3 evidence, never proof.)

## Finding

**PARTIAL — the local DTR geometry IS realizable at growing rank with
exactly ZERO finance negativity, but no tested family enters the full class
and none refutes the leaf.** Fresh codex xhigh worker, exact rationals,
orchestrator-reproduced 2026-07-14 (exit 0):

- **The exact family** (per rank m ∈ {4,8,16,32}: τ = 1/(2²⁰m), anchors
  L_a = e_j, probes L_u = c + (τ/20)·d_s with cyclic differences d_s,
  center L_v = c, B = (I_m 0 0); BL = I_m so P² = P; certified rank = m,
  genuinely growing) realizes carrierwise: h_u = 0 ≤ 3δ (hull-near),
  min-row distance > 3δ (row-far), rotating incidence, Tail₁ = 1/16 ≫ τ/8,
  P_f*⁺(U_tail) = 1 > τ/2560, and **maximum single-row negativity exactly 0
  at every rank** — rank really can distribute W55's finance cost to zero
  locally. The local diagnostic 𝓓_EC = −7/64 < 0.
- **But every GLOBAL gate fails by an exact margin, uniformly in rank:**
  R0 carrier ownership η_D* ≤ P_f*⁺ violated by excess exactly 1/8; the
  center is not a hidden vertex (H − 16τ = −16τ, i.e. H/τ = 0); shallow mass
  P_v⁺(𝓛_v) = 1 (vs the B4 budget < 2τ/15); ultra ω empty; hence B1–B5/R1
  unavailable and **𝓓_leaf > 0 at every rank** (e.g. 134217727/8589934592
  at m = 32). The rank-trend table shows NO gate margin improving with rank.
- **Unit tests both pass:** the W66/W63 plateau still routes to C0
  (ℓ/τ = 2τ), fails tallness, 𝓓_leaf > 0; the W55 A₀ = 5 completion
  reproduces its exact order-one finance negativity AND its actor residual
  ≤ 3δ routes it away from DTR (it is a T-esc shape).

**HONEST SCOPE:** bounded search over named families; no emptiness claim;
𝓓_EC < 0 here is a statement about an ILLEGAL (non-entrant) local probe, not
about the residual contract on its class. **Decision take-away for the
creative wave:** rank distributes the LOCAL finance cost for free, so the
DTR proof cannot win by charging single-row negativity; the wall a refuter
cannot cross (in every tested family) is the GLOBAL package — root
ownership + tallness + the ultra/shallow budgets. The creative mechanism
should therefore price root-to-top synchronization (exactly the W67 §1.6(c)
hard core), not local negativity.

## Command

```bash
cd runs/2026-07-14-w69-dtr-growing-rank-decider/scripts
PYTHONDONTWRITEBYTECODE=1 python3 -u search.py   # deterministic, no seed; exact Fractions
```

## Invariant (checkable)

Every claim is an exact `fractions.Fraction` assertion in `search.py`:
P = LB and BL = I entrywise (hence P² = P), certified rank = recurrent
support = m, row sums, per-row negativities (exactly 0 for the family),
hull-membership/row-distance certificates for h_u and min_f ||p_f − x_u||₁,
the tail and union quantities, the R0 ownership excess (exactly 1/8), the
foldback overflow ≤ e_δ, both diagnostics 𝓓_EC and 𝓓_leaf reported
separately, the rank-trend table, and both regression fixtures. Exits
nonzero on any mismatch; prints the verdict + rank-trend + two unit-test
lines + "PARTIAL — 0 full DTR entries and 0 refuters; exact L3 evidence
only, never a proof" (orchestrator-reproduced 2026-07-14, exit 0).
`data/certificates.json` freezes all exact values (sha256
d33332e84c038737c5909fb3b92e17b2e49db134cf53feea468717a5564e45e5).

## Next

Feeds the W69 DTR creative wave (attack doc in flight at close; downstream
pipeline = bd aism-cmk0): the mechanism should target the global
root-to-top synchronization package, not local negativity. A future refuter
attempt must show a gate margin that IMPROVES with rank — none did here.
