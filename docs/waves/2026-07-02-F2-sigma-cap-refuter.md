<!--
ROLE: verbatim harvest artifact of fr arm F, wave 2 (2026-07-02). Worker: opus:prover (subagent).
STATUS: L3 numerical + [check] heuristics (L0). Instance C's core arithmetic independently recomputed
by the orchestrator (fresh code: P^2=P over Q, delta=252559/1280000, P_vv=5343/5000) — confirmed; the
wave's certify.py / halo_bound_check.py re-run clean. Scripts re-homed:
runs/2026-07-02-sigma-cap-refuter/. Referenced by .frontier/log.jsonl (arm F wave 2) and bd aism-kpl.
-->

# Arm F · wave 2 · σ̃-cap KILL attempt (refuter) — harvest (verbatim report)

**L3 numerical evidence + [check] mechanisms. Nothing here is proved. Key instances certified EXACT (ℚ) and clone-invariant.**

## 1. Calibration confirmation (exact)

Pipeline reproduces both anchors exactly: s5 (δ=1841/1600000, H=1/1000, W={0,1,2}, hidden={3,4}, σ̃=1/2000; clone-invariance holds) and the wave-1 headline (PRIMAL=DUAL=LP H=1/20, H/δ=100/49). exact_lp self-test 0/300 fails.

## 2. The reframing that governs everything

The finisher combines with the **af-validated** collapse bound `H(1−σ̃) ≤ ν(2+4δ) ≤ 3δ`, so `1−σ̃ ≤ 3δ/H`. Hence **`1−σ̃ = o(τ)` ⟺ `H = ω(τ)` (super-linear height)** — killing the cap is *equivalent* to entering the never-entered dangerous regime. There is no cheap self-mass kill that leaves H small; the two are tied. The one loophole: if σ̃ ≥ 1 the collapse bound goes **vacuous** (LHS ≤ 0). That is the door I forced — and it turns out to be a **halo/self door**, not a real one.

## 3. Families table (each row = the frontier extremum of a family)

| family (script) | params | min (1−σ̃)/τ | δ there | H/τ there | binding constraint at stall |
|---|---|---|---|---|---|
| symmetric twin, tail-mass knob (`exp8/8b/9b`) | p=poke, r=self+twin mass | 3.71 (σ̃/τ=0.25) | 0.0636 | 0.079 | **EXPOSEDNESS**: raising tail mass lifts twins into fresh coords; t\*(v) jumps 0.024→**1.0** |
| **self-mass single row** (`certify.py`, C) | large-δ poke | **−0.154 (σ̃=1.069>1)** | 0.1973 | **0.020** | **HALO + δ-budget**: σ̃>1 is *all* self-mass P_vv=5343/5000 at v-dist 0.02τ; genuine σ̃(dist≥τ/4)=**0** |
| max genuine invisible mass (`search4f Sg`) | k≤5,m≤4 | 4.54 (σ̃_g/τ=**0.368**) | 0.0415 | 0.416 | **RECIPIENTS-EXPOSE**: genuine outside rows become the (ρ,κ)-exposed frontier → absorbed into C_W |
| max H/τ w/ genuine σ̃ (`search4f Ht`) | k=3,m=2 | 4.30 (σ̃_g/τ=0.332) | 0.0466 | **0.462** | **corner/exposedness cap** H/τ→0.536; distinct genuine partner exists but carries 0.0115 |
| σ̃>τ joint push (`search4f joint`) | k≤5 | 0.03 (σ̃/τ=2.83) | 0.122 | 0.026 | anti-correlation: σ̃ up ⟹ H→0 (all halo) |
| rank-growing towers (`search4f`, KCH≤7 MCH≤6) | k=4–7,m=3–6 | — (σ̃_g=0) | 0.25 | 0.020 | **collapses**: too many rows to keep hidden → expose/interior |

**Aggregate:** over ~25k float-searched hidden top vertices, **genuine invisible mass σ̃_g (recipients at dist ≥ τ/4) never exceeded ≈0.37τ**, i.e. `1−σ̃_g ≥ 0.92` everywhere. Total σ̃ (ε=0) reaches σ̃/τ≈2.9 and σ̃>1 — but only via self/halo. Max H/τ found = **0.462 < corner 0.536**. The joint (σ̃>τ ∧ H>Bτ) was **not entered** (confirms record).

## 4. Best instances (EXACT, clone-invariant)

**C — the ε=0 cap literally FALSE (self-mass), δ=`252559/1280000`≈0.1973.** Generator `build_from_LambdaC`, C=`[[28/25,1/200,0,−1/8]]`, R2=`[[−49/800],[−1/6],[−1/8],[−33/800]]`. Hidden top vertex (t\*=1/25≪κ, robust): **σ̃=`5343/5000`=1.0686 > 1 ⟹ 1−σ̃=−0.0686 < 0 < cτ**. But σ̃ is **entirely self-mass P_vv=5343/5000**, recipient = v itself at dist **0.0200τ** (deep ε-halo). σ̃ restricted to dist≥τ/4: **exactly 0**. → **ε-halo ONLY. Does NOT kill the cap** (and H/τ=0.02, nowhere near dangerous).

**A — max genuine invisible mass, δ=`3983/96000`≈0.0415.** C=`[[−3/80,23/400,5/12,−1/200,341/600]]`, R2=`[[3/80],[1/100],[1/16],[1/96],[7/80]]`. Hidden top vertex v=5, H/τ=0.4164, **σ̃=σ̃_g=`5991/80000`≈0.0749, σ̃/τ=0.368, 1−σ̃=0.925**. Recipient = self at **0.416τ** (genuine, but self). Collapse bound holds exactly.

**B — max H/τ with a genuine DISTINCT recipient, δ=`74551/1600000`≈0.0466.** C=`[[1/2,−1/20,11/20],[257/400,−7/200,157/400]]`, R2=`[[9/200,1/80],[1/200,1/200],[11/160,1/100]]`. Hidden top vertex v=3, **H/τ=0.4617** (near corner), σ̃=`229/3200`≈0.0716, σ̃/τ=0.332. Recipients: self @0.462τ (P=`961/16000`) **and a distinct partner row 4 @0.323τ** (P=`23/2000`) — both genuine (dist≥τ/4). `1−σ̃=0.928`.

**Brutal honesty:** the only place `1−σ̃ ≤ 0` is reached (instance C) the recipient is v's own self-mass at 0.02τ — pure halo. Every configuration with **genuinely-outside recipients (dist ≥ τ/4)** has σ̃ ≤ ~0.07 absolute, `1−σ̃ ≈ 0.93`. The cap survives on genuine recipients with margin ≈4τ, not merely cτ.

## 5. VERDICT — **PARETO-MAP (cap survives) + ALGEBRAIC-WALL-CANDIDATE**, with a bankable exact sub-refutation

- **NOT a kill.** The halo-robust σ̃-cap (`1−σ̃_g ≥ c`) **survives with margin `1−σ̃_g ≥ 0.92`** across all families incl. rank-growing towers.
- **Bankable exact fact:** the cap *as literally written* (ε=0 invisible mass) is **FALSE** — exact certificate σ̃=5343/5000>1 (instance C) via self-mass. Exactly the halo-non-robustness flagged in `def-invisible-mass`. A finisher must state the cap halo-robustly; the ε=0 form is not literally true.
- **[check] WALL — "no-free-frontier / exposedness-absorption":** σ̃_g>0 needs v's positive mass on rows genuinely outside C_W; those rows occupy separating directions, so the extremal one in each direction is (ρ,κ)-exposed → joins W, extending C_W to absorb the near-outside rows. Only **mutual-shield twins at equal extremity** persist, and their hostable mass is bounded by the poke depth ∝ ν = O(τ). Hence σ̃_g ≲ 0.37τ.
- **[check] halo-robust collapse bound**: `H(1−σ̃_g) ≤ (σ̃−σ̃_g)·τ/4 + ν(2+4δ)` — verified EXACT and non-vacuous on all three certified instances (gives H ≤ 0.45–0.70τ). Immune to the self-mass loophole.

## 6. NEXT PULL

1. Bank `obs-sigma-halo-nonrobust` + the genuine-σ̃_g-ceiling numbers; never re-quote the ε=0 cap.
2. Re-scope the finisher to the halo-robust cap `1−σ̃_g ≥ c`; af-elevate the halo-robust collapse bound.
3. Point the af elevation at the WALL: the clone-invariant core is *a row extremal in a C_W-separating direction, with all nearer rows within ρ, is (ρ,κ)-exposed*.
4. Do not chase σ̃>1 via self/halo (cheap, halo-only) or rank-growing towers (collapse). The frontier is genuine σ̃_g→1, which needs H≫τ — still walled at H/τ≤0.462.
