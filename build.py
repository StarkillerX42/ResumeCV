#!/usr/bin/env python3
from pathlib import Path
import subprocess as sub

here = Path(__file__).parent

### Build
for fil in ('dylan_gatlin_resume.tex', 'curriculum_vitae.tex'):
    sub.call(f'lualatex {here / fil}', shell=True)

### Cleanup
ignored = (here / '.gitignore').open('r').readlines()

for ignore in ignored:
    ignore = ignore.strip('\n')    
    if ignore == '':
        continue
    else:
        for fil in here.glob(ignore):
            print(f'Removing {fil}')
            fil.unlink()


