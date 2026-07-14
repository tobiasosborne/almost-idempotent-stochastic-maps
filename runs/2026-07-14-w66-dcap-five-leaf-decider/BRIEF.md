# W66 L3 decider batch — the five D-cap leaves (N / G<4 / C0 / A-esc / T-esc), exact arithmetic

You are a fresh, independent worker. Your workspace is this directory (registry
snapshot `argument/` + `definitions/` + `context/`). Everything you produce stays
inside it. This is an L3 (constructive/numerical evidence) job: **nothing you
produce is a proof**, and your report must say so.

## Target

`context/DCAP-ATTACK-W65.md` §4.2 — the pre-creative decider shapes gating the
five creative leaves of the W65 D-cap decomposition: **N** (near disjoint
hulls), **G<4** (natural gap, zero-face gauge below four), **C0** (large-gauge
collapsed zero-face cloud), **A-esc** (actorization escape), **T-esc**
(scalar-tail escape). Read that artifact IN FULL, including §1.1 (pinned
objects; it adopts `context/DECOMPOSITION-W63-I.md` §§0–1.1 verbatim — read
those too: I-base datum, b = c_m/128 with c_m = 1/4 working threshold, k_b,
D_0 = 2+4δ, e_δ = 2δ(1+δ), r_ω, scalar width Ω, θ and the depth rim, λ_A, the
selected-corner certificate and M_X/M_I/M_D). The SEVEN routine nodes of the
W65 tree are PROVED registry shards `argument/lemmas/lem-dcap-*.md` — consult
them (esp. root closure, tall same-center packet, the five-way 1/80 split, and
the B5 closed overlay in its verifier-corrected Ξ_X form; see
`context/VERDICT-W65-DCAP-BATCH.md` for the (B5.C) correction). Your candidates
must live WITH those theorems, and compute the true dual value Z_v(q_A) exactly
via the proved `lem-l5-top-face-ray-formula`.

## The gate every genuine candidate must pass (exact rationals — §4.2)

A genuine refuter sequence consists of exact rational factorizations
P_k = L_k B_k with B_k L_k = I (this certifies P_k² = P_k), with:

- τ_k → 0, δ_k = τ_k², EVERY row negativity ≤ δ_k;
- the FULL I-base/all-center hypotheses (nonempty visible set W, hidden top
  vertex v, S ≥ 1/4, all-center inequalities);
- tallness H_k > 16·τ_k  — **this has been the binding wall in FIVE consecutive
  exact batches** (see context/seeds/*/README.md); attack it head-on; a short
  gadget without tallness is evidence only;
- the ultra bounds of the pinned D-cap antecedent: ‖r_ω − p_v‖₁ < b·τ,
  Ω(ω) < b·τ, and θ_k < τ_k/D_{0,k};
- an EXHIBITED fixed D-certificate satisfying (1.1):
  M_X ≤ 1/8, M_I < 1/16, M_D > 1/16  (note: the W63 natural diagonal plateau
  had M_I = 0 exactly and routed to D with mass 1023/1024 — the D cell IS
  enterable at certificate level; the open wall is tallness + the leaf
  predicates);
- the true ray value verified exactly, with Z_{v_k}(q_{A,k})/τ_k → 0  (4.1).

## Mandatory print panel (every run, per §4.2)

Print, as exact Fractions with pass/fail:

- m_D* > 1/16;
- sup_{0≤g≤1} (Π_D*(g) − P_{f*}^+(g)) ≤ e_δ;
- P_v^+(𝓛_v) < ℓ_T < 2τ/15  (𝓛_v = {Q : d_Q ≤ τ/4});
- P_v^+(𝓔_*) ≥ τ·S/8   (4.2);
- EXACTLY ONE B5 overlay label among X_gap/X_near/I_far/I_near/D_gap/D_near,
  including (B5.1)–(B5.2) in BI/BD and the six exact overlay targets (B5.3);
  in particular D_gap and D_near must print the c_m/3072 inequalities and the
  near guard;
- the proposed leaf deficit
  𝓓_leaf := Z_v(q_A) − c_m·τ/64 + (c_m/16)·P_v^+(𝓛_v)   (4.3).
  A genuine refuter must make 𝓓_leaf < 0 while satisfying its exact priority
  package.

## The five branch targets (fix the arbitrary reduced display field FIRST, then measure the R1 cells)

1. **N:** η_D*{g_u < τ} ≥ 1/80.
2. **G<4:** N-mass < 1/80 and η_D*{g_u ≥ τ, A_u < 4} ≥ 1/80.
3. **C0:** first two masses < 1/80 and η_D*{g_u ≥ τ, A_u ≥ 4, ℓ_u < τ/2} ≥ 1/80.
4. **A-esc (DECISIVE):** first three masses < 1/80, and ≥ 1/80 on carriers with
   g_u ≥ τ, A_u ≥ 4, ℓ_u ≥ τ/2 and
   ∀f: ‖p_f − p_u + Ã_u(q̃_u − p_u)‖₁ > 3δ.
   The decisive refuter shape is a GROWING-RANK exact completion in which the
   synthetic displacement k_T − k_O stays > 3δ from every actual row
   displacement on constant D mass.
5. **T-esc (DECISIVE):** first four masses < 1/80, and strictly more than 1/80
   on carriers with an f satisfying the complementary residual inequality and
   Tail₁(u) > δ. The decisive refuter shape is a ROTATING-TAIL crown: actual
   residual-3δ actors exist but the scalar tails > δ rotate with the carrier,
   with no common receiver test producing (4.3).

Both decisive shapes must remain TALL; clone splitting, transient extensions,
or the short W63 plateau do not qualify.

## Mandatory unit tests (both must pass in search.py)

1. **W63 diagonal plateau** (reconstruct from
   `context/seeds/2026-07-11-w63-ihorn-six-shape-decider/` scripts/data): must
   route to D (M_I = 0, M_D = 1023/1024) and FAIL tallness. If your code
   classifies it as a refuter, your gate is wrong.
2. **W55 A0 = 5 completion** (same seeds): must reproduce its exact order-one
   finance-row negativity (ν_f ~ 5 vs τ²) rather than being mislabeled a
   refuter.

## Deliverables (all inside this directory)

1. `search.py` — self-contained exact-rational (fractions.Fraction)
   construction + verification; EVERY claim an exact assertion; exit nonzero on
   any mismatch. Deterministic (no float, no RNG without a fixed seed). Include
   per-leaf verdict lines, the mandatory print panel per candidate, the two
   unit-test lines, and one final summary line.
2. `certificates.json` — exact rational matrices (as strings) + all panel
   quantities for any hit or best near-miss per leaf.
3. `REPORT.md` — verdict per leaf: REALIZED (show the certificate) / BLOCKED
   (name the exact binding inequality per attempted family, with margins) /
   PARTIAL. State explicitly this is L3 evidence, never proof. Record where
   tallness binds if it does, and ANY by-catch entrant to any leaf's hypothesis
   class (no genuine I-base datum has EVER been constructed — one exact entrant
   to any cell is the single most valuable output). Record the g_u/τ, A_u, ℓ_u/τ
   distributions for your best D-routed families.

## Discipline

- `context/FINDINGS.md` dead routes are absolute; all quantities clone-invariant
  (full fibers, row points, ℓ¹); signed picture; no probabilistic readings.
- Do NOT modify anything under `argument/` or `definitions/` — they are a
  read-only snapshot.
- Timebox: prefer five honest BLOCKED-with-named-margins verdicts over one
  half-verified REALIZED. If time forces triage, prioritize A-esc, then T-esc
  (they are the decisive searches), then G<4, C0, N.
- Final answer: five verdict lines + two unit-test lines + one sentence.
