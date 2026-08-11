/* defense.js — the Swiss-Cheese Defense page.
   HARD RULE (L0 / plan principle P1): every number rendered here comes from site/data/defense.json or
   site/data/retractions.json at runtime. Nothing is hardcoded, so a regeneration cannot leave this page
   publishing a count the repository no longer supports. */
(function () {
  "use strict";
  var S = window.S;

  /* ---------- metric presentation ---------- */

  var LABELS = {
    validations_per_challenge_x100: "node validations per challenge",
    externals_total: "externals registered (provenance-gated)",
    externals_byte_matched_quotes: "… byte-matched verbatim quotes",
    externals_workspace_imports: "… dependency imports from proof workspaces",
    externals_without_quote: "… registered without a quote",
    externals_failed: "… failing the byte-match gate",
    definition_shards: "canonical definition shards",
    definitions_cited: "… ground-truth cited (byte-matched)",
    definitions_locked: "… locked (consensus / original)",
    refs_sources: "pinned reference sources",
    refs_pinned_files: "SHA256-pinned reference files",
    contracts: "one-line contracts in the DAG",
    dep_edges: "dependency edges",
    edges_rendered: "edges rendered (deps + routes)",
    route_edges: "OR-route edges",
    af_validated: "shards at af: validated",
    af_seeded: "shards at af: seeded",
    or_routed_shards: "OR-routed shards",
    status_proved: "rows at status: proved",
    proved_not_af_validated: "… proved but NOT af-validated",
    nonrigorous_rows: "rows tagged non-rigorous",
    retractions_caught_here: "retractions caught at this layer",
    workspaces: "af workspaces",
    workspaces_exported: "… exported",
    proof_initialized: "proof trees initialised",
    node_created: "proof nodes created",
    node_validated: "nodes validated by fresh verifiers",
    node_unvalidated: "nodes un-validated again",
    node_amended: "nodes amended after challenge",
    challenge_raised: "challenges raised",
    challenge_resolved: "challenges resolved",
    def_added: "byte-matched imports registered",
    ledger_files: "ledger event files parsed",
    ledger_unparseable: "… unparseable",
    qed: "QED events",
    af_node_amended_events: "af amendment events reviewed",
    af_node_unvalidated_events: "af un-validation events",
    balloon_tripwire_aborts: "balloon-tripwire aborts",
    disproved_results: "registry claims disproved",
    numerical_status_rows: "rows held at numerical (evidence, never proof)",
    obstruction_results: "obstruction results",
    run_bundles: "reproducible run bundles",
    dated_entries: "dated ledger entries",
    entries_with_catching_layer_named: "… naming the layer that caught it"
  };

  function label(k) { return LABELS[k] || k.replace(/_/g, " "); }

  function value(k, v) {
    if (/_x100$/.test(k) && typeof v === "number") return (v / 100).toFixed(2);
    if (typeof v === "number") return S.num(v);
    if (v && typeof v === "object") return S.esc(JSON.stringify(v));
    return S.esc(v);
  }

  function layerById(def, id) {
    var found = null;
    (def.layers || []).forEach(function (l) { if (l.id === id) found = l; });
    return found || { metrics: {} };
  }

  function m(def, id, key) {
    var v = layerById(def, id).metrics[key];
    return v === undefined ? "—" : S.num(v);
  }

  /* ---------- top line ---------- */

  function topline(def) {
    var L1 = "L1", L4 = "L4", L6 = "L6";
    var tiles = [
      [m(def, L4, "challenge_raised") + " / " + m(def, L4, "challenge_resolved"), "challenges raised / resolved"],
      [m(def, L4, "node_validated"), "node validations, fresh verifiers"],
      [m(def, L4, "node_amended"), "nodes amended after challenge"],
      [m(def, L4, "workspaces") + " / " + m(def, L4, "workspaces_exported"), "af workspaces / exported"],
      [m(def, L1, "externals_total"), "provenance-gated externals"],
      [m(def, L1, "definition_shards"), "canonical definitions"],
      [m(def, L6, "balloon_tripwire_aborts"), "balloon-tripwire aborts"],
      [m(def, L6, "disproved_results"), "registry claims disproved"],
      [S.num(S.get(def, "backstop.metrics.dated_entries", null)), "retraction-ledger entries"]
    ];
    document.getElementById("topline").innerHTML = tiles.map(function (t) {
      return '<div class="stat"><span class="n">' + t[0] + '</span><span class="k">' + t[1] + "</span></div>";
    }).join("");

    document.getElementById("topline-note").innerHTML =
      "Externals break down as <b>" + m(def, L1, "externals_byte_matched_quotes") +
      "</b> byte-matched verbatim quotes + <b>" + m(def, L1, "externals_workspace_imports") +
      "</b> dependency imports from proof workspaces + <b>" + m(def, L1, "externals_without_quote") +
      "</b> registered without a quote, with <b>" + m(def, L1, "externals_failed") +
      "</b> failing the byte-match gate. Ledger coverage: <b>" + m(def, "L4", "ledger_files") +
      "</b> event files parsed, <b>" + m(def, "L4", "ledger_unparseable") + "</b> unparseable.";
  }

  /* ---------- the six layers ---------- */

  function layers(def) {
    document.getElementById("layers").innerHTML = (def.layers || []).map(function (l) {
      var keys = Object.keys(l.metrics || {});
      return '<div class="card layer">' +
        '<span class="lid">' + S.esc(l.id) + "</span>" +
        "<h3>" + S.esc(l.name) + "</h3>" +
        '<p class="small" style="margin:.2rem 0 0">Targets: ' + S.esc(l.error_class) + "</p>" +
        '<ul class="metrics">' + keys.map(function (k) {
          return "<li><span>" + S.esc(label(k)) + "</span><b>" + value(k, l.metrics[k]) + "</b></li>";
        }).join("") + "</ul>" +
        '<p class="holes"><em>known hole</em> ' + S.esc(l.known_holes) + "</p>" +
        "</div>";
    }).join("");
  }

  /* ---------- the schematic ---------- */

  // Hole rows per slab, chosen so trajectory A (y=98) clears L1–L3 and is stopped by L4, and
  // trajectory B (y=152) clears L1–L4 and is stopped by L5. The slabs are a schematic, not data.
  var HOLES = [
    [72, 98, 152, 196],
    [98, 152, 208],
    [64, 98, 152],
    [128, 152, 178],
    [72, 104, 200],
    [84, 140, 192]
  ];

  function cheese(def, ret) {
    var byLayer = (ret && ret.by_catching_layer) || {};
    var x0 = 56, w = 38, gap = 70, top = 34, h = 196;
    var p = [];

    (def.layers || []).forEach(function (l, i) {
      var x = x0 + i * gap;
      p.push('<rect x="' + x + '" y="' + top + '" width="' + w + '" height="' + h +
        '" rx="4" fill="var(--surface-2)" stroke="var(--line)"></rect>');
      (HOLES[i] || []).forEach(function (y) {
        p.push('<ellipse cx="' + (x + w / 2) + '" cy="' + y + '" rx="' + (w / 2 - 5) +
          '" ry="9" fill="var(--ground)" stroke="var(--line)"></ellipse>');
      });
      p.push('<text x="' + (x + w / 2) + '" y="' + (top + h + 16) + '" text-anchor="middle" font-weight="700" fill="var(--accent)">' +
        S.esc(l.id) + "</text>");
      var words = String(l.name).split(" ").slice(0, 3);
      words.forEach(function (word, wi) {
        p.push('<text x="' + (x + w / 2) + '" y="' + (top + h + 28 + wi * 9) +
          '" text-anchor="middle" font-size="7">' + S.esc(word) + "</text>");
      });
    });

    // backstop slab
    var bx = x0 + 6 * gap;
    p.push('<rect x="' + bx + '" y="' + top + '" width="' + w + '" height="' + h +
      '" rx="4" fill="var(--st-dead-bg)" stroke="var(--st-dead)"></rect>');
    p.push('<text x="' + (bx + w / 2) + '" y="' + (top + h + 16) + '" text-anchor="middle" font-weight="700" fill="var(--st-dead)">ledger</text>');
    p.push('<text x="' + (bx + w / 2) + '" y="' + (top + h + 28) + '" text-anchor="middle" font-size="7">backstop</text>');

    function traj(y, stopIndex, colour, text) {
      var stopX = x0 + stopIndex * gap;
      p.push('<line x1="8" y1="' + y + '" x2="' + stopX + '" y2="' + y + '" stroke="' + colour +
        '" stroke-width="2"></line>');
      p.push('<polygon points="' + stopX + "," + y + " " + (stopX - 8) + "," + (y - 4) + " " +
        (stopX - 8) + "," + (y + 4) + '" fill="' + colour + '"></polygon>');
      // "stopped here" cross on the blocking slab face
      p.push('<g stroke="' + colour + '" stroke-width="2.5"><line x1="' + (stopX + 6) + '" y1="' + (y - 7) +
        '" x2="' + (stopX + 20) + '" y2="' + (y + 7) + '"></line><line x1="' + (stopX + 6) + '" y1="' + (y + 7) +
        '" x2="' + (stopX + 20) + '" y2="' + (y - 7) + '"></line></g>');
      p.push('<text x="10" y="' + (y - 8) + '" font-size="8.5" fill="' + colour + '">' + S.esc(text) + "</text>");
    }

    traj(98, 3, "var(--st-dead)",
      "lem-hx-financing-floor — passed L3 batched review, stopped at L4 (" + (byLayer.L4 || 0) + " ledger entry)");
    traj(152, 4, "var(--st-audit)",
      "af-validated certificates — passed L4 cohorts, stopped at L5 sweeps (" + (byLayer.L5 || 0) + " ledger entries)");

    p.push('<text x="8" y="' + (top - 12) + '" font-size="9" fill="var(--muted)">errors enter from the left; a hole is a known blind spot; the holes do not line up</text>');

    var svg = document.getElementById("cheese");
    svg.innerHTML = p.join("");
    svg.querySelectorAll("text").forEach(function (t) {
      if (!t.getAttribute("fill")) t.setAttribute("fill", "var(--ink-soft)");
      if (!t.getAttribute("font-size")) t.setAttribute("font-size", "9");
      t.setAttribute("font-family", "system-ui, sans-serif");
    });
  }

  function crossings(ret) {
    var entries = (ret && ret.entries) || [];
    var groups = [
      { layer: "L4", head: "Passed hostile batched review (L3) — caught by the af trees (L4)" },
      { layer: "L5", head: "Passed the af cohorts (L4) — caught by meta-audit sweeps (L5)" }
    ];
    document.getElementById("crossings").innerHTML = groups.map(function (g) {
      var hits = entries.filter(function (e) { return e.catch_layer === g.layer; });
      return '<div class="card">' +
        '<div class="chips" style="margin-bottom:.5rem">' +
        S.chip(g.layer === "L4" ? "audit" : "conj", g.layer + " caught " + hits.length) + "</div>" +
        "<h3>" + S.esc(g.head) + "</h3>" +
        (hits.length
          ? "<ul class=\"panel-list\" style=\"padding-left:1.1rem;font-size:.92rem\">" + hits.map(function (e) {
              return "<li><span class=\"mono small\">" + S.esc(e.date) + "</span> — " + S.escTicks(e.title) +
                '<br><span class="small">' + S.escTicks(e.caught_by) + "</span></li>";
            }).join("") + "</ul>"
          : '<p class="small">No ledger entry currently attributed to this layer.</p>') +
        "</div>";
    }).join("");
  }

  /* ---------- the retraction ledger ---------- */

  function retractions(ret) {
    var byLayer = ret.by_catching_layer || {};
    document.getElementById("backstop-chips").innerHTML =
      S.chip("dead", "entries: " + S.num(ret.total)) +
      Object.keys(byLayer).sort().map(function (k) {
        return S.chip(k === "L5" ? "conj" : k === "L4" ? "audit" : "num", "caught at " + k + ": " + byLayer[k]);
      }).join("");

    document.getElementById("retractions").innerHTML = (ret.entries || []).map(function (e) {
      var fields = [
        ["what was claimed", e.claimed],
        ["why it was wrong", e.why_wrong],
        ["caught by", e.caught_by],
        ["resolution", e.resolution]
      ];
      var extra = e.extra && Object.keys(e.extra).length
        ? Object.keys(e.extra).map(function (k) {
            return "<dt>" + S.esc(label(k)) + "</dt><dd>" + S.escTicks(e.extra[k]) + "</dd>";
          }).join("")
        : "";
      return '<div class="card retraction">' +
        '<div class="chips" style="margin-bottom:.4rem">' +
        '<span class="date">' + S.esc(e.date) + "</span>" +
        S.chip("dead", "caught at " + (e.catch_layer || "unclassified")) +
        (e.qualifier ? '<span class="small">' + S.esc(e.qualifier) + "</span>" : "") +
        "</div>" +
        "<h3>" + S.escTicks(e.title) + "</h3>" +
        "<dl>" + fields.map(function (f) {
          return f[1] ? "<dt>" + f[0] + "</dt><dd>" + S.escTicks(f[1]) + "</dd>" : "";
        }).join("") + extra + "</dl>" +
        "</div>";
    }).join("");

    document.getElementById("retraction-note").textContent = ret.note || "";
  }

  /* ---------- boot ---------- */

  document.addEventListener("DOMContentLoaded", function () {
    S.loadJSON(["defense", "retractions"], function (d) {
      topline(d.defense);
      layers(d.defense);
      cheese(d.defense, d.retractions);
      crossings(d.retractions);
      retractions(d.retractions);
      var n = document.createElement("p");
      n.className = "small";
      n.innerHTML = "Layer-attribution caveat, verbatim from the generator: " +
        S.esc(S.get(d.defense, "notes.catch_layer_classification", ""));
      document.getElementById("retraction-note").after(n);
    });
  });
})();
