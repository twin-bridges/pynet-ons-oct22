import requests
import json
import rich
from aruba_auth import auth, get_request_filter


host = "aruba.lasthop.io"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host)

relative_url = "object/vlan_name_id"
config_path = "/md/40Lab/VH"
filter_str = ""

# Initial GET with no filter
response = get_request_filter(
    session,
    host,
    relative_url=relative_url,
    config_path=config_path,
    filter_str=filter_str,
    uid_aruba=uid_aruba,
)
print()
rich.print(response.json())
print()

# Second GET with the filter
filter_str = [{"vlan_name_id.name": {"$in": ["guest"]}}]
response = get_request_filter(
    session,
    host,
    relative_url=relative_url,
    config_path=config_path,
    filter_str=filter_str,
    uid_aruba=uid_aruba,
)
print()
rich.print(response.json())
print()
