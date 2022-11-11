import requests
import rich
from aruba_auth import auth, get_request

host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host, api_port=api_port)

relative_url = "object/ap_group"
config_path = "/md/40Lab/VH/20:4c:03:39:5a:fc"
response = get_request(
    session,
    host,
    relative_url=relative_url,
    config_path=config_path,
    uid_aruba=uid_aruba,
)

rich.print(response.json())
