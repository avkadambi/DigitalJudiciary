#!/usr/bin/env python3
"""Digital Judiciary — single-container entrypoint.

Boot order: schema -> bootstrap ceremony (idempotent) -> demo corpus (opt-in)
-> lifecycle sweep thread -> HTTP API. The only external dependency at runtime
is the AI service, and only when DJ_JUDGE_MODE=llm.

`DJ_DEMO=<company>` boots the container onto one of the converted Paper-3
case-study corpora instead of the default SC seed, and replays its scenarios
through the real inbound gateway so the container comes up with a populated
docket and a non-empty review queue. The corpus selection has to happen before
`app.bootstrap` is imported, because that module resolves the seed directory at
import time — hence the env work below sitting above the imports.
"""
import os
import sys

# Default to seeding every company. A container that comes up empty teaches
# nothing, and a single-company one silently hides the tenancy story — so the
# default is the fullest demo. DJ_DEMO=off opts out entirely.
_DEMO = os.environ.get("DJ_DEMO", "_all").strip()
if _DEMO.lower() in ("off", "none", "0", "false"):
    _DEMO = ""
if _DEMO:
    _pack = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "demo", "companies", _DEMO)
    if os.path.isdir(_pack):
        # The demo company's rulebook and jurisprudence ARE the seed; they are
        # enacted and admitted through the same ceremony as any other seed, so
        # the demo is not a special path through the Kernel.
        os.environ.setdefault("DJ_SEED_DIR", _pack)
    else:
        print(f"DJ_DEMO={_DEMO!r}: no such demo corpus in demo/companies",
              file=sys.stderr)

from app.platform.dj_config import load_and_apply, ConfigError  # noqa: E402
try:
    load_and_apply()
except ConfigError as e:
    print(e, file=sys.stderr)
    sys.exit(2)
from app import bootstrap, demo, httpapi          # noqa: E402


def main() -> None:
    svc = bootstrap.build_services()
    keys = bootstrap.bootstrap(svc)
    if keys:
        print("== bootstrap ceremony complete; founding principal keys ==")
        for pid, key in keys.items():
            print(f"   {pid:12s} {key}")
        print("   (store these; they are not shown again)")

    if _DEMO:
        result = demo.run(svc)
        if result.get("ran"):
            print(f"== demo corpus: {result['display_name']} — "
                  f"{result['cases']} scenarios replayed ==")
            for disp, n in sorted(result["dispositions"].items(),
                                  key=lambda kv: -kv[1]):
                print(f"   {disp:26s} {n:4d}")
            print(f"   {'open review tasks':26s} "
                  f"{result['open_reviews']:4d}   -> /review")
            if result["expectation_mismatches"]:
                print(f"   note: {len(result['expectation_mismatches'])}"
                      f" case(s) landed on a different disposition than the"
                      f" original engine recorded; see /v1/demo/status")
            print("   this is a synthetic case study, not production traffic")
        else:
            print(f"== demo corpus not replayed: {result.get('reason')} ==")

    svc.lifecycle.sweep_once()
    svc.lifecycle.start()
    # Job worker always starts; it is idle unless DJ_ASYNC_INBOUND=1 or
    # post-merge jobs are enqueued. Keeps one container process model.
    if getattr(svc, "worker_plane", None):
        svc.worker_plane.start()
    elif getattr(svc, "job_worker", None):
        svc.job_worker.start()

    # Optional outbound delivery reaper (failed GitHub checks/comments).
    _retry_stop = None
    if os.environ.get("DJ_OUTBOUND_RETRY", "1") != "0":
        import threading
        from app import outbound as _outbound
        _retry_stop = threading.Event()

        def _outbound_reaper():
            interval = float(os.environ.get("DJ_OUTBOUND_RETRY_S", "60"))
            while not _retry_stop.wait(interval):
                try:
                    _outbound.retry_failed()
                except Exception:
                    pass

        threading.Thread(target=_outbound_reaper, daemon=True,
                         name="dj-outbound-retry").start()

    from app.platform.config import load_config
    cfg = load_config()
    host, port = cfg.host, cfg.port
    print(f"digital-judiciary listening on {host}:{port}"
          f"  profile={cfg.profile}  judge={cfg.judge_mode}"
          f"  async_inbound={int(cfg.async_inbound)}"
          f"  db={cfg.db_path}")
    # A pid file, so tooling can stop this process without guessing from
    # `ps` output. Matching on a command line is unsafe: any shell whose own
    # arguments merely mention serve.py looks identical to the server.
    pidfile = os.path.join("/tmp", f"dj-serve-{port}.pid")
    try:
        with open(pidfile, "w") as fh:
            fh.write(f"{os.getpid()}\n{cfg.db_path}\n")
    except OSError:
        pidfile = None

    httpd = httpapi.serve(svc, host, port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        svc.lifecycle.stop()
        if _retry_stop is not None:
            _retry_stop.set()
        if getattr(svc, "worker_plane", None):
            svc.worker_plane.stop()
        elif getattr(svc, "job_worker", None):
            svc.job_worker.stop()
        httpd.shutdown()
        if pidfile:
            try:
                os.remove(pidfile)
            except OSError:
                pass
        sys.exit(0)


if __name__ == "__main__":
    main()
