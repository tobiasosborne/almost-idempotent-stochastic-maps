#!/bin/bash
# scripts/build-workspace.sh — reproducible worker-workspace assembly.
#
# Assembles a self-contained snapshot of the current registry + context docs
# into a fresh out-dir, so a codex/af worker (or a human) doesn't have to
# rebuild it by hand each time (the recorded W56 rebuild-cost incident).
#
# USAGE
#   scripts/build-workspace.sh <out-dir> [--waves w1.md,w2.md,...] [--plans p1.md,p2.md,...]
#
#   <out-dir>   target directory; MUST NOT already exist and be non-empty
#               (refuses to run — no silent clobber). May not yet exist at all,
#               or may exist and be empty.
#   --waves     comma-separated list of docs/waves/<filename> to also copy
#               into <out-dir>/context/
#   --plans     comma-separated list of docs/plans/<filename> to also copy
#               into <out-dir>/context/
#
# LAYOUT PRODUCED
#   <out-dir>/argument/     <- copy of ALL argument/lemmas/*.md
#   <out-dir>/definitions/  <- copy of ALL definitions/*.md
#   <out-dir>/context/      <- CONVENTIONS.md, FINDINGS.md, + any named
#                              --waves / --plans docs
#
# OUTPUT
#   One-line manifest summary of file counts per subdirectory, e.g.:
#     [build-workspace] manifest: argument=151 definitions=11 context=4 -> <out-dir>
#
# EXIT CODES
#   0  workspace assembled
#   2  usage error
#   3  out-dir exists and is non-empty (refused — no silent clobber)
#   4  a named --waves/--plans file was not found under docs/waves or docs/plans

set -euo pipefail

usage() {
  echo "usage: $0 <out-dir> [--waves w1.md,w2.md,...] [--plans p1.md,p2.md,...]" >&2
  exit 2
}

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

[ "$#" -ge 1 ] || usage
OUT_DIR="$1"
shift

WAVES=""
PLANS=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --waves)
      [ "$#" -ge 2 ] || usage
      WAVES="$2"
      shift 2
      ;;
    --plans)
      [ "$#" -ge 2 ] || usage
      PLANS="$2"
      shift 2
      ;;
    -h|--help)
      usage
      ;;
    *)
      echo "$0: unrecognized argument: $1" >&2
      usage
      ;;
  esac
done

# Refuse to clobber: out-dir may be absent, or present-and-empty; anything
# else (present and non-empty) is a hard stop.
if [ -e "$OUT_DIR" ]; then
  if [ ! -d "$OUT_DIR" ]; then
    echo "$0: $OUT_DIR exists and is not a directory" >&2
    exit 3
  fi
  if [ -n "$(ls -A "$OUT_DIR" 2>/dev/null)" ]; then
    echo "$0: refusing to run — $OUT_DIR exists and is non-empty" >&2
    exit 3
  fi
fi

mkdir -p "$OUT_DIR/argument" "$OUT_DIR/definitions" "$OUT_DIR/context"

cp -f "$REPO_ROOT"/argument/lemmas/*.md "$OUT_DIR/argument/"
cp -f "$REPO_ROOT"/definitions/*.md "$OUT_DIR/definitions/"
cp -f "$REPO_ROOT/CONVENTIONS.md" "$REPO_ROOT/FINDINGS.md" "$OUT_DIR/context/"

copy_named() {
  local list="$1" subdir="$2"
  [ -n "$list" ] || return 0
  local old_ifs="$IFS"
  IFS=','
  local name
  for name in $list; do
    IFS="$old_ifs"
    [ -n "$name" ] || continue
    local src="$REPO_ROOT/docs/$subdir/$name"
    if [ ! -f "$src" ]; then
      echo "$0: named file not found: docs/$subdir/$name" >&2
      exit 4
    fi
    cp -f "$src" "$OUT_DIR/context/"
    IFS=','
  done
  IFS="$old_ifs"
}

copy_named "$WAVES" "waves"
copy_named "$PLANS" "plans"

n_argument=$(find "$OUT_DIR/argument" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
n_definitions=$(find "$OUT_DIR/definitions" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
n_context=$(find "$OUT_DIR/context" -maxdepth 1 -type f | wc -l | tr -d ' ')

echo "[build-workspace] manifest: argument=$n_argument definitions=$n_definitions context=$n_context -> $OUT_DIR"
