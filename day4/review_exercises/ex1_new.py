# Using the "auth" function, connect to the Aruba Controller.

# Retrieve "object/ssid_prof" using a config_path of "/md/40Lab/VH" and using the "get_request" function.

# From the returned data structure extract the "profile-names" and put them into a simple list.

# Use rich.print to print this profile_name_list to the screen.

# Note, remember your process for dealing with complex data structures. You will need to step multiple
# layers into this data structure to extract the field that you require.

from aruba_auth import auth
from my_aruba import get_request
from rich import print
import requests

session = requests.Session()
host = "aruba.lasthop.io"

uid_aruba = auth(session, host=host)


# Retrieve "object/ssid_prof" using a config_path of "/md/40Lab/VH" and using the "get_request" function.
relative_url = "object/ssid_prof"
config_path = "/md/40Lab/VH"
data = get_request(
    session,
    host=host,
    uid_aruba=uid_aruba,
    config_path=config_path,
    relative_url=relative_url,
)

data = data["_data"]["ssid_prof"]
profile_name_list = []
for ele in data:
    entry = [ele["profile-name"], ele["ssid_enable"]]
    profile_name_list.append(entry)

print(profile_name_list)
