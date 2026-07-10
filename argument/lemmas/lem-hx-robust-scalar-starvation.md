---
id: lem-hx-robust-scalar-starvation
kind: lemma
contract: For all reals K_R, L, K_C >= 0 there is a universal delta_R(K_R,L,K_C) in (0,2^(-16)] such that no finite exact signed idempotent P with 0 < delta(P) <= delta_R admits full row-point fibers represented by v and f, a real A >= 4 and a point q of the row polytope K(P) with sqrt(delta(P))/2 <= ||q - p_v||_1 <= 2*sqrt(delta(P)) and ||p_f - p_v + A*(q - p_v)||_1 <= K_R*delta(P), and an affine chi with chi(p_v) = 0, chi(q) = 1, and |chi(x) - chi(y)| <= ||x - y||_1/||q - p_v||_1 for all x,y in K(P), such that sum_{Q: |chi(p_Q)| > L} max(c_Q, 0) <= K_C*delta(P), where c_Q = sum_{j in Q} P_{vj}.
defs: def-signed-idempotent; def-negative-mass
deps: lem-hx-transverse-moment-identity
status: proved
af: validated
workspace: proofs/lem-hx-robust-scalar-starvation
provenance: W60 wave (docs/waves/2026-07-10-W60-artifacts/): codex prover (gpt-5.6-sol, high) PROOFS-W60-ENGINE.md §E4; fresh hostile codex verifier (gpt-5.6-sol, xhigh), batched verdict VERDICT-W60-ENGINE.md line 'E4: VALID' (incl. an independent small-exact-counterexample attack that failed exactly at the tail hypothesis, and the T0 fixture check). Reviewer != author. af-orchestrate 2026-07-10 (W61, aism-zo1): root validated, 12/12 nodes, taint clean; fresh codex verifier per node (prover != verifier); export.md/tex in proofs/.
owner: B
---

**Role (W60 engine bank, 4/5 — the T0 generalization proper).** The rank-free,
slab-free, tableau-window form of the starvation mechanism of
`lem-starvation-completion-obstruction`: fiberwise zero-top exterior support is
replaced by an \(O(\delta)\) positive top-tail cap, the exact metric pin
\(\lVert p_z-p_v\rVert_1=\tau\) by the window \([\tau/2,2\tau]\), the pinned
finance row by any \(K_R\delta\)-residual scaffold, and rank 3 by nothing.
**This retires §HONEST-LIMITS gaps 1 (rank) and 2 (slab) of PAPER-PROOF-w59.md at
the mechanism level and de-pins the tableau metric (gap 4's removable half).**

**Explicit ceiling (proved).** With \(B=K_C+1+(K_C+K_R+1)/4\) and \(H=2L+6B\):
\(\delta_R=\min\{2^{-16},(4H^2)^{-1}\}\).

**Mechanism (one line).** Unit moment ([[lem-hx-transverse-moment-identity]] at
\(D=q-p_v\)) vs supply: the tail sign-split pays \((K_C{+}1)\delta\) on the
negative union and \((K_C{+}K_R{+}1)\delta/A\) through the finance-row identity
\(p_f=p_v-AD+r\); core costs \(\le L\lVert D\rVert_1\); the window makes the total
\(O(\tau)<1\) below the ceiling.

**Fixtures (verifier-checked).** (i) The T0 display sits at calibration
\((K_R,L,K_C)=(3,1,0)\) with \(\delta_R(3,1,0)=2^{-16}\), consistent with and
slightly roomier than the W59 close. (ii) The verifier's independent rank-2 exact
near-example satisfies every hypothesis EXCEPT the tail cap
(\(\mathrm{Tail}_1\approx1\)) — confirming the top-tail cap is the indispensable
obstruction, not a hidden consequence of the scaffold.

**Scope.** Does NOT supply the actor pair \((A,q)\), the tail cap, or anything
about selected-corner data — producing those from an H-X datum is exactly the open
hard residual (route fork aism-ur9). Quantifier order: \((K_R,L,K_C)\) first, then
\(\delta_R\). Clone-invariant. Signed picture.

**Rigour tier.** af-validated (W61 orchestration 2026-07-10: root validated,
12/12 nodes, taint clean; prior L5 batched W60 verdict).
