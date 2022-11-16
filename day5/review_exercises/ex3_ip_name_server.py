# Complete this change by executing "object/write_memory" via the API. Once again, use the
# config_change method in aruba_class.py to accomplish this. Your payload will be empty.

from aruba_class import ArubaAPI
from getpass import getpass

host = "aruba.lasthop.io"
username = input("Enter your username: ")
password = getpass()
aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()

payload = {"address": "8.8.8.8"}
config_path = "/md/40Lab"
response = aruba_conn.config_change(
    relative_url="object/ip_name_server",
    config_path=config_path,
    config_payload=payload,
)
print(response)

response = aruba_conn.config_change(
    relative_url="object/write_memory",
    config_path=config_path,
)
print(response)
