# W63 L3 decider — S/C pre-creative shapes (exact arithmetic)

You are a fresh, independent worker. Your workspace is this directory (registry
snapshot `argument/` + `definitions/` + `context/`). Everything you produce stays
inside it. This is an L3 (constructive/numerical evidence) job: **nothing you
produce is a proof**, and your report must say so.

## Target

`context/DECOMPOSITION-W62-L5.md` nodes **S**
(`conj-w62-shallow-exterior-payer-exclusion`) and **C**
(`conj-w62-scalarizable-cotop-web-exclusion`) — the other two horns of the proved
S/C/I trichotomy for L5-GAP-1. Read the artifact's §1 shared notation block IN FULL
(L5 datum, fibers, G_v, Sh_v, E_c, K_v^loc, omega, r_omega, scalar width Omega,
q_A, Y_v, Z_v) and both nodes' (a)-(e). The four routine nodes R0-R3 are PROVED
(registry shards `lem-l5-*`); in particular `lem-l5-universal-exterior-payer` (R3)
is a THEOREM: for every c in K(P), P_v^+(E_c) >= tau*S/8 below its ceiling. Your
candidates must live WITH that floor, not against it. Compute Z_v exactly via the
proved ray formula `lem-l5-top-face-ray-formula`.

## Your job: two exact decider shapes (DECOMPOSITION-W62-L5.md §4.2, items 2-3)

Every genuine candidate family MUST satisfy, in exact rational arithmetic
(fractions.Fraction): P_k^2 = P_k entrywise, all row sums 1,
delta_k = delta(P_k) -> 0, nonempty visible set W(P_k), a hidden top vertex v with
H_k > 16*tau_k (tau = sqrt(delta)). Tallness is where ALL THREE prior refuter
searches died (context/2026-07-10-W61-deciders-and-elevation.md,
context/seeds/w62-i-horn-REPORT.md) — attack it head-on; a short local gadget
without tallness is evidence only.

1. **Shallow-counterweight completion (attacks S).** Attach the W54 shallow
   counterweight (context/l5-answer.md — mass ~ 4*tau/(2+4*delta) at depth
   <= H - 8*tau) to the W61 dyadic leak-financer seed
   (context/seeds/w61-leak-financing-data/) in factorized coordinates P = L*B with
   B*L = I (exactness for free), forcing the payer's receiver fiber into
   E_c ∩ Sh_v for a local center c in K_v^loc with
   P_v^+(E_c ∩ Sh_v) >= (1/16)*tau*S, while the TRUE normalized value
   Z_v(q_A)/tau -> 0 on a genuine L5 datum (far-deep supported A, S >= 1/4).
   Sweep H/tau downward toward 16: report exactly where (which inequality, what
   margin) the completion fails, or exhibit the certificate if it does not.
2. **Two-prong engine-financing bouquet (attacks C).** Two opposing co-top actor
   groups (drift ||r_omega - p_v||_1 >= 1/8 OR width Omega(omega) >= 1/16 — C's
   antecedent) sharing ONE reusable exterior payer, with q_A pinned on the summit
   axis and Z_v(q_A)/tau -> 0. This attacks the same-carrier alignment step after
   R3: the C mechanism's chord demand (§C(b): the weighted chord
   s_+*s_-*||q_+ - q_-||_1 >= 1/32 forcing T_omega(F) >= M_omega/(64*D_0) - 2*M_omega*delta)
   must be payable by the shared payer WITHOUT the ray certificate noticing.
   Check the full C antecedent (shallow mass < (1/16)*tau*S for every local
   center; co-top floor >= (1/16)*tau*S) and BOTH drift/width branches separately.

By-catch: if either search produces a genuine L5 datum that instead enters node I's
strict low-drift/low-width class, record it fully — the I horn's creative wave is
running in parallel and any exact entrant to ANY horn's hypothesis class is the
single most valuable output (no genuine L5 datum has EVER been constructed).

## Deliverables (all inside this directory)

1. `search.py` — self-contained exact-rational construction + verification; every
   check an exact assertion (P^2 = P entrywise; delta; visible/hiddenness
   certificates; H with primal+dual certificates; fiber quotient; Z_v via the ray
   formula with an exact minimizing pair; the S/C antecedent inequalities per local
   center; r_omega, Omega(omega); drift/width branch flags). "Runs without errors"
   is not a pass; exit nonzero on any mismatch.
2. `certificates.json` — exact rational matrices + all quantities for any hit or
   best near-miss per shape.
3. `REPORT.md` — verdict per shape: REALIZED (kills/restates S or C — show the
   certificate) / BLOCKED (name the exact binding inequality per attempted family,
   with margins) / PARTIAL. State explicitly this is L3 evidence, never proof.
   Record shapes tried, parameter ranges, dead ends, WHERE tallness binds if it
   does, and the sweep trace for H/tau -> 16 in shape 1.

## Discipline

- `context/FINDINGS.md` dead routes are absolute; all quantities clone-invariant
  (full fibers, row points, l1); signed picture; no probabilistic readings.
- Timebox: prefer two honest BLOCKED-with-named-margins verdicts over one
  half-verified REALIZED. Final answer: two verdict lines + one sentence.
