#!/usr/bin/env python3
"""Tag every Gumroad href on the built shop pages with UTM params so Gumroad
Analytics > Links shows clicks/sales per page. Idempotent. Run after ANY
regenerate (gen.py, landing.py, en_landing.py) and before committing.
source=site, medium=seo, campaign=<page folder> (home for index.html)."""
import re, pathlib, sys
root = pathlib.Path(__file__).parent
pat = re.compile(r'href="(https://buckylittleshop\.gumroad\.com/[^"?#]*)"')
n = 0
for f in sorted(root.glob('*/index.html')) + [root / 'index.html']:
    camp = 'home' if f.parent == root else f.parent.name
    s = f.read_text(encoding='utf-8')
    new, k = pat.subn(lambda m: f'href="{m.group(1)}?utm_source=site&utm_medium=seo&utm_campaign={camp}"', s)
    if k:
        f.write_text(new, encoding='utf-8'); n += k
        print(f'{camp}: {k}')
print('total tagged', n)
