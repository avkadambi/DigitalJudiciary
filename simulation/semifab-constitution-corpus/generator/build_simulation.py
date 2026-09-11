"""
Build the simulation read: docs/SIMULATION.md and docs/simulation.html.

SIMULATION.md is the plain-English account of the whole run — what the firm is,
how the run unfolded as the case base grew, what the adjudicator did with each
kind of change, a dozen worked examples read in full, and then a ledger listing
every one of the 5,000 code changes and how it was treated.

simulation.html is the same run, browsable: the store growing case by case, the
disposition mix, and a filterable ledger.

    python3 generator/build_docs.py        # first — this reads its output
    python3 generator/build_simulation.py
"""

import base64
import gzip
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))

import vocab      # noqa: E402
import engine     # noqa: E402

D = lambda *p: os.path.join(ROOT, *p)          # noqa: E731

ROUTE_EN = {
    "fresh_interpretation": "decided fresh",
    "fresh_interpretation_after_tie": "decided fresh after a tie",
    "bound_by_precedent": "bound by precedent",
    "consolidated_citation": "disposed by citation",
    "absolute_shortcircuit": "refused at the floor",
    "docketed_declined": "docketed — not charged",
    "docketed_null": "docketed — nothing engaged",
}
DEC_EN = {"permit": "permitted", "deny": "denied",
          "permit_conditional": "permitted with conditions"}


def load():
    rb = json.load(open(D("constitution", "rulebook.json")))
    params = json.load(open(D("constitution", "parameters.json")))
    pack = json.load(open(D("corpus", "cases.json")))
    seed = json.load(open(D("corpus", "store_seed_initial.json")))["records"]
    man = json.load(open(D("corpus", "manifest.json")))
    prov = {p["id"]: engine.Provision.from_dict(p) for p in rb["provisions"]}
    engine.load_roster(D("constitution", "organizations.json"))
    out = engine.replay(pack["cases"], seed, prov, params["theta"])
    return rb, params, pack, seed, man, prov, out


def rows_and_growth(pack, out, rb):
    prov_title = {p["id"]: p["title"] for p in rb["provisions"]}
    absolute = {p["id"] for p in rb["provisions"] if p["absolute"]}
    traces = {t["case"]: t for t in out["traces"]}
    rows, growth, _size = [], [], len(out["traces"]) and 0
    store_size = 0
    seed_n = len(out["store"]) - len(out["records_written"])
    store_size = seed_n
    for i, c in enumerate(pack["cases"]):
        t = traces[c["id"]]
        if t["admitted"]:
            store_size += 1
        if i % 25 == 0 or i == len(pack["cases"]) - 1:
            growth.append([i + 1, store_size])
        sc = c["scenario"]
        rows.append({
            "n": i + 1,
            "id": c["id"],
            "cat": c["category"],
            "ch": sc["change"],
            "kind": sc.get("change_kind", ""),
            "area": sc.get("area", ""),
            "svc": sc.get("service", ""),
            "p": c["rules"],
            "abs": any(p in absolute for p in c["rules"]),
            "d": t["decision"],
            "r": t["route"],
            "ctl": t["controlling"] if isinstance(t["controlling"], str) else None,
            "tie": t["controlling"] == "none_tie",
            "esc": t["escalated_to"],
            "st": bool(t["admitted"]),
            "au": c["author"]["kind"],
        })
    return rows, growth, prov_title


def phase_table(rows, k=5):
    n = len(rows)
    size = n // k
    out = []
    for i in range(k):
        chunk = rows[i * size: (i + 1) * size if i < k - 1 else n]
        bound = sum(1 for r in chunk if r["r"] == "bound_by_precedent")
        stored = sum(1 for r in chunk if r["st"])
        floor = sum(1 for r in chunk if r["r"] == "absolute_shortcircuit")
        out.append({"phase": i + 1,
                    "from": chunk[0]["n"], "to": chunk[-1]["n"],
                    "bound": bound, "stored": stored, "floor": floor,
                    "bound_pct": 100.0 * bound / len(chunk)})
    return out


WORKED = [
    ("A-routine", "an ordinary change that engages a provision and breaks nothing"),
    ("B-plain-deny", "an unarguable violation nobody contests"),
    ("C-precedent", "the case that makes this a judiciary: a prior decision controls"),
    ("E-distinguish", "the near-miss the system must refuse to follow"),
    ("D-ordering", "two prior decisions disagree and one ordering key decides"),
    ("F-absolute", "a floor: refused before any retrieval happens"),
    ("G-riskowner", "the automated tiers are exhausted and a named human accepts the risk"),
    ("H-control-plane", "a change to the rulebook itself, routed to an amendment"),
    ("K-tie", "two records tie on every key and the trail says so"),
    ("P-pressure", "the twin of a control case, carrying a pressure argument"),
    ("L-consolidated", "co-pending changes decided once and cited"),
    ("I-lapsed", "an expired acceptance is cited and must not be followed"),
]


def markdown(rb, params, pack, man, rows, growth, phases, prov_title):
    name = rb["name"]
    L = []
    A = L.append
    A(f"# {name} — the simulation, read end to end\n")
    A(f"Corpus {pack['corpus_version']} · rulebook {pack['rulebook_version']} · "
      f"{len(rows):,} proposed code changes · Apache-2.0 (code) + CC BY 4.0 (data)\n")
    A("## What this document is\n")
    A("This is the whole run in plain English. A simulated engineering "
      "organisation proposed five thousand code changes, one after another, and "
      "an adjudicator governed by a written constitution decided every one of "
      "them. Nothing here is an intention or a specification: every disposition "
      "below is what the reference engine actually did when the corpus was "
      "replayed, and the ledger at the end lists all five thousand changes with "
      "the answer each one got.\n")
    A("Read it as you would read a docket. The interesting part is not that the "
      "adjudicator said no to bad changes — a linter does that. It is that when "
      "a change was contested and resolved, the decision was written down, and "
      "the next materially identical change was **bound** by it.\n")
    A("## The firm and its constitution\n")
    A(rb["description"] + "\n")
    A(f"| | |\n| :--- | ---: |\n"
      f"| Provisions | {rb['counts']['provisions']} |\n"
      f"| — of them absolute | {rb['counts']['absolute']} |\n"
      f"| Provision families | {rb['counts']['families']} |\n"
      f"| Opening precedent records | {man['opening_store']} |\n"
      f"| Records written during the run | {man['records_written_in_run']} |\n"
      f"| Final store | {man['final_store']} |\n"
      f"| Retrieval threshold θ | {params['theta']} |\n")
    A("\n## The run in numbers\n")
    d = man["decisions"]; r = man["routes"]
    A("| The answer given | Changes |\n| :--- | ---: |")
    for k, v in sorted(d.items(), key=lambda x: -x[1]):
        A(f"| {DEC_EN.get(k,k)} | {v:,} |")
    A("\n| How the answer was reached | Changes |\n| :--- | ---: |")
    for k, v in sorted(r.items(), key=lambda x: -x[1]):
        A(f"| {ROUTE_EN.get(k,k)} | {v:,} |")
    A("")
    A("## How the run unfolded\n")
    A("The case base starts almost empty and grows only when a decision is "
      "contested and resolved above the first instance. That is the whole "
      "mechanism, and its consequence is visible in the run: early changes are "
      "mostly decided fresh, and later ones are increasingly decided by citing "
      "a decision the organisation already made.\n")
    A("| Fifth of the run | Changes | Bound by precedent | Share | New records | Refused at a floor |")
    A("| :--- | :--- | ---: | ---: | ---: | ---: |")
    for p in phases:
        A(f"| {p['phase']} | {p['from']:,}–{p['to']:,} | {p['bound']:,} | "
          f"{p['bound_pct']:.1f}% | {p['stored']:,} | {p['floor']:,} |")
    A("")
    first, last = phases[0], phases[-1]
    A(f"Precedent goes from **{first['bound_pct']:.1f}%** of changes in the first "
      f"fifth to **{last['bound_pct']:.1f}%** in the last. Nothing was tuned to "
      f"produce that: it is what contest-gated admission does to a stream of "
      f"changes over time.\n")
    A("## Twelve changes, read in full\n")
    A("One of each kind, taken from the run rather than chosen for effect — the "
      "first case of each category, whatever it happens to be.\n")
    by_cat = {}
    for row in rows:
        by_cat.setdefault(row["cat"], []).append(row)
    for cat, why in WORKED:
        got = by_cat.get(cat)
        if not got:
            continue
        row = got[0]
        A(f"### {row['id']} — *{row['ch']}*\n")
        A(f"**Why this kind of change is in the run.** {why.capitalize()}.\n")
        eng = ", ".join(f"`{p}`" for p in row["p"]) or "nothing"
        A(f"**What it touched.** The {row['svc'].split(':')[-1].replace('-',' ')} "
          f"in the {row['area']} area, filed by "
          f"{'an AI coding agent' if row['au']=='ai-agent' else 'a named engineer'}. "
          f"It engaged {eng}.\n")
        line = f"**What happened.** The change was {ROUTE_EN.get(row['r'], row['r'])}"
        if row["r"] not in ("absolute_shortcircuit", "docketed_declined", "docketed_null"):
            line += f" and {DEC_EN.get(row['d'], row['d'])}"
        if row["ctl"]:
            line += f", controlled by record `{row['ctl']}`"
        if row["tie"]:
            line += ", with the trail recording none(tie) rather than an absence of authority"
        if row["esc"] == "riskowner":
            line += "; escalation was exhausted and the named risk owner accepted the residual risk"
        line += (". The decision was written into the case base and binds later "
                 "materially identical changes." if row["st"]
                 else ". Nothing was stored: the decision is final and leaves no precedent.")
        A(line + "\n")
    A("## What happened to each kind of change\n")
    A("| Kind of change | Changes | Permitted | Denied | With conditions | Bound by precedent | Became precedent |")
    A("| :--- | ---: | ---: | ---: | ---: | ---: | ---: |")
    for cname, count, _desc in vocab.CATEGORIES:
        g = by_cat.get(cname, [])
        A(f"| {cname} | {len(g):,} | "
          f"{sum(1 for x in g if x['d']=='permit'):,} | "
          f"{sum(1 for x in g if x['d']=='deny'):,} | "
          f"{sum(1 for x in g if x['d']=='permit_conditional'):,} | "
          f"{sum(1 for x in g if x['r']=='bound_by_precedent'):,} | "
          f"{sum(1 for x in g if x['st']):,} |")
    A("")
    A("## The ledger — every change, and how it was treated\n")
    A("All five thousand, in the order they arrived. **Answer** is what the "
      "change got; **how** is the route that produced it; **controlling** names "
      "the record that decided it, where one did; **precedent** marks the "
      "changes whose decision entered the case base.\n")
    A("| # | Change | Engages | Answer | How | Controlling | Precedent |")
    A("| ---: | :--- | :--- | :--- | :--- | :--- | :-: |")
    for row in rows:
        ch = row["ch"].replace("|", "\\|")
        eng = " ".join(row["p"]) or "—"
        if row["abs"]:
            eng += " ⛔"
        ctl = row["ctl"] or ("none(tie)" if row["tie"] else "—")
        A(f"| {row['n']} | {ch} | {eng} | {DEC_EN.get(row['d'], row['d'])} | "
          f"{ROUTE_EN.get(row['r'], row['r'])} | {ctl} | {'●' if row['st'] else ''} |")
    A("")
    A("⛔ marks a change that engaged an absolute provision — a floor no officer "
      "of this organisation has the authority to waive.\n")
    A("## How to check any of this\n")
    A("```\npython3 harness/run_conformance.py     # 44 checks over the executed trace\n"
      "python3 harness/mutation_matrix.py     # evidence the checks can fail\n"
      "bash reproduce/run_all.sh              # rebuild everything, deterministically\n```\n")
    A("Every row above is produced by replaying the corpus through "
      "`harness/engine.py`. No row is copied from an authored expectation, so "
      "the ledger cannot drift from the corpus files.\n")
    return "\n".join(L)


def build():
    rb, params, pack, seed, man, prov, out = load()
    rows, growth, prov_title = rows_and_growth(pack, out, rb)
    phases = phase_table(rows)
    md = markdown(rb, params, pack, man, rows, growth, phases, prov_title)
    open(D("docs", "SIMULATION.md"), "w").write(md)

    payload = {
        "name": rb["name"], "version": pack["corpus_version"],
        "rulebook": pack["rulebook_version"],
        "counts": rb["counts"], "manifest": man,
        "growth": growth, "phases": phases,
        "categories": [{"name": n, "count": c, "desc": d} for n, c, d in vocab.CATEGORIES],
        "prov_title": prov_title,
        "rows": rows,
    }
    raw = json.dumps(payload, separators=(",", ":")).encode()
    enc = base64.b64encode(gzip.compress(raw, 9, mtime=0)).decode()
    head = open(os.path.join(HERE, "simulation", "head.html")).read()
    tail = open(os.path.join(HERE, "simulation", "tail.html")).read()
    page = head + '\n<script>window.__RUN__="' + enc + '";</script>\n' + tail
    open(D("docs", "simulation.html"), "w").write(page)
    print(f"docs/SIMULATION.md      {len(md):,} bytes")
    print(f"docs/simulation.html    {len(page):,} bytes ({len(raw):,} raw)")


if __name__ == "__main__":
    build()
