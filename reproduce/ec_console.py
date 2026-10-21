#!/usr/bin/env python3
"""
The EC console: two self-contained HTML pages per fast-track run, and an index.

    python3 reproduce/ec_console.py <run_dir> [--out <run_dir>/docs/]
    python3 reproduce/ec_console.py --all <results_root> [--jobs N]

A run directory is `<results_root>/<pack>/<arm>/seed-<n>/` as run_year.py writes
it (run.jsonl, summary.json, bench_log.json, glosses_final.json, registry.json,
store_final.json, manifest.json). For each run this writes

    <run_dir>/docs/ec_simulation.html   the year, browsable: title block, daily
                                        series, decision and reason mix, the tier
                                        table, and the ledger of every change
    <run_dir>/docs/ec_explorer.html     the change explorer: facets, full-text
                                        search, a per-change detail panel telling
                                        the story in order, and tabs for the token
                                        registry, the canon and the bench docket

and `--all` adds `<results_root>/index.html` linking every run. Both pages follow
the slow track's docs/simulation.html and docs/explorer.html (the head/tail
fragments under reproduce/ec_console/ are adapted copies of the pack generator's)
and keep their property: one file, no scripts or fonts fetched, works offline.
The payload is gzip+base64 in the page and rendered on demand, so a year run is
well under 3 MB per page.

Reads only. Nothing under simulation/ec/, prereg/ or tests/ is written; the
pages go under the run's own docs/ directory.
"""

from __future__ import annotations

import argparse
import base64
import collections
import datetime as _dt
import gzip
import html
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

from simulation.ec.examen import label_for          # noqa: E402  (read only)

HERE = os.path.join(REPO, "reproduce", "ec_console")
PACKS = {
    "vetpoc": "vetpoc-constitution-corpus",
    "semifab": "semifab-constitution-corpus",
    "frontierllm": "frontierllm-constitution-corpus",
    "dcvigil": "dcvigil-constitution-corpus",
    "meridian": "meridian-corpus",
}
ARMS = ("A", "B", "C", "D")
TIERS = ("T0", "T1", "T2", "T3")
STANDING_EXPIRY = 1000000000

# One ledger row is one compact JSON array; the page indexes it by these names.
COLS = [
    "i", "day", "seq", "case", "twin", "au", "cat", "eng", "drv", "lvl",
    "kind", "tgt", "addf", "reason", "wb", "ctx", "claim", "conf",
    "dec", "rc", "ventry", "vtier", "L1", "L2", "escf", "tok", "ev", "exe",
    "imp", "imptier", "impwhy", "ex", "lab", "dk", "dj", "t3", "cc", "cct", "pair", "bm",
]


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------


def read_json(path, default=None):
    try:
        with open(path) as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def read_text(path, default=""):
    try:
        with open(path) as fh:
            return fh.read().strip()
    except OSError:
        return default


def is_run_dir(d: str) -> bool:
    return (os.path.isfile(os.path.join(d, "run.jsonl"))
            and os.path.isfile(os.path.join(d, "manifest.json"))
            and os.path.isfile(os.path.join(d, "summary.json")))


def find_runs(root: str) -> list[str]:
    """Every complete run directory under a results root, in a stable order.
    A directory with a checkpoint.json is mid-run and skipped; a directory is
    listed once however it is reached."""
    seen, out = set(), []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        if "docs" in dirnames:
            dirnames.remove("docs")
        if "llm_cache" in dirnames:
            dirnames.remove("llm_cache")
        if "run.jsonl" in filenames and "manifest.json" in filenames and "summary.json" in filenames:
            if "checkpoint.json" in filenames:
                continue
            real = os.path.realpath(dirpath)
            if real in seen:
                continue
            seen.add(real)
            out.append(dirpath)
    return out


def pack_dir(pack: str) -> str | None:
    d = os.path.join(REPO, "simulation", PACKS.get(pack, pack))
    return d if os.path.isdir(d) else None


# ---------------------------------------------------------------------------
# Payload
# ---------------------------------------------------------------------------


def day_of(ts: int) -> int | None:
    return (ts - 1000) // 100 if ts >= 1100 else None


def build_payload(run_dir: str) -> dict:
    man = read_json(os.path.join(run_dir, "manifest.json"), {})
    summ = read_json(os.path.join(run_dir, "summary.json"), {})
    bench = read_json(os.path.join(run_dir, "bench_log.json"), {}) or {}
    glf = read_json(os.path.join(run_dir, "glosses_final.json"), {}) or {}
    reg = read_json(os.path.join(run_dir, "registry.json"), {}) or {}
    store = read_json(os.path.join(run_dir, "store_final.json"), {}) or {}
    pack = man.get("pack") or summ.get("pack") or ""
    arm = man.get("arm") or summ.get("arm") or ""
    pdir = pack_dir(pack)
    cases_json = read_json(os.path.join(pdir, "corpus", "cases.json"), {}) if pdir else {}
    canon_json = read_json(os.path.join(pdir, "constitution", "canon.json"), {}) if pdir else {}
    cases_by_id = {c["id"]: c for c in (cases_json.get("cases") or [])}
    cats = cases_json.get("categories") or {}
    cat_order = list(cats.keys()) if isinstance(cats, dict) else [
        (c.get("name") if isinstance(c, dict) else c[0]) for c in cats]

    # --- canon -------------------------------------------------------------
    canon = {}
    entries = canon_json.get("entries") or []
    if isinstance(entries, dict):
        entries = list(entries.values())
    for e in entries:
        g0 = e.get("gloss") or {}
        canon[e["id"]] = {
            "title": e.get("title", ""), "tier": e.get("tier"), "kind": e.get("kind"),
            "family": e.get("family"), "cls": e.get("act_class"), "office": e.get("office"),
            "vf": e.get("violate_factors") or [],
            "adm": g0.get("admitted_reasons") or [], "bound": g0.get("bound") or {},
            "ctx": g0.get("contexts") or [],
        }
    tiers = glf.get("tiers") or {}
    for eid, t in tiers.items():
        canon.setdefault(eid, {"title": "", "tier": t, "kind": "value" if "-VAL-" in eid else "provision",
                               "family": None, "cls": None, "office": None, "vf": [],
                               "adm": [], "bound": {}, "ctx": []})
        canon[eid]["tier"] = canon[eid].get("tier") or t
    for eid, g in (glf.get("glosses") or {}).items():
        if eid in canon:
            canon[eid]["final"] = {
                "version": g.get("version"), "holdings": g.get("holdings") or [],
                "nwc": g.get("no_waiver_classes") or [], "codified": bool(g.get("codified")),
                "adm": g.get("admitted_reasons") or [], "bound": g.get("bound") or {},
                "ctx": g.get("contexts") or [], "pri": g.get("priorities") or [],
            }
    tier_of = lambda eid: (canon.get(eid) or {}).get("tier")      # noqa: E731

    # --- bench docket ------------------------------------------------------
    hearings = {h["act_id"]: h for h in (bench.get("hearings") or [])}
    glosses = bench.get("glosses") or []
    gloss_by_act = {}
    for g in glosses:
        gloss_by_act.setdefault(g.get("act_id"), []).append(g)
    docket, docket_idx = [], {}
    days_done = int(summ.get("days") or man.get("days") or 0)
    for f in bench.get("filings") or []:
        h = hearings.get(f["act_id"])
        gl = gloss_by_act.get(f["act_id"]) or []
        status = "heard" if h else ("pending" if f.get("hear_day", 0) > days_done else "unheard")
        docket_idx[f["act_id"]] = len(docket)
        docket.append({
            "act": f["act_id"], "case": f.get("case_id"), "filed": f.get("day_filed"),
            "hear": f.get("hear_day"), "entry": f.get("entry"), "tier": f.get("tier"),
            "rc": f.get("reason_code"), "cto": f.get("contest_to"), "status": status,
            "holding": h.get("holding") if h else None, "route": h.get("route") if h else None,
            "record": h.get("record") if h else None, "internal": bool(h.get("internal")) if h else None,
            "gloss_day": gl[0].get("day") if gl else None,
        })

    # --- registry ----------------------------------------------------------
    consumed_by, revoked_on = {}, {}
    for ev in reg.get("events") or []:
        if ev.get("event") == "consume":
            consumed_by[ev["token"]] = (ev.get("act_id"), ev.get("day"))
        elif ev.get("event") == "revoke":
            revoked_on[ev["token"]] = ev.get("day")
    tokens = []
    for t in reg.get("tokens") or []:
        cb = consumed_by.get(t["id"])
        tokens.append([
            t["id"], t.get("office"), t.get("act_class"), t.get("scope"), t.get("issued_day"),
            None if t.get("expires_day", 0) >= STANDING_EXPIRY else t.get("expires_day"),
            bool(t.get("revoked")), bool(t.get("consumed")), bool(t.get("standing_emergency")),
            cb[0] if cb else None, cb[1] if cb else None, revoked_on.get(t["id"]),
            t.get("recorded_cause") or "",
        ])
    # tokens live at the end of each day
    live = [0] * (days_done + 2)
    for t in tokens:
        if t[8]:
            continue
        start = t[4] or 1
        end = min(t[5] if t[5] is not None else days_done, days_done)
        if t[7] and t[10] is not None:
            end = min(end, t[10] - 1)
        if t[6]:
            end = min(end, (t[11] - 1) if t[11] is not None else start - 1)
        for d in range(start, end + 1):
            if 1 <= d <= days_done:
                live[d] += 1

    # --- DJ store by day ---------------------------------------------------
    store_recs = store.get("records") or []
    seed_n = sum(1 for r in store_recs if (r.get("ts") or 0) < 1100)
    written_by_day = collections.Counter()
    for r in store_recs:
        d = day_of(r.get("ts") or 0)
        if d is not None:
            written_by_day[d] += 1

    # --- lines -------------------------------------------------------------
    facts_dict, facts_idx = [], {}

    def fidx(s):
        if s not in facts_idx:
            facts_idx[s] = len(facts_dict)
            facts_dict.append(s)
        return facts_idx[s]

    lines = []
    with open(os.path.join(run_dir, "run.jsonl")) as fh:
        for ln in fh:
            ln = ln.strip()
            if ln:
                lines.append(json.loads(ln))
    lines.sort(key=lambda r: (r.get("day", 0), r.get("seq", 0)))

    rows, by_act, case_ids = [], {}, set()
    for i, r in enumerate(lines):
        p, a, v = r["proposal"], r["proposal"]["act"], r["verdict"]
        ex = r.get("examen")
        lab = label_for(ex["reported_event"] if ex else None, ex.get("token_ref") if ex else None,
                        ex.get("narrative", "") if ex else "", v["event_type"], bool(r.get("executed")))
        dj = r.get("dj")
        djc = None
        if dj:
            djc = [dj.get("route"), dj.get("decision"), dj.get("controlling"), bool(dj.get("admitted")),
                   dj.get("admission_ground"), dj.get("escalated_to"), dj.get("record")]
        esc = r.get("escalation")
        dk = docket_idx.get(p["act_id"]) if esc else None
        if esc and dk is None:                      # filing missing from the log: keep the line's copy
            docket_idx[p["act_id"]] = len(docket)
            dk = len(docket)
            docket.append({"act": p["act_id"], "case": p["case_id"], "filed": esc.get("day_filed"),
                           "hear": esc.get("hear_day"), "entry": esc.get("entry"), "tier": esc.get("tier"),
                           "rc": esc.get("reason_code"), "cto": esc.get("contest_to"), "status": "unheard",
                           "holding": None, "route": None, "record": None, "internal": None, "gloss_day": None})
        by_act[p["act_id"]] = i
        case_ids.add(p["case_id"])
        rows.append([
            i, r["day"], r.get("seq", 0), p["case_id"], 1 if p.get("twin_of") else 0,
            "a" if p.get("author_kind") == "ai-agent" else "h", r.get("category"),
            list(p.get("engaged") or []), p.get("presented_driver"), p.get("driver_level"),
            a.get("kind"), a.get("target_entry"), fidx(a["added_factor"]) if a.get("added_factor") else None,
            a.get("stated_reason"), a.get("within_bound"), a.get("context"), a.get("token_claim"),
            bool(a.get("conflict")),
            v.get("decision"), v.get("reason_code"), v.get("entry"), v.get("tier"), v.get("L1"), v.get("L2"),
            bool(v.get("escalate")), v.get("token_used"), v.get("event_type"), bool(r.get("executed")),
            bool(r.get("impermissible")), r.get("impermissible_tier"), r.get("impermissible_why"),
            [ex.get("reported_event"), ex.get("stated_reason"), ex.get("token_ref"), ex.get("narrative")] if ex else None,
            lab, dk, djc, bool(r.get("t3_sampled")), bool(r.get("corpus_contested")), r.get("corpus_contest_to"),
            None, bool(r.get("believes_monitored")),
        ])
    # pair twins with their controls
    PAIR = COLS.index("pair")
    for i, r in enumerate(lines):
        tw = r["proposal"].get("twin_of")
        if tw and tw in by_act:
            j = by_act[tw]
            rows[i][PAIR] = j
            rows[j][PAIR] = i

    # --- cases (titles, scenario, facts) for every case in the run ------------
    cases = {}
    for cid in sorted(case_ids):
        c = cases_by_id.get(cid)
        if not c:
            cases[cid] = {"t": "", "f": []}
            continue
        sc = c.get("scenario") or {}
        cases[cid] = {
            "t": sc.get("change", ""), "cat": c.get("category"), "area": sc.get("area"),
            "svc": sc.get("service"), "ck": sc.get("change_kind"), "jur": sc.get("jurisdiction"),
            "rules": c.get("rules") or [], "cto": c.get("contest_to"),
            "intent": (c.get("meta") or {}).get("intent", ""),
            "f": [fidx(x) for x in (c.get("facts") or [])],
            "au": (c.get("author") or {}).get("id"),
        }

    # --- daily series ------------------------------------------------------
    by_day = []
    gl_cum, store_cum = 0, seed_n
    for d in summ.get("by_day") or []:
        day = d["day"]
        gl_cum += d.get("glosses_written", 0)
        store_cum += written_by_day.get(day, 0)
        lab = d.get("df_labels") or {}
        by_day.append([
            day, d.get("proposals", 0), d.get("executed", 0), d.get("blocked", 0), d.get("held", 0),
            d.get("escalations_filed", 0), d.get("heard", 0), gl_cum, live[day] if day < len(live) else 0,
            d.get("tokens_issued", 0), d.get("impermissible_proposed", 0), d.get("impermissible_executed", 0),
            d.get("twins", 0), d.get("t3_sampled", 0), store_cum,
            lab.get("discloses", 0), lab.get("silent", 0), lab.get("misrepresents", 0), lab.get("nothing_to_disclose", 0),
        ])

    # --- tier table --------------------------------------------------------
    tier_rows = {k: collections.Counter() for k in TIERS + ("VAL",)}
    DEC, RC, VT, IMP, IMPT, ENG, DK, KIND = (COLS.index(k) for k in
                                             ("dec", "rc", "vtier", "imp", "imptier", "eng", "dk", "kind"))
    for row in rows:
        keys = set()
        for eid in row[ENG]:
            t = tier_of(eid)
            if t:
                keys.add(t)
            if (canon.get(eid) or {}).get("kind") == "value":
                keys.add("VAL")
        for k in keys:
            tier_rows[k]["proposals"] += 1
        vt = row[VT]
        ve = row[COLS.index("ventry")]
        vkeys = set()
        if vt:
            vkeys.add(vt)
        if ve and (canon.get(ve) or {}).get("kind") == "value":
            vkeys.add("VAL")
        if row[IMP]:
            it = row[IMPT]
            tgt = row[COLS.index("tgt")]
            ikeys = {it} if it else set()
            if tgt and (canon.get(tgt) or {}).get("kind") == "value":
                ikeys.add("VAL")
            for k in ikeys:
                tier_rows[k]["impermissible"] += 1
        for k in vkeys:
            if row[DEC] == "block":
                tier_rows[k]["blocked"] += 1
            if row[DEC] == "hold":
                tier_rows[k]["held"] += 1
            if row[RC] == "t1_authorized":
                tier_rows[k]["authorized"] += 1
            if row[RC] in ("t2_departure_admitted", "t3_in_context"):
                tier_rows[k]["dep_allowed"] += 1
            if row[RC] in ("t2_departure_excluded_reason", "t2_departure_out_of_bound", "t3_out_of_context"):
                tier_rows[k]["dep_blocked"] += 1
            if row[RC] == "gloss_bar":
                tier_rows[k]["gloss_bar"] += 1
            if row[DK] is not None:
                tier_rows[k]["escalated"] += 1
    for g in glosses:
        t = tier_of(g.get("entry"))
        if t:
            tier_rows[t]["glossed"] += 1
        if (canon.get(g.get("entry")) or {}).get("kind") == "value":
            tier_rows["VAL"]["glossed"] += 1
    entry_counts = collections.Counter(canon[e]["tier"] for e in canon if canon[e].get("tier"))
    entry_counts["VAL"] = sum(1 for e in canon.values() if e.get("kind") == "value")

    dec_mix = collections.Counter(r[DEC] for r in rows)
    rc_mix = collections.Counter(r[RC] for r in rows)
    kind_mix = collections.Counter(r[KIND] for r in rows)

    rel = os.path.relpath(run_dir, REPO) if run_dir.startswith(REPO) else run_dir
    meta = {
        "pack": pack, "pack_display": cases_json.get("display_name") or pack,
        "pack_dir": PACKS.get(pack, pack), "corpus_version": cases_json.get("corpus_version"),
        "rulebook_version": cases_json.get("rulebook_version"),
        "arm": arm, "seed": man.get("seed", summ.get("seed")),
        "archetype": man.get("archetype") or summ.get("archetype"), "agent": man.get("agent") or summ.get("agent"),
        "mode": man.get("mode") or summ.get("mode"), "days": days_done,
        "canon_version": man.get("canon_version") or glf.get("canon_version"),
        "plan_hash": read_text(os.path.join(REPO, "prereg", "plan_hash.txt"), "unknown"),
        "digest": man.get("run_jsonl_sha256"), "engine_sha256": man.get("engine_sha256"),
        "engine_path": man.get("engine_path"), "constants": man.get("constants") or {},
        "run_dir": rel, "generated": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d"),
        "elapsed_s": summ.get("elapsed_s"), "bench_internal": bool((bench.get("bench") or {}).get("internal")),
        "seed_records": seed_n, "cat_order": cat_order,
    }
    return {
        "meta": meta, "totals": summ.get("totals") or {}, "cols": COLS, "rows": rows,
        "facts": facts_dict, "cases": cases, "canon": canon, "glosses": glosses,
        "codifications": bench.get("codifications") or [], "t3_samples": bench.get("t3_samples") or [],
        "docket": docket, "tokens": tokens, "offices": reg.get("offices") or {},
        "by_day": by_day, "tiers": {k: dict(v) for k, v in tier_rows.items()},
        "entry_counts": dict(entry_counts), "dec_mix": dict(dec_mix), "rc_mix": dict(rc_mix),
        "kind_mix": dict(kind_mix),
    }


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------


def encode(payload: dict) -> tuple[str, int]:
    raw = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return base64.b64encode(gzip.compress(raw, 9, mtime=0)).decode("ascii"), len(raw)


def fragment(name: str) -> str:
    with open(os.path.join(HERE, name)) as fh:
        return fh.read()


def write_page(kind: str, enc: str, out_path: str) -> int:
    head = fragment(f"{kind}_head.html")
    tail = fragment(f"{kind}_tail.html")
    page = ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n" + head +
            "</head><body>\n" + '<script>window.__EC__="' + enc + '";</script>\n' + tail + "\n</body></html>\n")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(page)
    return len(page.encode("utf-8"))


def results_root(run_dir: str) -> str:
    """The nearest ancestor that looks like a results root (holds run_config.json
    or timings.json), else the pack's grandparent: <root>/<pack>/<arm>/seed-n."""
    d = os.path.dirname(run_dir)
    for _ in range(6):
        if os.path.isfile(os.path.join(d, "run_config.json")) or os.path.isfile(os.path.join(d, "timings.json")):
            return d
        nxt = os.path.dirname(d)
        if nxt == d:
            break
        d = nxt
    return os.path.dirname(os.path.dirname(os.path.dirname(run_dir)))


def build_run(run_dir: str, out_dir: str | None = None, root: str | None = None) -> dict:
    t0 = time.time()
    run_dir = os.path.abspath(run_dir)
    out_dir = os.path.abspath(out_dir) if out_dir else os.path.join(run_dir, "docs")
    payload = build_payload(run_dir)
    root = os.path.abspath(root) if root else results_root(run_dir)
    payload["meta"]["index_href"] = os.path.relpath(os.path.join(root, "index.html"), out_dir).replace(os.sep, "/")
    sim_payload = {k: v for k, v in payload.items() if k not in ("facts", "tokens", "offices", "t3_samples")}
    # the ledger needs titles for search and display, not scenario text or facts
    sim_payload["cases"] = {k: {"t": v.get("t", ""), "cat": v.get("cat")} for k, v in payload["cases"].items()}
    sim_payload["canon"] = {k: {"title": v.get("title"), "tier": v.get("tier"), "kind": v.get("kind")}
                            for k, v in payload["canon"].items()}
    enc_sim, raw_sim = encode(sim_payload)
    enc_exp, raw_exp = encode(payload)
    n_sim = write_page("simulation", enc_sim, os.path.join(out_dir, "ec_simulation.html"))
    n_exp = write_page("explorer", enc_exp, os.path.join(out_dir, "ec_explorer.html"))
    m = payload["meta"]
    return {
        "run_dir": run_dir, "out_dir": out_dir, "pack": m["pack"], "arm": m["arm"], "seed": m["seed"],
        "archetype": m["archetype"], "agent": m["agent"], "mode": m["mode"], "days": m["days"],
        "proposals": len(payload["rows"]), "totals": payload["totals"],
        "sizes": {"ec_simulation.html": n_sim, "ec_explorer.html": n_exp, "raw_sim": raw_sim, "raw_exp": raw_exp},
        "elapsed_s": round(time.time() - t0, 2),
    }


def _build_one(args):
    run_dir, out_dir, root = args
    try:
        return build_run(run_dir, out_dir, root)
    except Exception as e:                      # one bad run must not stop the sweep
        return {"run_dir": run_dir, "error": f"{type(e).__name__}: {e}"}


# ---------------------------------------------------------------------------
# Index
# ---------------------------------------------------------------------------


def write_index(root: str, results: list[dict]) -> str:
    root = os.path.abspath(root)
    ok = [r for r in results if "error" not in r]
    bad = [r for r in results if "error" in r]

    def key(r):
        return (os.path.relpath(os.path.dirname(os.path.dirname(os.path.dirname(r["run_dir"]))), root),
                r["archetype"] or "", r["pack"], r["arm"], int(r["seed"] or 0))
    ok.sort(key=key)
    groups = collections.OrderedDict()
    for r in ok:
        groups.setdefault(key(r)[0], []).append(r)
    total_bytes = sum(r["sizes"]["ec_simulation.html"] + r["sizes"]["ec_explorer.html"] for r in ok)
    L = []
    A = L.append
    A("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
      "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">")
    A("<title>EC Console Index</title>")
    A("<style>" + fragment("index.css") + "</style></head><body>")
    A("<header class=\"mast\"><div class=\"wrap\"><h1>The EC console — every run</h1>"
      f"<div class=\"sub\">{len(ok)} runs under <code>{html.escape(os.path.relpath(root, REPO))}</code>, "
      "each with its year (<i>ec_simulation</i>) and its change explorer (<i>ec_explorer</i>). "
      "Pack × arm × seed × archetype; arm A is the rival stack, B the Digital Judiciary alone, "
      "C the Enterprise Conscience alone, D both.</div>"
      f"<div class=\"imprint\"><span>Generated {_dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%d')}</span>"
      f"<span>{total_bytes/1e6:.1f} MB of pages</span><span>Plan hash "
      f"{html.escape(read_text(os.path.join(REPO, 'prereg', 'plan_hash.txt'), 'unknown')[:16])}…</span></div></div></header>")
    A("<main class=\"wrap\">")
    A("<div class=\"controls\"><input id=\"q\" type=\"search\" placeholder=\"Filter runs — pack, arm, seed, archetype…\" "
      "aria-label=\"Filter runs\"><span class=\"count\" id=\"cnt\"></span></div>")
    for g, rs in groups.items():
        A(f"<section><h2>{html.escape(g if g != '.' else os.path.basename(root))}</h2>")
        A("<div class=\"scroll\"><table class=\"ledger\"><thead><tr><th>Archetype</th><th>Pack</th><th>Arm</th>"
          "<th>Seed</th><th>Days</th><th>Proposals</th><th>Executed</th><th>Blocked</th><th>Held</th>"
          "<th>Escalations</th><th>Glosses</th><th>Imperm. executed</th><th>Pages</th></tr></thead><tbody>")
        for r in rs:
            t = r["totals"]
            rel = os.path.relpath(r["out_dir"], root)
            hay = f"{r['archetype']} {r['pack']} {r['arm']} seed-{r['seed']} {r['agent']} {r['mode']}"
            A(f"<tr data-hay=\"{html.escape(hay.lower())}\" data-arm=\"{r['arm'].lower()}\"><td>{html.escape(str(r['archetype']))}</td>"
              f"<td>{html.escape(r['pack'])}</td><td class=\"p\">{r['arm']}</td><td class=\"n\">{r['seed']}</td>"
              f"<td class=\"n\">{r['days']}</td><td class=\"n\">{r['proposals']:,}</td>"
              f"<td class=\"n\">{t.get('executed', 0):,}</td><td class=\"n\">{t.get('blocked', 0):,}</td>"
              f"<td class=\"n\">{t.get('held', 0):,}</td><td class=\"n\">{t.get('escalations_filed', 0):,}</td>"
              f"<td class=\"n\">{t.get('glosses_written', 0):,}</td><td class=\"n\">{t.get('impermissible_executed', 0):,}</td>"
              f"<td><a href=\"{html.escape(rel)}/ec_simulation.html\">year</a> · "
              f"<a href=\"{html.escape(rel)}/ec_explorer.html\">explorer</a></td></tr>")
        A("</tbody></table></div></section>")
    if bad:
        A("<section><h2>Not built</h2><ul>")
        for r in bad:
            A(f"<li><code>{html.escape(os.path.relpath(r['run_dir'], root))}</code> — {html.escape(r['error'])}</li>")
        A("</ul></section>")
    A("</main><footer><div class=\"wrap\">Pages are generated by <code>reproduce/ec_console.py</code> from each "
      "run's own files; nothing on them is authored. Code Apache-2.0; data CC BY 4.0.</div></footer>")
    A("<script>(function(){var q=document.getElementById('q'),rows=[].slice.call(document.querySelectorAll('tr[data-hay]')),"
      "c=document.getElementById('cnt');function f(){var t=q.value.trim().toLowerCase().split(/\\s+/).filter(Boolean),n=0;"
      "rows.forEach(function(r){var h=r.dataset.hay,ok=t.every(function(x){return x.length===1?r.dataset.arm===x:h.indexOf(x)>=0;});r.hidden=!ok;if(ok)n++;});"
      "c.textContent=n+' of '+rows.length+' runs';}"
      "q.addEventListener('input',f);f();})();</script></body></html>")
    path = os.path.join(root, "index.html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    return path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_dir", nargs="?", help="one run directory (<root>/<pack>/<arm>/seed-<n>/)")
    ap.add_argument("--out", help="output directory for the two pages (default <run_dir>/docs/)")
    ap.add_argument("--all", metavar="RESULTS_ROOT", help="build every run under this root and an index.html")
    ap.add_argument("--jobs", type=int, default=max(1, min(4, os.cpu_count() or 1)),
                    help="parallel workers for --all (default: CPUs, at most 4)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)
    if not a.all and not a.run_dir:
        ap.error("give a run directory or --all <results_root>")

    t0 = time.time()
    if a.all:
        root = os.path.abspath(a.all)
        runs = find_runs(root)
        if not runs:
            print(f"no complete runs under {root}", file=sys.stderr)
            return 1
        jobs = [(r, None, root) for r in runs]
        results = []
        if a.jobs > 1 and len(jobs) > 1:
            import multiprocessing as mp
            with mp.Pool(a.jobs) as pool:
                for res in pool.imap_unordered(_build_one, jobs):
                    results.append(res)
                    if not a.quiet:
                        _say(res, root)
        else:
            for j in jobs:
                res = _build_one(j)
                results.append(res)
                if not a.quiet:
                    _say(res, root)
        index = write_index(root, results)
        ok = [r for r in results if "error" not in r]
        total = sum(r["sizes"]["ec_simulation.html"] + r["sizes"]["ec_explorer.html"] for r in ok)
        print(f"{len(ok)} runs, {len(results) - len(ok)} failed, {total/1e6:.1f} MB of pages, "
              f"{time.time() - t0:.0f}s -> {os.path.relpath(index, REPO) if index.startswith(REPO) else index}")
        return 0 if len(ok) == len(results) else 1

    if not is_run_dir(a.run_dir):
        print(f"not a run directory (needs run.jsonl, summary.json, manifest.json): {a.run_dir}", file=sys.stderr)
        return 1
    res = build_run(a.run_dir, a.out)
    _say(res, None)
    return 0


def _say(res, root):
    if "error" in res:
        print(f"FAILED {res['run_dir']}: {res['error']}")
        return
    s = res["sizes"]
    rel = os.path.relpath(res["out_dir"], root or REPO)
    print(f"{rel}: ec_simulation.html {s['ec_simulation.html']:,} B ({s['raw_sim']:,} raw), "
          f"ec_explorer.html {s['ec_explorer.html']:,} B ({s['raw_exp']:,} raw), "
          f"{res['proposals']:,} proposals, {res['elapsed_s']}s")


if __name__ == "__main__":
    sys.exit(main())
