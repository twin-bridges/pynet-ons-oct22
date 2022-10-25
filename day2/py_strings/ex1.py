
# import rich

from rich import print as r_print

f = open("aruba_show_ap_database.txt")
data = f.read()
f.close()

header = True
my_ds = {}
for line in data.splitlines():
    if header:
        if "name" in line.lower() and "standby ip" in line.lower():
            header = False
        continue
    elif "----------" in line:
        continue
    elif "=" in line:
        continue
    elif "Total APs" in line:
        continue
    elif line.strip() == "":
        continue

    fields = line.split()

    ap_name = fields[0]
    ap_ip_address = fields[3]
    ap_status = fields[4]

    my_ds[ap_name] = ap_status

r_print()
r_print(my_ds)
r_print()
