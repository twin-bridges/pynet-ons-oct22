import requests
import rich
from aruba_auth import auth, get_request

host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host, api_port=api_port)

relative_url = "object/ssid_prof"
config_path = "/md/40Lab/VH"
response = get_request(
    session,
    host,
    relative_url=relative_url,
    config_path=config_path,
    uid_aruba=uid_aruba,
)

data = response.json()
ssid_prof_list = data["_data"]["ssid_prof"]

profile_name_list = []
for e in ssid_prof_list:
    profile_name_list.append(e["profile-name"])

rich.print(profile_name_list)
