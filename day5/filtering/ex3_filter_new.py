from getpass import getpass
from my_aruba import ArubaAPI
from rich import print
import json

host = "aruba.lasthop.io"
username = input("Enter username: ")
password = getpass()
aruba_conn = ArubaAPI(host=host, username=username, password=password)

aruba_conn.auth()
print(aruba_conn.uid_aruba)

relative_url = "object/int_gig"
config_path = "/md/40Lab/VH/20:4c:03:39:5a:fc"
filter_obj = [{"OBJECT": {"$eq": ["int_gig.slot/module/port"]}}]
filter_obj_str = json.dumps(filter_obj)

data = aruba_conn.get_request(
    relative_url=relative_url, config_path=config_path, filter_obj=filter_obj_str
)
print(data)
