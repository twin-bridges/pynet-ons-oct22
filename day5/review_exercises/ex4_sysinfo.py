from rich import print
from getpass import getpass
from my_aruba import ArubaAPI

host = "aruba.lasthop.io"
username = input("Enter your username: ")
password = getpass()
aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()

relative_url = "object/sys_info"
# config_path = "/md/40Lab/VH"

data = aruba_conn.get_request(relative_url=relative_url)
sw_version = data["_global"]["_version"]["_image_version"]
local_data = data["_local"]
pending_cfg = local_data["_pending"]
write_mem_req = pending_cfg["write_mem_reqd"]
last_save_user = pending_cfg["last_save_user"]

print()
print(f"SW Version: {sw_version}")
print(f"Write Mem Reqd: {write_mem_req}")
print(f"Last Save User: {last_save_user}")
print()

aruba_conn.logout()
