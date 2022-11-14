import requests
import json
import rich
from aruba_auth import auth, get_request


host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"

uid_aruba = auth(session, host=host, api_port=api_port)
uid_aruba_qs = f"UIDARUBA={uid_aruba}"

# Retrieve current SysContact
relative_url = "object/syscontact"
config_path = "/md/40Lab/VH/20:4c:03:39:5a:fc"

response = get_request(
    session,
    host=host,
    relative_url=relative_url,
    config_path=config_path,
    uid_aruba=uid_aruba,
)

print()
rich.print(response.json())
print()
input("Hit any key to continue.")

base_url = f"https://{host}:{api_port}/v1/configuration/"
relative_url = "object/syscontact"
config_path = "?config_path=/md/40Lab/VH/20:4c:03:39:5a:fc"
url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"
full_url = f"{base_url}{url_and_qs}"

# Delete SysContact using an HTTP POST
cfg_payload = {"syscontact": "Fake Contact", "_action": "delete"}
response = session.post(full_url, data=json.dumps(cfg_payload), verify=False)

print(f"\n{full_url}\n")
rich.print(response.json())
print()

# # Performaing a write memory via the API
# relative_url = "object/write_memory"
# url_and_qs = f"{relative_url}{config_path}&{uid_aruba_qs}"
# full_url = f"{base_url}{url_and_qs}"
# response = session.post(full_url, verify=False)
# print(f"\n{full_url}\n")
# rich.print(response.json())
# print()
