import json
from rich import print

with open("int_gig.json") as f:
    data = json.load(f)

print()
print(f"Data structure is of type: {type(data)}")
data = data["_data"]["int_gig"]

print()
for ele in data:
    port_name = ele['slot/module/port']
    port_speed = ele["int_gig_speed"]["port_speed"]
    duplex = ele["int_gig_duplex"]["duplex_mode"]
    print(f"Interface GigE {port_name} -> Speed: {port_speed}, Duplex: {duplex}")
print()
