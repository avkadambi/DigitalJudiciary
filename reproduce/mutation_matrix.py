import os, subprocess, shutil, sys, json, hashlib, glob
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SUITES=[('run_conformance.py',61),('run_interface_conformance.py',44),('run_extension_conformance.py',53)]
env=dict(os.environ, DJ_JUDGE_MODE='oracle', DJ_DEV_KEYS='1', DJ_GITHUB_ALLOW_UNSIGNED='1',
         PYTHONDONTWRITEBYTECODE='1')
def clear_cache():
    for p in glob.glob(os.path.join(ROOT,'**','__pycache__'), recursive=True):
        shutil.rmtree(p, ignore_errors=True)
def run_suites():
    det=[]; fail=0
    for s,expect in SUITES:
        p=subprocess.run([sys.executable,s],cwd=ROOT,env=env,capture_output=True,text=True,timeout=600)
        lines=[l for l in p.stdout.splitlines() if l.startswith('RESULT')]
        if p.returncode!=0 or not lines:
            fail+=1; det.append('%s:CRASH'%s.replace('run_','').replace('_conformance.py','')); continue
        got=lines[0].split(':')[1].split('/')[0].strip()
        det.append('%s:%s/%d'%(s.replace('run_','').replace('_conformance.py',''),got,expect))
        if int(got)!=expect: fail+=1
    return fail,det
MUT=[
 ('M1','kill','app/adjudicate.py','        top = max(authority_rank(r["authority_tier"]) for r in pool)','        top = min(authority_rank(r["authority_tier"]) for r in pool)','ordering prefers LOWEST authority'),
 ('M2','kill','app/judges.py','        missing = sorted(premise - facts)','        missing = []','gate never distinguishes'),
 ('M3','kill','app/adjudicate.py','        if prov["absolute"]:','        if False and prov["absolute"]:','A6 absolute short-circuit disabled'),
 ('M4','kill','app/kernel.py','        elif a["tier"] < 2:','        elif a["tier"] < 0:','Def.7 depth>=2 admission bar removed'),
 ('M5','kill','app/kernel.py','            " AND lapsed = 0 AND superseded = 0",','            " AND 1=1 AND superseded = 0",','lapse filter removed from retrieval'),
 ('M6','kill','app/adjudicate.py','        if newer["resolved_at"] <= older["resolved_at"]:','        if newer["resolved_at"] >= older["resolved_at"]:','recency key inverted (oldest wins)'),
 ('M7','kill','app/judges.py','            "distinguished": bool(missing),','            "distinguished": not bool(missing),','distinguish verdict inverted'),
 ('M8','kill','app/adjudicate.py','        best = max(scope_closeness(r, case) for r in pool)','        best = min(scope_closeness(r, case) for r in pool)','scope key inverted (widest wins)'),
 # M9 removes the express-supersession condition, restoring the behaviour the
 # build had before Sect. 4.6 required a citation: any newer record displaces
 # any older one, conflicting or not, silently. Caught by CC-18, which probes
 # the case a trace cannot show — the reversal that must not happen.
 ('M9','kill','app/adjudicate.py','        return outcome(newer) == outcome(older) or older["id"] in cited_by(newer)','        return True','express supersession removed (silent reversal restored)'),
 # ---------------------------------------------------------------------
 # Consolidation (Definitions 15, 16; Definition 7 clause (ii)). Four faults
 # and two controls, one per clause that can be silently lost. Each was
 # written against a specific way a build could go wrong and NOT against the
 # check that catches it, which is why M10 and M11 are caught by different
 # checks than the ones their authors expected.
 # ---------------------------------------------------------------------
 # M10: the class pins no store. The artefact still carries a snapshot_hash
 # field and it is still written, but it is computed over nothing, so the
 # store a member was decided against cannot be recovered from the artefact.
 # Every disposition is unchanged and every other check passes: a correct
 # batch and a batch decided against a moving store are observationally
 # identical in the ledger, which is the whole reason CC-19 recomputes
 # instead of reading.
 ('M10','kill','app/consolidate.py','    payload = sorted(r["content_hash"] for r in store_rows)','    payload = []','the class artefact pins no store snapshot'),
 # M11: the signature reads the whole fact set instead of facts INTERSECT F_p.
 # Every OTHER limb of CC-20 still passes under it — the class it forms is
 # internally consistent — and only the completeness limb (g) notices that a
 # unit alike under the provision was dropped.
 ('M11','kill','app/consolidate.py','            tuple(sorted(set(facts) & vocab)))','            tuple(sorted(set(facts))))','signature computed on facts(c) rather than facts(c) INTERSECT F_p'),
 # M12: clause (e) deleted. A second consolidated record is admitted for a
 # signature a live record already covers, and the |Rules|*2^kappa ceiling of
 # Proposition A_cons(ii) stops being a ceiling.
 ('M12','kill','app/consolidate.py','        if sig in covered:                             # clause (e)','        if False and sig in covered:                   # clause (e)','clause (e) removed: the consolidated-admission ceiling stops binding'),
 # M13: the representative is chosen by arrival rather than by the published
 # total order. This is the back door the whole specification is built to
 # keep shut — which unit becomes law decided by something other than a
 # published rule — and CC-22(c) is what shuts it.
 ('M13','kill','app/consolidate.py','        members = sorted(members, key=_rep_key)','        members = list(members)','representative chosen by arrival order, not the published total order'),
 # S4: permute Classify's input. The representative is fixed by the published
 # order, so nothing moves. A control that could not have failed records
 # nothing; this one records that the order really is published.
 ('S4','survive','app/consolidate.py','    for u in docket:','    for u in list(docket)[::-1]:','Classify input order reversed'),
 # S5: raise N0 from 2 to 3. The only class that forms has three members, so
 # nothing moves — and that is a fact about the corpus, recorded rather than
 # assumed, exactly as S2 records a fact about the ordering keys.
 ('S5','survive','app/consolidate.py','DEFAULT_N0 = 2','DEFAULT_N0 = 3','class threshold N0 raised from 2 to 3'),
 ('S1','survive','app/judges.py','        premise = set(candidate["premise"])','        premise = set(list(candidate["premise"]))','true no-op (control)'),
 ('S2','survive','app/adjudicate.py','    keys = [k for k in _os.environ.get("DJ_ORDER", "auth,ts,scope").split(",") if k]','    keys = [k for k in _os.environ.get("DJ_ORDER", "auth,scope,ts").split(",") if k]','scope and ts swapped in the order'),
 ('S3','survive','app/judges.py','        facts = set(case["facts"])','        facts = set(case["facts"]) | set()','true no-op (control 2)'),
]
clear_cache()
b0,d0=run_suites()
print('CLEAN BASELINE: %s  -> %s' % ('PASS' if b0==0 else 'FAIL', '; '.join(d0)))
if b0: sys.exit('baseline not clean, aborting')
res=[]
print()
print('%-4s %-8s %-44s %-9s %s' % ('id','expect','mutation','outcome','suites'))
for mid,exp,f,a,b,note in MUT:
    path=os.path.join(ROOT,f)
    orig=open(path,encoding='utf8').read()
    if orig.count(a)!=1:
        print('%-4s ANCHOR MISS (%d)'%(mid,orig.count(a))); continue
    h0=hashlib.sha256(orig.encode()).hexdigest()
    clear_cache(); open(path,'w',encoding='utf8').write(orig.replace(a,b,1))
    fail,det=run_suites()
    open(path,'w',encoding='utf8').write(orig); clear_cache()
    assert hashlib.sha256(open(path,encoding='utf8').read().encode()).hexdigest()==h0, 'restore failed '+mid
    bb,_=run_suites()
    assert bb==0, 'baseline dirty after '+mid
    outcome='KILLED' if fail else 'survived'
    ok=(outcome=='KILLED')==(exp=='kill')
    res.append((mid,exp,outcome,ok,note,det))
    print('%-4s %-8s %-44s %-9s %s %s'%(mid,exp,note,outcome,'; '.join(det),'' if ok else ' <-- UNEXPECTED'))
print()
kk=sum(1 for r in res if r[1]=='kill' and r[2]=='KILLED'); nk=sum(1 for r in res if r[1]=='kill')
ss=sum(1 for r in res if r[1]=='survive' and r[2]=='survived'); ns=sum(1 for r in res if r[1]=='survive')
print('expected-kill    : %d/%d killed'%(kk,nk))
print('expected-survive : %d/%d survived'%(ss,ns))
os.makedirs(os.environ.get('OUT','/tmp/dj-reproduce'), exist_ok=True)
json.dump([{'id':r[0],'expect':r[1],'outcome':r[2],'as_expected':r[3],'mutation':r[4],'suites':r[5]} for r in res], open(os.path.join(os.environ.get('OUT','/tmp/dj-reproduce'),'mutants2.json'),'w'), indent=1)
