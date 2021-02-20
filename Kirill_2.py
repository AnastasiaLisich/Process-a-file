#!/usr/bin/env python3
from collections import defaultdict
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    with open(filename) as f:
        stdin = f.read().split('\n')
else:
    stdin = sys.stdin.read().split('\n')


errs = []
errs_dict = defaultdict(int)

for line in stdin:
    line = line.strip()
    if line == '':
        continue
    else:
        errs.append(line.split(' '))

for err in errs:
    if err[1].endswith(':'):
        curr_err = err[1].strip(':')
        errs_dict[curr_err] += 1
    else:
        errs_dict[err[1]] += 1


for key, value in sorted(errs_dict.items(), key=lambda x: x[1]):
    print(f'{key}\t{value}')
