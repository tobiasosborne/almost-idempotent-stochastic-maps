# AUDIT — landing transcription of LEDGER-SETTING-RESCOPE v2

Date: 2026-08-05
Role: fresh independent transcription auditor
Status: **NON-RIGOROUS TRANSCRIPTION AUDIT / NOTHING PROMOTED**

## 0. Verdict

**TRANSCRIPTION-REJECTED.**

The registry contracts, formation shard interface, `defs:` lines, `deps:`
lines, generator replay, live `af` roots, and `report/UNWIRED.md` entry all
pass the requested checks.  The landing nevertheless fails the strict
transcription requirement in two places:

1. after reversing only the declared `\tag` to `\qquad (1.n)`,
   `{\rm X}` to `{\mathrm{X}}`, and display-delimiter adaptations, the new
   definition body still differs from design section 1.1 at four exact
   loci; and
2. the row-3 body appends a citation inside the sentence that the design
   prescribed verbatim.

None of the definition drift adds a theorem or analytic conclusion.  It is
editorial/notation drift, but it is outside the explicitly allowed
adaptations and therefore cannot receive a byte-faithful confirmation.
This audit changes none of the landed files and promotes no result.

## 1. Numbered findings

| no. | severity | exact locus | finding | exact correction |
|---:|---|---|---|---|
| 1 | **HIGH (transcription)** | `definitions/def-routef-raw-factor-setting.md:19`; design section 1.1 lines 78--82 | The landed display changes the designed four-field tuple `(η_A,C_A,C_E,ε_E)` into the assignment `W_RF=(η_A,C_A,C_E,ε_E)`.  This is not one of the declared report adaptations. | Delete `W_{RF}=` so the display is exactly `(\eta_A,C_A,C_E,\varepsilon_E).` |
| 2 | **LOW (transcription)** | `definitions/def-routef-raw-factor-setting.md:25`; design section 1.1 line 88 | The landing changes `\frac18` to `\tfrac18`, an undeclared LaTeX rewrite. | Replace `\tfrac18` by `\frac18`. |
| 3 | **LOW (transcription)** | `definitions/def-routef-raw-factor-setting.md:162-166`; design section 1.1 lines 230--232 | The notes change the designed curly quotation marks to ASCII quotes and add a parenthesized list of three wiki links.  The extra links are not part of section 1.1 or a declared adaptation. | Restore exactly: `The terms “UCP map”, “extended epsilon-C*-algebra”, and “extended delta-isomorphism” are referenced from their canonical shards and are not redefined here.` |
| 4 | **LOW (transcription)** | `definitions/def-routef-raw-factor-setting.md:167-169`; design section 1.1 ends at line 234 | The landing adds the sentence identifying this definition as an instance of two other typed-witness patterns.  It is documentary, not theorem content, but it is absent from the ratified design. | Delete `This is the Route-F instance of the typed-witness pattern in [[def-maincb-witness-ledger]] and [[def-stage1-polar-witness-data]].` |
| 5 | **MEDIUM (transcription)** | `argument/lemmas/lem-routef-raw-factor-identities.md:36`; design section 3.2 lines 368--373 / re-audit finding 8 | The prescribed replacement sentence is not byte-equal: the landing inserts `(AUDIT-LEDGER-SETTING-RESCOPE-V2.md finding 8)` before its final period. | End the sentence exactly as prescribed: “Only this row uses `rho_id^corr`; later rows retain the two-term `rho_id`, and their effective domains are unchanged because they also descend from `rho_T <= rho_id^corr`.” |

## 2. Contract, definition-import, and dependency checks

The 16 landed family contracts are byte-equal to the corresponding design
section 3 blocks after applying re-audit correction 1 exactly:

- row 6 inserts `and for every X in S.B` before `writing the fields`;
- row 9 inserts `and for every X in B(H)` at the corresponding locus; and
- no other contract change was found.

For rows 1--13 plus D2/D3, the current contract ends with the complete
parent-commit contract byte-for-byte.  The independently recomputed suffix
SHA256 prefixes are:

| row | id | SHA256[:16] | result |
|---:|---|---|---|
| 1 | `lem-routef-raw-factor-norms` | `880d2f981e98975d` | BYTE-EQUAL |
| 2 | `lem-routef-raw-factor-units` | `41b441234ed6df2c` | BYTE-EQUAL |
| 3 | `lem-routef-raw-factor-identities` | `ada66693219c992b` | BYTE-EQUAL |
| 4 | `lem-routef-raw-product-estimate` | `2f4d8c2c0f9fc278` | BYTE-EQUAL |
| 5 | `lem-routef-delta-prime-closeness` | `be0654b5690e4e7a` | BYTE-EQUAL |
| 6 | `lem-routef-delta-normalization-closeness` | `38c4d6c810ee3c30` | BYTE-EQUAL |
| D2 | `lem-routef-degree-two-estimate` | `c9af7e4c3203eec8` | BYTE-EQUAL |
| 7 | `lem-routef-delta-phi-product` | `1967e28e3eec1204` | BYTE-EQUAL |
| D3 | `lem-routef-degree-three-estimate` | `fee246d3fe2936bd` | BYTE-EQUAL |
| 8 | `lem-routef-upsilon-prime-closeness` | `f19e937db51bfdf8` | BYTE-EQUAL |
| 9 | `lem-routef-upsilon-normalization-closeness` | `70bc606cc2fbd653` | BYTE-EQUAL |
| 10 | `lem-routef-delta-upsilon-telescope` | `a4af5c461ccb7517` | BYTE-EQUAL |
| 11 | `lem-routef-multiplicative-telescope` | `29f16e63504d4a17` | BYTE-EQUAL |
| 12 | `lem-routef-upsilon-delta-telescope` | `371d8380b51f8c23` | BYTE-EQUAL |
| 13 | `lem-routef-k-finiteness` | `abb2c54dabd9c5aa` | BYTE-EQUAL |

Row 14's complete landed contract is byte-equal to the revised design
section 3.5 contract.  It contains only the scalar threshold assertions and
does not restore the removed F2/F3/PRH interface.

All 16 `defs:` lines are byte-equal to design section 3.6.  All 16 `deps:`
lines are byte-equal to their individual design row blocks, including the
direct producer edges required by the earlier audit.

## 3. Formation and body checks

- `lem-routef-raw-factor-setting-formation` has a `contract:` byte-equal to
  design section 2.1.  Its `defs:` and `deps:` lines are also byte-equal.
- The row-6 and row-9 bodies explicitly record re-audit correction 1 with
  the correct binder domains and state that their suffixes are unchanged.
- Row 14 honestly records that it is the sole suffix revision, identifies
  the removed phantom F2/F3/PRH interface, and assigns actual application to
  the future strengthened `lem-routef-k-ledger`.
- Row 3 fails only in the exact documentary manner recorded as finding 5;
  its contract and mathematical suffix are correct.

The definition frontmatter is schema-correct (`original`, `locked`, internal
source, ratification recorded).  `python3 scripts/check-defs.py --check`
reports 47 shards and 0 errors.  Reversing the three allowed presentation
adaptations exposes exactly findings 1--4 above; no existence, positivity,
universality, idempotence, approximate-algebra, isomorphism, inverse, norm,
CP, or UCP theorem content has crept into the record schema.

## 4. Reproducer, live roots, and report wiring

The required replay was run:

```text
python3 scripts/land-ledger-domains-rows.py
git status --porcelain
```

The generator reported rewriting the 17 intended shards, and
`git status --porcelain` produced no output immediately afterward.  Thus the
retained generator reproduces the landed state idempotently, including its
currently transcribed definition/body text.

Using `/home/tobiasosborne/go/bin/af get 1 -f json`:

| workspace | root vs registry after whitespace normalization |
|---|---|
| `proofs/lem-routef-raw-factor-norms` | MATCH |
| `proofs/lem-routef-raw-factor-identities` | MATCH |

Finally, `report/UNWIRED.md:355` contains
`lem-routef-raw-factor-setting-formation` exactly.

## 5. Disposition

Apply findings 1--5 to both the landed files and the retained generator in a
separately authorized correction landing, then rerun this transcription
audit.  Until that happens, the mathematical registry interfaces are
faithfully landed, but the package as a whole is not byte-faithful to the
ratified source under the user's stated adaptation whitelist.

## RE-AUDIT (post-corrections)

Date: 2026-08-05
Role: fresh independent transcription re-auditor
Status: **NON-RIGOROUS TRANSCRIPTION AUDIT / NOTHING PROMOTED**

**Verdict: TRANSCRIPTION-CONFIRMED.**

**New findings: none.**

All five section-1 findings are corrected exactly as prescribed:

1. `definitions/def-routef-raw-factor-setting.md` now displays precisely
   `(\eta_A,C_A,C_E,\varepsilon_E).`, with no `W_{RF}=` assignment.
2. The same shard has `\rho_\theta:=\frac18`, not `\tfrac18`.
3. Its notes restore the exact curly-quoted sentence naming “UCP map”,
   “extended epsilon-C*-algebra”, and “extended delta-isomorphism”, with no
   appended wiki-link list.
4. The undeclared typed-witness-pattern sentence is absent.
5. `argument/lemmas/lem-routef-raw-factor-identities.md` ends the prescribed
   row-3 correction sentence immediately after
   ``rho_T <= rho_id^corr``; the parenthesized audit citation is absent.

The complete `HEAD~1..HEAD` diff contains eight paths.  The only primary
content changes are those five corrections in the definition and row-3
body, plus the matching retained-generator correction.  The remaining paths
are this prior audit file and deterministic report projections
(`report/generated/defs/*` and `report/generated/stats/*`).  No contract,
frontmatter, `defs:`, `deps:`, `af` root, `UNWIRED`, INDEX, or DAG content
changed.

I reran `python3 scripts/land-ledger-domains-rows.py`.  It reproduced all 17
argument shards without a delta.  In a clean clone at `HEAD`, the immediately
following `git status --porcelain` was empty.  The active orchestrator
worktree retained only its pre-existing `.frontier/log.jsonl` entry, and the
replay introduced no additional change there or anywhere else.

Finally, after applying exactly the declared presentation adaptations
(`\tag{1.n}` to `\qquad (1.n)`, `{\rm X}` to `{\mathrm{X}}`, and `\[...\]`
to `$$...$$`) and using the same whitespace-neutral Markdown comparison as
the first audit, the definition body is equal to design section 1.1.  No
additional textual adaptation is required.  The definition and argument
gates report zero errors, and the generated definition and statistics
projections pass their freshness checks.
