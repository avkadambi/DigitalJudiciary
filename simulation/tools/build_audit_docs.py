#!/usr/bin/env python3
"""Generate SCENARIO_INVENTORY.md and CONSTITUTION_AUDIT.md from the catalogue
and the five rulebooks as built. Nothing in the tables is typed by hand."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
PACKS = [
    ("vetpoc", "vetpoc-constitution-corpus", "VetPOC — veterinary practice management and point of care"),
    ("semifab", "semifab-constitution-corpus", "SemiFab — semiconductor fab monitoring and supply-chain control tower"),
    ("frontierllm", "frontierllm-constitution-corpus", "FrontierLLM — frontier model development and serving"),
    ("dcvigil", "dcvigil-constitution-corpus", "DCVigil — multi-tenant data-centre monitoring and AIOps"),
    ("meridian", "meridian-corpus", "Meridian Financial — payments, cards, ledger, lending, servicing"),
]

# Topics the survey raised that were deliberately NOT closed, with the reason.
NOT_CLOSED = {
    "vetpoc": [
        "HIPAA — correctly not applicable to veterinary records; no provision added.",
        "Pet-insurance claims interfaces and online-pharmacy fulfilment beyond prescription portability — no operative instrument beyond contract; left to a later survey.",
        "Compounding (503A/503B, GFI #256) beyond VP-VC-005 — FDA guidance status in flux; not asserted.",
    ],
    "semifab": [
        "Customs/HTS classification and import records — the pack's control tower does not model an import function; a later world extension.",
        "CFIUS/FIRRMA beyond the outbound-investment check in SF-SO-003 — inbound investment review is a corporate act, not a software change.",
        "Works-council consultation at the Dresden site — a process obligation with no repository artefact; VC-49 would reject it.",
        "Energy/water CSRD reporting — covered for the data-centre world (dcvigil EN); for the fab it is filed as a survey item, not a provision.",
    ],
    "frontierllm": [
        "DMCA takedown handling and output attribution for licensed corpora — a servicing process; only the training-side duties are provisions.",
        "Open-weight release as a distinct gate — FL-SF-001 and the new CB/WX floors gate deployment generally; a separate release gate is filed as a note.",
        "Energy reporting (EU AI Act Annex XI) — documentation content under FL-TR-002, not a separate provision.",
    ],
    "dcvigil": [
        "HIPAA/FedRAMP customer-specific regimes beyond the regime flags in CT — those bind the customer's deployment, not the vendor's change.",
        "EU AI Act Annex III(2) critical-infrastructure classification — deferred instrument; filed as a note rather than a deferred provision to avoid a second FL-GV-009-style placeholder.",
    ],
    "meridian": [
        "HMDA/Reg C, RESPA, flood insurance, §1071 small-business data — Meridian's lending area is unsecured consumer credit in the shipped pack; mortgage and small-business instruments would need a scenario vocabulary the pack does not carry.",
        "Tax information reporting (1099-INT/K, FATCA/CRS, TIN matching) — a reporting pipeline family is the next candidate; filed as a survey item.",
        "State money-transmitter licensing and state usury caps — licensing is corporate, and rate caps are a pricing-engine parameter already governed by MF-106's family; not separately provisioned.",
        "MiCA / stablecoin issuance — the VA family covers transfers of virtual assets; issuance is out of the shipped business model.",
    ],
}


def load():
    cat = json.load(open(os.path.join(SIM, "scenarios.json")))
    packs = {}
    for key, d, label in PACKS:
        root = os.path.join(SIM, d)
        rb = json.load(open(os.path.join(root, "constitution", "rulebook.json")))
        pa = json.load(open(os.path.join(root, "constitution", "proposed_amendments.json")))
        man = json.load(open(os.path.join(root, "corpus", "manifest.json")))
        packs[key] = {"label": label, "rulebook": rb, "amendments": pa["amendments"], "manifest": man}
    return cat, packs


INVENTORY_INTRO = """# The architect's scenario inventory

*What a constitution author would insist the simulation exercise, before trusting any of the
three arms — the Digital Judiciary, a monolithic per-case reasoner with no memory, or a priced
human review desk — with the software-development exception queue of a regulated firm.*

## Why an inventory, and why it is written as scenario classes rather than rules

A constitution is a list of provisions. A simulation is a stream of changes. The thing that
connects them — the reason a provision exists — is a scenario: a way the firm gets hurt, and
the mechanism by which the judiciary is supposed to stop it. An architect writing the
constitution wants to know, for every way the firm gets hurt, that the corpus makes the
architecture *show its work*: that a sanctions bypass hits the absolute floor before any model
is consulted (A6), that the same change filed twice gets the same answer with the same citation
(consistency), that a manager's say-so does not move a disposition (pressure invariance), that
a compliant change that merely *looks* like a violation is permitted (the guard item), that a
residual risk somebody may lawfully accept is accepted with an expiry and a referral (A7), and
that no one below the legislature can edit the threshold that decides any of it (A3).

So the unit of the inventory is the **scenario class**: a harm, its legal or reputational
anchor, the packs it applies to, whether the architect expects a **floor** (an absolute
provision — a claim about *who may decide*, never a severity tier), and the **mechanisms** in
which it must be exercised for the corpus to count as covering it. The classes are held in
`scenarios.json`; every provision in every pack carries the classes it instantiates; and
`harness/coverage.py` (conformance check VC-50) computes coverage from the executed corpus
rather than from anyone's assurance.

## The harm classes

**legal** — statutory or contractual liability (a fine, a suit, a voided contract).
**regulatory** — a supervisory obligation an examiner will test.
**reputational** — the headline, the viral complaint, the public-trust event: the chatbot that
advised a customer to break the law, the pet that died of a tenfold dose, the sanctions bypass on
the front page, the dark pattern that trends. These are the "public-relations nightmare" class
the constitution must reach even where the law is thin.
**safety** — life, health, animal welfare, physical plant.
**financial** — direct loss or a mis-statement.

A class usually carries more than one. Reputational harm is never modelled as a family of its
own: it is a tag on the provisions whose breach would produce the headline, so that the
coverage matrix can ask "how many reputational-class scenarios did the corpus exercise under
pressure?" without inventing a "PR" rulebook.

## The mechanisms, and what each one measures

| Letter | Category | What the architect learns from it |
| :-- | :-- | :-- |
| A | routine, compliant touch | The **guard item**: the change engages the scenario's provision and does nothing wrong. An arm that denies it is over-blocking. Every provision — every absolute included — receives at least one; touching a floor is not violating it (A6's conjunction). |
| B | plain deny | An ordinary provision violated; the author accepts the denial. Every titled violation factor in the constitution appears at least once. |
| F | absolute short-circuit | A floor violated: no retrieval, no precedent, no escalation. Every violation factor of every absolute appears at least once. |
| P | pressure twin | The immediately preceding compliant control, filed again with one of PACT's nine pressure mechanisms. The trace — disposition, route, controlling record, consulted set, stored status — must not move. Every provision, floors included, receives at least one twin. |
| V | like-case pair | The consistency endpoint: same material premise, different surface. Every provision anchors at least one pair. |
| G | risk-owner acceptance | Escalation exhausts the automated instances; a named officer accepts the residual risk with a mandatory expiry and a referral. Demanded only of classes with an ordinary limb — a floor cannot be accepted. |
| W | cross-jurisdiction | The same flow under two regimes. Reported for every class; guaranteed by the category, so not demanded per class. |
| H | control plane | A change to the rulebook itself, routed to a draft amendment under A3. Counted for every class: it is the scenario of governance evasion. |

The remaining seventeen categories (precedent, distinguishing, ordering, tie, lapse, renewal,
supersession, consolidation, standing, docket, reporter, acknowledgement, audit register,
cold start, adversarial, inexpressibility) are the architecture's own mechanics and are held
at identical composition in all five packs; the inventory does not re-derive them.

## What "covered" means, exactly

A scenario class is covered in a pack when every required mechanism has at least one executed
case whose first engaged provision maps to the class (for F, the absolute provision that
short-circuited). Where the catalogue expects a floor and a pack's constitution supplies no
absolute provision for the class, that is reported as a **constitution note for the
lawmakers** — a candidate draft amendment — and not as a corpus failure, because the corpus
cannot manufacture a floor the rulebook does not contain and must not pretend to.

## The classes
"""


def inventory(cat, packs):
    out = [INVENTORY_INTRO]
    for s in cat["scenarios"]:
        out.append(f"### {s['id']} — {s['title']}\n")
        out.append(f"{s['description']}\n")
        out.append(f"- Harm classes: {', '.join(s['harm_classes'])}")
        out.append(f"- Floor expected: {'yes' if s['floor'] else 'no'}; required mechanisms: {' '.join(s['required_mechanisms'])}")
        out.append(f"- Applies to: {', '.join(s['applies_to'])}")
        rows = []
        for key, _, _ in PACKS:
            rb = packs[key]["rulebook"]
            ps = [p for p in rb["provisions"] if s["id"] in (p.get("scenarios") or [])]
            if not ps:
                continue
            ab = [p["id"] for p in ps if p["absolute"]]
            oth = [p["id"] for p in ps if not p["absolute"]]
            rows.append(f"  - **{key}**: " + (f"absolute {', '.join(ab)}; " if ab else "") + (f"ordinary {', '.join(oth)}" if oth else ""))
        out.append("- Instantiated by:")
        out.extend(rows)
        out.append("")
    return "\n".join(out)


def audit(cat, packs):
    out = ["# Constitution audit — legal, compliance and reputational coverage\n",
           "Corpus 2.0.0. What each constitution lacked against the architect's inventory, what was added "
           "**by addition** (new families, `origin: extension`), what was **filed as a draft amendment** "
           "against existing provisions rather than edited (Axiom A3), and what remains open. Counts are "
           "read from the rulebooks as built.\n"]
    for key, _, label in PACKS:
        rb = packs[key]["rulebook"]
        c = rb["counts"]
        new = [p for p in rb["provisions"] if p["origin"] == "extension" and p["id"] in _ext_ids(key)]
        fams = {}
        for p in new:
            fams.setdefault(p["family"], []).append(p)
        out.append(f"## {label}\n")
        out.append(f"Provisions {c['provisions']} ({c['absolute']} absolute) across {c['families']} families; "
                   f"scenario extension added **{c.get('scenario_extension', len(new))}** provisions "
                   f"(**{c.get('scenario_extension_absolute', sum(1 for p in new if p['absolute']))}** absolute) "
                   f"in {len(fams)} new families. Status mix: in_force {c.get('in_force')}, deferred {c.get('deferred', 0)}, "
                   f"advisory {c.get('advisory', 0)}, readiness {c.get('readiness', 0)}. "
                   f"Draft amendments on file: {len(packs[key]['amendments'])}.\n")
        out.append("### New provisions\n")
        out.append("| id | abs | family | title | citation | scenarios | harm |")
        out.append("|---|---|---|---|---|---|---|")
        for fam, ps in fams.items():
            for p in ps:
                out.append(f"| {p['id']} | {'**yes**' if p['absolute'] else 'no'} | {fam} — {p['family_title']} | "
                           f"{p['title']} | {p['citation']} | {' '.join(p['scenarios'])} | {', '.join(p['harm_classes'])} |")
        out.append("")
        out.append("### Draft amendments filed against existing provisions (not applied)\n")
        for a in packs[key]["amendments"]:
            out.append(f"- **{a['id']}** → {', '.join(a['targets'])}: {a['finding'][:260].rstrip()}{'…' if len(a['finding']) > 260 else ''}")
        out.append("")
        out.append("### Deliberately not closed in this revision\n")
        for n in NOT_CLOSED.get(key, []):
            out.append(f"- {n}")
        out.append("")
    return "\n".join(out)


_EXT_CACHE = {}


def _ext_ids(key):
    if key in _EXT_CACHE:
        return _EXT_CACHE[key]
    d = dict((k, dd) for k, dd, _ in PACKS)[key]
    import importlib.util
    spec = importlib.util.spec_from_file_location("ext_vocab", os.path.join(SIM, d, "generator", "ext_vocab.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    _EXT_CACHE[key] = {p["id"] for p in m.PROVISIONS}
    return _EXT_CACHE[key]


def main():
    cat, packs = load()
    open(os.path.join(SIM, "SCENARIO_INVENTORY.md"), "w").write(inventory(cat, packs))
    open(os.path.join(SIM, "CONSTITUTION_AUDIT.md"), "w").write(audit(cat, packs))
    print("written SCENARIO_INVENTORY.md, CONSTITUTION_AUDIT.md")


if __name__ == "__main__":
    sys.exit(main())
