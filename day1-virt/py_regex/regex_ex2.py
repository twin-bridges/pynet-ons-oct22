#!/usr/bin/env python
import re
from rich import print

with open("show_mac_multicast.txt") as f:
    output = f.read()

# print(output)
entry = re.split(r"^------.*---------------$", output, flags=re.M)[1]
entry = entry.strip()
pattern = r"^(\d+)\s+([a-f0-9\.]+)\s+(\w+)\s+(.*)$"
match = re.search(pattern, entry, flags=re.M)

# Retrieve all of the matches
fields = []
for i in range(1, 5):
    fields.append(match.group(i))

vlan, mac_address, mac_type, ports = fields
port_list = re.split(r",", ports)

# Construct the final data structure
mac_dict = {mac_address: {"vlan": int(vlan), "type": mac_type, "ports": port_list}}
print()
print(mac_dict)
print()
