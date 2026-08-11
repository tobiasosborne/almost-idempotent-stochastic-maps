/* ledger.js — the Honesty Ledger: docs/LEARNINGS.md as dated cards.
   Every card, chip, and count is rendered from site/data/retractions.json at load time. The ledger
   fields are markdown-flavoured text: they are HTML-escaped, `backticked` spans become <code>, and
   line breaks are preserved by the .retraction dd rule in site.css (white-space: pre-wrap). */
(function () {
  "use strict";
  var S = window.S;

  var LAYER_CLASS = { L1: "num", L2: "num", L3: "audit", L4: "audit", L5: "conj", L6: "conj" };

  var LAYER_NAME = {
    L1: "vocabulary & provenance",
    L2: "contract DAG + linker",
    L3: "hostile review (reviewer ≠ author)",
    L4: "af adversarial trees",
    L5: "meta-audit sweeps",
    L6: "oracles, numerics, tripwires"
  };

  function chips(ret) {
    var by = ret.by_catching_layer || {};
    var keys = Object.keys(by).sort();
    document.getElementById("ledger-chips").innerHTML =
      S.chip("dead", "retracted claims: " + S.num(ret.total)) +
      keys.map(function (k) {
        return S.chip(LAYER_CLASS[k] || "num", "caught at " + k + ": " + by[k]);
      }).join("");
  }

  function card(e) {
    var fields = [
      ["what was claimed", e.claimed],
      ["why it was wrong", e.why_wrong],
      ["caught by", e.caught_by],
      ["resolution", e.resolution]
    ];
    var extra = e.extra && Object.keys(e.extra).length
      ? Object.keys(e.extra).map(function (k) {
          return "<dt>" + S.esc(k.replace(/_/g, " ")) + "</dt><dd>" + S.escTicks(e.extra[k]) + "</dd>";
        }).join("")
      : "";
    var layer = e.catch_layer || "";
    return '<div class="card retraction">' +
      '<div class="chips" style="margin-bottom:.45rem">' +
        '<span class="date">' + S.esc(e.date) + "</span>" +
        S.chip(LAYER_CLASS[layer] || "dead",
               layer ? "caught at " + layer + " — " + (LAYER_NAME[layer] || "") : "layer unclassified") +
        (e.qualifier ? '<span class="small">' + S.esc(e.qualifier) + "</span>" : "") +
      "</div>" +
      "<h3>" + S.escTicks(e.title) + "</h3>" +
      "<dl>" + fields.map(function (f) {
        return f[1] ? "<dt>" + f[0] + "</dt><dd>" + S.escTicks(f[1]) + "</dd>" : "";
      }).join("") + extra + "</dl>" +
      "</div>";
  }

  document.addEventListener("DOMContentLoaded", function () {
    S.loadJSON(["retractions"], function (d) {
      var ret = d.retractions;
      chips(ret);
      document.getElementById("retractions").innerHTML = (ret.entries || []).map(card).join("");
      document.getElementById("ledger-note").innerHTML =
        "Source note, verbatim from the generator: " + S.esc(ret.note || "") +
        " Layer names follow the six-layer breakdown on <a href=\"defense.html\">the defense page</a>; the " +
        "layer tag is a heuristic over the entry text, so read the <em>caught by</em> field, which is the " +
        "ledger's own wording.";
    });
  });
})();
