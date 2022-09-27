"""This program parses show ip int brief."""
from pprint import pprint

with open("show_ip_int_brief.txt") as f:
    show_ip = f.read()


intf_dict = {}
for line in show_ip.splitlines():
    if "Interface                  IP-Address" in line:
        continue

    fields = line.split()
    intf = fields[0]
    ip_address = fields[1]
    line_status = fields[4]
    line_protocol = fields[5]
    intf_dict[intf] = {
        "ip_address": ip_address,
        "line_status": line_status,
        "line_protocol": line_protocol,
    }

pprint(intf_dict)
