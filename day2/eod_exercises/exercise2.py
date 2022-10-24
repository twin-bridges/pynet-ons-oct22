from rich import print

with open("show_vlan.txt") as f:
    vlan_data = f.read()

vlan_ds = {}
header = True
for line in vlan_data.splitlines():
    if header:
        if "------------" in line:
            header = False
        continue

    # Unpacking (*ports is a bit of a trick)
    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_status = fields[2]
    # Use a list slice here, from index-3 (included) to the end of the fields list
    ports = fields[3:]

    vlan_ds[vlan_id] = {
        "vlan_name": vlan_name,
        "vlan_status": vlan_status,
        "ports": ports,
    }

print()
print(vlan_ds)
print()
