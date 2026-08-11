/* site.js — shared shell behaviour for the Glass-Box Lab site.
   Vanilla JS, classic script (no modules: file:// blocks module loading), no dependencies.
   Exposes the global `S` namespace. */
(function () {
  "use strict";

  var S = {};
  window.S = S;

  /* ---------- theme: three states (system / light / dark), persisted ---------- */
  var KEY = "aism-theme";
  function applyTheme(t) {
    var root = document.documentElement;
    if (t === "light" || t === "dark") root.setAttribute("data-theme", t);
    else root.removeAttribute("data-theme");
    var b = document.getElementById("theme-btn");
    if (b) {
      b.textContent = t === "system" ? "Theme: auto" : t === "light" ? "Theme: light" : "Theme: dark";
      b.setAttribute("aria-label", "Colour theme: " + t + ". Activate to change.");
    }
  }
  function currentTheme() {
    try { return localStorage.getItem(KEY) || "system"; } catch (e) { return "system"; }
  }
  S.initTheme = function () {
    applyTheme(currentTheme());
    var b = document.getElementById("theme-btn");
    if (!b) return;
    b.addEventListener("click", function () {
      var order = ["system", "light", "dark"];
      var next = order[(order.indexOf(currentTheme()) + 1) % order.length];
      try { localStorage.setItem(KEY, next); } catch (e) { /* private mode: session only */ }
      applyTheme(next);
      document.dispatchEvent(new CustomEvent("themechange", { detail: next }));
    });
  };
  // Apply immediately so the correct palette is in place before first paint of the body.
  applyTheme(currentTheme());

  /* ---------- data loading (relative paths; graceful file:// notice) ---------- */
  S.loadJSON = function (names, onReady) {
    var out = {}, pending = names.length, failed = false;
    if (typeof fetch !== "function") {          // ancient/exotic runtime: same honest notice
      S.fetchNotice(new Error("this browser has no fetch()"));
      return;
    }
    names.forEach(function (n) {
      Promise.resolve().then(function () { return fetch("data/" + n + ".json", { cache: "no-cache" }); })
        .then(function (r) {
          if (!r.ok) throw new Error("HTTP " + r.status + " for data/" + n + ".json");
          return r.json();
        })
        .then(function (j) {
          out[n] = j;
          if (--pending === 0 && !failed) onReady(out);
        })
        .catch(function (err) {
          if (failed) return;
          failed = true;
          S.fetchNotice(err);
        });
    });
  };

  S.fetchNotice = function (err) {
    var host = document.getElementById("data-error");
    if (!host) return;
    var isFile = location.protocol === "file:";
    host.hidden = false;
    host.innerHTML =
      "<strong>The page data could not be loaded.</strong> " +
      (isFile
        ? "This page reads <code>site/data/*.json</code> with <code>fetch</code>, which browsers block for <code>file://</code> URLs. " +
          "Serve the folder instead: run <code>python3 -m http.server 8000 -d site</code> from the repository root " +
          "(or <code>python3 -m http.server 8000</code> from inside <code>site/</code>) and open " +
          "<code>http://localhost:8000/</code>."
        : "Check that <code>site/data/*.json</code> is present next to this page. Regenerate it with " +
          "<code>python3 scripts/gen-site-data.py --generate</code>.") +
      "<br><span class=\"small\">" + S.esc(String(err && err.message ? err.message : err)) + "</span>";
    document.querySelectorAll("[data-needs-data]").forEach(function (el) { el.hidden = true; });
  };

  /* ---------- small helpers ---------- */
  S.esc = function (s) {
    return String(s === undefined || s === null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  };

  // Escape, then render `backticked` spans as <code> (the ledgers are markdown-flavoured text).
  S.escTicks = function (s) {
    return S.esc(s).replace(/`([^`]+)`/g, function (_, m) { return "<code>" + m + "</code>"; });
  };

  S.num = function (n) {
    if (n === undefined || n === null || isNaN(n)) return "—";
    return Number(n).toLocaleString("en-US");
  };

  S.get = function (obj, path, dflt) {
    var cur = obj;
    var parts = path.split(".");
    for (var i = 0; i < parts.length; i++) {
      if (cur === undefined || cur === null || !(parts[i] in cur)) return dflt;
      cur = cur[parts[i]];
    }
    return cur === undefined ? dflt : cur;
  };

  /* ---------- the rigour ladder: registry row -> one of five palette classes ---------- */
  // Classes mirror the plan's validated badge system: af-validated / paper-proved
  // (proved or proved-mod-audit without an af tree) / numerical / conjecture / disproved.
  S.statusClass = function (node) {
    var st = node.status || "", af = node.af || "none";
    if (af === "validated") return "t0";
    if (st === "disproved" || st === "obstruction") return "dead";
    if (st === "conjecture" || st === "open") return "conj";
    if (st === "numerical" || st === "heuristic" || st === "stated") return "num";
    return "audit"; // proved / proved-mod-audit without a validated af tree
  };

  S.CLASS_LABEL = {
    t0: "af-validated (T0)",
    audit: "proved, not af-validated",
    num: "numerical / stated",
    conj: "conjecture / open",
    dead: "disproved / obstruction"
  };

  S.CLASS_VAR = {
    t0: "--st-t0", audit: "--st-audit", num: "--st-num", conj: "--st-conj", dead: "--st-dead"
  };

  S.chip = function (cls, text) {
    return '<span class="chip chip--' + cls + '"><span class="dot" aria-hidden="true"></span>' + S.esc(text) + "</span>";
  };

  // Status chips for one registry node, always carrying the literal registry words.
  S.nodeChips = function (node) {
    var cls = S.statusClass(node);
    var html = S.chip(cls, "status: " + (node.status || "?"));
    html += S.chip(node.af === "validated" ? "t0" : node.af === "seeded" ? "num" : "audit", "af: " + (node.af || "none"));
    return html;
  };

  S.byId = function (nodes) {
    var m = {};
    nodes.forEach(function (n) { m[n.id] = n; });
    return m;
  };

  document.addEventListener("DOMContentLoaded", function () { S.initTheme(); });
})();
