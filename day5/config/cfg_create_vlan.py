import requests
import json
import rich
from aruba_auth import auth


host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
# Note, this "Content-Type" header was added for the POST
session.headers["Content-Type"] = "application/json"
session.headers["Accept"] = "application/json"

uid_aruba = auth(session, host=host, api_port=api_port)
uid_aruba_qs = f"UIDARUBA={uid_aruba}"

base_url = f"https://{host}:{api_port}/v1/configuration/"
relative_url = "object/vlan_id"

# config_path = "?config_path=/md/40Lab/VH"
config_path = "?config_path=/md"
url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"
full_url = f"{base_url}{url_and_qs}"

# Create VLAN using an HTTP POST
cfg_payload = {"id": 910}
response = session.post(full_url, data=json.dumps(cfg_payload), verify=False)
print(f"\n{full_url}\n")
rich.print(response.json())
print()

# Performaing a write memory via the API
relative_url = "object/write_memory"
url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"
full_url = f"{base_url}{url_and_qs}"
response = session.post(full_url, verify=False)
print(f"\n{full_url}\n")
rich.print(response.json())
print()
