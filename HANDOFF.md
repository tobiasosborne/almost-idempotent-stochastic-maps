<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (now **v31** — *the Route F
   chain is FACTORED; phases 2–3 of the L0 campaign are unblocked*) +
   `docs/plans/CHANGELOG.md` (newest entry = v31). **STEWARDSHIP mandate binding
   (Rule 9).**
3. Read `docs/plans/2026-07-24-af-elevation-campaign.md` (campaign ground plan,
   epic **aism-xuvw**) and the fudw design/verdict lineage in
   `docs/plans/2026-07-24-fudw-decomposition-artifacts/` (v1/v2/v3 designs +
   hostile verdicts; the v3 verdict's registry-impact section is the authority
   for what was codified).
4. **The decomposition pass (aism-fudw) is DONE and CLOSED**: after a 3-round
   adversarial design loop (6 fresh codex workers), the v3 verdict's safe
   seed-first subset was codified — **33 registry shards** (COMP 8 / H-CB 14 /
   EXT 6 / Stage-1 2 / finish leaves 3; 28 `proved-mod-audit` + 5 `stated`, all
   `af: none`; registry **248**) + **12 `draft` defs**. Parents untouched. The
   MAIN-CB/ledger remainder + 5 GAP interfaces are QUARANTINED in **aism-0163**
   (blocks phase 4 only). `lem-routef-k-ledger` is under a DO-NOT-REWIRE-OR-SEED
   guard until reviewed F2/F3 contracts exist.
5. **User decisions RESOLVED (2026-07-24, recorded in-session):**
   (a) all 12 fudw defs RATIFIED and locked (byte-match criterion; delegated
   for consensus/original tiers); (b) F2/F3 bridge closed via prover wave —
   both contracts hostile-verified (VERDICT-F2F3-BRIDGE.md, VALID-WITH-
   CORRECTIONS) and registered as lem-routef-f2-positive-unital-compression /
   lem-routef-f3-retract-defect (proved-mod-audit).
6. **STANDING DIRECTIVES (user, binding):** (i) capacity on the open leaves;
   (ii) decomposition as objective function; (iii) FINDINGS dead routes absolute;
   (iv) mostly serial; verification fresh-codex-only; af per §6 (Claude
   orchestrates, never judges); (v) no progress theatre; (vi) codex capped at
   xhigh; (vii) Route F L0 closure is P0; (viii) RDSE/LDHR-48 PAUSED.
   Session-24 addition (user): sonnet subagents for queries; general work
   delegated to codex `gpt-5.6-sol` xhigh; Claude monitors.
7. `fr board` + `bd ready`; beads sync via **bash** `scripts/beads-sync.sh`.
8. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-25 checkpoint, session 24 — fudw done; phase 2 executing)

**Rigorous (af-validated, T0): 49** (mid-campaign checkpoint 2026-07-25: the whole
COMP tier (8+naturality) + HCB-0 + column-hilbert-squared (the corrected
false-display estimate, 50/50) + the variational identity + 2 factored
micro-lemmas are all af-validated). **Registry: 253.** **Definitions: 36, all
locked** (12 fudw defs user-ratified 2026-07-24; +def-theta draft->locked path
pending only if challenged). F2/F3 bridge lemmas REGISTERED (hostile-verified).
**CAMPAIGN PAUSED (2026-07-25): codex usage limit exhausted — resets Jul 29
2026 9:08 AM (or purchase credits at chatgpt.com/codex/settings/usage). USER
DECISION: buy credits to continue now, or resume Jul 29.** In-flight:
proofs/lem-hcb3-diagonal-upper-norm banked mid-run (5/13 validated, tree
intact, NOTHING consumed by the outage); resume with:
`python3 scripts/af-orchestrate.py lem-hcb3-diagonal-upper-norm --workers 3
--max-rounds 16 --node-cap 40 --tier routine --phase verify`.
Remaining phase-2 queue after it: hcb3-diagonal-lower-modulus ->
hcb3-diagonal-inverse -> hcb3-offdiagonal-inverse -> hcb4-canonical-gram ->
hcb4-canonical-inverse -> hcb4-canonical-closeness -> conj-hcb parent
(seeding pattern: registry deps first-class + the 7-def kit + full-contract
externals — see the process laws below). Process laws learned this campaign (BINDING for phase 2 cont.):
(i) every workspace gets the FULL validated-contract battery as full-text
externals at seeding + the complete def kit (theta layer, norm axioms,
nonvanishing, column-hilbert displays with the false 1dQ_ip_norm_ext excluded
LOUDLY); (ii) contract typing defects (unbound ambient, u_Q/wtQ) are amended
mechanically from the challenge text (verdict-driven precedent) then re-seeded;
(iii) 3rd stall on one cluster => factor micro-lemmas from the challenge text.

### What session 24 did (details: worklog + the artifacts dir)

- Launched the L0 campaign phase 1 (aism-fudw): 7 fresh codex dispatches total
  (design architect; hostile reviewer; repair architect; reviewer #2; repair
  architect #2; reviewer #3; transcription worker) — strictly one at a time.
- All three hostile reviews returned INVALID **on the design layer** (contract
  drift, unproduced constants, compound contracts); the underlying Route F
  mathematics was never faulted. v3's verdict endorsed a 77-row inventory and
  named the safe seed-first subset; ONLY that subset was transcribed.
- One network outage mid-review: codex auto-reconnected; nothing lost.
- Process precedent upheld: bank INVALID → narrowest repair → fresh re-review;
  after 3 rounds, harvest the verdict-blessed subset rather than loop to v4.

## Next steps (ranked)

0. **Surface the two user decisions** (START-HERE #5): def ratification (12
   drafts) + F2/F3 bridge contracts.
1. **Phase 2 (aism-niwk, unblocked): af-elevate the H-CB subtree.** Order:
   (a) provision the Ha/COL-HILB def layer as af-consumable defs (byte-matched
   `af def-add` from `refs/kitaev-2405.02434/approximate_algebras.tex` where the
   *definitions* are sound); (b) seed COMP leaves first
   (`scripts/seed-af-workspaces.py`, contract VERBATIM), bottom-up by deps
   (`python3 scripts/argument.py --show <id>` for the order); (c) one
   `af-orchestrate.py` at a time, backgrounded, **NO repo edits while live**
   (porcelain-wide guard); (d) banking flips after landing.
2. **Phase 3 (aism-fgr7, unblocked after H-CB)**: EXT-CB subtree, same loop.
3. **aism-0163 (blocks phase 4)**: focused repair of the quarantined MAIN/ledger
   rows per the v3 verdict's exact corrections + fresh hostile review; needs the
   F2/F3 decision. Also acquire the 7 Stage-1 external topology sources into
   `refs/` (provisioning risk flagged since the campaign plan).
4. Route X deciders (aism-ea2f) — unchanged fallback pricing.

## Standing rules (delta from session 23)

- The fudw loop hard-codified: a design is transcribed ONLY from a hostile
  verdict's registry-impact section (verdict text wins over design text); when a
  verdict names a safe subset, transcribe that subset and quarantine the rest in
  a bead — no v4 design loops on a converging lineage.
- Codification workers run at `high` (routine transcription); design/review at
  `xhigh` (architecture). All fresh, all single-use, roles never mix.

## What is intentionally NOT here

- Any claim op-classical is proved/rigorous. T0 is exactly **49** (each one a
  root-validated taint-clean af tree; everything else in the chain remains
  `proved-mod-audit`/`stated`).
- Any transcription of the quarantined rows or the 5 GAP interfaces (GAP-EA,
  GAP-S1-POLAR-CONTRACT, GAP-MAIN-STRUCTURE, GAP-LEDGER-DOMAINS, F2/F3).
- Any movement on RDSE/LDHR-48, the signed trunk, or numerical `K`/`η_K`.
- (12-def ratification RESOLVED 2026-07-24 — see START-HERE #5.)
