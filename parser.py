#!/usr/bin/env python3

import sys
import time
import json

while True:
    line = sys.stdin.readline().strip()
    f = open('/var/tmp/workfile', 'w')
    f.write(line)
    time.sleep(1)


##
## /var/tmp/workfile gets:

## { "exabgp": "4.0.1", "time": 1560115858.3324125, "host" : "dev1", "pid" : 3224, "ppid" : 2692, "counter": 10, "type": "update", "neighbor": { "address": { "local": "20.0.0.2", "peer": "20.0.0.1" }, "asn": { "local": 65535, "peer": 65535 } , "direction": "receive", "message": { "update": { "withdraw": 
# { "bgp-ls bgp-ls": [ { "ls-nlri-type": 2, "l3-routing-topology": 0, 
# "protocol-id": 2, "local-node-descriptors": { "autonomous-system": 65535, 
#  "router-id": "000010000004" }, "remote-node-descriptors": { "autonomous-system": 
# 65535, "router-id": "000010000002" }, "interface-address": { "interface-address": 
# "10.1.1.5" }, "neighbor-address": { "neighbor-address": "10.1.1.4" } } ] } } } } }
