/* lexicon.js — the canonical definition shards from site/data/definitions.json.
   Search is over term + aliases + id (as typed, case-insensitive); the body is shown as the shard's
   own source text, escaped, with `backticked` spans as <code>. No count on this page is a literal. */
(function () {
  "use strict";
  var S = window.S;

  var DEFS_URL = "https://github.com/tobiasosborne/almost-idempotent-stochastic-maps/blob/master/definitions/";

  var State = { all: [], view: [] };

  /* provenance kind -> palette class. `cited` is the only ground-truth rung here (byte-matched to a
     local published source); consensus/original are project-side and say so. */
  function kindClass(k) { return k === "cited" ? "t0" : k === "consensus" ? "audit" : "num"; }
  function statusClass(s) { return s === "locked" ? "t0" : "conj"; }

  function haystack(d) {
    return ((d.term || "") + " " + (d.id || "") + " " + ((d.aliases || []).join(" "))).toLowerCase();
  }

  function chips(data) {
    var defs = data.definitions || [];
    var byKind = {}, byStatus = {};
    defs.forEach(function (d) {
      byKind[d.kind] = (byKind[d.kind] || 0) + 1;
      byStatus[d.status] = (byStatus[d.status] || 0) + 1;
    });
    var out = [S.chip("audit", "definition shards: " + S.num(data.total))];
    Object.keys(byKind).sort().forEach(function (k) {
      out.push(S.chip(kindClass(k), k + ": " + byKind[k]));
    });
    Object.keys(byStatus).sort().forEach(function (k) {
      out.push(S.chip(statusClass(k), k + ": " + byStatus[k]));
    });
    document.getElementById("lex-chips").innerHTML = out.join("");
    return { byKind: byKind, byStatus: byStatus };
  }

  function options(sel, counts, allLabel) {
    var keys = Object.keys(counts).sort();
    document.getElementById(sel).innerHTML =
      '<option value="">' + allLabel + "</option>" +
      keys.map(function (k) {
        return '<option value="' + S.esc(k) + '">' + S.esc(k) + " (" + counts[k] + ")</option>";
      }).join("");
  }

  function card(d) {
    var aliases = (d.aliases || []).filter(function (a) { return a && a !== d.term; });
    return '<div class="card defcard">' +
      '<div class="chips" style="margin-bottom:.4rem">' +
        S.chip(kindClass(d.kind), "provenance: " + (d.kind || "?")) +
        S.chip(statusClass(d.status), "status: " + (d.status || "?")) +
        S.chip("num", "source: " + (d.source || "internal")) +
      "</div>" +
      "<h3>" + S.esc(d.term || d.id) + "</h3>" +
      '<p class="did"><a href="' + DEFS_URL + S.esc(d.id) + '.md">' + S.esc(d.id) + ".md</a></p>" +
      (aliases.length
        ? '<p class="small" style="margin:.3rem 0 0">also: ' +
            aliases.map(function (a) { return "<em>" + S.esc(a) + "</em>"; }).join(", ") + "</p>"
        : "") +
      (d.locus ? '<p class="small" style="margin:.2rem 0 0">locus: ' + S.escTicks(d.locus) + "</p>" : "") +
      (d.consensus ? '<p class="small" style="margin:.2rem 0 0">sign-off: ' + S.escTicks(d.consensus) + "</p>" : "") +
      '<div class="defbody">' + S.escTicks(d.body || "(no body in the shard)") + "</div>" +
      "</div>";
  }

  function apply() {
    var q = document.getElementById("q").value.trim().toLowerCase();
    var k = document.getElementById("f-kind").value;
    var st = document.getElementById("f-status").value;

    State.view = State.all.filter(function (d) {
      if (k && d.kind !== k) return false;
      if (st && d.status !== st) return false;
      if (q && haystack(d).indexOf(q) < 0) return false;
      return true;
    });

    document.getElementById("defs").innerHTML = State.view.length
      ? State.view.map(card).join("")
      : '<p class="small">No definition matches. Search runs over the term, its aliases, and the shard id.</p>';
    document.getElementById("count").textContent =
      S.num(State.view.length) + " of " + S.num(State.all.length) + " definitions";
  }

  document.addEventListener("DOMContentLoaded", function () {
    S.loadJSON(["definitions"], function (d) {
      var data = d.definitions;
      var counts = chips(data);
      State.all = (data.definitions || []).slice().sort(function (a, b) {
        return String(a.term || a.id).localeCompare(String(b.term || b.id));
      });
      options("f-kind", counts.byKind, "any provenance");
      options("f-status", counts.byStatus, "any status");
      document.getElementById("q").addEventListener("input", apply);
      document.getElementById("f-kind").addEventListener("change", apply);
      document.getElementById("f-status").addEventListener("change", apply);
      document.getElementById("reset").addEventListener("click", function () {
        document.getElementById("q").value = "";
        document.getElementById("f-kind").value = "";
        document.getElementById("f-status").value = "";
        apply();
      });
      apply();
    });
  });
})();
