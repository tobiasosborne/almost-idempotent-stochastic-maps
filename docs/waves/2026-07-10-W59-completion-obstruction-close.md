<!--
ROLE: W59 wave-close record — the paper-proof + af-elevation of the K-free starvation
  completion obstruction. Terminal artifact of the W55-W59 arc (threat named -> exact
  kills -> paper proof -> af oracle). Registry 150 -> 151; T0 count 28 -> 29.
STATUS DISCIPLINE (L0): the paper proof is L5 (fresh-hostile-verified) UNTIL the
  af-elevation record below, after which the shard is af: validated, T0. Promotes
  nothing beyond `lem-starvation-completion-obstruction` itself.
-->

# Wave W59 CLOSE — the completion obstruction PROVED (L5) then af-VALIDATED (T0)

**Target:** the candidate "minimal actor-hull starvation completion obstruction" named
by W57/W58 (`runs/2026-07-10-w57-starvation-completion-lp`,
`runs/2026-07-10-w58-starvation-completion-extra-vertex`) — a dimension-free paper proof
was the open item (bd `aism-cq2`). **Method:** codex ultra prover (paper proof from
first principles, guided by but independent of the W57/W58 exact Farkas certificates) ->
fresh hostile codex verifier (serial, reviewer != author) -> banking -> `af`
orchestration (prover/verifier roles per §6, Claude orchestrator-only) -> `fr verify`.
All artifacts in `runs/2026-07-10-w58-starvation-completion-extra-vertex/`
(`PAPER-PROOF-w59.md`, `VERDICT-W59.md`, `VERDICT-W59-final-message.md`,
`CERTIFICATE.md`, `FORMULATION.md`, `RESULTS.md`).

## Verdict first-line (verbatim)

`VERDICT-W59-final-message.md`: `VERDICT: VALID-WITH-CORRECTIONS — the K-free
obstruction is proved; only an index-level coordinate abbreviation is missing.`

(`VERDICT-W59.md`'s own closing verdict line concurs: `VERDICT: VALID-WITH-CORRECTIONS
— the obstruction and K-free strengthening are proved, with only one missing
notational abbreviation in Claim 2.` The two files are the routed final message and the
full independent-derivation ledger of the same hostile pass.)

## The result (banked; registry 150 -> 151)

`lem-starvation-completion-obstruction` (status: proved, L5 at banking time): for every
finite index set `I`, every real `A0 in [4,6]`, every `tau in (0, 1/256]`, the W55
starvation gadget (rank-three exact signed idempotent, row negative mass `<= tau^2`)
admits NO completion with any finite number of exterior zero-top support fibers
confined to the canonical slab `0 <= y <= 1` — the K-FREE strengthening of the
W57/W58 finite-case certificate family. **Mechanism (one line):** exact idempotence at
the pinned display demands one unit of transverse moment (`sum_j x_j*D_j = 1`), while
the actor hull and the aggregated exterior sign-union row budgets can supply only
`O(tau)` — contradiction strictly below the universal ceiling `tau <= 1/256` (worst-case
margin `979/1024` at `A=6, tau=1/256`, per the hostile verifier's independent endpoint
recomputation).

The single correction applied (verifier Finding 1, MINOR): before equation (5), define
`x_j := x_[j]` and `y_j := y_[j]` (an index-level coordinate abbreviation; not a
mathematical gap). The verifier also flagged Finding 2 (NOTE, not a defect): several
tableau pins (`c_v = 1-tau`, `c_w = tau+t`, `c_f = -t`) are unused — the proof holds
under strictly weaker hypotheses than the registered contract states, i.e. a stronger
result than claimed. Hypothesis audit, K-free/clone audit, W57/W58 inclusion check, and
honest-limits audit all independently passed (`VERDICT-W59.md`, full ledger).

This is the FIRST PROVED MECHANISM on the H-X / large-gauge completion front — the W55
starvation-gadget threat (which survived every scalar ledger) is excluded at rank three
with slab-confined exteriors by paper proof, not just by exact-rational certificates.

**Honest gap to generalize** (unchanged residual toward `conj-sl1a-off-diagonal-cell`
and the L6.5 large-gauge wall): (i) without the slab confinement `0 <= y_Q <= 1` (or
derive it from the H-X hypotheses); (ii) at general rank `>= 3`; (iii) at the H-X cell's
actual tableau (majority-horn off-diagonal freight `> 1/8`) rather than the gadget
constants. Per the hostile verifier's honest-limits audit: at rank `> 3` the coefficient
identity `sum_Q x_Q*d_Q = 1` still holds after extending `p_v, D, E` to a basis, but the
two-coordinate lever estimate gains uncontrolled transverse terms and the financing
close does not follow as-is — the precise place a rank-generalization must repair.

## af-elevation (T0 count 28 -> 29)

`af` orchestration on `lem-starvation-completion-obstruction` (Claude orchestrator-only,
per §6; fresh codex prover/verifier per node, roles never mixed): attempt 1 was a quota
no-op (usage limit; bridged by the delayed dispatcher). Attempt 2 VALIDATED the root in
3 rounds — **7 nodes, all validated, taint clean**. `af export` written
(`proofs/lem-starvation-completion-obstruction/export.md`); shard flipped
`status: proved` / `af: validated` (mechanical ledger reflection, not a judgment call);
`fr verify` PASS against the af oracle (▣). The W55-W59 arc — threat named -> exact
kills (W57/W58, L3) -> paper proof (W59, L5) -> af oracle (T0) — terminates here. This
is the first T0 result of the H-X / large-gauge front.

## Process notes

- Reviewer != author throughout: the W59 paper proof's hostile verifier was a fresh
  codex instance with no authoring role; every `af` node's verifier was a separate fresh
  codex per §6 rule 2.
- The candidate lemma from W58 was K-parametric (ceiling degrading with `K`); the W59
  paper proof is STRONGER — it removes the `K`-dependence entirely, proving the finite
  case uniformly rather than case-by-case.
- Sketch v23 (W59 obstruction-lemma delta) and v24 (af-elevation delta) both record this
  wave; see `docs/plans/CHANGELOG.md` for the retrofit summaries.

## Next (see sketch v24 Tier-1 order, unchanged by this close)

The generalization wave: formulate the moment-vs-budget ledger at the H-X tableau and
decide which of (i)-(iii) above is the binding gap (strategy pass first, then prover) —
now anchored to a T0 lemma rather than an L5 one. E1-E5 codification, the small-gauge
bridge, H-D/H-I, SL1b, and the L5 minimax remain unchanged and independent.
