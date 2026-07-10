---
id: lem-hx-financing-floor
kind: lemma
contract: For every finite exact signed idempotent P, every ordered pair (a,b) of points of the row polytope K(P) with a != b, every affine chi with chi(a) - chi(b) = 1, all reals A, Lambda > 0, and every set N of full row-point fibers with |chi(p_Q)| <= A for every Q in N and |chi(p_Q)| <= Lambda for every Q not in N, the complement F of N satisfies a^+(F) + b^+(F) >= (1 - A*l_chi)/Lambda - nu(a) - nu(b), where l_chi = sum_Q |d_Q| and d_Q = sum_{j in Q}(a_j - b_j).
defs: def-signed-idempotent; def-negative-mass
deps: lem-hx-transverse-moment-identity; lem-hx-signed-variation-ledger
status: proved
af: none
provenance: W60 wave (docs/waves/2026-07-10-W60-artifacts/): codex prover (gpt-5.6-sol, high) PROOFS-W60-ENGINE.md §E3; fresh hostile codex verifier (gpt-5.6-sol, xhigh), batched verdict VERDICT-W60-ENGINE.md line 'E3: VALID-WITH-CORRECTIONS' (contract wording: the endpoint-pin normalization replaced by the difference-one condition chi(a)-chi(b)=1 actually used; correction applied in-file and here). Reviewer != author.
owner: B
---

**Role (W60 engine bank, 3/5 — THE ENGINE).** The quantitative demand side of the
H-X front: two separated (synthetic) rows must jointly finance positive coefficient
mass on every high-lever fiber set. Assembles [[lem-hx-transverse-moment-identity]]
(unit moment) with [[lem-hx-signed-variation-ledger]] (budget converter) by
splitting the moment over \(N\cup F\).

**Statement.** With hypotheses as in the contract,
\[ a^+(F)+b^+(F)\ \ge\ \frac{1-A\,\ell_\chi}{\Lambda}-\nu(a)-\nu(b),
   \qquad \ell_\chi:=\sum_Q|d_Q|\le\lVert a-b\rVert_1. \]

**Recentred instantiation (Corollary E3.3 in the source, body-level).** For rows
\(r,s\) at distance \(\ell>0\) and any center \(c\in K(P)\), the recentred sign
functional \(\psi_c(x)=\ell^{-1}\sum_j\operatorname{sgn}(D_j)(x_j-c_j)\) has
\(\psi_c(p_r)-\psi_c(p_s)=1\) and \(|\psi_c(p_Q)|\le\lVert p_Q-c\rVert_1/\ell\);
metric balls are automatically low-lever, and the global lever is
\(\Lambda=(2+4\delta)/\ell\) via the signed row-diameter bound
\(\lVert p_i\rVert_1=1+2\nu(p_i)\le1+2\delta\). Reading: **two rows at separation
\(\ell\) must jointly ship \(\gtrsim(1-A\ell_\chi)\,\ell/(2+4\delta)\) positive
mass outside every low-lever region** — the slab-free, rank-free replacement for
the W59 lever geometry.

**Scope.** Vacuous when \(A\ell_\chi\ge1\) or \(\Lambda\) is large relative to
\((1-A\ell_\chi)/(2\delta)\) — a usage window, not a defect. The consumer chooses
\((a,b,\chi,N,A,\Lambda)\) explicitly (no selectors, no tie-breaking).
Clone-invariant. Signed picture.

**Rigour tier.** L5 (fresh hostile codex, batched W60 verdict; wording correction
applied as prescribed). NOT af-validated. af-elevation candidate. Consumer:
[[lem-hx-forced-exterior-coupling]]; the W60 route fork's hard nodes consume this
engine (USER DECISION aism-ur9).
