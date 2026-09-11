"""Dashboard renderer: one self-contained HTML file, no JS, no CDN.

Same visual language as the review screen — book serif for judgment, mono for
machine facts — because they are two views of one system and a reviewer should
feel that.

The chart is a plain bar per condition with the Wilson interval drawn as a
whisker, in SVG. A point estimate without its interval is the kind of chart
that gets a paper into trouble, so the interval is not optional here.
"""
from __future__ import annotations

import html


def _e(x) -> str:
    return html.escape("" if x is None else str(x))


CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{--ink:#16181D;--paper:#FBFBF9;--rule:#D6D6CF;--mute:#6B6F76;
 --oxblood:#7A1F2B;--amber:#B4700A;--moss:#2F5D50;--wash:#F2F2EE;
 --book:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
 --sans:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 --mono:ui-monospace,"SF Mono","Cascadia Mono","Roboto Mono",Menlo,monospace}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);
 font-size:15px;line-height:1.55}
.wrap{max-width:1040px;margin:0 auto;padding:0 24px 96px}
.mast{border-bottom:2px solid var(--ink);padding:22px 0 12px;margin-bottom:8px;
 display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:12px}
.mast h1{font-family:var(--book);font-weight:400;font-size:25px;margin:0}
.mast .sub{font-family:var(--mono);font-size:11px;letter-spacing:.14em;
 text-transform:uppercase;color:var(--mute)}
.mock{background:#fdf7ec;border-left:3px solid var(--amber);padding:12px 16px;
 margin:18px 0;font-size:14px}
.note{color:var(--mute);font-size:13.5px;max-width:70ch;margin:16px 0 0}
h2{font-family:var(--book);font-weight:400;font-size:20px;margin:40px 0 4px}
.eyebrow{font-family:var(--mono);font-size:10px;letter-spacing:.14em;
 text-transform:uppercase;color:var(--mute);margin:38px 0 6px}
table{width:100%;border-collapse:collapse;font-size:13.5px;margin-top:10px}
th{font-family:var(--mono);font-size:10px;letter-spacing:.1em;
 text-transform:uppercase;color:var(--mute);text-align:left;font-weight:400;
 padding:0 12px 6px 0;border-bottom:1px solid var(--rule)}
td{padding:7px 12px 7px 0;border-bottom:1px solid var(--rule);
 font-family:var(--mono);font-size:12.5px;vertical-align:top}
td.n{text-align:right}
td.good{color:var(--moss)}
td.bad{color:var(--oxblood)}
.chart{margin-top:14px}
.bar-label{font-family:var(--mono);font-size:11px;fill:var(--ink)}
.bar-val{font-family:var(--mono);font-size:11px;fill:var(--mute)}
.pill{font-family:var(--mono);font-size:11px;border:1px solid var(--rule);
 background:var(--wash);padding:2px 7px;margin-right:4px;display:inline-block}
"""


def _bars(summaries: list[dict]) -> str:
    """Agreement per condition with 95% Wilson whiskers."""
    rows = [(f"{s['meta']['condition']} · {str(s['meta']['model'])[:18]}",
             s["disposition_agreement"]) for s in summaries]
    if not rows:
        return ""
    h = 34 * len(rows) + 34
    left, width = 190, 620
    svg = [f"<svg class='chart' viewBox='0 0 {left + width + 60} {h}' "
           f"role='img' aria-label='Disposition agreement by condition'>"]
    for i in range(0, 11, 2):
        x = left + width * i / 10
        svg.append(f"<line x1='{x:.0f}' y1='16' x2='{x:.0f}' y2='{h - 18}' "
                   f"stroke='#D6D6CF' stroke-width='1'/>")
        svg.append(f"<text x='{x:.0f}' y='{h - 4}' class='bar-val' "
                   f"text-anchor='middle'>{i * 10}%</text>")
    for i, (label, a) in enumerate(rows):
        y = 26 + i * 34
        r = a["rate"] or 0
        lo, hi = a["ci95"]
        svg.append(f"<text x='{left - 10}' y='{y + 11}' class='bar-label' "
                   f"text-anchor='end'>{_e(label)}</text>")
        svg.append(f"<rect x='{left}' y='{y}' width='{width * r:.1f}' "
                   f"height='15' fill='#7A1F2B'/>")
        svg.append(f"<line x1='{left + width * lo:.1f}' y1='{y + 7.5}' "
                   f"x2='{left + width * hi:.1f}' y2='{y + 7.5}' "
                   f"stroke='#16181D' stroke-width='1'/>")
        for b in (lo, hi):
            svg.append(f"<line x1='{left + width * b:.1f}' y1='{y + 2}' "
                       f"x2='{left + width * b:.1f}' y2='{y + 13}' "
                       f"stroke='#16181D' stroke-width='1'/>")
        svg.append(f"<text x='{left + width + 8}' y='{y + 11}' "
                   f"class='bar-val'>{r:.0%} (n={a['n']})</text>")
    svg.append("</svg>")
    return "".join(svg)


def _fidelity_table(summaries: list[dict]) -> str:
    head = ("<tr><th>Condition</th><th>Model</th><th>A6 floor</th>"
            "<th>A3 control plane</th><th>Let through wrongly</th>"
            "<th>Held wrongly</th><th>Lapsed reliance</th></tr>")
    body = ""
    for s in summaries:
        m = s["meta"]
        a6, a3 = s["a6_floor_fidelity"], s["a3_control_plane_fidelity"]
        lap = s.get("relied_on_lapsed_rate")
        body += (
            f"<tr><td>{_e(m['condition'])}</td>"
            f"<td>{_e(str(m['model'])[:22])}</td>"
            f"<td class='n {_cls(a6)}'>{_pct(a6)}</td>"
            f"<td class='n {_cls(a3)}'>{_pct(a3)}</td>"
            f"<td class='n'>{_pct(s['permissive_errors'], invert=True)}</td>"
            f"<td class='n'>{_pct(s['restrictive_errors'], invert=True)}</td>"
            f"<td class='n'>{_pct(lap, invert=True) if lap else '—'}</td>"
            "</tr>")
    return f"<table>{head}{body}</table>"


def _cls(r) -> str:
    if not r or r["rate"] is None:
        return ""
    return "good" if r["rate"] >= 0.999 else "bad"


def _pct(r, invert: bool = False) -> str:
    if not r or r["rate"] is None:
        return "—"
    return f"{r['rate']:.0%} ({r['k']}/{r['n']})"


def _class_table(summaries: list[dict]) -> str:
    classes = sorted({c for s in summaries for c in s["by_class"]})
    head = "<tr><th>Case class</th>" + "".join(
        f"<th>{_e(s['meta']['condition'])}</th>" for s in summaries) + "</tr>"
    body = ""
    for c in classes:
        body += f"<tr><td>{_e(c)}</td>"
        for s in summaries:
            r = s["by_class"].get(c)
            body += f"<td class='n'>{_pct(r)}</td>" if r else "<td>—</td>"
        body += "</tr>"
    return f"<table>{head}{body}</table>"


def render(summaries: list[dict]) -> str:
    if not summaries:
        return "<html><body>No runs.</body></html>"
    mock = any(s["meta"]["mock"] for s in summaries)
    company = summaries[0]["meta"]["company"]
    banner = ("<div class='mock'><strong>Mock run.</strong> These numbers "
              "exercise the pipeline with deterministic stand-ins. They are "
              "not findings and must not be cited or pasted into a draft."
              "</div>") if mock else ""

    dj = next((s for s in summaries if s["meta"]["condition"] == "dj"), None)
    dj_block = ""
    if dj:
        dist = dj.get("controlling_state_distribution", {})
        pills = "".join(f"<span class='pill'>{_e(k)} {v}</span>"
                        for k, v in sorted(dist.items()))
        dj_block = f"""
<h2>What the governed procedure actually did</h2>
<p class='note'>Controlling state is the auditable answer to "why this
outcome". These are counts over the run, read from the resolution artifacts,
not inferred from the decisions.</p>
<p style='margin-top:12px'>{pills}</p>
<p class='note'>Mean candidates consulted per case:
<strong>{dj.get('mean_candidates_consulted')}</strong> ·
escalated past tier 1: <strong>{_pct(dj.get('escalated_rate'))}</strong> ·
reached a human: <strong>{_pct(dj.get('human_review_rate'))}</strong></p>"""

    notes = summaries[0]["meta"].get("gold_note", "")
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>Benchmark — {_e(company)}</title><style>{CSS}</style></head><body>
<div class='wrap'>
  <header class='mast'><h1>Three conditions, one framework</h1>
  <span class='sub'>{_e(company)} · {_e(summaries[0]['meta']['run_at'][:16])}</span>
  </header>
  {banner}
  <p class='note'>All three conditions read the same extracted facts, the same
  engaged provisions and the same seeded jurisprudence from the same deployed
  container. Only the governance semantics differ, which is what makes this an
  ablation of the architecture rather than a comparison of prompts.</p>

  <p class='eyebrow'>Disposition agreement, 95% Wilson intervals</p>
  {_bars(summaries)}

  <h2>Fidelity to properties the architecture claims by construction</h2>
  <p class='note'>In the DJ condition A6 and A3 fidelity are mechanical and
  should read 100%. Anything less is a defect report, not a result. In the
  baselines they are behavioural, and the difference is the measurement.</p>
  {_fidelity_table(summaries)}

  <h2>Agreement by case class</h2>
  {_class_table(summaries)}
  {dj_block}

  <h2>Provenance</h2>
  <p class='note'>{_e(notes)}</p>
  <table><tr><th>Field</th><th>Value</th></tr>
  {"".join(f"<tr><td>{_e(k)}</td><td>{_e(v)}</td></tr>" for k, v in
           summaries[0]['meta'].items() if k != 'gold_note')}
  </table>
</div></body></html>"""
