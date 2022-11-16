import rich
from getpass import getpass
from aruba_class import ArubaAPI

host = "aruba.lasthop.io"
username = input("Enter your username: ")
password = getpass()
aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()
command = "show+interface+counters"
data = aruba_conn.show_command(command)
aruba_conn.logout()

data = data["_data"]
in_octets = 0
out_octets = 0
for line in data:
    if "Port" in line:
        continue
    if not in_octets:
        intf_name, in_octets, _, _, _ = line.split()
    elif not out_octets:
        intf_name2, out_octets, _, _, _ = line.split()

assert intf_name == intf_name2

print()
print(f"Int: {intf_name}")
print(f"InOctets -> {in_octets}")
print(f"OutOctets -> {out_octets}")
print()
