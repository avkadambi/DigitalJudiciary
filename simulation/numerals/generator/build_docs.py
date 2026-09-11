#!/usr/bin/env python3
"""Generate docs/INHERITANCE.md and docs/FEDERATION.md from the built artefacts."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
rb = json.load(open(os.path.join(ROOT, "constitution", "rulebook.json")))
inh = json.load(open(os.path.join(ROOT, "constitution", "inheritance.json")))
pa = json.load(open(os.path.join(ROOT, "constitution", "proposed_amendments.json")))["amendments"]
man = json.load(open(os.path.join(ROOT, "corpus", "manifest.json")))
divs = list(rb["divisions"])

L = ["# Inheritance — the enterprise constitution against the five division constitutions\n",
     f"Enterprise rulebook `{rb['rulebook_version']}`, {rb['counts']['provisions']} provisions, "
     f"{rb['counts']['absolute']} absolute, {rb['counts']['proposed_absolute']} proposed floors held ordinary. "
     "Rule: minimum harmonisation — a division may tighten, never loosen; an enterprise absolute is a floor in every division. "
     "Cells name the division provisions implementing each enterprise provision (`*` = absolute in the division). "
     "**tightened** = the division states a floor where the enterprise states an ordinary provision. "
     "**gap** = the enterprise provision applies and the division has no implementing provision; a draft amendment is filed. "
     "`n/a` = the enterprise provision is stated not to apply to that division.\n",
     "| enterprise | abs | " + " | ".join(divs) + " |", "|---|---|" + "---|" * len(divs)]
status = {(r["enterprise"], r["division"]): r for r in inh["rows"]}
for p in rb["provisions"]:
    cells = []
    for d in divs:
        r = status[(p["id"], d)]
        m = p["implemented_by"][d]
        if r["status"] == "not_applicable":
            cells.append("n/a")
        elif r["status"] == "gap":
            cells.append("**gap**")
        else:
            ids = ", ".join(x["id"] + ("*" if x["absolute"] else "") for x in m["provisions"])
            cells.append(ids + (" (tightened)" if r["status"] == "tightened" else ""))
    L.append(f"| {p['id']} {p['title'][:70]}{'…' if len(p['title']) > 70 else ''} | "
             f"{'**yes**' if p['absolute'] else ('proposed' if p['proposed_absolute'] else 'no')} | " + " | ".join(cells) + " |")
L.append("")
L.append(f"## Draft amendments filed by the enterprise ({len(pa)})\n")
L.append("None is applied. Under A3 the enterprise proposes and each division's lawmakers dispose.\n")
for a in pa:
    tg = "; ".join(f"{d}: {', '.join(ids) if ids else '(no provision)'}" for d, ids in a["targets"].items())
    L.append(f"- **{a['id']}** ({a['enterprise_provision']}) → {tg}. {a['finding']}")
open(os.path.join(ROOT, "docs", "INHERITANCE.md"), "w").write("\n".join(L) + "\n")

M = ["# The federated stream — what happened\n",
     f"Corpus {man['corpus_version']}, seed {man['generator_seed']}: {man['cases']:,} changes filed by five divisions against the "
     f"enterprise constitution and one shared store. Opening store {man['opening_store']} (one seeded holding per ordinary "
     f"provision per division, alternating permit and deny so that two divisions hold opposite views on every provision), "
     f"final store {man['final_store']}; {man['records_written_in_run']} records written in the run; "
     f"{man['bound_by_another_divisions_record']} cases controlled by a record another division wrote; "
     f"{man['like_case_pairs']} cross-division like-case pairs; {man['construction_anomalies']} construction anomalies.\n",
     "| category | cases | what it exercises |", "|---|---|---|"]
import sys
sys.path.insert(0, HERE)
import enterprise_vocab as V
for name, n, desc in V.CATEGORIES:
    M.append(f"| {name} | {man['categories'][name]} | {desc} |")
M.append("")
M.append("| route | cases |"); M.append("|---|---|")
for k, v in man["routes"].items():
    M.append(f"| {k} | {v} |")
M.append("")
M.append("| decision | cases |"); M.append("|---|---|")
for k, v in man["decisions"].items():
    M.append(f"| {k} | {v} |")
M.append("")
M.append("| division | cases filed |"); M.append("|---|---|")
for k, v in man["cases_per_division"].items():
    M.append(f"| {k} | {v} |")
open(os.path.join(ROOT, "docs", "FEDERATION.md"), "w").write("\n".join(M) + "\n")
print("docs written")
