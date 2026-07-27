# AUDIT v2 — fresh hostile re-audit of the LEDGER-DOMAINS design

Date: 2026-07-27
Role: fresh independent hostile auditor
Status: **NON-RIGOROUS AUDIT / DESIGN ONLY / DO NOT SHARD, SEED, REWIRE, OR PROMOTE**

## 0. Disposition

**LAND-14, WITH TWO EXACT CORRECTIONS.**

The load-bearing repairs in `DESIGN-LEDGER-DOMAINS-v2.md` survive hostile
recomputation:

1. the corrected \(\Upsilon'\) radius contains the first audit's exact
   \((2C_R)^{-1}\) term, in the correct place, and it proves every selected
   Choi multiplicity space nonzero;
2. all five dependency additions demanded by the first audit are present
   verbatim and introduce no cycle;
3. the first audit was right that the original terminal GAP was overstated:
   the literal landed `lem-thmainext-conditional` contract is a black-box
   producer of \(C_E,\varepsilon_E\), not a theorem conditional on a reset
   package supplied by the Route-F ledger; and
4. the ten-entry expanded terminal minimum is finite, positive,
   noncircular, and dimension-free.

One new contract-level radius defect was found:

- **Row 3 lacks the displayed domain of one of its new direct
  dependencies.** The landed `lem-kitaev-almost-idemp-audit` contract assumes
  \(\eta<1/4\)
  (`argument/lemmas/lem-kitaev-almost-idemp-audit.md:4`), while v2 states
  \[
  \rho_{\rm id}=\min\{\rho_{\rm AI},\varepsilon_E/C_A\}
  \]
  without exposing either input as \(<1/4\)
  (`DESIGN-LEDGER-DOMAINS-v2.md:92,184,253-259`). The exact repair is
  \[
  \boxed{\rho_{\rm id}^{\rm corr}
  :=\min\{\rho_\theta,\rho_{\rm AI},\varepsilon_E/C_A\}.}
  \]
  Since \(\rho_\theta=1/8<1/4\), this closes the direct Kitaev invocation.
  No downstream effective radius changes: \(\rho_T\le
  \rho_{\rm id}^{\rm corr}\), and every downstream minimum that consumes
  row 3 already also contains \(\rho_T\).

There is also one exact wording correction:

- v2 says the MAIN contract supplies a “unital extended isomorphism”
  (`DESIGN-LEDGER-DOMAINS-v2.md:242-248`). An extended
  \(\delta\)-isomorphism only **approximately** preserves the unit
  (`definitions/def-extended-delta-inclusion.md:13-17`;
  `refs/kitaev-2405.02434/approximate_algebras.tex:443-455`). Replace
  “unital extended isomorphism” by “extended isomorphism, with unit defect
  at most \(C_V\eta\).” The displayed row-2 arithmetic already uses the
  correct approximate statement, so no coefficient or radius changes.

These are local corrections, not reasons to hold back a row. Nothing in this
audit is rigorous or authorizes landing.

## 1. Binding-audit and scope checks

Locus abbreviations below are:

- **v2** =
  `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md`;
- **first audit** =
  `docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS.md`;
- **v4.1** =
  `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`;
- **G-verdict** =
  `docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-G-KLEDGER.md`;
- **TeX** = `refs/kitaev-2405.02434/approximate_algebras.tex`.

### 1.1 Every prescribed first-audit repair

| first-audit demand | v2 check | verdict |
|---|---|---|
| Add \((2C_R)^{-1}\), \(C_R=C_V+C_\Delta+C_2\), to \(\rho_{\Upsilon'}\) (first audit:133-148,201-230). | v2 defines \(C_R\) exactly so at lines 110-127 and uses it in table row 8 at line 191. | **APPLIED VERBATIM** |
| Add `lem-routef-ai-defect-linearization` to row 2 (first audit:186-187). | v2:183. | **APPLIED VERBATIM** |
| Add `lem-kitaev-almost-idemp-audit` to row 3 (first audit:188). | v2:184. | **APPLIED VERBATIM**, but its \(<1/4\) domain now requires the new correction above. |
| Add `lem-routef-ai-defect-linearization` to row 4 (first audit:189). | v2:185. | **APPLIED VERBATIM** |
| Add `lem-thmainext-conditional` to row 5 (first audit:190). | v2:186. | **APPLIED VERBATIM** |
| Add `lem-routef-functional-calculus-closeness` to D2 (first audit:234-249). | v2:188,527-534. | **APPLIED VERBATIM** |
| Replace the alleged terminal GAP by \(\min\{\rho_{\rm fac},(24K)^{-1},1\}\) using the landed MAIN interface (first audit:273-317). | v2:168-170,197,405-423,457-500. | **APPLIED VERBATIM** |

The remaining first-audit findings are also dispositioned accurately at v2
lines 572-589: the absent reset shard and omitted
\(\varepsilon_{\max}^{\rm cb}\) guard remain MAIN-front findings, the
serial order is rechecked, and dimension-freeness is rechecked. The v1
finite Route-F scope \(\mathcal H=\mathbb C^n\) is unchanged
(`DESIGN-LEDGER-DOMAINS.md:67-71`;
`DESIGN-LEDGER-DOMAINS-v2.md:45-48`). No row was silently narrowed in the
v1-to-v2 repair.

### 1.2 Corrected dependency graph

After deleting external leaves, v2's internal edges at lines 429-446 have
the displayed topological order
\[
1,2,3,4,5,6,\mathrm{D2},7,\mathrm{D3},8,9,10,11,12,13,14.
\]
Each of the five new imports is an external landed leaf. The new
\(\rho_\theta\) entry in \(\rho_{\rm id}^{\rm corr}\) is likewise supplied
by the already-landed functional-calculus leaf. Hence neither the prescribed
dependency repairs nor the new row-3 repair creates a forward edge, dangling
edge, or cycle.

## 2. Black-box `th_main_ext` attack

### 2.1 Literal condition set

The public contract says:

> there are universal \(C_E<\infty\) and \(\varepsilon_E>0\) such that
> every finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra
> \(\mathcal A\), for \(0\le\varepsilon\le\varepsilon_E\), is carried by an
> extended \(C_E\varepsilon\)-isomorphism from a finite-dimensional
> \(C^*\)-algebra

(`argument/lemmas/lem-thmainext-conditional.md:4-9`; the hostile-endorsed
restatement is also at
`docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-H-STAGE1.md:309-320`).

Its complete consumer-facing condition set is:

| condition | producer |
|---|---|
| \(\mathcal A\) is finite-dimensional | v2 restricts to \(\mathcal H=\mathbb C^n\), so \(\mathcal A=\operatorname{Im}\widetilde\Phi\subseteq M_n\) is finite-dimensional (v2:45-48; AI contract at `argument/lemmas/lem-routef-ai-defect-linearization.md:4-9`). |
| \(\mathcal A\) is an extended \(\varepsilon_{\rm AI}(\eta)\)-\(C^*\)-algebra | `lem-routef-ai-defect-linearization` (`argument/lemmas/lem-routef-ai-defect-linearization.md:4-9`). |
| \(0\le\varepsilon_{\rm AI}(\eta)\le\varepsilon_E\) | \(\varepsilon_{\rm AI}(\eta)\le C_A\eta\), and \(\rho_T\le\varepsilon_E/C_A\) (v2:77-86,226-240). |
| H-CB and EXT-CB proof dependencies | `conj-hcb` and `conj-extcb` are landed, with the exact deps shown in `lem-thmainext-conditional.md:5-9`; their landed contracts/statuses are at `argument/lemmas/conj-hcb.md:4-9` and `argument/lemmas/conj-extcb.md:4-9`. |

There is **no** hypothesis in the landed contract requiring the consumer to
supply `lem-maincb-reset-constant-ledger`, a Stage-1 state, a G-S1 producer,
or a reset radius. The phrase “the assembly uses ... Stage-1 reset packets”
is part of the asserted proof provenance, not an antecedent. The historical
word “conditional” remains in the stable id, but the shard explicitly records
that its former H-CB/EXT-CB premises were discharged and the contract was
restated (`lem-thmainext-conditional.md:17-24`).

Thus the missing reset shard and the narrowed IMPROVE-CB guard
(`lem-maincb-error-improvement.md:4,13-19,34-37`) are genuine obstacles to a
future unpacked MAIN decomposition. They are not hypotheses of this landed
black-box interface. At the present non-rigorous design rung, the first
audit's abstraction-boundary conclusion survives.

### 2.2 No terminal circularity

\(C_E,\varepsilon_E\) are chosen before row 1
(v2:66-86). All factor constants are then produced serially; the
three telescope coefficients produce \(K\) in row 13
(v2:383-403). Only after row 13 is
\[
\eta_K=\min\{\rho_{\rm fac},(24K)^{-1},1\}
\]
formed in row 14 (v2:405-423). Neither \(C_E\), any earlier radius,
nor \(K\) depends on \(\eta_K\). The occurrence of \(K\) in its own
subsequent threshold is therefore not circular.

**Terminal threshold / black-box verdict: VALID.** The original v1 terminal
GAP claim was indeed overstated. The result remains only relative to the
landed `proved-mod-audit` MAIN interface, exactly as v2 warns at lines
199-220.

## 3. Independent row-by-row recomputation

| row | id | verdict | hostile check |
|---:|---|---|---|
| 1 | `lem-routef-raw-factor-norms` | **VALID** | \(\rho_T\) includes the AI, MAIN, functional-calculus, and two Neumann guards. With \(a=C_\theta\eta,b=C_V\eta\le1/4\), \((1+a)/(1-b)\le1+a+3b\), giving \(C_T=C_\theta+3C_V\) (v2:77-86,226-240; TeX:2749-2753). |
| 2 | `lem-routef-raw-factor-units` | **VALID-WITH-CORRECTIONS** | The dependency correction is present and \(\rho_{\rm unit}=\rho_T\) is sufficient. Replace only the false word “unital” at v2:243 as specified in §0; the actual estimate \(C_V\eta/(1-C_V\eta)\le3C_V\eta\) is valid (v2:242-251; TeX:2754-2757). |
| 3 | `lem-routef-raw-factor-identities` | **VALID-WITH-CORRECTIONS** | The new direct Kitaev import is present, but its contract requires \(\eta<1/4\). Replace \(\rho_{\rm id}\) by \(\rho_{\rm id}^{\rm corr}=\min\{\rho_\theta,\rho_{\rm AI},\varepsilon_E/C_A\}\). Then exact idempotence and surjectivity give both identities (v2:253-259; `argument/lemmas/lem-kitaev-almost-idemp-audit.md:4-9`; TeX:2749-2753). |
| 4 | `lem-routef-raw-product-estimate` | **VALID** | On \(\rho_T\), the extended-isomorphism product defect is at most \(C_EC_A\eta\le C_V\eta\le C_T\eta\); the direct AI import supplies the Choi-Effros product (v2:261-269; TeX:2754-2766). |
| 5 | `lem-routef-delta-prime-closeness` | **VALID** | Row 4 costs \(C_T\eta\); replacing \(\widetilde\Phi\) by \(\Phi\) on two raw factors of norm at most \(2\) costs \(4C_\theta\eta\). The direct MAIN import supplies exact involution preservation required by CP-ization (v2:273-282; `argument/lemmas/cor-kitaev-diagonal-cpization.md:4-9`; TeX:2771-2801). |
| 6 | `lem-routef-delta-normalization-closeness` | **VALID** | The exact guard is \([2(C_T+C_{\Delta'})]^{-1}\), not a weaker \(C_{\Delta'}\)-only guard. It gives unit defect at most \(1/2\) and \(C_\Delta=6C_T+7C_{\Delta'}\) (v2:284-294; G-verdict:141-145,287-290). |
| 7 | `lem-routef-delta-phi-product` | **VALID** | The three insertions cost \(C_\theta,C_2,C_\Delta\), and \(\rho_{\Delta\Phi}\) intersects their producer domains (v2:304-314). |
| 8 | `lem-routef-upsilon-prime-closeness` | **VALID** | The componentwise guard and coefficient chain recompute exactly; see §4 below (v2:323-367; TeX:2831-2895). |
| 9 | `lem-routef-upsilon-normalization-closeness` | **VALID** | The guard \([2(C_T+C_{\Upsilon'})]^{-1}\) controls the full unit defect and gives \(C_\Upsilon=6C_T+7C_{\Upsilon'}\) (v2:369-381; G-verdict:144-149,291-295). |
| 10 | `lem-routef-delta-upsilon-telescope` | **VALID** | Exact row-3 identities and raw cb norm \(2\) give \(C_\theta+C_\Delta+2C_\Upsilon\) on the displayed intersection (v2:383-403; G-verdict:96-117). |
| 11 | `lem-routef-multiplicative-telescope` | **VALID** | The first comparison costs \(C_\Upsilon\); applying \(\widetilde\Upsilon\) to row 7 costs \(2(C_2+C_\theta+C_\Delta)\). The displayed domain contains every producer (v2:383-403; G-verdict:96-117). |
| 12 | `lem-routef-upsilon-delta-telescope` | **VALID** | Exact \(\widetilde\Upsilon\widetilde\Delta=I\) gives \(C_\Upsilon+2C_\Delta\) on the displayed domain (v2:383-403; G-verdict:96-117). |
| 13 | `lem-routef-k-finiteness` | **VALID** | The maximum is over four earlier finite universal coefficients. Its multiplicative coefficient dominates \(C_2\), and \(\rho_{\rm fac}\) is the minimum of four earlier positive domains (v2:149-164,393-403; G-verdict:96-117). |
| 14 | `lem-routef-threshold-minimum` | **VALID** | Row 13 supplies the common factorization packet; \((24K)^{-1}\) triggers F2 and gives \(3K\eta\le1/8\), \(3K\eta/(1-3K\eta)\le4K\eta\le1/6<1/2\); the entry \(1\) supplies the remaining PRH guard (v2:405-423; `argument/lemmas/lem-routef-f2-positive-unital-compression.md:4-9`; `argument/lemmas/lem-routef-f3-retract-defect.md:4-9`; `argument/lemmas/lem-routef-prh-finish.md:4-9`). |

No row uses \(\eta_A\) to certify an unrelated source estimate. It appears
only inside radii that invoke the AI row. The new row-3 correction is instead
the explicit domain of the newly added Kitaev dependency.

## 4. Corrected \(\Upsilon'\) radius

Rows 1 and 6 give
\[
\|\Delta_nX\|\ge(1-C_N\eta)\|X\|,\qquad C_N=C_V+C_\Delta.
\]
For the \(j\)-th Choi block, the D2 comparison at TeX:2840-2857 then gives
\[
R_j=I_{\mathcal L_j}\otimes C_j,\qquad
0\le C_j\le I,\qquad
\|C_j\|\ge1-(C_N+C_2)\eta=1-C_R\eta.
\]
These are exactly v2:325-337. The added **radius** guard
\(\eta\le(2C_R)^{-1}\), not a defect coefficient, gives
\(\|C_j\|\ge1/2\). Therefore \(C_j\ne0\), which is impossible on the zero
multiplicity space; hence \(\mathcal E_j\ne\{0\}\). Finite-dimensional norm
attainment supplies a unit \(\xi_j\) with
\(\|C_j\xi_j\|=\|C_j\|\), and
\[
1-\langle\xi_j,C_j^*C_j\xi_j\rangle
=1-\|C_j\|^2
\le1-(1-C_R\eta)^2
\le2C_R\eta.
\]
Thus
\[
C_L=C_2+C_3+2C_R,\qquad
C_{\Upsilon'}=1+C_\theta+2C_\Delta+2C_L
\]
recompute exactly (v2:339-364; TeX:2859-2895).

The smaller radius breaks no consumer. It propagates through
\[
\rho_{\Upsilon'}\to\rho_\Upsilon\to
\{\rho_{\Delta\Upsilon},\rho_{\rm mult},\rho_{\Upsilon\Delta}\}
\to\rho_{\rm fac}
\]
exactly as v2:393-403 records. Every later requirement is an upper-smallness
guard, so shrinking the domain can only help.

Probability averages have coefficient sum \(1\), and the direct-sum target
uses the maximum norm. Choosing one maximizing vector in each nonzero
finite-dimensional \(\mathcal E_j\) contributes no coefficient. Therefore
neither \(C_R\) nor any subsequent constant depends on \(n\), amplification,
block count, block size, or Choi multiplicity.

**\(\Upsilon'\) correction verdict: VALID.**

## 5. Fully expanded finite minimum

After the row-3 repair, \(\rho_T\le\rho_{\rm id}^{\rm corr}\). Recursive
expansion of \(\rho_{\rm fac}\) therefore still yields exactly the primitive
guard family
\[
\left\{
\rho_\theta,\rho_{\rm AI},\frac{\varepsilon_E}{C_A},
\frac1{4(1+C_\theta)},\frac1{4(1+C_V)},
\frac1{2(C_T+C_{\Delta'})},
\frac1{2C_R},
\frac1{2(C_T+C_{\Upsilon'})}
\right\}.
\]
The explicit \(\rho_\theta\) added to row 3 is already the first member, so
the expansion at v2:459-479 neither gains nor loses an entry. Adding
\((24K)^{-1}\) and \(1\) produces a finite ten-expression indexed family.

Every symbol is produced before use: functional calculus produces
\(\rho_\theta,C_\theta\); AI produces \(\rho_{\rm AI},C_A\); the landed
black box produces \(C_E,\varepsilon_E\); rows 1-9 produce the remaining
normalization and Choi coefficients; the telescope rows produce the three
factor coefficients; and row 13 produces finite universal \(K\) and positive
\(\rho_{\rm fac}\). No expression contains \(n\), an amplification index,
block data, a MAIN stage index, or the future \(\eta_K\).

**Finite-minimum verdict: VALID.**

## 6. Degree reconnection, dimension-freeness, and wiring

The D2 dependency list at v2:527-534 contains the first audit's exact added
functional-calculus leaf and the four earlier local rows. It supports
\[
C_2=C_{\Delta'}+4C_\Delta
\]
on \(\rho_2\), matching the checked mechanism
(`VERDICT-W74F-G-KLEDGER.md:119-128,287-290`; TeX:2803-2812).

The D3 list at v2:537-545 contains the Kitaev associativity leaf,
functional-calculus leaf, rows 1/5/6, and D2. It supports
\[
C_3=10+20C_\Delta+12C_\theta+2C_{\Delta'}
\]
on \(\rho_3\), with \(\rho_\theta=1/8<1/4\)
(`VERDICT-W74F-G-KLEDGER.md:119-128`; TeX:2813-2829). Both rows point only
backward. This is the concrete reviewed replacement contemplated by the
unresolved degree rows at
`DESIGN-FUDW-DECOMP-v4.1.md:230-245`.

All other coefficients are fixed sums, products, maxima, or minima of
universal inputs; normalization occurs on a fixed \(1/2\)-ball; the three
telescopes have fixed length. The componentwise selection was checked
separately in §4. **No route-level dimension-freeness alarm was found.**

The proposed parent dependencies at v2:556-567 contain exactly the three
telescopes, \(K\)-finiteness, the threshold, F2, F3, and PRH required by
`DESIGN-FUDW-DECOMP-v4.1.md:348-364`. V2 states both the prerequisite
“after and only after” at lines 552-554 and the explicit
**DO NOT REWIRE OR SEED** guard at lines 569-570. No instruction authorizes
premature mutation.

**Degree reconnection verdict: VALID.**

**Dimension-freeness verdict: VALID.**

**Wiring proposal verdict: VALID / PROPOSED-ONLY.**

## 7. Exact corrections and final disposition

Before any ratification or landing:

1. At v2 equations (1.2), table row 3, and §3.1
   (`DESIGN-LEDGER-DOMAINS-v2.md:92,184,253-259`), replace
   \[
   \rho_{\rm id}:=\min\{\rho_{\rm AI},\varepsilon_E/C_A\}
   \]
   by
   \[
   \rho_{\rm id}^{\rm corr}
   :=\min\{\rho_\theta,\rho_{\rm AI},\varepsilon_E/C_A\}.
   \]
   No other radius formula or primitive-minimum entry changes.
2. At v2:242-248, replace “the MAIN contract supplies the unital extended
   isomorphism” by “the MAIN contract supplies the extended isomorphism,
   whose unit defect is at most \(C_V\eta\).” No arithmetic changes.

With precisely those corrections:

- all fourteen reserved rows: **LAND-14** at the design level;
- D2 and D3: **VALID**, still design-only;
- corrected \(\Upsilon'\) radius: **VALID**;
- terminal black-box consumption: **VALID**;
- finite minimum and dimension-freeness: **VALID**;
- parent wiring: **VALID AS PROPOSED-ONLY / DO NOT REWIRE OR SEED**.

This is a non-rigorous audit verdict. It authorizes no status promotion,
registry mutation, seeding, rewiring, or claim that Route F or
`op-classical` is rigorous.
