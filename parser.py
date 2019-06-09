#!/usr/bin/env python3

import sys
import time
import json
import re

line = sys.stdin.readline().strip()
f = open('/var/tmp/workfile', 'w')
regexp = re.compile(r'bgp-ls')
if regexp.search(line):
    f.write(line)

