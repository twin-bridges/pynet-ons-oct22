import aruba_auth
import requests
from rich import print
from my_aruba import show_command

session = requests.Session()
# host = "10.5.235.12"
host = "aruba.lasthop.io"

uid_aruba = aruba_auth.auth(session, host=host)

command = "show+vlan"
data = show_command(session, host=host, command=command, uid_aruba=uid_aruba)
print(type(data))
print(data)
