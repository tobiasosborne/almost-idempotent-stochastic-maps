# BRIEF — GAP-S1-POLAR-CONTRACT design job (de-risk, riskiest-first)

You are a fresh, independent, HOSTILE design mathematician. Your job is to
close (or refute the closability of) **GAP-S1-POLAR-CONTRACT**: the only
family of the Route-F decomposition whose mathematics currently exists ONLY
as prose. Finding a genuine mathematical gap is a BIG SUCCESS, equal in value
to producing the contracts. Do not be charitable to the prose.

## Context (read these, in this order)

1. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   — §2.4 (the three rows marked DESIGN-ONLY / BLOCKED ON GAP-S1-POLAR-CONTRACT:
   `lem-stage1-inversion-derivative-control`, `lem-stage1-quotient-manifold-package`,
   `lem-stage1-quotient-left-inversion`), §2.6 (the `gap-stage1-polar-chart-contract`
   reservation), §4.1 (proposed definition shards incl. the approximate-unitary-space
   datum), risk register rows R14, R35.
2. `docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-H-STAGE1.md` and
   `VERDICT-W74F-H-STAGE1.md` — the permitted Stage-1 prose and the hostile
   verdict that quarantined the polar content.
3. `refs/kitaev-2405.02434/approximate_algebras.tex` — the ground-truth source.
   The polar machinery is approximately lines 690–950: the set 𝒰 and 𝒰_δ
   (~line 697), `lem_invfun`, `lem_gV`, `prop_polar` (~line 809, the polar map
   (U,H) ↦ UH and its diffeomorphism property), the inverse pair u(·), h(·)
   (~line 845), and the chart/group-law/derivative estimates through ~line 950.
4. `definitions/INDEX.md` + the def shards it points to (esp.
   `def-epsilon-cstar-algebra`). NOTE: `def-approximate-unitary-space` does NOT
   exist yet — v4.1 §4.1 proposes it; your design may specify it as a datum-only
   definition (no theorem content smuggled into a definition — R35).

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR.md`

Produce, in the exact style of the v4.1 §2.4 proposal table:

1. **The minimal set of closed formula-level result contracts** replacing the
   `gap-stage1-polar-chart-contract` reservation. Expected content (adjust as
   the mathematics dictates, splitting or merging as needed):
   - polar retraction existence + C¹ regularity of u, h on an explicit
     neighborhood, with explicit universal constants and explicit domain
     guards (every radius/threshold a closed formula in ε_X, δ — NO guessed
     radii, NO O(·) left unexpanded in a contract);
   - the group-law (multiplication) error contract on the chart;
   - the first-derivative error contract;
   - anything else the three blocked consumer rows genuinely need
     (enumerate the consumers' needs explicitly and map each need to a
     contract).
   For each row: proposed id, kind/status, one-line `contract:` (self-contained,
   quantified, closed), defs (existing or proposed), deps (existing registry ids
   only, or other rows of your table), provenance loci (exact TeX line ranges /
   PROOF sections), projected af node count (≤12 nodes / depth ≤3 per row —
   factor rather than balloon).
2. **A per-row FEASIBILITY VERDICT**: does the cited prose + TeX actually
   support this contract at the stated strength? Categories: SUPPORTED /
   SUPPORTED-WITH-DERIVATION (state exactly what must be derived) /
   **GAP (genuine mathematical hole — describe it precisely; this is a
   success, not a failure)**.
3. **A dimension-freeness audit**: for every constant and radius in your
   contracts, state why it is independent of dim X, amplification level, block
   data, and stage index — or flag it if it is not. A dimension-dependent
   constant anywhere on this path is a ROUTE-LEVEL ALARM: say so loudly.
4. **Unblocking map**: which of the three DESIGN-ONLY consumer rows become
   transcribable with your ids, and any correction their v4.1 draft contracts
   need.
5. **Definition provisioning**: the exact datum-only definition shards needed
   (name, one-line content, provenance), consistent with v4.1 §4.1.

## Hard constraints

- DESIGN ONLY. Write ONLY inside `docs/plans/2026-07-26-S1-POLAR-design/`.
  Do NOT touch `definitions/`, `argument/`, `proofs/`, or any other path.
- No status promotion: every proposed row is at most `stated` /
  `proved-mod-audit` candidate; nothing you write is rigorous.
- v4.1 discipline: no compound contracts; one result per row; explicit local
  domains; constants may appear in contracts only when the source pins them
  (else name them and pin them in the proof-body plan).
- Cite loci exactly (file + line ranges). If a needed fact is NOT in the
  local sources listed above, say NOT IN LOCAL REFS and stop on that point —
  do not paraphrase literature from memory.
