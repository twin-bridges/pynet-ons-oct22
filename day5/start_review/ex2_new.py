# Using the ArubaAPI class located in my_aruba.py, connect to the API.

# Use the show_command method to execute command="show+interface+counters".

# For interface GE0/0/0, extract the InOctets and OutOctets and print those values
# to standard output.

from getpass import getpass
from my_aruba import ArubaAPI
from rich import print


host = "aruba.lasthop.io"
username = input("Enter username: ")
password = getpass()

my_conn = ArubaAPI(host=host, username=username, password=password)
my_conn.auth()
command = "show+interface+counters"

data = my_conn.show_command(command)
data = data["_data"]
in_octets = 0
out_octets = 0
for line in data:
    if "Port" in line:
        continue
    if not in_octets:
        intf_name, in_octets, _, _, _ = line.split()
        in_octets = int(in_octets)
    elif not out_octets:
        intf_name2, out_octets, _, _, _ = line.split()
        out_octets = int(out_octets)

assert intf_name != intf_name2

print()
print(f"Interface name: {intf_name}")
print(f"InOctets: {in_octets}")
print(f"OutOctet: {out_octets}")
