import requests
import rich
from aruba_auth import auth, get_request, get_request_filter, logout


host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host, api_port=api_port)

# Retrieve SSID Profiles
relative_url = "object/ssid_prof"
config_path = "/md/40Lab"
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

# Repeat except with an "object" filter
filter_object = [{"OBJECT": {"$eq": ["ssid_prof.profile_name", "ssid_prof.ssid_enable"]}}]
response = get_request_filter(
    session,
    host=host,
    relative_url=relative_url,
    config_path=config_path,
    filter_str=filter_object,
    uid_aruba=uid_aruba,
)
print()
rich.print(response.json())
print()

response = logout(session, host=host, uid_aruba=uid_aruba)
print()
rich.print(response.json())
print()
