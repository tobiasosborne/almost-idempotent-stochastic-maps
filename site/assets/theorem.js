/* theorem.js — the Theorem page: live 4x4 sharpness witness + the data-driven status panels.
   The witness algebra is the af-validated family's own identities (lem-prh-sharpness /
   cor-classical-sharpness): eta = 2*lambda^2, floor sqrt(eta/2) = lambda, achieved sqrt(2*eta) = 2*lambda.
   It is reproduced here, never re-derived. */
(function () {
  "use strict";
  var S = window.S;

  /* ================= the witness widget (self-contained, no data needed) ================= */

  var LAM_MAX = 0.48;   // matches the slider max in index.html
  var ETA_MAX = 2 * LAM_MAX * LAM_MAX;   // 0.4608
  var D_MAX = 2 * LAM_MAX;               // 0.96
  var X0 = 52, X1 = 406, Y0 = 18, Y1 = 226;

  function sx(eta) { return X0 + (eta / ETA_MAX) * (X1 - X0); }
  function sy(d) { return Y1 - (d / D_MAX) * (Y1 - Y0); }
  function f4(x) { return x.toFixed(4); }

  function rows(l) {
    var c = 1 - l;
    return [
      [c, 0, l, 0],
      [0, c, 0, l],
      [c * c, l * c, l * c, l * l],
      [l * c, c * c, l * l, l * c]
    ];
  }

  function curvePath(fn) {
    var pts = [], N = 96;
    for (var i = 0; i <= N; i++) {
      var eta = (i / N) * ETA_MAX;
      pts.push((i ? "L" : "M") + sx(eta).toFixed(2) + " " + sy(fn(eta)).toFixed(2));
    }
    return pts.join(" ");
  }

  function buildChart() {
    var floor = function (eta) { return Math.sqrt(eta / 2); };
    var achieved = function (eta) { return Math.sqrt(2 * eta); };
    var parts = [];

    // forbidden region: everything strictly below the floor curve
    parts.push('<path d="' + curvePath(floor) + " L" + sx(ETA_MAX).toFixed(2) + " " + sy(0) +
      " L" + sx(0) + " " + sy(0) + ' Z" fill="var(--st-dead-bg)" stroke="none"></path>');

    // axes
    parts.push('<line x1="' + X0 + '" y1="' + Y1 + '" x2="' + X1 + '" y2="' + Y1 +
      '" stroke="var(--line)" stroke-width="1"></line>');
    parts.push('<line x1="' + X0 + '" y1="' + Y0 + '" x2="' + X0 + '" y2="' + Y1 +
      '" stroke="var(--line)" stroke-width="1"></line>');

    // ticks
    [0, 0.1, 0.2, 0.3, 0.4].forEach(function (e) {
      parts.push('<line x1="' + sx(e).toFixed(1) + '" y1="' + Y1 + '" x2="' + sx(e).toFixed(1) +
        '" y2="' + (Y1 + 4) + '" stroke="var(--line)"></line>');
      parts.push('<text x="' + sx(e).toFixed(1) + '" y="' + (Y1 + 15) + '" text-anchor="middle">' + e + "</text>");
    });
    [0, 0.25, 0.5, 0.75].forEach(function (d) {
      parts.push('<line x1="' + (X0 - 4) + '" y1="' + sy(d).toFixed(1) + '" x2="' + X0 +
        '" y2="' + sy(d).toFixed(1) + '" stroke="var(--line)"></line>');
      parts.push('<text x="' + (X0 - 8) + '" y="' + (sy(d) + 3.5).toFixed(1) + '" text-anchor="end">' + d + "</text>");
    });
    parts.push('<text x="' + ((X0 + X1) / 2) + '" y="' + (Y1 + 30) + '" text-anchor="middle">defect η = 2λ²</text>');
    parts.push('<text x="14" y="' + ((Y0 + Y1) / 2) + '" text-anchor="middle" transform="rotate(-90 14 ' +
      ((Y0 + Y1) / 2) + ')">distance ‖Q−E‖</text>');

    // curves
    parts.push('<path d="' + curvePath(achieved) + '" fill="none" stroke="var(--accent)" stroke-width="2"></path>');
    parts.push('<path d="' + curvePath(floor) + '" fill="none" stroke="var(--st-dead)" stroke-width="2" stroke-dasharray="6 4"></path>');

    // forbidden-region label
    parts.push('<text x="' + sx(0.24).toFixed(1) + '" y="' + sy(0.13).toFixed(1) +
      '" fill="var(--st-dead)" font-size="9">forbidden — an E below this line is wrong</text>');

    // live marker layer
    parts.push('<g id="marks">' +
      '<line id="mk-guide" x1="0" y1="' + Y0 + '" x2="0" y2="' + Y1 + '" stroke="var(--muted)" stroke-dasharray="3 3"></line>' +
      '<circle id="mk-ach" r="4.5" fill="var(--accent)"></circle>' +
      '<circle id="mk-floor" r="4.5" fill="var(--st-dead)"></circle>' +
      "</g>");

    // legend
    parts.push('<g transform="translate(' + (X0 + 8) + ',' + (Y0 + 4) + ')">' +
      '<line x1="0" y1="0" x2="18" y2="0" stroke="var(--accent)" stroke-width="2"></line>' +
      '<text x="24" y="3.5">achieved √(2η) = 2λ</text>' +
      '<line x1="0" y1="14" x2="18" y2="14" stroke="var(--st-dead)" stroke-width="2" stroke-dasharray="6 4"></line>' +
      '<text x="24" y="17.5">floor √(η/2) = λ (lem-prh-sharpness)</text>' +
      "</g>");

    document.getElementById("chart-body").innerHTML = parts.join("");
  }

  function render(l) {
    var eta = 2 * l * l, floor = l, ach = 2 * l;

    document.getElementById("lam-out").textContent = l.toFixed(3);
    document.getElementById("ro-eta").textContent = f4(eta);
    document.getElementById("ro-floor").textContent = f4(floor);
    document.getElementById("ro-ach").textContent = f4(ach);

    var html = rows(l).map(function (r) {
      return "<tr>" + r.map(function (x) { return "<td>" + f4(x) + "</td>"; }).join("") + "</tr>";
    }).join("");
    document.getElementById("qmat").innerHTML = html;

    var x = sx(eta);
    document.getElementById("mk-guide").setAttribute("x1", x);
    document.getElementById("mk-guide").setAttribute("x2", x);
    document.getElementById("mk-ach").setAttribute("cx", x);
    document.getElementById("mk-ach").setAttribute("cy", sy(ach));
    document.getElementById("mk-floor").setAttribute("cx", x);
    document.getElementById("mk-floor").setAttribute("cy", sy(floor));
  }

  /* ================= data-driven panels ================= */

  function li(k, v) {
    return "<li><span>" + k + "</span><b>" + v + "</b></li>";
  }

  function fill(d) {
    var dag = d.dag, stats = d.stats;
    var byId = S.byId(dag.nodes);
    var op = byId["op-classical"] || {};
    var sharp = byId["cor-classical-sharpness"] || {};
    var legacyThm = byId["thm-classical-factorization"] || {};
    var hume = byId["ex-hume"] || {};
    var closure = dag.op_classical_closure || {};
    var routes = closure.routes || [];
    var r1 = routes[0] || {}, r2 = routes[1] || {};
    var byStatus = S.get(dag, "summary.by_status", {});

    document.getElementById("hero-chips").innerHTML =
      S.nodeChips(op) +
      S.chip("audit", "T0 rung — not Lean") +
      S.chip(S.statusClass(sharp), "sharpness: " + (sharp.status || "?") + " / af " + (sharp.af || "none"));

    document.getElementById("hero-contract").textContent = op.contract || "(not found in dag.json)";

    document.getElementById("is-proved").innerHTML = [
      li("<code>op-classical</code> (upper bound)", S.esc(op.status + " / af " + op.af)),
      li("<code>cor-classical-sharpness</code> (exponent ½)", S.esc(sharp.status + " / af " + sharp.af)),
      li("Route-F closure &mdash; results below <code>op-classical</code>", S.num(r1.size)),
      li("&hellip; of those, af-validated", S.num(r1.af_validated) + (r1.all_available ? " (all)" : "")),
      li("af-validated results in the registry (T0)", S.num(stats.t0_validated) + " / " + S.num(stats.registry_total)),
      li("exported af workspaces", S.num(stats.workspaces_validated))
    ].join("");

    document.getElementById("not-proved").innerHTML = [
      li("Lean/mathlib <code>sorry</code>-free proofs", "none"),
      li("peer review / publication", "none"),
      li("explicit numerical value for <span class=\"math\"><span class=\"v\">C</span></span>", "none (K is big-O only)"),
      li("sharpness in the signed parameter <span class=\"math\">&delta;</span>", "no carrier"),
      li("legacy signed route &mdash; parked, results", S.num(r2.size) + ", af-validated " + S.num(r2.af_validated)),
      li("&hellip; its entry <code>thm-classical-factorization</code>", S.esc(legacyThm.status + " / af " + legacyThm.af)),
      li("<code>ex-hume</code> (the old sharpness carrier)", S.esc(hume.status || "?")),
      li("registry rows still <code>conjecture</code>", S.num(byStatus.conjecture)),
      li("registry rows still <code>proved-mod-audit</code>", S.num(byStatus["proved-mod-audit"]))
    ].join("");
  }

  /* ================= boot ================= */

  document.addEventListener("DOMContentLoaded", function () {
    buildChart();
    var slider = document.getElementById("lam");
    slider.addEventListener("input", function () { render(parseFloat(slider.value)); });
    render(parseFloat(slider.value));
    S.loadJSON(["dag", "stats"], fill);
  });
})();
