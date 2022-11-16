# Also extract whether a "write memory" is required and the username that last saved
# the config.

# Print these fields out to standard output.

from my_aruba import ArubaAPI
from rich import print
from getpass import getpass

host = "aruba.lasthop.io"
username = input("Enter username: ")
password = getpass()

aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()

relative_url = "object/sys_info"
data = aruba_conn.get_request(relative_url=relative_url)

sw_version = data["_global"]["_version"]["_image_version"]
print(sw_version)

wr_mem_reqd = data["_local"]["_pending"]["write_mem_reqd"]
last_save_user = data["_local"]["_pending"]["last_save_user"]
print(wr_mem_reqd)
print(last_save_user)
