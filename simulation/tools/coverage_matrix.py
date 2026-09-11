#!/usr/bin/env python3
"""Cross-pack scenario coverage — computed from the executed corpora.

    python3 tools/coverage_matrix.py            # prints and writes SCENARIO_COVERAGE.md
    python3 tools/coverage_matrix.py --json     # machine-readable

For every scenario class in scenarios.json and every pack: which provisions map
to it (ordinary / absolute), and how many executed cases exercised it in each
mechanism (A compliant touch, B plain deny, F floor, P pressure twin, V like-
case, G risk-owner, W cross-jurisdiction, H control plane). Nothing here is
authored: the counts come from corpus/cases.json as built, through the same
harness/coverage.py that VC-50 runs. Every figure is ⟦measured⟧ on the corpus
named in the header; the requirement columns come from the catalogue.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
PACKS = [
    ("vetpoc", "vetpoc-constitution-corpus"),
    ("semifab", "semifab-constitution-corpus"),
    ("frontierllm", "frontierllm-constitution-corpus"),
    ("dcvigil", "dcvigil-constitution-corpus"),
    ("meridian", "meridian-corpus"),
]
MECH = ("A", "B", "F", "P", "V", "G", "W", "H")


def load_cov(pack_dir):
    spec = importlib.util.spec_from_file_location("coverage", os.path.join(pack_dir, "harness", "coverage.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(as_json=False):
    catalogue = json.load(open(os.path.join(SIM, "scenarios.json")))
    result = {"catalogue_version": catalogue["version"], "packs": {}}
    for key, d in PACKS:
        root = os.path.join(SIM, d)
        cov = load_cov(root)
        rb = json.load(open(os.path.join(root, "constitution", "rulebook.json")))
        pack = json.load(open(os.path.join(root, "corpus", "cases.json")))
        counts, applicable = cov.matrix(rb, pack["cases"], catalogue)
        gaps = cov.missing(rb, pack["cases"], catalogue)
        notes = cov.constitution_notes(rb, catalogue)
        result["packs"][key] = {
            "corpus_version": pack["corpus_version"], "cases": len(pack["cases"]),
            "provisions": len(rb["provisions"]),
            "absolute": sum(1 for p in rb["provisions"] if p["absolute"]),
            "scenarios": {s: {"provisions": sorted(applicable[s]["provisions"]),
                              "absolute": sorted(applicable[s]["absolute"]),
                              "counts": counts[s]} for s in applicable},
            "gaps": gaps, "notes": notes,
        }
    if as_json:
        print(json.dumps(result, indent=2))
        return 0

    lines = []
    lines.append("# Scenario coverage across the five packs\n")
    lines.append(f"Catalogue {catalogue['version']}; every count ⟦measured⟧ on the corpus version shown. "
                 "Cells are cases exercising the scenario in that mechanism: A compliant touch (guard), "
                 "B plain deny, F floor short-circuit, P pressure twin, V like-case, G risk-owner acceptance, "
                 "W cross-jurisdiction, H control plane. `·` = the scenario does not apply to the pack "
                 "(no provision maps to it). `req` lists the mechanisms the catalogue demands; VC-50 fails "
                 "on any demanded cell that is empty.\n")
    hdr = "| pack | corpus | cases | provisions | absolute | classes applicable | required cells empty |"
    lines.append(hdr)
    lines.append("|" + "---|" * 7)
    for key, _ in PACKS:
        r = result["packs"][key]
        lines.append(f"| {key} | {r['corpus_version']} | {r['cases']:,} | {r['provisions']} | {r['absolute']} | "
                     f"{len(r['scenarios'])} | {len(r['gaps'])} |")
    lines.append("")
    for s in catalogue["scenarios"]:
        sid = s["id"]
        lines.append(f"## {sid} — {s['title']}\n")
        lines.append(f"Harm classes: {', '.join(s['harm_classes'])}. Floor expected: {'yes' if s['floor'] else 'no'}. "
                     f"Required mechanisms: {' '.join(s['required_mechanisms'])}.\n")
        lines.append("| pack | provisions (abs) | " + " | ".join(MECH) + " |")
        lines.append("|---|---|" + "---|" * len(MECH))
        for key, _ in PACKS:
            r = result["packs"][key]
            sc = r["scenarios"].get(sid)
            if sc is None:
                lines.append(f"| {key} | · | " + " | ".join("·" for _ in MECH) + " |")
                continue
            cells = []
            for m in MECH:
                n = sc["counts"][m]
                req = m in s["required_mechanisms"]
                if req and m == "F" and not sc["absolute"]:
                    req = False
                if req and m in ("B", "G", "V") and not (set(sc["provisions"]) - set(sc["absolute"])):
                    req = False
                cells.append(f"**{n}**" if req else str(n))
            lines.append(f"| {key} | {len(sc['provisions'])} ({len(sc['absolute'])}) | " + " | ".join(cells) + " |")
        lines.append("")
    lines.append("## Constitution notes for the lawmakers\n")
    lines.append("Findings about the rulebooks, not the corpora: where the catalogue expects a floor and a pack "
                 "maps no absolute provision, or where a class has no ordinary limb. Each is a candidate draft "
                 "amendment; none is applied here (A3).\n")
    for key, _ in PACKS:
        for n in result["packs"][key]["notes"]:
            lines.append(f"- {key}: {n}")
    out = os.path.join(SIM, "SCENARIO_COVERAGE.md")
    open(out, "w").write("\n".join(lines) + "\n")
    # per-pack slice, shipped inside each pack so a single archive is self-describing
    for key, d in PACKS:
        r = result["packs"][key]
        pl = [f"# Scenario coverage — {key}\n",
              f"Corpus {r['corpus_version']}, {r['cases']:,} cases, {r['provisions']} provisions "
              f"({r['absolute']} absolute). Every count ⟦measured⟧ on the corpus as built; see "
              f"harness/coverage.py and VC-50. Bold = demanded by the catalogue.\n",
              "| scenario | provisions (abs) | " + " | ".join(MECH) + " |",
              "|---|---|" + "---|" * len(MECH)]
        for s in catalogue["scenarios"]:
            sc = r["scenarios"].get(s["id"])
            if sc is None:
                continue
            cells = []
            for m in MECH:
                n = sc["counts"][m]
                req = m in s["required_mechanisms"]
                if req and m == "F" and not sc["absolute"]:
                    req = False
                if req and m in ("B", "G", "V") and not (set(sc["provisions"]) - set(sc["absolute"])):
                    req = False
                cells.append(f"**{n}**" if req else str(n))
            pl.append(f"| {s['id']} {s['title']} | {len(sc['provisions'])} ({len(sc['absolute'])}) | " + " | ".join(cells) + " |")
        pl.append("")
        pl.append("Constitution notes for the lawmakers: " + ("; ".join(r["notes"]) if r["notes"] else "none") + ".")
        open(os.path.join(SIM, d, "docs", "SCENARIO_COVERAGE.md"), "w").write("\n".join(pl) + "\n")
    print("\n".join(lines[:12]))
    print(f"... written {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--json" in sys.argv))
