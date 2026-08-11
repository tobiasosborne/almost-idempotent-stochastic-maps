#!/usr/bin/env python3
"""
check-site.py — freshness gate for the site data layer (Phase 1, slate J of
docs/plans/2026-08-11-communication-artifacts-plan.md; design principle P1).

The fourth generated layer (after report defs / dag / stats): site/data/*.json must equal a fresh
generation from the canonical record, so no site surface can publish a number the repo no longer
supports. Stale => non-zero exit => the commit is blocked (wired into scripts/check-all.sh).

Usage:
  python3 scripts/check-site.py --check    # exit 1 listing every drifted/missing file
  python3 scripts/check-site.py            # same (check is the only mode; refresh with
                                           #   python3 scripts/gen-site-data.py --generate)
"""
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _gen():
    spec = importlib.util.spec_from_file_location("gen_site_data",
                                                  ROOT / "scripts" / "gen-site-data.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv):
    return _gen().main(["--check"] if "--generate" not in argv else ["--generate"])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
