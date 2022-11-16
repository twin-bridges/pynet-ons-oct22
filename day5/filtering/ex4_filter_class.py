import rich
from getpass import getpass
from my_aruba import ArubaAPI

host = "aruba.lasthop.io"
username = input("Enter your username: ")
password = getpass()
aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()

# Apply the Filter
relative_url = "object/vlan_name_id"
config_path = "/md/40Lab/VH"
my_filter = [{"vlan_name_id.name": {"$in": ["guest"]}}]

data = aruba_conn.get_request(
    relative_url=relative_url, config_path=config_path, filter_obj=my_filter
)
rich.print(data)
aruba_conn.logout()
