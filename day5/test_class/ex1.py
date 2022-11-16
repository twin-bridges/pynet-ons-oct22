import rich
from getpass import getpass
from aruba_class import ArubaAPI

host = "aruba.lasthop.io"
username = input("Enter your username: ")
password = getpass()
aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()
# data = aruba_conn.get_request(relative_url="object/hostname", config_path="/md/40Lab/VH/20:4c:03:58:70:72")
# data = aruba_conn.get_request(relative_url="object/hostname")
data = aruba_conn.get_request(relative_url="object/int_gig", config_path="/md/40Lab/VH/20:4c:03:58:70:72")
# rich.print(data)
aruba_conn.logout()

import json
print(json.dumps(data, indent=4))