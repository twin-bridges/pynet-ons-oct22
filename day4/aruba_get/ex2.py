# Using the existing "auth" function, connect to the Aruba Controller.

# Construct a "showcommand" to retrieve: "show vlan".

# Use rich.print to print the result to the screen.

# Use the code in "day4/aruba_get/aruba_showcommand.py" as a model for this.

import aruba_auth
import requests
from rich import print

session = requests.Session()
host = "10.5.235.12"
host = "aruba.lasthop.io"
api_port = "4343"

uid_aruba = aruba_auth.auth(session, host=host)
uid_aruba_qs = f"UIDARUBA={uid_aruba}"

base_url = f"https://{host}:{api_port}/v1/configuration/"
command = "show+vlan"
relative_url = f"showcommand?command={command}&{uid_aruba_qs}"
full_url = f"{base_url}{relative_url}"

response = session.get(full_url, verify=False)
data = response.json()

print(type(data))
print(data)
