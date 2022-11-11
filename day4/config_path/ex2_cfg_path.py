import requests
import rich
from aruba_auth import auth, get_request

host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host, api_port=api_port)

# Test a GET operation
relative_url = "object/hostname"

for mac in ["20:4c:03:39:5a:fc", "20:4c:03:58:70:72"]:
    config_path = f"/md/40Lab/VH/{mac}"
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
