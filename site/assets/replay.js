/* replay.js — the Campaign Replay: the T0-over-time chart and the log explorer.
   Everything on this page is rendered from site/data/frontier.json at load time; no count, date, or
   note is a literal in the source. The chart is one series (no legend needed — the heading names it),
   drawn as a 2px line over a recessive grid, with every decrease marked and direct-labelled
   endpoints. The log list renders one page of rows at a time so 1,300 entries stay responsive. */
(function () {
  "use strict";
  var S = window.S;

  var PAGE = 100;
  // MR is wide enough for the direct end label ("200 af-validated") to sit outside the plot.
  var W = 720, H = 300, ML = 44, MR = 104, MT = 18, MB = 34;

  var State = { entries: [], view: [], page: 0 };

  /* ================= helpers ================= */

  function day(ts) { return String(ts || "").slice(0, 10); }
  function minute(ts) { return String(ts || "").slice(0, 16).replace("T", " "); }

  function niceMax(v) {
    var step = v > 400 ? 100 : v > 150 ? 50 : v > 60 ? 25 : 10;
    return Math.ceil(v / step) * step;
  }

  /* ================= the chart ================= */

  function dipsOf(tl) {
    var out = [];
    for (var i = 1; i < tl.length; i++) {
      if (tl[i].t0 < tl[i - 1].t0) out.push({ i: i, from: tl[i - 1].t0, to: tl[i].t0, ts: tl[i].ts });
    }
    return out;
  }

  function chart(fr) {
    var tl = (fr.t0_timeline || []).slice();
    var svg = document.getElementById("t0chart");
    if (!tl.length) { svg.innerHTML = ""; return { dips: [], points: 0 }; }

    var t = tl.map(function (p) { return Date.parse(p.ts); });
    var t0 = Math.min.apply(null, t), t1 = Math.max.apply(null, t);
    var ymax = niceMax(Math.max.apply(null, tl.map(function (p) { return p.t0; })));
    var span = (t1 - t0) || 1;

    function sx(ms) { return ML + (ms - t0) / span * (W - ML - MR); }
    function sy(v) { return H - MB - (v / ymax) * (H - MT - MB); }

    var p = [];

    // recessive grid: solid hairlines, one shade off the surface
    var ticks = 4, i;
    for (i = 0; i <= ticks; i++) {
      var v = Math.round(ymax * i / ticks), y = sy(v);
      p.push('<line class="gridline" x1="' + ML + '" y1="' + y + '" x2="' + (W - MR) + '" y2="' + y + '"></line>');
      p.push('<text x="' + (ML - 8) + '" y="' + (y + 3.5) + '" text-anchor="end">' + v + "</text>");
    }
    p.push('<line class="axis" x1="' + ML + '" y1="' + (H - MB) + '" x2="' + (W - MR) + '" y2="' + (H - MB) + '"></line>');

    // x ticks: one per ISO week boundary present in the data
    var seen = {};
    tl.forEach(function (pt) {
      var d = day(pt.ts);
      var wk = Math.floor(Date.parse(d) / 6048e5);
      if (seen[wk]) return;
      seen[wk] = true;
      var x = sx(Date.parse(pt.ts));
      p.push('<line class="gridline" x1="' + x + '" y1="' + MT + '" x2="' + x + '" y2="' + (H - MB) + '" opacity=".5"></line>');
      p.push('<text x="' + x + '" y="' + (H - MB + 15) + '" text-anchor="middle">' + S.esc(d) + "</text>");
    });

    // the series
    var pts = tl.map(function (pt) { return sx(Date.parse(pt.ts)).toFixed(1) + "," + sy(pt.t0).toFixed(1); });
    p.push('<polyline id="t0-line" class="series" points="' + pts.join(" ") + '"></polyline>');

    // the decreases — status red, 2px surface ring, ≥8px targets
    var dips = dipsOf(tl);
    dips.forEach(function (d, k) {
      p.push('<circle class="dip" data-dip="' + k + '" cx="' + sx(Date.parse(d.ts)).toFixed(1) +
        '" cy="' + sy(d.to).toFixed(1) + '" r="4.5"></circle>');
    });

    // endpoints, direct-labelled (no number on every point)
    var first = tl[0], last = tl[tl.length - 1];
    p.push('<circle class="endpt" cx="' + sx(Date.parse(first.ts)).toFixed(1) + '" cy="' + sy(first.t0).toFixed(1) + '" r="4"></circle>');
    p.push('<circle class="endpt" cx="' + sx(Date.parse(last.ts)).toFixed(1) + '" cy="' + sy(last.t0).toFixed(1) + '" r="5"></circle>');
    p.push('<text class="direct" x="' + (sx(Date.parse(first.ts)) + 8) + '" y="' + (sy(first.t0) + 14) +
      '" fill="var(--ink-soft)">' + first.t0 + " &middot; " + S.esc(day(first.ts)) + "</text>");
    p.push('<text class="direct" x="' + (sx(Date.parse(last.ts)) + 9) + '" y="' + (sy(last.t0) + 4) +
      '" fill="var(--st-t0)" font-weight="700">' + last.t0 + " af-validated</text>");
    p.push('<text class="direct" x="' + (sx(Date.parse(last.ts)) + 9) + '" y="' + (sy(last.t0) + 16) +
      '" fill="var(--muted)">' + S.esc(day(last.ts)) + "</text>");

    // hover layer: one crosshair + tooltip over the whole plot (no per-point marks)
    p.push('<line id="cross" class="crosshair" x1="0" y1="' + MT + '" x2="0" y2="' + (H - MB) + '" opacity="0"></line>');
    p.push('<circle id="hoverpt" r="4" fill="var(--st-t0)" stroke="var(--surface)" stroke-width="2" opacity="0"></circle>');
    p.push('<rect id="hitbox" x="' + ML + '" y="' + MT + '" width="' + (W - ML - MR) + '" height="' + (H - MT - MB) +
      '" fill="transparent"></rect>');

    svg.innerHTML = p.join("");
    svg.setAttribute("data-points", String(tl.length));
    svg.setAttribute("data-dips", String(dips.length));
    // the accessible description is computed, never a literal
    svg.setAttribute("aria-label",
      "Line chart of the af-validated result count over the campaign, rising from " + first.t0 +
      " on " + day(first.ts) + " to " + last.t0 + " on " + day(last.ts) + ", with " + dips.length +
      " marked decrease" + (dips.length === 1 ? "" : "s") +
      " where previously banked results were retracted.");
    svg.querySelectorAll("text").forEach(function (el) {
      if (!el.getAttribute("fill")) el.setAttribute("fill", "var(--muted)");
    });

    bindHover(svg, tl, dips, sx, sy, t0, t1);
    dipTable(dips);
    return { dips: dips, points: tl.length };
  }

  function bindHover(svg, tl, dips, sx, sy) {
    var tip = document.getElementById("tip");
    var box = document.getElementById("chartbox");
    var cross = document.getElementById("cross");
    var hp = document.getElementById("hoverpt");
    var dipAt = {};
    dips.forEach(function (d) { dipAt[d.i] = d; });
    var cur = -1;

    function show(idx, clientX, clientY) {
      if (idx < 0 || idx >= tl.length) return;
      cur = idx;
      var pt = tl[idx], d = dipAt[idx];
      var x = sx(Date.parse(pt.ts)), y = sy(pt.t0);
      cross.setAttribute("x1", x); cross.setAttribute("x2", x); cross.setAttribute("opacity", "1");
      hp.setAttribute("cx", x); hp.setAttribute("cy", y); hp.setAttribute("opacity", "1");
      hp.setAttribute("fill", d ? "var(--st-dead)" : "var(--st-t0)");
      tip.hidden = false;
      tip.innerHTML =
        "<b>" + S.esc(minute(pt.ts)) + "</b><br>af-validated: <b>" + pt.t0 + "</b>" +
        (d ? '<br><span style="color:var(--st-dead)">decrease: <b>' + d.from + " &rarr; " + d.to +
             "</b> &mdash; banked results taken back</span>" : "");
      var r = box.getBoundingClientRect(), sr = svg.getBoundingClientRect();
      var px = (clientX === undefined ? sr.left + (x / W) * sr.width : clientX) - r.left;
      var py = (clientY === undefined ? sr.top + (y / H) * sr.height : clientY) - r.top;
      tip.style.left = Math.max(4, Math.min(px + 12, r.width - tip.offsetWidth - 6)) + "px";
      tip.style.top = Math.max(4, py - tip.offsetHeight - 10) + "px";
    }

    function hide() {
      tip.hidden = true;
      cross.setAttribute("opacity", "0");
      hp.setAttribute("opacity", "0");
    }

    function nearest(clientX) {
      var r = svg.getBoundingClientRect();
      var ux = (clientX - r.left) / r.width * W;
      var best = 0, bd = Infinity;
      tl.forEach(function (pt, i) {
        var d = Math.abs(sx(Date.parse(pt.ts)) - ux);
        if (d < bd) { bd = d; best = i; }
      });
      return best;
    }

    svg.addEventListener("pointermove", function (ev) { show(nearest(ev.clientX), ev.clientX, ev.clientY); });
    svg.addEventListener("pointerleave", hide);
    svg.addEventListener("blur", hide);
    svg.addEventListener("keydown", function (ev) {
      if (ev.key === "ArrowRight" || ev.key === "ArrowLeft") {
        ev.preventDefault();
        show(Math.max(0, Math.min(tl.length - 1, (cur < 0 ? 0 : cur) + (ev.key === "ArrowRight" ? 1 : -1))));
      } else if (ev.key === "Escape") { hide(); }
    });
  }

  function dipTable(dips) {
    document.querySelector("#dip-table tbody").innerHTML = dips.map(function (d) {
      return "<tr><td class=\"mono-cell\">" + S.esc(minute(d.ts)) + "</td><td class=\"num\">" + d.from +
        "</td><td class=\"num\">" + d.to + "</td><td class=\"num\">&minus;" + (d.from - d.to) + "</td></tr>";
    }).join("");
  }

  /* ================= the top line ================= */

  function topline(fr, dips) {
    var e = fr.entries || [], tl = fr.t0_timeline || [];
    var banked = e.filter(function (x) { return x.outcome === "banked"; }).length;
    var arms = {};
    e.forEach(function (x) { if (x.arm) arms[x.arm] = 1; });
    var days = {};
    e.forEach(function (x) { days[day(x.ts)] = 1; });
    var lost = dips.reduce(function (a, d) { return a + (d.from - d.to); }, 0);

    var tiles = [
      [S.num(fr.total), "log entries (append-only)"],
      [S.num(banked), "entries logged <code>banked</code>"],
      [S.num(Object.keys(arms).length), "research arms pulled"],
      [S.num(Object.keys(days).length), "days of campaign"],
      [S.num(tl.length), "waves reporting a T0 count"],
      [S.num(dips.length), "decreases (de-bankings)"],
      [S.num(lost), "af-validated results taken back"],
      [tl.length ? S.num(tl[tl.length - 1].t0) : "—", "af-validated now (T0)"]
    ];
    document.getElementById("topline").innerHTML = tiles.map(function (t) {
      return '<div class="stat"><span class="n">' + t[0] + '</span><span class="k">' + t[1] + "</span></div>";
    }).join("");

    // the prose count of decreases is filled from the same computed dips as the chart
    var dc = document.getElementById("dip-count");
    if (dc) dc.textContent = S.num(dips.length);

    document.getElementById("chart-note").innerHTML =
      "Series note, verbatim from the generator: " + S.esc(fr.note || "");
  }

  /* ================= the log explorer ================= */

  // Some log records carry a malformed `outcome` (an entire note leaked into the field when it was
  // written). They are shown honestly rather than dropped: grouped under one filter option.
  function cleanOutcome(o) { return typeof o === "string" && /^[a-z][a-z-]{0,19}$/.test(o); }

  function buildFilters(entries) {
    var oc = {}, ar = {}, malformed = 0;
    entries.forEach(function (e) {
      if (cleanOutcome(e.outcome)) oc[e.outcome] = (oc[e.outcome] || 0) + 1;
      else malformed++;
      ar[e.arm || "(no arm)"] = (ar[e.arm || "(no arm)"] || 0) + 1;
    });

    var os = Object.keys(oc).sort(function (a, b) { return oc[b] - oc[a]; });
    var sel = document.getElementById("f-outcome");
    sel.innerHTML = '<option value="">all (' + entries.length + ")</option>" +
      os.map(function (k) { return '<option value="' + S.esc(k) + '">' + S.esc(k) + " (" + oc[k] + ")</option>"; }).join("") +
      (malformed ? '<option value=" malformed">malformed tag (' + malformed + ")</option>" : "");

    var as = Object.keys(ar).sort(function (a, b) { return ar[b] - ar[a]; });
    var sa = document.getElementById("f-arm");
    sa.innerHTML = '<option value="">all arms</option>' +
      as.map(function (k) { return '<option value="' + S.esc(k) + '">' + S.esc(k) + " (" + ar[k] + ")</option>"; }).join("");

    document.getElementById("parse-note").innerHTML =
      "Fields are the controller's own: <code>ts</code>, <code>cycle</code>, <code>arm</code>, " +
      "<code>outcome</code>, <code>note</code>. " + S.num(malformed) +
      " record" + (malformed === 1 ? " carries" : "s carry") + " a malformed <code>outcome</code> (the note text " +
      "leaked into the tag when it was logged); they are kept and grouped rather than dropped. " +
      S.num(entries.filter(function (e) { return !e.arm; }).length) +
      " records have no arm — turns that ran no wave are logged separately and are not arm pulls.";
  }

  function applyFilters() {
    var o = document.getElementById("f-outcome").value;
    var a = document.getElementById("f-arm").value;
    var q = document.getElementById("f-text").value.trim().toLowerCase();

    State.view = State.entries.filter(function (e) {
      if (o === " malformed") { if (cleanOutcome(e.outcome)) return false; }
      else if (o && e.outcome !== o) return false;
      if (a && (e.arm || "(no arm)") !== a) return false;
      if (q) {
        var hay = (e.note || "") + " " + (e.arm || "") + " " + (e.outcome || "") + " " + e.ts;
        if (hay.toLowerCase().indexOf(q) < 0) return false;
      }
      return true;
    });
    State.page = 0;
    renderPage();
  }

  function renderPage() {
    var n = State.view.length;
    var pages = Math.max(1, Math.ceil(n / PAGE));
    if (State.page >= pages) State.page = pages - 1;
    var from = State.page * PAGE, slice = State.view.slice(from, from + PAGE);

    document.getElementById("log-list").innerHTML = slice.length
      ? slice.map(function (e, i) { return row(e, from + i); }).join("")
      : '<p class="small" style="padding:.8rem 0">No log entry matches this filter.</p>';

    document.getElementById("f-count").textContent =
      S.num(n) + " of " + S.num(State.entries.length) + " entries";
    document.getElementById("pos").textContent = n
      ? "showing " + S.num(from + 1) + "–" + S.num(from + slice.length) + " (page " + (State.page + 1) + " of " + pages + ")"
      : "nothing to show";
    document.getElementById("prev").disabled = State.page === 0;
    document.getElementById("next").disabled = State.page >= pages - 1;
  }

  function row(e, idx) {
    var out = cleanOutcome(e.outcome) ? e.outcome : "malformed tag";
    var cls = cleanOutcome(e.outcome) ? " tag--" + e.outcome : "";
    var note = e.note || "";
    var trunc = note.length > 165 ? note.slice(0, 165) + "…" : note;
    return '<button class="logrow" type="button" data-i="' + idx + '" aria-expanded="false">' +
      '<span class="meta">' +
        '<span class="ts">' + S.esc(minute(e.ts)) + "</span>" +
        '<span class="tag tag--arm">' + S.esc(e.arm || "no arm") + "</span>" +
        '<span class="tag' + cls + '">' + S.esc(out) + "</span>" +
        '<span class="ts">#' + S.num(e.cycle) + "</span>" +
      "</span>" +
      '<span class="note">' + S.escTicks(trunc) + "</span>" +
      "</button>";
  }

  function bindLog() {
    document.getElementById("log-list").addEventListener("click", function (ev) {
      var btn = ev.target.closest ? ev.target.closest(".logrow") : null;
      if (!btn) return;
      var e = State.view[parseInt(btn.getAttribute("data-i"), 10)];
      if (!e) return;
      var open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", open ? "false" : "true");
      var note = e.note || "";
      btn.querySelector(".note").innerHTML = S.escTicks(
        open ? (note.length > 165 ? note.slice(0, 165) + "…" : note) : note);
    });

    ["f-outcome", "f-arm"].forEach(function (id) {
      document.getElementById(id).addEventListener("change", applyFilters);
    });
    document.getElementById("f-text").addEventListener("input", applyFilters);
    document.getElementById("f-reset").addEventListener("click", function () {
      document.getElementById("f-outcome").value = "";
      document.getElementById("f-arm").value = "";
      document.getElementById("f-text").value = "";
      applyFilters();
    });
    document.getElementById("prev").addEventListener("click", function () {
      if (State.page > 0) { State.page--; renderPage(); window.scrollBy(0, -1); }
    });
    document.getElementById("next").addEventListener("click", function () {
      State.page++; renderPage();
    });
  }

  /* ================= boot ================= */

  document.addEventListener("DOMContentLoaded", function () {
    S.loadJSON(["frontier"], function (d) {
      var fr = d.frontier;
      var c = chart(fr);
      topline(fr, c.dips);
      // newest first: the controller log is append-only, so the tail is the present
      State.entries = (fr.entries || []).slice().reverse();
      buildFilters(State.entries);
      bindLog();
      applyFilters();
    });
  });
})();
