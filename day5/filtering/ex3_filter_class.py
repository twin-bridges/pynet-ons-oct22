import rich
from getpass import getpass
from my_aruba import ArubaAPI
import json

host = "aruba.lasthop.io"
username = input("Enter your username: ")
password = getpass()
aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()

# Apply the Filter
relative_url = "object/int_gig"
config_path = "/md/40Lab/VH/20:4c:03:39:5a:fc"
my_filter = [{"OBJECT": {"$eq": ["int_gig.slot/module/port"]}}]
my_filter_str = json.dumps(my_filter)
print(type(my_filter_str))

data = aruba_conn.get_request(
    relative_url=relative_url, config_path=config_path, filter_obj=my_filter_str
)
rich.print(data)
aruba_conn.logout()
