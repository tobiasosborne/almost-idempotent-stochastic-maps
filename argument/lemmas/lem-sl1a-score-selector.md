---
id: lem-sl1a-score-selector
kind: lemma
contract: For every exact signed idempotent P with delta(P) > 0, nonempty visible set W, and hidden top vertex v of height H > 16sqrt(delta(P)), every probability measure lambda on row points whose support consists of points p_x satisfying ||p_x-p_v||_1 >= 4sqrt(delta(P)) and dist_1(p_x,conv{p_w:w in W}) > H-4sqrt(delta(P)), whose barycenter b satisfies ||b-p_v||_1 <= 11sqrt(delta(P))/5, and whose mean under every admissible exposer a at v is at most 4sqrt(delta(P))/13, every top support functional phi at v, and every admissible exposer h at v, some row point f in supp(lambda) satisfies 2(H-phi(p_f))/(2+4delta(P)) + h(p_f) <= 12sqrt(delta(P))/13.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-top-deficit-price
status: proved
af: none
provenance: W56 wave (docs/waves/2026-07-09-W56-artifacts/): extracted from the twice-hostile-verified routine material of DECOMPOSITION-v2 (verdict-round1.md, verdict-round2.md); per-shard fresh hostile codex verdict in verdict-extraction.md (4 VALID + 6 VALID-WITH-CORRECTIONS, corrections applied and re-listed in the wave doc); reviewer != author throughout.
owner: B
---

# SL1a score selector

## Statement

Let \(P\) be an exact signed idempotent with \(\delta:=\delta(P)>0\), put \(\tau:=\sqrt\delta\), \(\rho:=4\tau\), \(\kappa:=\tau/4\), and \(D:=2+4\delta\), and suppose that its visible set \(W\) is nonempty and that \(v\) is a hidden top vertex of height \(H>16\tau\).  Write
\[
 d_x:=\operatorname{dist}_1(p_x,\operatorname{conv}\{p_w:w\in W\}).
\]
Suppose \(\lambda\) is a probability measure on row points such that
\[
 \operatorname{supp}\lambda\subseteq
 \{x:\|p_x-p_v\|_1\ge4\tau\ \text{and}\ d_x>H-4\tau\},
\]
its barycenter \(b\) satisfies \(\|b-p_v\|_1\le11\tau/5\), and
\[
 \int a(p_x)\,d\lambda(x)\le\frac{4\tau}{13}
\]
for every admissible exposer \(a\) at \(v\).  Then, for every top support functional \(\phi\) at \(v\) and every admissible exposer \(h\) at \(v\), there is an \(f\in\operatorname{supp}\lambda\) such that, with \(z:=H-\phi\),
\[
 \frac{2z(p_f)}D+h(p_f)\le\frac{12\tau}{13}.
\]

## Proof

We consume the proved registry contract `lem-top-deficit-price` verbatim:

> Top-deficit price: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set W(P), a hidden top vertex v of height H, there exists a top support functional phi (affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1), and for ANY such phi, writing a_j = P_vj and z_j = H - phi(p_j) >= 0: for every subset A of row indices, sum over j in A of max(a_j,0)*z_j <= nu_v*(2+4*delta) <= delta*(2+4*delta); consequently for m >= 0, L >= 0, if sum over A of max(a_j,0) >= m and z_j >= L on A then m*L <= delta*(2+4*delta), and for delta <= 1/4, lambda > 0, theta < 1, positive v-row mass >= 1-theta on rows with z_j >= lambda*H forces H <= 3*delta/(lambda*(1-theta)), hence H <= 4*tau whenever delta <= min(1/4, (4*lambda*(1-theta)/3)^2).

Thus \(z(p_x)\ge0\) on every row point and \(z(p_v)=0\).  Since \(\phi\) is \(1\)-Lipschitz and the locked row geometry of `def-signed-idempotent` gives \(\|p_x-p_v\|_1\le2+4\delta=D\),
\[
 z(p_x)=\phi(p_v)-\phi(p_x)\le\|p_v-p_x\|_1\le D.
\]
Consequently \(z/D\) is an admissible exposer at \(v\).  Applying the assumed all-exposer bound first to \(z/D\) and then to \(h\) gives
\[
 \int\left(\frac{2z(p_x)}D+h(p_x)\right)d\lambda(x)
 \le 2\frac{4\tau}{13}+\frac{4\tau}{13}
 =\frac{12\tau}{13}.
\]
The row-point support is finite.  If every support point had score strictly larger than \(12\tau/13\), its probability average would also be strictly larger.  Hence at least one \(f\in\operatorname{supp}\lambda\) has the asserted score.

## Notes

The barycenter-radius clause is retained because the hypotheses are the complete SL1a counterexample data, but this selector does not use it and makes no antipode claim.  In particular, it does not make the false inference that two measures with the same barycenter have the same score-sublevel masses.  The conclusion selects a row point rather than an index, so clone splitting only divides the weight of the same candidate point.  The selected point remains in the strict co-top support set, so the Proposition-E shallow counterweight is not admitted by this lemma's assembled use.
