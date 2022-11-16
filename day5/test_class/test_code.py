from getpass import getpass
from my_aruba import ArubaAPI
from rich import print

host = "aruba.lasthop.io"
# host = "10.5.235.12"
username = input("Enter your username: ")
password = getpass()

aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()
data = aruba_conn.get_request(relative_url="object/hostname", config_path="/md/40Lab/VH/20:4c:03:58:70:72")
aruba_conn.logout()
print(data)
