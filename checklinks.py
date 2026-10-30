#!/usr/bin/env python3
"""Check Gumroad links on SEO pages WITHOUT sending UTM tags.
Usage: python3 checklinks.py <page-dir-or-html> [...]   (default: every */index.html)
Strips the query string before requesting, so our own checks never create
clicks in Gumroad Analytics > Links. Prints status and the JSON-LD price.
Rule from 2026-10-30 nightly: never curl or open a tagged Gumroad URL; use this.
"""
import glob, re, subprocess, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
args = sys.argv[1:] or sorted(glob.glob('*/index.html')) + ['index.html']
files = []
for a in args:
    files.append(os.path.join(a, 'index.html') if os.path.isdir(a) else a)
seen = {}
bad = 0
for f in files:
    html = open(f, encoding='utf-8').read()
    urls = sorted(set(u.split('?')[0] for u in re.findall(r'https://[a-z0-9.]*gumroad\.com/l/[A-Za-z0-9]+[^"\'\s<]*', html)))
    srcs = sorted(set(re.findall(r'utm_source=([a-z]+)', html)))
    badsrc = [s for s in srcs if s not in ('site', 'fbpage', 'ig', 'fbgroup')]
    print(f'== {f}: {len(urls)} products, utm_source={srcs}' + (f'  BAD SOURCE {badsrc}' if badsrc else ''))
    bad += len(badsrc)
    for u in urls:
        if u not in seen:
            r = subprocess.run(['curl', '-sL', '-w', '\n%{http_code}', u], capture_output=True, text=True)
            body, code = r.stdout.rsplit('\n', 1)
            m = re.search(r'"price":([0-9.]+)', body)
            seen[u] = (code, m.group(1) if m else '?')
        code, price = seen[u]
        if code != '200': bad += 1
        print(f'  {code} ${price} {u}')
print('ALL OK' if bad == 0 else f'{bad} PROBLEM(S)')
sys.exit(1 if bad else 0)
