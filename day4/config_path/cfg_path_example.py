import requests
import rich
from aruba_auth import auth


def proc_results(data):
    data = data["_data"]["ap_group"]
    ap_groups = [e["profile-name"] for e in data]
    return ap_groups


host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host, api_port=api_port)
uid_aruba_qs = f"UIDARUBA={uid_aruba}"

# Test a GET operation
base_url = f"https://{host}:{api_port}/v1/configuration/"
relative_url = "object/ap_group"

# Default config_path
config_path = "?config_path=/mm/mynode"
# Adding the UID_ARUBA query string for compatibility with 8.6.X.X
url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"
full_url = f"{base_url}{url_and_qs}"

response = session.get(full_url, verify=False)
ap_groups = proc_results(response.json())
print(f"\nCFG Path: {config_path}")
rich.print(ap_groups)
input("\nHit a key to continue: ")

# Managed Devices(md) config_path
config_path = "?config_path=/md"
url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"
full_url = f"{base_url}{url_and_qs}"
response = session.get(full_url, verify=False)
ap_groups = proc_results(response.json())
print(f"\nCFG Path: {config_path}")
rich.print(ap_groups)
input("\nHit a key to continue: ")

# Fuller config_path
config_path = "?config_path=/md/40Lab"
url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"
full_url = f"{base_url}{url_and_qs}"
response = session.get(full_url, verify=False)
ap_groups = proc_results(response.json())
print(f"\nCFG Path: {config_path}")
rich.print(ap_groups)
input("\nHit a key to continue: ")

# config_path down to device
config_path = "?config_path=/md/40Lab/VH/20:4c:03:39:5a:fc"
url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"
full_url = f"{base_url}{url_and_qs}"
response = session.get(full_url, verify=False)
ap_groups = proc_results(response.json())
print(f"\nCFG Path: {config_path}")
rich.print(ap_groups)
input("\nHit a key to continue: ")
