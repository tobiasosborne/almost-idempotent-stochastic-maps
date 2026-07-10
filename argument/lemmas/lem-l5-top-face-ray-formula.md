---
id: lem-l5-top-face-ray-formula
kind: lemma
contract: For every exact signed idempotent P with delta(P) > 0, nonempty visible set W with hull C_W, and hidden top vertex v of height H, and every point q of the row polytope K(P), Z_v(q) = min over Lambda >= 0 and c in C_W of ( ||p_v - q + Lambda*(p_v - c)||_1 - Lambda*H ), with c omitted when Lambda = 0, where Z_v(q) = sup_{y in Y_v} y.(p_v - q) and Y_v is the top dual face of lem-top-support-dual-face; the minimum is attained.
defs: def-signed-idempotent; def-visible-set; def-height
deps: lem-top-support-dual-face
status: proved
af: none
provenance: W62 wave (docs/waves/2026-07-10-W62-artifacts/): codex prover (gpt-5.6-sol, high) PROOFS-W62-L5-BATCH.md §R1; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W62-L5-BATCH.md line 'R1: VALID' (incl. the Lambda = 0 edge and attainment). Reviewer != author.
owner: B
---

**Role (W62 L5 batch, 2/4 — the constant-complexity dual certificate).** Finite LP
duality collapses the entire top dual face to ONE outward visible-ray certificate:
minimax failure at \(q\) is witnessed by a single pair \((\Lambda,c)\), not a large
family of extreme points of \(Y_v\). This is what makes the S/C/I horns
argue-from-failure with constant-complexity data.

**Mechanism (one line).** Dualize the finite LP defining
\(Z_v(q)=\sup\{y\cdot(p_v-q):\lVert y\rVert_\infty\le1,\ y\cdot(p_v-p_w)\ge H\ \forall w\in W\}\)
([[lem-top-support-dual-face]]); aggregate the visible multipliers
\(\lambda_w\ge0\) into \(\Lambda=\sum_w\lambda_w\) and the barycenter
\(c=\Lambda^{-1}\sum_w\lambda_wp_w\in C_W\); \(\ell^1\)-\(\ell^\infty\) duality
gives the norm term.

**Honest scope (verifier-mandated).** The minimizer is existential: no favorable
minimizer, tie rule, or canonical choice is supplied, and consumers must work with
an arbitrary attained certificate (the exists-exact-max-volume dead route is not
touched). At \(\Lambda=0\) there is no \(c\) and the value is
\(\lVert p_v-q\rVert_1\). Signed picture; clone-invariant (row-hull points and
visible-hull points only).

**Rigour tier.** L5 (fresh hostile batched codex verdict, W62). NOT af-validated.
af-elevation-shaped. Consumers: the S/C/I horns of the W62 assembly.
