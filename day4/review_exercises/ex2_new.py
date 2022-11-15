# Using {{ repo }}/day4/aruba_get/aruba_showcommand.py as a model, connect to the Aruba Controller and execute the
# following "showcommand":

# show configuration node-hierarchy

# Parse the data-structure that is returned and extract both the "Config Node" and the "Type" fields.

# For any "Config Node" with a type of "Device", print both the "Config Node" path and the "Type". The output should
# look similar to the following:

# Config Node: /md/40Lab/VH/20:4c:03:39:5a:fc --> Type: Device
# Config Node: /md/40Lab/VH/20:4c:03:58:70:72 --> Type: Device

from aruba_auth import auth
from my_aruba import show_command
from rich import print
import requests

session = requests.Session()
host = "aruba.lasthop.io"

uid_aruba = auth(session, host=host)

command = "show+configuration+node-hierarchy"

data = show_command(session, host=host, command=command, uid_aruba=uid_aruba)
data = data["Configuration node hierarchy"]

print()
for ele in data:
    config_node = ele["Config Node"]
    aruba_type = ele["Type"]
    if aruba_type != "Device":
        print(f"{config_node} -> {aruba_type}")
print()