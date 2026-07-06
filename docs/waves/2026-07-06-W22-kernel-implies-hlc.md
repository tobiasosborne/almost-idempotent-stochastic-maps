# Wave W22 — trunk step <2>5: Kernel ⇒ HLC, re-derived in-repo + hostile verification (2026-07-06)

**Node:** trunk <2>5 (sketch v4; staleness-rule debt), bd `aism-pu0` (remaining scope: HLC shard +
finisher wiring; the equivalence half was settled by DC4). **Design:** fresh codex prover (worker F,
instructed to treat `docs/ingest/report/kernel-conjecture.tex:150-221` as an object of study and
re-derive everything) + SEPARATE fresh codex adversarial verifier (worker G, hostile brief, told the
ingest text was off-limits to preserve independence). Prompts + raw answers in the session scratchpad
(`W22/PROMPT-{F,G}.md`, `W22/ANSWER-{F,G}.md`). No numeric bundle (paper wave; the verifier's exact
fixture checks were scratch-only by design).

## Verdicts (verbatim first lines)

- Worker F (prover): `PROVED (C1 = max{B,3}, delta <= min{delta0, 1/4})`
- Worker G (verifier): `VALID (no error found; checks: specified definition shards, conj-kernel,
  af-validated lem-mass-split, obs-height-collapse comparison, exact /tmp W19 fixture test)`

## The result (codified as `lem-kernel-implies-hlc`, status: proved, af: none)

Assume conj-kernel with constants (δ₀, B). Then every exact signed idempotent P with
δ ≤ min{δ₀, 1/4} has **H(P) ≤ max{B,3}·√δ** (the HLC inequality δ ≥ H²/C₁²). Proof shape: height
attained at a row vertex (extreme points = merged-duplicate row vertices; dist₁(·,C_W) convex);
δ = 0 branch (h ≡ 0 exposer, H = 0); positive-height maximizer is hidden; σ̃-dichotomy — small
branch re-derives the s8 cap H(1−σ̃_v) ≤ ν_v(2+4δ) via lem-mass-split + the row-diameter clause,
giving H ≤ 6δ ≤ 3τ; large branch consumes the Kernel hypothesis verbatim (H ≤ Bτ).

## Verification highlights (worker G, all [T1])

Row-diameter clause confirmed LITERALLY in `def-signed-idempotent`; vertex-attainment facts already
stated in `def-height` (the prover's re-derivation matches the shard); δ=0 branch legal per
`conj-kernel`'s contract (no δ>0 hypothesis); split identity + norm chain verified algebraically;
constants and the strict/non-strict dichotomy boundary verified; no forbidden imports; 17 hidden-top
vertices from banked exact fixtures satisfy the intermediate inequality exactly.

## Banking (orchestrator)

- Registry: `lem-kernel-implies-hlc` (proved/af:none; deps conj-kernel + lem-mass-split);
  `op-hlc` registered (open; the trunk's middle rung now a first-class DAG node);
  `op-exposed-hull` rewired to dep on op-hlc (the faithful <2>6 consumption). Linker green.
- Trunk ledger effect: <2>5 moves from [priced: T1-short, NOT a shard] to [reviewed, codified];
  <2>6 and <2>7 remain mod-audit/open — they are now the ONLY unreviewed links between a proved
  Kernel and op-classical.
- Honest tiers: reviewed paper proof (L5); NOT af-validated, NOT L0-rigorous.
