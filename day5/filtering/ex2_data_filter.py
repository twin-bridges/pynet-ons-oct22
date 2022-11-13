import requests
import json
import rich
from aruba_auth import auth


host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host, api_port=api_port)
uid_aruba_qs = f"UIDARUBA={uid_aruba}"

# Test a GET operation
base_url = f"https://{host}:{api_port}/v1/configuration/"
relative_url = "object/vlan_name_id"

config_path = "?config_path=/md/40Lab/VH"
url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"

# Initial GET with no filter
full_url = f"{base_url}{url_and_qs}"
response = session.get(full_url, verify=False)
print(f"\n{full_url}\n")
rich.print(response.json())
print()

# Apply the Filter
filter_data = [{"vlan_name_id.name": {"$in": ["guest"]}}]
filter_qs = f"filter={json.dumps(filter_data)}"
if filter_qs:
    url_and_qs += f"&{filter_qs}"

# Second GET with the filter
full_url = f"{base_url}{url_and_qs}"
response = session.get(full_url, verify=False)
print(f"\n{full_url}\n")
rich.print(response.json())
print()
