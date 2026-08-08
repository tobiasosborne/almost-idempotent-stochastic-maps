VERDICT: LAND-WITH-EXACT-CORRECTIONS

1. **HIGH — the old string is byte-exact, but the proposed replacement does
   not yet give fully honest formulation/status scoping.**  A literal comparison
   of the addendum's old block at
   `ADDENDUM-EXHUME-SHARPNESS-V3.md:24-30` with the live
   `definitions/def-near-positive-projection.md:23-25` passes byte-for-byte.
   The replacement correctly removes the prose eponym, keeps the
   `cor-classical-sharpness` claim on the stochastic parameter `eta`, says that
   signed-`delta` sharpness has no rigorous carrier, and labels the literal
   `ex-hume` proposition `disproved`.  Two adjacent statements nevertheless
   prevent the advertised honest scope:

   - `ADDENDUM-EXHUME-SHARPNESS-V3.md:35-36` says the signed definition "is"
     `op-classical`, while the rigorous bridge actually establishes equivalence
     only up to universal constants
     (`argument/lemmas/lem-classical-equiv.md:4,7-8`).
   - The prescribed edit leaves
     `definitions/def-near-positive-projection.md:22` calling the stability
     statement an "open hypothesis parenting `op-classical`" and line 31 calling
     it "an open registry problem", despite `op-classical` now being
     `proved` / `af: validated` (`argument/lemmas/op-classical.md:8-9,15-23`).

   Apply these exact corrections within locus 51.  First replace

   ```text
   positive map. *Near-positive-projection stability* (the open hypothesis parenting `op-classical`) asks
   ```

   by

   ```text
   positive map. *Near-positive-projection stability* asks
   ```

   Replace the addendum's proposed new block at lines 35-41 by:

   ```text
   unital idempotent — a [[def-stochastic|stochastic idempotent]] $E$. The signed and
   stochastic-defect formulations are equivalent up to universal constants by
   `lem-classical-equiv` (af-validated), and the corresponding stochastic upper-bound theorem
   is `op-classical` (af-validated 2026-08-08). Sharpness of the $\sqrt{}$ exponent
   in the stochastic parameter $\eta$ is the registry row `cor-classical-sharpness`
   (see its shard for status); it is not a certificate for sharpness in the signed
   parameter $\delta$ used by THIS definition. No signed-$\delta$ sharpness claim is
   currently established at any rigorous rung: the historical $3\times3$ family record
   (`ex-hume`) is `disproved` as literally stated, and its corrected distance-to-set
   statement remains an unproved candidate.
   ```

   Finally replace the live line-31 sentence

   ```text
   The *stability* statement is an open registry problem, not part of this definition.
   ```

   by

   ```text
   The *stability* statement is not part of this definition; see [[lem-classical-equiv]],
   [[op-classical]], and [[cor-classical-sharpness]] for the separate formulations and their statuses.
   ```

   Locus 51 must land in Stage A atomically with creation of
   `argument/lemmas/cor-classical-sharpness.md`; that shard does not exist in the
   live repository yet, although v2 lines 701-704 already prescribe its creation.

2. **MEDIUM — the sign-off mechanism is sound in substance but misidentifies
   the shard and records the wrong audit.**  The live frontmatter says
   `kind: original`, not `consensus`
   (`definitions/def-near-positive-projection.md:5`), so
   `ADDENDUM-EXHUME-SHARPNESS-V3.md:15-16,52` must say
   ``locked`/`original``.  The field is still correctly named `consensus:` for
   either kind (`definitions/README.md:23-28,39-49`), and recorded user
   ratification is the repository's established delegated-sign-off mechanism
   (for example `definitions/def-routef-raw-factor-setting.md:10`).  But this is
   a substantive correction to mathematical/status prose, not "no ...
   mathematical content" as addendum lines 52-54 claim, and the fresh audit of
   the correction is V3, not the rejecting V2 audit alone.  Replace lines 52-58
   by the following exact mechanics:

   ```text
   Mechanics: this is a substantive status/scoping correction in the **Statement** of a
   `locked`/`original` definition shard; it does not change the defined object, term, or
   aliases. Per L2/Rule 7 it requires recorded sign-off. Ratification of the corrected
   package is that sign-off, to be appended to the shard's `consensus:` line as:
   `; sharpness/status remarks corrected 2026-08-08 (fresh hostile review:
   AUDIT-EXHUME-SHARPNESS-V3.md finding 1; user-ratified W139 package; defined object unchanged)`.
   ```

   This satisfies `definitions/README.md:42-49,60-61` and
   `CLAUDE.md:127-128`; no kind/status/frontmatter change is authorized.

3. **CLEARED — the replacement's substantive status assertions check out.**
   `op-classical` is `proved` / `af: validated` at
   `argument/lemmas/op-classical.md:8-9`, with the root validation event at
   `proofs/op-classical/ledger/000027.json:1`.  A sweep of every shard under
   `argument/lemmas/` finds no rigorous signed-`delta` stability-sharpness row:
   the only literal `delta^beta` carrier is `ex-hume`, presently
   `proved-mod-audit` / `af: seeded`
   (`argument/lemmas/ex-hume.md:4,7-8`) and destined by the ratified package for
   `disproved` / `af: none`; `lem-prh-sharpness` is explicitly PRH-only and
   non-rigorous (`argument/lemmas/lem-prh-sharpness.md:4,7-15,32-34`).  Other
   rigorous uses of the word "sharp" in `argument/` concern local constants or
   unrelated lemmas, not the signed-`delta` stability exponent.  The corrected
   distance-to-set formula remains only the non-rigorous candidate recorded at
   `paper/main.tex:291-317` and
   `docs/plans/2026-08-08-PAPER/AUDIT-PAPER.md:26-45`.

4. **CLEARED — the full survivor sweep exposes no 52nd source locus.**  The
   repeated search for `ex-hume`, `Hume`, `sharp`, and `sharpness` covered the
   locus classes required by the v2 audit: `AGENTS.md`, `CLAUDE.md`, the root
   current-state files, `refs/manifest/`, all of `argument/`, all of
   `definitions/`, `docs/ingest/`, `report/`, `paper/`, and `INDEX.md`.  The
   26 active report source shards are exactly those enumerated at
   `DESIGN-EXHUME-SHARPNESS-V2.md:600-625`.  Within `definitions/`, the only
   survivor is `def-near-positive-projection.md:24-25`; within
   `report/generated/`, its only active-assertion twin is
   `report/generated/defs/layer-1-classical-picture.tex:448-449`, which is
   regenerated from that source.  The other generated survivors in
   `report/generated/dag/` and `report/generated/stats/`, plus
   `report/UNWIRED.md:89`, are mechanical id/status records, not sharpness
   assertions, and are already covered by v2's regeneration/whitelist steps.
   All remaining active source assertions are among loci 1-50; historical
   plans, waves, ingest payload, run scripts, frontier/bead logs, and worklog
   material fall under v2's explicit historical disposition
   (`DESIGN-EXHUME-SHARPNESS-V2.md:631-634`).

5. **CLEARED — the addendum changes no audit-cleared v2 mathematics or
   elevation mechanics.**  Its operative delta is confined to the one
   definition shard, its generated definition twin, the manifest count
   50-to-51, and the required definition sign-off
   (`ADDENDUM-EXHUME-SHARPNESS-V3.md:8-10,22-69`).  It supplies no replacement
   for any v2 proof contract, af skeleton, budget, seeding package, staging
   rule, report action, or paper action.  Subject to findings 1-2 above,
   `DESIGN-EXHUME-SHARPNESS-V2.md` is otherwise carried forward verbatim.
