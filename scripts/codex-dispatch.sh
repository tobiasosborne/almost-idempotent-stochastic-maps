#!/bin/bash
# scripts/codex-dispatch.sh — quota-resilient dispatch wrapper.
#
# Generalizes the twice-proven scratchpad dispatcher (the pattern that ran on
# 2026-07-10 against the af orchestration: probe → if quota-limited, sleep
# until the parsed reset time (+2min) or a fixed retry-wait → probe again →
# once clean, exec the wrapped command). No hardcoded epochs: the reset time
# (if any) is parsed fresh out of each probe's own error text.
#
# USAGE
#   scripts/codex-dispatch.sh [--max-attempts N] [--retry-wait SECS] [--log FILE] -- <command...>
#
#   --max-attempts N   probe attempts before giving up (default 6)
#   --retry-wait SECS  fallback sleep between probes when no reset time can be
#                       parsed out of the quota error (default 600)
#   --log FILE         durable append-only log file (default .frontier/dispatch-log.txt)
#   --                 required separator; everything after it is the command to exec
#
# BEHAVIOUR
#   1. PROBE: a cheap 1-token codex call —
#        echo "Reply with OK" | codex exec --skip-git-repo-check -C /tmp \
#          -m gpt-5.6-sol -c 'model_reasoning_effort="low"' -s read-only -
#      If its output (stdout+stderr) contains "usage limit", we are
#      quota-limited.
#   2. On quota-limit: try to parse "try again at <time>" out of the probe
#      output. If found, sleep until that time + 2 minutes (via `date -d`).
#      If the string isn't present or unparseable, sleep --retry-wait seconds
#      instead. Then re-probe (up to --max-attempts total probe attempts).
#   3. Once a probe succeeds (no "usage limit" in its output), exec the
#      wrapped command (replaces this shell — exit status is the command's).
#   4. Every attempt (probe result, sleep decision, final exec) is appended
#      to the log file with a timestamp. The log is append-only; the script
#      never truncates it.
#
# EXAMPLES
#   scripts/codex-dispatch.sh -- python3 scripts/af-orchestrate.py <id> \
#     --workers 6 --max-rounds 14 --node-cap 40
#   scripts/codex-dispatch.sh --max-attempts 3 --retry-wait 120 -- echo done
#
# EXIT CODES
#   0            wrapped command ran and exited 0 (or whatever it exited —
#                its exit status is forwarded via exec)
#   3            gave up after --max-attempts quota-limited probes
#   2            usage error (bad args / missing --)

set -euo pipefail

MAX_ATTEMPTS=6
RETRY_WAIT=600
LOG_FILE=".frontier/dispatch-log.txt"
CMD=()

usage() {
  echo "usage: $0 [--max-attempts N] [--retry-wait SECS] [--log FILE] -- <command...>" >&2
  exit 2
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --max-attempts)
      [ "$#" -ge 2 ] || usage
      MAX_ATTEMPTS="$2"
      shift 2
      ;;
    --retry-wait)
      [ "$#" -ge 2 ] || usage
      RETRY_WAIT="$2"
      shift 2
      ;;
    --log)
      [ "$#" -ge 2 ] || usage
      LOG_FILE="$2"
      shift 2
      ;;
    --)
      shift
      CMD=("$@")
      break
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

if [ "${#CMD[@]}" -eq 0 ]; then
  echo "$0: no command given after --" >&2
  usage
fi

mkdir -p "$(dirname "$LOG_FILE")"

log() {
  printf '[%s] %s\n' "$(date -Iseconds)" "$1" >> "$LOG_FILE"
}

# probe_output: run the cheap quota probe and echo its combined output.
# Never lets a probe failure (codex exiting non-zero) kill this script under
# set -e, since a quota-limit response is itself a non-zero/loud exit.
probe_output() {
  echo "Reply with OK" | codex exec --skip-git-repo-check -C /tmp \
    -m gpt-5.6-sol -c 'model_reasoning_effort="low"' -s read-only - 2>&1 || true
}

# parse_reset_epoch OUTPUT: extract "try again at <time>" and print its epoch
# seconds (via `date -d`), or print nothing if not present/unparseable.
parse_reset_epoch() {
  local output="$1"
  local when
  when=$(printf '%s\n' "$output" | grep -oE 'try again at [^.]*' | head -n1 | sed -E 's/^try again at //') || true
  [ -n "$when" ] || return 0
  date -d "$when" +%s 2>/dev/null || true
}

attempt=1
while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do
  log "attempt $attempt: probing quota"
  out="$(probe_output)"
  if printf '%s\n' "$out" | grep -qi "usage limit"; then
    reset_epoch="$(parse_reset_epoch "$out")"
    if [ -n "$reset_epoch" ]; then
      now=$(date +%s)
      wait_until=$((reset_epoch + 120))
      sleep_secs=$((wait_until - now))
      if [ "$sleep_secs" -gt 0 ]; then
        log "attempt $attempt: quota-limited; reset parsed at epoch $reset_epoch; sleeping ${sleep_secs}s (until reset+2min)"
        sleep "$sleep_secs"
      else
        log "attempt $attempt: quota-limited; parsed reset $reset_epoch already passed; retrying immediately"
      fi
    else
      log "attempt $attempt: quota-limited; no reset time parsed; sleeping ${RETRY_WAIT}s (fallback)"
      sleep "$RETRY_WAIT"
    fi
    attempt=$((attempt + 1))
    continue
  fi
  log "attempt $attempt: probe OK; exec'ing wrapped command: ${CMD[*]}"
  exec "${CMD[@]}"
done

log "gave up after $MAX_ATTEMPTS quota-limited attempts"
exit 3
