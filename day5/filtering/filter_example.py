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
relative_url = "object/int_vlan"

# Object filter
filter_object = [{"OBJECT": {"$eq": ["int_vlan.int_vlan_ip", "int_vlan.int_vlan_mtu"]}}]
filter_qs = f"filter={json.dumps(filter_object)}"

config_path = "?config_path=/md/40Lab/VH/20:4c:03:39:5a:fc"
url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}&{filter_qs}"
full_url = f"{base_url}{url_and_qs}"
response = session.get(full_url, verify=False)

print(f"\nCFG Path: {config_path}\n")
rich.print(response.json())
print(f"\n{full_url}")
