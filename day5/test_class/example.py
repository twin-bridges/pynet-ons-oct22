import rich
from getpass import getpass
from aruba_class import ArubaAPI

host = "aruba.lasthop.io"
username = input("Enter your username: ")
password = getpass()
aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()
data = aruba_conn.get_request(relative_url="object/ap_group")
rich.print(data)
aruba_conn.logout()
