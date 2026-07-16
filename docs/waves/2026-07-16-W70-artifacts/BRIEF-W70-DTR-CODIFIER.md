# W70 codifier — transcribe the verified DTR/POTI batch into registry shards

You are a fresh transcription codifier. You are NOT a prover and NOT a
verifier: you transcribe already-verified content into registry shard files
with byte-level fidelity to the sources. You add no mathematics, you repair
no proofs, you promote nothing beyond what the verdict file authorizes.

Workspace: this directory — registry snapshot (argument/, definitions/),
context docs (context/), DTR-ATTACK.md, APPENDIX-dtr-proofs.md, and the
governing verdict VERDICT-dtr-batch.md.

AUTHORITY ORDER (highest first): VERDICT-dtr-batch.md (any
VALID-WITH-CORRECTION must be transcribed in its CORRECTED form, with the
correction named in the provenance line) > APPENDIX-dtr-proofs.md (the
proofs and their shard-consumption lists) > DTR-ATTACK.md (the original
statements). A node whose verdict line is INVALID or UNDECIDED is NOT
codified as proved — stop and record it in INSTALL-NOTES.md instead.

DELIVERABLES — write EXACTLY these files into a new subdirectory codified/
(create it), plus codified/INSTALL-NOTES.md:

1. codified/conj-dtr-zero-oriented-surplus-exclusion.md
   (kind: lemma, status: conjecture, af: none, owner: B, deps: EMPTY)
   Contract = DTR-ATTACK.md §1.5 (ZOS.0 => the exact (EC) inequality),
   fully inline (see INLINING below).
2. codified/conj-dtr-positive-oriented-surplus-gap-exclusion.md
   (kind: lemma, status: conjecture, af: none, owner: B, deps: EMPTY)
   Contract = DTR-ATTACK.md §1.6 (POG.0 => (EC)), fully inline; the strict
   lower boundary G_phi = 0 belongs to the zero-surplus conjecture and
   equality at the upper boundary belongs to the routine close — state the
   window exactly as (POG.0) does.
3. codified/lem-dtr-canonical-overlap.md
   (kind: lemma, status: proved, af: none, owner: B)
   Contract = the COV contract as proved in APPENDIX-dtr-proofs.md §1
   (with any verdict correction), fully inline.
4. codified/lem-dtr-oriented-tail-ray-conversion.md
   (kind: lemma, status: proved, af: none, owner: B)
   Contract = the POTI-R contract as proved in APPENDIX-dtr-proofs.md §2:
   S*Z_v(q_A) >= G_phi on every pinned DTR datum, fully inline.
5. codified/lem-dtr-tail-coherent-conversion.md
   (kind: lemma, status: proved, af: none, owner: B)
   Contract = the TC contract as proved in APPENDIX-dtr-proofs.md §3
   ((1.16)-(1.18) => the strict gamma_coh*tau lower bound), fully inline;
   the optional exact upgrade (1.21)-(1.22) goes in the BODY, not the
   contract.
6. codified/lem-dtr-poti-assembly.md
   (kind: lemma, status: proved, af: none, owner: B)
   Contract = the ASM minimal conditional contract of APPENDIX-dtr-proofs.md
   §4: "Assume conj-dtr-zero-oriented-surplus-exclusion ... and
   conj-dtr-positive-oriented-surplus-gap-exclusion ... hold. Then every
   pinned DTR datum satisfies Z_v(q_A) >= (1/8)*P_v^+(E_*) -
   (c_m/16)*P_v^+(L_v)." — single conclusion; the strict
   (7*c_m/960)*tau close via B4.2-then-B4.1 and the weakened variant (2.5)
   go in the BODY as displayed consequences, not in the contract. Model the
   conditional phrasing on argument/lem-huddle-charge-assembly.md.

FRONTMATTER SCHEMA (copy the field set and style EXACTLY from the models):
- proved-lemma model: argument/lem-aesc-common-tail-union.md
- conjecture-registration model: argument/conj-l5-gap-1.md
  (NOTE its body: "This is a registration only; no proof is claimed" — both
  conj-dtr-* shards must carry the analogous body line, and must record in
  the BODY ONLY that lem-dtr-poti-assembly consumes them and that they are
  the two creative residuals of the W69 POTI reduction of DTR
  = conj-w67-aesc-diffuse-tail-ray-conversion. Reduction-tree relations are
  BODY text, never deps.)
- conditional-lemma model: argument/lem-huddle-charge-assembly.md
  (conjecture premises appear BOTH in the contract's "Assume ..." clause
  AND in deps — this is the W68-ratified pattern.)

INLINING (the hard transcription constraint): registry contracts are FULLY
INLINE — no reference to wave docs, no "the pinned DTR datum" by name, no
symbol left undefined. The canonical inline text for the shared A-esc/D-cap
datum ALREADY EXISTS in the registry: reuse the contract text of
argument/lem-aesc-common-tail-union.md verbatim up through the definition of
D_tail, then extend it with, exactly as APPENDIX-dtr-proofs.md §0 pins them:
the carrier set B subset D_tail with eta_D*(B) > 1/160 and Tail_1(u) > tau/8
for every u in B and min_f ||p_f - x_u||_1 > 3*delta(P) and h_u <= 3*delta(P)
(state x_u explicitly), the union floor P_f*^+(U_B) > tau/2560 if and only
if the appendix's pinned datum actually carries it, and the new objects:
m_A(Q) = sum_{j in A cap Q} max(P_vj, 0) with S = m_A(1) (say explicitly it
is the ORIGINAL top-selected measure, not a normalized variant), the
barycenter q_A = S^(-1) * sum_Q m_A(Q)*p_Q, rho(Q) = min{m_A(Q),
eta_D*(B cap Q)}, z(p) = H - phi(p) with D_0 = 2 + 4*delta(P), T_u = {R :
|chi_u(p_R)| > 1}, t_phi(u) = sum_{R in T_u} max(c_u,R, 0)*z(p_R), G_phi =
sum_{u in B} rho(u)*max(t_phi(u) - D_0*delta(P), 0), Z_v(q_A) (inline its
definition the way the appendix and the consumed lem-l5-* shards state it),
E_* and L_v (inline exactly as the appendix pins them from the B4 packet),
and for TC additionally C_{alpha,lambda}, r_{alpha,lambda}, delta_coh, and
gamma_coh per (1.16)-(1.18). Every symbol in a contract must be defined
inside that same contract. Where the appendix and DTR-ATTACK.md differ in a
display, the appendix (as corrected by the verdict) wins.

FIELDS:
- defs: choose from the def-* ids actually used by the model shards
  (lem-aesc-*, lem-dcap-*, conj-l5-gap-1); do not invent new def ids.
- deps (unconditional proof imports ONLY — the W68 ruling): transcribe from
  each proof's "Registry shards consumed" list in APPENDIX-dtr-proofs.md;
  for lem-dtr-poti-assembly additionally the two conj-dtr-* ids and
  lem-dtr-canonical-overlap + lem-dtr-oriented-tail-ray-conversion (+
  lem-dtr-tail-coherent-conversion only if the body's weakened display is
  claimed there — it is: include it). conj-dtr-* shards have EMPTY deps.
- status: proved for 3-6; conjecture for 1-2. af: none everywhere.
- provenance, one line, modeled on lem-aesc-common-tail-union.md:
  "W70 wave (docs/waves/2026-07-16-W70-artifacts/): codex strategist
  (gpt-5.6-sol, xhigh) DTR-ATTACK-W69.md §<n> (banked
  docs/waves/2026-07-14-W69-artifacts/); fresh routine prover (gpt-5.6-sol,
  high) APPENDIX-W70-dtr-proofs.md §<n>; fresh hostile batched codex
  verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W70-DTR-BATCH.md line
  <node>: <verdict>. Reviewer != author." — with the correction named
  inside the parenthetical if the line is VALID-WITH-CORRECTION. For the
  two conjecture registrations, provenance cites DTR-ATTACK-W69.md
  §1.5/§1.6 and the verdict's ASM line (they are registered as the named
  hypotheses of the verified conditional assembly).
- owner: B.

BODY (each shard, after the frontmatter, <= ~40 lines, modeled on the
models): **Role** (one line: which W69/W70 node this is), **Mechanism (one
line)**, **Honest scope** (for the proved lemmas: what is NOT claimed — no
leaf exclusion, POTI-0/POTI+ open, the conditional assembly's conclusion
not consumable unconditionally; for TC: the exact loss r_0*alpha*lambda/(16S)
and that coherence is an added hypothesis strictly weaker than
actorization; for the conjectures: registration only + refuter shape from
DTR-ATTACK.md §4.2), **Rigour tier** (L5 fresh hostile batched codex
verdict, W70; NOT af-validated — except the conj-* shards, which carry
"conjecture; registration only"). Use [[...]] links for related ids
(conj-w67-aesc-diffuse-tail-ray-conversion may appear as a body link even
though unregistered — the lem-aesc-* shards already do this).

INSTALL-NOTES.md must record: the verdict line per node; every correction
applied and where; the defs/deps chosen per shard and the exact appendix
line ranges transcribed; any judgment call you had to make (there should be
few — flag each loudly).

Do NOT touch argument/, definitions/, DTR-ATTACK.md, APPENDIX-dtr-proofs.md,
or VERDICT-dtr-batch.md. Write ONLY under codified/.
