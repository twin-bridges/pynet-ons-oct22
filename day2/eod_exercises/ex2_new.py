from rich import print

with open("show_vlan.txt") as my_file:
    vlan_data = my_file.read()

my_ds = {}
for line in vlan_data.splitlines():
    if "Name" in line:
        continue
    elif "----------------" in line:
        continue

    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_status = fields[2]
    ports = fields[3:]
    my_ds[vlan_id] = {
        "vlan_name": vlan_name,
        "vlan_status": vlan_status,
        "port": ports,
    }
    # my_ds[vlan_id]["vlan_name"] = vlan_name
    # my_ds[vlan_id]["vlan_status"] = vlan_status
    # my_ds[vlan_id]["ports"] = ports

print(my_ds)


# 3. Create a new dictionary where the key is the vlan_id. 
# The corresponding value should be a dictionary containing the
# following key-value pairs: vlan_name, status, ports. The ports 
# should be a list of ports.


