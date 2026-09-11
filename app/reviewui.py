"""L5 Human review screens — server-rendered HTML, stdlib only.

Design brief: the reader is a named risk owner, accountable, short on time,
about to put their name on a permanent record that carries a mandatory
expiry. The page is a **docket sheet**, not a dashboard: the caption, the
ladder that was climbed to get here, the record as it will be written, and
then the instrument they execute.

The one bold element is the tier ladder in the left rail — the exhaustion
proof of A4 made visible, each rung stamped with the contest-chain hash. It
is the only thing on the page that is allowed to be decorative-adjacent, and
it earns that because the order genuinely carries information: you cannot be
on this screen unless every rung below was actually contested.

Two deliberate refusals:
  * When Proposition 2 bars an acceptance, the accept control is not
    disabled — it is absent. A control that cannot lawfully be used should
    not be drawn.
  * The expiry sits inside the sentence the risk owner is signing, not in a
    field beside it, because A7 makes it constitutive of the act rather than
    metadata about it.
"""
from __future__ import annotations

import hmac
import html
import json
import urllib.parse
from datetime import date, datetime, timedelta
from hashlib import sha256 as _sha

from .kernel import CHAIN_KEY

CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --ink:#15171C; --paper:#FBFBFA; --rule:#DFDFDA; --mute:#6C7078;
  --oxblood:#7A1F2B; --amber:#9A6B08; --moss:#2F6B57; --wash:#F3F3F0;
  /* 5.5: the courtroom serif is gone. Plain language reads better in the
     same face as everything else the reader uses all day. --book is kept
     as a name so no rule below has to change. */
  --book:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,
         sans-serif;
  --sans:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,
         sans-serif;
  --mono:ui-monospace,"SF Mono","Cascadia Mono","Roboto Mono",Menlo,monospace;
}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);
     font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
h1,h2,h3{letter-spacing:-.012em}
a{color:var(--oxblood)}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px 96px}

/* masthead ---------------------------------------------------------- */
.mast{border-bottom:2px solid var(--ink);padding:22px 0 12px;margin-bottom:28px;
      display:flex;align-items:baseline;justify-content:space-between;gap:16px;
      flex-wrap:wrap}
.mast h1{font-family:var(--book);font-weight:400;font-size:25px;margin:0;
         letter-spacing:.005em}
.mast .sub{font-family:var(--mono);font-size:11px;letter-spacing:.14em;
           text-transform:uppercase;color:var(--mute)}

/* queue ------------------------------------------------------------- */
.queue{border-top:1px solid var(--rule)}
.row{display:grid;grid-template-columns:88px 1fr auto;gap:20px;
     padding:18px 0;border-bottom:1px solid var(--rule);align-items:baseline}
.row .pid{font-family:var(--mono);font-size:12px;color:var(--oxblood);
          letter-spacing:.04em}
.row h2{font-family:var(--book);font-weight:400;font-size:18px;margin:0 0 4px}
.row .meta{font-size:13px;color:var(--mute)}
.row .age{font-family:var(--mono);font-size:12px;color:var(--mute);
          white-space:nowrap}
.row a.open{font-family:var(--mono);font-size:12px;letter-spacing:.08em;
            text-transform:uppercase;text-decoration:none;border-bottom:1px
            solid var(--oxblood);padding-bottom:1px}

/* docket ------------------------------------------------------------ */
.docket{display:grid;grid-template-columns:236px 1fr;gap:48px}
.rail{border-right:1px solid var(--rule);padding-right:24px}
.caption dt{font-family:var(--mono);font-size:10px;letter-spacing:.12em;
            text-transform:uppercase;color:var(--mute);margin-top:14px}
.caption dd{margin:2px 0 0;font-family:var(--mono);font-size:12.5px;
            word-break:break-all}
.caption dd.plain{font-family:var(--sans);font-size:14px}

/* the signature: exhaustion ladder ---------------------------------- */
.ladder{margin:30px 0 0;padding:0;list-style:none;position:relative}
.ladder::before{content:"";position:absolute;left:5px;top:6px;bottom:14px;
                width:1px;background:var(--rule)}
.ladder li{position:relative;padding:0 0 18px 22px}
.ladder li::before{content:"";position:absolute;left:0;top:5px;width:11px;
                   height:11px;border:1px solid var(--ink);background:var(--paper)}
.ladder li.done::before{background:var(--ink)}
.ladder li.here::before{background:var(--oxblood);border-color:var(--oxblood);
                        box-shadow:0 0 0 3px rgba(122,31,43,.16)}
.ladder .t{font-size:13.5px;display:block}
.ladder .stamp{font-family:var(--mono);font-size:10.5px;color:var(--mute);
               display:block;margin-top:2px}

/* record ------------------------------------------------------------ */
.eyebrow{font-family:var(--mono);font-size:10px;letter-spacing:.14em;
         text-transform:uppercase;color:var(--mute);margin:34px 0 8px}
.eyebrow:first-child{margin-top:0}
.provision{font-family:var(--book);font-size:20px;line-height:1.42;margin:0}
.opinion{font-family:var(--book);font-size:17.5px;line-height:1.62;
         max-width:62ch;margin:0}
.facts{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:6px}
.facts li{font-family:var(--mono);font-size:12px;background:var(--wash);
          border:1px solid var(--rule);padding:3px 8px}
table.cand{width:100%;border-collapse:collapse;font-size:13.5px}
table.cand th{font-family:var(--mono);font-size:10px;letter-spacing:.1em;
              text-transform:uppercase;color:var(--mute);text-align:left;
              font-weight:400;padding:0 12px 6px 0;border-bottom:1px solid var(--rule)}
table.cand td{padding:8px 12px 8px 0;border-bottom:1px solid var(--rule);
              vertical-align:top;font-family:var(--mono);font-size:12.5px}
td.kept{color:var(--moss)}
td.dist{color:var(--mute);text-decoration:line-through}

/* banners ----------------------------------------------------------- */
.banner{border-left:3px solid var(--oxblood);background:#fbf4f4;padding:14px 18px;
        margin:26px 0}
.banner.warn{border-left-color:var(--amber);background:#fdf7ec}
.banner h3{font-family:var(--book);font-weight:400;font-size:17px;margin:0 0 4px}
.banner p{margin:0;font-size:14px}

/* instrument -------------------------------------------------------- */
.instrument{margin-top:40px;border-top:2px solid var(--ink);padding-top:24px}
.instrument h2{font-family:var(--book);font-weight:400;font-size:21px;
               margin:0 0 18px}
.sentence{font-family:var(--book);font-size:17.5px;line-height:2.1;
          max-width:62ch}
.sentence input[type=date]{font-family:var(--mono);font-size:14px;
          border:0;border-bottom:1px solid var(--ink);background:transparent;
          padding:2px 4px;color:var(--ink)}
textarea{width:100%;max-width:62ch;min-height:96px;font-family:var(--sans);
         font-size:14.5px;padding:10px 12px;border:1px solid var(--rule);
         background:#fff;color:var(--ink);resize:vertical}
label.fld{display:block;font-family:var(--mono);font-size:10px;
          letter-spacing:.12em;text-transform:uppercase;color:var(--mute);
          margin:20px 0 6px}
.actions{display:flex;gap:12px;margin-top:24px;flex-wrap:wrap}
button{font-family:var(--sans);font-size:14.5px;padding:11px 20px;border:1px
       solid var(--ink);background:var(--ink);color:var(--paper);cursor:pointer}
button.ghost{background:transparent;color:var(--ink)}
button:hover{opacity:.88}
a:focus-visible,button:focus-visible,input:focus-visible,
textarea:focus-visible{outline:2px solid var(--oxblood);outline-offset:2px}

/* the desks: one ledger, four questions ----------------------------- */
.desks{display:flex;gap:2px;border-bottom:1px solid var(--rule);
     margin:0 0 26px;flex-wrap:wrap}
.desks a{font-family:var(--mono);font-size:11px;letter-spacing:.1em;
     text-transform:uppercase;color:var(--mute);text-decoration:none;
     padding:9px 14px 9px 0;border-bottom:2px solid transparent;
     margin-bottom:-1px}
.desks a:hover{color:var(--ink)}
.desks a.on{color:var(--oxblood);border-bottom-color:var(--oxblood)}

/* the rulebook, for people who are not lawyers ---------------------- */
.desks.sub{margin:-14px 0 24px;border-bottom:0}
.desks.sub a{font-size:10.5px;padding:6px 14px 6px 0}
.clause{border-top:1px solid var(--rule);padding:20px 0 18px}
.clause.floor{border-left:3px solid var(--oxblood);padding-left:16px}
.clause.deny{border-left:3px solid var(--oxblood);padding-left:16px}
.clause.wait{border-left:3px solid var(--amber);padding-left:16px}
.clause .head{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;
     margin:0 0 8px}
.clause .head .pid{font-family:var(--mono);font-size:13px;color:var(--oxblood)}
.clause .src{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;
     text-transform:uppercase;border:1px solid var(--rule);padding:2px 7px;
     color:var(--mute)}
.clause .src.shared{color:var(--moss);border-color:var(--moss)}
.clause .src.override,.clause .src.floor{color:var(--oxblood);
     border-color:var(--oxblood)}
.clause .src.wait{color:var(--amber);border-color:var(--amber)}
.clause .formal{font-family:var(--book);font-size:17px;line-height:1.45;
     margin:0 0 10px}
.clause .human{font-size:14.5px;line-height:1.6;margin:0 0 8px;
     max-width:70ch;color:var(--ink)}
.clause .prov-meta{font-family:var(--mono);font-size:10.5px;color:var(--mute);
     margin:6px 0 0;letter-spacing:.04em}

/* activity: the statement ------------------------------------------- */
.reg.activity .r{grid-template-columns:10px 96px 132px minmax(0,1fr) 150px 96px}
.reg.activity .r .when{text-align:left}
.reg.activity .r .when .tm{display:block;color:var(--mute);font-size:10.5px}
.reg.activity .r .kind{font-family:var(--mono);font-size:10.5px;
     letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}
.reg.activity .r .org{font-family:var(--mono);font-size:10.5px;
     text-align:right;color:var(--mute)}
.reg.activity .r.head{border-bottom:1px solid var(--ink);padding:0 0 8px}
.reg.activity .r.head > *{font-family:var(--mono);font-size:9.5px;
     letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
.reg.activity .r.head .mark{border-left:0}
.reg.activity .r.deny .mark{border-left-color:var(--oxblood)}
.reg.activity .r.wait .mark{border-left-color:var(--amber)}
.reg.activity .r.law .mark{border-left-color:var(--ink)}
.filters{display:flex;gap:8px;align-items:center;flex-wrap:wrap;
     padding:16px 0 18px;border-bottom:1px solid var(--rule);margin:0 0 4px}
.filters input[type=search]{flex:1 1 260px;min-width:200px;margin:0}
.filters select{margin:0}
.filters button{margin:0}
.filters a.open{font-size:11px}

/* cost table -------------------------------------------------------- */
table.cost{width:100%;border-collapse:collapse;margin:0 0 8px}
table.cost th{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;
     text-transform:uppercase;color:var(--mute);text-align:right;
     padding:0 10px 8px 0;border-bottom:1px solid var(--ink);font-weight:400}
table.cost th:first-child{text-align:left}
table.cost td{padding:11px 10px 11px 0;border-bottom:1px solid var(--rule);
     font-size:14px}
table.cost td.t{font-family:var(--book);font-size:16px}
table.cost td.n{font-family:var(--mono);font-size:12.5px;text-align:right}
table.cost tr.human td{color:var(--oxblood)}
table.cost tr.human td.t{font-style:italic}

/* impact ------------------------------------------------------------ */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));
     gap:0;border-top:1px solid var(--rule);margin:0 0 2px}
.stat{padding:22px 22px 22px 0;border-bottom:1px solid var(--rule)}
.stat .n{font-family:var(--book);font-size:42px;line-height:1;display:block}
.stat.amber .n{color:var(--amber)}
.stat.oxblood .n{color:var(--oxblood)}
.stat .l{font-family:var(--mono);font-size:10px;letter-spacing:.12em;
     text-transform:uppercase;color:var(--mute);display:block;margin:8px 0 0}
.stat .m{font-size:13px;line-height:1.5;color:var(--ink);margin:10px 0 0;
     max-width:30ch}
.instrument.judicial{border-left:3px solid var(--oxblood);padding-left:18px}
.instrument h2 .ref{font-family:var(--mono);font-size:11px;color:var(--mute);
     font-weight:400;margin-left:8px}
.amend{border-top:1px solid var(--rule);margin:16px 0 0;padding:14px 0 4px}
.amend.deny{border-left:3px solid var(--oxblood);padding-left:14px}
.amend.wait{border-left:3px solid var(--amber);padding-left:14px}
table.diff{width:100%;border-collapse:collapse;margin:10px 0 8px}
table.diff th{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;
     text-transform:uppercase;color:var(--mute);text-align:left;
     padding:0 10px 6px 0;border-bottom:1px solid var(--rule);font-weight:400}
table.diff td{padding:8px 10px 8px 0;border-bottom:1px solid var(--rule);
     font-size:13px;vertical-align:top}
table.diff td.f{font-family:var(--mono);font-size:11px;color:var(--mute);
     width:110px}
table.diff td.was{color:var(--mute);text-decoration:line-through;width:38%}
table.diff td.now{color:var(--oxblood);width:38%}
.reg .r.clear .mark{border-left-color:var(--moss)}
.reg .r.open .mark{border-left-color:var(--amber)}
.reg .r.floor .mark,.reg .r.final .mark{border-left-color:var(--oxblood)}
.reg .r.waiting .mark{border-left-color:var(--amber)}
.reg .r.legislature .mark{border-left-color:var(--ink)}
.lane{font-family:var(--mono);font-size:10px;letter-spacing:.08em;
     text-transform:uppercase;border:1px solid var(--rule);padding:2px 7px;
     margin:6px 6px 0 0;display:inline-block;color:var(--oxblood)}
.lane.wait{color:var(--amber);border-style:dashed}

/* the register ------------------------------------------------------ */
.tally{display:flex;gap:28px;flex-wrap:wrap;border-bottom:1px solid var(--rule);
     padding:0 0 18px;margin:0 0 4px}
.tally div{display:flex;flex-direction:column;gap:2px}
.tally .k{font-family:var(--mono);font-size:10px;letter-spacing:.12em;
     text-transform:uppercase;color:var(--mute)}
.tally .v{font-family:var(--book);font-size:26px;line-height:1}
.tally .v.lapsed{color:var(--oxblood)}
.tally a{text-decoration:none;color:inherit;display:flex;flex-direction:column;
     gap:2px;padding:0 0 6px;border-bottom:2px solid transparent}
.tally a:hover .k{color:var(--ink)}
.tally a.on{border-bottom-color:var(--oxblood)}
.tally a.on .k{color:var(--oxblood)}
.scope{font-size:12.5px;color:var(--mute);margin:16px 0 0}
.scope a{color:var(--oxblood)}
.pager{display:flex;justify-content:space-between;align-items:baseline;
     padding:18px 0 0;font-family:var(--mono);font-size:11.5px}
.pager .count{color:var(--mute);letter-spacing:.06em}
.pager a{color:var(--oxblood);text-decoration:none;letter-spacing:.1em;
     text-transform:uppercase;border-bottom:1px solid var(--oxblood)}
.reg{border-top:0}
.reg .r{display:grid;grid-template-columns:10px 92px minmax(0,1fr) 150px 96px;
     gap:16px;padding:14px 0;border-bottom:1px solid var(--rule);
     align-items:baseline}
/* Every grid child must be allowed to shrink. Without min-width:0 a long
   identifier blows out of its track and prints on top of the next column. */
.reg .r > *{min-width:0;overflow-wrap:anywhere}
/* The change stream's first column is repo#number, not a provision id, so
   it needs materially more room than the register's. */
.reg.stream .r{grid-template-columns:10px 210px minmax(0,1fr) 132px 104px}
.reg.stream .r .pid{line-height:1.35}
.reg .r .mark{align-self:stretch;border-left:3px solid var(--moss)}
.reg .r.lapsed .mark{border-left-color:var(--oxblood)}
.reg .r.live-accept .mark{border-left-color:var(--amber)}
.reg .r .pid{font-family:var(--mono);font-size:12px;color:var(--oxblood)}
.reg .r .hold{font-family:var(--book);font-size:17px;margin:0 0 3px}
.reg .r .meta{font-size:12.5px;color:var(--mute)}
.reg .r .st{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;
     text-transform:uppercase;color:var(--mute)}
.reg .r .st.lapsed{color:var(--oxblood)}
.reg .r .st.accept{color:var(--amber)}
.reg .r .when{font-family:var(--mono);font-size:11.5px;color:var(--mute);
     text-align:right;white-space:nowrap}
.reg a.rec{text-decoration:none;color:inherit;display:block}
.reg a.rec:hover .hold{text-decoration:underline}

/* the lifecycle spine: what actually happened to this record -------- */
.spine{margin:26px 0 0;padding:0;list-style:none;position:relative}
.spine::before{content:"";position:absolute;left:5px;top:6px;bottom:12px;
     width:1px;background:var(--rule)}
.spine li{position:relative;padding:0 0 20px 22px}
.spine li::before{content:"";position:absolute;left:0;top:5px;width:11px;
     height:11px;border:1px solid var(--ink);background:var(--ink)}
.spine li.future::before{background:var(--paper);border-style:dashed}
.spine li.expiry::before{background:var(--amber);border-color:var(--amber)}
.spine li.lapse::before{background:var(--oxblood);border-color:var(--oxblood);
     box-shadow:0 0 0 3px rgba(122,31,43,.16)}
.spine .t{font-size:13.5px;display:block}
.spine .stamp{font-family:var(--mono);font-size:10.5px;color:var(--mute);
     display:block;margin-top:2px}

/* facts, with the ones the holding rests on marked ------------------ */
.facts li.mat{border-color:var(--ink);background:var(--paper);
     box-shadow:inset 2px 0 0 var(--oxblood)}
.legend{font-size:12.5px;color:var(--mute);margin:8px 0 0}

/* identity ---------------------------------------------------------- */
.who{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
.who .pid{font-family:var(--mono);font-size:12px;color:var(--ink)}
.who .branch{font-family:var(--mono);font-size:10px;letter-spacing:.1em;
     text-transform:uppercase;border:1px solid var(--rule);padding:2px 7px;
     color:var(--mute)}
.who .branch.power{color:var(--oxblood);border-color:var(--oxblood)}
.who .branch.tenant{border-style:dashed}
.who .branch.tenant.all{color:var(--moss);border-color:var(--moss)}
.who .switch select{font-family:var(--mono);font-size:10px;
     letter-spacing:.1em;text-transform:uppercase;color:var(--moss);
     background:var(--paper);border:1px dashed var(--moss);padding:2px 6px;
     border-radius:0}
.reg .r .org{font-family:var(--mono);font-size:10px;letter-spacing:.08em;
     text-transform:uppercase;color:var(--mute);display:block;margin-top:3px}
.who form{display:inline}
button.link{background:none;border:0;padding:0 0 1px;color:var(--oxblood);
     font-family:var(--mono);font-size:11px;letter-spacing:.08em;
     text-transform:uppercase;cursor:pointer;
     border-bottom:1px solid var(--oxblood)}
button.link:hover{opacity:.7}

/* the bench: who you may sign in as (development only) -------------- */
.bench{margin:14px 0 0}
.bench select{width:100%;font-family:var(--mono);font-size:12.5px;
     padding:9px 10px;border:1px solid var(--rule);background:var(--paper);
     border-radius:0;color:var(--ink)}
.bench optgroup{font-family:var(--sans);font-style:normal;font-weight:600}
.roster{border-top:1px solid var(--rule);margin-top:24px}
.roster .r{display:grid;grid-template-columns:1fr auto;gap:14px;
     align-items:baseline;padding:11px 0;border-bottom:1px solid var(--rule)}
.roster .r .n{font-family:var(--mono);font-size:12.5px}
.roster .r .b{font-family:var(--mono);font-size:10px;letter-spacing:.1em;
     text-transform:uppercase;color:var(--mute);display:block;margin-top:2px}
.roster .r .b.power{color:var(--oxblood)}
.devnote{font-family:var(--mono);font-size:10px;letter-spacing:.12em;
     text-transform:uppercase;color:var(--amber);margin:22px 0 4px}
.current{background:var(--wash);border:1px solid var(--rule);padding:12px 14px;
     margin:0 0 18px;font-size:13.5px}
.current .pid{font-family:var(--mono)}

/* login + empty ----------------------------------------------------- */
.card{max-width:420px;margin:64px auto;border:1px solid var(--rule);
      background:#fff;padding:28px}
.card h1{font-family:var(--book);font-weight:400;font-size:22px;margin:0 0 6px}
.card p{color:var(--mute);font-size:14px;margin:0 0 18px}
input[type=password]{width:100%;font-family:var(--mono);font-size:14px;
     padding:10px 12px;border:1px solid var(--rule);background:var(--paper)}
.empty{border:1px dashed var(--rule);padding:56px 32px;text-align:center;
       margin-top:8px}
.empty h2{font-family:var(--book);font-weight:400;font-size:20px;margin:0 0 6px}
.empty p{color:var(--mute);margin:0;font-size:14px}
.err{color:var(--oxblood);font-size:14px;margin:0 0 14px}
.verdict{font-family:var(--mono);font-size:11px;letter-spacing:.1em;
      text-transform:uppercase;color:var(--moss)}

@media (max-width:820px){
  .docket{grid-template-columns:1fr;gap:28px}
  .rail{border-right:0;border-bottom:1px solid var(--rule);padding:0 0 20px}
  .row{grid-template-columns:1fr;gap:6px}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}


/* status strip (added in 5.0) --------------------------------------- */
.status-strip{display:flex;gap:8px;flex-wrap:wrap;align-items:center;
     padding:10px 0 0;margin:0 0 6px}
.status-strip .pill{font-family:var(--mono);font-size:10px;letter-spacing:.1em;
     text-transform:uppercase;border:1px solid var(--rule);padding:3px 9px;
     color:var(--mute)}
.status-strip .pill.ok{color:var(--moss);border-color:var(--moss)}


/* found by EX-49: used in templates, never styled ------------------- */
button.secondary{background:var(--paper);color:var(--ink);
     border:1px solid var(--rule)}
button.secondary:hover{border-color:var(--ink)}
.or{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;
     text-transform:uppercase;color:var(--mute);margin:0 8px}
.foot{border-top:1px solid var(--rule);margin-top:36px;padding-top:14px;
     font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;
     color:var(--mute)}


/* rulebook: tags instead of forty repeated words --------------------- */
.clause .src.appeal{color:var(--moss);border-color:var(--moss)}
.clause .age{font-family:var(--mono);font-size:10px;color:var(--mute);
     margin-left:auto;letter-spacing:.04em}
.clause .age .warn{color:var(--amber)}
.clause .blocks{margin:10px 0 0;display:flex;gap:6px;flex-wrap:wrap;
     align-items:baseline}
.clause .blocks .lbl{font-family:var(--mono);font-size:9.5px;
     letter-spacing:.12em;text-transform:uppercase;color:var(--mute);
     margin-right:4px}
.trig{font-family:var(--mono);font-size:11.5px;border:1px solid var(--rule);
     padding:2px 8px;color:var(--ink);background:var(--wash)}
.clause.floor .trig{border-color:var(--oxblood);color:var(--oxblood)}
.legend-box{border:1px solid var(--rule);padding:14px 16px;margin:22px 0 26px;
     background:var(--wash)}
.legend-box p{margin:0 0 8px;font-size:13.5px;line-height:1.55;max-width:78ch}
.legend-box p:last-child{margin:0;color:var(--mute);font-size:12.5px}
.legend-box .src{margin-right:8px}


/* AI judge activity ------------------------------------------------- */
.qa{border-top:1px solid var(--rule);padding:16px 0 14px}
.qa.wait{border-left:3px solid var(--amber);padding-left:14px}
.qa.lapsed{border-left:3px solid var(--oxblood);padding-left:14px}
.qa-head{display:flex;gap:9px;align-items:baseline;flex-wrap:wrap;
     margin:0 0 9px}
.qa-head .pid{font-family:var(--mono);font-size:12.5px;color:var(--oxblood)}
.qa-head .when{font-family:var(--mono);font-size:10.5px;color:var(--mute);
     margin-left:auto}
.qa .ask,.qa .said{font-size:14.5px;line-height:1.55;margin:0 0 6px;
     max-width:78ch}
.qa .said{color:var(--ink)}
.qa .lbl{font-family:var(--mono);font-size:9.5px;letter-spacing:.12em;
     text-transform:uppercase;color:var(--mute);display:inline-block;
     min-width:74px}


/* per-role desk ----------------------------------------------------- */
.desks-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
     gap:0;border-top:1px solid var(--rule);margin:18px 0 0}
.deskcard{padding:22px 22px 20px 0;border-bottom:1px solid var(--rule)}
.deskcard .n{font-family:var(--book);font-size:40px;line-height:1;display:block}
.deskcard.amber .n{color:var(--amber)}
.deskcard.oxblood .n{color:var(--oxblood)}
.deskcard .l{font-family:var(--mono);font-size:10px;letter-spacing:.12em;
     text-transform:uppercase;color:var(--mute);display:block;margin:9px 0 0}
.deskcard .m{font-size:13px;line-height:1.55;margin:10px 0 12px;max-width:34ch}

/* Dark mode, carried over from 5.0. Appended last so it can
   only override the rules above — never remove them, which is
   how the layout blocks went missing in the first place. */
@media (prefers-color-scheme:dark){
  :root{
    --ink:#e8e8e4; --paper:#14161a; --rule:#2a2e36; --mute:#9aa0a8;
    --oxblood:#d4728a; --amber:#d4a85a; --moss:#6db89f; --wash:#1c1f26;
    --card:#1a1d24; --focus:#7ba3d4;
    --shadow:0 1px 2px rgba(0,0,0,.2),0 4px 16px rgba(0,0,0,.25);
  }
}


/* ================================================================== */
/* 5.5 - plain-language shell, touch targets, mobile approval flow.   */
/* Appended last so it may only refine the rules above, never remove  */
/* them. Every class here is either new or a restyle of a 5.4 class,  */
/* so screens whose markup was not rewritten inherit the theme.       */
/* ================================================================== */

/* --book is now a sans stack, so the old serif/sans contrast is gone.
   Weight and size carry the distinction instead. */
.provision,.opinion,.reg .r .hold,.clause .formal,.card h1,.empty h2,
.banner h3,.instrument h2,.mast h1,.deskcard .n,.stat .n,.tally .v,
table.cost td.t{font-family:var(--sans)}
.provision{font-weight:650;letter-spacing:-.012em}
.reg .r .hold{font-weight:600;font-size:16px}
.clause .formal{font-weight:600}
.instrument h2,.banner h3,.card h1,.empty h2{font-weight:650;
  letter-spacing:-.012em}
.stat .n,.deskcard .n,.tally .v{font-weight:600;letter-spacing:-.02em}

/* top bar ----------------------------------------------------------- */
.topbar{display:flex;align-items:center;gap:12px;padding:14px 0 12px;
  margin:0 0 4px;border-bottom:1px solid var(--rule);flex-wrap:wrap}
.topbar .brand{font-size:16px;font-weight:650;text-decoration:none;
  color:var(--ink);display:inline-flex;align-items:center;gap:9px}
.topbar .brand .mk{width:16px;height:16px;border:2.5px solid var(--oxblood);
  border-radius:5px}
.topbar .spacer{flex:1 1 auto}
.topbar select{font:inherit;font-size:13.5px;padding:7px 9px;
  border:1px solid var(--rule);border-radius:9px;background:#fff;
  color:var(--ink);max-width:190px;text-transform:none;letter-spacing:0}
.me{display:inline-flex;align-items:center;gap:9px;font-size:13.5px;
  color:var(--mute);flex-wrap:wrap}
.me strong{color:var(--ink);font-weight:600}
.me form{display:inline}
.pillrole{font-size:11.5px;border:1px solid var(--rule);border-radius:999px;
  padding:3px 10px;color:var(--mute);white-space:nowrap}
.pillrole.power{color:var(--oxblood);border-color:var(--oxblood)}
.me a,.me button.link{font-size:13px;letter-spacing:0;text-transform:none;
  font-family:var(--sans)}
.tabbar{display:none}
.crumb{font-size:13.5px;color:var(--mute);margin:16px 0 0}
.crumb a{text-decoration:none}

/* desks, restyled as pills ------------------------------------------ */
.desks{gap:4px;padding:4px 0 0}
.desks a{font-family:var(--sans);font-size:13.5px;letter-spacing:0;
  text-transform:none;padding:8px 12px;border-bottom:2px solid transparent;
  border-radius:8px 8px 0 0}
.desks a.on{font-weight:600}
.desks.sub a{font-size:13px;padding:7px 12px}

/* group heading ----------------------------------------------------- */
.grp{display:flex;align-items:center;gap:10px;margin:28px 0 12px}
.grp h2{font-size:15px;font-weight:650;margin:0;font-family:var(--sans);
  letter-spacing:-.008em}
.grp .n{font-size:11.5px;border:1px solid var(--rule);border-radius:999px;
  padding:2px 9px;color:var(--mute)}
.grp .n.hot{color:#fff;background:var(--oxblood);border-color:var(--oxblood)}
.grp .rule{flex:1;height:1px;background:var(--rule)}
.lede{font-size:15px;line-height:1.6;color:var(--mute);margin:6px 0 0;
  max-width:76ch;text-wrap:pretty}

/* one waiting decision ---------------------------------------------- */
.qcard{display:block;text-decoration:none;color:inherit;background:#fff;
  border:1px solid var(--rule);border-radius:12px;padding:16px 18px;
  margin:0 0 10px}
.qcard:hover{border-color:var(--ink)}
.qcard .top{display:flex;justify-content:space-between;gap:12px;
  align-items:baseline;flex-wrap:wrap;margin:0 0 6px}
.qcard .what{margin:0;font-size:17.5px;font-weight:650;
  font-family:var(--sans);text-wrap:pretty}
.qcard .src{font-family:var(--mono);font-size:12px;color:var(--mute)}
.qcard .why{margin:0;font-size:15px;line-height:1.55;max-width:76ch;
  text-wrap:pretty}
.qcard .foot2{display:flex;gap:8px;align-items:center;flex-wrap:wrap;
  margin:12px 0 0}
.age2{font-size:12.5px;color:var(--mute)}
.age2.old{color:var(--oxblood);font-weight:600}
.badge{font-size:11.5px;border-radius:999px;padding:3px 10px;
  border:1px solid var(--rule);color:var(--mute);white-space:nowrap}
.badge.hot{background:var(--oxblood);border-color:var(--oxblood);color:#fff}
.badge.warn{color:var(--amber);border-color:var(--amber)}
.badge.ok{color:var(--moss);border-color:var(--moss)}

/* controls ---------------------------------------------------------- */
.btn2{display:inline-flex;align-items:center;justify-content:center;gap:8px;
  min-height:44px;padding:11px 18px;border-radius:10px;font-size:15px;
  font-weight:550;font-family:var(--sans);text-decoration:none;cursor:pointer;
  border:1px solid var(--ink);background:var(--ink);color:var(--paper)}
.btn2:hover{opacity:.88}
.btn2.ghost{background:#fff;color:var(--ink);border-color:var(--rule)}
.btn2.ghost:hover{border-color:var(--ink);opacity:1}
/* Screens whose markup still uses a bare <button> or an .actions link get
   the same shape without a markup change. */
button{min-height:44px;border-radius:10px;font-size:15px;font-weight:550;
  padding:11px 18px}
button.link{min-height:0;border-radius:0;padding:0 0 1px;font-weight:400}
.actions a.open{display:inline-flex;align-items:center;justify-content:center;
  min-height:44px;padding:11px 18px;border:1px solid var(--rule);
  border-radius:10px;background:#fff;color:var(--ink);font-family:var(--sans);
  font-size:15px;font-weight:550;letter-spacing:0;text-transform:none;
  text-decoration:none}
.actions a.open:hover{border-color:var(--ink)}
textarea,input[type=password],input[type=date],input[type=search],
select{border-radius:9px}
textarea{font-size:15px}

/* the decision, one screen ------------------------------------------ */
.focus{max-width:840px}
.focus .q{font-size:28px;line-height:1.24;font-weight:650;margin:10px 0 18px;
  text-wrap:pretty;font-family:var(--sans);letter-spacing:-.018em}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:0 0 16px}
.panel{border:1px solid var(--rule);border-radius:12px;background:#fff;
  padding:16px 18px;margin:0 0 14px}
.panel h3{font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;
  color:var(--mute);font-weight:600;margin:0 0 8px;font-family:var(--sans)}
.panel p{margin:0;font-size:15px;line-height:1.55;text-wrap:pretty}
.panel .quote{font-size:16.5px;line-height:1.5}
.panel .src2{font-size:13px;color:var(--mute);margin-top:8px}
.two .panel{margin:0}
.trail2{display:flex;flex-wrap:wrap;gap:7px;align-items:center;
  font-size:13.5px}
.trail2 .s{border:1px solid var(--rule);border-radius:999px;padding:4px 11px;
  background:#fff}
.trail2 .s.off{color:var(--mute);border-style:dashed}
.trail2 .s.now{background:var(--oxblood);border-color:var(--oxblood);
  color:#fff}
.trail2 .arw{color:var(--mute)}

.instrument{border-top:1px solid var(--rule);margin-top:26px;padding-top:22px}
.instrument h2{font-size:19px;margin:0 0 14px}
.choice{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:12px 0 0;
  align-items:start}
.choice form{border:1px solid var(--rule);border-radius:12px;background:#fff;
  padding:18px;display:flex;flex-direction:column;gap:11px;margin:0}
.choice form.allow{border-color:var(--ink);border-width:1.5px}
.choice h3{margin:0;font-size:17.5px;font-weight:650;font-family:var(--sans)}
.choice .sub{margin:0;font-size:14px;line-height:1.5;color:var(--mute)}
.choice textarea{min-height:78px;max-width:none;margin:0}
.choice label.fld{margin:0;font-size:11px}
.choice .sentence{font-family:var(--sans);font-size:15px;line-height:1.9;
  max-width:none;margin:0}
.chips{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.chips label{font-size:14px;border:1px solid var(--rule);border-radius:999px;
  padding:0 15px;min-height:40px;display:inline-flex;align-items:center;
  cursor:pointer;background:#fff;margin:0;letter-spacing:0;
  text-transform:none;font-family:var(--sans);color:var(--ink)}
.chips input{position:absolute;width:1px;height:1px;opacity:0}
.chips label:has(input:checked){border-color:var(--ink);
  background:var(--wash);font-weight:600}
.note2{font-size:13px;color:var(--mute);margin:0;line-height:1.5}

/* how you get unblocked --------------------------------------------- */
.paths{display:flex;flex-direction:column;gap:12px;margin:14px 0 0}
.path{border:1px solid var(--rule);border-radius:12px;background:#fff;
  padding:16px 18px}
.path .h{display:flex;justify-content:space-between;gap:12px;
  align-items:baseline;flex-wrap:wrap}
.path h3{margin:0 0 6px;font-size:17px;font-weight:650;
  font-family:var(--sans)}
.path p{margin:0 0 10px;font-size:14.5px;line-height:1.55;max-width:74ch}
.path textarea{min-height:70px;max-width:none;margin:0 0 10px}
.path.none{border-color:var(--oxblood);background:rgba(122,31,43,.035)}
.path form{margin:0}

details.more{border:1px solid var(--rule);border-radius:12px;background:#fff;
  padding:12px 16px;margin:16px 0}
details.more > summary{cursor:pointer;font-size:14.5px;font-weight:600;
  list-style:none}
details.more > summary::-webkit-details-marker{display:none}
details.more .caption{margin:12px 0 0}

/* cards, banners and shells, rounded to match ----------------------- */
.card{border-radius:14px;max-width:460px;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.card p{color:var(--ink);font-size:14.5px;line-height:1.6}
.empty{border-radius:14px;padding:44px 28px}
.banner{border-radius:0 12px 12px 0;margin:20px 0}
.current{border-radius:11px}
.legend-box{border-radius:12px}
.status-strip .pill{border-radius:999px}
.clause{border-radius:0}
.deskcard,.stat{padding-right:22px}
.qa{padding:16px 0 14px}

/* mobile: bottom tab bar, single column, full-width actions --------- */
@media (max-width:760px){
  .wrap{padding:0 16px 32px}
  body{padding-bottom:74px}
  .desks{display:none}
  .desks.sub{display:flex;margin:14px 0 18px}
  .tabbar{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:30;
    background:var(--paper);border-top:1px solid var(--rule);
    padding:5px 4px calc(5px + env(safe-area-inset-bottom))}
  .tabbar a{flex:1;min-height:46px;display:flex;align-items:center;
    justify-content:center;text-align:center;text-decoration:none;
    color:var(--mute);font-size:11.5px;line-height:1.2;padding:6px 3px;
    border-radius:10px}
  .tabbar a.on{color:var(--oxblood);background:var(--wash);font-weight:600}
  .two,.choice{grid-template-columns:1fr}
  .focus .q{font-size:23px}
  .docket{grid-template-columns:1fr;gap:24px}
  .rail{border-right:0;padding-right:0}
  .actions{flex-direction:column}
  .actions button,.actions .btn2,.actions a.open{width:100%}
  .topbar{position:sticky;top:0;z-index:20;background:var(--paper)}
  .topbar select{max-width:130px}
  /* The register rows are fixed-track grids needing ~410px before content.
     On a phone the flexible track starves to zero and the holding prints on
     top of the next column, so they stack. Every screen built on .reg —
     ledger, changes, activity, the desk, clause-by-clause — is reachable
     from the tab bar, so all of them need this. */
  .reg .r,.reg.stream .r,.reg.activity .r{
    grid-template-columns:8px minmax(0,1fr);gap:6px 10px}
  .reg .r > *{grid-column:2}
  .reg .r > .mark{grid-column:1;grid-row:1/-1;align-self:stretch}
  .reg .r .when,.reg .r .st,.reg.activity .r .org,
  .reg.activity .r .when{text-align:left}
  .reg.activity .r.head{display:none}
  .tally{gap:18px}
  .stats,.desks-grid{grid-template-columns:1fr}
  .qa-head .when{margin-left:0}
  .clause .age{margin-left:0}
  .filters{gap:8px}
  .filters input[type=search],.filters select,.filters button{
    flex:1 1 100%;width:100%}
  table.cost,table.diff,table.cand{font-size:13px}
  table.cost th,table.cost td{padding-right:6px}
  .card{margin:20px auto}
}
@media (prefers-color-scheme:dark){
  .qcard,.panel,.choice form,.path,details.more,.topbar select,
  .chips label,.btn2.ghost,.actions a.open,.card,.trail2 .s{
    background:var(--card,#1a1d24)}
}
"""



def _e(x) -> str:
    return html.escape("" if x is None else str(x))


def page(title: str, body: str) -> str:
    return (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<meta name='color-scheme' content='light dark'>"
        "<meta name='theme-color' content='#f7f7f5' "
        "media='(prefers-color-scheme: light)'>"
        "<meta name='theme-color' content='#14161a' "
        "media='(prefers-color-scheme: dark)'>"
        f"<title>{_e(title)}</title>"
        f"<style>{CSS}</style></head>"
        f"<body>{body}"
        "<div class='wrap'><footer class='foot'>"
        "Digital Judiciary · decisions are permanent records"
        "</footer></div></body></html>")


def _ago(ts):
    """(plain English age, whole days) for an ISO timestamp."""
    if not ts:
        return "", 0
    try:
        t = datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
        if t.tzinfo is not None:
            t = t.replace(tzinfo=None)
    except Exception:
        return str(ts)[:10], 0
    d = (datetime.utcnow() - t).days
    if d <= 0:
        return "today", 0
    if d == 1:
        return "yesterday", 1
    if d < 14:
        return f"{d} days ago", d
    return f"{d // 7} weeks ago", d


BRANCH_LABEL = {"risk_owner": "risk owner", "lawmakers": "lawmakers",
                "judges": "judges", None: "no branch"}

# What a branch may DO, in words a first-time reader can act on. The branch
# name is the architecture's vocabulary; this is the reader's.
ROLE_CAN = {"risk_owner": "can sign decisions",
            "lawmakers": "can change the rules",
            "judges": "adjudicates"}


def masthead(principal: str = "", branch: str | None = None,
             org: str | None = None, org_name: str | None = None,
             scoped: bool = True, tenants: list[dict] | None = None,
             here: str = "/review") -> str:
    """Who you are, whose ledger you are reading, and what you may sign.

    5.5: a working top bar rather than a masthead. The branch is still shown
    beside the name — what you are empowered to do is the only fact on this
    line that changes what any screen offers — but it is written as something
    a new reader can act on rather than in constitutional vocabulary.
    """
    if not principal:
        return ("<header class='topbar'>"
                "<a class='brand' href='/review'><span class='mk'></span>"
                "Digital Judiciary</a></header>")
    power = " power" if branch == "risk_owner" else ""
    role = ROLE_CAN.get(branch, "read only")
    if scoped:
        tenant = (f"<span class='pillrole'>{_e(org_name or org)}</span>"
                  if org else
                  "<span class='pillrole'>every company</span>")
    else:
        opts = "".join(
            f"<option value='{_e(t['org_id'])}'"
            f"{' selected' if t['org_id'] == org else ''}>"
            f"{_e(t['name'])}</option>" for t in (tenants or []))
        tenant = (
            f"<form method='get' action='{_e(here)}' class='switch'>"
            f"<select name='as' aria-label='Company'"
            f" onchange='this.form.submit()'>"
            f"<option value=''>All companies</option>{opts}</select>"
            f"<noscript><button class='link' type='submit'>Go</button>"
            f"</noscript></form>")
    return (
        "<header class='topbar'>"
        "<a class='brand' href='/review'><span class='mk'></span>"
        "Digital Judiciary</a>"
        f"{tenant}"
        "<span class='spacer'></span>"
        "<span class='me'>"
        f"<strong>{_e(principal)}</strong>"
        f"<span class='pillrole{power}'>{_e(role)}</span>"
        "<a href='/review/login'>Switch</a>"
        "<form method='post' action='/review/logout'>"
        "<button class='link' type='submit'>Sign out</button></form>"
        "</span></header>")


def grp(title: str, count=None, hot: bool = False) -> str:
    """A section heading: name, optional count, rule to the right."""
    n = ""
    if count is not None:
        n = f"<span class='n{' hot' if hot else ''}'>{_e(count)}</span>"
    return (f"<div class='grp'><h2>{_e(title)}</h2>{n}"
            f"<span class='rule'></span></div>")


def csrf_token(task_id: str, api_key: str) -> str:
    return hmac.new(CHAIN_KEY, f"{task_id}|{api_key}".encode(),
                    _sha).hexdigest()[:32]


def csrf_ok(task_id: str, api_key: str, given: str) -> bool:
    return hmac.compare_digest(csrf_token(task_id, api_key), given or "")


# ---------------------------------------------------------------------------
def live_panel(state: dict) -> str:
    """The "switch to live" control on the sign-in page.

    It deliberately does NOT take an API key. This form posts over whatever
    transport the browser happens to be using, the value would land in the
    server process, and this page already keeps its credential in a cookie —
    none of which is an acceptable path for a billing credential that covers
    an entire Anthropic account. The key is read from the server's
    environment, where it is not typed, not transmitted, and not logged; the
    button only reports whether it is there and starts the run.
    """
    mode = state.get("mode", "oracle")
    have_key = state.get("have_key")
    running = state.get("running")

    if mode == "llm":
        return f"""
<p class='devnote' style='margin-top:20px'>Live judging is on</p>
<p class='legend'>A real model is answering the distinguishing question at
   {_e(state.get('ladder') or 'every tier')}. The Analytics tab shows the
   tokens and cost it is actually spending.</p>"""

    if not have_key:
        return """
<p class='devnote' style='margin-top:20px'>Running on the deterministic
   oracle</p>
<p class='legend'>To put a real model at the judge position, set
   <code>ANTHROPIC_API_KEY</code> in the environment the server runs in and
   restart. There is deliberately no field for it here: an API key is a
   billing credential for your whole account, and this page is not a safe
   place to type one.</p>"""

    if running:
        return """
<p class='devnote' style='margin-top:20px'>Switching to live judging…</p>
<p class='legend'>Seeding calls the model once per candidate, sequentially,
   so this takes minutes. This page refreshes itself; the server restarts
   when it finishes.</p>"""

    return """
<p class='devnote' style='margin-top:20px'>Running on the deterministic
   oracle</p>
<form method='post' action='/review/live'>
  <div class='actions'><button type='submit'>Switch to live judging</button>
  </div>
</form>
<p class='legend'>Uses the <code>ANTHROPIC_API_KEY</code> already set in the
   server's environment — nothing is typed here. It rebuilds the demo with a
   real model answering every distinguishing question, which takes minutes
   and costs real money. The run is published afterwards so it can be
   compared against the oracle.</p>"""


def login_page(error: str = "", next_url: str = "/review",
               current: tuple[str, str | None] | None = None,
               roster: list[dict] | None = None,
               orgs: list[dict] | None = None,
               corpus: str | None = None,
               live: dict | None = None) -> str:
    """Sign in, and be told at the door what this account may do.

    Switching identity is still first-class, because the thing this screen
    exists to demonstrate is that the same ledger affords different powers to
    different people. 5.5 states those powers BEFORE you use the account — the
    old screen let you in and then, three clicks later, told you the decision
    was not yours to make. The roster below is DEVELOPMENT ONLY: it lists
    credentials, so it appears only when the container was booted with
    deterministic dev keys.
    """
    err = f"<p class='err'>{_e(error)}</p>" if error else ""
    now = ""
    if current and current[0]:
        pid, branch = current
        can = {"risk_owner": "You can sign decisions.",
               "lawmakers": "You can change the rules."}.get(
                   branch, "You can read everything, and sign nothing.")
        now = (f"<div class='current'>Signed in as "
               f"<strong>{_e(pid)}</strong>. {_e(can)} Signing in below "
               f"replaces that session."
               "<form method='post' action='/review/logout'"
               " style='margin-top:10px'>"
               "<button class='link' type='submit'>Sign out instead</button>"
               "</form></div>")

    # Which corpus is loaded, stated plainly. Without this a single-company
    # demo looks identical to a multi-tenant one that has lost its other
    # tenants, and the only way to tell is to already know.
    loaded = ""
    if corpus:
        n = len(orgs or [])
        names = ", ".join(o["name"] for o in (orgs or [])) or "none"
        loaded = (f"<p class='devnote' style='margin-top:18px'>Demo data "
                  f"<strong>{_e(corpus)}</strong> — {n} "
                  f"{'company' if n == 1 else 'companies'}: {_e(names)}</p>")
        if n <= 1:
            loaded += ("<p class='legend'>One company only, so there is one"
                       " company's people and activity to look at. Rebuild"
                       " with <code>python3 demo/reset.py --company"
                       " _all</code> to see four side by side.</p>")

    bench = ""
    if roster:
        # A grouped dropdown rather than twenty sign-in buttons: the roster
        # grows with every tenant, and a wall of buttons is not a choice. The
        # grouping keeps what matters visible — which company someone belongs
        # to, and what they are allowed to do.
        names_by_org = {o["org_id"]: o["name"] for o in (orgs or [])}
        groups: dict = {}
        for r in roster:
            groups.setdefault(r.get("organization"), []).append(r)

        opts = ""
        for org_id in sorted(groups, key=lambda o: (o is None, o or "")):
            label = (names_by_org.get(org_id, org_id) if org_id
                     else "Platform — sees every company")
            rows = ""
            for r in groups[org_id]:
                power = " ★" if r["branch"] == "risk_owner" else ""
                rows += (f"<option value='{_e(r['key'])}'>"
                         f"{_e(r['principal'])} — {_e(r['can'])}{power}"
                         f"</option>")
            opts += f"<optgroup label='{_e(label)}'>{rows}</optgroup>"

        bench = f"""
<p class='devnote'>Demo keys are on — sign in as anyone</p>
<form method='post' action='/review/login' class='bench'>
  <input type='hidden' name='next' value='{_e(next_url)}'>
  <select name='key' aria-label='Sign in as'>{opts}</select>
  <div class='actions'><button class='btn2' type='submit'>Sign in as this
     person</button></div>
</form>
<p class='legend'>★ marks an account that can sign a decision. Everyone here
   reads the same records; what differs is what each is <em>offered</em> —
   only a risk owner sees the control that accepts a risk, only the rules team
   sees the control that changes a rule, and only a platform administrator
   sees more than one company.</p>"""

    return page("Sign in — Digital Judiciary", f"""
<div class='card'>
  <h1>Sign in</h1>
  <p>Anyone signed in can read every decision and every past ruling. Only a
     risk owner can allow a blocked change, and only the rules team can change
     a rule. That is checked when you sign, not now.</p>
  {err}
  {now}
  <form method='post' action='/review/login'>
    <input type='hidden' name='next' value='{_e(next_url)}'>
    <input type='password' name='key' placeholder='API key' autofocus
           autocomplete='current-password'>
    <div class='actions'><button class='btn2' type='submit'>Sign in</button>
    </div>
  </form>
  {bench}
  {loaded}
  {live_panel(live or {})}
</div>""")


def signed_out_page() -> str:
    return page("Signed out — Digital Judiciary", """
<div class='card'>
  <h1>Signed out</h1>
  <p>Your key has been cleared from this browser. Anything you already
     signed is permanent and unaffected.</p>
  <div class='actions'><a class='btn2' href='/review/login'>Sign in
     again</a></div>
</div>""")


def status_strip(*, open_count: int = 0, judge_mode: str = "oracle",
                 ledger: str = "sqlite", profile: str = "demo",
                 async_inbound: bool = False, queue_backend: str = "sqlite") -> str:
    """Compact ops cue on the review queue — not a dashboard."""
    mode = (judge_mode or "oracle").lower()
    mode_cls = "ok" if mode == "oracle" else "warn"
    bits = [
        f"<span class='pill'><strong>{int(open_count)}</strong> open</span>",
        f"<span class='pill {mode_cls}'>judge <strong>{_e(mode)}</strong></span>",
        f"<span class='pill'>ledger <strong>{_e(ledger)}</strong></span>",
        f"<span class='pill'>queue <strong>{_e(queue_backend)}</strong></span>",
        f"<span class='pill'>profile <strong>{_e(profile)}</strong></span>",
    ]
    if async_inbound:
        bits.append("<span class='pill ok'>async inbound</span>")
    return "<div class='status-strip' role='status'>" + "".join(bits) + "</div>"


def _plain_why(s: dict) -> str:
    """One sentence saying why this is stuck, in the reader's language."""
    text = (s.get("provision_text") or "").strip().rstrip(".")
    if text:
        lead = "Blocked because " + text[0].lower() + text[1:] + "."
    else:
        lead = "Blocked by a rule in force."
    if s.get("contested_tier"):
        lead += (" It was contested and looked at again, and the block stood"
                 " each time.")
    return _e(lead)


def queue_page(tasks: list[dict], principal: str,
               branch: str | None = None, org: str | None = None,
               scoped: bool = True, tenants: list[dict] | None = None,
               here: str = '/review', strip: str = "") -> str:
    """The waiting decisions, as an inbox.

    5.5: grouped by whether it is yours, one sentence of plain English per row
    derived from the provision instead of a provision code, and the age is the
    loudest thing on an overdue row — it is the only number a risk owner acts
    on.
    """
    mine = branch == "risk_owner"
    if not tasks:
        rows = ("<div class='empty'><h2>Nothing waiting</h2>"
                "<p>Blocked changes arrive here only after every automatic "
                "review has already said no.</p></div>")
    else:
        cards = ""
        for t in tasks:
            s = t["summary"]
            guard = (s.get("renewal_guard") or {}).get("state")
            flags = ""
            if guard == "barred":
                flags = "<span class='badge hot'>cannot be allowed</span>"
            elif guard == "must_cite":
                flags = ("<span class='badge warn'>renews a lapsed "
                         "exception</span>")
            when, days = _ago(t.get("opened_at"))
            old = " old" if days >= 5 else ""
            whose = ("<span class='badge hot'>yours to decide</span>" if mine
                     else "<span class='badge'>with a risk owner</span>")
            cards += f"""
  <a class='qcard' href='/review/{_e(t['task_id'])}'>
    <div class='top'>
      <h3 class='what'>{_e(s.get('repo'))}#{_e(s.get('pr_number'))}</h3>
      <span class='src'>{_e(t['provision_id'])}</span>
    </div>
    <p class='why'>{_plain_why(s)}</p>
    <div class='foot2'>
      <span class='age2{old}'>waiting since {_e(when)}</span>
      {whose}{flags}
    </div>
  </a>"""
        head = "Waiting on you" if mine else "Waiting on a risk owner"
        rows = grp(head, len(tasks), hot=True) + cards
        if not mine:
            rows += ("<p class='note2'>You can open any of these and read"
                     " everything. Signing one needs the risk-owner"
                     " account.</p>")
    return page("Decisions — Digital Judiciary",
                f"<div class='wrap'>"
                f"{masthead(principal, branch, org, scoped=scoped, tenants=tenants, here=here)}"
                f"{nav('/review', simulator=SIMULATOR_ON())}"
                f"{strip}"
                f"{rows}"
                f"<p class='note2' style='margin-top:22px'>Every decision here"
                f" becomes a permanent record other teams can point to. "
                f"<a href='/review/ledger'>See past rulings &rarr;</a></p>"
                f"</div>")


def _ladder(trail: list[dict], k: int = 4) -> str:
    """How this reached a person, as a short line rather than a diagram.

    The exhaustion proof of A4 is still the point — you cannot be on this
    screen unless every rung below was actually contested — but a reader needs
    the fact, not the ceremony. The tier numbers move into the drawer with the
    rest of the provenance.
    """
    seen = {e["tier"] for e in trail}
    names = {1: "Automatic check", 2: "Looked at again",
             3: "Looked at once more"}
    steps = []
    for tier in range(1, k):
        cls = "s" if tier in seen else "s off"
        label = names.get(tier, f"Level {tier}")
        if tier not in seen:
            label += " — not needed"
        steps.append(f"<span class='{cls}'>{_e(label)}</span>")
    steps.append("<span class='s now'>You</span>")
    joiner = "<span class='arw'>&rarr;</span>"
    return "<div class='trail2'>" + joiner.join(steps) + "</div>"


def _candidates(summary: dict) -> str:
    verdicts = summary.get("verdicts") or []
    if not verdicts:
        return ("<p class='opinion' style='color:var(--mute)'>No prior record "
                "was similar enough to consult.</p>")
    rows = ""
    for v in verdicts:
        dist = v.get("distinguished")
        cls = "dist" if dist else "kept"
        word = "distinguished" if dist else "in the pool"
        rows += (f"<tr><td class='{cls}'>{_e(v.get('record_id'))}</td>"
                 f"<td>{_e(word)}</td>"
                 f"<td style='font-family:var(--sans)'>"
                 f"{_e(v.get('grounds', ''))}</td></tr>")
    return ("<table class='cand'><thead><tr><th>Record</th><th>Gate</th>"
            f"<th>Grounds</th></tr></thead><tbody>{rows}</tbody></table>")


def task_page(task: dict, principal: str, token: str,
              error: str = "", can_decide: bool = True,
              viewer_branch: str | None = None) -> str:
    """One decision, one screen, on a phone or at a desk.

    5.5 structure: the question, what happened, what the rule says, how it
    reached you, then the two things you can do. Identifiers, precedent
    consulted and provenance move into a drawer — they are evidence, not the
    argument, and putting them first is what made this screen unreadable.

    Two refusals are unchanged and load-bearing:
      * when Proposition 2 bars an acceptance the control is ABSENT, not
        disabled;
      * the end date sits inside the sentence being signed, because A7 makes
        it constitutive of the act rather than metadata about it.
    """
    s = task["summary"]
    guard = s.get("renewal_guard") or {}
    barred = guard.get("state") == "barred"
    decided = task["state"] != "open"
    when, days = _ago(task.get("opened_at"))

    facts = "".join(f"<li>{_e(f)}</li>" for f in s.get("facts", []))
    err = f"<p class='err'>{_e(error)}</p>" if error else ""

    drawer = f"""
<details class='more'>
  <summary>The full file — identifiers, precedent, provenance</summary>
  <dl class='caption'>
    <dt>Case</dt><dd>{_e(task['case_id'])}</dd>
    <dt>Rule</dt><dd>{_e(task['provision_id'])}</dd>
    <dt>Pull request</dt>
    <dd class='plain'><a href='{_e(s.get('pr_url'))}'>{_e(s.get('repo'))}#{_e(s.get('pr_number'))}</a></dd>
    <dt>Commit</dt><dd>{_e((s.get('head_sha') or '')[:12])}</dd>
    <dt>Rulebook</dt><dd>{_e(s.get('rulebook_version'))}</dd>
    <dt>Asked for by</dt><dd>{_e(s.get('requested_by'))}</dd>
    <dt>Contested at</dt><dd>tier {_e(s.get('contested_tier'))}</dd>
  </dl>
  <p class='eyebrow'>What was read from the change</p>
  <ul class='facts'>{facts}</ul>
  <p class='eyebrow'>Earlier rulings consulted</p>
  {_candidates(s)}
</details>"""

    banner = ""
    if barred:
        banner = f"""
<div class='banner'>
  <h3>You cannot allow this one</h3>
  <p>An earlier exception on this rule expired, and the rules team refused to
     renew it. Under Proposition&nbsp;2 a materially similar exception is
     barred, so this screen offers only the block. Changing that means
     changing the rule. Reference <code>{_e(guard.get('predecessor'))}</code>.
     </p>
</div>"""
    elif guard.get("state") == "must_cite":
        banner = f"""
<div class='banner warn'>
  <h3>This repeats an exception that already expired</h3>
  <p>Exception <code>{_e(guard.get('predecessor'))}</code> ran out and is
     still with the rules team. If you allow this, the new record will say so
     openly.</p>
</div>"""

    if not decided and not can_decide:
        # The screen is NOT the enforcement point and must not look like one.
        # Authority is resolved in the Kernel at the moment of action; hiding
        # the control here is candour, not security. Anyone who reconstructs
        # the POST by hand meets the same refusal from risk_decision().
        instrument = f"""
<div class='instrument'>
  <h2>You can read this, but not sign it</h2>
  <p class='opinion'>You are signed in as <strong>{_e(principal)}</strong>,
     which cannot allow a blocked change. Only a named risk owner can, because
     their name goes on a permanent record. Nothing here is hidden from you —
     that is deliberate.</p>
  {err}
  <div class='actions'><a class='btn2 ghost' href='/review/login'>Switch
     account</a></div>
  <input type='hidden' name='csrf' value='{_e(token)}'>
</div>"""
    elif decided:
        instrument = f"""
<div class='instrument'>
  <h2>Already decided</h2>
  <p class='opinion'><strong>{_e(task['outcome'])}</strong> by
     {_e(task['decided_by'])} on
     {_e((task['closed_at'] or '')[:16].replace('T', ' '))}. Record
     <code>{_e(task['record_id'])}</code> is permanent. A later case may be
     judged differently; nothing can edit this one.</p>
</div>"""
    else:
        d7 = (date.today() + timedelta(days=7)).isoformat()
        d30 = (date.today() + timedelta(days=30)).isoformat()
        d90 = (date.today() + timedelta(days=90)).isoformat()
        pick = "this.form.expiry.value=this.value"
        accept = "" if barred else f"""
  <form class='allow' method='post'
        action='/review/{_e(task['task_id'])}/decide'>
    <input type='hidden' name='csrf' value='{_e(token)}'>
    <input type='hidden' name='decision' value='accept'>
    <h3>Allow it anyway</h3>
    <p class='sub'>You are accepting this risk on the record. An exception is
       always temporary, so it has to have an end date.</p>
    <label class='fld'>Ends on</label>
    <div class='chips'>
      <label><input type='radio' name='exp_pick' value='{d7}'
        onclick='{pick}'><span>7 days</span></label>
      <label><input type='radio' name='exp_pick' value='{d30}' checked
        onclick='{pick}'><span>30 days</span></label>
      <label><input type='radio' name='exp_pick' value='{d90}'
        onclick='{pick}'><span>90 days</span></label>
    </div>
    <p class='sentence'>I, <strong>{_e(principal)}</strong>, accept this risk
       until <input type='date' name='expiry' required value='{d30}'
       aria-label='End date'>, after which the block comes back automatically
       and the rules team is told.</p>
    <label class='fld' for='ar'>Why this is acceptable</label>
    <textarea id='ar' name='rationale' required
      placeholder='Goes on the permanent record, under your name.'></textarea>
    <button class='btn2' type='submit'>Sign and allow</button>
  </form>"""
        instrument = f"""
<div class='instrument'>
  <h2>Your decision</h2>
  {err}
  <div class='choice'>
  {accept}
  <form method='post' action='/review/{_e(task['task_id'])}/decide'>
    <input type='hidden' name='csrf' value='{_e(token)}'>
    <input type='hidden' name='decision' value='decline'>
    <h3>Keep it blocked</h3>
    <p class='sub'>The team has to change the change, or ask for the rule
       itself to be revisited.</p>
    <label class='fld' for='dr'>What you want them to know</label>
    <textarea id='dr' name='rationale' required
      placeholder='Recorded under your name.'></textarea>
    <button class='btn2 ghost' type='submit'>Keep it blocked</button>
  </form>
  </div>
  <p class='note2' style='margin-top:14px'>Either way this becomes a permanent
     record other teams can point to.</p>
</div>"""

    body = f"""
<div class='wrap'>
  {masthead(principal, viewer_branch)}
  {nav('/review', simulator=SIMULATOR_ON())}
  <p class='crumb'><a href='/review'>&larr; Decisions</a> · waiting since
     {_e(when)}</p>
  <div class='focus'>
    <h1 class='q'>Should {_e(s.get('repo'))}#{_e(s.get('pr_number'))} be
       allowed to ship?</h1>
    <div class='two'>
      <div class='panel'>
        <h3>What happened</h3>
        <p>{_e(s.get('rationale'))}</p>
      </div>
      <div class='panel'>
        <h3>What the rule says</h3>
        <p class='quote'>{_e(s.get('provision_text'))}</p>
        <p class='src2'>{_e(task['provision_id'])} · rulebook
           {_e(s.get('rulebook_version'))}</p>
      </div>
    </div>
    <div class='panel'>
      <h3>How it reached you</h3>
      {_ladder(s.get('trail', []))}
      <p class='note2' style='margin-top:10px'>Every automatic review is
         spent. There is no further step after you.</p>
    </div>
    {banner}
    {instrument}
    {drawer}
  </div>
</div>"""
    return page(f"{s.get('repo')}#{s.get('pr_number')} — decide", body)


# ---------------------------------------------------------------------------
# The register: every record the judiciary has produced, and its life
# ---------------------------------------------------------------------------
def _status(rec: dict) -> tuple[str, str, str]:
    """(css class, label, explanation) for a record's standing today."""
    if rec.get("superseded"):
        return ("lapsed", "superseded",
                "the clause this holding interpreted was materially amended,"
                " so it no longer controls anything")
    if not rec["is_acceptance"]:
        return "", "in force", "an ordinary holding; it does not expire"
    if rec.get("lapsed"):
        return ("lapsed", "lapsed",
                "the acceptance expired and no longer controls anything")
    return ("live-accept", "expires " + (rec.get("expiry") or "")[:10],
            "a live risk acceptance, carrying a mandatory expiry (A7)")


def ledger_page(census: dict, rows: list[dict], principal: str,
                branch: str | None = None, status: str | None = None,
                provision: str | None = None,
                next_cursor: tuple | None = None, org: str | None = None,
                show_org: bool = False) -> str:
    """A reporter volume: newest first, one line per holding.

    The census doubles as the filter control. That is not decoration — the
    four numbers an auditor wants (how many holdings, how many live
    acceptances, how many lapsed) are exactly the four views they want to
    open, so making them the same object removes a whole row of chrome.
    """
    def q(**kw):
        base = {"status": status, "provision": provision}
        base.update(kw)
        parts = [f"{k}={urllib.parse.quote(str(v))}"
                 for k, v in base.items() if v]
        return "/review/ledger" + ("?" + "&".join(parts) if parts else "")

    def tab(key, label, value, cls=""):
        on = " on" if status == key else ""
        return (f"<a class='{on.strip()}' href='{q(status=key)}'>"
                f"<span class='k'>{label}</span>"
                f"<span class='v {cls}'>{value}</span></a>")

    tally = (
        "<div class='tally'>"
        + tab(None, "All records", census["records"])
        + tab("holding", "Holdings", census["holdings"])
        + tab("acceptance", "Live acceptances", census["live_acceptances"],
              "amber" if census["live_acceptances"] else "")
        + tab("lapsed", "Lapsed", census["lapsed"],
              "lapsed" if census["lapsed"] else "")
        + "</div>")

    scope = ""
    if provision:
        scope = (f"<p class='scope'>Filtered to <strong>{_e(provision)}</strong>"
                 f" &nbsp;·&nbsp; <a href='{q(provision=None)}'>show every"
                 f" provision</a></p>")

    if not rows:
        listing = ("<div class='empty'><h2>Nothing here</h2>"
                   "<p>A precedent is written only when a decision is "
                   "contested and resolved above tier 1. No record matches "
                   "this view.</p></div>")
    else:
        listing = "<div class='reg'>"
        for r in rows:
            lapsed = bool(r.get("lapsed"))
            cls = ("lapsed" if lapsed
                   else "live-accept" if r["is_acceptance"] else "")
            label = ("lapsed" if lapsed else
                     "expires " + (r.get("expiry") or "")[:10]
                     if r["is_acceptance"] else "in force")
            st_cls = ("lapsed" if lapsed
                      else "accept" if r["is_acceptance"] else "")
            interp = (r.get("interpretation") or {}).get("outcome", "?")
            cited = (f"followed {r['controlling_id'][:8]}"
                     if r.get("controlling_id")
                     else say("controlling_state", r["controlling_state"]))
            listing += f"""
  <div class='r {cls}'>
    <div class='mark'></div>
    <div class='pid'><a class='rec'
       href='{q(provision=r['provision_id'])}'>{_e(r['provision_id'])}</a></div>
    <div><a class='rec' href='/review/ledger/{_e(r['id'])}'>
      <p class='hold'>{_e(say('outcome', interp))}</p>
      <div class='meta'>tier {_e(r['authority_tier'])} ·
        {_e(r['resolving_principal'])} · {_e(cited)}</div>
      {"<span class='org'>" + _e(r.get('organization') or 'platform')
       + "</span>" if show_org else ""}</a></div>
    <div class='st {st_cls}'>{_e(label)}</div>
    <div class='when'>{_e((r['resolved_at'] or '')[:10])}</div>
  </div>"""
        listing += "</div>"

    older = ""
    if next_cursor:
        older = (f"<a href='{q(ats=next_cursor[0], aid=next_cursor[1])}'>"
                 f"Older &rarr;</a>")
    pager = (f"<div class='pager'><span class='count'>showing {len(rows)}"
             f" record(s)</span>{older}</div>") if rows else ""

    return page("Past rulings — Digital Judiciary",
                f"<div class='wrap'>{masthead(principal, branch, org)}"
                f"{nav('/review/ledger', simulator=SIMULATOR_ON())}"
                f"{grp('Past rulings')}"
                f"<p class='lede' style='margin:-6px 0 16px'>Every decision"
                f" this system has recorded, newest first. Nothing here can"
                f" be edited or deleted.</p>"
                f"{tally}{scope}{listing}{pager}"
                f"</div>")


def _spine(rec: dict, events: list[dict]) -> str:
    """The record's life, in the order it actually happened.

    Two kinds of node are interleaved on one timeline, and the difference is
    the point: lifecycle EVENTS are things that occurred and are in the log,
    while the expiry is a SCHEDULED fact carrying no event of its own. It is
    placed by its date like anything else — ahead of today for a live
    acceptance, behind for one that has lapsed — because a reader tracing A7
    needs to see where the deadline sat relative to the referral, not be told
    about it out of sequence.
    """
    nodes: list[tuple[str, str]] = [(
        rec["resolved_at"],
        f"""<li><span class='t'>Admitted through the Challenge Gate</span>
      <span class='stamp'>{_e(rec['resolved_at'][:19].replace('T', ' '))} ·
      {_e(rec['resolving_principal'])} · tier {_e(rec['authority_tier'])}
      </span></li>""")]

    if rec["is_acceptance"] and rec.get("expiry"):
        future = not rec.get("lapsed")
        nodes.append((rec["expiry"], f"""<li class='expiry{' future' if future
      else ''}'><span class='t'>{'Expires' if future else 'Expiry passed'}
      </span><span class='stamp'>{_e(rec['expiry'][:10])} ·
      {'mandatory under A7' if future else 'after which it controls nothing'}
      </span></li>"""))

    label = {"lapsed": "Lapsed",
             "referral_emitted": "Referred to the lawmakers",
             "referral_adopted": "Referral adopted",
             "referral_rejected": "Referral rejected",
             "referral_withdrawn": "Referral withdrawn",
             "renewed_by": "Renewed by a later acceptance",
             "superseded": "Superseded — the clause was amended",
             "outcome_recorded": "Outcome recorded"}
    for e in events:
        cls = "lapse" if e["event_type"] == "lapsed" else ""
        nodes.append((e["occurred_at"], f"""<li class='{cls}'>
      <span class='t'>{_e(label.get(e['event_type'], e['event_type']))}</span>
      <span class='stamp'>{_e(e['occurred_at'][:19].replace('T', ' '))} ·
      {_e(e['actor'])}</span></li>"""))

    nodes.sort(key=lambda n: n[0])
    if not rec["is_acceptance"] and not events:
        nodes.append(("~", """<li class='future'><span class='t'>No further
      events</span><span class='stamp'>an ordinary holding does not expire;
      it stands until a later case distinguishes it</span></li>"""))
    return "<ul class='spine'>" + "".join(h for _, h in nodes) + "</ul>"


def record_page(rec: dict, events: list[dict], judgments: list[dict],
                principal: str, branch: str | None = None,
                org: str | None = None, may_promote: bool = False,
                token: str = "") -> str:
    cls, label, why = _status(rec)
    premise = set(rec.get("premise") or [])
    facts = "".join(
        f"<li class='{'mat' if f in premise else ''}'>{_e(f)}</li>"
        for f in rec.get("facts", []))
    interp = (rec.get("interpretation") or {}).get("outcome", "?")

    caption = f"""
<dl class='caption'>
  <dt>Record</dt><dd>{_e(rec['id'])}</dd>
  <dt>Provision</dt><dd>{_e(rec['provision_id'])}</dd>
  <dt>Authority</dt><dd class='plain'>tier {_e(rec['authority_tier'])} —
     {_e(rec['resolving_principal'])}</dd>
  <dt>Standing</dt><dd class='plain'>{_e(label)}</dd>
  <dt>Case</dt><dd>{_e(rec['case_id'])}</dd>
  <dt>Rulebook</dt><dd>{_e(rec['rulebook_version'])}</dd>
  <dt>Scope</dt><dd class='plain'>{_e(say('scope_level', rec.get('scope_level')))}</dd>
  <dt>Tenant</dt><dd>{_e(rec.get('organization') or 'platform law')}</dd>
  <dt>Scope</dt><dd class='plain'>{_e(rec.get('scope_level'))}</dd>
</dl>"""

    ctrl = (f"Bound by <code>{_e(rec['controlling_id'])}</code>"
            if rec.get("controlling_id")
            else f"No earlier decision applied — <em>{_e(say('controlling_state', rec['controlling_state']))}"
                 f"</em>")
    consulted = rec.get("consulted_ids") or []

    jrows = ""
    for j in judgments:
        v = json.loads(j["verdict"]) if isinstance(j["verdict"], str) \
            else j["verdict"]
        if j["kind"] == "premise":
            word, gcls = "premise proposed", "kept"
        else:
            dist = v.get("distinguished")
            word = "distinguished" if dist else "in the pool"
            gcls = "dist" if dist else "kept"
        jrows += (f"<tr><td class='{gcls}'>{_e(j['candidate_hash'][:12])}</td>"
                  f"<td>{_e(word)}</td><td>tier {_e(j['tier'])}</td>"
                  f"<td style='font-family:var(--sans)'>"
                  f"{_e(v.get('grounds', ''))}</td></tr>")
    jtable = (f"<table class='cand'><thead><tr><th>Candidate</th><th>Gate</th>"
              f"<th>Asked by</th><th>Grounds</th></tr></thead><tbody>{jrows}"
              f"</tbody></table>") if jrows else \
        ("<p class='opinion' style='color:var(--mute)'>No judgment was "
         "recorded against this record's batch.</p>")

    promote = ""
    if may_promote:
        promote = f"""
<div class='instrument judicial'>
  <h2>Ratify this holding as platform law</h2>
  <p class='opinion'>This is one tenant's reading of
     {_e(rec['provision_id'])}. Ratifying it writes a new platform-scope
     holding that every tenant's cases may cite — general law, which any
     tenant's own holding on the same facts still outranks. The original
     stays where it is; the ledger is immutable.</p>
  <form method='post' action='/review/ledger/{_e(rec['id'])}/promote'>
    <input type='hidden' name='csrf' value='{_e(token)}'>
    <div class='actions'><button type='submit'>Promote to platform law
       </button></div>
  </form>
  <p class='legend'>Promotion is a legislative act. A holding that became
     everyone's law merely by being filed would transfer authority nobody
     exercised.</p>
</div>"""
    elif rec.get("organization") is None and rec.get("promoted_from"):
        promote = ("<div class='banner'><h3>Platform law</h3><p>Ratified from"
                   " a tenant holding and citable by every tenant. A tenant's"
                   " own holding on the same facts takes precedence.</p>"
                   "</div>")

    banner = ""
    if rec.get("superseded"):
        banner = """
<div class='banner'>
  <h3>Superseded by amendment</h3>
  <p>The legislature materially changed the clause this holding interpreted.
     It is excluded from retrieval and controls nothing. It stays in the
     ledger because the ledger is immutable — a record of what was decided
     under the words that applied at the time.</p>
</div>"""
    elif rec.get("lapsed"):
        banner = """
<div class='banner'>
  <h3>This acceptance has lapsed</h3>
  <p>It is excluded from retrieval and controls nothing. It remains in the
     ledger because the ledger is immutable — a record of what was decided,
     not of what is still in force.</p>
</div>"""

    body = f"""
<div class='wrap'>
  {masthead(principal, branch, org)}
  <p class='eyebrow'><a href='/review/ledger'>&larr; The ledger</a></p>
  <div class='docket'>
    <aside class='rail'>{caption}{_spine(rec, events)}</aside>
    <main>
      <p class='eyebrow'>Holding</p>
      <p class='provision'>{_e(say('outcome', interp))}</p>
      <p class='opinion'>{_e(rec.get('rationale_text'))}</p>
      {banner}

      <p class='eyebrow'>Facts of the case</p>
      <ul class='facts'>{facts}</ul>
      <p class='legend'>Marked facts are the <strong>premise</strong> — what
         this holding rests on. A later case is distinguished from this one
         exactly when it lacks one of them, so the premise is what decides how
         far this record reaches.</p>

      {promote}
      <p class='eyebrow'>What it consulted</p>
      <p class='opinion'>{ctrl}. {_e(len(consulted))} record(s) retrieved.</p>
      {jtable}
    </main>
  </div>
</div>"""
    return page(f"{rec['provision_id']} — record", body)


# ===========================================================================
# The four desks
# ===========================================================================
# One ledger, four questions. The architecture's claim is that authority is
# separated, so the application is not one screen with role-based hiding — it
# is four front doors, each opening on the question its occupant actually
# has. Everything stays READABLE to everyone (transparency is the audit
# claim); what changes per role is what is *offered* and what leads.
#
#   engineer    "what is happening to my change, and what can I do?"
#   risk owner  "what needs my signature, and what am I still on the hook for?"
#   lawmaker    "where is the rulebook wrong, and who says so?"
#   auditor     "can I trust this, and can I prove it?"

DESKS = [
    ("/review", "Your work", None),
    ("/review/changes", "Changes", None),
    ("/review/amendments", "Rule changes", None),
    ("/review/ledger", "Past rulings", None),
    ("/review/impact", "Impact", None),
    ("/review/analytics", "Cost", None),
    ("/review/activity", "Activity", None),
    ("/review/rulebook", "Rules", None),
]

# Shown only when the simulator is switched on; see nav().
ADMIN_DESK = ("/review/admin", "Simulator", None)


def SIMULATOR_ON() -> bool:
    import os
    return os.environ.get("DJ_SIMULATOR") == "1"


def nav(active: str, simulator: bool = False) -> str:
    """Desks on a desktop; a five-item tab bar on a phone.

    The tab bar is the same list truncated, not a second information
    architecture — so a link sent from a laptop lands somewhere a phone can
    still navigate out of.
    """
    desks = DESKS + ([ADMIN_DESK] if simulator else [])
    items = "".join(
        f"<a class='{'on' if href == active else ''}' href='{href}'>"
        f"{_e(label)}</a>"
        for href, label, _ in desks)
    tabs = "".join(
        f"<a class='{'on' if href == active else ''}' href='{href}'>"
        f"{_e(label)}</a>"
        for href, label, _ in desks[:5])
    return (f"<nav class='desks'>{items}</nav>"
            f"<nav class='tabbar' aria-label='Sections'>{tabs}</nav>")


def landing_for(branch: str | None) -> str:
    """Everyone lands on their own desk now that every role has one."""
    return "/review"


LANES = {
    "proceed": ("clear", "merged without waiting for anyone"),
    "proceed_with_conditions": ("clear", "cleared, with conditions attached"),
    "blocked_challengeable": ("open", "you can say the rule does not apply, "
                                      "or ask a person to allow it"),
    "blocked_absolute": ("floor", "cannot be waived by anyone — only a rule "
                                  "change gets past this"),
    "blocked_final": ("final", "upheld at the last level; nothing further "
                               "is automatic"),
    "human_review": ("waiting", "with a named risk owner now"),
    "routed_amendment": ("legislature", "a rule change — it goes to the rules "
                                        "team, it is never judged"),
    "ignored": ("n/a", "nothing here to decide"),
}


def changes_page(rows: list[dict], counts: dict, principal: str,
                 branch: str | None = None, org: str | None = None,
                 scoped: bool = True,
                 tenants: list[dict] | None = None) -> str:
    """The change stream: every governed change and what is still open to it.

    This is the screen the architecture was missing. An engineer whose pull
    request is blocked has, until now, had a check annotation and nowhere to
    go. Corollary 2 says a denial short of the ceiling always leaves an exit;
    a person can only use an exit they can see.
    """
    tiles = "".join(
        f"<div><span class='k'>{_e(k)}</span><span class='v'>{v}</span></div>"
        for k, v in counts.items())
    body = ""
    for r in rows:
        kind, meaning = LANES.get(r["disposition"] or "", ("", ""))
        lanes = ""
        if r["disposition"] == "blocked_challengeable":
            lanes = ("<span class='lane'>say it does not apply</span>"
                     "<span class='lane'>ask a person</span>")
        elif r["disposition"] == "blocked_absolute":
            lanes = "<span class='lane'>rule change only</span>"
        elif r["disposition"] == "human_review":
            lanes = "<span class='lane wait'>awaiting a risk owner</span>"
        body += f"""
  <div class='r {kind}'>
    <div class='mark'></div>
    <div class='pid'>{_e(r['repo'])}#{_e(r['pr_number'])}</div>
    <div><a class='rec' href='/review/change/{_e(r['session_id'])}'>
      <p class='hold'>{_e(say('disposition', r['disposition'], 'Not yet decided'))}</p>
      <div class='meta'>{_e(meaning)}</div></a>{lanes}</div>
    <div class='st'>{_e(', '.join(json.loads(r['provisions'] or '[]'))
                        or 'no clause engaged')}</div>
    <div class='when'>{_e((r['received_at'] or '')[:10])}</div>
  </div>"""
    listing = (f"<div class='reg stream'>{body}</div>" if rows else
               "<div class='empty'><h2>No changes yet</h2><p>Nothing has been"
               " submitted for governance.</p></div>")
    return page("Changes — Digital Judiciary",
                f"<div class='wrap'>{masthead(principal, branch, org, scoped=scoped, tenants=tenants, here='/review/changes')}"
                f"{nav('/review/changes', simulator=SIMULATOR_ON())}"
                f"{grp('Changes')}"
                f"<p class='lede' style='margin:-6px 0 16px'>Every change"
                f" this system looked at, and what is still open to it.</p>"
                f"<div class='tally'>{tiles}</div>{listing}</div>")


def amendments_page(pending: list[dict], decided: list[dict], friction:
                    list[dict], principal: str, branch: str | None = None,
                    org: str | None = None, token: str = "",
                    flash: dict | None = None) -> str:
    """The legislature's desk.

    Judicial referrals land here. That is the whole point of the mechanism:
    a tier that had to resolve an unbroken conflict, or that has watched a
    provision be waived again and again, is holding evidence the legislature
    needs — and before this screen existed, that evidence was computed and
    thrown away.
    """
    may_decide = branch == "lawmakers"

    # Say what just happened. Ten referrals read almost identically — same
    # origin, same question, only the clause differs — so disposing of one
    # leaves a list that looks untouched, and the honest conclusion for
    # anyone using it is that the button did nothing. It did; the page was
    # simply silent about it.
    banner = ""
    if flash and flash.get("status"):
        st = flash["status"]
        if st == "adopted" and flash.get("no_rule_change"):
            extra = ("It named no concrete rule change, so no rule text or"
                     " predicate changed and no existing decision was"
                     " disturbed.")
        elif st == "adopted" and (flash.get("superseded") or "0") != "0":
            extra = (f"{flash['superseded']} existing decision(s) were retired:"
                     f" they interpreted wording no longer in force.")
        elif st == "adopted":
            extra = "The new rulebook version is in force from now on."
        else:
            extra = "The rule is unchanged."
        banner = f"""
<div class='banner'>
  <h3>Proposal #{_e((flash.get('id') or '')[:8])} {_e(st)}</h3>
  <p>Recorded against <strong>{_e(principal)}</strong>. {_e(extra)}</p>
</div>"""

    def card(a, closed=False):
        b = json.loads(a["body"] or "{}")
        origin = say("origin", a["origin"])
        judicial = a["origin"] == "judicial_referral"
        ev = b.get("evidence") or {}
        evidence = "".join(f"<li>{_e(k.replace('_', ' '))}: "
                           f"<strong>{_e(v)}</strong></li>"
                           for k, v in ev.items())

        # --- what is actually being decided -----------------------------
        # A lawmaker asked to adopt or reject needs the rule in front of
        # them: what it says now, what it would say, and what adopting does
        # to the decisions already made under it. Without that the buttons
        # are a coin toss with a permanent record attached.
        # --- the package -------------------------------------------------
        # Sections in the order a person needs them: what the rule says now,
        # what it has actually done, what provoked this, and what each answer
        # costs. A referral that arrives as one sentence is a notification;
        # this is the file behind it.
        d = a.get("_dossier") or {}
        dossier = ""
        cp = b.get("change_request") or {}
        if cp.get("repo"):
            files = "".join(f"<li>{_e(f)}</li>" for f in cp.get("files") or [])
            dossier = f"""
<div class='amend'>
  <p class='eyebrow'>The change you are being asked to approve</p>
  <p class='formal'>{_e(cp.get('title') or 'untitled change')}</p>
  <p class='human'><strong>{_e(cp.get('repo'))}#{_e(cp.get('number'))}</strong>
     opened by {_e(cp.get('author') or 'unknown')}. It edits the rulebook
     itself, which is why it is here rather than being judged like ordinary
     work — nobody but the lawmakers can change a rule.</p>
  {f"<p class='eyebrow'>Files it touches</p><ul class='facts'>{files}</ul>"
   if files else ""}
  <div class='actions'>
    {f"<a class='open' href='{_e(cp['url'])}' target='_blank'"
     f" rel='noopener noreferrer'>Read the pull request on GitHub &nearr;</a>"
     if cp.get('url') else ""}
    {f"<a class='open' href='/review/change/{_e(cp['session_id'])}'>"
     f"How this system handled it</a>" if cp.get('session_id') else ""}
  </div>
  {"<p class='legend'>This is a replayed demo scenario, so there is no real"
   " pull request to open. On a live deployment this links straight to the"
   " diff.</p>" if cp.get('source') == 'simulator' else ""}
</div>"""
        elif d.get("provision_id"):
            floor = ("<span class='src floor'>cannot be waived</span>"
                     if d.get("absolute") else "")
            waived = ""
            if d.get("waiver_log"):
                items = "".join(
                    f"<tr><td class='f'>{_e(w['when'])}</td>"
                    f"<td>{_e(w['who'])}</td>"
                    f"<td>until {_e(w['until'])} — {_e(w['state'])}</td>"
                    f"<td style='font-size:12px'>{_e(w['why'])}</td></tr>"
                    for w in d["waiver_log"])
                waived = (f"<p class='eyebrow'>Every waiver granted on this"
                          f" rule</p><table class='diff'><thead><tr>"
                          f"<th>Granted</th><th>By</th><th>Ran to</th>"
                          f"<th>Stated reason</th></tr></thead>"
                          f"<tbody>{items}</tbody></table>")
            trig = ""
            if d.get("trigger"):
                t = d["trigger"]
                trig = f"""
  <p class='eyebrow'>What provoked this</p>
  <p class='human'>On {_e(t['when'])}, <strong>{_e(t['who'])}</strong> accepted
     this risk until {_e(t['until'])}, on the grounds that:
     “{_e(t['why'][:220])}”</p>
  <p class='legend'>It rested on {_e(', '.join(_plain(f) for f in t['premise'])
                                    or 'no stated facts')}.
     Since then: {_e(' · '.join(t['events']) or 'nothing further')}.</p>"""
            dossier = f"""
<div class='amend'>
  <p class='eyebrow'>The rule as it stands {floor}</p>
  <p class='formal'>{_e(d.get('text') or d['provision_id'])}</p>
  <p class='human'>{_e(d.get('plain') or '')}</p>

  <p class='eyebrow'>What it has actually done</p>
  <div class='tally'>
    <div><span class='k'>Changes it judged</span>
         <span class='v'>{d['engaged']}</span></div>
    <div><span class='k'>Decisions recorded</span>
         <span class='v'>{d['decisions']}</span></div>
    <div><span class='k'>Times waived</span>
         <span class='v{' amber' if d['waivers'] else ''}'>{d['waivers']}
         </span></div>
    <div><span class='k'>Settled by citing an earlier one</span>
         <span class='v'>{d['bound']}</span></div>
  </div>
  <p class='legend'>Active between {_e(d.get('first_at') or '—')} and
     {_e(d.get('last_at') or '—')}.</p>
  {trig}
  {waived}
</div>"""

        brief = ""
        detail = (a.get("_brief") or {})
        changes = b.get("changes") or []
        if detail.get("clauses"):
            for cl in detail["clauses"]:
                verdict = cl["effect"]
                tone = ("deny" if verdict == "supersedes" else
                        "wait" if verdict == "new" else "")
                before_after = ""
                for field, was, now in cl["diff"]:
                    before_after += f"""
      <tr><td class='f'>{_e(field)}</td>
          <td class='was'>{_e(was)}</td>
          <td class='now'>{_e(now)}</td></tr>"""
                brief += f"""
  <div class='amend {tone}'>
    <p class='eyebrow'>{_e(cl['provision_id'])} — {_e(cl['headline'])}</p>
    <p class='human'>{_e(cl['plain'])}</p>
    {f"<table class='diff'><thead><tr><th>Field</th><th>Now</th>"
     f"<th>Would become</th></tr></thead><tbody>{before_after}</tbody>"
     f"</table>" if before_after else ""}
    <p class='legend'>{_e(cl['consequence'])}</p>
  </div>"""
        elif not changes:
            # A proposal with no drafted edit is not one situation, it is
            # three, and the old single sentence described none of them. What
            # matters to the person deciding is: what am I being asked, and
            # what happens to the rule if I say yes.
            asks = {
                "risk_acceptance_referral": (
                    "A waiver on this rule ran out. You are being asked "
                    "whether the exception should become part of the rule "
                    "itself.",
                    "Nothing is drafted yet. Adopting records that the "
                    "lawmakers agree the rule should change — somebody then "
                    "has to write that change and bring it back here. "
                    "Rejecting leaves the rule exactly as it is, and future "
                    "changes will keep being blocked by it."),
                "judicial_referral": (
                    "The review tiers ran into a problem with this rule — "
                    "either two past decisions that conflict, or a rule that "
                    "keeps having to be waived — and referred it to you.",
                    "Nothing is drafted yet. Adopting records that the "
                    "lawmakers agree something should change; somebody then "
                    "has to write it. Rejecting leaves the rule as it is."),
                "control_plane_routed": (
                    "Somebody wants to change a rule. Because the wording "
                    "lives in the pull request above, it is not repeated "
                    "here — open it and read the edit before you decide.",
                    "Adopting records that the lawmakers approve that edit. "
                    "Rejecting means the rulebook stays as it is and the "
                    "change does not go in. Either way, no case already "
                    "decided is affected."),
            }
            ask, effect = asks.get(a["origin"], (
                "This proposal does not spell out a change to any rule.",
                "Adopting records the lawmakers' agreement; no rule text "
                "changes and no past decision is affected."))
            brief = (f"<div class='amend'><p class='human'>{_e(ask)}</p>"
                     f"<p class='legend'>{_e(effect)}</p></div>")

        controls = ""
        if may_decide and not closed:
            controls = f"""
    <form method='post' action='/review/amendments/{_e(a['id'])}/decide'>
      <input type='hidden' name='csrf' value='{_e(token)}'>
      <div class='actions'>
        <button type='submit' name='decision' value='adopted'>Adopt</button>
        <button type='submit' name='decision' value='rejected'
                class='secondary'>Reject</button>
      </div>
    </form>"""
        elif not closed:
            controls = ("<p class='legend'>Only a principal holding the "
                        "lawmakers branch can dispose of this.</p>")
        return f"""
<div class='instrument{' judicial' if judicial else ''}'>
  <p class='eyebrow'>{_e(origin)}{' · from the judiciary' if judicial else ''}
     {' · ' + _e(a['status']) if closed else ''}</p>
  <h2>{_e(b.get('provision_id') or 'constitution')}
     <span class='ref'>#{_e(a['id'][:8])}</span></h2>
  <p class='prov-meta'>filed {_e((a['created_at'] or '')[:16].replace('T', ' '))}
     {'· on record ' + _e((a['source_record'] or '')[:8])
      if a['source_record'] else ''}</p>
  <p class='opinion'>{_e(b.get('note') or b.get('question')
                         or 'No statement of reasons was recorded with this'
                            ' proposal.')}</p>
  {f"<ul class='facts'>{evidence}</ul>" if evidence else ""}
  {dossier}
  {brief}
  <p class='legend'>Proposed by <strong>{_e(a['proposed_by'])}</strong>
     {'· cites record ' + _e((a['source_record'] or '')[:8])
      if a['source_record'] else ''}</p>
  {controls}
</div>"""

    rows = "".join(card(a) for a in pending) or (
        "<div class='empty'><h2>Nothing waiting on the rules team</h2>"
        "<p>No amendment is pending. Referrals arrive here automatically when "
        "a tier resolves an unbroken conflict, or when a provision has been "
        "risk-accepted repeatedly.</p></div>")

    agenda = ""
    if friction:
        items = "".join(
            f"<div class='r'><div class='mark'></div>"
            f"<div class='pid'>{_e(f['provision_id'])}</div>"
            f"<div><p class='hold'>{f['waivers']} acceptance(s), "
            f"{f['records']} recorded decision(s)</p>"
            f"<div class='meta'>the more a clause is waived or litigated, the "
            f"more likely it is the clause, not the change, that is wrong"
            f"</div></div>"
            f"<div class='st'></div><div class='when'></div></div>"
            for f in friction)
        agenda = (grp('Where the rules are under strain')
                  + f"<div class='reg'>{items}</div>")

    hist = ""
    if decided:
        hist = ("<p class='eyebrow'>Recently disposed of</p>"
                + "".join(card(a, closed=True) for a in decided))

    return page("Rule changes — Digital Judiciary",
                f"<div class='wrap'>{masthead(principal, branch, org)}"
                f"{nav('/review/amendments', simulator=SIMULATOR_ON())}"
                f"{banner}"
                f"<p class='eyebrow'>{len(pending)} proposal(s) awaiting the"
                f" lawmakers</p>"
                f"{rows}{agenda}{hist}</div>")


def impact_page(m: dict, principal: str, branch: str | None = None,
                org: str | None = None, scoped: bool = True,
                tenants: list[dict] | None = None) -> str:
    """What the enterprise is getting.

    Every number here is a count from the ledger, and each is paired with the
    sentence that says what it means — a bare governance metric invites the
    reader to supply their own story, usually a flattering one.
    """
    def stat(value, label, meaning, tone=""):
        return f"""
  <div class='stat {tone}'>
    <span class='n'>{value}</span>
    <span class='l'>{_e(label)}</span>
    <p class='m'>{_e(meaning)}</p>
  </div>"""

    total = m["governed"] or 1
    pct = lambda n: f"{round(100 * n / total)}%"

    return page("Impact — Digital Judiciary", f"""
<div class='wrap'>
  {masthead(principal, branch, org, scoped=scoped, tenants=tenants, here='/review/impact')}
  {nav('/review/impact', simulator=SIMULATOR_ON())}
  {grp('Impact')}
  <p class='lede' style='margin:-6px 0 18px'>What this cost, and what it
     bought.</p>

  <div class='stats'>
    {stat(m['governed'], "changes governed",
          "every one carries a written rationale and an auditable chain")}
    {stat(pct(m['cleared']), "cleared without a human",
          "throughput preserved: no person waited on these, and none was "
          "asked to")}
    {stat(m['to_human'], "reached a named human",
          "human judgement was spent here and nowhere else — the scarce "
          "resource, deliberately rationed", "amber")}
    {stat(m['floors'], "held at an absolute floor",
          "never waived, never negotiated, not once escalated around",
          "oxblood")}
  </div>

  <div class='stats'>
    {stat(m['bound'], "decided by citation",
          "like cases decided alike: an existing holding controlled the "
          "outcome instead of a fresh judgement")}
    {stat(m['records'], "precedents written",
          "only contested matters are recorded; the uncontested majority "
          "writes nothing and costs nothing")}
    {stat(m['live_acceptances'], "live risk acceptances",
          "each carries a mandatory expiry — there are no permanent silent "
          "waivers in this system", "amber")}
    {stat(m['lapsed'], "waivers expired and re-examined",
          "risk that would elsewhere have been accepted once and forgotten",
          "oxblood")}
  </div>

  <div class='stats'>
    {stat(m['to_legislature'], "sent to the lawmakers",
          "rulebook changes are never adjudicated as if they were ordinary "
          "work")}
    {stat(m['referrals'], "referrals raised by the judiciary",
          "the system telling its own owners where the rules are "
          "underdetermined")}
    {stat(m['judge_calls'], "model judgements",
          "the only question ever asked of a model is whether a precedent "
          "distinguishes; the decision is never delegated")}
    {stat(m['cache_hits'], "reused rather than re-asked",
          "identical questions are not paid for twice")}
  </div>

  <div class='banner'>
    <h3>Read these as a demonstration, not a benchmark</h3>
    <p>These are counts from a synthetic case-study corpus replayed through
       the real interface. They show the shape of the mechanism — how much
       work clears without a person, how little reaches one, what gets
       written down. They are not evidence about decision quality, which is
       measured separately and against real models.</p>
  </div>
</div>""")


def change_page(v: dict, principal: str, branch: str | None = None,
                org: str | None = None, token: str = "",
                error: str = "") -> str:
    """The engineer's screen: why you are blocked, and how you get unblocked.

    5.5 leads with the routes rather than the disposition. Corollary 2 says a
    denial short of the ceiling always leaves an exit — a person can only use
    an exit they can see, and can only weigh it if they are told what it
    costs, so each route now carries its price. The lanes are still read from
    `lanes_for`, the same function that annotates GitHub, so this screen
    cannot offer an exit the architecture does not.
    """
    disp = v.get("disposition") or "pending"
    kind, meaning = LANES.get(disp, ("", ""))
    lanes = {l["lane"] for l in v.get("lanes_open") or []}
    err = f"<p class='err'>{_e(error)}</p>" if error else ""
    blocked = str(disp).startswith("blocked") or disp == "human_review"

    def route(lane, n, heading, cost, prompt, verb):
        return f"""
<div class='path'>
  <div class='h'><h3>{_e(n)} · {_e(heading)}</h3>
     <span class='badge'>{_e(cost)}</span></div>
  <p>{_e(prompt)}</p>
  <form method='post' action='/review/change/{_e(v['session_id'])}/{lane}'>
    <input type='hidden' name='csrf' value='{_e(token)}'>
    <textarea name='grounds' rows='3'
      placeholder='Why this case is different. Recorded against your name and
                   travels with the case.'></textarea>
    <button class='btn2 ghost' type='submit'>{_e(verb)}</button>
  </form>
</div>"""

    routes, n = "", 1
    if blocked and disp != "blocked_absolute":
        routes += f"""
<div class='path'>
  <div class='h'><h3>{n} · Change the code</h3>
     <span class='badge ok'>fastest</span></div>
  <p>Fix what the rule objects to and push again. The block clears by itself
     and nobody else is involved.</p>
</div>"""
        n += 1
    if "challenge" in lanes:
        routes += route("challenge", n, "Say the rule does not apply here",
                        "minutes",
                        "Explain why this case is different. A stricter "
                        "review takes another look. If it agrees with you, "
                        "you are unblocked. A challenge without a reason is "
                        "not a challenge.",
                        "Send for another look")
        n += 1
    if "human_review" in lanes and disp != "human_review":
        routes += route("human-review", n, "Ask a person to allow it",
                        "usually days",
                        "This uses up the remaining automatic reviews and "
                        "then stops with a named risk owner. If they allow "
                        "it, the exception is temporary and is recorded "
                        "against your team.",
                        "Send to a risk owner")
        n += 1

    if disp == "blocked_absolute":
        routes = """
<div class='path none'>
  <h3>There is no way around this one</h3>
  <p>This rule cannot be waived by anyone — not your lead, not a risk owner,
     not an administrator. The only route is changing the rule itself, which
     the rules team votes on. That takes weeks and is rarely granted.</p>
  <div class='actions'><a class='btn2 ghost' href='/review/amendments'>See
     rule changes</a></div>
</div>"""
    elif disp == "human_review":
        t = (v.get("review_tasks") or [{}])[0]
        seen = (f"<div class='actions'><a class='btn2 ghost'"
                f" href='{_e(t.get('url'))}'>See the decision</a></div>"
                if t.get("url") else "")
        routes = f"""
<div class='path'>
  <h3>It is with a person now</h3>
  <p>Every automatic review is spent. A named risk owner has to decide this,
     and nothing you or the system can do will move it along faster.</p>
  {seen}
</div>"""
    elif not blocked:
        routes = """
<div class='path'>
  <h3>Nothing is blocking you</h3>
  <p>This change cleared. Any conditions attached to it are listed below and
     travel with the merge.</p>
</div>"""

    headline = ("You cannot merge this yet." if blocked
                else "This change is cleared.")

    reasons = ""
    for c in v.get("cases") or []:
        if not str(c.get("disposition") or "").startswith("blocked"):
            continue
        text = (c.get("provision_text") or "").strip().rstrip(".")
        hard = " · cannot be waived" if c.get("absolute") else ""
        reasons += f"""
  <div class='panel'>
    <h3>{_e(c['provision_id'])}{hard}</h3>
    <p class='quote'>{_e(text or say('outcome', c.get('outcome')))}</p>
    <p class='src2'>{_e(c.get('rationale'))}</p>
  </div>"""
    if not reasons:
        reasons = (f"<div class='panel'><h3>Where it stands</h3>"
                   f"<p>{_e(say('disposition', disp))} — {_e(meaning)}. "
                   f"{_e(v.get('reason') or '')}</p></div>")

    clauses = ""
    for c in v.get("cases") or []:
        ctrl = (f"bound by <code>{_e((c.get('controlling') or '')[:8])}</code>"
                if c.get("controlling") else
                f"no earlier decision applied — "
                f"{_e(say('controlling_state', c.get('controlling_state')))}")
        floor = "floor" if c.get("absolute") else ""
        hard = ("<span class='org'>cannot be waived</span>"
                if c.get("absolute") else "")
        clauses += f"""
  <div class='r {floor}'>
    <div class='mark'></div>
    <div class='pid'>{_e(c['provision_id'])} {hard}</div>
    <div><p class='hold'>{_e(say('outcome', c.get('outcome')))}</p>
      <div class='meta'>level {_e(c.get('tier'))} · {ctrl}</div>
      <div class='meta'>{_e(c.get('rationale'))}</div></div>
    <div class='st'>{_e(say('disposition', c.get('disposition')))}</div>
    <div class='when'></div>
  </div>"""
    clauses = (f"<div class='reg'>{clauses}</div>" if clauses else
               "<p class='opinion'>No rule was engaged by this change, so"
               " nothing was decided.</p>")

    not_reached = ""
    if v.get("not_reached"):
        items = "".join(f"<li>{_e(p)}</li>" for p in v["not_reached"])
        not_reached = f"""
<p class='eyebrow'>Never looked at</p>
<ul class='facts'>{items}</ul>
<p class='legend'>A rule that cannot be waived blocked this first, so these
   were never reached. They were not considered and dismissed — they were not
   considered at all, and the record says so rather than implying a judgement
   nobody made.</p>"""

    facts = "".join(f"<li>{_e(f)}</li>" for f in v.get("factors") or [])
    trail = "".join(
        f"<li><span class='t'>{_e(say('disposition', h['disposition']))}</span>"
        f"<span class='stamp'>{_e(h['occurred_at'][:19].replace('T', ' '))}"
        f" · {_e(h['actor'])} · {_e(h['reason'])}</span></li>"
        for h in v.get("history") or [])
    history = (f"<p class='eyebrow'>History</p><ul class='spine'>{trail}</ul>"
               if trail else "")
    heading = "Ways forward" if blocked else "Where it stands"

    return page(f"{v['repo']}#{v['pr_number']} — change", f"""
<div class='wrap'>
  {masthead(principal, branch, org)}
  {nav('/review/changes', simulator=SIMULATOR_ON())}
  <p class='crumb'><a href='/review/changes'>&larr; All changes</a> ·
     {_e(v['repo'])}#{_e(v['pr_number'])}</p>
  <div class='focus'>
    <h1 class='q'>{_e(headline)}</h1>
    {err}
    {reasons}
    {grp(heading)}
    <div class='paths'>{routes}</div>

    <details class='more'>
      <summary>Rule by rule, and what was read from the change</summary>
      {clauses}
      {not_reached}
      <p class='eyebrow'>Read from the change</p>
      <ul class='facts'>{facts}</ul>
      <dl class='caption'>
        <dt>Session</dt><dd>{_e(v['session_id'])}</dd>
        <dt>Commit</dt><dd>{_e((v.get('head_sha') or '')[:12])}</dd>
        <dt>Author</dt><dd>{_e(v.get('pr_author'))}</dd>
        <dt>Filed by</dt><dd>{_e(v.get('filed_by'))}</dd>
        <dt>Reader version</dt><dd>{_e(v.get('extractor_version'))}</dd>
        <dt>Escalation</dt>
        <dd class='plain'>{_e(v.get('escalation_policy'))}</dd>
      </dl>
      <p class='legend'>Pinned to reader
         <code>{_e(v.get('extractor_version'))}</code>, so this change can be
         replayed against exactly the reading that produced it.</p>
      {history}
    </details>
  </div>
</div>""")


def admin_page(tenants: list[dict], job: dict, principal: str,
               branch: str | None = None, org: str | None = None,
               token: str = "", error: str = "") -> str:
    """The simulator console. Rendered only when DJ_SIMULATOR=1.

    Deliberately plain about what the button does, because a control that
    calls a model and writes to the ledger should not look like a toggle.
    """
    state = job.get("state", "idle")
    running = state in ("generating", "adjudicating")
    opts = "".join(f"<option value='{_e(t['org_id'])}'>{_e(t['name'])}"
                   f"</option>" for t in tenants)
    err = f"<p class='err'>{_e(error)}</p>" if error else ""

    if state == "done":
        disp = "".join(
            f"<div class='r'><div class='mark'></div>"
            f"<div class='pid'>{_e(k)}</div><div></div>"
            f"<div class='st'>{v}</div><div class='when'></div></div>"
            for k, v in sorted(job.get("dispositions", {}).items(),
                               key=lambda kv: -kv[1]))
        dropped = ""
        if job.get("dropped_count"):
            items = "".join(f"<li>{_e(d)}</li>" for d in job.get("dropped", []))
            dropped = (f"<p class='eyebrow'>Rejected before filing "
                       f"({job['dropped_count']})</p><ul class='facts'>{items}"
                       f"</ul><p class='legend'>Proposals referencing a fact "
                       f"or clause this company does not have are dropped, "
                       f"not corrected. The model may not widen the "
                       f"vocabulary it was given.</p>")
        result = f"""
<div class='instrument'>
  <h2>{job.get('filed', 0)} generated changes are in the docket</h2>
  <p class='opinion'>{_e(job.get('made', 0))} proposals came back from
     <code>{_e(job.get('model'))}</code> and were filed through the same
     intake a real pull request uses. The dispositions below are this
     system's, not the model's.</p>
  <div class='reg'>{disp}</div>
  {dropped}
  <div class='actions'><a class='open' href='/review/changes'>See them in the
     change stream</a></div>
</div>"""
    elif state == "failed":
        result = (f"<div class='instrument judicial'><h2>Run failed</h2>"
                  f"<p class='opinion'>{_e(job.get('error'))}</p></div>")
    elif running:
        result = f"""
<div class='instrument'>
  <h2>Working…</h2>
  <p class='opinion'>{_e(job.get('phase', ''))} — {job.get('made', 0)} of
     {job.get('target', 0)} proposed, {job.get('filed', 0)} filed.</p>
  <p class='legend'>This page refreshes itself. Generation is a few model
     calls; filing then runs each change through real adjudication.</p>
</div>"""
    else:
        result = ""

    form = "" if running else f"""
<div class='instrument'>
  <h2>Generate a fresh docket</h2>
  <p class='opinion'>Asks <code>{_e(job.get('model') or 'claude-sonnet-4-6')}
     </code> to invent plausible changes against a company's actual
     constitution, then files each one through the ordinary intake. The model
     proposes <strong>facts only</strong> — what happens to each change is
     decided here, by the same tiers, precedent and floors as everything
     else.</p>
  {err}
  <form method='post' action='/review/admin/generate'>
    <input type='hidden' name='csrf' value='{_e(token)}'>
    <label class='legend'>Company</label>
    <select name='company'>{opts}</select>
    <label class='legend'>How many</label>
    <select name='n'>
      <option value='10'>10 — quick</option>
      <option value='25'>25</option>
      <option value='100' selected>100 — a full corpus</option>
    </select>
    <div class='actions'><button type='submit'>Generate and adjudicate
       </button></div>
  </form>
  <p class='legend'>This costs real API calls and writes real records to the
     ledger. Generated changes are filed under a <code>generated/</code>
     repository prefix so they are never confused with the case study.</p>
</div>"""

    meta = ("<meta http-equiv='refresh' content='3'>" if running else "")
    return page("Simulator — Digital Judiciary", f"""
<div class='wrap'>
  {meta}
  {masthead(principal, branch, org)}
  {nav('/review/admin', simulator=True)}
  <p class='eyebrow'>Live scenario generation — off unless DJ_SIMULATOR=1</p>
  {form}
  {result}
</div>""")


def analytics_page(a: dict, principal: str, branch: str | None = None,
                   org: str | None = None) -> str:
    """What adjudication cost, broken out by how far each case escalated.

    The shape of this table is the argument. Cost is concentrated at the
    bottom, where the work is; each rung up costs more per case and serves
    fewer of them; and the most expensive rung is not a model at all.
    """
    rows = ""
    for t in a["tiers"]:
        human = t["tier"] >= a["k"]
        rows += f"""
  <tr{" class='human'" if human else ""}>
    <td class='t'>Tier {t['tier']}{' — a person' if human else ''}</td>
    <td class='n'>{t['cases']}</td>
    <td class='n'>{t['paid']}</td>
    <td class='n'>{t['cached']}</td>
    <td class='n'>{t['tokens_in'] or '—'}</td>
    <td class='n'>{t['tokens_out'] or '—'}</td>
    <td class='n'>{t['latency']} ms</td>
    <td class='n'>{'human time' if human and not t['paid']
                   else t['cost_display']}</td>
    <td class='n'>{t['per_case']}</td>
  </tr>"""

    warn = ""
    if a["degraded"]:
        warn = (f"<div class='banner'><h3>{a['degraded']} degraded"
                f" judgement(s)</h3><p>A call timed out or failed to parse and"
                f" the verdict fell back per §12. Cost figures below are real,"
                f" but those decisions were made on a weaker basis — read them"
                f" with that in mind.</p></div>")

    mode = ("the deterministic oracle — no model was called, so the money"
            " column is zero by construction and only the call counts and"
            " latencies are meaningful"
            if a["oracle_only"] else
            f"a live model at the judge position, priced at"
            f" ${a['price_in']}/M input and ${a['price_out']}/M output")

    return page("Analytics — Digital Judiciary", f"""
<div class='wrap'>
  {masthead(principal, branch, org)}
  {nav('/review/analytics', simulator=SIMULATOR_ON())}
  <p class='eyebrow'>Adjudication cost, by how far a case escalated</p>

  <div class='stats'>
    <div class='stat'><span class='n'>{a['cases']}</span>
      <span class='l'>cases adjudicated</span>
      <p class='m'>each one carries a rationale and a provenance chain</p></div>
    <div class='stat'><span class='n'>{a['calls_paid']}</span>
      <span class='l'>judge calls paid for</span>
      <p class='m'>{a['calls_cached']} more were answered from cache and cost
         nothing</p></div>
    <div class='stat'><span class='n'>{a['mean_calls']}</span>
      <span class='l'>mean calls per case</span>
      <p class='m'>the whole model bill for one governed decision</p></div>
    <div class='stat {'amber' if not a['oracle_only'] else ''}'>
      <span class='n'>{a['mean_cost_display']}</span>
      <span class='l'>mean cost per case</span>
      <p class='m'>{a['mean_contested_display']} for a case somebody actually
         contested</p></div>
  </div>

  {warn}

  <p class='eyebrow'>Per level of escalation</p>
  <table class='cost'>
    <thead><tr>
      <th>Level</th><th>Cases ending here</th><th>Calls paid</th>
      <th>Reused</th><th>Tokens in</th><th>Tokens out</th>
      <th>Mean latency</th><th>Cost</th><th>Per case</th>
    </tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <p class='legend'>Running on {mode}. Token counts are what the API
     reported, not an estimate; a cache hit is recorded with no usage because
     no call went out. Rates are set with <code>DJ_PRICE_IN</code> and
     <code>DJ_PRICE_OUT</code> (dollars per million tokens) and should be
     checked against current pricing — this system does not know what you are
     charged.</p>

  {grp('What the shape means')}
  <p class='opinion'>{_e(a['reading'])}</p>

  <div class='banner'>
    <h3>What is not counted here</h3>
    <p>Human time. A case that reaches the top rung stops costing model calls
       and starts costing a named person's attention, which is the expensive
       resource this architecture exists to ration. {a['to_human']} case(s)
       reached that rung. Cost is also measured container-wide rather than
       per tenant: the judge records which tier asked, not which company, so
       splitting this bill by tenant would need the judge to carry a tenant
       it currently has no reason to know.</p>
  </div>
</div>""")


ACTIVITY_KINDS = {
    "change": ("Change received", "a pull request arrived and became cases"),
    "decision": ("Decision issued", "a disposition went back to the change"),
    "review": ("Review", "a named person was asked, or answered"),
    "precedent": ("Precedent written", "a contested matter became citable"),
    "lifecycle": ("Lifecycle", "a waiver expired, or a referral was emitted"),
    "amendment": ("Legislative", "a proposal was filed or disposed of"),
}


def activity_page(rows: list[dict], counts: dict, tenants: list[dict],
                  f: dict, next_cursor: str | None, principal: str,
                  branch: str | None = None, org: str | None = None,
                  scoped: bool = True) -> str:
    """Everything that has been through the system, newest first.

    A statement, in the sense a card statement is one: every event that
    touched the ledger on one line, in time order, filterable. The other
    desks each answer a role's question; this one answers "what happened",
    which is the question an auditor, an investigator, or anyone reconciling
    a dispute actually starts from.
    """
    def q(**kw):
        base = dict(f)
        base.update(kw)
        base.pop("cursor", None)
        parts = [f"{k}={urllib.parse.quote(str(v))}"
                 for k, v in base.items() if v]
        return "/review/activity" + ("?" + "&".join(parts) if parts else "")

    kinds = "".join(
        f"<a class='{'on' if f.get('kind') == k else ''}' href='{q(kind=k)}'>"
        f"<span class='k'>{_e(ACTIVITY_KINDS[k][0])}</span>"
        f"<span class='v'>{counts.get(k, 0)}</span></a>"
        for k in ACTIVITY_KINDS)
    tally = (f"<div class='tally'>"
             f"<a class='{'on' if not f.get('kind') else ''}' href='{q(kind=None)}'>"
             f"<span class='k'>Everything</span>"
             f"<span class='v'>{sum(counts.values())}</span></a>{kinds}</div>")

    tenant_filter = ""
    if not scoped and tenants:
        opts = "".join(
            f"<option value='{_e(t['org_id'])}'"
            f"{' selected' if f.get('tenant') == t['org_id'] else ''}>"
            f"{_e(t['name'])}</option>" for t in tenants)
        tenant_filter = (f"<select name='tenant'><option value=''>every"
                         f" tenant</option>{opts}</select>")

    controls = f"""
<form method='get' action='/review/activity' class='filters'>
  <input type='hidden' name='kind' value='{_e(f.get('kind') or '')}'>
  <input type='search' name='q' value='{_e(f.get('q') or '')}'
         placeholder='search id, actor, provision, repository'>
  {tenant_filter}
  <select name='since'>
    <option value=''{'' if f.get('since') else ' selected'}>all time</option>
    <option value='1'{' selected' if f.get('since') == '1' else ''}>last 24 hours</option>
    <option value='7'{' selected' if f.get('since') == '7' else ''}>last 7 days</option>
    <option value='30'{' selected' if f.get('since') == '30' else ''}>last 30 days</option>
  </select>
  <button type='submit'>Filter</button>
  <a class='open' href='/review/activity'>Clear</a>
</form>"""

    names = {t["org_id"]: t["name"] for t in (tenants or [])}
    body = ""
    # `what` is a stored enum for most kinds — a disposition, an event type,
    # an origin. Translate by kind, or the feed reads "lapsed / lapsed /
    # lapsed" down the page.
    def phrase(row):
        k, w = row["kind"], row["what"]
        if k == "decision":
            return say("disposition", w)
        if k == "lifecycle":
            return say("event", w)
        if k == "precedent" and " — " in str(w):
            pid, _, outcome = str(w).partition(" — ")
            return f"{pid} — {say('outcome', outcome)}"
        if k == "amendment":
            origin, _, status = str(w).partition(" — ")
            return (f"{say('origin', origin)}"
                    f"{' — ' + say('status', status) if status else ''}")
        if k == "review":
            return {"accept": "Risk accepted", "decline": "Denial upheld",
                    "decline_barred": "Denial upheld — renewal barred"
                    }.get(str(w), str(w))
        return w

    for r in rows:
        label, _meaning = ACTIVITY_KINDS.get(r["kind"], (r["kind"], ""))
        body += f"""
  <div class='r {_e(r.get('tone') or '')}'>
    <div class='mark'></div>
    <div class='when'>{_e((r['at'] or '')[:10])}<span class='tm'>
      {_e((r['at'] or '')[11:19])}</span></div>
    <div class='kind'>{_e(label)}</div>
    <div>{f"<a class='rec' href='{_e(r['url'])}'>" if r.get('url') else ""}
      <p class='hold'>{_e(phrase(r))}</p>
      <div class='meta'>{_e(r['detail'])}</div>
      {"</a>" if r.get('url') else ""}</div>
    <div class='st'>{_e(r.get('actor') or '')}</div>
    <div class='org'>{_e(names.get(r.get('organization'))
                          or r.get('organization') or 'platform')}</div>
  </div>"""
    # A header, because six unlabelled columns is a puzzle rather than a
    # statement — and the tenant column especially needs naming: "where did
    # this happen" is the first question anyone asks of a shared ledger.
    header = """
  <div class='r head'>
    <div class='mark'></div>
    <div class='when'>When</div>
    <div class='kind'>Kind</div>
    <div>What happened</div>
    <div class='st'>Who did it</div>
    <div class='org'>Company</div>
  </div>"""
    listing = (f"<div class='reg activity'>{header}{body}</div>" if rows else
               "<div class='empty'><h2>Nothing matches</h2><p>No event in the"
               " ledger fits these filters.</p></div>")

    older = (f"<a href='{q()}{'&' if '?' in q() else '?'}cursor="
             f"{urllib.parse.quote(next_cursor)}'>Older &rarr;</a>"
             if next_cursor else "")

    return page("Activity — Digital Judiciary", f"""
<div class='wrap'>
  {masthead(principal, branch, org, scoped=scoped, tenants=tenants,
            here='/review/activity')}
  {nav('/review/activity', simulator=SIMULATOR_ON())}
  {activity_subnav('/review/activity')}
  {grp('Activity')}
  {tally}
  {controls}
  {listing}
  <div class='pager'><span class='count'>{len(rows)} event(s)</span>{older}
  </div>
  <p class='legend'>Assembled from the ledger itself rather than a separate
     log: changes, dispositions, reviews, precedents, lifecycle events and
     legislative acts, in the order they happened. Nothing here is written
     twice, so there is no second record to drift out of step with the
     first.</p>
</div>""")


# ===========================================================================
# The rulebook, for people who are not lawyers
# ===========================================================================
# ===========================================================================
# Machine words -> English
# ===========================================================================
# Every value below is an enum the system stores. Storing `blocked_absolute`
# is right; showing it to a person is not. These are the words the screens
# use, defined once so a disposition cannot read one way on the change list
# and another on the docket.
WORDS = {
    "disposition": {
        "proceed": "Cleared",
        "proceed_with_conditions": "Cleared, with conditions",
        "blocked_challengeable": "Blocked — you can contest this",
        "blocked_absolute": "Blocked by a rule that cannot be waived",
        "blocked_final": "Blocked — no further appeal",
        "human_review": "Waiting for a named risk owner",
        "routed_amendment": "Sent to the lawmakers",
        "ignored": "Not something this system judges",
        "pending": "Not yet decided",
    },
    "outcome": {
        "permit": "Allowed",
        "deny": "Denied",
        "permit_conditional": "Allowed, with conditions",
        "accept_risk": "Risk accepted by a named person",
    },
    "controlling_state": {
        "bound": "Followed an earlier decision",
        "none_empty": "No earlier decision on these facts",
        "none_all_distinguished": "Earlier decisions did not fit these facts",
        "none_tie": "Earlier decisions conflicted and could not be ranked",
        "absolute_short_circuit": "Stopped at a rule that cannot be waived",
        "promoted": "Ratified for every company",
        "n/a": "—",
    },
    "scope_level": {
        "platform": "shared with every company",
        "org": "company-wide",
        "service": "one service",
        "team": "one team",
        "domain": "one domain",
    },
    "origin": {
        "control_plane_routed": "Someone edited the rulebook files",
        "risk_acceptance_referral": "A waiver expired",
        "judicial_referral": "Raised by the review tiers",
        "lifecycle_referral": "Raised by routine housekeeping",
        "holding_promotion": "Request to share a decision with every company",
        "adjudication_tier": "Raised by a review tier",
        "engineer": "Proposed by a person",
        "lawmaker": "Proposed by the lawmakers",
    },
    "status": {
        "pending": "Waiting for the lawmakers",
        "adopted": "Adopted — this is the rule now",
        "rejected": "Rejected — the rule is unchanged",
        "withdrawn": "Withdrawn before it was decided",
    },
    "event": {
        "lapsed": "Waiver expired",
        "superseded": "Retired — the rule was changed",
        "referral_emitted": "Referred to the lawmakers",
        "referral_adopted": "The lawmakers adopted the referral",
        "referral_rejected": "The lawmakers rejected the referral",
        "referral_withdrawn": "Referral withdrawn",
        "renewed_by": "Renewed by a later waiver",
        "outcome_recorded": "Outcome recorded",
    },
}


def say(kind: str, value, fallback: str | None = None) -> str:
    """The English for a stored value, falling back to a readable form.

    Unknown values are de-underscored rather than dropped: a new enum should
    read awkwardly, not vanish.
    """
    if value is None:
        return fallback or "—"
    v = str(value)
    return WORDS.get(kind, {}).get(v, fallback or v.replace("_", " "))


def _plain(name: str) -> str:
    return str(name).replace("_", " ")


def _plain_list(items: list[str]) -> str:
    items = [_plain(i) for i in items]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " or " + items[-1]


def appeal_tag(p: dict) -> tuple[str, str]:
    """(css class, label) for what recourse a rule allows.

    This is the same forty words on every clause — what you may do when it
    blocks you — and repeating it twenty-one times buries the one line that
    differs. Said once in the legend, it becomes a tag.
    """
    if p.get("absolute"):
        return "floor", "No appeal"
    return "appeal", "Appeal allowed"


def explain_provision(p: dict, brief: bool = False) -> str:
    """What this clause means, in words, derived from the predicate itself.

    Generated from the rule rather than written alongside it, so it cannot
    drift from what the system will actually do. A hand-written summary that
    disagrees with the predicate is worse than none: it is a promise the
    machine will not keep.
    """
    triggers = (p.get("policy") or {}).get("deny_if_any") or []
    if not triggers:
        return ("On the books, but currently stops nothing: no fact has been "
                "listed that triggers it.")
    what = _plain_list(triggers)
    if brief:
        # Only the part that differs between rules. What happens next is a
        # tag, explained once at the top of the page.
        return f"Blocks a change involving {what}."
    if p.get("absolute"):
        return (f"If your change involves {what}, it is blocked and stays "
                f"blocked. There is no appeal, no waiver, and nobody — not "
                f"an engineer, not a risk owner — can let it through. The "
                f"only way past this is to change the rule itself.")
    return (f"If your change involves {what}, it is blocked. You can contest "
            f"that decision, and if you still disagree you can ask a named "
            f"risk owner to accept the risk and let it proceed. Whoever does "
            f"that puts their name on it, and the acceptance expires.")


def source_of(p: dict, override: bool, tenant_name: str | None) -> tuple:
    """(label, plain explanation) for where a clause comes from."""
    if override:
        return ("override", f"{tenant_name or 'This tenant'}'s own version of "
                            f"a shared rule. It applies here instead of the "
                            f"shared one, and it can only be stricter.")
    if p.get("organization"):
        return ("tenant", f"{tenant_name or 'This tenant'}'s own rule. No "
                          f"other company is governed by it.")
    return ("shared", "A shared rule. Every tenant on the platform is "
                      "governed by it unless they have their own stricter "
                      "version.")


AMENDMENT_ORIGIN_LONG = {
    "judicial_referral": "Raised by the adjudication tiers — they hit a"
                         " conflict or a repeatedly waived rule and referred"
                         " it upward",
    "risk_acceptance_referral": "Raised automatically when a risk acceptance"
                                " expired: should this exception become the"
                                " rule?",
    "control_plane_routed": "Somebody changed the rulebook repository; that is"
                            " never adjudicated, it comes here",
    "holding_promotion": "A request to make one tenant's decision apply to"
                         " everyone",
    "lifecycle_referral": "Raised by the system's own housekeeping",
    "engineer": "Proposed by a person",
    "lawmaker": "Proposed by the lawmakers themselves",
    "adjudication_tier": "Raised by an adjudication tier",
}

AMENDMENT_STATUS = {
    "pending": ("wait", "Waiting for the lawmakers to decide"),
    "adopted": ("", "Adopted — this is the rule now"),
    "rejected": ("deny", "Rejected — the rule is unchanged"),
    "withdrawn": ("deny", "Withdrawn before it was decided"),
}


def rulebook_subnav(active: str) -> str:
    tabs = (("/review/rulebook", "In force now"),
            ("/review/rulebook/history", "How it got here"))
    return "<nav class='desks sub'>" + "".join(
        f"<a class='{'on' if h == active else ''}' href='{h}'>{_e(l)}</a>"
        for h, l in tabs) + "</nav>"


def rulebook_page(rows: list[dict], version: str, tenant_name: str | None,
                  principal: str, branch: str | None = None,
                  org: str | None = None) -> str:
    floors = sum(1 for p in rows if p.get("absolute"))
    shared = sum(1 for p in rows if not p.get("organization"))
    live = sum(p.get("live_waivers", 0) for p in rows)

    # Floors first. "Which rules can I not argue with?" is the first question
    # anybody has of a rulebook, and answering it by making the reader scan
    # 21 cards for a tag is answering it badly. Within each group, id order.
    ordered = sorted(rows, key=lambda p: (0 if p.get("absolute") else 1,
                                          p["provision_id"]))
    body = ""
    seen_group = None
    for p in ordered:
        group = bool(p.get("absolute"))
        if group != seen_group:
            seen_group = group
            body += (
                "<p class='eyebrow' style='margin-top:26px'>Cannot be waived"
                " by anyone</p>" if group else
                "<p class='eyebrow' style='margin-top:26px'>Can be contested,"
                " and waived by a named risk owner</p>")
        kind, why = source_of(p, p.get("is_override"), tenant_name)
        acls, alabel = appeal_tag(p)
        triggers = (p.get("policy") or {}).get("deny_if_any") or []
        chips = "".join(f"<span class='trig'>{_e(_plain(t))}</span>"
                        for t in triggers)
        used = (f"{p.get('holdings', 0)} decision(s)"
                if p.get("holdings") else "never yet applied")
        waivers = (f" · <span class='warn'>{p['live_waivers']} live waiver(s)"
                   f"</span>" if p.get("live_waivers") else "")
        body += f"""
  <div class='clause{' floor' if p.get('absolute') else ''}'>
    <div class='head'>
      <span class='pid'>{_e(p['provision_id'])}</span>
      <span class='src {acls}'>{_e(alabel)}</span>
      <span class='src {kind}'>{_e(kind)}</span>
      <span class='age'>{_e(used)}{waivers}</span>
    </div>
    <p class='formal'>{_e(p['text'])}</p>
    {f"<p class='blocks'><span class='lbl'>Blocks</span>{chips}</p>"
     if chips else
     "<p class='blocks'><span class='lbl'>Blocks nothing yet</span></p>"}
  </div>"""

    # Said once, so it does not have to be said on every rule.
    legend = """
<div class='legend-box'>
  <p><span class='src appeal'>Appeal allowed</span> If this rule blocks your
     change you can contest the decision, and if you still disagree ask a
     named risk owner to accept the risk. Whoever does puts their name on it,
     and the acceptance expires.</p>
  <p><span class='src floor'>No appeal</span> A floor. No contest, no waiver,
     nobody can let it through — not an engineer, not a risk owner. The only
     way past it is to change the rule.</p>
  <p><span class='src shared'>shared</span> applies to every company ·
     <span class='src tenant'>tenant</span> yours alone ·
     <span class='src override'>override</span> your stricter version of a
     shared rule</p>
</div>"""

    return page("Rulebook — Digital Judiciary", f"""
<div class='wrap'>
  {masthead(principal, branch, org)}
  {nav('/review/rulebook', simulator=SIMULATOR_ON())}
  {rulebook_subnav('/review/rulebook')}
  {grp('Rules in force', 'version ' + str(version))}
  <p class='lede' style='margin:-6px 0 16px'>The rules every change is
     measured against right now{f", as they apply to {_e(tenant_name)}"
                                 if tenant_name else ""}.</p>
  <div class='tally'>
    <div><span class='k'>Rules in force</span>
         <span class='v'>{len(rows)}</span></div>
    <div><span class='k'>Cannot be waived</span>
         <span class='v lapsed'>{floors}</span></div>
    <div><span class='k'>Shared</span><span class='v'>{shared}</span></div>
    <div><span class='k'>Live waivers</span>
         <span class='v{' amber' if live else ''}'>{live}</span></div>
  </div>
  {legend}
  {body or "<div class='empty'><h2>No rules in force</h2></div>"}
</div>""")


def rulebook_history_page(rows: list[dict], principal: str,
                          branch: str | None = None, org: str | None = None
                          ) -> str:
    body = ""
    for a in rows:
        b = json.loads(a["body"] or "{}")
        tone = {"pending": "wait", "adopted": "",
                "rejected": "deny", "withdrawn": "deny"}.get(a["status"], "")
        status_words = say("status", a["status"])
        origin = say("origin", a["origin"])
        changes = b.get("changes") or []
        if changes:
            names = _plain_list([c.get("provision_id", "?") for c in changes])
            what = f"Changes {names}."
        elif b.get("provision_id"):
            what = f"Concerns {b['provision_id']}."
        else:
            what = "No specific rule named."

        effect = ""
        if a["status"] == "adopted":
            if b.get("supersedes_precedent") is False:
                effect = ("Wording only: past decisions made under this rule "
                          "still stand.")
            elif changes:
                effect = ("Where a rule's meaning changed, past decisions "
                          "made under the old wording no longer apply to new "
                          "cases. They stay in the ledger; they just stop "
                          "controlling.")
        note = b.get("note") or b.get("question") or ""

        body += f"""
  <div class='clause {tone}'>
    <div class='head'>
      <span class='pid'>{_e((a['created_at'] or '')[:10])}</span>
      <span class='src {tone or 'shared'}'>{_e(status_words)}</span>
    </div>
    <p class='formal'>{_e(what)}</p>
    <p class='human'>{_e(origin)}.{f" {_e(note)}" if note else ""}</p>
    {f"<p class='human'>{_e(effect)}</p>" if effect else ""}
    <p class='prov-meta'>Proposed by {_e(a['proposed_by'])}
       {f"· decided by {_e(a['decided_by'])}" if a['decided_by'] else ""}
       &nbsp;·&nbsp; {_e(a['organization'] or 'platform-wide')}</p>
  </div>"""

    return page("Rulebook history — Digital Judiciary", f"""
<div class='wrap'>
  {masthead(principal, branch, org)}
  {nav('/review/rulebook', simulator=SIMULATOR_ON())}
  {rulebook_subnav('/review/rulebook/history')}
  {grp('How the rules got here')}
  <p class='opinion'>Rules only change through this channel. Nothing else in
     the system can alter what is enforced — not an adjudication, not a risk
     acceptance, not an administrator.</p>
  {body or "<div class='empty'><h2>No proposals yet</h2><p>The rulebook has"
           " never been amended.</p></div>"}
</div>""")


# ===========================================================================
# AI judge activity — every question put to a model, and what came back
# ===========================================================================
def judge_activity_page(rows: list[dict], stats: dict, principal: str,
                        branch: str | None = None, org: str | None = None,
                        f: dict | None = None, next_cursor: str | None = None,
                        tenants: list[dict] | None = None) -> str:
    """The complete record of the system's dealings with a model.

    This is the page that answers "what did you actually ask it, and what did
    it say" — the question anyone auditing an AI-assisted decision starts
    from, and the one the architecture is built to be able to answer.

    The QUESTION is reconstructed from the case facts and the candidate's
    premise rather than read back from a stored prompt string, because the
    prompt is not stored. That is the better arrangement: a saved copy can
    drift from what was really sent, whereas this is derived from the same
    ledger fields the call was built from, and the template version is
    recorded beside it so the exact wording is recoverable.
    """
    f = f or {}

    def q(**kw):
        base = dict(f)
        base.update(kw)
        base.pop("cursor", None)
        parts = [f"{k}={urllib.parse.quote(str(v))}"
                 for k, v in base.items() if v]
        return "/review/activity/judge" + ("?" + "&".join(parts)
                                           if parts else "")

    tabs = "".join(
        f"<a class='{'on' if f.get('view') == k else ''}' href='{q(view=k)}'>"
        f"<span class='k'>{lbl}</span><span class='v{cls}'>{stats.get(k, 0)}"
        f"</span></a>"
        for k, lbl, cls in (
            (None, "Every question", ""),
            ("paid", "Actually asked", ""),
            ("cached", "Answered from cache", ""),
            ("disagreed", "Set a precedent aside", ""),
            ("quorum", "Put to a vote", ""),
            ("degraded", "Failed and fell back",
             " lapsed" if stats.get("degraded") else "")))

    banner = ""
    if stats.get("mode") == "oracle":
        banner = """
<div class='banner'>
  <h3>No model was called</h3>
  <p>This ledger was built with the deterministic oracle — the paper's own
     definition of distinguishing, executed as a rule. The questions below
     were answered by arithmetic, not by a model. Run with
     <code>DJ_JUDGE_MODE=llm</code> to put a model at this position.</p>
</div>"""
    elif stats.get("degraded"):
        banner = f"""
<div class='banner'>
  <h3>{stats['degraded']} answer(s) did not come from the model</h3>
  <p>A call timed out or returned something unparseable, and the system fell
     back rather than failing. Those decisions were made on a weaker basis
     than the rest, and any analysis of this run should exclude them.</p>
</div>"""

    body = ""
    for r in rows:
        tone = ("lapsed" if r["degraded"] else
                "" if not r["distinguished"] else "wait")
        premise = ", ".join(_plain(x) for x in r["premise"]) or "nothing"
        facts = ", ".join(_plain(x) for x in r["facts"]) or "nothing"
        missing = [x for x in r["premise"] if x not in r["facts"]]
        answer = ("Yes — set aside" if r["distinguished"]
                  else "No — it still applies")
        cost = ""
        if r["in_tok"] or r["out_tok"]:
            cost = (f" · {r['in_tok']}+{r['out_tok']} tokens"
                    f" · {r['latency_ms']} ms")
        elif r["latency_ms"]:
            cost = f" · {r['latency_ms']} ms"

        body += f"""
  <div class='qa {tone}'>
    <div class='qa-head'>
      <span class='pid'>{_e(r['provision_id'] or '—')}</span>
      <span class='src'>{_e(r['judge'])}</span>
      <span class='src'>tier {_e(r['tier'])}</span>
      {"<span class='src'>from cache — not re-asked</span>"
       if r['from_cache'] else ""}
      {"<span class='src floor'>fell back</span>" if r['degraded'] else ""}
      {f"<span class='src'>{r['votes']} votes</span>" if r['votes'] else ""}
      <span class='when'>{_e((r['at'] or '')[:19].replace('T', ' '))}</span>
    </div>
    <p class='ask'><span class='lbl'>Asked</span>
       Does an earlier decision that rested on <strong>{_e(premise)}</strong>
       still apply to a change involving <strong>{_e(facts)}</strong>?</p>
    <p class='said'><span class='lbl'>Answered</span>
       <strong>{_e(answer)}</strong>
       {f"— {_e(r['grounds'])}" if r['grounds'] else ""}</p>
    <p class='prov-meta'>{_e(r['prompt_version'])}{_e(cost)}
       {f" · the earlier decision needed {_e(', '.join(_plain(m) for m in missing))}, which this change does not have"
        if missing and r['distinguished'] else ""}</p>
  </div>"""

    listing = (body or "<div class='empty'><h2>Nothing to show</h2>"
                       "<p>No distinguishing question matches this view.</p>"
                       "</div>")
    older = (f"<div class='pager'><span class='count'>{len(rows)} question(s)"
             f"</span><a href='{q()}{'&' if '?' in q() else '?'}cursor="
             f"{urllib.parse.quote(next_cursor)}'>Older &rarr;</a></div>"
             if next_cursor else
             f"<div class='pager'><span class='count'>{len(rows)} question(s)"
             f"</span></div>")

    return page("AI judge activity — Digital Judiciary", f"""
<div class='wrap'>
  {masthead(principal, branch, org)}
  {nav('/review/activity', simulator=SIMULATOR_ON())}
  {activity_subnav('/review/activity/judge')}
  {grp('AI judge activity')}
  <p class='opinion'>The judge is asked one question and only one: does an
     earlier decision's reasoning still apply here? It never decides an
     outcome. What follows is the complete record of those exchanges —
     including the ones answered from cache, which cost nothing and were not
     re-asked.</p>
  <div class='tally'>{tabs}</div>
  {banner}
  {listing}
  {older}
  <p class='legend'>Questions are reconstructed from the case facts and the
     earlier decision's premise, not from a saved copy of the prompt. A saved
     copy can drift from what was really sent; this is built from the same
     ledger fields the call itself was built from, and
     <code>{_e(stats.get('prompt_version') or 'the template version')}</code>
     identifies the exact wording used.</p>
</div>""")


def activity_subnav(active: str) -> str:
    tabs = (("/review/activity", "Everything"),
            ("/review/activity/judge", "AI judge"))
    return "<nav class='desks sub'>" + "".join(
        f"<a class='{'on' if h == active else ''}' href='{h}'>{_e(l)}</a>"
        for h, l in tabs) + "</nav>"


# ===========================================================================
# The desk — what is waiting for YOU
# ===========================================================================
# Every role has work; only the risk owner had a desk. A lawmaker signing in
# saw "no decisions waiting", which is true of the risk-owner queue and says
# nothing about the amendments sitting unread with their name on them.
#
# The desk answers one question for whoever is looking: what needs me, and
# what have I already done? It never invents authority — the items shown are
# the ones this principal can actually act on, which is exactly the set the
# Kernel would permit.
def desk_page(items: dict, principal: str, branch: str | None = None,
              org: str | None = None, scoped: bool = True,
              tenants: list[dict] | None = None,
              is_auditor: bool = False) -> str:
    """The landing screen: what this person has to do, in their words.

    An auditor holds no branch, so branch alone cannot tell them from an
    engineer — and they were landing on the engineer's desk, which is about
    changes they did not file and cannot contest. Reading everything and
    signing nothing is a distinct position here, and it gets its own desk.

    5.5 restyles each block as a titled section with a one-line reason and a
    plain heading, and the role is named in the words the person would use of
    themselves rather than the branch name.
    """
    role = ("auditor" if is_auditor else
            {"risk_owner": "risk owner", "lawmakers": "rules team",
             "judges": "adjudication service"}.get(branch, "engineer"))

    def block(title, why, rows, empty, cta=None, hot=False):
        if not rows:
            inner = f"<div class='empty'><h2>{_e(empty)}</h2></div>"
        else:
            inner = "<div class='reg'>" + "".join(
                f"""
  <div class='r {r.get('tone', '')}'>
    <div class='mark'></div>
    <div class='pid'>{_e(r['tag'])}</div>
    <div>{f"<a class='rec' href='{_e(r['url'])}'>" if r.get('url') else ""}
      <p class='hold'>{_e(r['what'])}</p>
      <div class='meta'>{_e(r['detail'])}</div>
      {"</a>" if r.get('url') else ""}</div>
    <div class='st'>{_e(r.get('note', ''))}</div>
    <div class='when'>{_e(r.get('when', ''))}</div>
  </div>""" for r in rows) + "</div>"
        action = ""
        if cta:
            action = (f"<div class='actions'><a class='btn2 ghost'"
                      f" href='{cta[1]}'>{_e(cta[0])}</a></div>")
        return (grp(title, len(rows) or None, hot=hot and bool(rows))
                + f"<p class='lede' style='margin:-6px 0 12px'>{_e(why)}</p>"
                + inner + action)

    sections = ""
    if branch == "risk_owner":
        sections += block(
            "Waiting on your signature",
            "Every automatic review is spent on these. Nobody but a named"
            " risk owner can close them, and whoever does puts their name on"
            " a permanent record.",
            items["reviews"], "Nothing is waiting on you",
            ("See every change", "/review/changes"), hot=True)
        sections += block(
            "Risks you allowed that are still live",
            "Each one ends. When it does the question comes back — either as"
            " a fresh decision or as a proposal to change the rule.",
            items["my_waivers"], "You have nothing live")
        sections += block(
            "Ending within 30 days",
            "These run out soon. Once an exception ends it counts for"
            " nothing, and the change it allowed is judged again.",
            items["expiring"], "Nothing ends in the next 30 days")

    elif branch == "lawmakers":
        sections += block(
            "Proposals waiting on you",
            "Nobody else can decide these. Until you do, the rule stands as"
            " written and every change keeps meeting it.",
            items["amendments"], "No proposal is waiting",
            ("See all rule changes", "/review/amendments"), hot=True)
        sections += block(
            "Rules under strain",
            "Rules that keep having to be waived or argued with. A rule that"
            " must be repeatedly waived is usually the problem, not the"
            " changes it blocks.",
            items["friction"], "No rule is showing strain")
        sections += block(
            "Recently decided",
            "What your team has already settled.",
            items["decided"], "You have not decided anything yet")

    else:
        sections += block(
            "Your changes that are blocked",
            "Each of these still has a route open — say the rule does not"
            " apply, or ask a named risk owner to allow it.",
            items["blocked"], "None of your changes is blocked",
            ("See every change", "/review/changes"), hot=True)
        sections += block(
            "Waiting on somebody else",
            "You have taken these as far as you can. A named person has to"
            " decide, and nothing you do will move them.",
            items["waiting"], "Nothing of yours is waiting on a person")
        sections += block(
            "Stopped by a rule that cannot be waived",
            "There is no appeal for these. The only route is proposing a"
            " change to the rule itself.",
            items["floored"], "None of your changes hit one",
            ("See rule changes", "/review/amendments"))

    if is_auditor:
        # Deliberately not a queue: an auditor has nothing to sign. What they
        # have is the things worth looking at first — the decisions nobody can
        # revisit, the exceptions that quietly ran out, and the answers that
        # did not come from the judge at all.
        sections = block(
            "Answers that did not come from the judge",
            "A call failed and the system fell back rather than stopping."
            " Those decisions rest on a weaker basis than the rest, and any"
            " analysis of this ledger should exclude them.",
            items["degraded"], "Every answer came from the judge",
            ("All AI judge activity", "/review/activity/judge"), hot=True)
        sections += block(
            "Exceptions that ran out",
            "Risk that was allowed for a fixed period and then came back on"
            " its own. Elsewhere this is where an exception becomes permanent"
            " because nobody noticed.",
            items["lapsed_recent"], "Nothing has run out yet",
            ("All past rulings", "/review/ledger?status=lapsed"))
        sections += block(
            "Signed and closed for good",
            "A named person signed these and they cannot be reopened — not by"
            " them, not by an administrator, not by anyone.",
            items["decided_final"], "Nothing has been signed at the top",
            ("Everything that happened", "/review/activity"))

    tiles = "".join(
        f"<div><span class='k'>{_e(k)}</span>"
        f"<span class='v{c}'>{v}</span></div>"
        for k, v, c in items['counts'])

    return page("Your work — Digital Judiciary", f"""
<div class='wrap'>
  {masthead(principal, branch, org, scoped=scoped, tenants=tenants,
            here='/review')}
  {nav('/review', simulator=SIMULATOR_ON())}
  <div class='grp' style='margin-top:22px'><h2>Your work</h2>
    <span class='n'>{_e(role)}</span><span class='rule'></span></div>
  <div class='tally'>{tiles}</div>
  {sections}
</div>""")
