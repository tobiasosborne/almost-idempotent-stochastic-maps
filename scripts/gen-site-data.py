#!/usr/bin/env python3
"""
gen-site-data.py — the SITE DATA LAYER generator (Phase 1, slate J of
docs/plans/2026-08-11-communication-artifacts-plan.md).

Design principle P1 ("truth from canon, enforced"): every number on every site surface is
GENERATED from the canonical repo record — the argument registry, the definitions DB, the af
ledgers, docs/LEARNINGS.md, runs/, refs/manifest, .frontier/log.jsonl — and re-checked by a
freshness gate wired into scripts/check-all.sh. A stale site fails the gate; there are NO
hand-entered counts anywhere in site/data/.

Outputs (site/data/, all deterministic: sort_keys, stable ordering, no timestamps, no SHAs):
  dag.json          the 374-shard knowledge DAG: nodes, dep+route edges, op-classical closures
  defense.json      the Swiss-Cheese layers (plan §2) with LIVE counts, per layer
  retractions.json  docs/LEARNINGS.md, parsed into dated retraction records
  runs.json         one record per runs/ bundle (headline finding verbatim from its README)
  definitions.json  the definitions DB (fields per check-defs.py) + body text
  frontier.json     the fr wave log + the derived T0-over-time series (campaign replay)
  stats.json        the headline counters, all recomputed

Usage:
  python3 scripts/gen-site-data.py --generate   # (re)write site/data/*.json
  python3 scripts/gen-site-data.py --check      # regenerate to a temp dir + diff (exit 1 on drift)

NOTHING here promotes a status: statuses are transcribed from the shards verbatim (CLAUDE.md L0).
"""
import json
import pathlib
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "site" / "data"
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))
import site_sources as S  # noqa: E402

FILES = ("dag.json", "defense.json", "definitions.json", "frontier.json",
         "retractions.json", "runs.json", "stats.json")
# The af event types the Defense page reports explicitly (absent type => 0, never omitted, so a
# vanished event class is visible rather than silently missing).
AF_EVENT_TYPES = ("challenge_raised", "challenge_resolved", "node_validated", "node_amended",
                  "node_created", "proof_initialized", "qed", "node_unvalidated", "def_added")


def _counts(values):
    out = {}
    for v in values:
        out[v] = out.get(v, 0) + 1
    return out


# ---------- dag.json ----------

def build_dag(lemmas, argument):
    """Nodes + edges + the op-classical closures. Edge kinds: `dep` (unconditional) and `route`
    (a member of one OR-route, tagged with its 1-based route index) — the same edge set the
    linker uses for acyclicity/closures (argument.py all_dep_ids)."""
    ids = {l["id"] for l in lemmas}
    nodes, edges = [], []
    for l in sorted(lemmas, key=lambda d: d["id"]):
        nodes.append({
            "id": l["id"], "kind": l.get("kind", ""), "status": l.get("status", ""),
            "af": l.get("af", "none"), "owner": l.get("owner", ""),
            "contract": l.get("contract", ""),
            "defs": list(l.get("defs", [])), "deps": list(l.get("deps", [])),
            "routes": [list(r) for r in l.get("routes", [])],
            "workspace": l.get("workspace", ""),
            "proof_class": argument.proof_class(l),
            "available": argument._available(l),
        })
        for d in l.get("deps", []):
            edges.append({"from": d, "to": l["id"], "kind": "dep", "route": None})
        for i, r in enumerate(l.get("routes", []), 1):
            for m in sorted(r):
                edges.append({"from": m, "to": l["id"], "kind": "route", "route": i})
    edges.sort(key=lambda e: (e["to"], e["kind"], e["from"], e["route"] or 0))

    by = {l["id"]: l for l in lemmas}
    root = "op-classical"
    closure = {}
    if root in by:
        union = sorted(argument.deps_closure(lemmas, root) or [])
        routes = []
        for idx, members, clo in argument.route_closures(lemmas, root):
            clo = sorted(clo)
            routes.append({
                "route": idx, "members": list(members), "ancestors": clo, "size": len(clo),
                "all_available": all(argument._available(by[a]) for a in clo if a in by),
                "af_validated": sum(1 for a in clo
                                    if by.get(a, {}).get("af", "none") == "validated"),
            })
        validated = sorted(a for a in union
                           if a in by and argument._available(by[a]))
        closure = {"root": root,
                   "root_status": by[root].get("status", ""),
                   "root_af": by[root].get("af", "none"),
                   "union_ancestors": union,
                   "union_size": len(union),
                   "validated_ancestors": validated,
                   "validated_size": len(validated),
                   "routes": routes}

    dep_edges = sum(1 for e in edges if e["kind"] == "dep")
    route_edges = len(edges) - dep_edges
    n_routes = sum(len(l.get("routes", [])) for l in lemmas)
    return {
        "nodes": nodes,
        "edges": edges,
        "op_classical_closure": closure,
        "summary": {
            "total": len(lemmas),
            "by_status": _counts(l.get("status", "") for l in lemmas),
            "by_af": _counts(l.get("af", "none") for l in lemmas),
            "by_kind": _counts(l.get("kind", "") for l in lemmas),
            "by_proof_class": _counts(argument.proof_class(l) for l in lemmas),
            "dep_edges": dep_edges,
            "route_edges": route_edges,
            "routes": n_routes,
            # argument/DAG.md renders one extra dashed OR edge per route (junction -> shard);
            # this is that header's edge count, so the site and DAG.md never disagree.
            "edges_rendered": dep_edges + route_edges + n_routes,
            "dangling_deps": sorted({d for l in lemmas for d in argument.all_dep_ids(l)
                                     if d not in ids}),
        },
    }


# ---------- defense.json ----------

def build_defense(dag, defs, ev, ws, ext, refs, retr, runs, fr_entries, balloon_aborts):
    """The six Swiss-Cheese layers of the plan's §2 table + the retraction backstop, each with
    LIVE metrics. Prose fields carry NO numbers (P1: numbers live only in `metrics`)."""
    s = dag["summary"]
    af = {t: ev["counts"].get(t, 0) for t in AF_EVENT_TYPES}
    nonrigorous = {"stated", "proved-mod-audit", "conjecture", "heuristic", "numerical"}
    layers = [
        {"id": "L1", "name": "vocabulary & provenance",
         "error_class": "hallucinated citations; definition drift",
         "known_holes": "says nothing about proof correctness",
         "metrics": {"definition_shards": len(defs),
                     "definitions_locked": sum(1 for d in defs if d["status"] == "locked"),
                     "definitions_cited": sum(1 for d in defs if d["kind"] == "cited"),
                     "refs_sources": len(refs["sources"]),
                     "refs_pinned_files": refs["pinned_files"],
                     "externals_total": ext["total"],
                     "externals_byte_matched_quotes": ext["byte_matched_quotes"],
                     "externals_workspace_imports": ext["workspace_imports"],
                     "externals_without_quote": ext["no_quote"],
                     "externals_failed": ext["failed"]}},
        {"id": "L2", "name": "contract DAG + linker",
         "error_class": "contract mismatch; circularity; rigour resting on non-rigour",
         "known_holes": "cannot read proof bodies",
         "metrics": {"contracts": s["total"], "dep_edges": s["dep_edges"],
                     "route_edges": s["route_edges"], "edges_rendered": s["edges_rendered"],
                     "or_routed_shards": sum(1 for n in dag["nodes"] if n["routes"]),
                     "af_validated": s["by_af"].get("validated", 0),
                     "af_seeded": s["by_af"].get("seeded", 0)}},
        {"id": "L3", "name": "hostile review (reviewer != author)",
         "error_class": "plausible-but-wrong paper proofs",
         "known_holes": "batched review misses corners (documented: the empty-N corner)",
         "metrics": {"status_proved": s["by_status"].get("proved", 0),
                     "proved_not_af_validated": sum(
                         1 for n in dag["nodes"]
                         if n["status"] == "proved" and n["af"] != "validated"),
                     "nonrigorous_rows": sum(1 for n in dag["nodes"]
                                             if n["status"] in nonrigorous),
                     "retractions_caught_here": retr["by_layer"].get("L3", 0)}},
        {"id": "L4", "name": "af adversarial trees",
         "error_class": "in-proof gaps; silent assumptions; unregistered premises",
         "known_holes": "a cohort can accept an inference class a differently-framed cohort rejects",
         "metrics": {"workspaces": ws["total"], "workspaces_exported": ws["exported"],
                     "ledger_files": ev["files"], "ledger_unparseable": ev["unparseable"],
                     **af,
                     "validations_per_challenge_x100": (
                         round(100 * af["node_validated"] / af["challenge_raised"])
                         if af["challenge_raised"] else 0),
                     "retractions_caught_here": retr["by_layer"].get("L4", 0)}},
        {"id": "L5", "name": "meta-audit sweeps",
         "error_class": "the af cohorts' own blind spots",
         "known_holes": "runs only when a design round triggers re-audit",
         "metrics": {"retractions_caught_here": retr["by_layer"].get("L5", 0),
                     "af_node_unvalidated_events": af["node_unvalidated"],
                     "af_node_amended_events": af["node_amended"]}},
        {"id": "L6", "name": "oracles, numerics, tripwires",
         "error_class": "wishful conjectures; ballooning proofs",
         "known_holes": "refutes but cannot certify",
         "metrics": {"disproved_results": s["by_status"].get("disproved", 0),
                     "obstruction_results": s["by_status"].get("obstruction", 0),
                     "balloon_tripwire_aborts": balloon_aborts,
                     "run_bundles": len(runs),
                     "numerical_status_rows": s["by_status"].get("numerical", 0),
                     "retractions_caught_here": retr["by_layer"].get("L6", 0)}},
    ]
    return {
        "layers": layers,
        "backstop": {"id": "ledger", "name": "retraction ledger",
                     "error_class": "errors that survived the layers above",
                     "known_holes": "-",
                     "metrics": {"dated_entries": retr["total"],
                                 "entries_with_catching_layer_named": retr["classified"],
                                 "by_catching_layer": retr["by_layer"]}},
        "notes": {
            "catch_layer_classification": ("per-retraction `caught_by` layer tags are a KEYWORD "
                                           "heuristic over the raw markdown of docs/LEARNINGS.md, "
                                           "not a curated field — see retractions.json for the "
                                           "verbatim text"),
            "frontier_entries": len(fr_entries),
            "provenance": ("generated by scripts/gen-site-data.py from the canonical record; "
                           "gated by scripts/check-site.py --check inside scripts/check-all.sh"),
        },
    }


# ---------- retractions.json ----------

_LAYER_KEYS = (("L5", ("sweep", "meta-audit", "design-audit", "design round", "re-audit",
                       "audit chain")),
               ("L4", ("af verifier", "af elevation", "fresh per-node", "af validation",
                       "challenge", "stuck tripwire", "orchestrator's stuck")),
               ("L3", ("reviewer", "review", "hostile", "verdict", "opus worker", "wave")),
               ("L6", ("oracle", "refuter", "counterexample", "numerical", "balloon", "enumeration")),
               ("L2", ("linker", "contract bar", "contract-match", "propagation")),
               ("L1", ("byte-match", "verbatim", "provenance", "refs/")))


def _catch_layer(caught_by):
    """Heuristic tag of WHICH Swiss-Cheese layer caught a retraction, from its `Caught by:` text.
    Most-specific first; returns '' when no keyword fires (the site then shows the raw text)."""
    t = (caught_by or "").lower()
    for layer, keys in _LAYER_KEYS:
        if any(k in t for k in keys):
            return layer
    return ""


def build_retractions(entries):
    recs = []
    for e in entries:
        recs.append({"date": e["date"], "qualifier": e["qualifier"], "title": e["title"],
                     "claimed": e["claimed"], "why_wrong": e["why_wrong"],
                     "caught_by": e["caught_by"], "resolution": e["resolution"],
                     "extra": e["extra"], "catch_layer": _catch_layer(e["caught_by"])})
    by_layer = _counts(r["catch_layer"] for r in recs if r["catch_layer"])
    return ({"entries": recs, "total": len(recs),
             "by_catching_layer": by_layer,
             "note": ("dated entries of docs/LEARNINGS.md (the HTML-comment TEMPLATE is excluded); "
                      "`catch_layer` is a keyword heuristic over `caught_by`")},
            {"total": len(recs), "by_layer": by_layer,
             "classified": sum(1 for r in recs if r["catch_layer"])})


# ---------- driver ----------

def build_all(root=ROOT):
    lemmas, reg_errors, argument = S.registry(root)
    defs = S.definitions(root)
    counts, files, bad = S.ledger_events(root)
    ws = S.workspaces(root)
    ext = S.externals(root)
    refs = S.refs_manifest(root)
    runs = S.run_bundles(root)
    fr_entries, t0 = S.frontier(root)
    retr_json, retr_summary = build_retractions(S.learnings(root))
    dag = build_dag(lemmas, argument)
    log = (pathlib.Path(root) / ".frontier" / "log.jsonl")
    balloon = (log.read_text(encoding="utf-8").count("ABORTED [BALLOON]") if log.is_file() else 0)
    ev = {"counts": counts, "files": files, "unparseable": bad}
    defense = build_defense(dag, defs, ev, ws, ext, refs, retr_summary, runs,
                            fr_entries, balloon)
    stats = {
        "registry_total": dag["summary"]["total"],
        "t0_validated": dag["summary"]["by_af"].get("validated", 0),
        "edges": dag["summary"]["edges_rendered"],
        "definitions": len(defs),
        "run_bundles": len(runs),
        "retractions": retr_summary["total"],
        "workspaces_validated": ws["exported"],
        "frontier_entries": len(fr_entries),
    }
    if reg_errors:
        stats["registry_parse_errors"] = reg_errors
    return {
        "dag.json": dag,
        "defense.json": defense,
        "definitions.json": {"definitions": defs, "total": len(defs)},
        "frontier.json": {"entries": fr_entries, "total": len(fr_entries),
                          "t0_timeline": t0,
                          "note": ("T0 points are parsed out of free-text wave notes (liberal "
                                   "match on the last T0 count mentioned); dips are real — "
                                   "de-banked/retracted validations")},
        "retractions.json": retr_json,
        "runs.json": {"bundles": runs, "total": len(runs),
                      "note": "L3 numerical evidence only — never rigorous (CLAUDE.md L0/L3)"},
        "stats.json": stats,
    }


def render(obj):
    return json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n"


def write_all(payload, out_dir):
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        (out_dir / name).write_text(render(payload[name]), encoding="utf-8")


def check(root=ROOT, out_dir=OUT_DIR):
    """Regenerate into a temp dir and byte-diff against the committed site/data/."""
    payload = build_all(root)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="site-data-check-"))
    try:
        write_all(payload, tmp)
        drift = []
        for name in FILES:
            have = pathlib.Path(out_dir) / name
            fresh = (tmp / name).read_text(encoding="utf-8")
            if not have.is_file():
                drift.append(f"site/data/{name}: MISSING")
            elif have.read_text(encoding="utf-8") != fresh:
                drift.append(f"site/data/{name}: STALE (differs from a fresh generation)")
        extra = sorted(p.name for p in pathlib.Path(out_dir).glob("*.json")
                       if p.name not in FILES) if pathlib.Path(out_dir).is_dir() else []
        for name in extra:
            drift.append(f"site/data/{name}: UNKNOWN file (not produced by gen-site-data.py)")
        return drift
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv):
    args = set(argv) or {"--check"}
    if "--generate" in args:
        payload = build_all()
        write_all(payload, OUT_DIR)
        print(f"wrote site/data/ ({len(FILES)} files: {', '.join(FILES)})")
        return 0
    drift = check()
    for d in drift:
        print(f"ERROR {d}")
    if drift:
        print("check-site: FAILED — run `python3 scripts/gen-site-data.py --generate` "
              "(the site data layer is out of sync with the canonical record)")
        return 1
    print(f"check-site: OK ({len(FILES)} data files fresh)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
