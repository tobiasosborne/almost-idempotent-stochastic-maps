# DESIGN — LEDGER-SETTING-RESCOPE

Date: 2026-08-05
Role: fresh codex designer (W136)
Status: **DESIGN ONLY / NON-RIGOROUS / NOT USER-RATIFIED / DO NOT LAND,
SHARD, AMEND, REWIRE, SEED, OR PROMOTE**

## 0. Disposition

**DESIGN-CLOSABLE, SUBJECT TO A SEPARATE FRESH HOSTILE AUDIT AND USER
RATIFICATION.**

The verifier finding is systematic and real.  The sixteen landed contract
suffixes are mathematically usable only after their shared finite-dimensional
UCP/cb setting, witness choices, raw maps, and scalar ledger are bound at the
contract level.  The row-stochastic definition `def-almost-idempotent` cannot
provide that setting and should be removed from all sixteen `defs:` lines.

This design proposes one canonical witness-package definition,
`def-routef-raw-factor-setting`, and adds only ambient/serial-output binders in
front of the sixteen landed contracts.  After deleting the proposed prefix
from each contract below, the remaining bytes are exactly the current landed
`contract:` value.  In particular, no coefficient, radius, inequality,
quantifier already present in a suffix, or estimate is changed.

The setting datum is defined only for
`0 <= eta <= rho_id^corr`.  This is not a hidden narrowing:

- row 3 already has exactly that domain;
- `rho_T <= rho_id^corr` because `rho_T` contains `rho_theta`, `rho_AI`, and
  `epsilon_E/C_A` in its defining minimum; and
- every other analytic row domain and `eta_K` is at most `rho_T` by the
  serial ledger.

The definition is a package of chosen witnesses, not an independent existence
theorem.  The named T0 dependencies remain responsible for furnishing the
package.  A hostile audit should apply the deletion test in Risk 1 below to
ensure that this packaging does not launder those theorem obligations into a
definition.

## 1. Proposed canonical setting definition

### 1.1 Exact proposed shard

Proposed path: `definitions/def-routef-raw-factor-setting.md`.
It remains `draft` until the separate audit and user ratification.

```markdown
---
id: def-routef-raw-factor-setting
term: Route-F raw-factor setting datum
aliases: finite-dimensional Route-F raw-factor datum; raw-factor witness package
kind: original
status: draft
source: internal
locus: DESIGN-LEDGER-SETTING-RESCOPE.md sect-1 (W136 proposal; pending hostile audit and user ratification)
sha256: -
consensus: W136 design proposal only; pending separate hostile audit and explicit user ratification
---

**Statement (witness package and notation).** A *Route-F raw-factor setting
datum* (S) consists of the following choices and derived objects.

1. Fix
   \[
   C_\theta:=12(\sqrt2-1),\qquad
   C_A:=20+\frac{211}{8}C_\theta,
   \]
   and fix a universal witness \(\eta_A>0\) furnished together with this
   \(C_A\) by `lem-routef-ai-defect-linearization`.  Fix universal witnesses
   \(C_E<\infty\) and \(\varepsilon_E>0\) furnished by
   `lem-thmainext-conditional`.  Put
   \[
   \rho_\theta:=\frac18,\qquad \rho_{\rm AI}:=\eta_A.
   \]

2. Choose a nonzero finite-dimensional complex Hilbert space \(H\), a scalar
   \(0\le\eta\le\rho_{\rm id}^{\rm corr}\), where the corrected radius is
   defined in item 5 below, and a
   [[def-ucp-map|UCP map]]
   \(\Phi:B(H)\to B(H)\) satisfying
   \(\lVert\Phi^2-\Phi\rVert_{\rm cb}\le\eta\).  This is the
   finite Route-F input; it is not the row-stochastic notion in
   [[def-almost-idempotent]].

3. Define, exactly as in `lem-routef-ai-defect-linearization`,
   \[
   \begin{aligned}
   \widetilde\Phi&:=\frac12\left(I+(2\Phi-I)
      \bigl(I-4(\Phi-\Phi^2)\bigr)^{-1/2}\right),
      &\mathcal A&:=\operatorname{Im}(\widetilde\Phi),\\
   X\star Y&:=\widetilde\Phi(XY),
      &r&:=\frac32\left((1-4\eta)^{-1/2}-1\right),
   \end{aligned}
   \]
   \[
   \varepsilon_{\rm AI}(\eta)
   :=\max\left\{
      r,
      20\eta+2\bigl((1+r)^5-1\bigr),
      3r-r^2
   \right\}.
   \]

   The datum uses the inherited operator-space norms, involution, and unit on
   \(\mathcal A\), and references
   [[def-extended-epsilon-cstar-algebra]] for the resulting structure; it does
   not restate that definition.

4. The applicability chain for the raw factor is part of the witness package.
   Since \(H\) is finite-dimensional,
   \(\mathcal A\subseteq B(H)\) is finite-dimensional.  Since
   \(\eta\le\rho_{\rm AI}=\eta_A\),
   `lem-routef-ai-defect-linearization` supplies the extended
   \(\varepsilon_{\rm AI}(\eta)\)-\(C^*\)-algebra structure and
   \[
   0\le\varepsilon_{\rm AI}(\eta)
      \le C_A\eta
      \le\varepsilon_E.
   \]
   Therefore `lem-thmainext-conditional`, applied to this same
   \(\mathcal A\), furnishes a finite-dimensional \(C^*\)-algebra
   \(\mathcal B\) and an
   [[def-extended-delta-inclusion|extended
   \(C_E\varepsilon_{\rm AI}(\eta)\)-isomorphism]]
   \(v:\mathcal B\to\mathcal A\).  The datum carries one such supplied pair
   \((\mathcal B,v)\) and defines
   \[
   \widetilde\Delta:=v:\mathcal B\to B(H),
   \qquad
   \widetilde\Upsilon:=v^{-1}\widetilde\Phi:B(H)\to\mathcal B.
   \]
   This clause packages chosen outputs of the two named result rows; it does
   not assert their existence without those dependencies.

5. The datum carries the following named scalar ledger, with the audit's
   corrected identity radius.  First,
   \[
   \bar C_E:=\max\{1,C_E\},\qquad
   C_V:=\bar C_EC_A,\qquad
   C_T:=C_\theta+3C_V,
   \]

   \[
   \rho_T:=\min\left\{
      \rho_\theta,\rho_{\rm AI},\frac{\varepsilon_E}{C_A},
      \frac1{4(1+C_\theta)},\frac1{4(1+C_V)}
   \right\}.
   \tag{1.1}
   \]
   Next,
   \[
   \begin{aligned}
   \rho_{\rm unit}&:=\rho_T,\\
   \rho_{\rm id}&:=\min\{\rho_{\rm AI},\varepsilon_E/C_A\},\\
   \rho_{\rm id}^{\rm corr}
     &:=\min\{\rho_\theta,\rho_{\rm AI},\varepsilon_E/C_A\},\\
   \rho_{\rm prod}&:=\rho_T,\\
   C_{\Delta'}&:=C_T+4C_\theta,\\
   \rho_{\Delta'}&:=\min\{\rho_T,\rho_{\rm prod}\},\\
   C_\Delta&:=6C_T+7C_{\Delta'},\\
   \rho_\Delta&:=\min\left\{
      \rho_{\rm unit},\rho_{\Delta'},
      [2(C_T+C_{\Delta'})]^{-1}
   \right\},\\
   C_2&:=C_{\Delta'}+4C_\Delta,\\
   \rho_2&:=\min\{\rho_{\rm prod},\rho_{\Delta'},\rho_\Delta\},\\
   \rho_{\Delta\Phi}&:=\min\{\rho_\theta,\rho_\Delta,\rho_2\},\\
   C_3&:=10+20C_\Delta+12C_\theta+2C_{\Delta'},\\
   \rho_3&:=\min\{\rho_\theta,\rho_{\Delta'},\rho_\Delta,\rho_2\}.
   \end{aligned}
   \tag{1.2}
   \]
   For the componentwise repair,
   \[
   \begin{aligned}
   C_N&:=C_V+C_\Delta,\\
   C_R&:=C_N+C_2=C_V+C_\Delta+C_2,\\
   C_L&:=C_2+C_3+2C_R,\\
   C_{\Upsilon'}&:=1+C_\theta+2C_\Delta+2C_L.
   \end{aligned}
   \tag{1.3}
   \]
   \[
   \rho_{\Upsilon'}:=\min\left\{
      \rho_T,\rho_{\rm id},\rho_\Delta,\rho_2,\rho_3,
      (2C_R)^{-1}
   \right\}.
   \tag{1.4}
   \]
   Continue with
   \[
   \begin{aligned}
   C_\Upsilon&:=6C_T+7C_{\Upsilon'},\\
   \rho_\Upsilon&:=\min\left\{
      \rho_{\rm unit},\rho_{\Upsilon'},
      [2(C_T+C_{\Upsilon'})]^{-1}
   \right\},\\
   \rho_{\Delta\Upsilon}&:=\min\{
      \rho_\theta,\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\},\\
   \rho_{\rm mult}&:=\min\{
      \rho_T,\rho_{\rm id},\rho_{\Delta\Phi},\rho_\Upsilon\},\\
   \rho_{\Upsilon\Delta}&:=\min\{
      \rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\}.
   \end{aligned}
   \tag{1.5}
   \]
   Finally,
   \[
   K:=\max\left\{
      1,
      C_\theta+C_\Delta+2C_\Upsilon,
      C_\Upsilon+2(C_2+C_\theta+C_\Delta),
      C_\Upsilon+2C_\Delta
   \right\},
   \tag{1.6}
   \]
   \[
   \rho_{\rm fac}:=\min\{
      \rho_2,\rho_{\Delta\Upsilon},
      \rho_{\rm mult},\rho_{\Upsilon\Delta}
   \},
   \tag{1.7}
   \]
   \[
   \eta_K:=\min\{\rho_{\rm fac},(24K)^{-1},1\}.
   \tag{1.8}
   \]

6. For a linear map \(T\) occurring in the datum and every integer \(q\ge1\),
   \(T_q:=\operatorname{id}_{M_q}\otimes T\).  In the registry contracts,
   the displayed subscript \(n\) is this arbitrary amplification index (not
   \(\dim H\)); “every amplification” quantifies over every \(n\ge1\), and
   the displayed \(X,Y,Z\) lie in \(M_n(\mathcal B)\) unless the displayed
   map types force another standard matrix-level domain.  Registry ASCII
   `A` and `B` denote \(\mathcal A\) and \(\mathcal B\); `I_B` is the unit of
   \(\mathcal B\).  An un-subscripted \(I\) denotes the unit of the source or
   target forced by the adjacent map.

**Scope and provenance.** This is one canonical project-introduced package
for the ambient notation formerly stated only in
`DESIGN-LEDGER-DOMAINS-v2.md` sect-1.  It references, rather than restates,
[[def-ucp-map]], [[def-extended-epsilon-cstar-algebra]], and
[[def-extended-delta-inclusion]].  It is not the stochastic
[[def-almost-idempotent]] notion, does not define the later repaired maps
\(\Delta',\Delta,\Upsilon',\Upsilon\), and promotes no result.
```

### 1.2 Definition-design checks

- **Why the corrected identity radius is the datum domain.** It is the
  largest named radius in this package on which all ingredients needed to
  define \(v\), \(v^{-1}\), `tilde-Delta`, and `tilde-Upsilon` are explicit,
  including the Kitaev `eta < 1/4` guard through `rho_theta=1/8`.
- **Why `rho_id` and `rho_id^corr` both appear.** The landed row 3 exports
  the corrected three-term radius, while later landed suffixes retain the
  original two-term `rho_id`.  They are not aliases:
  `rho_id^corr <= rho_id`.  No downstream effective domain changes because
  every later minimum that uses `rho_id` also descends from `rho_T`, and
  `rho_T <= rho_id^corr`.
- **Why the setting is not `def-almost-idempotent`.** The latter is a
  row-stochastic real `infinity->infinity` notion.  This package is a
  finite-dimensional complex UCP/cb datum.  The F0 lift is the later bridge
  between them.
- **Formation obligation.** A datum may be instantiated only using the named
  AI and MAIN witnesses.  The definition is not a replacement for those
  results.  The row-1 and row-3 dependency lists continue to carry both
  providers, and the future strengthened K-ledger must construct this same
  package from its F0 input rather than assume it for free.

## 2. Exact re-scoped registry contracts

### 2.1 Binding rule

The text after the final binder colon in every code block is the current
landed contract byte-for-byte.  The prefixes do three jobs only:

1. bind the raw setting and the equality `rho_AI := eta_A` through the new
   `def-` id;
2. bind `X,Y,Z` through the amplification convention in the definition; and
3. from row 6 onward, force every row to consume the same serially furnished
   maps rather than unrelated existential outputs.

“Furnished by `<id>`” means an output satisfying that dependency's exact
contract for the same setting datum; it introduces no new estimate.  The
later rows quantify over each such compatible choice because the producer
contracts do not claim uniqueness.

The naive raw-setting-only prefix is sufficient for rows 1--5.  It is
insufficient for rows 6, D2, 7, D3, and 8 (which need the same
`Delta',Delta` pair), row 9 (which additionally needs the matching
`Upsilon'`), and rows 10--14 (which need the whole successive packet).
Rows 1, 4, D2, 7, D3, and 11 also rely on the setting definition's explicit
amplification/index convention.  Row 14 needs its three imported scalar
interfaces in addition to the packet; its special restriction is explained
below.

### 2.2 Rows 1--4: raw packet

#### Row 1 — `lem-routef-raw-factor-norms`

```text
contract: For every def-routef-raw-factor-setting datum S, with the fields of S written as the unqualified symbols below: Raw factor-map norms: with C_V, C_T, rho_T from (1.1), for 0 <= eta <= rho_T, every amplification satisfies (1-C_V*eta)*||X|| <= ||tilde-Delta_n X|| <= (1+C_V*eta)*||X|| and max{||tilde-Delta||_cb, ||tilde-Upsilon||_cb} <= 1+C_T*eta.
```

The naive prefix is sufficient because the definition types `tilde-Delta`,
`tilde-Upsilon`, their amplifications, and `X`.

#### Row 2 — `lem-routef-raw-factor-units`

```text
contract: For every def-routef-raw-factor-setting datum S, with the fields of S written as the unqualified symbols below: Raw factor-map units: for 0 <= eta <= rho_unit := rho_T, max{||tilde-Delta(I)-I||, ||tilde-Upsilon(I)-I||} <= C_T*eta.
```

The unit convention in the definition removes the source/target ambiguity
without changing the landed shorthand.

#### Row 3 — `lem-routef-raw-factor-identities`

```text
contract: For every def-routef-raw-factor-setting datum S, with the fields of S written as the unqualified symbols below: Raw factor-map identities: for 0 <= eta <= rho_id^corr := min{rho_theta, rho_AI, epsilon_E/C_A}, tilde-Delta tilde-Upsilon = tilde-Phi and tilde-Upsilon tilde-Delta = I_B.
```

This is the exact repair of challenges `ch-fe50a1d47d30ca64`,
`ch-d2d3e5c963af4c30`, and `ch-dd2ab7c37c8541f1`: all named maps and
constants, the UCP/cb hypotheses, finite-dimensionality, and
`rho_AI := eta_A` are now in the root's registered definition import.

#### Row 4 — `lem-routef-raw-product-estimate`

```text
contract: For every def-routef-raw-factor-setting datum S, with the fields of S written as the unqualified symbols below: Raw tilde-Delta-product estimate: for 0 <= eta <= rho_prod := rho_T, every amplification and all X, Y satisfy ||tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y) - tilde-Delta_n(XY)|| <= C_T*eta*||X||*||Y||.
```

The naive prefix is sufficient; `X,Y` are typed by the definition's
amplification convention.

### 2.3 Delta packet, including D2/D3

#### Row 5 — `lem-routef-delta-prime-closeness`

```text
contract: For every def-routef-raw-factor-setting datum S, with the fields of S written as the unqualified symbols below: Delta-prime CP closeness: with C_Delta' := C_T+4*C_theta and rho_Delta' := min{rho_T, rho_prod}, for 0 <= eta <= rho_Delta', the repaired norm-one diagonal produces a CP map Delta' with ||Delta' - tilde-Delta||_cb <= C_Delta'*eta.
```

The row itself produces `Delta'`; no serial-output prefix is needed yet.

#### Row 6 — `lem-routef-delta-normalization-closeness`

```text
contract: For every def-routef-raw-factor-setting datum S and every Delta' furnished for S by lem-routef-delta-prime-closeness, with the fields of S written as the unqualified symbols below: Delta UCP normalization: with C_Delta := 6*C_T+7*C_Delta' and rho_Delta := min{rho_unit, rho_Delta', [2*(C_T+C_Delta')]^(-1)}, for 0 <= eta <= rho_Delta, a = Delta'(I) is invertible and Delta(X) = a^(-1/2)*Delta'(X)*a^(-1/2) is UCP with ||Delta - tilde-Delta||_cb <= C_Delta*eta.
```

The naive setting prefix alone would be wrong: `Delta'` is not a raw-setting
field and must be the output of row 5 for this same datum.

#### D2 — `lem-routef-degree-two-estimate`

```text
contract: For every def-routef-raw-factor-setting datum S and every successive pair (Delta', Delta) furnished for S by lem-routef-delta-prime-closeness and lem-routef-delta-normalization-closeness, with the fields of S written as the unqualified symbols below: Route F degree-two estimate: with C_2 := C_Delta'+4*C_Delta and rho_2 := min{rho_prod, rho_Delta', rho_Delta}, for 0 <= eta <= rho_2, every amplification satisfies ||Phi_n(Delta_n X Delta_n Y) - Delta_n(XY)|| <= C_2*eta*||X||*||Y||.
```

D2 needs both the serial-output binder and the definition's typing of every
amplification and `X,Y`.  A naive prefix leaves `Delta` free.

#### Row 7 — `lem-routef-delta-phi-product`

```text
contract: For every def-routef-raw-factor-setting datum S and every successive pair (Delta', Delta) furnished for S by lem-routef-delta-prime-closeness and lem-routef-delta-normalization-closeness, with the fields of S written as the unqualified symbols below: Normalized Delta product: for rho_DeltaPhi := min{rho_theta, rho_Delta, rho_2} and 0 <= eta <= rho_DeltaPhi, every amplification satisfies ||tilde-Phi_n(Delta_n X Delta_n Y) - tilde-Delta_n(XY)|| <= (C_2+C_theta+C_Delta)*eta*||X||*||Y||.
```

The pair binder retains the exact `Delta` produced from the row-5
`Delta'`; D2 supplies the estimate for that same pair.

#### D3 — `lem-routef-degree-three-estimate`

```text
contract: For every def-routef-raw-factor-setting datum S and every successive pair (Delta', Delta) furnished for S by lem-routef-delta-prime-closeness and lem-routef-delta-normalization-closeness, with the fields of S written as the unqualified symbols below: Route F degree-three estimate: with C_3 := 10+20*C_Delta+12*C_theta+2*C_Delta' and rho_3 := min{rho_theta, rho_Delta', rho_Delta, rho_2}, for 0 <= eta <= rho_3, every amplification satisfies ||Phi_n(Delta_n X Delta_n Y Delta_n Z) - Delta_n(XYZ)|| <= C_3*eta*||X||*||Y||*||Z||.
```

D3 needs the same serial-output and amplification binders as D2, now also
typing `Z`.  Its direct Kitaev dependency still supplies the associativity
estimate; the setting definition does not replace that proof obligation.

### 2.4 Upsilon packet and telescopes

#### Row 8 — `lem-routef-upsilon-prime-closeness`

```text
contract: For every def-routef-raw-factor-setting datum S and every successive pair (Delta', Delta) furnished for S by lem-routef-delta-prime-closeness and lem-routef-delta-normalization-closeness, with the fields of S written as the unqualified symbols below: Upsilon-prime CP closeness: with C_N, C_R, C_L, C_Upsilon' from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every Choi multiplicity space used below is nonzero and the componentwise construction produces CP Upsilon' with ||Upsilon' - tilde-Upsilon||_cb <= C_Upsilon'*eta.
```

The row produces `Upsilon'` but consumes the same normalized `Delta` used by
D2 and D3.  A raw-setting-only prefix would not enforce that coherence.

#### Row 9 — `lem-routef-upsilon-normalization-closeness`

```text
contract: For every def-routef-raw-factor-setting datum S, every successive pair (Delta', Delta) furnished for S by lem-routef-delta-prime-closeness and lem-routef-delta-normalization-closeness, and every Upsilon' furnished for those same data by lem-routef-upsilon-prime-closeness, with the fields of S written as the unqualified symbols below: Upsilon UCP normalization: with C_Upsilon := 6*C_T+7*C_Upsilon' and rho_Upsilon := min{rho_unit, rho_Upsilon', [2*(C_T+C_Upsilon')]^(-1)}, for 0 <= eta <= rho_Upsilon, b = Upsilon'(I) is invertible and Upsilon(X) = b^(-1/2)*Upsilon'(X)*b^(-1/2) is UCP with ||Upsilon - tilde-Upsilon||_cb <= C_Upsilon*eta.
```

The naive prefix is wrong because `Upsilon'` is a row-8 output, not a field
of the raw datum.

#### Row 10 — `lem-routef-delta-upsilon-telescope`

```text
contract: For every def-routef-raw-factor-setting datum S and every successive packet (Delta', Delta, Upsilon', Upsilon) furnished for S by lem-routef-delta-prime-closeness, lem-routef-delta-normalization-closeness, lem-routef-upsilon-prime-closeness, and lem-routef-upsilon-normalization-closeness, with the fields of S written as the unqualified symbols below: Delta-Upsilon telescope: for rho_DeltaUpsilon := min{rho_theta, rho_T, rho_id, rho_Delta, rho_Upsilon} and 0 <= eta <= rho_DeltaUpsilon, ||Delta Upsilon - Phi||_cb <= (C_theta+C_Delta+2*C_Upsilon)*eta.
```

#### Row 11 — `lem-routef-multiplicative-telescope`

```text
contract: For every def-routef-raw-factor-setting datum S and every successive packet (Delta', Delta, Upsilon', Upsilon) furnished for S by lem-routef-delta-prime-closeness, lem-routef-delta-normalization-closeness, lem-routef-upsilon-prime-closeness, and lem-routef-upsilon-normalization-closeness, with the fields of S written as the unqualified symbols below: Multiplicative telescope: for rho_mult := min{rho_T, rho_id, rho_DeltaPhi, rho_Upsilon} and 0 <= eta <= rho_mult, every amplification satisfies ||Upsilon_n(Delta_n X Delta_n Y) - XY|| <= [C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||.
```

The definition supplies the amplification convention; the packet prefix
ensures the same `Delta,Upsilon` are used at every level.

#### Row 12 — `lem-routef-upsilon-delta-telescope`

```text
contract: For every def-routef-raw-factor-setting datum S and every successive packet (Delta', Delta, Upsilon', Upsilon) furnished for S by lem-routef-delta-prime-closeness, lem-routef-delta-normalization-closeness, lem-routef-upsilon-prime-closeness, and lem-routef-upsilon-normalization-closeness, with the fields of S written as the unqualified symbols below: Upsilon-Delta telescope: for rho_UpsilonDelta := min{rho_T, rho_id, rho_Delta, rho_Upsilon} and 0 <= eta <= rho_UpsilonDelta, ||Upsilon Delta - I_B||_cb <= (C_Upsilon+2*C_Delta)*eta.
```

### 2.5 Aggregation and terminal admissibility

#### Row 13 — `lem-routef-k-finiteness`

```text
contract: For every def-routef-raw-factor-setting datum S and every successive packet (Delta', Delta, Upsilon', Upsilon) furnished for S by lem-routef-delta-prime-closeness, lem-routef-delta-normalization-closeness, lem-routef-upsilon-prime-closeness, and lem-routef-upsilon-normalization-closeness, with the fields of S written as the unqualified symbols below: Route F common coefficient/domain: K in (1.6) is finite and universal, and rho_fac in (1.7) is positive and is a common domain for the degree-two estimate and the three Route-F factorization estimates.
```

The packet binder makes “the” four estimates refer to one construction,
which is exactly what the proposed strengthened K-ledger consumes.

#### Row 14 — `lem-routef-threshold-minimum`

```text
contract: For every def-routef-raw-factor-setting datum S and every successive packet (Delta', Delta, Upsilon', Upsilon) furnished for S by lem-routef-delta-prime-closeness, lem-routef-delta-normalization-closeness, lem-routef-upsilon-prime-closeness, and lem-routef-upsilon-normalization-closeness, with the fields of S written as the unqualified symbols below and with the scalar hypotheses of lem-routef-f2-positive-unital-compression, lem-routef-f3-retract-defect, and lem-routef-prh-finish read at the same eta and K: Route F threshold minimum: importing the black-box constants C_E, epsilon_E used in rows 1-4, let eta_K := min{rho_fac, (24*K)^(-1), 1}; then eta_K > 0, and for 0 <= eta <= eta_K the three factorization estimates have common coefficient K, the F2 and F3 smallness conditions hold, and the PRH finish is admissible.
```

The naive raw-setting prefix is wrong for row 14.  An arbitrary UCP
`Phi:B(H)->B(H)` is not yet an F0 lift of a row-stochastic `Q`, and the raw
datum does not contain F2's `Q,D,J,Q_C`, F3's `A,M`, or PRH's retract datum.
The added binder names all three imported result ids and is deliberately
limited to their **scalar hypotheses at the same `eta,K`**.  The future
strengthened `lem-routef-k-ledger` remains
responsible for binding the F0 variables, applying F2 to this same factor-map
packet, passing its outputs to F3, and then invoking PRH.  This prefix does not
claim those non-smallness hypotheses follow from an arbitrary raw datum.

## 3. Corrected `defs:` lines

### 3.1 Global disposition

`def-almost-idempotent` must be dropped from every one of the sixteen rows.
It defines a real row-stochastic `infinity->infinity` defect and is not an
ambient definition for a complex UCP/cb raw factorization.  The replacement
is `def-routef-raw-factor-setting`.

`def-extended-epsilon-cstar-algebra` and
`def-extended-delta-inclusion` are referenced inside the one canonical
setting definition and should not be repeated on contracts whose suffix does
not itself use those terms.  `def-ucp-map` remains a direct import on rows
whose suffix concludes that a named map is CP or UCP.  The diagonal and
stochastic/PRH definitions remain where the suffix directly uses their
vocabulary.

### 3.2 Full proposed lines

| order | id | exact proposed `defs:` line |
|---:|---|---|
| 1 | `lem-routef-raw-factor-norms` | `defs: def-routef-raw-factor-setting` |
| 2 | `lem-routef-raw-factor-units` | `defs: def-routef-raw-factor-setting` |
| 3 | `lem-routef-raw-factor-identities` | `defs: def-routef-raw-factor-setting` |
| 4 | `lem-routef-raw-product-estimate` | `defs: def-routef-raw-factor-setting` |
| 5 | `lem-routef-delta-prime-closeness` | `defs: def-routef-raw-factor-setting; def-fd-cstar-diagonal; def-ucp-map` |
| 6 | `lem-routef-delta-normalization-closeness` | `defs: def-routef-raw-factor-setting; def-ucp-map` |
| D2 | `lem-routef-degree-two-estimate` | `defs: def-routef-raw-factor-setting` |
| 7 | `lem-routef-delta-phi-product` | `defs: def-routef-raw-factor-setting` |
| D3 | `lem-routef-degree-three-estimate` | `defs: def-routef-raw-factor-setting` |
| 8 | `lem-routef-upsilon-prime-closeness` | `defs: def-routef-raw-factor-setting; def-ucp-map` |
| 9 | `lem-routef-upsilon-normalization-closeness` | `defs: def-routef-raw-factor-setting; def-ucp-map` |
| 10 | `lem-routef-delta-upsilon-telescope` | `defs: def-routef-raw-factor-setting` |
| 11 | `lem-routef-multiplicative-telescope` | `defs: def-routef-raw-factor-setting` |
| 12 | `lem-routef-upsilon-delta-telescope` | `defs: def-routef-raw-factor-setting` |
| 13 | `lem-routef-k-finiteness` | `defs: def-routef-raw-factor-setting` |
| 14 | `lem-routef-threshold-minimum` | `defs: def-routef-raw-factor-setting; def-stochastic; def-positive-approximate-retract` |

The hostile audit should specifically test whether CP, as used on rows 5 and
8, is accepted as the CP clause of `def-ucp-map`; if the definitions gate
requires a separate CP term, that is a definition-design escalation rather
than permission to duplicate the CP definition here.

## 4. Continuation plan for the two live `af` trees

### 4.1 What `af amend` preserves

With the installed `af version 0.1.6`, `af amend` is allowed only on a
`pending` node.  Its ledger replay handler changes only that node's statement
and content hash and records amendment history; it does not change child
statements or epistemic states.  Thus amending either pending root, or a
pending interior node, mechanically preserves all already-validated
descendants.

That is state preservation, not a correctness shortcut.  Every amended node
and each amended ancestor must still be reviewed bottom-up by a fresh hostile
verifier, who must check that the unchanged validated children really imply
the amended statement.  A validated node cannot be amended; if its statement
is awkward but still usable, add a small pending bridge instead of
unvalidating it.

Landing must be atomic with contract match: add the new definition, register
it once in each workspace, change the registry contract, and `af amend 1` to
the exact same text before running the linker.  Do not leave a changed shard
against an old root even transiently at a commit boundary.

### 4.2 `lem-routef-raw-factor-norms`

Current state: 20 nodes, 13 validated, 7 pending.  Preserve all 13 validated
nodes.  Register `def-routef-raw-factor-setting` exactly once, then amend the
following pending nodes:

| node | required amendment |
|---|---|
| `1` | exact row-1 contract from §2.2; this is mandatory for linker contract match and directly answers `ch-782c366f12ac5fee` |
| `1.1` | replace “ambient finite-dimensional raw-factor setup” by the fixed `def-routef-raw-factor-setting` datum `S`, with `tilde-Delta=v` unpacked from `S` |
| `1.1.1` | state the radius/domain inference as unpacking `S.rho_AI=S.eta_A`, `S.rho_T`, and the AI/MAIN applicability chain already recorded in the definition |
| `1.1.1.1` | replace the unsupported `local_assume` by “unpack the fixed datum `S`”; then resolve open challenge `ch-7d5f34bdc70447b1` with that exact scope repair |
| `1.2` | bind `tilde-Upsilon=v^(-1) tilde-Phi` as the field of the same `S` |
| `1.2.3` | replace “reapplying” the ambient setup by the extended-isomorphism and raw-map fields of `S`; retain the same inverse estimate and conclusion |
| `1.2.3.2` | replace the unqualified “by definition” with the `tilde-Upsilon=v^(-1) tilde-Phi` field of `S`; retain its validated estimate child and conclusion |

These are all seven currently pending nodes.  In particular, amendment of
`1.2.3.2` is wording/scope repair only: its validated child `1.2.3.2.1`
already supplies the two estimates and the composition identity.  No
validated node is to be amended or unvalidated.

Expected finish budget:

- **nodes:** 20 total, no new node expected; hard stop at 22 permits at most
  two genuinely necessary repair leaves while remaining below the shared
  soft cap 26;
- **verification waves:** four bottom-up waves are forced by the current
  longest pending chain
  `1.1.1.1 -> 1.1.1 -> 1.1 -> 1` (the inverse branch can proceed in
  parallel); and
- **round allowance:** resume verification on the same tree with at most six
  rounds.  A request to exceed 22 nodes or six rounds is a stop for factoring,
  not permission to enlarge the cap.

### 4.3 `lem-routef-raw-factor-identities`

Current state: 5 nodes, 4 validated, only root `1` pending.  Register the new
definition exactly once and amend only root `1` to the exact row-3 contract
from §2.2.  The two validated children remain valid reusable components:

- `1.1` is an explicitly conditional setup lemma with the exact
  `rho_AI:=eta_A` equality and the AI/MAIN applicability chain; and
- `1.2` is the abstract algebraic identity lemma.

The amended root's definition binder supplies precisely the hypotheses of
`1.1`, so the sentence in `1.1` saying that it did not derive them from the
*old* root is harmless historical caution, not a new premise.  Resolve open
challenge `ch-fe50a1d47d30ca64` only after the root amendment and definition
registration, then send the root to a fresh verifier.

Expected finish budget:

- **nodes:** 5 total, no new node expected;
- **rounds:** one fresh root-verification round expected;
- **contingency:** if the verifier demands an explicit definition-to-`1.1`
  application bridge because of that historical sentence, add one root child
  and stop at 6 total nodes / two rounds.  Do not unvalidate or amend `1.1`.

Neither continuation changes mathematical status by itself.  Both registry
rows remain `status: stated` until their amended roots are independently
validated and banked under the normal protocol.

## 5. Blast-radius and consumer audit

### 5.1 Current registry consumers

At the current registry state, every direct consumer of one of the sixteen
rows is another row in the same serial family.  There is no external registry
consumer yet: the proposed `lem-routef-k-ledger` rewire has deliberately not
landed.  The serial order remains

```text
1, 2, 3, 4, 5, 6, D2, 7, D3, 8, 9, 10, 11, 12, 13, 14.
```

The new prefixes add no dependency edge and no reverse reference.  They make
the already-intended common data explicit, so the internal DAG remains
acyclic.  The `deps:` lines themselves are unchanged by this design.

### 5.2 Proposed `lem-routef-k-ledger` consumption

The audited v2 proposed parent wiring consumes rows 10--14 plus F2, F3, and
PRH.  The F0 design's strengthened replacement contract also requires that
the three estimates use one `B,Phi,Delta,Upsilon,eta` packet.  The re-scope is
consumption-compatible:

- F0 supplies a finite-dimensional UCP `Phi` and transfers the same defect
  `eta` exactly;
- the AI and MAIN rows furnish a `def-routef-raw-factor-setting` datum for
  that input on the required radius;
- rows 5--9 furnish one explicitly threaded
  `(Delta',Delta,Upsilon',Upsilon)` packet;
- rows 10--12 export the three estimates for that same packet;
- row 13 chooses the same universal `K`; and
- row 14 checks the F2/F3/PRH scalar guards for that same `eta,K` without
  pretending the raw datum itself contains a stochastic `Q`.

When the strengthened K-ledger is separately landed, its own `defs:` line
should import `def-routef-raw-factor-setting` because its contract will bind
this packet.  That is a future F0-package edit, not part of the sixteen-row
re-scope.

### 5.3 F0 assembly and guard

`lem-routef-f0-assembly` consumes only the future strengthened
`lem-routef-k-ledger`, so its contract and dependency line need no change for
this re-scope.  The F0 design already identified “common-datum binders” as a
precondition to the strengthened parent; this package supplies them.

**The DO-NOT-REWIRE guard stays untouched.**  This design does not change
`lem-routef-k-ledger`, `lem-routef-f0-assembly`, `op-classical`, any
`deps:`/`routes:` line, or any status.  The guard may be released only by the
separately audited and user-ratified F0 landing package in its prescribed
serial order.

## 6. Ranked hostile-audit risks

1. **Definition-as-theorem laundering / formation gap (highest).**  Delete
   the AI and MAIN dependencies mentally.  If the new definition alone would
   still assert that `B,v` exist for every UCP/cb input, the design is wrong.
   It must package chosen outputs only, while the named results furnish them.
   The auditor must also verify that the future K-ledger can form the datum
   from F0 rather than assume it.
2. **Silent domain narrowing or circular datum formation.**  Recompute that
   `rho_T <= rho_id^corr <= rho_id`, every later row radius is at most `rho_T`, and
   `eta_K <= rho_T`; verify that `v` is chosen before any quantity whose
   definition depends on `v`, and that no scalar depends on future `eta_K`.
3. **Existential-output coherence.**  Attack rows 6--14 by choosing different
   valid `Delta'`, `Delta`, `Upsilon'`, or `Upsilon` outputs at adjacent rows.
   The prefixes must force one successive packet without adding uniqueness.
4. **Row-14 F0/F2/F3/PRH quantifier leakage.**  Verify that the terminal row
   asserts only common scalar admissibility at the same `eta,K`; it must not
   infer row-stochastic `Q`, F2 maps `A,M`, or PRH hypotheses from an arbitrary
   raw UCP datum.
5. **Witness-choice drift.**  `C_A,eta_A` and `C_E,epsilon_E` must be fixed
   once and threaded throughout; `rho_AI := eta_A` must be literal.  An
   existential witness may not be silently reselected between rows.
6. **L2 duplication.**  Compare the proposed definition line-by-line with
   `def-ucp-map`, `def-extended-epsilon-cstar-algebra`,
   `def-extended-delta-inclusion`, and `def-almost-idempotent`.  It should
   reference their terms and define only the Route-F package and ledger.
7. **Suffix byte drift / ASCII normalization.**  Strip each prefix through
   its final `: ` and compare the remaining bytes with the landed shard's
   `contract:` value.  Pay special attention to `rho_id^corr`, apostrophes in
   `C_Delta'`/`C_Upsilon'`, multiplication stars, brackets, `I_B`, and
   `infinity` versus `inf` spelling.  Any difference is a design rejection.
8. **Amplification typing.**  Attack rows 1, 4, D2, 7, D3, and 11 at a general
   matrix level.  Check that the setting convention types `X,Y,Z`, and that
   every serial output is amplified on the intended source and target.
9. **Mechanical preservation mistaken for review.**  `af amend` preserves
   validated child states mechanically, but a changed ancestor still needs a
   fresh verifier.  The auditor should reject any continuation plan that
   treats preserved child badges as validation of the new root.
10. **Premature blast-radius expansion.**  Confirm a repository diff for the
    eventual design landing would touch only the authorized definition, the
    sixteen contract/defs lines and their exact two live roots, plus required
    generated artifacts.  In particular, the K-ledger DO-NOT-REWIRE guard and
    all statuses remain unchanged until their later authorized phases.

## 7. Audit/ratification gate

This file is the complete design package, not authorization to enact it.  A
separate fresh hostile auditor should return one of `LAND`,
`LAND-WITH-EXACT-CORRECTIONS`, or `DESIGN-REJECTED`, explicitly disposing all
ten risks and independently checking all sixteen suffixes.  Only after the
user ratifies that audited package may an implementation round touch
`definitions/`, `argument/`, or either `proofs/` workspace.

Until then:

- all sixteen rows remain `status: stated`;
- the two live rows remain `af: seeded` with their current ledgers intact;
- no definition is added;
- no root or interior node is amended; and
- the `lem-routef-k-ledger` DO-NOT-REWIRE guard remains in force.
