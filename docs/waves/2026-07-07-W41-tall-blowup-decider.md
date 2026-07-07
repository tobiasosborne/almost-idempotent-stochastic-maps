# Wave W41 — the fork decider: topness vs the alpha blow-up; radial thickness named (2026-07-07, session 11)

**Node:** the W40 fork on conj-near-cluster-absorption, bd `aism-2fi` (P0). **Design:**
mutually-blind pair — AN (prove tall-mode alpha control) ∥ AM (realize the blow-up in the tall
regime, exact certificates) — + SEPARATE fresh hostile verifier VAN over both. Prompts + raw
answers in the session-11 scratchpad (`W41/`); AM's exact verifier banked in the bundle.

## Verdicts (verbatim first lines)

- Worker AN: `PARTIAL (tall-mode alpha bound only under zero-face radial thickness; tall
  heavy-cluster hypotheses alone do not control that thickness)`
- Worker AM: `NOT-SUSTAINED (frontier: v-top `H/tau = sqrt(5/49)`, `S4 = 0`, `A_min = 0`,
  `delta = 49/2000`; alpha-preserved record has `H_global/tau = sqrt(101183481/985900000)`,
  `A_min = 100`, but `v` is not top; binding constraint: the thin alpha row becomes
  visible/taller, and forcing `v` top collapses `A_min` to 0)`
- Verifier VAN: `VALID-WITH-CORRECTIONS (AN-B formula passes with the `R=0` caveat; AN-C
  “exact equivalence” is overclaimed; AM certificates pass)`

## Results

1. **`lem-radial-alpha-bound` (codified, VAN-corrected).** A_min is priced by the zero face's
   radial reach in the residual direction — IN THE CONVEX HULL (not the cone; the free conic
   mass creates the hull normalization); R = 0 gives A_min = 0; thickness mu gives
   A_min <= (1 + tau/4)(2 + 4*delta)/mu. One-way (thickness => bound).
2. **`conj-tall-zero-face-radial-thickness` REGISTERED** — the named intermediate: tall heavy-
   cluster tops admit a datum with R = 0 or radial reach >= mu. Gives tall-mode alpha control
   via 1; honest scope kept loud: even bounded alpha leaves the dual-direction conversion open.
3. **The certified dichotomy (AM, four exact families, VAN-rerun):** the alpha blow-up and
   the hidden-TOP condition are mutually exclusive in every construction — topness collapses
   A_min to 0. Exact-certificate support for the radial-thickness conjecture exactly where
   the program needs it.
4. **VAN's no-control confirmations:** slab leakage, depth-Markov, and the pincer all miss
   r_Z — the conjecture needs a genuinely new mechanism (candidate: WHY topness fattens the
   zero face — the residual points downhill where near/cluster rows give hull thickness).

## Banking (orchestrator)

Registry: the lemma + the conjecture (VAN as reviewer). Bundle:
`runs/2026-07-07-w41-tall-blowup/` (AM's verifier, double-rerun PASS). Sketch v10 +
FINDINGS at the round close. Honest tiers: reviewed (L5) + L3 certificates; NOT L0.
