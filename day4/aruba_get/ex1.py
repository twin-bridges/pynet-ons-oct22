# Using the existing "auth" function, connect to the Aruba Controller.

# Construct a query to retrieve: "object/hostname".

# Use rich.print to print the result to the screen.

# Use the code in "day4/aruba_get/aruba_get.py" as a model for this.

from aruba_auth import auth
import requests
import rich

session = requests.Session()
host = "10.5.235.16"
# host = "aruba.lasthop.io"
api_port = "4343"

uid_aruba = auth(session, host=host)
print(uid_aruba)

base_url = f"https://{host}:{api_port}/v1/configuration/"
relative_url = "object/hostname"
uid_aruba_qs = f"UIDARUBA={uid_aruba}"
full_url = f"{base_url}{relative_url}?{uid_aruba_qs}"
print(full_url)

response = session.get(full_url, verify=False)
data = response.json()
rich.print(data)
