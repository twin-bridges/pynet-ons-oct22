import json
from rich import print

with open("int_gig.json") as f:
    data = json.load(f)

data = data["_data"]["int_gig"]

print()
for ele in data:
    port_name = ele["slot/module/port"]
    port_speed = ele["int_gig_speed"]["port_speed"]
    duplex = ele["int_gig_duplex"]["duplex_mode"]
    print(f"Port Name: {port_name}")
    print(f"Port Speed: {port_speed}")
    print(f"Duplex: {duplex}")
    print("-" * 10)
    if port_speed != "auto" or duplex != "auto":
        raise ValueError(f"Invalid port speed or duplex detected: {port_name}")

print("Hello")
print()
