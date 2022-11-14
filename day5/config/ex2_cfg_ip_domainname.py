import requests
import json
import rich
from aruba_auth import auth, config_change


host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host, api_port=api_port)

relative_url = "object/ip_domain_name"
config_path = "/md/40Lab"
cfg_payload = {"name": "lasthop.io"}
response = config_change(
    session,
    host=host,
    relative_url=relative_url,
    config_path=config_path,
    config_payload=cfg_payload,
    uid_aruba=uid_aruba,
)
response_data = response.json()
print()
rich.print(response_data)
print()

change_pending = response_data.get("_global_result", {}).get("_pending", False)
if change_pending:
    # Performaing a write memory via the API
    relative_url = "object/write_memory"
    response = config_change(
        session,
        host=host,
        relative_url=relative_url,
        config_path=config_path,
        # No config_payload
        config_payload="",
        uid_aruba=uid_aruba,
    )

    print()
    print("Executing 'write_memory'")
    rich.print(response.json())
    print()
