/* atlas.js — the Proof Atlas: all registry nodes and edges from site/data/dag.json.
   No libraries. Layout is a deterministic longest-path layering (columns = depth, wrapped into
   sub-columns so no layer runs off the canvas), computed once on load; interaction is a single
   SVG transform, so pan/zoom never re-lays-out. */
(function () {
  "use strict";
  var S = window.S;

  var REPO = "https://github.com/tobiasosborne/almost-idempotent-stochastic-maps/blob/master/";

  // Layout constants: tuned so the whole 374-node graph fits a wide-but-readable canvas
  // (~2.4:1); denser layers wrap into sub-columns of MAX_ROWS.
  var ROWH = 20, COLW = 38, LAYER_GAP = 18, MARGIN = 30, MAX_ROWS = 52, R = 6.5;

  var G = {                       // module state
    nodes: [], edges: [], byId: {}, pos: {},
    active: { t0: true, audit: true, num: true, conj: true, dead: true },
    lens: "all", lensSet: null, selected: null,
    view: { k: 1, x: 0, y: 0 }, bounds: null
  };

  /* ---------------- layout ---------------- */

  function layout(nodes, edges) {
    var out = {}, indeg = {}, adj = {};
    nodes.forEach(function (n) { indeg[n.id] = 0; adj[n.id] = []; });
    edges.forEach(function (e) {
      if (!(e.from in adj) || !(e.to in indeg)) return;
      adj[e.from].push(e.to);
      indeg[e.to]++;
    });

    var depth = {}, queue = [];
    nodes.forEach(function (n) { depth[n.id] = 0; if (indeg[n.id] === 0) queue.push(n.id); });
    var rem = {};
    Object.keys(indeg).forEach(function (k) { rem[k] = indeg[k]; });
    for (var qi = 0; qi < queue.length; qi++) {
      var u = queue[qi];
      adj[u].forEach(function (v) {
        if (depth[v] < depth[u] + 1) depth[v] = depth[u] + 1;
        if (--rem[v] === 0) queue.push(v);
      });
    }

    var layers = {};
    nodes.forEach(function (n) {
      var d = depth[n.id] || 0;
      (layers[d] = layers[d] || []).push(n);
    });

    var depths = Object.keys(layers).map(Number).sort(function (a, b) { return a - b; });
    var x = MARGIN, maxY = 0;
    depths.forEach(function (d) {
      var group = layers[d].slice().sort(function (a, b) {
        var fa = family(a.id), fb = family(b.id);
        return fa === fb ? (a.id < b.id ? -1 : 1) : (fa < fb ? -1 : 1);
      });
      var cols = Math.max(1, Math.ceil(group.length / MAX_ROWS));
      var rowsPer = Math.ceil(group.length / cols);
      group.forEach(function (n, i) {
        var c = Math.floor(i / rowsPer), r = i % rowsPer;
        var px = x + c * COLW, py = MARGIN + r * ROWH;
        out[n.id] = { x: px, y: py, depth: d };
        if (py > maxY) maxY = py;
      });
      x += cols * COLW + LAYER_GAP;
    });

    G.bounds = { w: x + MARGIN, h: maxY + MARGIN };
    return out;
  }

  function family(id) {
    var parts = id.split("-");
    return parts.length > 1 ? parts[1] : id;
  }

  /* ---------------- rendering ---------------- */

  function draw() {
    var ep = [], np = [];
    G.edges.forEach(function (e, i) {
      var a = G.pos[e.from], b = G.pos[e.to];
      if (!a || !b) return;
      ep.push('<line class="edge" data-i="' + i + '" data-from="' + S.esc(e.from) + '" data-to="' + S.esc(e.to) +
        '" x1="' + a.x + '" y1="' + a.y + '" x2="' + b.x + '" y2="' + b.y + '"' +
        (e.kind === "route" ? ' stroke-dasharray="4 3"' : "") + "></line>");
    });
    G.nodes.forEach(function (n) {
      var p = G.pos[n.id];
      if (!p) return;
      var cls = S.statusClass(n);
      np.push('<g class="node" data-id="' + S.esc(n.id) + '" data-cls="' + cls +
        '" transform="translate(' + p.x + "," + p.y + ')" tabindex="0" role="button">' +
        '<circle r="' + R + '" fill="var(' + S.CLASS_VAR[cls] + ')"></circle>' +
        "<title>" + S.esc(n.id + " — " + n.status + " / af " + n.af + " — " + S.CLASS_LABEL[cls]) + "</title>" +
        '<text x="' + (R + 3) + '" y="2.5">' + S.esc(n.id) + "</text></g>");
    });
    document.getElementById("edges").innerHTML = ep.join("");
    document.getElementById("nodes").innerHTML = np.join("");
  }

  function applyFilters() {
    var visible = {};
    document.querySelectorAll("#nodes .node").forEach(function (g) {
      var id = g.getAttribute("data-id");
      var on = G.active[g.getAttribute("data-cls")];
      var inLens = !G.lensSet || G.lensSet[id];
      g.classList.toggle("hidden", !on);
      g.classList.toggle("dim", on && !inLens);
      g.classList.toggle("sel", id === G.selected);
      visible[id] = on;
    });
    document.querySelectorAll("#edges .edge").forEach(function (l) {
      var f = l.getAttribute("data-from"), t = l.getAttribute("data-to");
      var on = visible[f] && visible[t];
      var inLens = !G.lensSet || (G.lensSet[f] && G.lensSet[t]);
      var touchesSel = G.selected && (f === G.selected || t === G.selected);
      l.classList.toggle("hidden", !on);
      l.classList.toggle("dim", on && !inLens && !touchesSel);
      l.classList.toggle("hi", !!touchesSel);
    });
  }

  /* ---------------- camera ---------------- */

  function setView() {
    document.getElementById("cam").setAttribute("transform",
      "translate(" + G.view.x + "," + G.view.y + ") scale(" + G.view.k + ")");
    document.getElementById("atlas").classList.toggle("zoomed", G.view.k > 1.5);
  }

  function fit() {
    var svg = document.getElementById("atlas");
    var r = svg.getBoundingClientRect();
    var k = Math.min(r.width / G.bounds.w, r.height / G.bounds.h) * 0.98;
    G.view.k = k || 1;
    G.view.x = (r.width - G.bounds.w * G.view.k) / 2;
    G.view.y = (r.height - G.bounds.h * G.view.k) / 2;
    setView();
  }

  function centerOn(id) {
    var p = G.pos[id];
    if (!p) return;
    var r = document.getElementById("atlas").getBoundingClientRect();
    G.view.k = Math.max(G.view.k, 1.8);
    G.view.x = r.width / 2 - p.x * G.view.k;
    G.view.y = r.height / 2 - p.y * G.view.k;
    setView();
  }

  function bindCamera() {
    var svg = document.getElementById("atlas");
    var drag = null;
    svg.addEventListener("pointerdown", function (ev) {
      drag = { x: ev.clientX, y: ev.clientY, vx: G.view.x, vy: G.view.y, moved: false };
      svg.classList.add("dragging");
      svg.setPointerCapture(ev.pointerId);
    });
    svg.addEventListener("pointermove", function (ev) {
      if (!drag) return;
      var dx = ev.clientX - drag.x, dy = ev.clientY - drag.y;
      if (Math.abs(dx) + Math.abs(dy) > 3) drag.moved = true;
      G.view.x = drag.vx + dx;
      G.view.y = drag.vy + dy;
      setView();
    });
    function endDrag(ev) {
      if (drag) { try { svg.releasePointerCapture(ev.pointerId); } catch (e) { /* already released */ } }
      svg.classList.remove("dragging");
      drag = null;
    }
    svg.addEventListener("pointerup", endDrag);
    svg.addEventListener("pointercancel", endDrag);
    svg.addEventListener("wheel", function (ev) {
      ev.preventDefault();
      var r = svg.getBoundingClientRect();
      var mx = ev.clientX - r.left, my = ev.clientY - r.top;
      var f = Math.exp(-ev.deltaY * 0.0015);
      var k2 = Math.min(8, Math.max(0.12, G.view.k * f));
      G.view.x = mx - (mx - G.view.x) * (k2 / G.view.k);
      G.view.y = my - (my - G.view.y) * (k2 / G.view.k);
      G.view.k = k2;
      setView();
    }, { passive: false });

    document.getElementById("nodes").addEventListener("click", function (ev) {
      var g = ev.target.closest(".node");
      if (g) select(g.getAttribute("data-id"));
    });
    document.getElementById("nodes").addEventListener("keydown", function (ev) {
      if (ev.key !== "Enter" && ev.key !== " ") return;
      var g = ev.target.closest(".node");
      if (g) { ev.preventDefault(); select(g.getAttribute("data-id")); }
    });
    document.getElementById("fit").addEventListener("click", function () { fit(); });
    window.addEventListener("resize", function () { setView(); });
  }

  /* ---------------- side panel ---------------- */

  function select(id) {
    var n = G.byId[id];
    if (!n) return;
    G.selected = id;
    var kids = G.nodes.filter(function (m) { return (m.deps || []).indexOf(id) >= 0; });
    var validated = n.af === "validated" && n.workspace;

    var html = '<p class="label">selection</p>' +
      '<h3 class="mono" style="font-size:.95rem;word-break:break-word">' + S.esc(n.id) + "</h3>" +
      '<div class="chips" style="margin-bottom:.6rem">' + S.nodeChips(n) +
      S.chip("num", "kind: " + S.esc(n.kind || "?")) +
      S.chip("audit", "owner: " + S.esc(n.owner || "?")) + "</div>" +
      '<p class="label">contract (verbatim)</p><p class="contract">' + S.esc(n.contract || "") + "</p>";

    html += '<p class="label" style="margin-top:.8rem">depends on (' + (n.deps || []).length + ")</p>";
    html += (n.deps || []).length
      ? "<ul>" + n.deps.map(function (d) {
          return '<li><a class="dep" data-goto="' + S.esc(d) + '">' + S.esc(d) + "</a></li>";
        }).join("") + "</ul>"
      : '<p class="small">none (a leaf of the DAG)</p>';

    if ((n.routes || []).length) {
      html += '<p class="label" style="margin-top:.8rem">OR-routes</p><ul>' + n.routes.map(function (r, i) {
        return "<li>route " + (i + 1) + ": " + r.map(function (d) {
          return '<a class="dep" data-goto="' + S.esc(d) + '">' + S.esc(d) + "</a>";
        }).join(", ") + "</li>";
      }).join("") + "</ul>";
    }

    html += '<p class="label" style="margin-top:.8rem">used by (' + kids.length + ")</p>";
    html += kids.length
      ? "<ul>" + kids.slice(0, 40).map(function (k) {
          return '<li><a class="dep" data-goto="' + S.esc(k.id) + '">' + S.esc(k.id) + "</a></li>";
        }).join("") + (kids.length > 40 ? "<li class=\"small\">… " + (kids.length - 40) + " more</li>" : "") + "</ul>"
      : '<p class="small">nothing depends on it yet</p>';

    html += '<p style="margin-top:1rem">' +
      (validated
        ? '<a href="' + REPO + S.esc(n.workspace) + '/export.md">audit deeper: the exported af tree &rarr;</a>'
        : '<span class="small">No validated af workspace — nothing to audit at the tree level. Registry shard: ' +
          '<a href="' + REPO + "argument/lemmas/" + S.esc(n.id) + '.md">' + S.esc(n.id) + ".md</a></span>") +
      "</p>";
    if (validated) {
      html += '<p class="small"><a href="' + REPO + "argument/lemmas/" + S.esc(n.id) + '.md">registry shard &rarr;</a></p>';
    }

    var panel = document.getElementById("panel-body");
    panel.innerHTML = html;
    panel.querySelectorAll("a.dep").forEach(function (a) {
      a.addEventListener("click", function () {
        var t = a.getAttribute("data-goto");
        select(t);
        centerOn(t);
      });
    });
    applyFilters();
  }

  /* ---------------- controls ---------------- */

  function ancestorsOf(id) {
    var parents = {};
    G.nodes.forEach(function (n) { parents[n.id] = (n.deps || []).slice(); });
    G.nodes.forEach(function (n) {
      (n.routes || []).forEach(function (r) { parents[n.id] = parents[n.id].concat(r); });
    });
    var seen = {}, stack = [id];
    while (stack.length) {
      var u = stack.pop();
      (parents[u] || []).forEach(function (p) {
        if (!seen[p]) { seen[p] = true; stack.push(p); }
      });
    }
    seen[id] = true;
    return seen;
  }

  function setify(list) {
    var s = {};
    (list || []).forEach(function (i) { s[i] = true; });
    return s;
  }

  function buildControls(dag) {
    var counts = { t0: 0, audit: 0, num: 0, conj: 0, dead: 0 };
    G.nodes.forEach(function (n) { counts[S.statusClass(n)]++; });

    document.getElementById("status-filters").innerHTML = Object.keys(counts).map(function (c) {
      return '<button class="tog st-' + c + '" type="button" data-cls="' + c + '" aria-pressed="true">' +
        '<span class="dot" aria-hidden="true"></span>' + S.esc(S.CLASS_LABEL[c]) + " · " + counts[c] + "</button>";
    }).join(" ");
    document.getElementById("status-filters").addEventListener("click", function (ev) {
      var b = ev.target.closest("button.tog");
      if (!b) return;
      var c = b.getAttribute("data-cls");
      G.active[c] = !G.active[c];
      b.setAttribute("aria-pressed", G.active[c] ? "true" : "false");
      applyFilters();
    });

    var closure = dag.op_classical_closure || {};
    var routes = closure.routes || [];
    var r1 = routes[0] || { ancestors: [] }, r2 = routes[1] || { ancestors: [] };
    var r1set = setify(r1.ancestors.concat([closure.root]));
    var r2set = setify(r2.ancestors.concat([closure.root]));
    var sharp = ancestorsOf("cor-classical-sharpness");
    var sharpN = Object.keys(sharp).length;

    // Lens labels carry the closure's own ancestor count from the data (r*.size); the highlighted
    // set additionally includes the root op-classical, which the route closes.
    var lenses = [
      { id: "all", name: "All · " + G.nodes.length, set: null },
      { id: "routef", name: "Route-F closure · " + S.num(r1.size), set: r1set },
      { id: "legacy", name: "Legacy signed route · " + S.num(r2.size), set: r2set },
      { id: "sharp", name: "Sharpness island · " + sharpN, set: sharp }
    ];
    document.getElementById("lens-buttons").innerHTML = lenses.map(function (l) {
      return '<button class="tog" type="button" data-lens="' + l.id + '" aria-pressed="' +
        (l.id === "all" ? "true" : "false") + '">' + S.esc(l.name) + "</button>";
    }).join(" ");
    document.getElementById("lens-buttons").addEventListener("click", function (ev) {
      var b = ev.target.closest("button.tog");
      if (!b) return;
      var id = b.getAttribute("data-lens");
      lenses.forEach(function (l) { if (l.id === id) G.lensSet = l.set; });
      G.lens = id;
      document.querySelectorAll("#lens-buttons button.tog").forEach(function (x) {
        x.setAttribute("aria-pressed", x === b ? "true" : "false");
      });
      applyFilters();
    });

    document.getElementById("legend").innerHTML =
      '<p class="label" style="margin-top:1rem">legend</p>' +
      Object.keys(counts).map(function (c) {
        return '<div style="display:flex;align-items:center;gap:.45rem;margin:.2rem 0">' +
          '<span style="width:.7rem;height:.7rem;border-radius:50%;background:var(' + S.CLASS_VAR[c] +
          ');display:inline-block"></span><span>' + S.esc(S.CLASS_LABEL[c]) + " — " + counts[c] + "</span></div>";
      }).join("") +
      '<p class="small" style="margin-top:.6rem">Solid edges are declared dependencies; dashed edges are ' +
      'OR-route edges (a result closed by either of two independent routes). Labels appear as you zoom in.</p>';
  }

  /* ---------------- boot ---------------- */

  document.addEventListener("DOMContentLoaded", function () {
    S.loadJSON(["dag"], function (d) {
      var dag = d.dag;
      G.nodes = dag.nodes;
      G.edges = dag.edges;
      G.byId = S.byId(G.nodes);
      G.pos = layout(G.nodes, G.edges);

      draw();
      buildControls(dag);
      applyFilters();
      bindCamera();
      fit();

      var s = dag.summary || {};
      document.getElementById("atlas-blurb").innerHTML =
        "Every registry result is a node (<b>" + S.num(s.total || G.nodes.length) + "</b>); every edge is a " +
        "declared dependency (<b>" + S.num(s.edges_rendered || G.edges.length) + "</b>, of which <b>" +
        S.num(s.route_edges) + "</b> are OR-route edges), drawn left to right from support to consumer. " +
        "Colour is the rigour rung and the text label always travels with it. Drag to pan, scroll to zoom, " +
        "click a node for its verbatim one-line contract; validated nodes link straight to their exported " +
        "adversarial proof tree.";

      select("op-classical");
      fit();
    });
  });
})();
