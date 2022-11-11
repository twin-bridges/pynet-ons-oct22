import requests
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
relative_url = "object/hostname"

for mac in ["20:4c:03:39:5a:fc", "20:4c:03:58:70:72"]:
    config_path = f"?config_path=/md/40Lab/VH/{mac}"
    url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"
    full_url = f"{base_url}{url_and_qs}"

    response = session.get(full_url, verify=False)
    print()
    rich.print(response.json())
    print()
