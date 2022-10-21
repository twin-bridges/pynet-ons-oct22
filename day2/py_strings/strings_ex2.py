from rich import print

with open("aruba_show_ap_database.txt") as aruba_file:
    ap_database = aruba_file.read()

header = True
footer = False
ap_table = {}
for line in ap_database.splitlines():
    # Strip header and footer information
    if header:
        if "Name" in line and "Standby IP" in line:
            header = False
        continue
    elif "---------" in line:
        continue
    elif footer:
        continue

    if "Flags" in line and "Unprovisioned" in line:
        footer = True
        continue

    fields = line.split()
    ap_name = fields[0]
    ap_ip_address = fields[3]
    ap_status = fields[4]

    ap_table[ap_name] = ap_status
    break

print()
print(ap_table)
print()
