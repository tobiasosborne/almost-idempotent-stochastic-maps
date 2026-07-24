---
id: lem-routef-k-ledger
kind: lemma
contract: Relative Route F factorization ledger: there are universal K >= 1 and eta_K > 0, independent of Hilbert-space dimension, amplification level, simple-block count, and block dimensions, such that for every 0 <= eta <= eta_K the repaired Kitaev factorization supplies UCP maps Delta, Upsilon with the three estimates bounded by K*eta, and the associated stochastic map admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta); the constants and threshold are the explicit relative finite expressions in the hostile-verified ledger.
defs: def-stochastic; def-extended-epsilon-cstar-algebra
deps: lem-thmainext-conditional; cor-kitaev-diagonal-cpization; lem-kitaev-almost-idemp-audit; lem-prh
status: proved-mod-audit
af: none
provenance: docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md (ledger) + PROOF-W74F-H-STAGE1.md (Stage-1 packet); hostile verdicts VERDICT-W74F-G-KLEDGER.md (INVALID as first written — Stage-1 packet missing) then VERDICT-W74F-H-STAGE1.md (VALID-WITH-CORRECTIONS — ledger CLOSED at proved-mod-audit; contract text endorsed verbatim by the verifier); report lem:routef-k-ledger
owner: A
workspace: proofs/lem-routef-k-ledger
---

**Status.** Hostile-verified paper ledger (fresh codex provers, separate
fresh hostile codex verifiers, two rounds — the first verdict rejected
the ledger for one missing packet; the second confirmed the repaired
ledger closed), hence `proved-mod-audit`; not `af`-validated and not
L0-rigorous.

**What is proved.** All constants are explicit RELATIVE finite
expressions in the named universal source/artifact constants (the source
prints no decimals; none were invented): the symbol table of
`LEDGER-W74F-G-K.md` §1 plus the Stage-1 packet
(\(C_{\rm split}, e_{\rm split}\)) of `PROOF-W74F-H-STAGE1.md`;
\(K=\max\{K_{\Delta\Upsilon},K_{\rm mult},K_{\Upsilon\Delta},1\}\); the
\(\eta_K\) minimum includes the guard \(e_{\rm split}/(C_{\rm pre}C_A)\).

**Verifier corrections (recorded).** (i) The old Stage-1 side
(\(v^{(1)}_{\rm comm}\)) is governed by COMP-CB against the ambient
defect \(\varepsilon_0\); the fresh \(\mathbb C^2\)-inclusion
(\(v^{(2)}_{\rm comm}\)) is governed by \(C_{\rm split}\) against the
split-corner defect \(\varepsilon_S\), with
\(\varepsilon_S\le C_{\rm co}(1+c_0^{\rm cb})\varepsilon_0\) inside
MAIN-CB — the two must not be conflated. (ii) The nonvanishing shrink
\(e_{\rm nv}\) is explicit in the packet's radius minimum.

**Honest rung.** The chain rests on [[lem-thmainext-conditional]] (with
[[conj-hcb]] and [[conj-extcb]] proved-mod-audit), the repaired diagonal
([[cor-kitaev-diagonal-cpization]]), the audited `th_almost_idemp`
interface ([[lem-kitaev-almost-idemp-audit]]), and [[lem-prh]].  NOTHING
in it is af-validated; the repaired chain is not a byte-verbatim theorem
import.  L0 closure (af/Lean) is the remaining open work for Route F.
