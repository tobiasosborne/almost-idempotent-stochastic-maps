/* evidence.js — the run-bundle table from site/data/runs.json.
   L3 discipline: this page renders the bundles' own dates, slugs, and headline text, and links each row
   to the bundle README in the repository (where the re-run command, seeds, schema, and invariant live).
   No number here is a literal, and no run result is presented as a proof. */
(function () {
  "use strict";
  var S = window.S;

  var RUNS = "https://github.com/tobiasosborne/almost-idempotent-stochastic-maps/tree/master/runs/";

  var State = { all: [], view: [], key: "date", dir: -1 };

  function chips(data) {
    var b = data.bundles || [];
    var years = {}, months = {};
    b.forEach(function (r) {
      years[String(r.date).slice(0, 4)] = 1;
      months[String(r.date).slice(0, 7)] = 1;
    });
    var dates = b.map(function (r) { return r.date; }).sort();
    document.getElementById("ev-chips").innerHTML =
      S.chip("num", "run bundles: " + S.num(data.total)) +
      S.chip("num", "evidence, never proof (L3)") +
      (dates.length ? S.chip("audit", "first: " + dates[0]) + S.chip("audit", "latest: " + dates[dates.length - 1]) : "");
  }

  function sortView() {
    var k = State.key, dir = State.dir;
    State.view.sort(function (a, b) {
      var x = String(a[k] || ""), y = String(b[k] || "");
      if (x === y) return String(a.slug).localeCompare(String(b.slug));
      return x < y ? -dir : dir;
    });
  }

  function render() {
    var tb = document.querySelector("#runs tbody");
    tb.innerHTML = State.view.length
      ? State.view.map(function (r) {
          return "<tr>" +
            '<td class="mono-cell">' + S.esc(r.date) + "</td>" +
            "<td><a href=\"" + RUNS + encodeURIComponent(r.bundle) + "\"><span class=\"mono-cell\">" +
              S.esc(r.slug) + "</span></a><br><span class=\"small\">" + S.esc(r.bundle) + "</span></td>" +
            "<td><span class=\"headline\">" + S.escTicks(r.headline || "(no headline recorded)") + "</span></td>" +
            "</tr>";
        }).join("")
      : '<tr><td colspan="3" class="small">No bundle matches this search.</td></tr>';

    document.getElementById("count").textContent =
      S.num(State.view.length) + " of " + S.num(State.all.length) + " bundles";

    ["date", "slug"].forEach(function (k) {
      var th = document.getElementById("th-" + k);
      if (k === State.key) th.setAttribute("aria-sort", State.dir === 1 ? "ascending" : "descending");
      else th.removeAttribute("aria-sort");
    });
  }

  function apply() {
    var q = document.getElementById("q").value.trim().toLowerCase();
    State.view = State.all.filter(function (r) {
      if (!q) return true;
      return ((r.slug || "") + " " + (r.bundle || "") + " " + (r.title || "") + " " + (r.headline || ""))
        .toLowerCase().indexOf(q) >= 0;
    });
    sortView();
    render();
  }

  document.addEventListener("DOMContentLoaded", function () {
    S.loadJSON(["runs"], function (d) {
      var data = d.runs;
      State.all = (data.bundles || []).slice();
      chips(data);

      document.querySelectorAll("#runs th.sortable button").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var k = btn.getAttribute("data-key");
          if (State.key === k) State.dir = -State.dir;
          else { State.key = k; State.dir = k === "date" ? -1 : 1; }
          sortView();
          render();
        });
      });
      document.getElementById("q").addEventListener("input", apply);
      document.getElementById("reset").addEventListener("click", function () {
        document.getElementById("q").value = "";
        apply();
      });

      document.getElementById("runs-note").innerHTML =
        "Generator note, verbatim: " + S.esc(data.note || "") +
        " Headlines are excerpted from each bundle README and may be truncated by the generator; the bundle " +
        "link is the full record — parameters, seeds, command line, data under <code>data/SCHEMA.md</code>, " +
        "and the invariant that makes the run checkable.";

      apply();
    });
  });
})();
