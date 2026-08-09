#!/usr/bin/env python3
"""Regression tests for the campaign-statistics extractor and renderer."""

import importlib.util
import json
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "gen_report_stats", ROOT / "scripts" / "gen-report-stats.py")
STATS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(STATS)


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class FrontierExtractionTests(unittest.TestCase):
    def test_normalizes_legacy_outcome_and_extracts_t0_events(self):
        with tempfile.TemporaryDirectory() as td:
            repo = pathlib.Path(td)
            records = [
                {"cycle": 1, "ts": "2026-08-08T10:00:00Z", "arm": None,
                 "outcome": "orient", "note": "no wave"},
                {"cycle": 2, "ts": "2026-08-08T11:00:00Z", "arm": "FH",
                 "outcome": "a legacy sentence rather than an outcome", "note": None},
                {"cycle": 3, "ts": "2026-08-08T12:00:00Z", "arm": "FH",
                 "outcome": "banked", "note": "ROOT DISCHARGED — op-classical "
                 "af-VALIDATED (T0 195 -> 196)",
                 "evidence": {"tier": "T0", "artifact": "proofs/op-classical/export.md"}},
                {"cycle": 4, "ts": "2026-08-09T06:00:00Z", "arm": "FH",
                 "outcome": "banked", "note": "family arithmetic T0 196 -> 197; xhigh; "
                 "24/24 nodes; cap 26", "evidence": {"tier": "T0", "artifact":
                 "proofs/lem-prh-sharpness-family-arithmetic/export.md"}},
            ]
            write(repo / ".frontier" / "log.jsonl",
                  "".join(json.dumps(r) + "\n" for r in records))

            got = STATS.extract_frontier(repo)

            self.assertEqual(got["outcomes"]["legacy-free-text"], 1)
            self.assertEqual(got["legacy_outcome_records"], 1)
            self.assertEqual(got["no_wave_turns"], 1)
            self.assertEqual(got["no_arm_records"], 1)
            self.assertEqual(got["t0_transitions"][-1]["after"], 197)
            self.assertEqual(got["op_classical_discharge"]["after"], 196)
            self.assertEqual(got["sharpness_xhigh_remedy"]["nodes"], 24)


class AfExtractionTests(unittest.TestCase):
    def test_counts_historical_roots_revalidations_and_first_pass(self):
        with tempfile.TemporaryDirectory() as td:
            repo = pathlib.Path(td)
            ledger = repo / "proofs" / "lem-a" / "ledger"
            events = [
                {"type": "proof_initialized", "timestamp": "2026-08-01T00:00:00Z"},
                {"type": "nodes_claimed", "timestamp": "2026-08-01T00:01:00Z",
                 "node_ids": ["1"], "owner": "prover-build"},
                {"type": "node_created", "timestamp": "2026-08-01T00:02:00Z", "node_id": "1"},
                {"type": "nodes_claimed", "timestamp": "2026-08-01T00:03:00Z",
                 "node_ids": ["1"], "owner": "v-1-r1"},
                {"type": "node_validated", "timestamp": "2026-08-01T00:04:00Z", "node_id": "1"},
                {"type": "node_unvalidated", "timestamp": "2026-08-01T00:05:00Z", "node_id": "1"},
                {"type": "node_validated", "timestamp": "2026-08-01T00:06:00Z", "node_id": "1"},
            ]
            for i, event in enumerate(events, 1):
                write(ledger / f"{i:06d}.json", json.dumps(event))

            got = STATS.extract_af(repo)

            self.assertEqual(got["ever_root_validated"], 1)
            self.assertEqual(got["root_validation_events"], 2)
            self.assertEqual(got["root_unvalidation_events"], 1)
            self.assertEqual(got["root_revalidation_events"], 1)
            self.assertEqual(got["first_pass_trees"], 1)


class FindingsExtractionTests(unittest.TestCase):
    def test_extracts_learning_drops_and_sharpness_balloon_sizes(self):
        with tempfile.TemporaryDirectory() as td:
            repo = pathlib.Path(td)
            write(repo / "FINDINGS.md", """
**DEAD-ROUTE**: [one](#one) · [two](#two)
## 2026-08-08 — sharpness-family elevation: THREE consecutive balloons
- monolith ballooned twice (27, 28 live vs cap 26), then sub-row (27 > 26).
""")
            write(repo / "docs" / "LEARNINGS.md", """
## 2026-07-28 — first retraction (T0 107 → 105)
## 2026-07-28 — second retraction (T0 105 -> 101)
## 2026-08-08 — `ex-hume`: false
""")

            got = STATS.extract_findings(repo)

            self.assertEqual(got["learning_entries"], 3)
            self.assertEqual(got["t0_removed_slots"], 6)
            self.assertEqual(got["sharpness_balloon_sizes"], [27, 28, 27])
            self.assertEqual(got["sharpness_balloons"], 3)


class ReportExtractionTests(unittest.TestCase):
    def test_reconstructs_pre_and_post_sync_t0_backlog_from_labels(self):
        with tempfile.TemporaryDirectory() as td:
            repo = pathlib.Path(td)
            for rid in ("lem-old", "lem-new", "lem-left"):
                write(repo / "argument" / "lemmas" / f"{rid}.md", """---
id: %s
status: proved
af: validated
provenance: internal
---
""" % rid)
            write(repo / "report" / "sections" / "10_old.tex", r"\label{lem:old}")
            write(repo / "report" / "sections" / "52_new.tex", r"\label{lem:new}")
            write(repo / ".frontier" / "log.jsonl", json.dumps({
                "cycle": 9, "note": "W140 report sync: shards 52-72; statistics layer T0 3/3"
            }) + "\n")

            got = STATS.extract_report(repo)

            self.assertEqual(got["current_t0"], 3)
            self.assertEqual(got["anchored_before_sync"], 1)
            self.assertEqual(got["anchored_after_sync"], 2)
            self.assertEqual(got["backlog_before_sync"], 2)
            self.assertEqual(got["backlog_after_sync"], 1)
            self.assertEqual(got["newly_anchored_by_sync"], 1)
            self.assertEqual(got["backlog_before_at_dispatch"], 2)
            self.assertEqual(got["backlog_after_at_dispatch"], 1)
            self.assertEqual(got["sync_shards_expected"], 21)
            self.assertEqual(got["sync_shards_present"], 1)


class RendererTests(unittest.TestCase):
    def test_headline_uses_current_registry_t0_not_historical_roots(self):
        data = {
            "extracted_at": "2026-08-09T00:00:00Z",
            "successor": {
                "frontier": {"max_cycle": 4},
                "af": {"root_validated": 199, "nodes_total": 10},
                "registry": {"results": 374, "af": {"validated": 197}},
                "git": {"first_day": "2026-08-08", "last_day": "2026-08-09"},
                "worklog": {"entries": 1}, "runs": {},
            },
            "progenitor": {"git": {}, "af": {"nodes_total": 0}},
        }

        rendered = STATS.render_headline(data)

        self.assertIn(r"{\large\bfseries 197}", rendered)
        self.assertNotIn(r"{\large\bfseries 199}", rendered)

    def test_ladder_ends_on_snapshot_day_not_synthetic_future_day(self):
        data = {
            "extracted_at": "2026-08-09T07:00:00Z",
            "successor": {
                "frontier": {"t0_daily": {"2026-08-08": 196, "2026-08-09": 198}},
                "af": {"validation_days": {}, "ever_root_validated": 201, "workspaces": 210,
                       "historical_not_current": 2},
                "registry": {"results": 374, "status": {"proved": 1},
                             "af": {"validated": 199}},
                "definitions": {},
            },
        }

        rendered = STATS.sec_ladder(data)

        self.assertIn("(68,199)", rendered)
        self.assertNotIn("(70,199)", rendered)


if __name__ == "__main__":
    unittest.main()
