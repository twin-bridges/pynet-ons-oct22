from aruba_auth import auth
from my_aruba import get_request
from rich import print
import requests
import json

session = requests.Session()
host = "aruba.lasthop.io"
api_port = "4343"

uid_aruba = auth(session, host=host)
uid_aruba_qs = f"UIDARUBA={uid_aruba}"

config_path = "/md/40Lab/VH/20:4c:03:39:5a:fc"
relative_url = "object/syscontact"
data = get_request(
    session,
    host=host,
    relative_url=relative_url,
    config_path=config_path,
    uid_aruba=uid_aruba,
)
print(data)

# base_url = f"https://{host}:{api_port}/v1/configuration/"
# query_string = f"?config_path={config_path}"
# query_string += f"&{uid_aruba_qs}"
# 
# # Adding the UID_ARUBA query string for compatibility with 8.6.X.X
# full_url = f"{base_url}{relative_url}{query_string}"
# print(full_url)
# 
# payload = {"syscontact": "John Doe, 415.111.1111"}
# data = session.post(full_url, data=json.dumps(payload), verify=False)
# print(data.json())
# 
# relative_url = "object/write_memory"
# full_url = f"{base_url}{relative_url}{query_string}"
# data = session.post(full_url, verify=False)
# print(data.json())
