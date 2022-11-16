from aruba_auth import auth
from my_aruba import get_request, config_change
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

payload = {"syscontact": "Jane Doe, 415.111.1111"}
data = config_change(
    session,
    host=host,
    relative_url=relative_url,
    payload=payload,
    config_path=config_path,
    uid_aruba=uid_aruba,
)
print(data)

relative_url = "object/write_memory"
data = config_change(
    session,
    host=host,
    relative_url=relative_url,
    config_path=config_path,
    uid_aruba=uid_aruba,
)
print(data)
