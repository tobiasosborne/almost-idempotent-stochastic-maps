# BRIEF — v2 design: repair DESIGN-KLEDGER-STRENGTHENED.md per the hostile audit

You are a fresh design worker (independent context; you wrote neither the v1
design nor the audit). The v1 design
(`docs/plans/2026-08-08-KLEDGER-STRENGTHENED/DESIGN-KLEDGER-STRENGTHENED.md`)
was hostile-audited
(`docs/plans/2026-08-08-KLEDGER-STRENGTHENED/AUDIT-KLEDGER-STRENGTHENED.md`)
with **VERDICT: REJECT** — 1 FATAL + 3 HIGH findings, and 10 attacks CLEARED.
Your job: produce the v2 design that repairs the four findings WITHOUT
disturbing anything the audit cleared.

## Binding starting point

The audit CLEARED (findings 5–12): the strengthened parent contract text and
its 15-dep block (authorization-faithful, byte-exact seams, Q_C typing), the
eta-domain chain, packet existence via formation + rows 5/6/8/9, the
15-vs-16 decision (do NOT add the component-construction row), same-datum
threading, dimension-freeness, F0-assembly minimality (§3), status honesty
(`stated`/`af: none`, superseded W74F history), and guard-release scope.
**Reuse all of that VERBATIM from v1.** Any change to a cleared contract
text must be flagged loudly and justified — default is byte-identical reuse.

## The four findings to repair (BINDING; quote each and show its repair)

1. **FATAL — no cap-compliant elevation package (audit finding 1).** The
   parent monolith honestly projects 26–51 nodes against HARD CAP 22. The
   v1 fallback factoring (§6.2) had no auditable contracts. You must now
   design the factoring PROPERLY, as first-class registry rows: land-ready
   helper shard(s) with complete frontmatter (contract/defs/deps/status/
   provenance/workspace), same-datum quantifier prefixes consistent with
   the family pattern, exact seeding packages, and af skeletons whose
   honest expectation under the observed 1.5–3x expansion is STRICTLY
   under each cap (cap <= 22 per target; do not park a target exactly at
   its cap under 3x). The audit suggests the natural split; you decide the
   exact one, but every piece must be independently auditable. The
   strengthened parent's contract stays as cleared; only its deps line may
   gain the helper ids (justify each edge).
2. **HIGH — quantifier hoist (audit finding 2).** The root asserts
   `K >= 1` and `eta_K > 0` BEFORE `for every n, Q, eta`, but rows 13/14
   supply those facts only inside a fixed admissible packet. Repair
   explicitly: either (a) a pre-forall scalar-positivity argument from the
   W_RF header scalars alone (check `definitions/def-routef-raw-factor-setting.md`
   (1.1)–(1.8): are K and eta_K defined by header-scalar formulas
   independent of the packet? If so, prove positivity/finiteness at that
   level — possibly as one of the helper rows), or (b) an admissible
   dummy-input instantiation, or (c) a contract rephrasing that moves the
   scalar claims inside the quantifiers WITHOUT weakening what
   `lem-routef-f0-assembly` and the future root discharge need (if you take
   (c), re-verify the F0-assembly specialization still goes through and
   flag the contract delta loudly — it touches a cleared text). Argue
   which option is correct, pick ONE, and design it fully.
3. **HIGH — textbook-fact census (audit finding 3).** Enumerate EVERY
   textbook/definitional fact the skeleton silently uses (the audit names:
   positivity and coordinate inequalities for finite minima/maxima and
   reciprocals; the canonical identifications `M_1(B)=B`, `Delta_1=Delta`,
   `Upsilon_1=Upsilon` at level one; positivity of `sqrt(eta)` and
   `K+4*sqrt(2K)`; find any others). For each: classify as
   BSc/MSc-common-knowledge (L2 exemption, no provisioning) or as a fact
   to provision (say exactly how: def-add, external, or in-skeleton node).
   The 37-node Wedderburn balloon (FINDINGS.md 2026-08-08) is the
   precedent: no silently-invoked theorem may be left for a prover to
   re-derive.
4. **HIGH — stale report prose (audit finding 4).** Extend the landing
   manifest (§8) to explicitly include repairing
   `report/sections/41_status_outlook.tex:97–111` (stale
   `lem-thmainext-conditional` proved-mod-audit/quarantine prose),
   `report/sections/36_routef_prh_finish.tex:124–127`, and
   `report/sections/44_routef_f2_f3.tex:199–203`; re-sweep `report/` for
   any OTHER prose stale against the current registry state (grep for
   thmainext/k-ledger/proved-mod-audit claims) and enumerate every locus.

## Inputs you MUST read

- The v1 design and the audit (same directory) — your primary sources.
- `definitions/def-routef-raw-factor-setting.md` (whether K, eta_K are
  header-scalar formulas — decisive for finding 2).
- The frozen contracts of rows 13/14 (`lem-routef-k-finiteness`,
  `lem-routef-threshold-minimum`) and of all 15 deps.
- `docs/plans/2026-08-08-ROW8-FACTOR/DESIGN-ROW8-FACTOR.md` (the ratified
  factoring precedent: shard format, budgets, seeding-package style).
- `report/sections/41_status_outlook.tex`, `36_routef_prh_finish.tex`,
  `44_routef_f2_f3.tex` (the named stale loci) + a repo-wide grep.
- `CLAUDE.md` §§1, 6; `FINDINGS.md` 2026-08-05 and 2026-08-08;
  `scripts/af_constants.py`.

## Deliverable

Write EXACTLY ONE file:
`docs/plans/2026-08-08-KLEDGER-STRENGTHENED/DESIGN-KLEDGER-STRENGTHENED-V2.md`
— self-contained (a reader must not need v1): carry forward the cleared
material verbatim, then the four repairs, each headed
`## Repair of audit finding N`, then the updated complete package:
(a) all land-ready shard texts (parent replacement, F0 assembly, every new
    helper row); (b) re-run seam table if any contract changed (else state
    byte-identity); (c) af skeletons + budgets per target (honest 1.5–3x
    assessment, every target strictly under its cap); (d) seeding packages
    incl. the finding-3 census; (e) the corrected complete landing
    manifest; (f) elevation order; (g) ranked risks for the fresh
    re-audit, incl. any NEW risk your repairs introduce.

Head the file with: `Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD,
SEED, OR PROMOTE — pending fresh hostile re-audit and user ratification.`

## Discipline (non-negotiable)

Write ONLY the deliverable file. Do NOT edit `argument/`, `definitions/`,
`proofs/`, `report/`, or any other file. Do NOT run git commit or git push.
Do NOT run `af` mutations. Your final message: <=10 lines — the factoring
you chose (row count + budgets), the finding-2 option you took, the census
size, and whether any cleared contract text changed.
