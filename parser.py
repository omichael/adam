#!/usr/bin/env python3

import sys
import time
import json

while True:
    line = sys.stdin.readline().strip()
    f = open('/var/tmp/workfile', 'w')
    f.write(line)
    time.sleep(1)
