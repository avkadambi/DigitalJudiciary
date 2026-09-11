"""
Generate the human-readable side of the corpus:

  docs/CASE_CATALOG.md   every case explained in English, grouped by category
  docs/case_catalog.csv  the same, one row per case, for spreadsheets
  docs/COVERAGE.md       coverage of axioms, requirements, checks, provisions
  corpus/explorer_data.json  the compact payload the HTML explorer loads

Deterministic. Standard library only.

    python3 generator/build_docs.py
"""

from __future__ import annotations

import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))

import vocab  # noqa: E402

with open(os.path.join(ROOT, "constitution", "rulebook.json")) as fh:
    RULEBOOK = json.load(fh)
with open(os.path.join(ROOT, "corpus", "cases.json")) as fh:
    PACK = json.load(fh)
with open(os.path.join(ROOT, "corpus", "store_seed_initial.json")) as fh:
    SEED = json.load(fh)["records"]
with open(os.path.join(ROOT, "corpus", "manifest.json")) as fh:
    MANIFEST = json.load(fh)

PROV = {p["id"]: p for p in RULEBOOK["provisions"]}
CASES = PACK["cases"]
CAT_DESC = {n: d for n, _c, d in vocab.CATEGORIES}

ROUTE_EN = {
    "absolute_shortcircuit": "denied at once on an absolute provision, before any retrieval ran",
    "bound_by_precedent": "bound by a controlling record",
    "fresh_interpretation": "decided on a fresh reading of the rulebook",
    "fresh_interpretation_after_tie": "decided fresh after the ordering deadlocked",
    "consolidated_citation": "disposed by direct citation of a consolidation representative",
    "docketed_declined": "not charged, and docketed on the declined route",
    "docketed_null": "not charged, and docketed on the null route",
}

# Routes whose English already states the disposition; repeating it reads badly.
ROUTE_STATES_DECISION = {"absolute_shortcircuit", "docketed_declined", "docketed_null"}

DEC_EN = {
    "permit": "permitted",
    "deny": "denied",
    "permit_conditional": "permitted subject to conditions, with a mandatory expiry",
}


def _name(qualified: str) -> str:
    return qualified.split(":", 1)[1].replace("-", " ")


def humanise(name: str) -> str:
    return name.replace("_", " ")


def explain(c: dict) -> str:
    sc = c["scenario"]
    e = c["expect"]
    provs = [PROV[p] for p in c["rules"]]
    role = sc["role"].replace("-", " ")
    article = "An" if role[0] in "aeiou" else "A"
    author = ("An AI coding agent" if c["author"]["kind"] == "ai-agent"
              else f"{article} {role}")
    service = _name(sc["service"])

    if provs:
        plist = "; ".join(
            f"{p['id']} ({p['title'].rstrip('.').lower()})"
            + (" — an absolute provision" if p["absolute"]
               else f" — {p['status']}, not in force" if p.get("status", "in_force") != "in_force"
               else "")
            for p in provs)
        engaged = f"The change engages {plist}."
    else:
        engaged = ("The evaluator finds no provision engaged at all, which is the "
                   "null route of the docket.")

    # Name the decisive factor first: it is what a reader needs, and burying it in
    # an alphabetical list is how a case file becomes unreadable.
    decisive = []
    for p in provs:
        for f in p["factors"]["violate"]:
            if f in c["facts"]:
                decisive.append(f)
    facts = [f for f in c["facts"] if not f.startswith("ctx_observation_")]
    rest = [f for f in facts if f not in decisive]
    if decisive:
        dline = ("The decisive fact is " if len(decisive) == 1 else "The decisive facts are ") + \
                ", ".join(f"`{f}`" for f in decisive) + ". "
    else:
        dline = ""
    shown = ", ".join(f"`{f}`" for f in rest[:3])
    hidden = len(rest) - 3
    more = (f" and {hidden} further factor" + ("s" if hidden != 1 else "")) if hidden > 0 else ""
    if rest:
        factline = (f"{dline}The case records {len(c['facts'])} facts in all, among them "
                    f"{shown}{more}.")
    elif decisive:
        factline = f"{dline}The case records {len(c['facts'])} facts in all."
    else:
        factline = "The case records only contextual observations."

    intent = c["meta"].get("intent", "")

    if e["route"] in ROUTE_STATES_DECISION:
        outcome = [f"Executed: the case is {ROUTE_EN.get(e['route'], e['route'])}."]
    else:
        outcome = [f"Executed: the case is {ROUTE_EN.get(e['route'], e['route'])} and "
                   f"{DEC_EN.get(e['final_decision'], e['final_decision'])}."]
    if e["controlling"] and e["controlling"] != "none_tie":
        outcome.append(f"The controlling record is {e['controlling']}.")
    elif e["controlling"] == "none_tie":
        outcome.append("Two survivors tie on every ordering key, so the trail records "
                       "none(tie) rather than an absence of authority.")
    if e["keys_applied"]:
        outcome.append("The ordering separated them on " +
                       ", ".join(e["keys_applied"]) + ".")
    if e["consulted"]:
        outcome.append(f"{len(e['consulted'])} record(s) were consulted and "
                       f"{len(e['distinguished'])} fell at the distinguishing gate.")
    if e["escalated_to"] == "riskowner":
        outcome.append("Escalation was exhausted, so the risk owner accepted the "
                       "residual risk; the acceptance carries an expiry and emits a "
                       "referral to the lawmakers.")
    elif e["escalated_to"]:
        outcome.append(f"The decision was contested to {e['escalated_to']}.")
    if e.get("draft_amendment"):
        outcome.append("Because the change targets the rulebook, the only route is a "
                       "draft amendment.")
    if e["admitted"]:
        ground = ("clause (i), contested and resolved above first instance"
                  if e["admission_ground"] == "clause_i"
                  else "clause (ii), as the representative of a consolidation class")
        outcome.append(f"The case is admitted to the store under {ground}, as "
                       f"{e.get('record_written', 'a new record')}.")
    elif e["route"] in ("docketed_declined", "docketed_null"):
        outcome.append("The arrival is docketed rather than adjudicated, so nothing "
                       "enters the store and no rationale trail is owed.")
    else:
        outcome.append("Nothing is admitted to the store: the decision is final but "
                       "leaves no precedent behind.")
    if e.get("cites_representative"):
        outcome.append(f"It cites the class representative {e['cites_representative']}.")
    if e["rating"] is not None:
        outcome.append(f"The prosecutor rated it {e['rating']} against a "
                       f"constitutional threshold of {e['tau']}.")

    checks = ", ".join(c["asserts"])
    reqs = ", ".join(c["requirements"])

    if sc.get("floor_facing"):
        crit = (" — a service inside the cardholder-data or financial-reporting "
                "boundary" if sc.get("service_is_critical") else "")
        subject = (f"{crit}, on the {sc['rail']} rail with "
                   f"{_name(sc['counterparty'])}")
    else:
        subject = f", with {_name(sc['counterparty'])} as the counterparty of record"
    return (
        f"**{c['id']}** — *{sc['change']}*\n\n"
        f"{author} files it against the {service} in the {sc['area']} area"
        f"{subject}, {sc['region']}. {engaged} {factline}\n\n"
        f"*Why this case exists:* {intent}.\n\n"
        f"*What happens:* {' '.join(outcome)}\n\n"
        f"*Exercises:* {checks}. *Requirements touched:* {reqs}.\n"
    )


def build_catalog():
    by_cat = {}
    for c in CASES:
        by_cat.setdefault(c["category"], []).append(c)

    out = [
        "# Meridian Financial Constitution Corpus — Case Catalog\n",
        f"Corpus version {PACK['corpus_version']}, rulebook {PACK['rulebook_version']}. "
        f"{len(CASES):,} cases in {len(by_cat)} categories.\n",
        "Every case below is explained in English: what the change is, why the case "
        "exists in the corpus, what the reference engine actually did with it, and "
        "which conformance checks and programme requirements it exercises. The "
        "'what happens' paragraph is generated from the executed trace, not from an "
        "authored expectation, so it cannot drift from the corpus files.\n",
        "## Contents\n",
    ]
    for name, count, desc in vocab.CATEGORIES:
        anchor = name.lower().replace(" ", "-")
        out.append(f"- [{name}](#{anchor}) — {count} cases. {desc}")
    out.append("")

    for name, count, desc in vocab.CATEGORIES:
        out.append(f"\n## {name}\n")
        out.append(f"*{desc}* — {count} cases.\n")
        for c in by_cat.get(name, []):
            out.append(explain(c))
            out.append("---\n")

    path = os.path.join(ROOT, "docs", "CASE_CATALOG.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write("\n".join(out))
    return path


def build_csv():
    path = os.path.join(ROOT, "docs", "case_catalog.csv")
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow([
            "case_id", "category", "provisions", "provision_status", "provision_origin", "absolute_engaged", "author",
            "region", "service", "decision", "route", "controlling",
            "keys_applied", "consulted", "distinguished", "escalated_to",
            "admitted", "admission_ground", "referral_emitted", "rating", "tau",
            "checks", "requirements", "explanation",
        ])
        for c in CASES:
            e = c["expect"]
            w.writerow([
                c["id"], c["category"], "|".join(c["rules"]),
                "|".join(sorted({PROV[p].get("status", "in_force") for p in c["rules"]})),
                "|".join(sorted({PROV[p].get("origin", "extension") for p in c["rules"]})),
                "yes" if any(PROV[p]["absolute"] for p in c["rules"]) else "no",
                c["author"]["kind"], c["scenario"]["region"], c["scenario"]["service"],
                e["final_decision"], e["route"], e["controlling"],
                "|".join(e["keys_applied"]), len(e["consulted"]), len(e["distinguished"]),
                e["escalated_to"] or "", e["admitted"], e["admission_ground"] or "",
                e["referral_emitted"], e["rating"] if e["rating"] is not None else "",
                e["tau"] if e["tau"] is not None else "",
                "|".join(c["asserts"]), "|".join(c["requirements"]),
                c["meta"].get("intent", "").replace("\n", " "),
            ])
    return path


def build_coverage():
    axiom_counts, check_counts, req_counts = {}, {}, {}
    prov_counts, family_counts, risk_counts = {}, {}, {}
    for c in CASES:
        for a in c["asserts"]:
            if a.startswith("A"):
                axiom_counts[a] = axiom_counts.get(a, 0) + 1
            else:
                check_counts[a] = check_counts.get(a, 0) + 1
        for r in c["requirements"]:
            req_counts[r] = req_counts.get(r, 0) + 1
        for p in c["rules"]:
            prov_counts[p] = prov_counts.get(p, 0) + 1
            family_counts[PROV[p]["family"]] = family_counts.get(PROV[p]["family"], 0) + 1
            risk_counts[PROV[p]["risk_framework"]] = risk_counts.get(PROV[p]["risk_framework"], 0) + 1

    lines = [
        "# Coverage report\n",
        f"Corpus {PACK['corpus_version']}. {len(CASES):,} cases, "
        f"{len(PROV)} provisions ({sum(1 for p in PROV.values() if p['absolute'])} absolute), "
        f"opening store {MANIFEST['opening_store']}, final store {MANIFEST['final_store']}.\n",
        "## Axioms of the architectural contract\n",
        "| Axiom | Name | Cases exercising it |",
        "| :---- | :---- | ----: |",
    ]
    for a, name in vocab.AXIOMS.items():
        lines.append(f"| {a} | {name} | {axiom_counts.get(a, 0):,} |")

    lines += ["", "## Requirements spine\n",
              "| Req | Statement | Cases touching it |", "| :---- | :---- | ----: |"]
    for r, name in vocab.REQUIREMENTS.items():
        lines.append(f"| {r} | {name} | {req_counts.get(r, 0):,} |")

    lines += ["", "## Conformance checks\n",
              "| Check | Cases exercising it |", "| :---- | ----: |"]
    for k in sorted(check_counts):
        lines.append(f"| {k} | {check_counts[k]:,} |")

    lines += ["", "## Provision families\n",
              "| Family | Title | Provisions | Cases |", "| :---- | :---- | ----: | ----: |"]
    for fam, meta in vocab.FAMILIES.items():
        n_prov = sum(1 for p in PROV.values() if p["family"] == fam)
        lines.append(f"| {fam} | {meta['title']} | {n_prov} | {family_counts.get(fam, 0):,} |")

    lines += ["", "## Risk-framework areas (FinTech risk architecture document)\n",
              "| Area | Cases |", "| :---- | ----: |"]
    for k in sorted(risk_counts):
        lines.append(f"| {k} | {risk_counts[k]:,} |")

    lines += ["", "## Routes taken\n", "| Route | Cases |", "| :---- | ----: |"]
    for k, v in sorted(MANIFEST["routes"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {ROUTE_EN.get(k, k)} | {v:,} |")

    status_counts = {}
    for c in CASES:
        for p in c["rules"]:
            st = PROV[p].get("status", "in_force")
            status_counts[st] = status_counts.get(st, 0) + 1
    lines += ["", "## Provision status\n",
              "A deferred provision is enacted but not yet applicable; a readiness "
              "provision states an architecture the firm must be able to meet when a "
              "suspended rule resumes; an advisory "
              "provision names suggested actions rather than obligations. None of the three may "
              "be marked absolute, and VC-04 checks it.\n",
              "| Status | Provisions | Cases engaging one |", "| :---- | ----: | ----: |"]
    for st in ("in_force", "deferred", "advisory", "readiness"):
        n = sum(1 for p in PROV.values() if p.get("status", "in_force") == st)
        lines.append(f"| {st} | {n} | {status_counts.get(st, 0):,} |")

    origin_counts = {}
    for c in CASES:
        for p in c["rules"]:
            o = PROV[p].get("origin", "extension")
            origin_counts[o] = origin_counts.get(o, 0) + 1
    lines += ["", "## Provision origin\n",
              "The thirty-seven provisions of the released Meridian Financial pack appear here with "
              "their text and absolute flags unchanged, so the 68 shipped cases remain "
              "valid against this constitution.\n",
              "| Origin | Provisions | Cases engaging one |", "| :---- | ----: | ----: |"]
    for o in ("shipped", "extension"):
        n = sum(1 for p in PROV.values() if p.get("origin", "extension") == o)
        lines.append(f"| {o} | {n} | {origin_counts.get(o, 0):,} |")

    lines += ["", "## Provisions never exercised\n"]
    unused = [p for p in PROV if p not in prov_counts]
    if unused:
        lines.append("The following provisions carry no case. They are reachable and "
                     "are left in the constitution deliberately, so that an adopter can "
                     "see what the corpus does not yet cover:\n")
        for p in unused:
            lines.append(f"- {p} — {PROV[p]['title']}")
    else:
        lines.append("None: every provision in the constitution carries at least one case.")

    lines.append("")
    path = os.path.join(ROOT, "docs", "COVERAGE.md")
    with open(path, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    return path


def build_explorer_data():
    rows = []
    for c in CASES:
        e = c["expect"]
        rows.append({
            "id": c["id"], "cat": c["category"], "p": c["rules"],
            "abs": any(PROV[p]["absolute"] for p in c["rules"]),
            "d": e["final_decision"], "r": e["route"],
            "ctl": e["controlling"], "k": e["keys_applied"],
            "nc": len(e["consulted"]), "nd": len(e["distinguished"]),
            "esc": e["escalated_to"], "adm": e["admitted"],
            "ag": e["admission_ground"], "au": c["author"]["kind"],
            "j": c["scenario"]["region"], "sp": c["scenario"]["service"],
            "ax": c["asserts"], "rq": c["requirements"],
            "st": sorted({PROV[p].get("status", "in_force") for p in c["rules"]}),
            "og": sorted({PROV[p].get("origin", "extension") for p in c["rules"]}),
            "why": c["meta"].get("intent", ""),
            "en": explain(c),
        })
    payload = {
        "version": PACK["corpus_version"],
        "manifest": {k: v for k, v in MANIFEST.items() if k != "sha256"},
        "categories": [{"name": n, "count": c, "desc": d} for n, c, d in vocab.CATEGORIES],
        "provisions": [{"id": p["id"], "title": p["title"], "absolute": p["absolute"],
                        "family": p["family"], "family_title": p["family_title"],
                        "citation": p["citation"], "risk": p["risk_framework"],
                        "status": p.get("status", "in_force"),
                        "origin": p.get("origin", "extension")}
                       for p in RULEBOOK["provisions"]],
        "axioms": vocab.AXIOMS, "requirements": vocab.REQUIREMENTS,
        "cases": rows,
    }
    path = os.path.join(ROOT, "corpus", "explorer_data.json")
    with open(path, "w") as fh:
        json.dump(payload, fh, separators=(",", ":"))
    return path


if __name__ == "__main__":
    for p in (build_catalog(), build_csv(), build_coverage(), build_explorer_data()):
        print(f"{os.path.relpath(p, ROOT):40s} {os.path.getsize(p):>12,} bytes")
# --- scenario extension (corpus 2.0.0) ---
