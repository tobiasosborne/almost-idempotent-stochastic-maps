---
id: lem-prh
kind: lemma
contract: Positive-retract hardening (PRH): let k,n >= 1 and let A:l-infinity(k)->l-infinity(n) and M:l-infinity(n)->l-infinity(k) be positive unital maps (equivalently, have probability-vector rows); if ||MA-I_k||_{infinity->infinity} <= epsilon with 0 <= epsilon < 1/2, then there is a stochastic idempotent E:l-infinity(n)->l-infinity(n) with ||AM-E||_{infinity->infinity} <= 2*sqrt(2*epsilon).
defs: def-positive-approximate-retract; def-stochastic
deps:
status: proved-mod-audit
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md §§1-6; hostile batch verdict VERDICT-W74F-BATCH.md §A (VALID, no correction); report lem:prh
owner: A
workspace: proofs/lem-prh
---

**Status.** Hostile-verified paper proof, hence `proved-mod-audit`; not
`af`-validated and not L0-rigorous.

**Transcribed construction.** For
\(\lambda=\sqrt{\varepsilon/2}\), use the disjoint cores
\[
C_s=\{i:a_{is}>1-\lambda\}.
\]
The stochastic-row identity gives
\[
\sum_i\mu_s(i)(1-a_{is})\le\varepsilon/2,
\qquad
\beta_s:=\mu_s(C_s^c)\le\varepsilon/(2\lambda).
\]
Condition each row \(\mu_s\) on \(C_s\), obtaining the stochastic map
\(N\).  Replace every encoder row in \(C_s\) by \(e_s\), obtaining
\(\widehat A\).  Then
\[
N\widehat A=I_k,\qquad E=\widehat A N,\qquad E^2=E.
\]
The two changes cost
\[
\lVert AM-AN\rVert_{\infty\to\infty}\le\varepsilon/\lambda,
\qquad
\lVert AN-E\rVert_{\infty\to\infty}\le2\lambda.
\]
Optimizing gives \(2\sqrt{2\varepsilon}\).  At \(\varepsilon=0\), the
artifact takes \(E=AM\) directly.

**Framing.** This installs the reduction
`op-classical` \(\Leftarrow\) “a positive approximate retract exists”:
find stochastic \(A,M\) with
\(\lVert AM-Q\rVert_{\infty\to\infty}=O(\eta)\) and
\(\lVert MA-I\rVert_{\infty\to\infty}=O(\eta)\), then apply PRH.
