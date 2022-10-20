from pprint import pprint

with open("show_arp.txt") as f:
    show_arp = f.read()

ip_dict = {}
for line in show_arp.splitlines():
    if "Internet" in line:
        fields = line.split()
        ip_addr = fields[1]
        mac_addr = fields[3]
        ip_dict[ip_addr] = mac_addr

mac_dict = {}
for k, v in ip_dict.items():
    mac_dict[v] = k

pprint(ip_dict)
print()
pprint(mac_dict)
