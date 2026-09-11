#!/usr/bin/env python3
"""One line of Sect. 7 numbers from an executed database.

Reads only what the run wrote. Nothing here is asserted; every figure is a
query over the traces.
"""
import collections, json, sqlite3, sys

SEED = "select count(*) from precedent_record where case_id like 'SEED-%'"
RUN  = "select count(*) from precedent_record where case_id not like 'SEED-%'"


def main(db: str, label: str) -> None:
    c = sqlite3.connect(db)
    q = lambda s: c.execute(s).fetchone()[0]
    controlling, state = set(), collections.Counter()
    for (detail,) in c.execute("select detail from pr_disposition"):
        try:
            rows = json.loads(detail)
        except Exception:
            continue
        for r in rows or []:
            if not isinstance(r, dict):
                continue
            state[r.get("controlling_state")] += 1
            if r.get("controlling"):
                controlling.add(r.get("case_id"))
    candidates = sum(k * v for k, v in
                     c.execute("select candidates,count(*) from retrieval_log group by 1"))
    # The four intake routes, reported separately and summed against the
    # session count. Erratum E1: the chapters used to report "87 adjudicated /
    # 8 absolute / 6 amendment", which folds the no-provision route in with
    # the adjudicated one and moves phi — a hypothesis of Proposition 6 — by
    # eight percent. A split that does not sum is how that survived, so the
    # sum is asserted here rather than left to a reader.
    routes = collections.Counter()
    for (disp,) in c.execute(
            "select disposition from pr_session_current"):
        routes[disp] += 1
    sessions = q("select count(*) from pr_session")
    amendment = routes.get("routed_amendment", 0)
    no_provision = routes.get("proceed", 0) - _proceed_with_cases(c)
    absolute = routes.get("blocked_absolute", 0)
    adjudicated = sessions - amendment - no_provision - absolute
    assert amendment + no_provision + absolute + adjudicated == sessions, (
        "the four routes do not sum to the session count")

    consolidated = q("select count(*) from precedent_record"
                     " where admission_ground='consolidation'")
    classes = q("select count(*) from consolidation_class")
    members = q("select count(*) from consolidated_disposition")

    print("  %-16s store %2d = %2d seed + %2d stored | controlling %2d | bound %2d"
          " | distinguished %2d | tie %d | absolute %d | candidates %d"
          % (label, q("select count(*) from precedent_record"), q(SEED), q(RUN),
             len(controlling), state.get("bound", 0),
             state.get("none_all_distinguished", 0), state.get("none_tie", 0),
             state.get("absolute_short_circuit", 0), candidates))
    print("  %-16s routes %d = %d adjudicated + %d no-provision + %d absolute"
          " + %d amendment | consolidation: %d class(es), %d record(s),"
          " %d member(s) by citation"
          % ("", sessions, adjudicated, no_provision, absolute, amendment,
             classes, consolidated, members))


def _proceed_with_cases(c) -> int:
    """Sessions that proceeded WITH a case filed — adjudicated permits. The
    no-provision route is the complement: `proceed` with no case at all, which
    files nothing and enters no ledger."""
    return c.execute(
        "select count(*) from pr_session_current s"
        " where s.disposition='proceed'"
        "   and exists (select 1 from pr_case p"
        "               where p.session_id = s.session_id)").fetchone()[0]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: report.py <database> <label>")
    main(sys.argv[1], sys.argv[2])
