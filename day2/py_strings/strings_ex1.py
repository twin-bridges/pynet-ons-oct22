
with open("aruba_show_ap_database.txt") as aruba_file:
    ap_database = aruba_file.read()

header = True
footer = False
print()
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
    print(line)
